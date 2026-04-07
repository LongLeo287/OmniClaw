---
id: shriek
type: knowledge
owner: OA_Triage
---
# shriek
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# ShriekFx:zap: 
[![](https://img.shields.io/badge/.NET%20Core-2.0.0-brightgreen.svg?style=flat-square)](https://www.microsoft.com/net/download/core) 
[![Build status](https://ci.appveyor.com/api/projects/status/mcwi2kqe0daija6c?svg=true)](https://ci.appveyor.com/project/ElderJames/shriekfx)
[![MyGet Pre Release](https://img.shields.io/myget/shriek-fx/vpre/Shriek.svg?style=flat-square&label=myget)](https://www.myget.org/feed/Packages/shriek-fx)
[![Author](https://img.shields.io/badge/author-ElderJames-brightgreen.svg?style=flat-square)](https://yangshunjie.com)
[![GitHub license](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](https://github.com/ElderJames/ShriekFx/blob/master/LICENSE)  

shriek-fx 是一个基于 **.NET Core 2.0** 开发的简单易用的快速开发框架，遵循领域驱动设计规范约束，并结合CQRS架构提供实现事件驱动、事件回溯、响应式等特性的基础设施。内部调用对用户几乎无感知也无需自己实现，开箱即用。目标是协助小型应用使用DDD的思维去开发，最终让开发者告别对领域驱动设计的复杂认识，并且享受到正真意义的面向对象设计模式来带的美感。

除此之外，还包含为了增强核心框架功能和迎合通用业务系统快速开发需求的众多实用的、面向微服务的拓展组件。

PS. 领域驱动设计是一种软件系统设计方法理论，而本框架则提供了规范约束，是能够让这种设计理论真正落地实现的开发工具套件（SDK）。

本框架参考自《领域驱动设计》原著、《实现领域驱动设计》和ENode。

### 特性：

1. 领域驱动设计（DDD）
2. 命令查询职责分离（CQRS）
3. 事件驱动架构 (EDA)
4. 事件回溯 （ES）
5. 最终一致性 （Eventually Consistent）
6. [契约即服务](https://ehttps://shriek-projects.github.io/shriek-fx) (通过定义的接口自动生成客户端和服务端实现，支持Http和Socket)
7. 框架中每个组件都有基础实现，最简单时只需一个核心类库就能跑起来
8. 遵循端口与适配器模式，框架组件适配多种第三方组件实现，可从单体架构到面向服务架构按需扩展

### 设计规范

1. 尽量使用.NET Standard和官方提供的类库，第三方类库设计成组件利用DI来按需组合。


---

### 文档

- [中文](https://shriek-projects.github.io/shriek-fx)

### 安装Nuget包

目前开发版本已发布到MyGet，从Nuget安装时需要添加MyGet的源地址，或者在解决方案根目录添加`NuGet.config`文件，内容如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
	<add key="Shriek-Fx" value="https://www.myget.org/F/shriek-fx/api/v3/index.json" />
	<add key="Nuget.org" value="https://api.nuget.org/v3/index.json" />
  </packageSources>
</configuration>
```

### 开发环境

1. [Visual Studio 15.3+](https://www.visualstudio.com/zh-hans/thank-you-downloading-visual-studio/?sku=Community&rel=15)
2. [.NET Core SDK 2.0+](https://github.com/dotnet/core/blob/master/release-notes/download-archive.md)

---

### 示例项目

[认证授权系统 ShriekFX.Auth](https://github.com/Shriek-Projects/shriek-auth) 开发中

[内容管理系统 ShriekFX.CMS](https://github.com/Shriek-Projects/shriek-cms) 开发中

其他示例在Samples目录下

### 任务列表（会不断调整）：

- C端
  - [x] 命令总线 CommandBus
  - [x] 事件总线 EventBus
  - [x] 进程内异步队列
  - [x] 内存事件缓存
  - [x] 接口实现自动注册
  - [ ] Actor 响应式架构
  - [ ] Saga 流程管理
  - 事件存储 + 聚合快照（备忘录模式）
	- [x] 内存模式 *(聚合修改后立刻持久化)*
	- [x] EF Core实现
	- NoSQL实现
		- [x] LiteDB
		- [x] Cosmos DB （MongoDB API）
	- [x] InfluxDB (时序数据库)
	- [x] Redis
  - Bus / 消息队列（MQ）
	- [x] RabbitMQ
- Q端 + Real DB ORM
  - [x] EF Core
  - Dapper
    - [x] 接口标注Sql特性动态创建仓储
    - [ ] Linq 扩展
    - [ ] 特性指定事务范围
  - [x] [SmartSql](https://github.com/Ahoo-Wang/SmartSql)扩展（实现Xml Sql模板）
  - [ ] TiDB
  - [ ] 查询基类
- 应用服务层
  - 接口即服务
	- [x] Http / MVC
	- [x] TCP  / RPC
	- [ ] Dotnetty
  - [ ] GraphQL
- UI层
  - [ ] 权限管理
  - [ ] OAuth 2.0
  - [ ] ASP.NET Core 扩展
	- [ ] WebApi JS客户端生成
	- [ ] Swagger
  - [ ] 动态表单
  - [ ] Angular
  - [ ] Vue (Vuetify)
- 定时任务
  - [ ] Hangfire
- 基础设施
  - Aop 拦截器
	- [ ] [AspectCore](https://github.com/dotnetcore/AspectCore-Framework)
  - 跟踪监控
	- [ ] [SkyWalking](https://github.com/OpenSkywalking/skywalking-netcore)
    - [ ] [Butterfly](https://github.com/ButterflyAPM)
  - 日志
	- [ ] NLog
	- [ ] Log4net
	- [ ] Exceptionless
	- [ ] Kafka + ELK
  - [ ] 序列化器
  - [ ] 服务定位器
  - [ ] 加密
  - [ ] 爬虫
- 单元测试
  - [ ] CQRS
  - [ ] ServiceProxy
- 示例 （Samples）
  - [x] 内存事件仓储
  - [x] EFCore事件仓储
  - [x] NoSQL事件仓储
  - [x] InfluxDB事件仓储
  - [x] Redis事件仓储
  - [x] RabbitMQ总线
  - [x] WebApi代理
  - [ ] CQRS 整体示例

```

### File: docs\README.md
```md
# ShriekFx:zap: 
[![](https://img.shields.io/badge/.NET%20Core-2.0.0-brightgreen.svg?style=flat-square)](https://www.microsoft.com/net/download/core) 
[![Build Status](https://travis-ci.org/ElderJames/shriek-fx.svg?branch=master)](https://travis-ci.org/ElderJames/shriek-fx)
[![Build status](https://ci.appveyor.com/api/projects/status/mcwi2kqe0daija6c?svg=true)](https://ci.appveyor.com/project/ElderJames/shriekfx)
[![MyGet Pre Release](https://img.shields.io/myget/shriek-fx/vpre/Shriek.svg?style=flat-square&label=myget)](https://www.myget.org/feed/Packages/shriek-fx)
[![Author](https://img.shields.io/badge/author-ElderJames-brightgreen.svg?style=flat-square)](https://yangshunjie.com)
[![GitHub license](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](https://github.com/ElderJames/ShriekFx/blob/master/LICENSE)  

A ddd-cqrs framework for **.NET Core 2.0**  that would make you shriek! For it's simple,elegant and useful!

一个使用 **.NET Core 2.0** 开发的简单易用的领域驱动设计分层框架（DDD+CQRS），宗旨是让小型应用也能用DDD的思想去开发，使开发者告别对领域驱动设计的复杂认识。

### 特性：

1. 领域驱动设计（DDD）
2. 命令查询职责分离（CQRS）
3. 事件驱动架构 (EDA)
4. 事件回溯 （ES）
5. 最终一致性 （Eventually Consistent）
6. Server/Client 动态代理 (提供接口自动实现客户端和服务端)
7. 框架中每个组件都有基础实现，只需一个核心类库就能跑起来
8. 遵循端口与适配器模式，框架组件适配多种第三方组件实现，从单体到面向服务按需扩展

---

### 安装Nuget包

目前开发版本已发布到MyGet，从Nuget安装时需要添加MyGet的源地址，或者在解决方案根目录添加`NuGet.config`文件，内容如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
	<add key="Shriek-Fx" value="https://www.myget.org/F/shriek-fx/api/v3/index.json" />
	<add key="Nuget.org" value="https://api.nuget.org/v3/index.json" />
  </packageSources>
</configuration>
```

### 开发环境

1. [Visual Studio 15.3](https://www.visualstudio.com/zh-hans/thank-you-downloading-visual-studio/?sku=Community&rel=15)
2. .NET Core 2.0 SDK [ [x64](https://download.microsoft.com/download/0/F/D/0FD852A4-7EA1-4E2A-983A-0484AC19B92C/dotnet-sdk-2.0.0-win-x64.exe) | [x86](https://download.microsoft.com/download/0/F/D/0FD852A4-7EA1-4E2A-983A-0484AC19B92C/dotnet-sdk-2.0.0-win-x86.exe) ]

---

### 任务列表（更新中）：

- C端
  - [x] 命令总线 CommandBus
  - [x] 事件总线 EventBus
  - [x] 进程内异步队列
  - [x] 内存事件缓存
  - [x] 接口实现自动注册
  - 事件存储 + 聚合快照（备忘录模式）
	- [x] 内存模式 *(聚合修改后立刻持久化)*
	- [x] EF Core实现
	- NoSQL实现
		- [x] LiteDB
		- [x] Cosmos DB （MongoDB API）
	- [x] InfluxDB (时序数据库)
	- [x] Redis
  - Bus / 消息队列（MQ）
	- [x] RabbitMQ
	- [ ] Orleans
  - [ ] Actor
  - [ ] Saga
- Q端 + Real DB 
  - [x] EF Core
  - [ ] Dapper
  - [ ] 查询基类
- 应用服务层
  - WebApi 接口动态代理
	- [x] Http / MVC
	- [ ] TCP  / RPC (DotNetty)
  - [ ] GraphSQL
- UI层
  - [ ] 权限管理
  - [ ] OAuth 2.0
  - [ ] MVC Razor Helpers
  - [ ] Angular
- 定时任务
  - [ ] Hangfire
- 基础设施
  - 日志
	- [ ] NLog
	- [ ] Log4net
	- [ ] Exceptionless
  - [ ] 序列化器
  - [ ] 服务定位器
  - [ ] 加密
  - [ ] 爬虫
- 示例 （Samples）
  - [x] 内存事件仓储
  - [x] EFCore事件仓储
  - [x] NoSQL事件仓储
  - [x] InfluxDB事件仓储
  - [x] Redis事件仓储 
  - [x] RabbitMQ总线
  - [x] WebApi代理
  - [ ] CQRS 整体示例

```

### File: docs\index.html
```html
﻿<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>ShriekFx⚡</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="description" content="Description">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <link rel="stylesheet" href="//unpkg.com/docsify/lib/themes/vue.css">
</head>

<body>
    <div id="app"></div>
    <script>
        window.$docsify = {
            name: 'ShriekFx⚡',
            repo: 'https://github.com/ElderJames/shriek-fx',
            loadSidebar: true,
            subMaxLevel: 2
        }
    </script>
    <script src="//unpkg.com/docsify/lib/docsify.min.js"></script>
</body>
</html>
```

### File: docs\_sidebar.md
```md
- 入门
    - [快速开始](zh-cn/quickstart)

<!-- - 框架规约
    - [基本概念](zh-cn/base) -->

- [契约即服务](zh-cn/service-intro)
    - [基础使用](zh-cn/service-simple)
```

### File: docs\zh-cn\quickstart.md
```md
# 快速开始 

## 环境准备

1. .NET Core SDK 2.0
2. Visual Studio 2017 15.3+ 或者 Visual Studio Code

## 引入Myget源

目前开发版本已发布到MyGet，从Nuget安装时需要添加MyGet的源地址，或者在解决方案根目录添加`NuGet.config`文件，内容如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
	<add key="Shriek-Fx" value="https://www.myget.org/F/shriek-fx/api/v3/index.json" />
	<add key="Nuget.org" value="https://api.nuget.org/v3/index.json" />
  </packageSources>
</configuration>
```


```

### File: docs\zh-cn\service-intro.md
```md
# 契约即服务

契约即服务是指只需定义接口，通过简单的配置，即可把接口的实现类和对其的调用从应用内调用解耦成服务间调用，摇身一变成为面向服务架构(SOA)，目前支持 HTTP 和 TCP 服务。

**适合场景**

1. 服务间调用是面向服务架构、微服务应用中不可或缺的基础部分，本功能可以通过简单配置释放对接接口的重复劳动。
2. 希望把旧项目逐步迁移到.NTE Core，可保留后台使用.NET 4.6，前台使用 ASP.NET Core，两者使用 Shirek 的契约即服务功能实现快速对接。
3. 也可以只是希望便捷（无感知）地创建一个网络服务或者对接第三方 API。

```

### File: docs\zh-cn\service-simple.md
```md
# 基础使用

## 定义契约

服务契约最简单可以是一个普通接口类型，通过简单配置，shriek-fx 即可以把它的实现类变成服务端和可调用此服务的客户端，当然，二者可以单独使用。

```csharp
public interface ISimpleInterface
{
    Task<string> Test(string sth);
}
```

## 服务设置

首先，实现这个接口定义一个类，这个类只是简单的类：

```csharp
public class SimpleInterface : ISimpleInterface
{
    public async Task<string> Test(string sth)
    {
        return await Task.FromResult("server: " + sth);
    }
}
```

接下来，我们要把这个实现类设置成一个网络服务，只需要简单地在`Startup.cs`文件中的`ConfigureServices`方法中使用注册方法。

1. HTTP 服务的配置

   ```csharp
   //Startup.cs

   public void ConfigureServices(IServiceCollection services)
   {
       //HTTP 配置
       services.AddMvc().AddWebApiProxyServer(opt =>
       {
           opt.AddService<ISimpleInterface>();
       });
   }
   ```

   此时，已经自动配置了一个可以用 POST 方式调用的 WebApi，接受一个字符串参数，路由是用接口名+方法名+参数名生成的。

   > HTTP 服务设置需要安装`Shriek.ServiceProxy.Http.Server`类库。另外还需要以下 ASP.NET Core 基础类库:
   >
   > * Microsoft.AspNetCore.Hosting.Server.Abstractions
   > * Microsoft.AspNetCore.Hosting
   > * Microsoft.AspNetCore.Server.Kestrel
   > * Microsoft.Extensions.DependencyInjection

2. TCP 服务的配置

   ```csharp
   //Startup.cs

   public void ConfigureServices(IServiceCollection services)
   {
       //TCP 配置
       services.AddSocketServer(opt =>
       {
           opt.EndPoint = new IPEndPoint(IPAddress.Loopback, 1212);
           opt.AddService<ISimpleInterface>();
       });
   }
   ```

   此时，已经配置好了一个监听 1212 端口的 TCP 服务端，可以通过配套客户端来调用服务端的特定方法。

   > TCP 服务设置需要安装`Shriek.ServiceProxy.Socket.Server`类库

## 服务调用

只需要在需要调用服务端简单地在`IServiceCollection`中注册我们的客户端组件。

### 注册组件

1. 注册 HTTP 客户端组件

   ```csharp
   var services = new ServiceCollection();

   services.AddWebApiProxy(opt =>
   {
        option.ProxyHost = "http://localhost:5000";
        opt.AddService<ISimpleInterface>();
   });
   ```

   > 服务调用需要安装`Shriek.ServiceProxy.Http`类库

2. 注册 TCP 客户端组件

   ```csharp
   var services = new ServiceCollection();

   services.AddSocketProxy(options =>
   {
        options.ProxyHost = "localhost:1212";//对应服务端的ip和端口号
        options.AddService<ISimpleInterface>();
   });
   ```

   > 服务调用需要安装`Shriek.ServiceProxy.Socket`类库

### 调用方法

调用时可以直接从`IServiceProvider`获取实例，并且直接调用。

```csharp
var provider = services.BuildServiceProvider();
var simpleService = provider.GetService<ISimpleInterface>();
var result = await simpleService.Test("hello word!"); // -->result = "server: hello word!"
```

### 注意

当在 ASP.NET Core 中使用时，则需在`Startup.cs`类中的`ConfigureServices`方法中通过`IServiceCollection`注册客户端组建，即可在控制器（或者其他在控制器注入的组件中）注入客户端了。

```csharp
//Startup.cs

public void ConfigureServices(IServiceCollection services)
{
    services.AddWebApiProxy(opt =>
    {
        option.ProxyHost = "http://localhost:5000";
        opt.AddService<ISimpleInterface>();
    });

    services.AddSocketProxy(options =>
    {
        options.ProxyHost = "localhost:1212";//对应服务端的ip和端口号
        options.AddService<ISimpleInterface>();
    });
}
```

初学者可能会感觉奇怪，“我没注册接口实例呀，怎么就能注入一个实例呢？”其实，这个实例是 AOP 动态代理出来的，会给接口方法绑定一个 HttpClient 的封装。这个特性还会有更多高级用法，如拦截器、路由配置等等，请看下一章节！

```

