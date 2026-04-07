---
id: TodoMVC-DDD-CQRS-EventSourcing
type: knowledge
owner: OA_Triage
---
# TodoMVC-DDD-CQRS-EventSourcing
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Instructions

**Start**

```
docker compose build
docker compose up
```

# Source Code!

Being this project has such a small domain context there are only a couple source files which contain real logic.  Other files are helpers, extensions, or setup.  

### Important backend files:

* [Domain Command Handler](src/Domain/Todo/Handler.cs)
* [Domain Todo Aggregate](src/Domain/Todo/Todo.cs)
* [Read Model Projector](src/Application/Todo/Handler.cs)
* [Web Request Handler](src/Web/Controllers/TodoController.cs)
* [Domain Handler Tests](src/Test/DomainHandler.cs)
* [Event Handler Tests](src/Test/EventHandler.cs)

Web frontend from [TodoMVC-React](https://github.com/blacksonic/todomvc-react)

### What is EventSourcing?

EventSourcing is a process of representing domain objects (Orders, Invoices, Accounts, etc) as a series of separate events.

Your application ends up being 1 long audit log which records every state-changing event that occurs.  The advantage of this approach is other processes can read this event log and generate models that contain only the information the process cares about.  There is also additional information available that other services perhaps don't record themselves.

Imagine a shoppign cart which fills with items to buy.  The warehouse only cares about the final order of the stuff the customer actually agreed to purchase -

<img src="img/eventsourcing.png" height="400px">

but the marketing team might care more about the items the customer removed from their cart **without** buying.  

Using eventsourcing correctly you can generate models which contain both sets of information to satisfy both departments with only 1 set of data.

### What is CQRS

CQRS stands for **Command and Query Responsibility Segregation**

<img src="img/cqrs-logical.svg" height="400px">

In a nut shell - commands are everything that want to change the application state.  Queries are anything that want to read application state.  **There is no overlap**

Commands do not return any data other than if they were *Accepted* or *Rejected*. Accepted meaning the change was saved and read models will be updated.  Rejected meaning the command failed validation or was not valid to be run at this time.  (One example would be trying to invoice a sales order which has already been invoiced)

## Architecture Overview

<img src="img/overview.png" height="400px">

## Commands Processing

<img src="img/commands.png" height="400px">

### Good reads

* [Microsoft's CQRS architecture guide](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/cqrs)
* [Microsoft's eventsourcing architecture guide](https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)

### EventStore Management

{host}:2113

### RabbitMq Management

{host}:15672

```

### File: src\Application\Endpoint.cs
```cs
﻿using Aggregates;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using NServiceBus;
using Infrastructure;
using System.Threading.Tasks;
using System;
using System.Threading;

var configurationBuilder = new ConfigurationBuilder();
configurationBuilder.AddEnvironmentVariables("TODOMVC_");

var configuration = configurationBuilder.Build();

var endpointConfiguration = new EndpointConfiguration("Application");

var transport = endpointConfiguration.UseTransport<RabbitMQTransport>();
transport.UseConventionalRoutingTopology(QueueType.Classic);
transport.ConnectionString(GetRabbitConnectionString(configuration));

endpointConfiguration.Pipeline.Register(
            behavior: typeof(IncomingLoggingMessageBehavior),
            description: "Logs incoming messages"
        );
endpointConfiguration.Pipeline.Register(
            behavior: typeof(OutgoingLoggingMessageBehavior),
            description: "Logs outgoing messages"
        );


var host = Host.CreateDefaultBuilder(args)
    .UseConsoleLifetime()
    .AddAggregatesNet(c => c
            .EventStore(es => es.AddClient(GetEventStoreConnectionString(configuration), "Application"))
            .NewtonsoftJson()
            .Application<Application.UnitOfWork>()
            .NServiceBus(endpointConfiguration)
            .SetCommandDestination("Domain"))
    .ConfigureServices((context, services) =>
    {
        services.AddLogging(builder =>
        {
            builder.ClearProviders();
            builder.AddConfiguration(context.Configuration.GetSection("Logging"));
            builder.AddFile(o => o.RootPath = AppContext.BaseDirectory);
        });
    }).Build();


await host.RunAsync();


static string GetRabbitConnectionString(IConfiguration config)
{
    var host = config["RabbitConnection"];
    var user = config["RabbitUserName"];
    var password = config["RabbitPassword"];

    if (string.IsNullOrEmpty(user))
        return $"host={host}";

    return $"host={host};username={user};password={password};";
}
static string GetEventStoreConnectionString(IConfiguration config)
{
    var host = config["EventStoreConnection"];
    var user = config["EventStoreUserName"] ?? "admin";
    var password = config["EventStorePassword"] ?? "changeit";
    return $"esdb://{user}:{password}@{host}?tls=false";
}



```

### File: src\Application\UnitOfWork.cs
```cs
﻿using Aggregates;
using Aggregates.UnitOfWork.Query;
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Application
{
    public class UnitOfWork : Aggregates.UnitOfWork.IApplicationUnitOfWork, Aggregates.UnitOfWork.IBaseUnitOfWork
    {
        private static ConcurrentDictionary<Guid, object> MemoryDB = new ConcurrentDictionary<Guid, object>();

        private enum Operation
        {
            Add,
            Update,
            Remove,
        }
        private ConcurrentBag<(Operation Operation, object document)> _pending = new ConcurrentBag<(Operation Operation, object document)>();

        public dynamic Bag { get; set; }

        public Task Add<T>(Id id, T todo) where T : class
        {
            _pending.Add((Operation.Add, todo));
            return Task.CompletedTask;
        }
        public Task Update<T>(Id id, T todo) where T : class
        {
            _pending.Add((Operation.Update, todo));
            return Task.CompletedTask;
        }

        public Task<T> Get<T>(Id id) where T : class
        {
            if (MemoryDB.TryGetValue(id, out var todo))
                return Task.FromResult((T)todo);
            throw new ArgumentException("Unknown todo");
        }
        public Task<T> TryGet<T>(Id id) where T : class
        {
            if (MemoryDB.TryGetValue(id, out var todo))
                return Task.FromResult((T)todo);
            return Task.FromResult((T)null);
        }

        public Task Delete<T>(Id id) where T : class
        {
            if (MemoryDB.TryGetValue(id, out var todo))
                _pending.Add((Operation.Remove, todo));
            return Task.CompletedTask;
        }

        public Task<IQueryResult<T>> Query<T>(IDefinition query) where T : class
        {
            throw new NotImplementedException();
        }

        public IEnumerable<Example.Todo.Models.TodoResponse> GetAll()
        {
            return MemoryDB.Values.Cast<Example.Todo.Models.TodoResponse>().ToList();
        }

        public Task Begin()
        {
            return Task.CompletedTask;
        }

        public Task End(Exception ex = null)
        {
            if (ex != null)
                return Task.CompletedTask;

            foreach(var todo in _pending)
            {
                var model = (Example.Todo.Models.TodoResponse)todo.document;
                switch (todo.Operation)
                {
                    case Operation.Add:
                        if (!MemoryDB.TryAdd(model.Id, new Example.Todo.Models.TodoResponse
                        {
                            Id = model.Id,
                            Message = model.Message,
                            Active = true
                        }))
                            throw new InvalidOperationException($"Todo {model.Id} already exists");
                        break;
                    case Operation.Update:
                        if (!MemoryDB.TryGetValue(model.Id, out var existing))
                            throw new InvalidOperationException($"Todo {model.Id} doesn't exist");

                        if (!MemoryDB.TryUpdate(model.Id, new Example.Todo.Models.TodoResponse
                        {
                            Id = model.Id,
                            Message = model.Message,
                            Active = model.Active
                        }, existing))
                            throw new InvalidOperationException($"Failed to update {model.Id}");
                        break;
                    case Operation.Remove:
                        if (!MemoryDB.TryRemove(model.Id, out var temp))
                            throw new InvalidOperationException($"Todo {model.Id} doesn't exist");
                        break;
                }
            }

            return Task.CompletedTask;
        }
    }
}

```

### File: src\Domain\Endpoint.cs
```cs
﻿using Aggregates;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using NServiceBus;
using Infrastructure;
using System;

var configurationBuilder = new ConfigurationBuilder();
configurationBuilder.AddEnvironmentVariables("TODOMVC_");

var configuration = configurationBuilder.Build();

var endpointConfiguration = new EndpointConfiguration("Domain");

var transport = endpointConfiguration.UseTransport<RabbitMQTransport>();
transport.UseConventionalRoutingTopology(QueueType.Classic);
transport.ConnectionString(GetRabbitConnectionString(configuration));

endpointConfiguration.Pipeline.Register(
            behavior: typeof(IncomingLoggingMessageBehavior),
            description: "Logs incoming messages"
        );
endpointConfiguration.Pipeline.Register(
            behavior: typeof(OutgoingLoggingMessageBehavior),
            description: "Logs outgoing messages"
        );


var host = Host.CreateDefaultBuilder(args)
    .UseConsoleLifetime()
    .AddAggregatesNet(c => c
        .EventStore(es => es.AddClient(GetEventStoreConnectionString(configuration), "Domain"))
        .Domain()
        .NewtonsoftJson()
        .NServiceBus(endpointConfiguration)
        .SetCommandDestination("Domain"))
    .ConfigureServices((context, services) =>
    {
        services.AddLogging(builder =>
        {
            builder.ClearProviders();
            builder.AddConfiguration(context.Configuration.GetSection("Logging"));
            builder.AddFile(o => o.RootPath = AppContext.BaseDirectory);
        });
    }).Build();

await host.RunAsync();


static string GetRabbitConnectionString(IConfiguration config)
{
    var host = config["RabbitConnection"];
    var user = config["RabbitUserName"];
    var password = config["RabbitPassword"];

    if (string.IsNullOrEmpty(user))
        return $"host={host}";

    return $"host={host};username={user};password={password};";
}

static string GetEventStoreConnectionString(IConfiguration config)
{
    var host = config["EventStoreConnection"];
    var user = config["EventStoreUserName"] ?? "admin";
    var password = config["EventStorePassword"] ?? "changeit";
    return $"esdb://{user}:{password}@{host}?tls=false";
}




```

### File: src\Domain\Mutator.cs
```cs
﻿using Aggregates;
using NServiceBus;
using System.Collections.Generic;
using Aggregates.Contracts;
using Infrastructure.Commands;

namespace Example
{
    public class Mutator : IMutate
    {
        private readonly Aggregates.UnitOfWork.IDomainUnitOfWork _uow;


        public Mutator(Aggregates.UnitOfWork.IDomainUnitOfWork uow)
        {
            _uow = uow;
        }

        public IMutating MutateIncoming(IMutating mutating)
        {

            return mutating;
        }

        public IMutating MutateOutgoing(IMutating mutating)
        {
            // Make sure UserId and Stamp are transfer from message to message
            if (mutating.Message is StampedCommand)
            {
                if (_uow.CurrentMessage is StampedCommand)
                {
                    var command = _uow.CurrentMessage as StampedCommand;
                    ((StampedCommand)mutating.Message).Stamp = command.Stamp;
                }
                if (_uow.CurrentMessage is IStampedEvent)
                {
                    var @event = _uow.CurrentMessage as IStampedEvent;
                    ((StampedCommand)mutating.Message).Stamp = @event.Stamp;
                }
            }
            else if (mutating.Message is IStampedEvent)
            {
                if (_uow.CurrentMessage is StampedCommand)
                {
                    var command = _uow.CurrentMessage as StampedCommand;
                    ((IStampedEvent)mutating.Message).Stamp = command.Stamp;
                }
                if (_uow.CurrentMessage is IStampedEvent)
                {
                    var @event = _uow.CurrentMessage as IStampedEvent;
                    ((IStampedEvent)mutating.Message).Stamp = @event.Stamp;
                }
            }

            return mutating;
        }
    }
}

```

### File: src\Infrastructure\LoggingMessageBehavior.cs
```cs
﻿using Microsoft.Extensions.Logging;
using NServiceBus.Pipeline;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Infrastructure
{
    public class IncomingLoggingMessageBehavior : Behavior<IIncomingLogicalMessageContext>
    {
        private readonly ILogger<IncomingLoggingMessageBehavior> _logger;
        public IncomingLoggingMessageBehavior(ILogger<IncomingLoggingMessageBehavior> logger)
        {
            _logger = logger;
        }

        public override Task Invoke(IIncomingLogicalMessageContext context, Func<Task> next)
        {


            _logger.LogDebug("<{EventId:l}> Received message '{MessageType}'.\n" +
                            "ToString() of the message yields: {MessageBody}\n" +
                            "Message headers:\n{MessageHeaders}", "Incoming",
                            context.Message.MessageType != null ? context.Message.MessageType.AssemblyQualifiedName : "unknown",
                context.Message.Instance,
                string.Join(", ", context.MessageHeaders.Select(h => h.Key + ":" + h.Value).ToArray()));

            return next();
        }

    }
    public class OutgoingLoggingMessageBehavior : Behavior<IOutgoingLogicalMessageContext>
    {
        private readonly ILogger<OutgoingLoggingMessageBehavior> _logger;
        public OutgoingLoggingMessageBehavior(ILogger<OutgoingLoggingMessageBehavior> logger)
        {
            _logger = logger;
        }

        public override Task Invoke(IOutgoingLogicalMessageContext context, Func<Task> next)
        {

            _logger.LogDebug("<{EventId:l}> Sending message '{MessageType}'.\n" +
                            "ToString() of the message yields: {MessageBody}\n" +
                            "Message headers:\n{MessageHeaders}", "Outgoing",
                            context.Message.MessageType != null ? context.Message.MessageType.AssemblyQualifiedName : "unknown",
                context.Message.Instance,
                string.Join(", ", context.Headers.Select(h => h.Key + ":" + h.Value).ToArray()));

            return next();
        }

    }
}

```

### File: src\Test\DomainHandler.cs
```cs
using Aggregates;
using System;
using System.Threading.Tasks;
using Xunit;
using FluentAssertions;

namespace Test
{
    public class DomainHandler : TestSubject<Example.Todo.Domain.Handler>
    {
        [Fact]
        public async Task HandleAddTodo()
        {
            var command = new Example.Todo.Commands.Add
            {
                TodoId = Context.Id(),
                Message = "test"
            };

            await Sut.Handle(command, Context).ConfigureAwait(false);

            Context.UoW
                .Check<Example.Todo.Todo>(Context.Id())
                .Raised<Example.Todo.Events.Added>();
        }
        [Fact]
        public async Task HandleEditTodo()
        {
            Context.UoW.Plan<Example.Todo.Todo>(Context.Id())
                .HasEvent<Example.Todo.Events.Added>(x =>
                {
                    x.TodoId = Context.Id();
                    x.Message = "test";
                });

            var command = new Example.Todo.Commands.Edit
            {
                TodoId = Context.Id(),
                Message = "test2"
            };

            await Sut.Handle(command, Context).ConfigureAwait(false);

            Context.UoW
                .Check<Example.Todo.Todo>(Context.Id())
                .Raised<Example.Todo.Events.Edited>();
        }
        [Fact]
        public async Task EditUnknownTodo()
        {

            var command = new Example.Todo.Commands.Edit
            {
                TodoId = Context.Id(),
                Message = "test2"
            };
            var ex = await Record.ExceptionAsync(() => Sut.Handle(command, Context)).ConfigureAwait(false);
            ex.Should().BeOfType<Aggregates.Exceptions.NotFoundException>();
        }
        [Fact]
        public async Task HandleRemote()
        {
            Context.UoW.Plan<Example.Todo.Todo>(Context.Id())
                .HasEvent<Example.Todo.Events.Added>(x =>
                {
                    x.TodoId = Context.Id();
                    x.Message = "test";
                });

            var command = new Example.Todo.Commands.Remove
            {
                TodoId = Context.Id(),
            };

            await Sut.Handle(command, Context).ConfigureAwait(false);

            Context.UoW
                .Check<Example.Todo.Todo>(Context.Id())
                .Raised<Example.Todo.Events.Removed>();
        }
        [Fact]
        public async Task HandleMarkActive()
        {
            Context.UoW.Plan<Example.Todo.Todo>(Context.Id())
                .HasEvent<Example.Todo.Events.Added>(x =>
                {
                    x.TodoId = Context.Id();
                    x.Message = "test";
                })
                .HasEvent<Example.Todo.Events.MarkedComplete>(x =>
                {
                    x.TodoId = Context.Id();
                });

            var command = new Example.Todo.Commands.MarkActive
            {
                TodoId = Context.Id(),
            };

            await Sut.Handle(command, Context).ConfigureAwait(false);

            Context.UoW
                .Check<Example.Todo.Todo>(Context.Id())
                .Raised<Example.Todo.Events.MarkedActive>();
        }
        [Fact]
        public async Task HandleMarkComplete()
        {
            Context.UoW.Plan<Example.Todo.Todo>(Context.Id())
                .HasEvent<Example.Todo.Events.Added>(x =>
                {
                    x.TodoId = Context.Id();
                    x.Message = "test";
                });

            var command = new Example.Todo.Commands.MarkComplete
            {
                TodoId = Context.Id(),
            };

            await Sut.Handle(command, Context).ConfigureAwait(false);

            Context.UoW
                .Check<Example.Todo.Todo>(Context.Id())
                .Raised<Example.Todo.Events.MarkedComplete>();
        }
        [Fact]
        public async Task MarkActiveWhileActive()
        {
            Context.UoW.Plan<Example.Todo.Todo>(Context.Id())
                .HasEvent<Example.Todo.Events.Added>(x =>
                {
                    x.TodoId = Context.Id();
                    x.Message = "test";
                });

            var command = new Example.Todo.Commands.MarkActive
            {
                TodoId = Context.Id(),
            };

            var ex = await Record.ExceptionAsync(() => Sut.Handle(command, Context)).ConfigureAwait(false);
            ex.Should().BeOfType<BusinessException>();
        }
        [Fact]
        public async Task MarkCompleteWhileComplete()
        {
            Context.UoW.Plan<Example.Todo.Todo>(Context.Id())
                .HasEvent<Example.Todo.Events.Added>(x =>
                {
                    x.TodoId = Context.Id();
                    x.Message = "test";
                })
                .HasEvent<Example.Todo.Events.MarkedComplete>(x =>
                {
                    x.TodoId = Context.Id();
                });

            var command = new Example.Todo.Commands.MarkComplete
            {
                TodoId = Context.Id(),
            };

            var ex = await Record.ExceptionAsync(() => Sut.Handle(command, Context)).ConfigureAwait(false);
            ex.Should().BeOfType<BusinessException>();
        }
    }
}

```

### File: src\Test\EventHandler.cs
```cs
﻿using Aggregates;
using System;
using System.Threading.Tasks;
using Xunit;
using FluentAssertions;

namespace Test
{
    public class EventHandler : TestSubject<Example.Todo.Application.Handler>
    {
        [Fact]
        public async Task CreateTodo()
        {
            var @event = Context.Create<Example.Todo.Events.Added>(x =>
            {
                x.TodoId = Context.Id();
                x.Message = "test";
            });

            await Sut.Handle(@event, Context).ConfigureAwait(false);

            Context.App.Check<Example.Todo.Models.TodoResponse>(Context.Id()).Added();
        }
        [Fact]
        public async Task EditTodo()
        {
            Context.App.Plan<Example.Todo.Models.TodoResponse>(Context.Id()).Exists();

            var @event = Context.Create<Example.Todo.Events.Edited>(x =>
            {
                x.TodoId = Context.Id();
                x.Message = "test2";
            });

            await Sut.Handle(@event, Context).ConfigureAwait(false);

            Context.App.Check<Example.Todo.Models.TodoResponse>(Context.Id()).Updated();
        }
        [Fact]
        public async Task RemoveTodo()
        {
            Context.App.Plan<Example.Todo.Models.TodoResponse>(Context.Id()).Exists();

            var @event = Context.Create<Example.Todo.Events.Removed>(x =>
            {
                x.TodoId = Context.Id();
            });

            await Sut.Handle(@event, Context).ConfigureAwait(false);

            Context.App.Check<Example.Todo.Models.TodoResponse>(Context.Id()).Deleted();
        }
    }
}

```

### File: src\Test\Test.cs
```cs
﻿
using AutoFixture;
using AutoFixture.AutoFakeItEasy;
using FakeItEasy;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Test
{
    public abstract class Test
    {
        protected IFixture Fixture { get; private set; }

        public Test()
        {
            Fixture = new Fixture().Customize(new AutoFakeItEasyCustomization { ConfigureMembers = true });

        }

        protected T Fake<T>() => Fixture.Create<T>();
        protected T[] Many<T>(int count = 3) => Fixture.CreateMany<T>(count).ToArray();
        protected void Inject<T>(T instance) => Fixture.Inject(instance);
    }
}

```

### File: src\Test\TestSubject.cs
```cs
﻿using AutoFixture;
using System;
using System.Collections.Generic;
using System.Text;

namespace Test
{
    public abstract class TestSubject<T> : Test, IDisposable
    {
        private Lazy<T> _lazy;
        protected T Sut => _lazy.Value;
        protected Aggregates.TestableContext Context;

        public TestSubject()
        {
            _lazy = new Lazy<T>(CreateSut);
            Context = new Aggregates.TestableContext();
            Context.Extensions.Set("CommandDestination", "domain");
        }
        public void Dispose()
        {
            if (Sut is IDisposable)
                (Sut as IDisposable).Dispose();
        }

        protected virtual T CreateSut() => Fixture.Create<T>();
    }
}
```

### File: src\Web\appsettings.Development.json
```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.AspNetCore.SpaProxy": "Information",
      "Microsoft.Hosting.Lifetime": "Information"
    }
  }
}

```

### File: src\Web\appsettings.json
```json
{
  "Logging": {
      "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
      }
    },
"AllowedHosts": "*"
}

```

### File: src\Web\Program.cs
```cs
using Aggregates;
using Infrastructure;
using NServiceBus;

var builder = WebApplication.CreateBuilder(args);

builder.Configuration.AddEnvironmentVariables("TODOMVC_");

// Add services to the container.

builder.Services.AddControllersWithViews();

var endpointConfiguration = new EndpointConfiguration("Web");

var transport = endpointConfiguration.UseTransport<RabbitMQTransport>();
transport.UseConventionalRoutingTopology(QueueType.Classic);
transport.ConnectionString(GetRabbitConnectionString(builder.Configuration));

endpointConfiguration.Pipeline.Register(
            behavior: typeof(IncomingLoggingMessageBehavior),
            description: "Logs incoming messages"
        );
endpointConfiguration.Pipeline.Register(
            behavior: typeof(OutgoingLoggingMessageBehavior),
            description: "Logs outgoing messages"
        );

builder.Host
    .AddAggregatesNet(c => c
            .NewtonsoftJson()
            .NServiceBus(endpointConfiguration)
            .SetCommandDestination("Domain"));

var app = builder
    .Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();


app.MapControllerRoute(
    name: "default",
    pattern: "{controller}/{action=Index}/{id?}");

app.MapFallbackToFile("index.html"); ;

app.Run();


static string GetRabbitConnectionString(IConfiguration config)
{
    var host = config["RabbitConnection"];
    var user = config["RabbitUserName"];
    var password = config["RabbitPassword"];

    if (string.IsNullOrEmpty(user))
        return $"host={host}";

    return $"host={host};username={user};password={password};";
}



```

### File: src\Domain\Todo\Handler.cs
```cs
﻿using Aggregates;
using Aggregates.Domain;
using NServiceBus;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Example.Todo.Domain
{
    public class Handler :
        IHandleMessages<Commands.Add>,
        IHandleMessages<Commands.Remove>,
        IHandleMessages<Commands.MarkActive>,
        IHandleMessages<Commands.MarkComplete>
    {
        public async Task Handle(Commands.Add command, IMessageHandlerContext ctx)
        {
            var task = await ctx.For<Todo>().New(command.TodoId).ConfigureAwait(false);
            task.Add(command.Message);
        }
        public async Task Handle(Commands.Edit command, IMessageHandlerContext ctx)
        {
            var task = await ctx.For<Todo>().Get(command.TodoId).ConfigureAwait(false);
            task.Edit(command.Message);
        }
        public async Task Handle(Commands.Remove command, IMessageHandlerContext ctx)
        {
            var task = await ctx.For<Todo>().Get(command.TodoId).ConfigureAwait(false);
            task.Remove();
        }
        public async Task Handle(Commands.MarkActive command, IMessageHandlerContext ctx)
        {
            var task = await ctx.For<Todo>().Get(command.TodoId).ConfigureAwait(false);
            task.MarkActive();
        }
        public async Task Handle(Commands.MarkComplete command, IMessageHandlerContext ctx)
        {
            var task = await ctx.For<Todo>().Get(command.TodoId).ConfigureAwait(false);
            task.MarkComplete();
        }
    }
}

```

### File: src\Domain\Todo\Todo.cs
```cs
﻿using Aggregates;
using System;
using System.Collections.Generic;
using System.Text;

namespace Example.Todo
{
    public class Todo : Aggregates.Entity<Todo, State>
    {
        private Todo() { }

        public void Add(string message)
        {
            Apply<Events.Added>(x =>
            {
                x.TodoId = Id;
                x.Message = message;
            });
        }
        public void Edit(string message)
        {
            Apply<Events.Edited>(x =>
            {
                x.TodoId = Id;
                x.Message = message;
            });
        }
        public void Remove()
        {
            Apply<Events.Removed>(x =>
            {
                x.TodoId = Id;
            });
        }
        public void MarkActive()
        {
            Rule("Not Active", x => x.Active);

            Apply<Events.MarkedActive>(x =>
            {
                x.TodoId = Id;
            });
        }
        public void MarkComplete()
        {
            Rule("Active", x => !x.Active);

            Apply<Events.MarkedComplete>(x =>
            {
                x.TodoId = Id;
            });
        }
    }
}

```

### File: src\Infrastructure\Commands\IStampedEvent.cs
```cs
﻿using Aggregates.Messages;

namespace Infrastructure.Commands
{
    public interface IStampedEvent : IEvent
    {
        long Stamp { get; set; }
    }
}

```

### File: src\Infrastructure\Commands\StampedCommand.cs
```cs
﻿using Aggregates.Messages;

namespace Infrastructure.Commands
{
    public class StampedCommand : ICommand
    {
        public long Stamp { get; set; }
    }
}

```

### File: src\Infrastructure\Extensions\BusExtensions.cs
```cs
﻿using Aggregates;
using Aggregates.Exceptions;
using Aggregates.Messages;
using Infrastructure.Commands;
using Infrastructure.Exceptions;
using Infrastructure.Queries;
using NServiceBus;
using Serilog;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Infrastructure.Extensions
{
    public static class BusExtensions
    {
        private static readonly TimeSpan TenSeconds = TimeSpan.FromSeconds(10);

        private static void CheckResponse(Aggregates.Messages.ICommand command, Aggregates.Messages.IMessage msg)
        {
            if (msg is Reject)
            {
                var reject = (Reject)msg;
                Log.Logger.WarnEvent("Rejection", $"Command was rejected - Message: {reject.Message}");
                throw new RejectedException(command.GetType(), reject.Message);
            }
            if (msg is Error)
            {
                var error = (Error)msg;
                Log.Logger.WarnEvent("Fault", $"Command Fault!\n{error.Message}");
                throw new RejectedException(command.GetType(), $"Command Fault!\n{error.Message}");
            }
        }

        public static Task Result<TResponse>(this IMessageHandlerContext context, TResponse payload, string eTag = "") where TResponse : class
        {
            return context.Reply<Reply>(x =>
            {
                x.ETag = eTag;
                x.Payload = payload;
            });
        }
        public static Task Result<TResponse>(this IMessageHandlerContext context, IEnumerable<TResponse> records, long total, long elapsedMs) where TResponse : class
        {
            return context.Reply<PagedReply>(x =>
            {
                x.Records = records.ToList();
                x.Total = total;
                x.ElapsedMs = elapsedMs;
            });
        }
        public static Responses.Paged<TResponse> RequestPaged<TResponse>(this Aggregates.Messages.IMessage message) where TResponse : class
        {
            if (message == null || message is Reject)
            {
                var reject = (Reject)message;
                Log.Logger.Warning("Query was rejected - Message: {0}\n", reject?.Message);
                if (reject != null)
                    throw new QueryRejectedException(reject.Message);
                throw new QueryRejectedException();
            }
            if (message is Error)
            {
                var error = (Error)message;
                Log.Logger.Warning("Query raised an error - Message: {0}", error.Message);
                throw new QueryRejectedException(error.Message);
            }

            var package = (PagedReply)message;
            if (package == null)
                throw new QueryRejectedException($"Unexpected response type: {message.GetType().FullName}");

            return new Responses.Paged<TResponse>()
            {
                ElapsedMs = package.ElapsedMs,
                Total = package.Total,
                Records = package.Records.Cast<TResponse>().ToArray()
            };
        }
        public static async Task CommandToDomain<T>(this IMessageSession bus, T message) where T : StampedCommand
        {
            var options = new SendOptions();
            options.SetDestination("Domain");
            options.SetHeader(Aggregates.Defaults.RequestResponse, "1");

            var response = bus.Request<Aggregates.Messages.IMessage>(message, options);

            await Task.WhenAny(
                    Task.Delay(TenSeconds), response)
                .ConfigureAwait(false);

            if (!response.IsCompleted)
                throw new CommandTimeoutException("Command timed out");

            // verify command was accepted
            CheckResponse(message, response.Result);
        }
        public static async Task<Responses.Paged<TResponse>> Request<T, TResponse>(this IMessageSession bus, T message) where T : Paged where TResponse : class
        {
            var options = new SendOptions();
            options.SetDestination("Application");
            options.SetHeader(Aggregates.Defaults.RequestResponse, "1");

            var response = bus.Request<PagedReply>(message, options);

            await Task.WhenAny(
                Task.Delay(TenSeconds), response)
                .ConfigureAwait(false);

            if(!response.IsCompleted)
                throw new CommandTimeoutException("Request timed out");

            return response.Result.RequestPaged<TResponse>();
        }
    }
}

```

### File: src\Infrastructure\Extensions\LoggingExtensions.cs
```cs
﻿using Serilog;
using Serilog.Events;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Infrastructure.Extensions
{
    public static class LoggingExtensions
    {

        public static void LogEvent(this ILogger logger, LogEventLevel level, string eventId, string messageTemplate, params object[] propertyValues)
        {
            var props = new[] { eventId }.Concat(propertyValues).ToArray();
            logger.Write(level, "<{EventId:l}> " + messageTemplate, props);
        }
        public static void LogEvent(this ILogger logger, LogEventLevel level, string eventId, Exception ex, string messageTemplate, params object[] propertyValues)
        {
            var props = new[] { eventId }.Concat(propertyValues).ToArray();
            logger.Write(level, ex, "<{EventId:l}> " + messageTemplate, props);
        }

        public static void DebugEvent(this ILogger logger, string eventId, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Debug, eventId, messageTemplate, propertyValues);
        }
        public static void InfoEvent(this ILogger logger, string eventId, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Information, eventId, messageTemplate, propertyValues);
        }
        public static void WarnEvent(this ILogger logger, string eventId, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Warning, eventId, messageTemplate, propertyValues);
        }
        public static void ErrorEvent(this ILogger logger, string eventId, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Error, eventId, messageTemplate, propertyValues);
        }
        public static void FatalEvent(this ILogger logger, string eventId, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Fatal, eventId, messageTemplate, propertyValues);
        }
        public static void DebugEvent(this ILogger logger, string eventId, Exception ex, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Debug, eventId, ex, messageTemplate, propertyValues);
        }
        public static void InfoEvent(this ILogger logger, string eventId, Exception ex, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Information, eventId, ex, messageTemplate, propertyValues);
        }
        public static void WarnEvent(this ILogger logger, string eventId, Exception ex, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Warning, eventId, ex, messageTemplate, propertyValues);
        }
        public static void ErrorEvent(this ILogger logger, string eventId, Exception ex, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Error, eventId, ex, messageTemplate, propertyValues);
        }
        public static void FatalEvent(this ILogger logger, string eventId, Exception ex, string messageTemplate, params object[] propertyValues)
        {
            logger.LogEvent(LogEventLevel.Fatal, eventId, ex, messageTemplate, propertyValues);
        }



        public static ILogger With(this ILogger logger, string propertyName, object value)
        {
            return logger.ForContext(propertyName, value, destructureObjects: true);
        }
        public static ILogger With<TClass>(this ILogger logger)
        {
            return logger.ForContext<TClass>();
        }
    }
}

```

### File: src\Infrastructure\Extensions\TaskExtensions.cs
```cs
﻿using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Infrastructure.Extensions
{
    public static class TaskExtensions
    {
        // https://blogs.msdn.microsoft.com/pfxteam/2012/03/05/implementing-a-simple-foreachasync-part-2/
        public static Task StartEachAsync<T>(
         this T[] source, int dop, Func<T, Task> body)
        {
            return Task.WhenAll(
                from partition in Partitioner.Create(source, loadBalance: true).GetPartitions(dop)
                select Task.Run(async () =>
                {
                    using (partition)
                        while (partition.MoveNext())
                            await body(partition.Current).ConfigureAwait(false);

                }));
        }

        // http://compiledexperience.com/blog/posts/async-extensions/
        public static Task WhenAllAsync<T>(this IEnumerable<T> values, Func<T, Task> asyncAction)
        {
            return Task.WhenAll(values.Select(asyncAction));
        }

        // http://compiledexperience.com/blog/posts/async-extensions/
        public static Task<TResult[]> SelectAsync<TSource, TResult>(this IEnumerable<TSource> values, Func<TSource, Task<TResult>> asyncSelector)
        {
            return Task.WhenAll(values.Select(asyncSelector));
        }
        public static Task SelectAsync<TSource>(this IEnumerable<TSource> values, Func<TSource, Task> asyncSelector)
        {
            return Task.WhenAll(values.Select(asyncSelector));
        }
        public static async Task WhenAllSync<T>(this IEnumerable<T> values, Func<T, Task> asyncAction)
        {
            foreach (var val in values)
                await asyncAction.Invoke(val).ConfigureAwait(false);
        }
    }
}

```

### File: src\Infrastructure\Queries\IHandleQueries.cs
```cs
﻿using NServiceBus;
using System;
using System.Collections.Generic;
using System.Text;

namespace Infrastructure.Queries
{
    public interface IHandleQueries<TQuery> : IHandleMessages<TQuery> where TQuery : Query
    {
    }
}

```

### File: src\Infrastructure\Queries\Query.cs
```cs
﻿using Aggregates.Messages;

namespace Infrastructure.Queries
{
    public class Query : IMessage
    {
    }
    public class Paged : Query
    {
    }
}

```

### File: src\Infrastructure\Queries\Reply.cs
```cs
﻿using System;
using System.Collections.Generic;
using System.Text;

namespace Infrastructure.Queries
{

    // Used when replying to a query
    public class Reply : Aggregates.Messages.IMessage
    {
        public string ETag { get; set; }

        public object Payload { get; set; }
    }
    public class PagedReply : Aggregates.Messages.IMessage
    {
        public long ElapsedMs { get; set; }

        public long Total { get; set; }

        public IEnumerable<object> Records { get; set; }
    }
}

```

### File: src\Infrastructure\Validation\FluentValidationBehavior.cs
```cs
﻿using Aggregates.Messages;
using FluentValidation;
using Infrastructure.Extensions;
using Microsoft.Extensions.DependencyInjection;
using NServiceBus.Pipeline;
using Serilog;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Infrastructure.Validation
{
    public class FluentValidationBehaviour : Behavior<IIncomingLogicalMessageContext>
    {
        private static readonly object Lock = new object();
        private static readonly HashSet<Type> NotValidated = new HashSet<Type>();

        public override async Task Invoke(IIncomingLogicalMessageContext context, Func<Task> next)
        {
            var messageType = context.Message.MessageType;

            if (!(context.Message.Instance is ICommand) || NotValidated.Contains(messageType))
            {
                await next().ConfigureAwait(false);
                return;
            }

            var validators = GetBaseTypes(messageType).Concat(new[] { messageType })
                .Where(type => typeof(IMessage).IsAssignableFrom(type))
                .Where(type => type != typeof(IMessage))
                .Select(type =>
                {
                    Type genericType = typeof(IValidator<>).MakeGenericType(type);
                    return (IValidator)context.Builder.GetService(genericType);
                })
                .Where(validator => validator != null);

            var validationContext = new ValidationContext<object>(context.Message.Instance);

            var validationResults = await validators
                .SelectAsync(validator => validator.ValidateAsync(validationContext))
                .ConfigureAwait(false);

            if (validationResults == null || !validationResults.Any())
            {
                lock (Lock)
                {
                    // 2 commands of the same type received at the same time.  Just check
                    if (!NotValidated.Contains(context.Message.MessageType))
                        NotValidated.Add(context.Message.MessageType);
                }
                await next().ConfigureAwait(false);
                return;
            }
            if (validationResults.Any(x => !x.IsValid))
            {
                Log.Logger.With<FluentValidationBehaviour>().WarnEvent("Validation", "Message {MessageId} has failed validation\n{@Failures}\n{@Message}", context.MessageId, validationResults.SelectMany(x => x.Errors).Select(x => $"{x.PropertyName}: {x.ErrorMessage}"), context.Message.Instance);
                throw new ValidationException(validationResults.SelectMany(x => x.Errors));
            }
            await next().ConfigureAwait(false);
        }
        public IEnumerable<Type> GetBaseTypes(Type type)
        {
            if (type.BaseType == null) return type.GetInterfaces();

            return Enumerable.Repeat(type.BaseType, 1)
                             .Concat(type.GetInterfaces())
                             .Concat(type.GetInterfaces().SelectMany<Type, Type>(GetBaseTypes))
                             .Concat(GetBaseTypes(type.BaseType));
        }
    }
    public class FluentValidationRegistration : RegisterStep
    {
        public FluentValidationRegistration() : base(
            stepId: "FluentValidation",
            behavior: typeof(FluentValidationBehaviour),
            description: "Runs fluent validation on incoming commands")
        {
            InsertAfter("LocalMessageUnpack");
            InsertAfterIfExists("CommandAcceptor");
        }
    }
}

```

### File: src\Infrastructure\Validation\ValidationException.cs
```cs
﻿using Aggregates;
using FluentValidation.Results;
using System;
using System.Collections.Generic;
using System.Text;

namespace Infrastructure.Validation
{
    public class ValidationException : BusinessException
    {
        public ValidationException(IEnumerable<ValidationFailure> failures)
            : base("Validation Failure")
        {
            Failures = failures;
        }

        public readonly IEnumerable<ValidationFailure> Failures;
    }
}

```

### File: src\Web\Controllers\TodoController.cs
```cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NServiceBus;
using Infrastructure.Responses;
using Infrastructure.Extensions;

namespace Example.Controllers
{
    [ApiController]
    [Route("[controller]/[action]")]
    public class TodoController : ControllerBase
    {

        private readonly ILogger<TodoController> _logger;
        private readonly IMessageSession _session;

        public TodoController(ILogger<TodoController> logger, IMessageSession session)
        {
            _logger = logger;
            _session = session;
        }

        [HttpGet]
        public Task<Paged<Todo.Models.TodoResponse>> All()
        {
            return _session.Request<Todo.Queries.AllTodos, Todo.Models.TodoResponse>(new Todo.Queries.AllTodos
            {
            });
        }
        [HttpGet]
        public Task<Paged<Todo.Models.TodoResponse>> Active()
        {
            return _session.Request<Todo.Queries.ActiveTodos, Todo.Models.TodoResponse>(new Todo.Queries.ActiveTodos
            {
            });
        }
        [HttpGet]
        public Task<Paged<Todo.Models.TodoResponse>> Complete()
        {
            return _session.Request<Todo.Queries.CompleteTodos, Todo.Models.TodoResponse>(new Todo.Queries.CompleteTodos
            {
            });
        }

        [HttpPost]
        public Task Add(DTOs.Todo model)
        {
            return _session.CommandToDomain(new Todo.Commands.Add
            {
                TodoId = model.TodoId,
                Message = model.Message
            });
        }
        [HttpPost]
        public Task Edit(DTOs.Todo model)
        {
            return _session.CommandToDomain(new Todo.Commands.Edit
            {
                TodoId = model.TodoId,
                Message = model.Message
            });
        }
        [HttpDelete]
        public Task Remove(DTOs.Todo model)
        {
            return _session.CommandToDomain(new Todo.Commands.Remove
            {
                TodoId = model.TodoId,
            });
        }
        [HttpPost]
        public Task Complete(DTOs.Todo model)
        {
            return _session.CommandToDomain(new Todo.Commands.MarkComplete
            {
                TodoId = model.TodoId,
            });
        }
        [HttpPost]
        public Task Active(DTOs.Todo model)
        {
            return _session.CommandToDomain(new Todo.Commands.MarkActive
            {
                TodoId = model.TodoId,
            });
        }
    }
}

```

### File: src\Web\Pages\Error.cshtml.cs
```cs
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Diagnostics;

namespace Web.Pages
{
    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public class ErrorModel : PageModel
    {
        private readonly ILogger<ErrorModel> _logger;

        public ErrorModel(ILogger<ErrorModel> logger)
        {
            _logger = logger;
        }

        public string? RequestId { get; set; }

        public bool ShowRequestId => !string.IsNullOrEmpty(RequestId);

        public void OnGet()
        {
            RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier;
        }
    }
}
```

### File: src\Web\Properties\launchSettings.json
```json
{
  "iisSettings": {
    "windowsAuthentication": false,
    "anonymousAuthentication": true,
    "iisExpress": {
      "applicationUrl": "http://localhost:49962",
      "sslPort": 44375
    }
  },
  "profiles": {
    "Web": {
      "commandName": "Project",
      "launchBrowser": true,
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development",
        "ASPNETCORE_HOSTINGSTARTUPASSEMBLIES": "Microsoft.AspNetCore.SpaProxy",
        "TODOMVC_RabbitConnection": "localhost"
      },
      "applicationUrl": "https://localhost:7227;http://localhost:5227"
    },
    "IIS Express": {
      "commandName": "IISExpress",
      "launchBrowser": true,
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development",
        "ASPNETCORE_HOSTINGSTARTUPASSEMBLIES": "Microsoft.AspNetCore.SpaProxy"
      }
    }
  }
}
```

