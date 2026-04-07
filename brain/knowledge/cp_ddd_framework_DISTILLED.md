---
id: cp-ddd-framework
type: knowledge
owner: OA_Triage
---
# cp-ddd-framework
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h1 align="center">DDDplus</h1>

<div align="center">

A lightweight DDD(Domain Driven Design) enhancement framework for forward/reverse business modeling, supporting complex system architecture evolution!

[![CI](https://github.com/funkygao/cp-ddd-framework/workflows/CI/badge.svg?branch=master)](https://github.com/funkygao/cp-ddd-framework/actions?query=branch%3Amaster+workflow%3ACI)
[![Javadoc](https://img.shields.io/badge/javadoc-Reference-blue.svg)](https://funkygao.github.io/cp-ddd-framework/doc/apidocs/)
[![Maven Central](https://img.shields.io/maven-central/v/io.github.dddplus/dddplus.svg?label=Maven%20Central)](https://central.sonatype.com/namespace/io.github.dddplus)
![Requirement](https://img.shields.io/badge/JDK-8+-blue.svg)
[![Coverage Status](https://img.shields.io/codecov/c/github/funkygao/cp-ddd-framework.svg)](https://codecov.io/gh/funkygao/cp-ddd-framework)
[![Mentioned in Awesome DDD](https://awesome.re/mentioned-badge.svg)](https://github.com/heynickc/awesome-ddd#jvm)
[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg)](https://gitter.im/cp-ddd-framework/community)

</div>

<div align="center">

Languages： English | [中文](README.zh-cn.md) | [deepwiki](https://deepwiki.com/funkygao/cp-ddd-framework)
</div>

----

## What is DDDplus?

DDDplus, formerly named cp-ddd-framework(cp means Central Platform：中台), is a lightweight DDD(Domain Driven Design) enhancement framework for forward/reverse business modeling, supporting complex system architecture evolution!

>It captures DDD missing concepts and patches the building block. It empowers building domain model with forward and reverse modeling. It visualizes the complete domain knowledge from code. It connects frontline developers with (architect, product manager, business stakeholder, management team). It makes (analysis, design, design review, implementation, code review, test) a positive feedback closed-loop. It strengthens building extension oriented flexible software solution. It eliminates frequently encountered misunderstanding of DDD via thorough javadoc for each building block with detailed example.

In short, the 3 most essential `plus` are:
1. [patch](/dddplus-spec/src/main/java/io/github/dddplus/model) DDD building blocks for pragmatic forward modeling, clearing obstacles of DDD implementation
2. offer a reverse modeling [DSL](/dddplus-spec/src/main/java/io/github/dddplus/dsl), visualizing complete domain knowledge from code
3. provide [extension point](/dddplus-spec/src/main/java/io/github/dddplus/ext) with multiple routing mechanism, suited for complex business scenarios

## Current status

Used for several complex critical central platform projects in production environment.

## Showcase

[A full demo of DDDplus forward/reverse modeling ->](dddplus-test/src/test/java/ddd/plus/showcase/README.md)

## Quickstart

### Forward modeling

```xml
<dependency>
    <groupId>io.github.dddplus</groupId>
    <artifactId>dddplus-runtime</artifactId>
</dependency>
```

#### Integration with SpringBoot

```java
@SpringBootApplication(scanBasePackages = {"${your base packages}", "io.github.dddplus"})
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class);
    }
}
```

### Reverse Modeling

Please check out the [《step by step guide》](doc/ReverseModelingGuide.md).

```xml
<dependency>
    <groupId>io.github.dddplus</groupId>
    <artifactId>dddplus-spec</artifactId>
</dependency>
```

Annotate your code With [DSL](/dddplus-spec/src/main/java/io/github/dddplus/dsl), DDDplus will parse AST and render domain model in multiple views.

```bash
mvn io.github.dddplus:dddplus-maven-plugin:model \
    -DrootDir=${colon separated source code dirs} \
    -DplantUml=${target business model in svg format} \
    -DtextModel=${target business model in txt format}
```

### Architecture Guard

```bash
mvn io.github.dddplus:dddplus-maven-plugin:enforce \
    -DrootPackage={your pkg} \
    -DrootDir={your src dir}
```

## Known Issues

- reverse modeling assumes unique class names within a code repo

## Contribution

You are welcome to contribute to the project with pull requests on GitHub.

If you find a bug or want to request a feature, please use the [Issue Tracker](https://github.com/funkygao/cp-ddd-framework/issues).

For any question, you can use [Gitter Chat](https://gitter.im/cp-ddd-framework/community) to ask.

## Licensing

DDDplus is licensed under the Apache License, Version 2.0 (the "License"); you may not use this project except in compliance with the License. You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0).

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at funky.gao@gmail.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq

```

### File: README.zh-cn.md
```md
<h1 align="center">DDDplus</h1>

<div align="center">

轻量级DDD正向/逆向业务建模框架，支撑复杂业务系统的架构演化！

[![CI](https://github.com/funkygao/cp-ddd-framework/workflows/CI/badge.svg?branch=master)](https://github.com/funkygao/cp-ddd-framework/actions?query=branch%3Amaster+workflow%3ACI)
[![Javadoc](https://img.shields.io/badge/javadoc-Reference-blue.svg)](https://funkygao.github.io/cp-ddd-framework/doc/apidocs/)
[![Maven Central](https://img.shields.io/maven-central/v/io.github.dddplus/dddplus.svg?label=Maven%20Central)](https://central.sonatype.com/namespace/io.github.dddplus)
![Requirement](https://img.shields.io/badge/JDK-8+-blue.svg)
[![Coverage Status](https://img.shields.io/codecov/c/github/funkygao/cp-ddd-framework.svg)](https://codecov.io/gh/funkygao/cp-ddd-framework)
[![Mentioned in Awesome DDD](https://awesome.re/mentioned-badge.svg)](https://github.com/heynickc/awesome-ddd#jvm)
[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg)](https://gitter.im/cp-ddd-framework/community)

</div>

<div align="center">

Languages： [English](README.md) | 中文 | [deepwiki](https://deepwiki.com/funkygao/cp-ddd-framework)
</div>

----

## DDDplus是什么

软件开发不仅仅是业务交付的生产过程，本质上是系统化的知识工程，大型复杂软件开发的核心难点是如何处理隐藏在业务知识中的核心复杂度，除了清晰地理解业务诉求之外，还需要通过建模的方式对这种复杂度进行简化与精炼。

作为软件交付最终产品的代码，由于具有(可运行，包含完全细节，演进过程完整追溯，自我修复)特点而成为业务的唯一事实真相，但代码如何以易于理解的形式直观反映业务知识一直是业界难题。

`DDDplus`扩充了DDD，通过正向的DDD建模，配合基于DSL声明式标注从而让代码自动生成业务模型的逆向建模过程，实现了：代码与模型统一，统一语言，抑制熵增。

>它捕获了DDD里缺失的构造块；它为正向和逆向业务建模赋能；它把代码可视化成完整的业务知识；它连接了(架构师，产品经理，业务方，管理者)；它把(业务分析，设计，设计评审，开发实现，代码评审，测试)成为一个正反馈的闭环；它方便构建面向扩展的灵活平台架构；它纠正了常见的DDD的错误理解。

简单地讲，DDDplus的`plus`最关键核心是：
- [扩充](/dddplus-spec/src/main/java/io/github/dddplus/model)了DDD的building blocks，解决DDD落地难问题
- 逆向建模的[DSL](/dddplus-spec/src/main/java/io/github/dddplus/dsl)，让代码可视化地表达完整业务模型
- 支持多种路由模式的[扩展点机制](/dddplus-spec/src/main/java/io/github/dddplus/ext)，应对复杂业务场景

## 项目现状

应用于多个大型核心复杂项目的生产环境。

## 项目演示

[正向和逆向建模的项目演示 ->](dddplus-test/src/test/java/ddd/plus/showcase/README.zh-cn.md)

## 快速入门

### 正向建模

```xml
<dependency>
    <groupId>io.github.dddplus</groupId>
    <artifactId>dddplus-runtime</artifactId>
</dependency>
```

#### 与SpringBoot集成

```java
@SpringBootApplication(scanBasePackages = {"${your base packages}", "io.github.dddplus"})
public class WebApplication {
    public static void main(String[] args) {
        SpringApplication.run(WebApplication.class);
    }
}
```

### 逆向建模

`DDDplus`里的基于DDD的正向建模，与基于AST静态分析的逆向建模是相互独立的。如果你觉得DDD落地太难，那么可以只使用逆向建模部分，即使一个遗留系统，也可以使用逆向建模功能：让代码承载领域知识，生成业务洞见，还原架构设计，识别代码设计缺陷，为需求分析提供依据。

请参考[《逆向建模教程》](doc/ReverseModelingGuide.md)。

```xml
<dependency>
    <groupId>io.github.dddplus</groupId>
    <artifactId>dddplus-visualization</artifactId>
</dependency>
```

通过[DSL](/dddplus-spec/src/main/java/io/github/dddplus/dsl)在代码进行标注后，自动生成多视角视图。

```bash
mvn io.github.dddplus:dddplus-maven-plugin:model \
    -DrootDir=${colon separated source code dirs} \
    -DplantUml=${target business model in svg format} \
    -DtextModel=${target business model in txt format}
```

### 架构守护

为了避免错误使用造成的线上事故，建议CI流水线里增加DDDplus的错误使用门禁。

```bash
mvn io.github.dddplus:dddplus-maven-plugin:enforce \
    -DrootPackage={your pkg} \
    -DrootDir={your src dir}
```

## Contribution

You are welcome to contribute to the project with pull requests on GitHub.

If you find a bug or want to request a feature, please use the [Issue Tracker](https://github.com/funkygao/cp-ddd-framework/issues).

For any question, you can use [Gitter Chat](https://gitter.im/cp-ddd-framework/community) to ask.

## Licensing

DDDplus is licensed under the Apache License, Version 2.0 (the "License"); you may not use this project except in compliance with the License. You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0).

```

### File: RELEASE_NOTES.md
```md
## Release Notes - DDDplus - 2.1.0

* Feature
   * 通过apache bcel库实现完全非侵入式call graph图
      * 提示哪些类和方法在关系图上可能被排除
      * 支持用户自定义类关系
   * 提供io.github.dddplus:dddplus-maven-plugin的三个功能
      * 与IDEA内置的Call Hierarchy功能相比
         * IDEA只能基于单个方法分析，DDDplus全局分析
         * 提供配置驱动的噪音过滤机制，使得自动生成的关系图突出重点
      * model 基于DDDplus DSL标注产生的逆向业务模型
      * call 完全非侵入式基于字节码增强机制分析jar包生成类方法调用关系图
      * polymorphism 完全非侵入式基于AST Parser自动生成具有多态的类关系图
      * enforce DDDplus正向建模的架构约束强化工具

## Release Notes - DDDplus - 2.0.3

* Feature
   * 根据源代码AST分析，形成结构化数据，导出到sqlite数据库
   * 生成原始的plantuml文件
   * 可以修改实体所在的包
   * KeyUsecase图里显示类的javadoc
   * 业务字典，枚举类，也可以使用 KeyElement 进行标注
   * PlantUML类图里，KeyFlow对应的文件可以点击，自动在IDEA中打开到对应位置

* Bug Fix
   * 逆向分析时，KeyRelation会把一个类放在了错误的package


## Release Notes - DDDplus - 2.0.2

* Feature
   * 提供详细的《逆向建模教程》
   * ClassMethodReport 增加大方法的自动发现
   * KeyElement#types 增加默认值，降低DSL标注成本
* Fix
   * CallGraphAstNodeVisitor 运行是抛出异常导致无法继续执行

## Release Notes - DDDplus - 2.0.1-RELEASE

* 新功能
   * 从代码里自动生成方法的call graph图，用于评估代码改动的影响范围和风险，从宏观上对代码结构和类之间关系有了洞察
      * 由于只关注DSL标注的方法，去除了噪音，这样的图才不会混乱
   * 从代码里自动分析包之间的交叉引用图，用于发现不合理依赖关系，包的设计是否合理
   * 新增dddplus-maven-plugin模块，把静态检查、代码可视化等功能集成到maven插件里，方便使用和集成
   * 扩展点的方法返回值不能为primitive type，以避免NPE，之前只是规范说明，目前增加了ExtensionMethodSignatureEnforcer，结合CI可以彻底杜绝此类问题

* Feature
   * add ExtensionMethodSignatureEnforcer to avoid NPE risk
   * call graph complete and exact click through
   * add dddplus-maven-plugin
   * visualize package cross reference in svg file

## Release Notes - DDDplus - 2.0.0-SNAPSHOT

* FIXED
   * [如果所有pattern扩展点叠加执行，导致 ClassCastException](https://github.com/dddplus/dddplus/commit/b90bd6a71b66f5b1c60460949bdd8b7ab833f854)

* Feature
   * [Reverse Modeling DSL](/dddplus-spec/src/main/java/io/github/dddplus/dsl/package-info.java)
   * Patches DDD with complete [building blocks](/dddplus-spec/src/main/java/io/github/dddplus/model/)
   * [Pragmatic DDDplus Showcase Project](/dddplus-test/src/test/java/ddd/plus/showcase/)

* Incompatible changes with 1.x.y
   * Removed
      * `IBaseTranslator`, `ApiResult`, `RequestProfile`, `IModelAttachmentExt`, `IDomainModelCreator`
   * Renamed
      * `IExtPolicy` -> `IPolicy`
      * `BaseDomainAbility` -> `BaseRouter`, `@DomainAbility` -> `@Router`
      * `DDD.findAbility` -> `DDD.useRouter`/`DDD.usePolicy`
      * `Reducer` -> `IReducer`
   * Function signature changed
      * all `IDomainExtension` input argument changed from `IDomainModel` to `IIdentity`

## Release Notes - DDDplus - Version 1.1.1

* FIXED
   * [#39](https://github.com/funkygao/cp-ddd-framework/issues/39) 解决Policy定位的扩展点如果不存在则抛出NullPointerException

## Release Notes - DDDplus - Version 1.1.0

* FIXED
   * 解决了`BaseDomainAbility`由于泛型机制不支持继承的问题
   * [#7](https://github.com/dddplus/dddplus/issues/7) 解决`DomainArtifacts`暴露扩展点不全的问题：如果一个扩展点只被`Partner`实现，就没有暴露
   * [#30](https://github.com/funkygao/cp-ddd-framework/issues/30) 解决了Plugin jar reload后，`DomainArtifacts`没有刷新的问题

* Feature
   * [#37](https://github.com/funkygao/cp-ddd-framework/issues/37) 除了`Partner/Pattern`的静态的扩展点路由机制外，提供了动态路由机制：`Policy`，供使用者扩展
   * [#35](https://github.com/funkygao/cp-ddd-framework/issues/35) 提供绕过`BaseDomainAbility`而直接路由扩展点的机制，在业务属性不明显的场景下使用
   * [#32](https://github.com/funkygao/cp-ddd-framework/issues/32) 框架提供默认的步骤编排能力，使用者不必从头编写`Ability`来编排步骤
   * 增加了一个使用`DDDplus`来搭建`low-code`平台的例子工程：https://github.com/dddplus/easyapp
      * 其中的Trigger机制依靠扩展点和Plugin的动态加载实现

## Release Notes - DDDplus - Version 1.0.3

* FIXED
   * [#20](https://github.com/funkygao/cp-ddd-framework/issues/20) Plugin reloading, Spring unable to get the Partner bean
   * [#28](https://github.com/funkygao/cp-ddd-framework/issues/28) ArchitectureEnforcer的接口规范 bug，需要把注解排除在外
   * [dddplus/dddplus#4](https://github.com/dddplus/dddplus/issues/4) 在Spring Boot集成时，无法触发`IStartupListener`

* Improvement
   * [#19](https://github.com/funkygao/cp-ddd-framework/issues/19) Add `@Specification` for `ISpecification` interface: specifications are Spring beans
   * [#29](https://github.com/funkygao/cp-ddd-framework/issues/29) 演示如何对step进行方法拦截

* Feature
   * [#24](https://github.com/funkygao/cp-ddd-framework/issues/24) Step可以异步执行，同步回滚
   * [#23](https://github.com/funkygao/cp-ddd-framework/issues/23) 提供`DomainArtifacts`，方便业务能力可视化

* Test
   * [#26](https://github.com/funkygao/cp-ddd-framework/issues/26) Stress test for plugin jar reloading passed

## Release Notes - DDDplus - Version 1.0.2

* FIXED
   * NPE when Plugin load without using Spring

* Improvement
   * Add Specification & Notification Pattern to DDDplus for explicit business rules expression

## Release Notes - DDDplus - Version 1.0.1

* Improvement
   * Integrated with CodeQL
   * Being renamed to DDDplus
   * Container.java and Plugin.java refactored: explicit over implicit
   * Plugin jar reloading will not allow concurrency

* Test
   * NamedThreadFactory test case bug fixed

```

