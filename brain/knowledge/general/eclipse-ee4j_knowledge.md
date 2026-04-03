---
id: eclipse-ee4j-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:21.431368
---

# KNOWLEDGE EXTRACT: eclipse-ee4j
> **Extracted on:** 2026-03-30 17:36:11
> **Source:** eclipse-ee4j

---

## File: `cargotracker.md`
```markdown
# 📦 eclipse-ee4j/cargotracker [🔖 PENDING/APPROVE]
🔗 https://github.com/eclipse-ee4j/cargotracker
🌐 https://eclipse-ee4j.github.io/cargotracker/

## Meta
- **Stars:** ⭐ 375 | **Forks:** 🍴 176
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The project demonstrates how you can develop applications with Jakarta EE using widely adopted architectural best practices like Domain-Driven Design (DDD).

## README (trích đầu)
```
# Eclipse Cargo Tracker - Applied Domain-Driven Design Blueprints for Jakarta EE



The project demonstrates how you can develop applications with Jakarta EE using widely adopted architectural best 

practices like Domain-Driven Design (DDD). The project is based on the well-known [Java DDD sample application](https://github.com/citerus/dddsample-core) 

developed by DDD pioneer Eric Evans' company Domain Language and the Swedish software consulting company Citerus. 

The cargo example actually comes from Eric Evans' seminal book on DDD.



The application is an end-to-end system for keeping track of shipping cargo. It

has several interfaces described in the following sections.



For further details on the project, please visit: https://eclipse-ee4j.github.io/cargotracker/.



A slide deck introducing the fundamentals of the project is available on the official Eclipse

Foundation [Jakarta EE SlideShare account](https://www.slideshare.net/Jakarta_EE/applied-domaindriven-design-blueprints-for-jakarta-ee). A recording of the slide deck is available on the official [Jakarta EE YouTube account](https://www.youtube.com/watch?v=pKmmZd-3mhA).



![Eclipse Cargo Tracker cover](cargo_tracker_cover.png)



## Getting Started



The [project website](https://eclipse-ee4j.github.io/cargotracker/) has detailed information on how to get started.



The simplest steps are the following (no IDE required):



* Get the project source code.

* Ensure you are running Java SE 11 or Java SE 17.

* Make sure JAVA_HOME is set.

* Navigate to the project source root and type:

```

./mvnw clean package cargo:run

```

* Go to http://localhost:8080/cargo-tracker



This will run the application with Payara Server by default. The project also has Maven profiles to support GlassFish 

and Open Liberty. For example, you can run using GlassFish using the following command: 



```

./mvnw clean package -Pglassfish cargo:run

```



Similarly, you can run using Open Liberty using the following command:



```

./mvnw clean package -Popenliberty liberty:run

```



To set up in Visual Studio Code, follow these steps:



* Set up Java SE 11, or Java SE 17, [Visual Studio Code](https://code.visualstudio.com/download) and [Payara 6](https://www.payara.fish/downloads/payara-platform-community-edition/). You will also need to set up the [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack) and [Payara Tools](https://marketplace.visualstudio.com/items?itemName=Payara.payara-vscode) in Visual Studio Code.

* Make sure JAVA_HOME is set.

* Open the directory that contains the code in Visual Studio Code. Visual Studio Code will do the rest for you, it should automatically configure a Maven project. Proceed with clean/building the application.

* After the project is built (which will take a while the very first time as Maven downloads dependencies), simply run the generated `cargo-tracker.war` file under the `target` directory using P
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

