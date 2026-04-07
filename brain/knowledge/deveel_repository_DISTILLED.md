---
id: deveel.repository
type: knowledge
owner: OA_Triage
---
# deveel.repository
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![GitHub release](https://img.shields.io/github/v/release/deveel/deveel.repository)
![GitHub license](https://img.shields.io/github/license/deveel/deveel.repository?color=blue)
 ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/deveel/deveel.repository/ci.yml?logo=github)
 [![codecov](https://codecov.io/gh/deveel/deveel.repository/graph/badge.svg?token=5US7L3C7ES)](https://codecov.io/gh/deveel/deveel.repository) ![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/deveel/deveel.repository) [![Documentation](https://img.shields.io/badge/gitbook-docs?logo=gitbook&label=docs&color=blue)](https://deveel.gitbook.io/repository/)



# Deveel Repository

This project wants to provide a _low-ambitions_ / _low-expectations_ implementation of the (_infamous_) _[Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)_ for .NET to support the development of applications that need to access different data sources, using a common interface, respecting the principles of the _[Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)_ and the _[SOLID](https://en.wikipedia.org/wiki/SOLID)_ principles.

## Libraries

The framework is based on a _kernel_ package, that provides the basic interfaces and abstractions, and a set of _drivers_ that implement the interfaces to access different data sources.

| Package | NuGet |
| ------- | ----- |
| _Deveel.Repository.Core_ | [![NuGet](https://img.shields.io/nuget/v/Deveel.Repository.Core.svg)](https://www.nuget.org/packages/Deveel.Repository.Core/) |
| _Deveel.Repository.InMemory_ | [![NuGet](https://img.shields.io/nuget/v/Deveel.Repository.InMemory.svg)](https://www.nuget.org/packages/Deveel.Repository.InMemory/) |
| _Deveel.Repository.MongoFramework_ | [![NuGet](https://img.shields.io/nuget/v/Deveel.Repository.MongoFramework.svg)](https://www.nuget.org/packages/Deveel.Repository.MongoFramework/) |
| _Deveel.Repository.EntityFramework_ | [![NuGet](https://img.shields.io/nuget/v/Deveel.Repository.EntityFramework.svg)](https://www.nuget.org/packages/Deveel.Repository.EntityFramework/) |
| _Deveel.Repository.DynamicLinq_ | [![NuGet](https://img.shields.io/nuget/v/Deveel.Repository.DynamicLinq.svg)](https://www.nuget.org/packages/Deveel.Repository.DynamicLinq/) |
| _Deveel.Repository.Manager_ | [![NuGet](https://img.shields.io/nuget/v/Deveel.Repository.Manager.svg)](https://www.nuget.org/packages/Deveel.Repository.Manager/) |
| _Deveel.Repository.Manager.DynamicLinq_ | [![NuGet](https://img.shields.io/nuget/v/Deveel.Repository.Manager.DynamicLinq.svg)](https://www.nuget.org/packages/Deveel.Repository.Manager.DynamicLinq/) |
| _Deveel.Repository.Manager.EasyCaching_ | [![NuGet](https://img.shields.io/nuget/v/Deveel.Repository.Manager.EasyCaching.svg)](https://www.nuget.org/packages/Deveel.Repository.Manager.EasyCaching/) |


## Why Deveel Repository?

The _Repository Pattern_ is a well-known pattern in the software development, that is used to abstract the access to a data source, and to provide a common interface to query and manipulate the data.

You can read the [motivations and drivers](docs/motivations.md) that have led to the development of this framework, and decide if it is suited for your needs.

## Documentation and Guides

A brief gruide on how to use the framework is available in the [documentation](docs/index.md) section of the repository, that will be updated regularly with any major release of the framework.

[Read Here](docs/index.md) or at [GitBook](https://deveel.gitbook.io/repository/).

## License

The project is licensed under the terms of the [Apache Public License v2](LICENSE), that allows the use of the code in any project, open-source or commercial, without any restriction.

## Contributing

The project is open to contributions: if you want to contribute to the project, please read the [contributing guidelines](CONTRIBUTING.md) for more information.

```

### File: docs\README.md
```md
# Why Another Repository Pattern Library?

## Drivers and Motivation

The repository pattern is a well-known pattern in the domain-driven design, that allows to abstract of the data access layer from the domain model, providing a clean separation of concerns.

The repository pattern is often used in conjunction with the _unit of work_ pattern, which allows to grouping of a set of operations in a single transaction.

While implementing several projects for my own needs, and while creating some Open-Source projects requiring a certain degree of data persistence, I've found myself implementing the same pattern over and over again, with some minor differences, depending on the data source I was using.

I tried to look for existing solutions that could help me in this task, but I found that most of the existing libraries were either unreliable, either too opinionated or simply not providing the features I was looking for.

Although this pattern is not applicable to all scenarios (for instance in the case of _event-driven_ applications), I found that it is still a good pattern to use in many cases, and I decided to create this library to provide a simple and reliable implementation of the pattern, that can be used in different scenarios.

### Why Not Just Use Entity Framework Core?

A great advantage of the usage of _Entity Framework Core_ is that it provides a set of abstractions that allows one to access different data sources and use the same LINQ syntax to query the data.

Anyway, design-wise the Entity Framework is closer to an ORM than to a repository pattern, and it doesn't provide a way to abstract the data access layer from the domain model.

Furthermore, the project was started to address the need to access different data sources, and not only relational databases (for example, MongoDB, or in-memory data sources).

```

### File: CONTRIBUTING.md
```md
# Contributing to Deveel Repository

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## We Develop with Github
We use github to host code, to track issues and feature requests, as well as accept pull requests.

## GitHub Flow

We use the [Github Flow](https://guides.github.com/introduction/flow/index.html) that basically means that all code changes happen through pull requests. 

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## License of Your Contributions

In short, when you submit code changes, your submissions are understood to be under the same [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) that covers the project. Feel free to contact the maintainers if that's a concern.

## Reporting Bugs

We use GitHub [issues](https://github.com/deveel/deveel.repository/issues) to track public bugs. Report a bug by [opening a new issue](); it's that easy!

### Write bug reports with detail, background, and sample code

[This is an example](http://stackoverflow.com/q/12488905/180626) of a bug report I wrote, and I think it's not a bad model. Here's [another example from Craig Hockenberry](http://www.openradar.me/11905408), an app developer whom I greatly respect.

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can. [My stackoverflow question](http://stackoverflow.com/q/12488905/180626) includes sample code that *anyone* with a base R setup can run to reproduce what I was seeing
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People *love* thorough bug reports. I'm not even kidding.
```

### File: docs\custom-repository.md
```md
# Customize the Repository

In most of the circumstances, the default functions provided by the repository are enough, implementing the CRUD operations, but sometimes you need to add some custom functions to the repository. 

For example, you may want to add a function to get all the users that have a specific role, or you may want to add a function to get all the users that have a specific role and are active: in this case, you can use the query functions provided by implementations of the `IQueryableRepository` or the `IFilterableRepository` interface, when a driver supports them.

## Your Custom Repository

Depending on your desining style, you might want to extend the `IRepository<TEntity>` interface contract, or you might want to extend the specific drivers implementations, for example the `MongoRepository<TEntity>`.

If your intention is to being agnostic from the driver, you should extend the `IRepository<TEntity>` interface, for example:

```csharp
public interface IUserRepository : IRepository<User> {
    Task<IEnumerable<User>> GetUsersByRoleAsync(string role);
}
```

or even more generic:

```csharp
public interface IUserRepository<TUser> : IRepository<TUser> where TUser : class, IUser {
    Task<IEnumerable<User>> GetUsersByRoleAsync(string role);
}
```

## Registering the Custom Repository

Once you have defined your custom repository, you need to register it in the `Startup` class, in the `ConfigureServices` method:

```csharp
public void ConfigureServices(IServiceCollection services) {
    // ...
    services.AddRepository<UserRepository>();
    // ...
}
```

The provided `AddRepository` extension method will register the repository as a scoped service by default, but you can still specify the lifetime you prefer.

The method is smart enough to scan the type specified for its base classes and interfaces that implement the `IRepository<TEntity>` interface, and register them as well.

In fact, once you have invoked the above method, you will have the following services registered:

| Service Type | Description |
| --- | --- |
| `UserRepository` | The concrete implementation of the custom repository you have defined |
| `IUserRepository` | The custom repository contract you have defined |
| `IRepository<User>` | The default repository for the `User` entity |


If your custom `IRepository<TEntity>` implements the `IQueryableRepository<TEntity>` or the `IFilterableRepository<TEntity>` interface, the `AddRepository` method will register the following services as well:

| Service Type | Description |
| --- | --- |
| `IQueryableRepository<User>` | A queryable repository for the `User` entity |
| `IFilterableRepository<User>` | A filterable repository for the `User` entity |
```

### File: docs\index.md
```md
# Getting Started

The _Deveel Repository_ is a framework that provides a set of abstractions and implementations of the [_Repository Pattern_](https://en.wikipedia.org/wiki/Repository\_pattern), to simplify the access to data sources in your application.

Below you will find a quick and generic guide to start using the framework in your application.

To learn about the specific usage of the framework, you can read the following documentation:

| Topic                                                                                 | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [_Using the Entity Framework Core Repository_](repository-implementations/ef-core.md) | Learn how to use the Repository pattern with [Entity Framework Core](https://github.com/dotnet/efcore)                                                                         |
| [_Using the MongoDB Repository_](repository-implementations/mongodb.md)               | Accessing [MongoDB](https://mongodb.com) databases through the Repository pattern                                                                                              |
| [_Using the In-Memory Repository_](repository-implementations/in-memory.md)           | Interface a volatile and in-process storage using a Repository pattern.                                                                                                        |
| [_The Entity Manager_](entity-manager/)                                               | Provide your application with a business layer on top of the Repository for additional functions (_logging_, _validation_, _normalization_, _caching_, _event sourcing_, etc.) |
| [_Extending the Repository_](custom-repository.md)                                    | Learn how to create a custom repository to access your data source, according to your specific data logic                                                                      |
| [_Multi-Tenancy_](multi-tenancy.md)                                                   | Learn how to use the framework in a multi-tenant application                                                                                                                   |

## Installation

The framework is based on a _kernel_ package, that provides the basic interfaces and abstractions, and a set of _drivers_ that implement the interfaces to access different data sources.

When installing any of the libraries of the framework, the _kernel_ package (`Deveel.Repository.Core`) will be installed as a dependency, so you don't need to install it explicitly.

### Requirements

Until the version 1.2.5, the library is built on top of the [_.NET 6.0_](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) and requires a runtime that supports it: ensure that your application is configured to use the latest version of the runtime.

Since that version we have started targetting multiple runtimes of the .NET Framework, and the following table shows the compatibility matrix:

| Version  | .NET Runtime       |
| -------- | ------------------ |
| =< 1.2.2 | .NET 6.0           |
| >= 1.2.5 | .NET 6.0, .NET 7.0 |

### The Kernel Package

All the specific drivers are built on top of the _kernel_ package, that provides the basic interfaces and abstractions to implement the repository pattern.

If you are interested developing a driver for a specific data source, you can use the _kernel_ package as a dependency, and implement the interfaces to access the data source: you will still receive many benefits by using the abstractions provided by the library, simplifying your development and usage.

To install the package, run the following command in the _Package Manager Console_ in your project folder:

```powershell
Install-Package Deveel.Repository.Core
```

or using the _.NET CLI_:

```bash
dotnet add package Deveel.Repository.Core
```

### The Drivers

The library provides a set of drivers to access different data sources, that can be used as a dependency in your project.

| Driver                                                           | Package                             | Description                                                                                                                                                                    |
| ---------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [_In-Memory_](repository-implementations/in-memory.md)           | `Deveel.Repository.InMemory`        | A very simple implementation of the repository pattern that stores the data in-memory.                                                                                         |
| [_MongoDB_](repository-implementations/mongodb.md)               | `Deveel.Repository.MongoFramework`  | An implementation of the repository pattern that stores the data in a MongoDB database (using the [MongoFramework](https://github.com/turnersoftware/mongoframework) library). |
| [_Entity Framework Core_](repository-implementations/ef-core.md) | `Deveel.Repository.EntityFramework` | An implementation of the repository pattern that stores the data in a relational database, using the [Entity Framework Core](https://github.com/dotnet/efcore).                |

## Instrumentation

The library provides a set of common extensions to leverage the [_Dependency Injection_](https://en.wikipedia.org/wiki/Dependency\_injection) pattern, and to simplify the registration of the services in the dependency injection container.

To register a repository in the dependency injection container, and be ready to use it in your application, you can use the `AddRepository<TRepository>` extension method of the `IServiceCollection` interface.

For example, if you want to register the default _in-memory_ repository, you can use the following code:

```csharp
public void ConfigureServices(IServiceCollection services) {
    services.AddRepository<InMemoryRepository<MyEntity>>();
}
```

If you have implemented your own repository, deriving from the `IRepository<TEntity>` interface, or from one of the _drivers-specific_ repositories (eg. `MongoRepository<TEntity>`, `EntityRepository<TEntity>`), or even if you have implemented your own driver, you can register it in the same way:

```csharp
public void ConfigureServices(IServiceCollection services) {
    services.AddRepository<MyCustomRepository>();
}
```

The type of the argument of the method is not the type of the entity, but the type of the repository: the library will use reflection to scan the type itself and find all the generic arguments of the `IRepository<TEntity>` interface, and register the repository in the dependency injection container.

### Consuming the Repository

In fact, after that example call above, you will have the following services available to be injected into your application:

| Service                           | Description                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------ |
| `MyCustomRepository`              | The repository to access the data.                                                               |
| `IRepository<MyEntity>`           | The repository to access the data.                                                               |
| `IMyCustomRepository`             | The abstration that provides custom business logic and implementing the `IRepository<MyEntity>`. |
| `IQueryableRepository<MyEntity>`  | The repository to access the data using the LINQ syntax (if the repository implements it).       |
| `IPageableRepository<MyEntity>`   | The repository to access the data using pagination (if the repository implements it).            |
| `IFilterableRepository<MyEntity>` | The repository to access the data using filters (if the repository implements it).               |

```

### File: docs\multi-tenancy.md
```md
# Multi-Tenancy of Data Sources

Software-as-a-Service (SaaS) applications and Enterprise-level applications often need to segregate data between different _tenants_ of the application, that could be different customers or different departments of the same company.

By default, the _kernel_ library doesn't provides any set of abstractions and implementations to support multi-tenancy in your application, but the single drivers can provide it, accordingly to their specific capabilities.

| Driver | Multi-Tenancy | Notes
| ------ | ------------- |------|
| _In-Memory_ | :x: | |
| _MongoDB_ | :white_check_mark: | |
| _Entity Framework Core_ | :warning: | _Starting from version 1.4, the support was removed, and depdends from Finbuckle MultiTenant for EntityFramework_ |

### The Tenant Context

On a general basis, the tenant context is resolved through the identity of a user of the application, using mechanisms like _claims_ or _roles_ (see at [Finbuckle Multi-Tenant](https://github.com/Finbuckle/Finbuckle.MultiTenant) how this is implemented in ASP.NET Core).

Some scenarios anyway require the access to those segregated information from a _service_ or a _background task_, where the user identity is not available: for this reason the framework provides an abstraction named `IRepositoryProvider<TEntity>` that will be used to resolve the repository to access the data, for the tenant identifier.

To learn more about the usage of the `IRepositoryProvider<TEntity>` interface, you can read the documentation [here](multi-tenancy.md).

## Repository Providers

:warning: _The repository providers are not available anymore starting from the version 1.4 of the Deveel.Repository framework._

The preferred approach of the library is to use the [Finbuckle.MultiTenant](https://www.finbuckle.com/MultiTenant) framework to implement multi-tenant applications, and to use the `ITenantInfo` interface to retrieve the current tenant information: this is obtained by scanning the current HTTP request, and retrieving the tenant information from the request.

In some cases, like in background services, where the identity of the tenant is not available through the user (eg. _machine-to-machine_ communication), it is possible to obtain the repository for a specific tenant by using the `IRepositoryProvider<TEntity>` interface: these are still drivers-specific, and produce instances of the repository for a specific tenant and specific driver.


#### The `IRepositoryProvider<TEntity>` interface

The `IRepositoryProvider<TEntity>` exposes a single method that allows to obtain an instance of `IRepository<TEntity>` for a specific tenant.

```csharp
Task<IRepository<TEntity>> GetRepositoryAsync(string tenantId, CancellationToken cancellationToken = default);
```

Every driver that supports multi-tenancy will implement this interface, and the `IRepository<TEntity>` instance returned will be specific for the tenant identifier passed as parameter.

## Finbuckle.MultiTenant for Entity Framework Core

Starting from version 1.4, the support for multi-tenancy in Entity Framework Core was removed from the kernel library, and it is now provided by the [Finbuckle.MultiTenant](https://www.finbuckle.com/MultiTenant) library.

To enable multi-tenancy in a repository that is based on the Entity Framework Core, you need to install the `Finbuckle.MultiTenant.EntityFrameworkCore` package, and configure the `DbContext` to use the `ITenantInfo` interface to retrieve the tenant information.

To do this, you need to add the `Finbuckle.MultiTenant` services in the `ConfigureServices` method of your `Startup` class:

```csharp
services.AddMultiTenant()
	.WithConfigurationStore()
	.WithRouteStrategy();
```
Then, you can use the `ITenantInfo` interface to retrieve the current tenant information in your `DbContext`:

```csharp
public class MyDbContext : DbContext
{
	private readonly IMultiTenantContext _tenantContext;

	public MyDbContext(DbContextOptions<MyDbContext> options, IMultiTenantContext<DbTenantInfo> tenantContext)
		: base(options)
	{
		_tenantContext = tenantContext;
	}

	protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
	{
		// Configure the DbContext to use the tenant information
		optionsBuilder.UseSql(_tenantContext.Tenant.ConnectionString);
	}

	protected override void OnModelCreating(ModelBuilder modelBuilder)
	{
		// Use _tenantInfo to configure the model for the specific tenant
	}
}
```

This way, the `DbContext` will be configured to use the tenant information from the `ITenantInfo` interface, and you can use it to access the data for the specific tenant.

You can then use the `IRepository<TEntity>` interface to access the data for the specific tenant as you would normally do:

```csharp
var repository = serviceProvider.GetRequiredService<IRepository<MyEntity>>();

var entity = await repository.FindByIdAsync(entityId, cancellationToken);
```

In fact the data segregation is handled by the `DbContext` and the `ITenantInfo` interface, so you don't need to worry about it in your application code.

## Multi-Tenancy in MongoDB

The repository implementation to interface the MongoDB database in the Deveel.Repository library is based on the [MongoFramework](https://github.com/TurnerSoftware/MongoFramework) project, that provides a set of abstractions to handle multi-tenancy in MongoDB.

Unfortunately, some design limitations from the model used by the project made us to add some additional code to handle multi-tenancy in MongoDB, that is not available in the original project.

To use multi-tenancy in MongoDB, you need to install the `Deveel.Repository.MongoFramework` package, and configure it to be used in your application.

To do this, you need to add the `MongoRepository` service in the `ConfigureServices` method of your `Startup` class:

```csharp
services.AddMultiTenant<MongoDbTenantInfo>()
	.WithConfigurationStore()
	.WithRouteStrategy();

services.AddMongoRepository(options =>
{
	// this will instruct the MongoDB driver 
	// to use the tenant information from the
	// current context
	options.UseTenant();
});
```

Then, you can use the `IRepository<TEntity>` interface to access the data for the specific tenant as you would normally do:

```csharp
var repository = serviceProvider.GetRequiredService<IRepository<MyEntity>>();

var entity = await repository.FindByIdAsync(entityId, cancellationToken);
```
```

### File: docs\repository-pattern.md
```md
# The Repository Pattern

The `IRepository<TEntity>` interface is the main interface of the repository pattern, that defines the basic operations to query and manipulate the data.

The interface is defined as:

```csharp
public interface IRepository<TEntity> : where TEntity : class {
    Task AddAsync(TEntity entity, CancellationToken cancellationToken = default);
    Task AddRangeAsync(IEnumerable<TEntity> entities, CancellationToken cancellationToken = default);
    Task<bool> RemoveAsync(TEntity entity, CancellationToken cancellationToken = default);
    Task RemoveRangeAsync(IEnumerable<TEntity> entities, CancellationToken cancellationToken = default);
    Task<bool> UpdateAsync(TEntity entity, CancellationToken cancellationToken = default);
    Task<TEntity?> FindByIdAsync(object key, CancellationToken cancellationToken = default);
}
```

## Querying the Repository

The foundational contract of the repository pattern provides one single method to query the repository, that is the `FindByIdAsync(object)` method: one of the core concepts of a _domain-driven design_ is that entities are associated to a unique identifier, and the repository pattern provides a way to query the repository by the identifier.

Extensions of the repository pattern can provide additional methods to query the repository, using different criteria, and the library provides a set of interfaces that extend the basic repository interface to provide additional querying capabilities.

You can also implement your own methods to query the repository according to the business logic of your application, and the library will provide a set of extension methods to allow you to use the repository in a functional way. See the [documentation](custom-repository.md) for more details on this specific matter.

### The `IQuery` Interface

The library provides an abstraction to define a query to the repository, to filter the items to be returned and sort the result of the query.

You can use a simple query object like the `Query` structure, or you can implement your own query object, as long as it implements the `IQuery` interface.

These are the predefined query objects provided by the library:

| Query | Description |
| ----- | ----------- |
| `Query` | A simple query object that defines a filter and a sorting rule. |
| `PageQuery<TEntity>` | A query object that defines a page query, with a page number, a page size, a filter and a sorting rule. |
| `QueryBuilder<TEntity>` | An object that allows to build a query using a fluent syntax for a specific entity type. |

### The `IQueryFilter` Interface

The `IQueryFilter` interface is a marker interface that defines a filter to apply to a query: it doesn't provide any method, and it's up to the repository implementation to define the actual filter.

The library provides a set of predefined filter types that can be used to query the repository, and that can be used to implement your own filters.

| Filter | Description |
| ------ | ----------- |
| `ExpressionFilter<TEntity>` | A filter that is backed by a lambda expression of type `Expression<Func<TEntity, bool>>`. |
| `CombinedFilter` | A filter that combines two or more filters using a logical AND operator. |
| `QueryFilter.Empty` | A filter that doesn't apply any filter to the query. In fact, applying this filter to a query has no effect> the use of it is for combination purposes or for colascing. |

Implementations of the repository might provide additional types of query filters: for example, the `MongoDbRepository<TEntity>` provides a `MongoFilter` that is backed by a MongoDB filter expression, and a `MongoGeoDistanceFilter`: see the [MongoDB](mongodb-repository.md) for more information on the specifics).

### The `ISort` Interface

The `ISort` interface is a marker interface that defines a sorting rule to apply to a query: it doesn't provide any method, and it's up to the repository implementation to define the actual sorting rule.

The library provides a set of predefined sorting rules that can be used to query the repository, and that can be used to implement your own sorting rules.

| Sort | Description |
| ---- | ----------- |
| `ExpressionSort<TEntity>` | A sorting rule that is backed by a lambda expression of type `Expression<Func<TEntity, object>>`, used to select the member of `TEntity` for sorting by. |
| `CombinedSort` | A sorting rule that combines two or more sorting rules. |
| `FieldSort` | A  rule that sorts by a field name (_Note_: for IQueryable implementation of the Repository, it requires a mapping function to resolve the member). |

### Extensions

To enrich the capabilities of operations that can be performed on the data source, the library provides a set of interfaces that extend the `IRepository<TEntity>` interface.

#### IFilterableRepository

The `IFilterableRepository<TEntity>` interface provides some extensions that allows to query the repository using instances of the `IQueryFilter` contract.

It is up to the repository implementation support or not the concrete types of filters, either by throwing an exception, either by ignoring the filter.

The interface is defined as:

```csharp
public interface IFilterableRepository<TEntity> : IRepository<TEntity> where TEntity : class {
    Task<TEntity?> FindAsync(IQuery query, CancellationToken cancellationToken = default);
    Task<IList<TEntity>> FindAllAsync(IQuery query, CancellationToken cancellationToken = default);
    Task<long> CountAsync(IQueryFilter filter, CancellationToken cancellationToken = default);
    Task<bool> ExistsAsync(IQueryFilter filter, CancellationToken cancellationToken = default);
}
```


#### IQueryableRepository

The `IQueryableRepository<TEntity>` interface allows to query the repository using the LINQ syntax, as defined in the `System.Linq` namespace.

Such provisioning allows a _mutable_ repository (that implements functions for _Adding_, _Removing_ and _Updating_ entities) to be queried using the LINQ syntax, and to be used in a _functional_ way.

The interface is defined as:

```csharp
public interface IQueryableRepository<TEntity> : IRepository<TEntity> where TEntity : class {
    IQueryable<TEntity> AsQueryable();
}
```


#### IPageableRepository

The `IPageableRepository<TEntity>` interface extends the basic repository functions with a function to query the repository using pagination definition.

A page query is defined by a `PageQuery<TEntity>` object, that defines the page number, the page size, and an optional filter to apply to the query, and an optional list of sorting rules to apply to the result.

The interface is defined as:

```csharp
public interface IPageableRepository<TEntity> : IRepository<TEntity> where TEntity : class {
	Task<PageResult<TEntity>> GetPageAsync(PageQuery<TEntity> query, CancellationToken cancellationToken = default);
}
```

The `PageQuery<TEntity>` class encapsulates the definition of a page query, and is defined as follows:

```csharp
public class PageQuery<TEntity> where TEntity : class {
    public PageQuery(int page, int pageSize, Expression<Func<TEntity, bool>> filter = null) {
        Page = page;
        PageSize = pageSize;
	}

    public int Page { get; }
    
    public int PageSize { get; }

    public IQueryFilter Filter { get; set; }
    
    public IList<IResultSort> SortBy { get; set; }
}
```

The result of a paged query is an instance of `PageResult<TEntity>`, that is defined as:

```csharp
public class PageResult<TEntity> where TEntity : class {
    public PageResult(PageQuery<TEntity>, int total, IEnumerable<TEntity> items) {
        // ...
    }

    public PageQuery<TEntity> Query { get; }

    public int TotalItems { get; }

    public IReadOnly<TEntity> Items { get; }
}
```

```

### File: docs\SUMMARY.md
```md
# Table of contents

* [Why Another Repository Pattern Library?](README.md)
* [The Repository Pattern](repository-pattern.md)
* [Getting Started](index.md)
* [Customize the Repository](custom-repository.md)
* [Multi-Tenancy of Data Sources](multi-tenancy.md)
* [User Entities](user-entities.md)
* [Repository Implementations](repository-implementations/README.md)
  * [In-Memory Repositories](repository-implementations/in-memory.md)
  * [Entity Framework Core Repositories](repository-implementations/ef-core.md)
  * [MongoDB Repositories](repository-implementations/mongodb.md)
* [The Entity Manager](entity-manager/README.md)
  * [Caching Entities](entity-manager/caching-entities.md)

```

### File: docs\user-entities.md
```md
# User Entities

The repository pattern library provides a way to define user entities. These are entities that are specific to the user of the application, and that are not shared between different users.

Within the scope of a tenant, there might be several users, and each user might have its own set of entities (eg. configurations, preferences, etc.).

## Defining User Entities

The data model of an entity is free to be defined by the developer, and it can be any class, but to be used as a user entity, it should implement the `IHaveOwner<TKey>` contract.

Anyway, entities that are intended to be user-specific should provide a field that identifies the user that owns the entity.

For instance, a user entity might look like this:

```csharp
public class UserConfiguration : IHaveOwner<string>
{
    public string Id { get; set; }

    public string UserId { get; set; }

    string IHaveOwner<string>.OwnerKey => UserId;

    public string ConfigurationKey { get; set; }

    public string ConfigurationValue { get; set; }
}
```

In this case, the `UserId` field is used to identify the user that owns the configuration, and the `ConfigurationKey` and `ConfigurationValue` fields are used to store the configuration data.

**Note**: _The above example uses the `IHaveOwner<TKey>` explicit implementation to provide the owner key of the entity. If you prefer, you can implement the `IHaveOwner<TKey>` interface directly on the entity class, and provide the `OwnerKey` property as a public property._

## Using User Entities Repository

The Deveel Repository framework provides a way to define a repository for user entities, that is specific to the user that is accessing the data.

The repository for user entities is defined by the `IUserRepository<TEntity, TKey, TOwnerKey>` interface, that extends the `IRepository<TEntity>` interface.

In this specific model, the `TEntity` is the type of the entity, `TKey` is the type of the key of the entity, and `TOwnerKey` is the type of the key of the owner of the entity.

With reference to the previous example, the repository for the `UserConfiguration` entity might look like this:

```csharp
public interface IUserConfigurationRepository : IUserRepository<UserConfiguration, string, string>
{
    Task<UserConfiguration> FindByUserAsync(string userId, string configurationKey, CancellationToken cancellationToken = default);
}
```

In this case, the `IUserConfigurationRepository` interface extends the `IUserRepository<UserConfiguration, string, string>` interface, and provides an additional method to find a configuration by the user and the configuration key.

### Accessing the Current User at Runtime

The `IUserRepository` interface requires the implementation of a `IUserAccessor` service, that provides the current user identifier at runtime.

The `IUserAccessor` service is defined as follows:
```csharp
public interface IUserAccessor<TKey>
{
    TKey? GetUserId();
}
```

The `GetUserId` method should return the identifier of the current user, or `null` if the user is not authenticated.

The `IUserAccessor` service should be registered in the dependency injection container of the application, and it should be provided to the repository implementation.

## Entity Framework Core User Entities Repository

The framework provides a specific implementation of the user entities repository for Entity Framework Core, that allows to store user-specific entities in a relational database.

The `EntityUserRepository<TEntity, TKey, TOwnerKey>` class is the base implementation of the user entities repository for Entity Framework Core, that implements the `IUserRepository<TEntity, TKey, TOwnerKey>` interface.

The logic behind the implementation of the user entities repository is to filter the entities by the owner key, that is provided by the `IUserAccessor` service.
```

