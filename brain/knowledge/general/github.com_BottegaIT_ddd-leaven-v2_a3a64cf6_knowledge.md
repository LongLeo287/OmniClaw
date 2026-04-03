---
id: github.com-bottegait-ddd-leaven-v2-a3a64cf6-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:35.740705
---

# KNOWLEDGE EXTRACT: github.com_BottegaIT_ddd-leaven-v2_a3a64cf6
> **Extracted on:** 2026-04-01 14:38:50
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524024/github.com_BottegaIT_ddd-leaven-v2_a3a64cf6

---

## File: `.gitignore`
```
/target
/.settings
/.classpath
/.project
```

## File: `LICENSE.txt`
```
Copyright 2011-2014 the original author or authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## File: `README.md`
```markdown
ddd-leaven-v2
=============

DDD-CqRS sample v2.0 project that helps you with starting out advanced domain modeling using Spring, JPA and testing.

Wiki is still under construction, bout you can use this "map" to navigate through the code: http://prezi.com/akrfq7jyau8w/ddd-cqrs-leaven-v20/

Group: https://groups.google.com/forum/#!forum/ddd-cqrs-sample

Blog: http://ddd-cqrs-leaven.blogspot.com/


## Another DDD and CqRS Sample?

Primary goals of this project are the following: 
* presenting sample implementation of all DDD Building Blocks and techniques - no technical compromises, real world problems and solutions 
* presenting advanced lingustic techniques that are usefull for exploring Domian Exper knowledge during Modeling Wirlpool sessions
* providing well crafted code, ready to be utilized in production 
* presenting ready ready to use and easy to adopt tools and best practices 


## What is Leaven idea?

Our intention is to provide a leaven ([leavening agent](http://en.wikipedia.org/wiki/Leavening_agent)) - something that you use to make bread - a good one. 


## You are the Architect!

So you take our leaven, understand it deeply and modify to fit your context. 

You don't need to couple your code with the leaven code. You can, but don't have to extend our classes. Better approach is to change, rename and repackage leaven classes:. 

Leaven is really simple and small. We achieved this by developing straightforward code without unnecessary abstraction-distraction like XML, and inner accidental complexity typical for frameowrks. 

If You want to change something then go straight to the code and do it instead of reading this documentation. You are the Architect! 
Noninvasive philosophy

Our goal is to prepare a business developer programming model (way of thinking about class-level design) that is free of any platform-specific solutions. 

Business developer should focus on analysis and domain modeling - engine does technical stuff. 
Portable architecture - technical independence

Although the implementation is based on Spring and JPA we managed to avoid any special approach or programming model. Therefore our architecture is portable which means You can implement this "style" using any Java framework or platform (EJB, etc).
```

## File: `pom.xml`
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>pl.com.bottega.ddd-sample-2</groupId>
	<artifactId>ddd-sample-2</artifactId>
	<version>0.0.1-SNAPSHOT</version>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>

		<spring.version>4.2.6.RELEASE</spring.version>
	</properties>

	<build>
		<pluginManagement>
			<plugins>
				<plugin>
					<groupId>org.apache.maven.plugins</groupId>
					<artifactId>maven-compiler-plugin</artifactId>
					<version>2.5.1</version>
					<configuration>
						<source>1.7</source>
						<target>1.7</target>
					</configuration>
				</plugin>
			</plugins>
		</pluginManagement>
		<plugins>
			<!-- run maven build with license:format goals to add license notice to 
				the files that are missing it -->
			<plugin>
				<groupId>com.mycila.maven-license-plugin</groupId>
				<artifactId>maven-license-plugin</artifactId>
				<configuration>
					<header>LICENSE.txt</header>
					<mapping>
						<java>SLASHSTAR_STYLE</java>
					</mapping>
				</configuration>
			</plugin>
		</plugins>
	</build>

	<dependencies>
		<dependency>
			<groupId>org.hibernate</groupId>
			<artifactId>hibernate-entitymanager</artifactId>
			<version>4.2.0.Final</version>
		</dependency>
		<dependency>
			<groupId>org.hsqldb</groupId>
			<artifactId>hsqldb</artifactId>
			<version>2.2.9</version>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>javax.inject</groupId>
			<artifactId>javax.inject</artifactId>
			<version>1</version>
		</dependency>
		<dependency>
			<groupId>javax.annotation</groupId>
			<artifactId>jsr250-api</artifactId>
			<version>1.0</version>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-context</artifactId>
			<version>${spring.version}</version>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-web</artifactId>
			<version>${spring.version}</version>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-tx</artifactId>
			<version>${spring.version}</version>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-orm</artifactId>
			<version>${spring.version}</version>
		</dependency>

		<!-- required for @Scope(proxyMode = ScopedProxyMode.TARGET_CLASS) -->
		<dependency>
			<groupId>cglib</groupId>
			<artifactId>cglib-nodep</artifactId>
			<version>2.2.2</version>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-log4j12</artifactId>
			<version>1.7.1</version>
		</dependency>
		<!-- commonly used utils libraries -->
		<dependency>
			<groupId>com.google.guava</groupId>
			<artifactId>guava</artifactId>
			<version>13.0.1</version>
		</dependency>
		<dependency>
			<groupId>org.apache.commons</groupId>
			<artifactId>commons-lang3</artifactId>
			<version>3.1</version>
		</dependency>

		<!-- test scope -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-test</artifactId>
			<version>${spring.version}</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit-dep</artifactId>
			<version>4.10</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.mockito</groupId>
			<artifactId>mockito-core</artifactId>
			<version>1.9.5</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.hamcrest</groupId>
			<artifactId>hamcrest-core</artifactId>
			<version>1.3</version>
			<scope>test</scope>
		</dependency>
		<!-- <dependency> <groupId>org.kubek2k</groupId> <artifactId>springockito-annotations</artifactId> 
			<version>1.0.8</version> <scope>test</scope> </dependency> -->
		<dependency>
			<groupId>org.easytesting</groupId>
			<artifactId>fest-assert-core</artifactId>
			<version>2.0M10</version>
		</dependency>
	</dependencies>

	<repositories>
		<repository>
			<id>org.springframework.maven.milestone</id>
			<url>http://maven.springframework.org/milestone </url>
		</repository>
	</repositories>
</project>
```

## File: `diagrams/OrderingService.ucls`
```
<?xml version="1.0" encoding="UTF-8"?>
<class-diagram version="1.1.4" icons="true" automaticImage="PNG" always-add-relationships="true" generalizations="true" 
  realizations="true" associations="true" dependencies="true" nesting-relationships="true">  
  <class id="1" language="java" name="pl.com.bottega.ecommerce.sales.application.impl.OrderingServiceImpl" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/application/impl/OrderingServiceImpl.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="537" y="200"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="2" language="java" name="pl.com.bottega.ecommerce.system.application.SystemUser" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/core/application/SystemUser.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="897" y="186"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="3" language="java" name="pl.com.bottega.ecommerce.system.application.SystemContext" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/core/application/SystemContext.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="1153" y="191"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <association id="4">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="5" name="systemUser"/>      
      <multiplicity id="6" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="2" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <dependency id="7">    
    <end type="SOURCE" refId="3"/>    
    <end type="TARGET" refId="2"/>  
  </dependency>  
  <classifier-display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" 
    accessors="true" visibility="true">    
    <attributes public="true" package="true" protected="false" private="false" static="false"/>    
    <operations public="true" package="true" protected="false" private="false" static="false"/>  
  </classifier-display>  
  <association-display labels="true" multiplicity="true"/>
</class-diagram>
```

## File: `diagrams/equivalent.ucls`
```
<?xml version="1.0" encoding="UTF-8"?>
<class-diagram version="1.1.4" icons="true" automaticImage="PNG" always-add-relationships="false" generalizations="true" 
  realizations="true" associations="true" dependencies="false" nesting-relationships="true">  
  <class id="1" language="java" name="pl.com.bottega.ecommerce.sales.domain.equivalent.SuggestionService" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/equivalent/SuggestionService.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="99" width="228" x="295" y="226"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="2" language="java" name="pl.com.bottega.ecommerce.sales.domain.productscatalog.Product" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/Product.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="416" y="496"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="3" language="java" name="pl.com.bottega.ecommerce.sales.domain.client.Client" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/client/Client.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="103" y="163"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="4" language="java" name="pl.com.bottega.ecommerce.sales.domain.equivalent.ProductSpecificationFactory" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/equivalent/ProductSpecificationFactory.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="745" y="126"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <association id="5">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="6" name="productSpecificationFactory"/>      
      <multiplicity id="7" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="4" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <classifier-display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" 
    accessors="true" visibility="true">    
    <attributes public="true" package="true" protected="false" private="false" static="false"/>    
    <operations public="true" package="true" protected="false" private="false" static="false"/>  
  </classifier-display>  
  <association-display labels="true" multiplicity="true"/>
</class-diagram>
```

## File: `diagrams/invoicing.ucls`
```
<?xml version="1.0" encoding="UTF-8"?>
<class-diagram version="1.1.4" icons="true" automaticImage="PNG" always-add-relationships="true" generalizations="true" 
  realizations="true" associations="true" dependencies="true" nesting-relationships="true">  
  <class id="1" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.BookKeeper" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/BookKeeper.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="550" y="516"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="2" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.InvoiceRequest" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceRequest.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="104" y="417"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="3" language="java" 
    name="pl.com.bottega.ecommerce.sales.application.internal.bookkeeping.BookKeepingListener" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/application/internal/bookkeeping/BookKeepingListener.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="99" width="284" x="-44" y="-26"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="4" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.InvoiceRequestFactory" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceRequestFactory.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="101" y="214"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <interface id="5" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.TaxPolicy" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/TaxPolicy.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="548" y="337"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </interface>  
  <class id="6" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.TaxAdvisor" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/TaxAdvisor.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="549" y="196"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="7" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.InvoiceFactory" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceFactory.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="856" y="514"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="8" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.Invoice" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/Invoice.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="1151" y="510"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="9" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.InvoiceLine" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceLine.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="1147" y="746"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="10" language="java" name="pl.com.bottega.ecommerce.sales.domain.invoicing.Tax" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/Tax.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="813" y="778"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="11" language="java" name="pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/canonicalmodel/publishedlanguage/ClientData.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="1447" y="741"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="12" language="java" name="pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductData" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/ProductData.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="1198" y="988"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <dependency id="13">    
    <end type="SOURCE" refId="4"/>    
    <end type="TARGET" refId="2"/>  
  </dependency>  
  <association id="14">    
    <end type="SOURCE" refId="8" navigable="false">      
      <attribute id="15" name="items"/>      
      <multiplicity id="16" minimum="0" maximum="2147483647"/>    
    </end>    
    <end type="TARGET" refId="9" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <dependency id="17">    
    <end type="SOURCE" refId="1"/>    
    <end type="TARGET" refId="2"/>  
  </dependency>  
  <association id="18">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="19" name="invoiceFactory"/>      
      <multiplicity id="20" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="7" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="21">    
    <end type="SOURCE" refId="9" navigable="false">      
      <attribute id="22" name="tax"/>      
      <multiplicity id="23" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="10" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="24">    
    <end type="SOURCE" refId="3" navigable="false">      
      <attribute id="25" name="invoiceRequestFactory"/>      
      <multiplicity id="26" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="4" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <dependency id="27">    
    <end type="SOURCE" refId="1"/>    
    <end type="TARGET" refId="5"/>  
  </dependency>  
  <association id="28">    
    <end type="SOURCE" refId="3" navigable="false">      
      <attribute id="29" name="taxAdvisor"/>      
      <multiplicity id="30" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="6" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="31">    
    <end type="SOURCE" refId="9" navigable="false">      
      <attribute id="32" name="product"/>      
      <multiplicity id="33" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="12" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="34">    
    <end type="SOURCE" refId="8" navigable="false">      
      <attribute id="35" name="client"/>      
      <multiplicity id="36" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="11" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <dependency id="37">    
    <end type="SOURCE" refId="6"/>    
    <end type="TARGET" refId="5"/>  
  </dependency>  
  <dependency id="38">    
    <end type="SOURCE" refId="7"/>    
    <end type="TARGET" refId="8"/>  
  </dependency>  
  <classifier-display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" 
    accessors="true" visibility="true">    
    <attributes public="true" package="true" protected="false" private="false" static="false"/>    
    <operations public="true" package="true" protected="false" private="false" static="false"/>  
  </classifier-display>  
  <association-display labels="true" multiplicity="true"/>
</class-diagram>
```

## File: `diagrams/offer.ucls`
```
<?xml version="1.0" encoding="UTF-8"?>
<class-diagram version="1.1.4" icons="true" automaticImage="PNG" always-add-relationships="true" generalizations="true" 
  realizations="true" associations="true" dependencies="true" nesting-relationships="true">  
  <class id="1" language="java" name="pl.com.bottega.ecommerce.sales.domain.offer.Offer" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/Offer.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="171" width="211" x="471" y="144"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="2" language="java" name="pl.com.bottega.ecommerce.sales.domain.offer.OfferItem" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/OfferItem.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="568" y="528"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="3" language="java" name="pl.com.bottega.ecommerce.sales.domain.productscatalog.Product" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/Product.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="-104" y="512"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="4" language="java" name="pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductData" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/ProductData.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="230" y="504"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="5" language="java" name="pl.com.bottega.ecommerce.sales.domain.reservation.Reservation" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/Reservation.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="-24" y="142"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <interface id="6" language="java" name="pl.com.bottega.ecommerce.sales.domain.offer.DiscountPolicy" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/DiscountPolicy.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="-3" y="-127"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </interface>  
  <class id="7" language="java" name="pl.com.bottega.ecommerce.sales.domain.offer.DiscountFactory" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/DiscountFactory.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="-301" y="-119"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <dependency id="8">    
    <end type="SOURCE" refId="5"/>    
    <end type="TARGET" refId="6"/>  
  </dependency>  
  <dependency id="9">    
    <end type="SOURCE" refId="5"/>    
    <end type="TARGET" refId="3"/>  
  </dependency>  
  <dependency id="10">    
    <end type="SOURCE" refId="7"/>    
    <end type="TARGET" refId="6"/>  
  </dependency>  
  <dependency id="11">    
    <end type="SOURCE" refId="3"/>    
    <end type="TARGET" refId="4"/>  
  </dependency>  
  <association id="12">    
    <bendpoint x="531" y="365"/>    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="13" name="unavailableItems"/>      
      <multiplicity id="14" minimum="0" maximum="2147483647"/>    
    </end>    
    <end type="TARGET" refId="2" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="15">    
    <bendpoint x="687" y="361"/>    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="16" name="availabeItems"/>      
      <multiplicity id="17" minimum="0" maximum="2147483647"/>    
    </end>    
    <end type="TARGET" refId="2" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="18">    
    <end type="SOURCE" refId="2" navigable="false">      
      <attribute id="19" name="productData"/>      
      <multiplicity id="20" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="4" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <dependency id="21">    
    <end type="SOURCE" refId="5"/>    
    <end type="TARGET" refId="1"/>  
  </dependency>  
  <classifier-display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" 
    accessors="true" visibility="true">    
    <attributes public="true" package="true" protected="false" private="false" static="false"/>    
    <operations public="true" package="true" protected="false" private="false" static="false"/>  
  </classifier-display>  
  <association-display labels="true" multiplicity="true"/>
</class-diagram>
```

## File: `diagrams/payments.ucls`
```
<?xml version="1.0" encoding="UTF-8"?>
<class-diagram version="1.1.4" icons="true" automaticImage="PNG" always-add-relationships="false" generalizations="true" 
  realizations="true" associations="true" dependencies="false" nesting-relationships="true">  
  <class id="1" language="java" name="pl.com.bottega.ecommerce.sales.domain.payment.Payment" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/payment/Payment.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="99" width="222" x="499" y="228"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="2" language="java" name="pl.com.bottega.ecommerce.sales.domain.payment.PaymentFactory" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/payment/PaymentFactory.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="273" y="280"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="3" language="java" name="pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/canonicalmodel/publishedlanguage/ClientData.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="598" y="486"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="4" language="java" name="pl.com.bottega.ecommerce.canonicalmodel.events.PaymentRolledBackEvent" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/canonicalmodel/events/PaymentRolledBackEvent.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="1019" y="671"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="5" language="java" name="pl.com.bottega.ecommerce.canonicalmodel.events.ClientPaidEvent" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/canonicalmodel/events/ClientPaidEvent.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="234" y="707"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="6" language="java" name="pl.com.bottega.ecommerce.sales.domain.client.Client" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/client/Client.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="-53" y="287"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <association id="7">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="8" name="paymentFactory"/>      
      <multiplicity id="9" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="2" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="10">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="11" name="clientData"/>      
      <multiplicity id="12" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="3" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="13">    
    <end type="SOURCE" refId="6" navigable="false">      
      <attribute id="14" name="paymentFactory"/>      
      <multiplicity id="15" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="2" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <classifier-display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" 
    accessors="true" visibility="true">    
    <attributes public="true" package="true" protected="false" private="false" static="false"/>    
    <operations public="true" package="true" protected="false" private="false" static="false"/>  
  </classifier-display>  
  <association-display labels="true" multiplicity="true"/>
</class-diagram>
```

## File: `diagrams/purchase.ucls`
```
<?xml version="1.0" encoding="UTF-8"?>
<class-diagram version="1.1.4" icons="true" automaticImage="PNG" always-add-relationships="true" generalizations="true" 
  realizations="true" associations="true" dependencies="true" nesting-relationships="true">  
  <class id="1" language="java" name="pl.com.bottega.ecommerce.sales.domain.purchase.Purchase" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/purchase/Purchase.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="189" width="388" x="291" y="182"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="2" language="java" name="pl.com.bottega.ecommerce.sales.domain.purchase.PurchaseFactory" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/purchase/PurchaseFactory.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="49" y="245"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="3" language="java" name="pl.com.bottega.ecommerce.sales.domain.purchase.PurchaseItem" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/purchase/PurchaseItem.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="430" y="525"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="4" language="java" name="pl.com.bottega.ecommerce.sales.domain.offer.Offer" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/Offer.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="-260" y="196"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="5" language="java" name="pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductData" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/ProductData.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="128" y="682"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="6" language="java" name="pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/canonicalmodel/publishedlanguage/ClientData.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="117" width="270" x="606" y="427"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="7" language="java" name="pl.com.bottega.ecommerce.sales.domain.client.Client" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/client/Client.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="-257" y="406"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="8" language="java" name="pl.com.bottega.ecommerce.canonicalmodel.events.OrderSubmittedEvent" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/canonicalmodel/events/OrderSubmittedEvent.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="877" y="794"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <association id="9">    
    <end type="SOURCE" refId="3" navigable="false">      
      <attribute id="10" name="productData"/>      
      <multiplicity id="11" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="5" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="12">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="13" name="items"/>      
      <multiplicity id="14" minimum="0" maximum="2147483647"/>    
    </end>    
    <end type="TARGET" refId="3" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <dependency id="15">    
    <end type="SOURCE" refId="2"/>    
    <end type="TARGET" refId="1"/>  
  </dependency>  
  <dependency id="16">    
    <end type="SOURCE" refId="2"/>    
    <end type="TARGET" refId="7"/>  
  </dependency>  
  <association id="17">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="18" name="clientData"/>      
      <multiplicity id="19" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="6" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <dependency id="20">    
    <end type="SOURCE" refId="2"/>    
    <end type="TARGET" refId="4"/>  
  </dependency>  
  <classifier-display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" 
    accessors="true" visibility="true">    
    <attributes public="true" package="true" protected="false" private="false" static="false"/>    
    <operations public="true" package="true" protected="false" private="false" static="false"/>  
  </classifier-display>  
  <association-display labels="true" multiplicity="true"/>
</class-diagram>
```

## File: `diagrams/reservation.ucls`
```
<?xml version="1.0" encoding="UTF-8"?>
<class-diagram version="1.1.4" icons="true" automaticImage="PNG" always-add-relationships="true" generalizations="true" 
  realizations="true" associations="true" dependencies="true" nesting-relationships="true">  
  <class id="1" language="java" name="pl.com.bottega.ecommerce.sales.domain.reservation.Reservation" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/Reservation.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="802" y="164"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="2" language="java" name="pl.com.bottega.ecommerce.sales.domain.reservation.ReservationFactory" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservationFactory.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="116" y="120"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="3" language="java" name="pl.com.bottega.ecommerce.sales.domain.reservation.ReservationItem" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservationItem.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="881" y="512"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="4" language="java" name="pl.com.bottega.ecommerce.sales.domain.reservation.ReservedProduct" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservedProduct.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="464" y="517"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="5" language="java" name="pl.com.bottega.ecommerce.sales.domain.client.Client" project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/client/Client.java" binary="false" 
    corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="111" y="352"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="6" language="java" name="pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/canonicalmodel/publishedlanguage/ClientData.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="439" y="245"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <class id="7" language="java" name="pl.com.bottega.ecommerce.sales.domain.productscatalog.Product" 
    project="ddd-leaven-v2" 
    file="/ddd-leaven-v2/src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/Product.java" 
    binary="false" corner="BOTTOM_RIGHT">    
    <position height="-1" width="-1" x="880" y="797"/>    
    <display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" accessors="true" 
      visibility="true">      
      <attributes public="true" package="true" protected="false" private="false" static="false"/>      
      <operations public="true" package="true" protected="false" private="false" static="false"/>    
    </display>  
  </class>  
  <dependency id="8">    
    <end type="SOURCE" refId="2"/>    
    <end type="TARGET" refId="1"/>  
  </dependency>  
  <dependency id="9">    
    <end type="SOURCE" refId="2"/>    
    <end type="TARGET" refId="5"/>  
  </dependency>  
  <dependency id="10">    
    <end type="SOURCE" refId="1"/>    
    <end type="TARGET" refId="4"/>  
  </dependency>  
  <dependency id="11">    
    <end type="SOURCE" refId="5"/>    
    <end type="TARGET" refId="6"/>  
  </dependency>  
  <association id="12">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="13" name="clientData"/>      
      <multiplicity id="14" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="6" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="15">    
    <end type="SOURCE" refId="1" navigable="false">      
      <attribute id="16" name="items"/>      
      <multiplicity id="17" minimum="0" maximum="2147483647"/>    
    </end>    
    <end type="TARGET" refId="3" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <association id="18">    
    <end type="SOURCE" refId="3" navigable="false">      
      <attribute id="19" name="product"/>      
      <multiplicity id="20" minimum="0" maximum="1"/>    
    </end>    
    <end type="TARGET" refId="7" navigable="true"/>    
    <display labels="true" multiplicity="true"/>  
  </association>  
  <classifier-display autosize="true" stereotype="true" package="true" initial-value="false" signature="true" 
    accessors="true" visibility="true">    
    <attributes public="true" package="true" protected="false" private="false" static="false"/>    
    <operations public="true" package="true" protected="false" private="false" static="false"/>  
  </classifier-display>  
  <association-display labels="true" multiplicity="true"/>
</class-diagram>
```

## File: `src/main/java/pl/com/bottega/cqrs/annotations/Command.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.cqrs.annotations;

import java.lang.annotation.Documented;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import pl.com.bottega.cqrs.command.handler.CommandHandler;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface Command {
	/**
	 * Suggestion for a Server that this command may be run in asynchronous way.
	 * <br>
	 * If true than {@link CommandHandler} must return void - otherwise Serwer will throw an exception 
	 * @return
	 */
    boolean asynchronous() default false;

    /**
     * Suggestion for a Server that this command should checked if the same command is sent again.<br>
     * If true than command class must implement equals and hashCode
     * @return
     */
    boolean unique() default false;

    /**
     * If unique is true than this property may specify maximum timeout in miliseconds before same command can be executed
     * @return
     */
    long uniqueStorageTimeout() default 0L;
}
```

## File: `src/main/java/pl/com/bottega/cqrs/annotations/CommandHandlerAnnotation.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.cqrs.annotations;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

/**
 * @author Slawek
 */
@Component
@Transactional
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface CommandHandlerAnnotation {
}
```

## File: `src/main/java/pl/com/bottega/cqrs/command/Gate.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.cqrs.command;

/**
 * Main access point to the Application.<br>
 * It handles:
 * <ul>
 * <li>filtering command duplicates
 * <li>command queues for asynchronous commands 
 * </ul>
 * 
 * @author Slawek
 *
 */
public interface Gate {

	public abstract Object dispatch(Object command);

}
```

## File: `src/main/java/pl/com/bottega/cqrs/command/handler/CommandHandler.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.cqrs.command.handler;

import pl.com.bottega.cqrs.annotations.Command;

/**
 * 
 * @author Slawek
 *
 * @param <C> command
 * @param <R> result type - for asynchronous {@link Command}commands (asynchronous=true) should be {@link Void}
 */
public interface CommandHandler<C, R> {

    public R handle(C command);
}
```

## File: `src/main/java/pl/com/bottega/cqrs/command/handler/spring/SpringHandlersProvider.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.cqrs.command.handler.spring;

import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.Map;

import javax.inject.Inject;

import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.stereotype.Component;

import pl.com.bottega.cqrs.command.handler.CommandHandler;
import pl.com.bottega.cqrs.command.impl.RunEnvironment.HandlersProvider;

@Component
public class SpringHandlersProvider implements HandlersProvider, ApplicationListener<ContextRefreshedEvent> {

    @Inject
    private ConfigurableListableBeanFactory beanFactory;

    private Map<Class<?>, String> handlers = new HashMap<Class<?>, String>();

    @SuppressWarnings("unchecked")
	@Override
    public CommandHandler<Object, Object> getHandler(Object command) {
        String beanName = handlers.get(command.getClass());
        if (beanName == null) {
            throw new RuntimeException("command handler not found. Command class is " + command.getClass());
        }
        CommandHandler<Object, Object> handler = beanFactory.getBean(beanName, CommandHandler.class);
        return handler;
    }

    @Override
    public void onApplicationEvent(ContextRefreshedEvent event) {
        handlers.clear();
        String[] commandHandlersNames = beanFactory.getBeanNamesForType(CommandHandler.class);
        for (String beanName : commandHandlersNames) {
            BeanDefinition commandHandler = beanFactory.getBeanDefinition(beanName);
            try {
                Class<?> handlerClass = Class.forName(commandHandler.getBeanClassName());
                handlers.put(getHandledCommandType(handlerClass), beanName);
            } catch (ClassNotFoundException e) {
                throw new RuntimeException(e);
            }
        }
    }

    private Class<?> getHandledCommandType(Class<?> clazz) {
        Type[] genericInterfaces = clazz.getGenericInterfaces();
        ParameterizedType type = findByRawType(genericInterfaces, CommandHandler.class);
        return (Class<?>) type.getActualTypeArguments()[0];
    }

    private ParameterizedType findByRawType(Type[] genericInterfaces, Class<?> expectedRawType) {
        for (Type type : genericInterfaces) {
            if (type instanceof ParameterizedType) {
                ParameterizedType parametrized = (ParameterizedType) type;
                if (expectedRawType.equals(parametrized.getRawType())) {
                    return parametrized;
                }
            }
        }
        throw new RuntimeException();
    }
}
```

## File: `src/main/java/pl/com/bottega/cqrs/command/impl/GateHistory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.cqrs.command.impl;

import java.util.Date;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

import pl.com.bottega.cqrs.annotations.Command;

/**
 * Manages command execution history based on {@link Command} annotation attributes<br>
 * Commands that are annotated as unique=true are stored in this history.<br>
 * History checks if the same command (equals) is called again.<br>
 * <br>
 * Each command class has it's own entries in history - history length can be parameterized via constructor parameter. 
 * 
 * @author Slawek
 * 
 */
class GateHistory {

	@SuppressWarnings("serial")
	// TODO Sprawdzic czy nie musi byc concurrent (history jest, na tym
	// poziomie nie musi byc totalnej synchronizacji, to tylko rodzaj
	// cache)
	private class CommandExecutionsMap extends LinkedHashMap<Object, Date> {
		protected boolean removeEldestEntry(Map.Entry<Object, Date> eldest) {
			return this.size() > maxHistoryCapacity;
		}
	};

	private static final int DEFAULT_MAX_HISTORY_CAPACITY = 3;

	/**
	 * History model. Each command class has map of executions (command instance
	 * and time)
	 */
	@SuppressWarnings("rawtypes")
	private Map<Class, CommandExecutionsMap> history = new ConcurrentHashMap<Class, CommandExecutionsMap>();

	private int maxHistoryCapacity;

	public GateHistory(int maxHistoryCapacity) {
		this.maxHistoryCapacity = maxHistoryCapacity;
	}

	public GateHistory() {
		this(DEFAULT_MAX_HISTORY_CAPACITY);
	}

	/**
	 * 
	 * @param command
	 * @return true if command is not a repetition, false if command is
	 *         repetition and should not be executed now
	 */
	public boolean register(Object command) {
		if (!isUnique(command))
			return true;

		Date lastRun = getFromHistory(command);

		// update history
		Date now = new Date();
		addToHistory(command, now);

		// first run, so go
		if (lastRun == null)
			return true;

		long uniqueStorageTimeout = getUniqueStorageTimeout(command);
		// no timeout so by default it is duplicated
		if (uniqueStorageTimeout == 0)
			return false;

		long milisFromLastRun = now.getTime() - lastRun.getTime();
		return milisFromLastRun > uniqueStorageTimeout;
	}

	private boolean isUnique(Object command) {
		if (!command.getClass().isAnnotationPresent(Command.class))
			return false;

		Command commandAnnotation = command.getClass().getAnnotation(
				Command.class);

		return commandAnnotation.unique();
	}

	private Long getUniqueStorageTimeout(Object command) {
		Command commandAnnotation = command.getClass().getAnnotation(
				Command.class);
		return commandAnnotation.uniqueStorageTimeout();
	}

	private Date getFromHistory(Object command) {
		Map<Object, Date> executions = history.get(command.getClass());
		if (executions == null)
			return null;
		return executions.get(command);
	}

	private void addToHistory(Object command, Date executeDate) {
		CommandExecutionsMap executions = history.get(command.getClass());
		if (executions == null) {
			executions = new CommandExecutionsMap();
			history.put(command.getClass(), executions);
		}
		executions.put(command, executeDate);
	}
}
```

## File: `src/main/java/pl/com/bottega/cqrs/command/impl/RunEnvironment.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.cqrs.command.impl;

import javax.inject.Inject;

import org.springframework.stereotype.Component;

import pl.com.bottega.cqrs.command.handler.CommandHandler;

/**
 * @author Slawek
 */
@Component
public class RunEnvironment {

	public interface HandlersProvider{
		CommandHandler<Object, Object> getHandler(Object command);
	}
	
	@Inject
	private HandlersProvider handlersProfiver;
	
	public Object run(Object command) {		
		CommandHandler<Object, Object> handler = handlersProfiver.getHandler(command);
		
		//You can add Your own capabilities here: dependency injection, security, transaction management, logging, profiling, spying, storing commands, etc
		
		Object result = handler.handle(command);

		//You can add Your own capabilities here
		
		return result;
	}

}
```

## File: `src/main/java/pl/com/bottega/cqrs/command/impl/StandardGate.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.cqrs.command.impl;

import javax.inject.Inject;

import org.springframework.stereotype.Component;

import pl.com.bottega.cqrs.annotations.Command;
import pl.com.bottega.cqrs.command.Gate;


@Component
public class StandardGate implements Gate {
	
	@Inject
	private RunEnvironment runEnvironment;
	
	private GateHistory gateHistory = new GateHistory();

	/* (non-Javadoc)
	 * @see pl.com.bottega.cqrs.command.impl.Gate#dispatch(java.lang.Object)
	 */
	@Override
	public Object dispatch(Object command){
		if (! gateHistory.register(command)){
			//TODO log.info(duplicate)
			return null;//skip duplicate
		}
			
		if (isAsynchronous(command)){
			//TODO add to the queue. Queue should send this command to the RunEnvironment
			return null;
		}
		
		
		return runEnvironment.run(command);
	}

	/**
	 * @param command
	 * @return
	 */
	private boolean isAsynchronous(Object command) {
		if (! command.getClass().isAnnotationPresent(Command.class))
			return false;
		
		Command commandAnnotation = command.getClass().getAnnotation(Command.class);		
		return commandAnnotation.asynchronous();		
	}

	
}
```

## File: `src/main/java/pl/com/bottega/cqrs/query/PaginatedResult.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.cqrs.query;

import java.io.Serializable;
import java.util.Collections;
import java.util.List;

@SuppressWarnings("serial")
public class PaginatedResult<T> implements Serializable {
    private final List<T> items;
    private final int pageSize;
    private final int pageNumber;
    private final int pagesCount;
    private final int totalItemsCount;

    public PaginatedResult(int pageNumber, int pageSize) {
        this.pageNumber = pageNumber;
        this.pageSize = pageSize;
        items = Collections.emptyList();
        pagesCount = 0;
        totalItemsCount = 0;
    }

    public PaginatedResult(List<T> items, int pageNumber, int pageSize, int totalItemsCount) {
        this.items = items;
        this.pageNumber = pageNumber;
        this.pageSize = pageSize;
        this.pagesCount = countPages(pageSize, totalItemsCount);
        this.totalItemsCount = totalItemsCount;
    }

    private int countPages(int size, int itemsCount) {
        return (int) Math.ceil((double) itemsCount / size);
    }

    public List<T> getItems() {
        return items;
    }

    public int getPageSize() {
        return pageSize;
    }

    public int getPageNumber() {
        return pageNumber;
    }

    public int getPagesCount() {
        return pagesCount;
    }

    public int getTotalItemsCount() {
        return totalItemsCount;
    }
}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/application/ApplicationService.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.application;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

@Component
@Retention(RetentionPolicy.RUNTIME)
@Transactional(propagation = Propagation.REQUIRED)
@Target(ElementType.TYPE)
public @interface ApplicationService {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/application/Finder.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.application;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

/**
 * @author Slawek
 * 
 */
@Service
@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface Finder {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/application/InternalApplicationService.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.application;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

@Service
@Retention(RetentionPolicy.RUNTIME)
@Transactional(propagation = Propagation.MANDATORY)
@Target(ElementType.TYPE)
public @interface InternalApplicationService {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/AggregateRoot.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface AggregateRoot {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/DomainFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Component;

@Component
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface DomainFactory {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/DomainPolicy.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Component;

@Component
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface DomainPolicy {
}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/DomainPolicyImpl.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface DomainPolicyImpl {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/DomainRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface DomainRepository {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/DomainRepositoryImpl.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Component;

@Component
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface DomainRepositoryImpl {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/DomainService.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Component;

@Component
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface DomainService {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/FinderImpl.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import org.springframework.stereotype.Component;

@Component
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface FinderImpl {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/Function.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Function {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/Invariant.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * List of Aggregate invariants implemented in method
 * 
 * @author Slawek
 *
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Invariant {

	String[] value();
}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/InvariantsList.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * list of all invariants supported by aggregate
 * @author Slawek
 *
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface InvariantsList {

	String[] value();

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/PublishedLanguage.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface PublishedLanguage {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/domain/ValueObject.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.domain;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface ValueObject {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/event/Event.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.event;

public @interface Event {

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/event/EventListener.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.event;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * @author Slawek
 * 
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface EventListener {

    boolean asynchronous() default false;

}
```

## File: `src/main/java/pl/com/bottega/ddd/annotations/event/EventListeners.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.annotations.event;

import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

import org.springframework.stereotype.Component;

/**
 * @author Slawek
 * 
 */
@Component
@Target(ElementType.TYPE)
public @interface EventListeners {

}
```

## File: `src/main/java/pl/com/bottega/ddd/support/domain/BaseAggregateRoot.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.ddd.support.domain;

import javax.inject.Inject;
import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.MappedSuperclass;
import javax.persistence.Transient;
import javax.persistence.Version;

import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sharedkernel.exceptions.DomainOperationException;

/**
 * @author Slawek
 * 
 */
@Component
@Scope("prototype")//created in domain factories, not in spring container, therefore we don't want eager creation
@MappedSuperclass
public abstract class BaseAggregateRoot {
	public static enum AggregateStatus {
		ACTIVE, ARCHIVE
	}

	@EmbeddedId
	@AttributeOverrides({
		  @AttributeOverride(name = "idValue", column = @Column(name = "aggregateId", nullable = false))})
	protected AggregateId aggregateId;

	@Version
	private Long version;

	@Enumerated(EnumType.ORDINAL)
	private AggregateStatus aggregateStatus = AggregateStatus.ACTIVE;
	
	@Transient
	@Inject
	protected DomainEventPublisher eventPublisher;
	
	public void markAsRemoved() {
		aggregateStatus = AggregateStatus.ARCHIVE;
	}

	public AggregateId getAggregateId() {
		return aggregateId;
	}

	public boolean isRemoved() {
		return aggregateStatus == AggregateStatus.ARCHIVE;
	}
	
	protected void domainError(String message) {
		throw new DomainOperationException(aggregateId, message);
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (obj instanceof BaseAggregateRoot) {
			BaseAggregateRoot other = (BaseAggregateRoot) obj;
			if (other.aggregateId == null)
				return false;
			return other.aggregateId.equals(aggregateId);
		}
		
		return false;
	}
	
	@Override
	public int hashCode() {	
		return aggregateId.hashCode();
	}
}
```

## File: `src/main/java/pl/com/bottega/ddd/support/domain/BaseEntity.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.support.domain;

import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.MappedSuperclass;

/**
 * 
 * @author Slawek
 * 
 */
@MappedSuperclass
public abstract class BaseEntity {

    @Id
    @GeneratedValue
    private Long entityId;

    public Long getEntityId() {
        return entityId;
    }
}
```

## File: `src/main/java/pl/com/bottega/ddd/support/domain/DomainEventPublisher.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ddd.support.domain;

import java.io.Serializable;

public interface DomainEventPublisher {
    void publish(Serializable event);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/businessprocess/ordertracking/OrderShipmentStatusTrackerData.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.businessprocess.ordertracking;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@Entity
public class OrderShipmentStatusTrackerData {

    @Id
    @GeneratedValue
    private Long id;

    @AttributeOverrides({
		@AttributeOverride(name = "aggregateId", column = @Column(name = "orderId"))})
    private AggregateId orderId;

    @AttributeOverrides({
		@AttributeOverride(name = "aggregateId", column = @Column(name = "shipmentId"))})
    private AggregateId shipmentId;

    private Boolean shipmentReceived = false;

    public AggregateId getOrderId() {
        return orderId;
    }

    /**
     * Id of order aggregate.
     */
    public void setOrderId(AggregateId orderId) {
        this.orderId = orderId;
    }

    /**
     * Id of shipment aggregate (from shipment module) once it's created.
     */
    public AggregateId getShipmentId() {
        return shipmentId;
    }

    public void setShipmentId(AggregateId shipmentId) {
        this.shipmentId = shipmentId;
    }

    public Boolean getShipmentReceived() {
        return shipmentReceived;
    }

    public void setShipmentReceived(Boolean shipmentReceived) {
        this.shipmentReceived = shipmentReceived;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/businessprocess/ordertracking/OrderShipmentStatusTrackerSaga.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.businessprocess.ordertracking;

import javax.inject.Inject;

import pl.com.bottega.ecommerce.canonicalmodel.events.OrderSubmittedEvent;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderFinder;
import pl.com.bottega.ecommerce.shipping.domain.events.OrderShippedEvent;
import pl.com.bottega.ecommerce.shipping.domain.events.ShipmentDeliveredEvent;
import pl.com.bottega.ecommerce.system.saga.SagaInstance;
import pl.com.bottega.ecommerce.system.saga.annotations.Saga;
import pl.com.bottega.ecommerce.system.saga.annotations.SagaAction;

@Saga
public class OrderShipmentStatusTrackerSaga extends SagaInstance<OrderShipmentStatusTrackerData> {

    @Inject
    private OrderFinder orderFinder;

    @SagaAction
    public void handleOrderCreated(OrderSubmittedEvent event) {
        data.setOrderId(event.getOrderId());
        completeIfPossible();
    }

    @SagaAction
    public void orderShipped(OrderShippedEvent event) {
        data.setOrderId(event.getOrderId());
        data.setShipmentId(event.getShipmentId());
        completeIfPossible();
    }
    
    @SagaAction
    public void shipmentDelivered(ShipmentDeliveredEvent event) {
        data.setShipmentId(event.getShipmentId());
        data.setShipmentReceived(true);
        completeIfPossible();
    }

    private void completeIfPossible() {
        if (data.getOrderId() != null && data.getShipmentId() != null && data.getShipmentReceived()) {
            //TODO move process forward, ex call service or publish event
        	
            markAsCompleted();
        }
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/businessprocess/ordertracking/OrderShipmentStatusTrackerSagaManager.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.businessprocess.ordertracking;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.Query;

import org.springframework.stereotype.Component;

import pl.com.bottega.ecommerce.canonicalmodel.events.OrderSubmittedEvent;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.shipping.domain.events.OrderShippedEvent;
import pl.com.bottega.ecommerce.shipping.domain.events.ShipmentDeliveredEvent;
import pl.com.bottega.ecommerce.system.saga.SagaManager;
import pl.com.bottega.ecommerce.system.saga.annotations.LoadSaga;

@Component
public class OrderShipmentStatusTrackerSagaManager implements
        SagaManager<OrderShipmentStatusTrackerSaga, OrderShipmentStatusTrackerData> {

    @PersistenceContext
    private EntityManager entityManager;

    @LoadSaga
    public OrderShipmentStatusTrackerData loadSaga(OrderSubmittedEvent event) {
        return findByOrderId(event.getOrderId());
    }

    @LoadSaga
    public OrderShipmentStatusTrackerData loadSaga(OrderShippedEvent event) {
        return findByOrderId(event.getOrderId());
    }

    @LoadSaga
    public OrderShipmentStatusTrackerData loadSaga(ShipmentDeliveredEvent event) {
        return findByShipmentId(event.getShipmentId());
    }

    private OrderShipmentStatusTrackerData findByOrderId(AggregateId orderId) {
        Query query = entityManager.createQuery("from OrderShipmentStatusTrackerData where orderId=:orderId")
                .setParameter("orderId", orderId);
        return (OrderShipmentStatusTrackerData) query.getSingleResult();
    }

    private OrderShipmentStatusTrackerData findByShipmentId(AggregateId shipmentId) {
        Query query = entityManager.createQuery("from OrderShipmentStatusTrackerData where shipmentId=:shipmentId")
                .setParameter("shipmentId", shipmentId);
        return (OrderShipmentStatusTrackerData) query.getSingleResult();
    }

    @Override
    public void removeSaga(OrderShipmentStatusTrackerSaga saga) {
        OrderShipmentStatusTrackerData sagaData = entityManager.merge(saga.getData());
        entityManager.remove(sagaData);
    }

    @Override
    public OrderShipmentStatusTrackerData createNewSagaData() {
        OrderShipmentStatusTrackerData sagaData = new OrderShipmentStatusTrackerData();
        entityManager.persist(sagaData);
        return sagaData;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/canonicalmodel/events/ClientPaidEvent.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.ecommerce.canonicalmodel.events;

import java.io.Serializable;

import pl.com.bottega.ddd.annotations.event.Event;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * @author Slawek
 * 
 */
@SuppressWarnings("serial")
@Event
public class ClientPaidEvent implements Serializable {

    private final AggregateId paymentId;
    private ClientData clientData;
    private Money amount;
    
    
    public ClientPaidEvent(AggregateId paymentId, ClientData clientData, Money amount) {
        this.paymentId = paymentId;
        this.clientData = clientData;
        this.amount = amount;
    }

	public AggregateId getPaymentId() {
		return paymentId;
	}
	
	public ClientData getClientData() {
		return clientData;
	}
	
	public Money getAmount() {
		return amount;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/canonicalmodel/events/CustomerStatusChangedEvent.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.ecommerce.canonicalmodel.events;

import java.io.Serializable;

import pl.com.bottega.ddd.annotations.event.Event;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.crm.domain.Customer.CustomerStatus;

/**
 * @author Slawek
 * 
 */
@SuppressWarnings("serial")
@Event
public class CustomerStatusChangedEvent implements Serializable {

    private final AggregateId customerId;
    private final CustomerStatus status;

    public CustomerStatusChangedEvent(AggregateId customerId, CustomerStatus status) {
        this.customerId = customerId;
        this.status = status;
    }

    public AggregateId getCustomerId() {
        return customerId;
    }

    public CustomerStatus getStatus() {
        return status;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/canonicalmodel/events/OrderSubmittedEvent.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.canonicalmodel.events;

import java.io.Serializable;

import pl.com.bottega.ddd.annotations.event.Event;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@SuppressWarnings("serial")
@Event
public class OrderSubmittedEvent implements Serializable{

	private AggregateId orderId;
	
	public OrderSubmittedEvent(AggregateId orderId){
		this.orderId = orderId;
	}
	
	public AggregateId getOrderId() {
		return orderId;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/canonicalmodel/events/PaymentRolledBackEvent.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.canonicalmodel.events;

import java.io.Serializable;

import pl.com.bottega.ddd.annotations.event.Event;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@SuppressWarnings("serial")
@Event
public class PaymentRolledBackEvent implements Serializable{

	private AggregateId paymentId;
	
	public PaymentRolledBackEvent(AggregateId paymentId){
		this.paymentId = paymentId;
	}
	
	public AggregateId getPaymentId() {
		return paymentId;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/canonicalmodel/publishedlanguage/AggregateId.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage;

import java.io.Serializable;
import java.util.UUID;

import javax.persistence.Embeddable;

import org.apache.commons.lang3.Validate;

@SuppressWarnings("serial")
@Embeddable
public class AggregateId implements Serializable{

	private String aggregateId;

	public AggregateId(String aggregateId) {
		Validate.notNull(aggregateId);
		this.aggregateId = aggregateId;
	}

	protected AggregateId() {
	}
	
	public static AggregateId generate(){
		return new AggregateId(UUID.randomUUID().toString());
	}

	public String getId() {
		return aggregateId;
	}

	@Override
	public int hashCode() {
		return aggregateId.hashCode();
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		AggregateId other = (AggregateId) obj;
		if (aggregateId == null) {
			if (other.aggregateId != null)
				return false;
		} else if (!aggregateId.equals(other.aggregateId))
			return false;
		return true;
	}

	@Override
	public String toString() {
		return aggregateId;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/canonicalmodel/publishedlanguage/ClientData.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Embeddable;
import javax.persistence.Embedded;

import pl.com.bottega.ddd.annotations.domain.ValueObject;

/**
 * Client's snapshot
 * 
 * @author Slawek
 */
@ValueObject
@Embeddable
public class ClientData {
	
	@Embedded
	@AttributeOverrides({
			  @AttributeOverride(name = "aggregateId", column = @Column(name = "clientId", nullable = false))})
	private AggregateId aggregateId;
	
	private String name;

	@SuppressWarnings("unused")
	private ClientData(){}
	
	public ClientData(AggregateId aggregateId, String name) {
		this.aggregateId = aggregateId;
		this.name = name;
	}
	
	public AggregateId getAggregateId() {
		return aggregateId;
	}
	
	public String getName() {
		return name;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/crm/application/commands/ChangeCustomerStatusCommand.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.ecommerce.crm.application.commands;

import java.io.Serializable;

import pl.com.bottega.cqrs.annotations.Command;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.crm.domain.Customer.CustomerStatus;

/**
 * @author Slawek
 *
 */
@SuppressWarnings("serial")
@Command
public class ChangeCustomerStatusCommand implements Serializable{

	private AggregateId customerId;
	
	private CustomerStatus status;

	public ChangeCustomerStatusCommand(AggregateId customerId, CustomerStatus status) {
		super();
		this.customerId = customerId;
		this.status = status;
	}

	public AggregateId getCustomerId() {
		return customerId;
	}

	public CustomerStatus getStatus() {
		return status;
	}
	
	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/crm/domain/Customer.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.ecommerce.crm.domain;

import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;

import pl.com.bottega.ddd.annotations.domain.AggregateRoot;
import pl.com.bottega.ddd.support.domain.BaseAggregateRoot;
import pl.com.bottega.ecommerce.canonicalmodel.events.CustomerStatusChangedEvent;

/**
 * @author Slawek
 *
 */
@Entity
@AggregateRoot
public class Customer extends BaseAggregateRoot{

	public enum CustomerStatus{
		STANDARD, VIP, PLATINUM
	}
	
	@Enumerated(EnumType.STRING)
	private CustomerStatus status;
	
	
	public void changeStatus(CustomerStatus status){
		if (status.equals(this.status))
			return;
		
		this.status = status;
		
		//Sample Case: give 10% rebate for all draft orders - communication via events with different Bounded Context to achieve decoupling
		eventPublisher.publish(new CustomerStatusChangedEvent(getAggregateId(), status));
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/crm/domain/CustomerRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.ecommerce.crm.domain;

import pl.com.bottega.ddd.annotations.domain.DomainRepository;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

/**
 * @author Slawek
 * 
 */
@DomainRepository
public interface CustomerRepository {

	public Customer load(AggregateId id);

	public void save(Customer entity);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/application/impl/OrderingServiceImpl.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.application.impl;

import javax.inject.Inject;

import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Transactional;

import pl.com.bottega.ddd.annotations.application.ApplicationService;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sales.application.api.command.OrderDetailsCommand;
import pl.com.bottega.ecommerce.sales.application.api.service.OfferChangedExcpetion;
import pl.com.bottega.ecommerce.sales.application.api.service.OrderingService;
import pl.com.bottega.ecommerce.sales.domain.client.Client;
import pl.com.bottega.ecommerce.sales.domain.client.ClientRepository;
import pl.com.bottega.ecommerce.sales.domain.equivalent.SuggestionService;
import pl.com.bottega.ecommerce.sales.domain.offer.DiscountFactory;
import pl.com.bottega.ecommerce.sales.domain.offer.DiscountPolicy;
import pl.com.bottega.ecommerce.sales.domain.offer.Offer;
import pl.com.bottega.ecommerce.sales.domain.payment.Payment;
import pl.com.bottega.ecommerce.sales.domain.payment.PaymentRepository;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.Product;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductRepository;
import pl.com.bottega.ecommerce.sales.domain.purchase.Purchase;
import pl.com.bottega.ecommerce.sales.domain.purchase.PurchaseFactory;
import pl.com.bottega.ecommerce.sales.domain.purchase.PurchaseRepository;
import pl.com.bottega.ecommerce.sales.domain.reservation.Reservation;
import pl.com.bottega.ecommerce.sales.domain.reservation.ReservationFactory;
import pl.com.bottega.ecommerce.sales.domain.reservation.ReservationRepository;
import pl.com.bottega.ecommerce.sharedkernel.exceptions.DomainOperationException;
import pl.com.bottega.ecommerce.system.application.SystemContext;

/**
 * Ordering Use Case steps<br>
 * Each step is a Domain Story<br>
 * <br>
 * Notice that application language is different (simpler) than domain language, ex: we don'nt want to exposure domain concepts like Purchase and Reservation to the upper layers, we hide them under the Order term  
 * <br>
 * Technically App Service is just a bunch of procedures, therefore OO principles (ex: CqS, SOLID, GRASP) does not apply here  
 *
 * @author Slawek
 */
@ApplicationService
public class OrderingServiceImpl implements OrderingService {

	@Inject
	private SystemContext systemContext;
	
	@Inject
	private ClientRepository clientRepository;

	@Inject
	private ReservationRepository reservationRepository;

	@Inject
	private ReservationFactory reservationFactory;

	@Inject
	private PurchaseFactory purchaseFactory;

	@Inject
	private PurchaseRepository purchaseRepository;
	
	@Inject
	private ProductRepository productRepository;
	
	@Inject 
	private PaymentRepository paymentRepository;

	@Inject
	private DiscountFactory discountFactory;
	
	@Inject
	private SuggestionService suggestionService;

	// @Secured requires BUYER role
	public AggregateId createOrder() {
		Reservation reservation = reservationFactory.create(loadClient());
		reservationRepository.save(reservation);
		return reservation.getAggregateId();
	}

	/**
	 * DOMAIN STORY<br>
	 * try to read this as a full sentence, this way: subject.predicate(completion)<br>
	 * <br>
	 * Load reservation by orderId<br>
	 * Load product by productId<br>
	 * Check if product is not available<br>
	 * -if so, than suggest equivalent for that product based on client<br>
	 * Reservation add product by given quantity
	 */
	@Override
	public void addProduct(AggregateId orderId, AggregateId productId,
			int quantity) {
		Reservation reservation = reservationRepository.load(orderId);
		
		Product product = productRepository.load(productId);
		
		if (! product.isAvailabe()){
			Client client = loadClient();	
			product = suggestionService.suggestEquivalent(product, client);
		}
			
		reservation.add(product, quantity);
		
		reservationRepository.save(reservation);
	}
	
	/**
	 * Can be invoked many times for the same order (with different params).<br>
	 * Offer VO is not stored in the Repo, it is stored on the Client Tier instead.
	 */
	public Offer calculateOffer(AggregateId orderId) {
		Reservation reservation = reservationRepository.load(orderId);

		DiscountPolicy discountPolicy = discountFactory.create(loadClient());
		
		/*
		 * Sample pattern: Aggregate generates Value Object using function<br>
		 * Higher order function is closured by policy
		 */
		return reservation.calculateOffer(discountPolicy);
	}

	/**
	 * DOMAIN STORY<br>
	 * try to read this as a full sentence, this way: subject.predicate(completion)<br>
	 * <br>
	 * Load reservation by orderId<br>
	 * Check if reservation is closed - if so, than Error<br>
	 * Generate new offer from reservation using discount created per client<br>
	 * Check if new offer is not the same as seen offer using delta = 5<br>
	 * Create purchase per client based on seen offer<br>
	 * Check if client can not afford total cost of purchase - if so, than Error<br>
	 * Confirm purchase<br>
	 * Close reservation<br>
	 */
	@Override
	@Transactional(isolation = Isolation.SERIALIZABLE)//highest isolation needed because of manipulating many Aggregates
	public void confirm(AggregateId orderId, OrderDetailsCommand orderDetailsCommand, Offer seenOffer)
			throws OfferChangedExcpetion {
		Reservation reservation = reservationRepository.load(orderId);
		if (reservation.isClosed())
			throw new DomainOperationException(reservation.getAggregateId(), "reservation is already closed");
		
		/*
		 * Sample pattern: Aggregate generates Value Object using function<br>
		 * Higher order function is closured by policy
		 */
		Offer newOffer = reservation.calculateOffer(
									discountFactory.create(loadClient()));
		
		/*
		 * Sample pattern: Client Tier sends back old VOs, Server generates new VOs based on Aggregate state<br>
		 * Notice that this VO is not stored in Repo, it's stored on the Client Tier. 
		 */
		if (! newOffer.sameAs(seenOffer, 5))//TODO load delta from conf.
			throw new OfferChangedExcpetion(reservation.getAggregateId(), seenOffer, newOffer);
		
		Client client = loadClient();//create per logged client, not reservation owner					
		Purchase purchase = purchaseFactory.create(reservation.getAggregateId(), client, seenOffer);
				
		if (! client.canAfford(purchase.getTotalCost()))
			throw new DomainOperationException(client.getAggregateId(), "client has insufficent money");
		
		purchaseRepository.save(purchase);//Aggregate must be managed by persistence context before firing events (synchronous listeners may need to load it) 
		
		/*
		 * Sample model where one aggregate creates another. Client does not manage payment lifecycle, therefore application must manage it. 
		 */
		Payment payment = client.charge(purchase.getTotalCost());
		paymentRepository.save(payment);
		
		purchase.confirm();	
		reservation.close();				
		
		reservationRepository.save(reservation);
		clientRepository.save(client);
		
	}
	
	private Client loadClient() {
		return clientRepository.load(systemContext.getSystemUser().getClientId());
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/application/listeners/ClientStatusChangedListener.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.application.listeners;

import javax.inject.Inject;

import pl.com.bottega.cqrs.query.PaginatedResult;
import pl.com.bottega.ddd.annotations.event.EventListener;
import pl.com.bottega.ddd.annotations.event.EventListeners;
import pl.com.bottega.ecommerce.canonicalmodel.events.CustomerStatusChangedEvent;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sales.application.internal.discounts.DiscountingService;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderDto;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderFinder;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderQuery;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * Sample Anti-corruption Layer: translates Customer-Client vocabulary
 * <br>
 * Applies discount 
 * 
 * @author Slawek
 *
 */
@EventListeners
public class ClientStatusChangedListener {

	@Inject
	private DiscountingService discountingService;
	@Inject
	private OrderFinder orderFinder;
	
	@EventListener
	public void handle(CustomerStatusChangedEvent event){
		OrderQuery orderQuery = new OrderQuery(null, event.getCustomerId());
		PaginatedResult<OrderDto> orders = orderFinder.query(orderQuery);
		
		Money discount = calculateDiscout(event.getCustomerId());
		
		for(OrderDto dto : orders.getItems()){
			discountingService.applyDiscount(dto.getOrderId(), discount);
		}
	}

	private Money calculateDiscout(AggregateId customerId) {
		// TODO explore domain rules
		return new Money(10);
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/client/Client.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.client;

import javax.inject.Inject;
import javax.persistence.Entity;
import javax.persistence.Transient;

import pl.com.bottega.ddd.annotations.domain.AggregateRoot;
import pl.com.bottega.ddd.support.domain.BaseAggregateRoot;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;
import pl.com.bottega.ecommerce.sales.domain.payment.Payment;
import pl.com.bottega.ecommerce.sales.domain.payment.PaymentFactory;
import pl.com.bottega.ecommerce.sharedkernel.Money;

@Entity
@AggregateRoot
public class Client extends BaseAggregateRoot{

	private String name;
	
	@Inject
	@Transient
	private PaymentFactory paymentFactory;
	
	public ClientData generateSnapshot(){
		return new ClientData(aggregateId, name);
	}

	public boolean canAfford(Money amount) {		
		return true;//TODO explore domain rules ex: credit limit
	}

	/**
	 * Sample model: one aggregate creates another.<br>
	 * Client model does not compose Payment - therefore it does not manage Payment lifecycle.<br>
	 * Application layer is responsible for managing Payment lifecycle;
	 * 
	 * @param amount
	 * @return
	 */
	public Payment charge(Money amount) {
		if (! canAfford(amount)){			
			domainError("Can not afford: " + amount);
		}
		// TODO facade to the payment module
		
		return paymentFactory.createPayment(generateSnapshot(), amount);
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/client/ClientRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.client;

import pl.com.bottega.ddd.annotations.domain.DomainRepository;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@DomainRepository
public interface ClientRepository {

	public Client load(AggregateId id);

	public void save(Client client);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/equivalent/ProductSpecificationFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.equivalent;

import pl.com.bottega.ddd.annotations.domain.DomainFactory;
import pl.com.bottega.ecommerce.sales.domain.client.Client;
import pl.com.bottega.ecommerce.sales.domain.equivalent.specification.SameCategory;
import pl.com.bottega.ecommerce.sales.domain.equivalent.specification.SimilarName;
import pl.com.bottega.ecommerce.sales.domain.equivalent.specification.SimilarPrice;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.Product;
import pl.com.bottega.ecommerce.sharedkernel.Money;
import pl.com.bottega.ecommerce.sharedkernel.specification.DisjunctionSpecification;
import pl.com.bottega.ecommerce.sharedkernel.specification.Specification;

@DomainFactory
public class ProductSpecificationFactory {

	@SuppressWarnings("unchecked")
	public Specification<Product> create(Client client,
			Product problematicProduct) {
		// TODO explore domain rules, maybe use genetic algorithm to breed spec;)
		return new DisjunctionSpecification<Product>(
					new SimilarPrice(problematicProduct.getPrice(), generateAcceptableDifference(client)), 
					new SimilarName(problematicProduct.getName()),
					new SameCategory(problematicProduct.getProductType()));
	}

	private Money generateAcceptableDifference(Client client) {
		// TODO explore rules
		return new Money(7);
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/equivalent/SuggestionService.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.equivalent;

import java.util.List;

import javax.inject.Inject;

import pl.com.bottega.ddd.annotations.domain.DomainService;
import pl.com.bottega.ecommerce.sales.domain.client.Client;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.Product;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductRepository;
import pl.com.bottega.ecommerce.sales.readmodel.offer.Offer;
import pl.com.bottega.ecommerce.sharedkernel.specification.Specification;

/**
 * Sample Decision Support feature: suggests equivalent of the product based on client's habits. 
 * 
 * @author Slawek
 *
 */
@DomainService
public class SuggestionService {

	@Inject
	private ProductRepository productRepository;
	
	@Inject
	private Offer offer;
	
	@Inject
	private ProductSpecificationFactory productSpecificationFactory;
	
	public Product suggestEquivalent(Product problematicProduct, Client client) {
		List<Product> expiringProducts = productRepository.findProductWhereBestBeforeExpiredIn(5);
		
		Specification<Product> specification = productSpecificationFactory.create(client, problematicProduct);
		
		for (Product suggestedProduct : expiringProducts) {
			if (specification.isSatisfiedBy(suggestedProduct))
				return suggestedProduct;
		}
		
		return null;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/BookKeeper.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import javax.inject.Inject;

import pl.com.bottega.ddd.annotations.domain.DomainService;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductRepository;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * Sample Domain Service that contains logic that:
 * <ul>
 * <li> Does not have a natural place in any aggregate - we don't want to bloat Order with issuance of the Invoice
 * <li> Has broad dependencies - we don't want Order to become a 'God Class'
 * <li> Is used only (or not many) in one Use Case/user Story so is not essential for any Aggregate
 * <ul>
 * 
 * Notice that this Domain Service is managed by Container in order to be able to inject dependencies like Repo  
 * 
 * @author Slawek
 *
 */
@DomainService
public class BookKeeper {
	
	@Inject
	private ProductRepository productRepository;
	
	@Inject
	private InvoiceFactory invoiceFactory;
	
	public Invoice issuance(InvoiceRequest invoiceRequest, TaxPolicy taxPolicy){
		Invoice invoice = invoiceFactory.create(invoiceRequest.getClientData());
		
		for (RequestItem item : invoiceRequest.getItems()){
			Money net = item.getTotalCost();			
			Tax tax = taxPolicy.calculateTax(item.getProductData().getType(), net);			
						
			InvoiceLine invoiceLine = new InvoiceLine(item.getProductData(), item.getQuantity(), net, tax);			
			invoice.addItem(invoiceLine);
		}
		
		return invoice;
	}
	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/Invoice.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;

import org.hibernate.annotations.Fetch;
import org.hibernate.annotations.FetchMode;

import pl.com.bottega.ddd.annotations.domain.AggregateRoot;
import pl.com.bottega.ddd.support.domain.BaseAggregateRoot;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * 
 * @author Slawek
 * 
 */
@AggregateRoot
@Entity
public class Invoice extends BaseAggregateRoot {

	@Embedded
	private ClientData client;

	@Embedded
	@AttributeOverrides({
			@AttributeOverride(name = "denomination", column = @Column(name = "net_denomination")),
			@AttributeOverride(name = "currencyCode", column = @Column(name = "net_currencyCode")) })
	private Money net;

	@Embedded
	@AttributeOverrides({
		@AttributeOverride(name = "denomination", column = @Column(name = "gros_denomination")),
		@AttributeOverride(name = "currencyCode", column = @Column(name = "gros_currencyCode")) })
	private Money gros;

	@OneToMany(cascade = CascadeType.ALL, fetch = FetchType.EAGER, orphanRemoval = true)
	@JoinColumn(name = "invoiceId")
	@Fetch(FetchMode.JOIN)
	private List<InvoiceLine> items;

	Invoice(AggregateId invoiceId, ClientData client) {
		this.aggregateId = invoiceId;
		this.client = client;
		this.items = new ArrayList<InvoiceLine>();
		
		this.net = Money.ZERO;
		this.gros = Money.ZERO;
	}
	
	/**
	 * For JPA Only
	 */
	@SuppressWarnings("unused")
	private Invoice(){}

	public void addItem(InvoiceLine item) {
		items.add(item);

		net = net.add(item.getNet());
		gros = gros.add(item.getGros());
	}

	/**
	 * 
	 * @return immutable projection
	 */
	public List<InvoiceLine> getItems() {
		return Collections.unmodifiableList(items);
	}

	public ClientData getClient() {
		return client;
	}

	public Money getNet() {
		return net;
	}

	public Money getGros() {
		return gros;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import javax.inject.Inject;

import org.springframework.beans.factory.config.AutowireCapableBeanFactory;

import pl.com.bottega.ddd.annotations.domain.DomainFactory;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;

/**
 * 
 * @author Slawek
 *
 */
@DomainFactory
public class InvoiceFactory {

	@Inject
	private AutowireCapableBeanFactory spring;
	
	public Invoice create(ClientData client){
		Invoice invoice = new Invoice(AggregateId.generate(), client);
		spring.autowireBean(invoice);
		return invoice;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceLine.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Embedded;
import javax.persistence.Entity;

import pl.com.bottega.ddd.support.domain.BaseEntity;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * @author Slawek
 *
 */
@Entity
public class InvoiceLine extends BaseEntity{
		
	@Embedded
	private ProductData product;
	
	private int quantity;
	
	@Embedded
	@AttributeOverrides({
		@AttributeOverride(name = "denomination", column = @Column(name = "net_denomination")),
		@AttributeOverride(name = "currencyCode", column = @Column(name = "net_currencyCode")) })
	private Money net;
	
	@Embedded
	@AttributeOverrides({
		@AttributeOverride(name = "denomination", column = @Column(name = "gros_denomination")),
		@AttributeOverride(name = "currencyCode", column = @Column(name = "gros_currencyCode")) })
	private Money gros;
	
	@Embedded
	private Tax tax;

	/**
	 * JPA only
	 */
	public InvoiceLine(){}
	

	InvoiceLine(ProductData product, int quantity, Money net, Tax tax) {
		this.product = product;
		this.quantity = quantity;
		this.net = net;
		this.tax = tax;
		
		this.gros = net.add(tax.getAmount());	
	}

	public ProductData getProduct() {
		return product;
	}

	public int getQuantity() {
		return quantity;
	}

	public Money getNet() {
		return net;
	}

	public Money getGros() {
		return gros;
	}
	
	public Tax getTax(){
		return tax;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import pl.com.bottega.ddd.annotations.domain.DomainRepository;

/**
 * 
 * @author Slawek
 *
 */
@DomainRepository
public interface InvoiceRepository {

	/**
	 * @param invoice
	 */
	public void save(Invoice invoice);

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceRequest.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;

@ValueObject
public class InvoiceRequest {

	private ClientData client;	
	private List<RequestItem> items = new ArrayList<RequestItem>();
	
	public InvoiceRequest(ClientData client){
		this.client = client;
	}
	
	public void add(RequestItem item){
		items.add(item);
	}
	
	public ClientData getClient() {
		return client;
	}
	
	public Collection<RequestItem> getItems() {
		return Collections.unmodifiableCollection(items);
	}

	public ClientData getClientData() {
		return client;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/InvoiceRequestFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import pl.com.bottega.ddd.annotations.domain.DomainFactory;
import pl.com.bottega.ecommerce.sales.domain.client.Client;
import pl.com.bottega.ecommerce.sales.domain.purchase.Purchase;
import pl.com.bottega.ecommerce.sales.domain.purchase.PurchaseItem;
import pl.com.bottega.ecommerce.sharedkernel.exceptions.DomainOperationException;

@DomainFactory
public class InvoiceRequestFactory {

	public InvoiceRequest create(Client client, Purchase... purchases) {
		InvoiceRequest request = new InvoiceRequest(client.generateSnapshot());
		
		for (Purchase purchase : purchases) {
			if (! purchase.isPaid())
				throw new DomainOperationException(purchase.getAggregateId(), "Purchase is not paid");
			
			for (PurchaseItem item : purchase.getItems()) {
				request.add(new RequestItem(item.getProductData(), item.getQuantity(), item.getTotalCost()));
			}
		}
		
		return request;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/RequestItem.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

@ValueObject
class RequestItem {

	private ProductData productData;
	
	private int quantity;
	
	private Money totalCost;
	
	public RequestItem(ProductData productData, int quantity, Money totalCost) {
		this.productData = productData;
		this.quantity = quantity;
		this.totalCost = totalCost;
	}

	public Money getTotalCost() {
		return totalCost;
	}

	public ProductData getProductData() {
		return productData;
	}

	public int getQuantity() {
		return quantity;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/Tax.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Embeddable;
import javax.persistence.Embedded;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * 
 * @author Slawek
 *
 */
@Embeddable
@ValueObject
public class Tax {
	
	@Embedded
	@AttributeOverrides({
		@AttributeOverride(name = "denomination", column = @Column(name = "tax_denomination")),
		@AttributeOverride(name = "currencyCode", column = @Column(name = "tax_currencyCode")) })
	private Money amount;

	private String description;
	
	/**
	 * For JPA only
	 */
	public Tax(){}
	
	public Tax(Money amount, String description) {
		super();
		this.amount = amount;
		this.description = description;
	}

	public Money getAmount() {
		return amount;
	}

	public String getDescription() {
		return description;
	}

	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/TaxAdvisor.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import pl.com.bottega.ddd.annotations.domain.DomainService;
import pl.com.bottega.ecommerce.sales.domain.client.Client;
import pl.com.bottega.ecommerce.sales.domain.invoicing.tax.DefaultTaxPolicy;

@DomainService
public class TaxAdvisor {

	public TaxPolicy suggestBestTax(Client client){
		//TODO explore domain rules
		return new DefaultTaxPolicy();
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/invoicing/TaxPolicy.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.invoicing;

import pl.com.bottega.ddd.annotations.domain.DomainPolicy;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductType;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * Sample Policy
 * 
 * @author Slawek
 *
 */
@DomainPolicy
public interface TaxPolicy {	

	/**
	 * calculates tax per product type based on net value
	 * @param productType
	 * @param net
	 * @return
	 */
	public Tax calculateTax(ProductType productType, Money net);

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/Discount.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.offer;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ecommerce.sharedkernel.Money;

@ValueObject
public class Discount {

	private String cause;
	
	private Money value;

	public Discount(String cause, Money value) {
		this.cause = cause;
		this.value = value;
	}
	
	public String getCause() {
		return cause;
	}
	
	public Money getValue() {
		return value;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((cause == null) ? 0 : cause.hashCode());
		result = prime * result + ((value == null) ? 0 : value.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Discount other = (Discount) obj;
		if (cause == null) {
			if (other.cause != null)
				return false;
		} else if (!cause.equals(other.cause))
			return false;
		if (value == null) {
			if (other.value != null)
				return false;
		} else if (!value.equals(other.value))
			return false;
		return true;
	}
	
	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/DiscountFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.offer;

import pl.com.bottega.ddd.annotations.domain.DomainFactory;
import pl.com.bottega.ecommerce.sales.domain.client.Client;
import pl.com.bottega.ecommerce.sales.domain.offer.discounts.QuantityDiscount;

@DomainFactory
public class DiscountFactory {

	public DiscountPolicy create(Client client) {
		// TODO explore domain rules
		return new QuantityDiscount(20, 3);//20% for over 3 items
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/DiscountPolicy.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.offer;

import pl.com.bottega.ddd.annotations.domain.DomainPolicy;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.Product;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * trivial discounting sample
 *  
 * @author Slawek
 */
@DomainPolicy
public interface DiscountPolicy {

	public Discount applyDiscount(Product product, int quantity, Money reularCost);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/Offer.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.offer;

import java.util.ArrayList;
import java.util.List;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

/**
 * Offer that is available per client (including availability and discounts)
 *   
 * @author Slawek
 *
 */
@ValueObject
public class Offer {

	private List<OfferItem> availabeItems = new ArrayList<OfferItem>();
	
	private List<OfferItem> unavailableItems = new ArrayList<OfferItem>();
	
	
	public Offer(List<OfferItem> availabeItems, List<OfferItem> unavailableItems) {
		this.availabeItems = availabeItems;
		this.unavailableItems = unavailableItems;
	}

	public List<OfferItem> getAvailabeItems() {
		return availabeItems;
	}
	
	public List<OfferItem> getUnavailableItems() {
		return unavailableItems;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result
				+ ((availabeItems == null) ? 0 : availabeItems.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Offer other = (Offer) obj;
		if (availabeItems == null) {
			if (other.availabeItems != null)
				return false;
		} else if (!availabeItems.equals(other.availabeItems))
			return false;
		return true;
	}

	/**
	 * 
	 * @param seenOffer
	 * @param delta acceptable difference in percent
	 * @return
	 */
	public boolean sameAs(Offer seenOffer, double delta) {
		if (! (availabeItems.size() == seenOffer.availabeItems.size()))
			return false;
		
		for (OfferItem item : availabeItems) {
			OfferItem sameItem = seenOffer.findItem(item.getProductData().getProductId());
			if (sameItem == null)
				return false;
			if (!sameItem.sameAs(item, delta))
				return false;
		}
		
		return true;
	}

	private OfferItem findItem(AggregateId productId) {
		for (OfferItem item : availabeItems){
			if (item.getProductData().getProductId().equals(productId))
				return item;
		}
		return null;
	}
	
	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/offer/OfferItem.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.offer;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

@ValueObject
public class OfferItem {

	private ProductData productData;
	
	private int quantity;
	
	private Discount discount;
	
	private Money totalCost;
	

	public OfferItem(ProductData productData, int quantity) {
		this(productData, quantity, null);
	}
	
	public OfferItem(ProductData productData, int quantity, Discount discount) {
		this.productData = productData;
		this.quantity = quantity;
		this.discount = discount;
		
		Money discountValue = Money.ZERO;
		if (discount != null)
			 discountValue =  discountValue.subtract(discount.getValue());
		
		this.totalCost = productData.getPrice().multiplyBy(quantity).subtract(discountValue);
	}

	public ProductData getProductData() {
		return productData;
	}

	public Money getTotalCost() {
		return totalCost;
	}

	public Discount getDiscount() {
		return discount;
	}
	
	public int getQuantity() {
		return quantity;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result
				+ ((discount == null) ? 0 : discount.hashCode());
		result = prime * result
				+ ((productData == null) ? 0 : productData.hashCode());
		result = prime * result + quantity;
		result = prime * result
				+ ((totalCost == null) ? 0 : totalCost.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		OfferItem other = (OfferItem) obj;
		if (discount == null) {
			if (other.discount != null)
				return false;
		} else if (!discount.equals(other.discount))
			return false;
		if (productData == null) {
			if (other.productData != null)
				return false;
		} else if (!productData.equals(other.productData))
			return false;
		if (quantity != other.quantity)
			return false;
		if (totalCost == null) {
			if (other.totalCost != null)
				return false;
		} else if (!totalCost.equals(other.totalCost))
			return false;
		return true;
	}

	/**
	 * 
	 * @param item
	 * @param delta acceptable percentage difference 
	 * @return
	 */
	public boolean sameAs(OfferItem item, double delta) {
		if (! productData.equals(item.productData))
			return false;
		
		if (quantity != item.quantity)
			return false;
		
		
		Money max, min;
		if (totalCost.greaterThan(item.totalCost)){
			max = totalCost;
			min = item.totalCost;
		}
		else{
			max = item.totalCost;
			min = totalCost;
		}
		
		Money difference = max.subtract(min);
		Money acceptableDelta = max.multiplyBy(delta / 100); 
		
		return acceptableDelta.greaterThan(difference);
	}

	
	


}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/payment/Payment.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.payment;

import javax.inject.Inject;
import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.Transient;

import pl.com.bottega.ddd.annotations.domain.AggregateRoot;
import pl.com.bottega.ddd.support.domain.BaseAggregateRoot;
import pl.com.bottega.ecommerce.canonicalmodel.events.PaymentRolledBackEvent;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * 
 * @author Slawek
 *
 */
@AggregateRoot
@Entity
public class Payment extends BaseAggregateRoot{

	@Embedded
	private ClientData clientData;
	
	@Embedded
	private Money amount;
	
	@Transient
	@Inject
	private PaymentFactory paymentFactory;
	
	@SuppressWarnings("unused")
	private Payment(){}
	
	Payment(AggregateId aggregateId, ClientData clientData, Money amount) {
		this.aggregateId = aggregateId;
		this.clientData = clientData;
		this.amount = amount;
	}

	public Payment rollBack(){
		//TODO explore domain rules
		eventPublisher.publish(new PaymentRolledBackEvent(getAggregateId()));
		return paymentFactory.createPayment(clientData, amount.multiplyBy(-1));
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/payment/PaymentFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.payment;

import javax.inject.Inject;

import pl.com.bottega.ddd.annotations.domain.DomainFactory;
import pl.com.bottega.ddd.support.domain.DomainEventPublisher;
import pl.com.bottega.ecommerce.canonicalmodel.events.ClientPaidEvent;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * 
 * @author Slawek
 *
 */
@DomainFactory
public class PaymentFactory {
	
	@Inject
	private DomainEventPublisher publisher;

	public Payment createPayment(ClientData clientData, Money amount){
		//TODO validate
		
		AggregateId aggregateId = AggregateId.generate();
		publisher.publish(new ClientPaidEvent(aggregateId, clientData, amount));
		return new Payment(aggregateId, clientData, amount);
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/payment/PaymentRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.payment;

import pl.com.bottega.ddd.annotations.domain.DomainRepository;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@DomainRepository
public interface PaymentRepository {

	public Payment load(AggregateId paymentId);
	
	public void save(Payment payment);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/Product.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.productscatalog;

import java.util.Date;

import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;

import pl.com.bottega.ddd.annotations.domain.AggregateRoot;
import pl.com.bottega.ddd.support.domain.BaseAggregateRoot;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sharedkernel.Money;

@Entity
@AggregateRoot
public class Product extends BaseAggregateRoot{

	@Embedded
	private Money price;
	
	private String name;
	
	@Enumerated(EnumType.STRING)
	private ProductType productType;
	
	@SuppressWarnings("unused")
	private Product(){}
	
	Product(AggregateId aggregateId, Money price, String name, ProductType productType){
		this.aggregateId = aggregateId;
		this.price = price;
		this.name = name;
		this.productType = productType;
	}
	
	public boolean isAvailabe(){		
		return ! isRemoved();//TODO explore domain rules
	}
	
	public Money getPrice() {
		return price;
	}
	
	public String getName() {
		return name;
	}
	
	public ProductType getProductType() {
		return productType;
	}
	
	public ProductData generateSnapshot(){
		return new ProductData(getAggregateId(), price, name, productType, new Date());
	}
	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/ProductData.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.productscatalog;

import java.util.Date;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Embeddable;
import javax.persistence.Embedded;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sharedkernel.Money;

@Embeddable
@ValueObject
public class ProductData {

	@Embedded
	private AggregateId productId;
	
	@Embedded
	@AttributeOverrides({
		@AttributeOverride(name = "denomination", column = @Column(name = "productPrice_denomination")),
		@AttributeOverride(name = "currencyCode", column = @Column(name = "productPrice_currencyCode")) })
	private Money price;
	
	private String name;
	
	private Date snapshotDate;
	
	@Enumerated(EnumType.STRING)
	private ProductType type;

	
	@SuppressWarnings("unused")
	private ProductData(){}
	
	ProductData(AggregateId productId, Money price, String name, ProductType type, 
			Date snapshotDate) {
		this.productId = productId;
		this.price = price;
		this.name = name;
		this.snapshotDate = snapshotDate;
		this.type = type;
	}

	public AggregateId getProductId() {
		return productId;
	}

	public Money getPrice() {
		return price;
	}

	public String getName() {
		return name;
	}

	public Date getSnapshotDate() {
		return snapshotDate;
	}
	
	public ProductType getType() {
		return type;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		result = prime * result + ((price == null) ? 0 : price.hashCode());
		result = prime * result
				+ ((productId == null) ? 0 : productId.hashCode());
		result = prime * result + ((type == null) ? 0 : type.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ProductData other = (ProductData) obj;
		if (name == null) {
			if (other.name != null)
				return false;
		} else if (!name.equals(other.name))
			return false;
		if (price == null) {
			if (other.price != null)
				return false;
		} else if (!price.equals(other.price))
			return false;
		if (productId == null) {
			if (other.productId != null)
				return false;
		} else if (!productId.equals(other.productId))
			return false;
		if (type != other.type)
			return false;
		return true;
	}
	
	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/ProductRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.productscatalog;

import java.util.List;

import org.springframework.stereotype.Repository;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@Repository
public interface ProductRepository {

	public Product load(AggregateId productId);
	
	public List<Product> findProductWhereBestBeforeExpiredIn(int days);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/ProductType.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.productscatalog;

public enum ProductType {
	DRUG, FOOD, STANDARD

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/purchase/Purchase.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.purchase;

import java.util.Collection;
import java.util.Collections;
import java.util.Date;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.persistence.OrderColumn;

import org.hibernate.annotations.Fetch;
import org.hibernate.annotations.FetchMode;

import pl.com.bottega.ddd.annotations.domain.AggregateRoot;
import pl.com.bottega.ddd.support.domain.BaseAggregateRoot;
import pl.com.bottega.ecommerce.canonicalmodel.events.OrderSubmittedEvent;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * Models fact of purchase.
 * 
 * @author Slawek
 *
 */
@Entity
@AggregateRoot
public class Purchase extends BaseAggregateRoot{

	@OneToMany(cascade = CascadeType.ALL, fetch = FetchType.EAGER, orphanRemoval = true)
	@Fetch(FetchMode.JOIN)
	@OrderColumn(name = "itemNumber")
	@JoinColumn(name = "purchase_id")
	private List<PurchaseItem> items;
	
	private boolean paid;

	@Embedded
	private ClientData clientData;

	private Date purchaseDate;

	@Embedded
	private Money totalCost;

	
	@SuppressWarnings("unused")
	private  Purchase() {}

	Purchase(AggregateId aggregateId, ClientData clientData, List<PurchaseItem> items, Date purchaseDate,
			boolean paid, Money totalCost){
		this.aggregateId = aggregateId;
		this.clientData = clientData;
		this.items = items;
		this.purchaseDate = purchaseDate;
		this.paid = paid;
		this.totalCost = totalCost;
	}
	
	public void confirm() {
		paid = true;
		eventPublisher.publish(new OrderSubmittedEvent(getAggregateId()));
	}
	
	public boolean isPaid() {
		return paid;
	}
	
	public Money getTotalCost() {
		return totalCost;
	}
	
	public Date getPurchaseDate() {
		return purchaseDate;
	}

	public ClientData getClientData() {
		return clientData;
	}
	
	public Collection<PurchaseItem> getItems() {
		return (Collection<PurchaseItem>) Collections.unmodifiableCollection(items);
	}
	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/purchase/PurchaseFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.purchase;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.inject.Inject;

import org.springframework.beans.factory.config.AutowireCapableBeanFactory;

import pl.com.bottega.ddd.annotations.domain.DomainFactory;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sales.domain.client.Client;
import pl.com.bottega.ecommerce.sales.domain.offer.Offer;
import pl.com.bottega.ecommerce.sales.domain.offer.OfferItem;
import pl.com.bottega.ecommerce.sharedkernel.Money;
import pl.com.bottega.ecommerce.sharedkernel.exceptions.DomainOperationException;

@DomainFactory
public class PurchaseFactory {

	@Inject
	private AutowireCapableBeanFactory spring;
	
	/**
	 * 
	 * @param orderId correlation id - correlates purchases and reservations  
	 * @param client
	 * @param offer
	 * @return
	 */
	public Purchase create(AggregateId orderId, Client client, Offer offer){
		if (! canPurchse(client, offer.getAvailabeItems()))
			throw new DomainOperationException(client.getAggregateId(), "client can not purchase");
		
		ArrayList<PurchaseItem> items = new ArrayList<PurchaseItem>(offer.getAvailabeItems().size());
		Money purchaseTotlCost = Money.ZERO;
		
		for (OfferItem item : offer.getAvailabeItems()) {
			PurchaseItem purchaseItem = new PurchaseItem(item.getProductData(), item.getQuantity(), item.getTotalCost());
			items.add(purchaseItem);
			purchaseTotlCost = purchaseTotlCost.add(purchaseItem.getTotalCost());
		}
		
		Purchase purchase = new Purchase(orderId, client.generateSnapshot(),
				items, new Date(), false, purchaseTotlCost);
		
		spring.autowireBean(purchase);
		
		return purchase;
	}

	private boolean canPurchse(Client client, List<OfferItem> availabeItems) {
		return true;//TODO explore domain rules
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/purchase/PurchaseItem.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.purchase;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Embedded;
import javax.persistence.Entity;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ddd.support.domain.BaseEntity;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductData;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * Models purchased items - contains copied data in case on catalog proces and discount change 
 * @author Slawek
 *
 */
@ValueObject
@Entity
public class PurchaseItem extends BaseEntity{
	
	@Embedded
	private ProductData productData;
	
	private int quantity;	
	
	@AttributeOverrides({
		@AttributeOverride(name = "denomination", column = @Column(name = "purchaseTotalCost_denomination")),
		@AttributeOverride(name = "currencyCode", column = @Column(name = "purchaseTotalCost_currencyCode")) })
	private Money totalCost;
	
	@SuppressWarnings("unused")
	private PurchaseItem() {}
	
	public PurchaseItem(ProductData productData, int quantity, Money totalCost) {
		this.productData = productData;
		this.quantity = quantity;
		this.totalCost = totalCost;
	}

	public int getQuantity() {
		return quantity;
	}

	public ProductData getProductData() {
		return productData;
	}

	public Money getTotalCost() {
		return totalCost;
	}

	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/purchase/PurchaseRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.purchase;

import pl.com.bottega.ddd.annotations.domain.DomainRepository;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@DomainRepository
public interface PurchaseRepository {

	Purchase load(AggregateId orderId);

	void save(Purchase purchase);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/Reservation.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.reservation;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;

import org.hibernate.annotations.Fetch;
import org.hibernate.annotations.FetchMode;

import pl.com.bottega.ddd.annotations.domain.AggregateRoot;
import pl.com.bottega.ddd.annotations.domain.Function;
import pl.com.bottega.ddd.annotations.domain.Invariant;
import pl.com.bottega.ddd.annotations.domain.InvariantsList;
import pl.com.bottega.ddd.support.domain.BaseAggregateRoot;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;
import pl.com.bottega.ecommerce.sales.domain.offer.Discount;
import pl.com.bottega.ecommerce.sales.domain.offer.DiscountPolicy;
import pl.com.bottega.ecommerce.sales.domain.offer.Offer;
import pl.com.bottega.ecommerce.sales.domain.offer.OfferItem;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.Product;
import pl.com.bottega.ecommerce.sharedkernel.Money;

/**
 * Reservation is just a "wish list". System can not guarantee that user can buy desired products.</br>
 * Reservation generates Offer VO, that is calculated based on current prices and current avability.
 * 
 * @author Slawek
 *
 */

@InvariantsList({
	"closed: closed reservation cano not be modified",
	"duplicates: can not add already added product, increase quantity instead",
})

@Entity
@AggregateRoot
public class Reservation extends BaseAggregateRoot{
	
	public enum ReservationStatus{
		OPENED, CLOSED
	}
	
	@Enumerated(EnumType.STRING)
	private ReservationStatus status;

	@OneToMany(cascade = CascadeType.ALL, fetch=FetchType.EAGER, orphanRemoval = true)
	@JoinColumn(name = "reservation")
	@Fetch(FetchMode.JOIN)
	private List<ReservationItem> items;

	@Embedded
	private ClientData clientData;

	private Date createDate;

	@SuppressWarnings("unused")
	private Reservation() {}

	Reservation(AggregateId aggregateId, ReservationStatus status, ClientData clientData, Date createDate){
		this.aggregateId = aggregateId;
		this.status = status;
		this.clientData = clientData;
		this.createDate = createDate;
		this.items = new ArrayList<ReservationItem>();
	}

	@Invariant({"closed", "duplicates"})
	public void add(Product product, int quantity){
		if (isClosed())
			domainError("Reservation already closed");
		if (!product.isAvailabe())
			domainError("Product is no longer available");
		
		if (contains(product)){
			increase(product, quantity);			
		}
		else{
			addNew(product, quantity);
		}
	}
	
	/**
	 * Sample function closured by policy </br> 
	 * Higher order function closured by policy function</br>
	 * </br>
	 * Function loads current prices, and prepares offer according to the current availability and given discount
	 * @param discountPolicy
	 * @return
	 */
	@Function
	public Offer calculateOffer(DiscountPolicy discountPolicy) {
		List<OfferItem> availabeItems = new ArrayList<OfferItem>();
		List<OfferItem> unavailableItems = new ArrayList<OfferItem>();
		
		for (ReservationItem item : items) {						
			if (item.getProduct().isAvailabe()){
				Discount discount = discountPolicy.applyDiscount(item.getProduct(), item.getQuantity(), item.getProduct().getPrice());
				OfferItem offerItem = new OfferItem(item.getProduct().generateSnapshot(), item.getQuantity(), discount);
				
				availabeItems.add(offerItem);
			}
			else {
				OfferItem offerItem = new OfferItem(item.getProduct().generateSnapshot(), item.getQuantity());
				
				unavailableItems.add(offerItem);
			}
		}
		
		return new Offer(availabeItems, unavailableItems);
	}

	private void addNew(Product product, int quantity) {
		ReservationItem item = new ReservationItem(product, quantity);
		items.add(item);
	}

	private void increase(Product product, int quantity) {
		for (ReservationItem item : items) {
			if (item.getProduct().equals(product)){
				item.changeQuantityBy(quantity);
				break;
			}
		}
	}

	public boolean contains(Product product) {
		for (ReservationItem item : items) {
			if (item.getProduct().equals(product))
				return true;
		}
		return false;
	}

	public boolean isClosed() {
		return status.equals(ReservationStatus.CLOSED);
	}
	
	@Invariant({"closed"})
	public void close(){
		if (isClosed())
			domainError("Reservation is already closed");
		status = ReservationStatus.CLOSED;
	}

	public List<ReservedProduct> getReservedProducts() {
		ArrayList<ReservedProduct> result = new ArrayList<ReservedProduct>(items.size());
		
		for (ReservationItem item : items) {
			result.add(new ReservedProduct(item.getProduct().getAggregateId(), item.getProduct().getName(), item.getQuantity(), calculateItemCost(item)));
		}
		
		return result;
	}
	
	private Money calculateItemCost(ReservationItem item){
		return item.getProduct().getPrice().multiplyBy(item.getQuantity());
	}

	

	public ClientData getClientData() {
		return clientData;
	}
	
	public Date getCreateDate() {
		return createDate;
	}
	
	public ReservationStatus getStatus() {
		return status;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservationFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.reservation;

import java.util.Date;

import javax.inject.Inject;

import org.springframework.beans.factory.config.AutowireCapableBeanFactory;

import pl.com.bottega.ddd.annotations.domain.DomainFactory;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sales.domain.client.Client;
import pl.com.bottega.ecommerce.sales.domain.reservation.Reservation.ReservationStatus;
import pl.com.bottega.ecommerce.sharedkernel.exceptions.DomainOperationException;

@DomainFactory
public class ReservationFactory {

	@Inject
	private AutowireCapableBeanFactory spring;
	
	public Reservation create(Client client){
		if (! canReserve(client))
			throw new DomainOperationException(client.getAggregateId(), "Client can not create reservations");
		
		Reservation reservation = new Reservation(AggregateId.generate(), ReservationStatus.OPENED, client.generateSnapshot(), new Date());
		spring.autowireBean(reservation);
		
		addGratis(reservation, client);
		
		return reservation;
	}

	private void addGratis(Reservation reservation, Client client) {				
		//TODO explore domain rules
	}

	private boolean canReserve(Client client) {
		return true;//TODO explore domain rules (ex: cleint's debts, stataus etc) 
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservationItem.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.reservation;

import javax.persistence.Entity;
import javax.persistence.ManyToOne;

import pl.com.bottega.ddd.support.domain.BaseEntity;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.Product;
import pl.com.bottega.ecommerce.sharedkernel.exceptions.DomainOperationException;

@Entity
class ReservationItem extends BaseEntity{

	@ManyToOne
	private Product product;
	
	private int quantity;

	@SuppressWarnings("unused")
	private ReservationItem(){}
	
	ReservationItem(Product product, int quantity) {
		this.product = product;
		this.quantity = quantity;
	}

	void changeQuantityBy(int change) {
		int changed = quantity + change;
		if (changed <= 0)
			throw new DomainOperationException(null, "change below 1");
		this.quantity = changed;
	}
	
	public Product getProduct() {
		return product;
	}

	public int getQuantity() {
		return quantity;
	}

	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservationRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.reservation;

import pl.com.bottega.ddd.annotations.domain.DomainRepository;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@DomainRepository
public interface ReservationRepository {

	void save(Reservation reservation);

	Reservation load(AggregateId reservationId);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservedProduct.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.reservation;

import pl.com.bottega.ddd.annotations.domain.ValueObject;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sharedkernel.Money;

@ValueObject
public class ReservedProduct {

	private String name;
	
	private Money totalCost;
	
	private AggregateId productId;

	private int quantity;
	
	public ReservedProduct(AggregateId productId, String name, int quantity, Money totalCost) {
		this.productId = productId;
		this.name = name;
		this.quantity = quantity;
		this.totalCost = totalCost;
	}

	public String getName() {
		return name;
	}
	
	public Money getTotalCost() {
		return totalCost;
	}
	
	public AggregateId getProductId() {
		return productId;
	}

	public int getQuantity() {
		return quantity;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/impl/JpaOfferFinder.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.readmodel.impl;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

import pl.com.bottega.ddd.annotations.domain.FinderImpl;
import pl.com.bottega.ecommerce.sales.readmodel.offer.Offer;
import pl.com.bottega.ecommerce.sales.readmodel.offer.OfferedProductDto;
import pl.com.bottega.ecommerce.sales.readmodel.offer.OfferQuery;

@FinderImpl
public class JpaOfferFinder implements Offer {

	@PersistenceContext
	private EntityManager entityManager;

	@SuppressWarnings("unchecked")
	@Override
	public List<OfferedProductDto> find(OfferQuery query) {
		@SuppressWarnings("unused")
		boolean bestBeforeExpired = query.isBestBeforeExpired();
		// TODO take into consideration in query

		return (List<OfferedProductDto>) entityManager
				.createQuery(
						"SELECT NEW pl.com.bottega.ecommerce.sales.readmodel.offer.ProductDto(p.aggregateId) FROM Product p")
				.getResultList();
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/impl/JpaOrderFinder.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.readmodel.impl;

import static com.google.common.collect.Lists.transform;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

import pl.com.bottega.cqrs.query.PaginatedResult;
import pl.com.bottega.ddd.annotations.domain.FinderImpl;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sales.domain.purchase.Purchase;
import pl.com.bottega.ecommerce.sales.domain.reservation.Reservation;
import pl.com.bottega.ecommerce.sales.domain.reservation.ReservedProduct;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderDto;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderFinder;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderQuery;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderStatus;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderedProductDto;

import com.google.common.base.Function;

@FinderImpl
public class JpaOrderFinder implements OrderFinder {

	@PersistenceContext
	private EntityManager entityManager;

	@Override
	public OrderDto find(AggregateId orderId) {
		Reservation reservation = entityManager.find(Reservation.class, orderId);
		Purchase purchase = entityManager.find(Purchase.class, orderId);
		
		return toOrderDto(reservation, purchase);
	}

	private OrderDto toOrderDto(Reservation reservation, Purchase purchase) {
		OrderDto dto = new OrderDto();
		dto.setOrderId(reservation.getAggregateId());
		List<ReservedProduct> reservedProducts = reservation.getReservedProducts();
		dto.setOrderedProducts(new ArrayList<OrderedProductDto>(transform(reservedProducts,
				reservedProductToOrderedProductDto())));
		if (purchase != null) {
			dto.setStatus(OrderStatus.CONFIRMED);

			// TODO CHECK PAYMENT!
			
		} else {
			dto.setStatus(OrderStatus.NEW);
		}
		return dto;
	}

	private static Function<ReservedProduct, OrderedProductDto> reservedProductToOrderedProductDto() {
		return new Function<ReservedProduct, OrderedProductDto>() {
			public OrderedProductDto apply(ReservedProduct product) {
				OrderedProductDto dto = new OrderedProductDto();
				dto.setOfferId(product.getProductId());
				return dto;
			}
		};
	}

	@Override
	public PaginatedResult<OrderDto> query(OrderQuery orderQuery) {
		return null;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/offer/Offer.java`
```java
package pl.com.bottega.ecommerce.sales.readmodel.offer;

import java.util.List;

import pl.com.bottega.ddd.annotations.application.Finder;

@Finder
public interface Offer {

	public List<OfferedProductDto> find(OfferQuery query);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/offer/OfferQuery.java`
```java
package pl.com.bottega.ecommerce.sales.readmodel.offer;

public class OfferQuery {

	public boolean isBestBeforeExpired() {
		// TODO Auto-generated method stub
		return false;
	}

	
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/offer/OfferedProductDto.java`
```java
package pl.com.bottega.ecommerce.sales.readmodel.offer;

public class OfferedProductDto {

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/orders/OrderDto.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.readmodel.orders;

import java.util.ArrayList;
import java.util.List;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

public class OrderDto {

	private AggregateId orderId;
	private List<OrderedProductDto> orderedProducts = new ArrayList<OrderedProductDto>();
	private OrderStatus status;
	private Boolean confirmable;

	public AggregateId getOrderId() {
		return orderId;
	}

	public void setOrderId(AggregateId orderId) {
		this.orderId = orderId;
	}

	public List<OrderedProductDto> getOrderedProducts() {
		return orderedProducts;
	}

	public void setOrderedProducts(List<OrderedProductDto> orderedProducts) {
		this.orderedProducts = orderedProducts;
	}

	public OrderStatus getStatus() {
		return status;
	}

	public void setStatus(OrderStatus status) {
		this.status = status;
	}

	public Boolean getConfirmable() {
		return confirmable;
	}

	public void setConfirmable(Boolean confirmable) {
		this.confirmable = confirmable;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/orders/OrderFinder.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.readmodel.orders;

import pl.com.bottega.cqrs.query.PaginatedResult;
import pl.com.bottega.ddd.annotations.application.Finder;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@Finder
public interface OrderFinder {

	OrderDto find(AggregateId orderId);

	PaginatedResult<OrderDto> query(OrderQuery orderQuery);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/orders/OrderQuery.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.readmodel.orders;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

public class OrderQuery {

	private String productName;
	
	public OrderQuery(String productName, AggregateId clientId){
		this.productName = productName;
		//TODO search by client
	}
	
	public String getProductName() {
		return productName;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/orders/OrderStatus.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.readmodel.orders;

public enum OrderStatus {
	NEW, CONFIRMED, PROCESSING_PAYMENT, PAYMENT_ACCEPTED, PAYMENT_REJECTED;

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sales/readmodel/orders/OrderedProductDto.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.readmodel.orders;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

// TODO more attrs
public class OrderedProductDto {
	private AggregateId offerId;

	public AggregateId getOfferId() {
		return offerId;
	}

	public void setOfferId(AggregateId offerId) {
		this.offerId = offerId;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/Money.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sharedkernel;

import java.io.Serializable;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Currency;

import javax.persistence.Embeddable;

import org.fest.util.Objects;

import pl.com.bottega.ddd.annotations.domain.ValueObject;

/**
 * 
 */
@SuppressWarnings("serial")
@Embeddable
@ValueObject
public class Money implements Serializable {

	public static final Currency DEFAULT_CURRENCY = Currency.getInstance("EUR");

	public static final Money ZERO = new Money(BigDecimal.ZERO);

	private BigDecimal denomination;

	private String currencyCode;

	protected Money() {
	}

	public Money(BigDecimal denomination, Currency currency) {
		this(denomination, currency.getCurrencyCode());
	}

	private Money(BigDecimal denomination, String currencyCode) {
		this.denomination = denomination.setScale(2, RoundingMode.HALF_EVEN);
		this.currencyCode = currencyCode;
	}

	public Money(BigDecimal denomination) {
		this(denomination, DEFAULT_CURRENCY);
	}

	public Money(double denomination, Currency currency) {
		this(new BigDecimal(denomination), currency.getCurrencyCode());
	}

	public Money(double denomination, String currencyCode) {
		this(new BigDecimal(denomination), currencyCode);
	}

	public Money(double denomination) {
		this(denomination, DEFAULT_CURRENCY);
	}

	public Money multiplyBy(double multiplier) {
		return multiplyBy(new BigDecimal(multiplier));
	}

	public Money multiplyBy(BigDecimal multiplier) {
		return new Money(denomination.multiply(multiplier), currencyCode);
	}

	public Money add(Money money) {
		if (!compatibleCurrency(money)) {
			throw new IllegalArgumentException("Currency mismatch");
		}

		return new Money(denomination.add(money.denomination), determineCurrencyCode(money));
	}

	public Money subtract(Money money) {
		if (!compatibleCurrency(money))
			throw new IllegalArgumentException("Currency mismatch");

		return new Money(denomination.subtract(money.denomination), determineCurrencyCode(money));
	}

	/**
	 * Currency is compatible if the same or either money object has zero value.
	 */
	private boolean compatibleCurrency(Money money) {
		return isZero(denomination) || isZero(money.denomination) || currencyCode.equals(money.getCurrencyCode());
	}

	private boolean isZero(BigDecimal testedValue) {
		return BigDecimal.ZERO.compareTo(testedValue) == 0;
	}

	/**
	 * @return currency from this object or otherCurrencyCode. Preferred is the
	 *         one that comes from Money that has non-zero value.
	 */
	private Currency determineCurrencyCode(Money otherMoney) {
		String resultingCurrenctCode = isZero(denomination) ? otherMoney.currencyCode : currencyCode;
		return Currency.getInstance(resultingCurrenctCode);
	}

	public String getCurrencyCode() {
		return currencyCode;
	}

	public Currency getCurrency() {
		return Currency.getInstance(currencyCode);
	}

	public boolean greaterThan(Money other) {
		return denomination.compareTo(other.denomination) > 0;
	}

	public boolean lessThan(Money other) {
		return denomination.compareTo(other.denomination) < 0;
	}

	public boolean lessOrEquals(Money other) {
		return denomination.compareTo(other.denomination) <= 0;
	}

	@Override
	public String toString() {
		return String.format("%0$.2f %s", denomination, getCurrency().getSymbol());
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((currencyCode == null) ? 0 : currencyCode.hashCode());
		result = prime * result + ((denomination == null) ? 0 : denomination.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Money other = (Money) obj;
		return compatibleCurrency(other) && Objects.areEqual(denomination, other.denomination);
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/exceptions/DomainOperationException.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sharedkernel.exceptions;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@SuppressWarnings("serial")
public class DomainOperationException extends RuntimeException{

	private AggregateId aggregateId;

	public DomainOperationException(AggregateId aggregateId, String message){
		super(message);
		this.aggregateId = aggregateId;
	}
	
	public AggregateId getAggregateId() {
		return aggregateId;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/specification/AndSpecification.java`
```java
package pl.com.bottega.ecommerce.sharedkernel.specification;

/**
 * 
 * @author Slawek
 *
 * @param <T>
 */
public class AndSpecification<T> extends CompositeSpecification<T>{
    private Specification<T> a;
    private Specification<T> b;

    public AndSpecification(Specification<T> a, Specification<T> b){
        this.a = a;
        this.b = b;
    }

    public boolean isSatisfiedBy(T candidate){
        return a.isSatisfiedBy(candidate) && b.isSatisfiedBy(candidate);
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/specification/CompositeSpecification.java`
```java
package pl.com.bottega.ecommerce.sharedkernel.specification;

import java.util.Arrays;
import java.util.List;

/**
 * 
 * @author Slawek
 * 
 * @param <T>
 */
public abstract class CompositeSpecification<T> implements Specification<T> {

	public Specification<T> and(Specification<T> other) {
		return new AndSpecification<T>(this, other);
	}

	public Specification<T> or(Specification<T> other) {
		return new OrSpecification<T>(this, other);
	}

	public Specification<T> not() {
		return new NotSpecification<T>(this);
	}

	@SuppressWarnings("unchecked")
	public Specification<T> conjunction(Specification<T>... others) {
		List<Specification<T>> list = Arrays.asList(others);
		list.add(this);
		return new Conjunction<T>(list);
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/specification/Conjunction.java`
```java
package pl.com.bottega.ecommerce.sharedkernel.specification;

import java.util.List;

public class Conjunction<T> extends CompositeSpecification<T> {

	private List<Specification<T>> list;
	
	public Conjunction(List<Specification<T>> list) {
		this.list = list;
	}

	@Override
	public boolean isSatisfiedBy(T candidate) {
		for (Specification<T> spec : list) {
			if (! spec.isSatisfiedBy(candidate))
				return false;
		}
		
		return true;
	}

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/specification/ConjunctionSpecification.java`
```java
package pl.com.bottega.ecommerce.sharedkernel.specification;

/**
 * 
 * @author Slawek
 *
 * @param <T>
 */
public class ConjunctionSpecification<T> extends CompositeSpecification<T>{
    private Specification<T>[] conjunction;

    @SuppressWarnings("unchecked")
	public ConjunctionSpecification(Specification<T>... conjunction){
        this.conjunction = conjunction;
    }

    public boolean isSatisfiedBy(T candidate){
        for (Specification<T> spec : conjunction){
        	if (!spec.isSatisfiedBy(candidate))
        		return false;
        }
    	
    	return true;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/specification/DisjunctionSpecification.java`
```java
package pl.com.bottega.ecommerce.sharedkernel.specification;

/**
 * 
 * @author Slawek
 *
 * @param <T>
 */
public class DisjunctionSpecification<T> extends CompositeSpecification<T>{
    private Specification<T>[] disjunction;

    @SuppressWarnings("unchecked")
	public DisjunctionSpecification(Specification<T>... disjunction){
        this.disjunction = disjunction;
    }

    public boolean isSatisfiedBy(T candidate){
        for (Specification<T> spec : disjunction){
        	if (spec.isSatisfiedBy(candidate))
        		return true;
        }
    	
    	return false;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/specification/NotSpecification.java`
```java
package pl.com.bottega.ecommerce.sharedkernel.specification;

/**
 * 
 * @author Slawek
 *
 * @param <T>
 */
public class NotSpecification<T> extends CompositeSpecification<T> {
    private Specification<T> wrapped;

    public NotSpecification(Specification<T> wrapped) {
        this.wrapped = wrapped;
    }

    public boolean isSatisfiedBy(T candidate) {
        return !wrapped.isSatisfiedBy(candidate);
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/specification/OrSpecification.java`
```java
package pl.com.bottega.ecommerce.sharedkernel.specification;

/**
 * 
 * @author Slawek
 *
 * @param <T>
 */
public class OrSpecification<T> extends CompositeSpecification<T>{
    private Specification<T> a;
    private Specification<T> b;

    public OrSpecification(Specification<T> a, Specification<T> b){
        this.a = a;
        this.b = b;
    }

    public boolean isSatisfiedBy(T candidate){
        return a.isSatisfiedBy(candidate) || b.isSatisfiedBy(candidate);
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/sharedkernel/specification/Specification.java`
```java
package pl.com.bottega.ecommerce.sharedkernel.specification;

/**
 * 
 * @author Slawek
 *
 * @param <T>
 */
public interface Specification<T> {
	public boolean isSatisfiedBy(T candidate);

	public Specification<T> and(Specification<T> other);

	public Specification<T> or(Specification<T> other);
	
	@SuppressWarnings("unchecked")
	public Specification<T> conjunction(Specification<T>... others);

	public Specification<T> not();
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/application/commands/DeliverShipmentCommand.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.application.commands;

import java.io.Serializable;

import pl.com.bottega.cqrs.annotations.Command;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@SuppressWarnings("serial")
@Command
public class DeliverShipmentCommand implements Serializable {

    private final AggregateId shipmentId;

    public DeliverShipmentCommand(AggregateId shipmentId) {
        this.shipmentId = shipmentId;
    }

    public AggregateId getShipmentId() {
        return shipmentId;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/application/commands/SendShipmentCommand.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.application.commands;

import java.io.Serializable;

import pl.com.bottega.cqrs.annotations.Command;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@SuppressWarnings("serial")
@Command
public class SendShipmentCommand implements Serializable {

    private final AggregateId shipmentId;

    public SendShipmentCommand(AggregateId shipmentId) {
        this.shipmentId = shipmentId;
    }

    public AggregateId getShipmentId() {
        return shipmentId;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/application/listeners/OrderSubmittedForShippingListener.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.application.listeners;

import javax.inject.Inject;

import pl.com.bottega.ddd.annotations.event.EventListener;
import pl.com.bottega.ddd.annotations.event.EventListeners;
import pl.com.bottega.ecommerce.canonicalmodel.events.OrderSubmittedEvent;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderDto;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderFinder;
import pl.com.bottega.ecommerce.shipping.domain.Shipment;
import pl.com.bottega.ecommerce.shipping.domain.ShipmentFactory;
import pl.com.bottega.ecommerce.shipping.domain.ShipmentRepository;

/**
 * When an order is submitted by a customer automatically create a shipment in
 * WAITING status.
 * 
 * NOTICE: This is an example of communication across multiple bounded contexts
 * using events. In this context we can't access Order aggregate directly so we
 * use DTO from the read model instead.
 * 
 * @author Rafał Jamróz
 */
@EventListeners
public class OrderSubmittedForShippingListener {

    @Inject
    private ShipmentFactory factory;

    @Inject
    private OrderFinder orderFinder;

    @Inject
    private ShipmentRepository repository;

    @EventListener(asynchronous = true)
    public void handle(OrderSubmittedEvent event) {
        OrderDto orderDetails = orderFinder.find(event.getOrderId());
        Shipment shipment = factory.createShipment(orderDetails.getOrderId());
        repository.save(shipment);
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/domain/Shipment.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.domain;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Entity;

import pl.com.bottega.ddd.annotations.domain.AggregateRoot;
import pl.com.bottega.ddd.support.domain.BaseAggregateRoot;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.shipping.domain.events.OrderShippedEvent;
import pl.com.bottega.ecommerce.shipping.domain.events.ShipmentDeliveredEvent;

/**
 * @author Rafał Jamróz
 */
@Entity
@AggregateRoot
public class Shipment extends BaseAggregateRoot {

	@AttributeOverrides({
		@AttributeOverride(name = "aggregateId", column = @Column(name = "orderId"))})
    private AggregateId orderId;

    private ShippingStatus status;

    
    @SuppressWarnings("unused")
	private Shipment() {}

    Shipment(AggregateId shipmentId, AggregateId orderId) {
        this.aggregateId = shipmentId;
    	this.orderId = orderId;
        this.status = ShippingStatus.WAITING;
    }

    /**
     * Shipment has been sent to the customer.
     */
    public void ship() {
        if (status != ShippingStatus.WAITING) {
            throw new IllegalStateException("cannot ship in status " + status);
        }
        status = ShippingStatus.SENT;
        eventPublisher.publish(new OrderShippedEvent(orderId, getAggregateId()));
    }

    /**
     * Shipment has been confirmed received by the customer.
     */
    public void deliver() {
        if (status != ShippingStatus.SENT) {
            throw new IllegalStateException("cannot deliver in status " + status);
        }
        status = ShippingStatus.DELIVERED;
        eventPublisher.publish(new ShipmentDeliveredEvent(getAggregateId()));
    }

    public AggregateId getOrderId() {
        return orderId;
    }

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/domain/ShipmentFactory.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.domain;

import javax.inject.Inject;

import org.springframework.beans.factory.config.AutowireCapableBeanFactory;

import pl.com.bottega.ddd.annotations.domain.DomainFactory;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@DomainFactory
public class ShipmentFactory {

    @Inject
    private AutowireCapableBeanFactory spring;

    public Shipment createShipment(AggregateId orderId) {
        Shipment shipment = new Shipment(AggregateId.generate(), orderId);
        spring.autowireBean(shipment);
        return shipment;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/domain/ShipmentRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.domain;

import pl.com.bottega.ddd.annotations.domain.DomainRepository;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

/**
 * @author Rafał Jamróz
 */
@DomainRepository
public interface ShipmentRepository {

    void save(Shipment order);

    Shipment load(AggregateId orderId);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/domain/ShippingStatus.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.domain;

public enum ShippingStatus {
    WAITING, SENT, DELIVERED;
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/domain/events/OrderShippedEvent.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.domain.events;

import java.io.Serializable;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@SuppressWarnings("serial")
public class OrderShippedEvent implements Serializable {

    private final AggregateId orderId;
    private final AggregateId shipmentId;

    public OrderShippedEvent(AggregateId orderId, AggregateId shipmentId) {
        this.orderId = orderId;
        this.shipmentId = shipmentId;
    }

    public AggregateId getOrderId() {
        return orderId;
    }

    public AggregateId getShipmentId() {
        return shipmentId;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/domain/events/ShipmentDeliveredEvent.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.domain.events;

import java.io.Serializable;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@SuppressWarnings("serial")
public class ShipmentDeliveredEvent implements Serializable {

    private final AggregateId shipmentId;

    public ShipmentDeliveredEvent(AggregateId shipmentId) {
        this.shipmentId = shipmentId;
    }

    public AggregateId getShipmentId() {
        return shipmentId;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/intrastructure/JpaShipmentRepository.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.intrastructure;

import pl.com.bottega.ddd.annotations.domain.DomainRepositoryImpl;
import pl.com.bottega.ddd.support.infrastructure.repository.jpa.GenericJpaRepository;
import pl.com.bottega.ecommerce.shipping.domain.Shipment;
import pl.com.bottega.ecommerce.shipping.domain.ShipmentRepository;

@DomainRepositoryImpl
public class JpaShipmentRepository extends GenericJpaRepository<Shipment> implements ShipmentRepository {

  
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/readmodel/ShipmentDto.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.readmodel;

import java.io.Serializable;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.shipping.domain.ShippingStatus;

@SuppressWarnings("serial")
public class ShipmentDto implements Serializable {

    private AggregateId shipmentId;
    private AggregateId orderId;
    private ShippingStatus status;

    public ShipmentDto(AggregateId shipmentId, AggregateId orderId, ShippingStatus status) {
        this.shipmentId = shipmentId;
        this.orderId = orderId;
        this.status = status;
    }

    public AggregateId getShipmentId() {
        return shipmentId;
    }

    public AggregateId getOrderId() {
        return orderId;
    }

    public ShippingStatus getStatus() {
        return status;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/readmodel/ShipmentFinder.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.readmodel;

import java.util.List;

public interface ShipmentFinder {

    List<ShipmentDto> findShipment();

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/readmodel/impl/JpaShipmentFinder.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.readmodel.impl;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.Query;

import pl.com.bottega.ddd.annotations.application.Finder;
import pl.com.bottega.ecommerce.shipping.readmodel.ShipmentDto;
import pl.com.bottega.ecommerce.shipping.readmodel.ShipmentFinder;

@Finder
public class JpaShipmentFinder implements ShipmentFinder {

    @PersistenceContext
    private EntityManager entityManager;

    @SuppressWarnings("unchecked")
	@Override
    public List<ShipmentDto> findShipment() {
        String jpql = "select new pl.com.bottega.erp.shipping.presentation.ShipmentDto(s.id, s.orderId, s.status) from Shipment s";
        Query query = entityManager.createQuery(jpql);
        return query.getResultList();
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/shipping/webui/ShipmentsListController.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.shipping.webui;

import java.util.List;

import javax.inject.Inject;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import pl.com.bottega.cqrs.command.Gate;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.shipping.application.commands.DeliverShipmentCommand;
import pl.com.bottega.ecommerce.shipping.application.commands.SendShipmentCommand;
import pl.com.bottega.ecommerce.shipping.readmodel.ShipmentDto;
import pl.com.bottega.ecommerce.shipping.readmodel.ShipmentFinder;

@Controller
@RequestMapping("/shipping/shipment")
public class ShipmentsListController {

    @Inject
    private ShipmentFinder finder;

    @Inject
    private Gate gate;

    @RequestMapping("/list")
    public String shippingList(Model model) {
        List<ShipmentDto> shipments = finder.findShipment();
        model.addAttribute("shipments", shipments);
        return "/shipping/shipmentsList";
    }

    @RequestMapping(value = "/send", method = RequestMethod.POST)
    public String shipOrder(@RequestParam("shipmentId") String shipmentId) {
        gate.dispatch(new SendShipmentCommand(new AggregateId(shipmentId)));
        return "redirect:/shipping/shipment/list";
    }

    @RequestMapping(value = "/deliver", method = RequestMethod.POST)
    public String receiveShipment(@RequestParam("shipmentId") String shipmentId) {
        gate.dispatch(new DeliverShipmentCommand(new AggregateId(shipmentId)));
        return "redirect:/shipping/shipment/list";
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/application/SystemContext.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.application;



import org.springframework.stereotype.Component;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

@Component
public class SystemContext {
	
	public SystemUser getSystemUser(){
		return new SystemUser(new AggregateId("1"));//TODO introduce security integration
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/application/SystemUser.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.application;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;

/**
 * Application model of the logged user
 * 
 * TODO introduce roles model
 * 
 * @author Slawek
 *
 */
public class SystemUser {

	private AggregateId clientId;
		
	SystemUser(AggregateId clientId) {
		this.clientId = clientId;
	}

	/**
	 * 
	 * @return Domain model Client
	 */
	public AggregateId getClientId(){
		return clientId;
	}
	
	public boolean isLoogedIn(){
		return clientId != null;
	}
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/infrastructure/events/SimpleEventPublisher.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.infrastructure.events;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import pl.com.bottega.ddd.support.domain.DomainEventPublisher;
import pl.com.bottega.ecommerce.system.infrastructure.events.impl.handlers.EventHandler;

@Component
public class SimpleEventPublisher implements DomainEventPublisher {

    private static final Logger LOGGER = LoggerFactory.getLogger(SimpleEventPublisher.class);

    private Set<EventHandler> eventHandlers = new HashSet<EventHandler>();

    public void registerEventHandler(EventHandler handler) {
        eventHandlers.add(handler);
        // new SpringEventHandler(eventType, beanName, method));
    }

    @Override
    public void publish(Serializable event) {
        doPublish(event);
    }

    protected void doPublish(Object event) {
        for (EventHandler handler : new ArrayList<EventHandler>(eventHandlers)) {
            if (handler.canHandle(event)) {
                try {
                    handler.handle(event);
                } catch (Exception e) {
                    LOGGER.error("event handling error", e);
                }
            }
        }
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/SagaEngine.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga;

public interface SagaEngine {

    void handleSagasEvent(Object event);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/SagaInstance.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga;

/**
 * 
 * @author Rafał Jamróz
 * 
 * @param <D>
 *            saga data type (memento)
 */
public class SagaInstance<D> {
    protected D data;
    private boolean completed;

    public D getData() {
        return data;
    }

    public void setData(D data) {
        this.data = data;
    }

    protected void markAsCompleted() {
        completed = true;
    }

    public boolean isCompleted() {
        return completed;
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/SagaManager.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga;

/**
 * @author Rafał Jamróz
 * 
 * @param <T>
 *            saga type
 * @param <D>
 *            saga data type
 */
public interface SagaManager<T extends SagaInstance<D>, D> {

    void removeSaga(T saga);

    D createNewSagaData();
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/annotations/LoadSaga.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga.annotations;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface LoadSaga {

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/annotations/Saga.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga.annotations;

import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

@Component
@Scope(BeanDefinition.SCOPE_PROTOTYPE)
public @interface Saga {

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/annotations/SagaAction.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga.annotations;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface SagaAction {

}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/impl/SagaRegistry.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga.impl;

import java.util.Collection;

import pl.com.bottega.ecommerce.system.saga.SagaInstance;
import pl.com.bottega.ecommerce.system.saga.SagaManager;

public interface SagaRegistry {

    @SuppressWarnings("rawtypes")
	Collection<SagaManager> getLoadersForEvent(Object event);

    @SuppressWarnings("rawtypes")
	SagaInstance createSagaInstance(Class<? extends SagaInstance> sagaType);
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/impl/SimpleSagaEngine.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga.impl;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.Collection;

import javax.annotation.PostConstruct;
import javax.inject.Inject;
import javax.persistence.NoResultException;

import org.springframework.stereotype.Component;

import pl.com.bottega.ecommerce.system.infrastructure.events.SimpleEventPublisher;
import pl.com.bottega.ecommerce.system.infrastructure.events.impl.handlers.EventHandler;
import pl.com.bottega.ecommerce.system.saga.SagaEngine;
import pl.com.bottega.ecommerce.system.saga.SagaInstance;
import pl.com.bottega.ecommerce.system.saga.SagaManager;
import pl.com.bottega.ecommerce.system.saga.annotations.LoadSaga;
import pl.com.bottega.ecommerce.system.saga.annotations.SagaAction;

/**
 * @author Rafał Jamróz
 */
@Component
public class SimpleSagaEngine implements SagaEngine {

    private final SagaRegistry sagaRegistry;

    private final SimpleEventPublisher eventPublisher;

    @Inject
    public SimpleSagaEngine(SagaRegistry sagaRegistry, SimpleEventPublisher eventPublisher) {
        this.sagaRegistry = sagaRegistry;
        this.eventPublisher = eventPublisher;
    }

    @PostConstruct
    public void registerEventHandler() {
        eventPublisher.registerEventHandler(new SagaEventHandler(this));
    }

    @SuppressWarnings({ "rawtypes", "unchecked" })
    @Override
    public void handleSagasEvent(Object event) {
        Collection<SagaManager> loaders = sagaRegistry.getLoadersForEvent(event);
        for (SagaManager loader : loaders) {
            SagaInstance sagaInstance = loadSaga(loader, event);
            invokeSagaActionForEvent(sagaInstance, event);
            if (sagaInstance.isCompleted()) {
                loader.removeSaga(sagaInstance);
            }
        }
    }

    @SuppressWarnings({ "rawtypes", "unchecked" })
	private SagaInstance loadSaga(SagaManager loader, Object event) {
        Class<? extends SagaInstance> sagaType = determineSagaTypeByLoader(loader);
        Object sagaData = loadSagaData(loader, event);
        if (sagaData == null) {
            sagaData = loader.createNewSagaData();
        }
        SagaInstance sagaInstance = sagaRegistry.createSagaInstance(sagaType);
        sagaInstance.setData(sagaData);
        return sagaInstance;
    }

    // TODO determine saga type more reliably
    @SuppressWarnings({ "rawtypes", "unchecked" })
	private Class<? extends SagaInstance> determineSagaTypeByLoader(SagaManager loader) {
        Type type = ((ParameterizedType) loader.getClass().getGenericInterfaces()[0]).getActualTypeArguments()[0];
        return ((Class<? extends SagaInstance>) type);
    }

    /**
     * TODO handle exception in more generic way
     */
    @SuppressWarnings("rawtypes")
	private Object loadSagaData(SagaManager loader, Object event) {
        Method loaderMethod = findHandlerMethodForEvent(loader.getClass(), event);
        try {
            Object sagaData = loaderMethod.invoke(loader, event);
            return sagaData;
        } catch (InvocationTargetException e) {
            // NRE is ok here, it means that saga hasn't been started yet
            if (e.getTargetException() instanceof NoResultException) {
                return null;
            } else {
                throw new RuntimeException(e);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private void invokeSagaActionForEvent(SagaInstance<?> saga, Object event) {
        Method eventHandler = findHandlerMethodForEvent(saga.getClass(), event);
        try {
            eventHandler.invoke(saga, event);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private Method findHandlerMethodForEvent(Class<?> type, Object event) {
        for (Method method : type.getMethods()) {
            if (method.getAnnotation(SagaAction.class) != null || method.getAnnotation(LoadSaga.class) != null) {
                if (method.getParameterTypes().length == 1
                        && method.getParameterTypes()[0].isAssignableFrom(event.getClass())) {
                    return method;
                }
            }
        }
        throw new RuntimeException("no method handling " + event.getClass());
    }

    private static class SagaEventHandler implements EventHandler {

        private final SagaEngine sagaEngine;

        public SagaEventHandler(SagaEngine sagaEngine) {
            this.sagaEngine = sagaEngine;
        }

        @Override
        public boolean canHandle(Object event) {
            return true;
        }

        @Override
        public void handle(Object event) {
            sagaEngine.handleSagasEvent(event);
        }
    }
}
```

## File: `src/main/java/pl/com/bottega/ecommerce/core/saga/impl/SpringSagaRegistry.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.system.saga.impl;

import java.lang.reflect.Method;
import java.util.Collection;
import java.util.HashSet;

import javax.inject.Inject;

import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.stereotype.Component;

import pl.com.bottega.ecommerce.system.saga.SagaInstance;
import pl.com.bottega.ecommerce.system.saga.SagaManager;
import pl.com.bottega.ecommerce.system.saga.annotations.LoadSaga;
import pl.com.bottega.ecommerce.system.saga.annotations.SagaAction;

import com.google.common.collect.HashMultimap;
import com.google.common.collect.Multimap;

/**
 * @author Rafał Jamróz
 */
@SuppressWarnings({"rawtypes" })
@Component
public class SpringSagaRegistry implements SagaRegistry, ApplicationListener<ContextRefreshedEvent> {

    private Multimap<Class<?>, String> loadersInterestedIn = HashMultimap.create();

    @Inject
    private ConfigurableListableBeanFactory beanFactory;

    @Override
    public Collection<SagaManager> getLoadersForEvent(Object event) {
        Collection<SagaManager> results = new HashSet<SagaManager>();
        Collection<String> loadersBeansNames = loadersInterestedIn.get(event.getClass());
        for (String loaderBeanName : loadersBeansNames) {
            SagaManager loader = beanFactory.getBean(loaderBeanName, SagaManager.class);
            results.add(loader);
        }
        return results;
    }

    @Override
    public SagaInstance createSagaInstance(Class<? extends SagaInstance> sagaType) {
        return (SagaInstance) beanFactory.getBean(sagaType);
    }

    @Override
    public void onApplicationEvent(ContextRefreshedEvent event) {
        loadersInterestedIn.clear();
        registerSagaLoaderBeans();
    }

    private void registerSagaLoaderBeans() {
        String[] loadersNames = beanFactory.getBeanNamesForType(SagaManager.class);
        for (String loaderBeanName : loadersNames) {
            BeanDefinition loaderBeanDefinition = beanFactory.getBeanDefinition(loaderBeanName);
            try {
                registerSagaLoader(Class.forName(loaderBeanDefinition.getBeanClassName()), loaderBeanName);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }

    private void registerSagaLoader(Class<?> loaderClass, String beanName) {
        for (Method method : loaderClass.getMethods()) {
            if (method.getAnnotation(SagaAction.class) != null || method.getAnnotation(LoadSaga.class) != null) {
                Class<?>[] params = method.getParameterTypes();
                if (params.length == 1) {
                    loadersInterestedIn.put(params[0], beanName);
                } else {
                    throw new RuntimeException("incorred event hadndler: " + method);
                }
            }
        }
    }

}
```

## File: `src/main/resources/commons-logging.properties`
```
#
# Copyright 2011-2014 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

org.apache.commons.logging.Log=org.apache.commons.logging.impl.Log4JLogger
```

## File: `src/main/resources/configurationContext.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--

    Copyright 2011-2014 the original author or authors.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

-->
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context" xmlns:p="http://www.springframework.org/schema/p"
	xmlns:tx="http://www.springframework.org/schema/tx"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx-3.1.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-3.1.xsd">

	<context:component-scan base-package="pl.com.bottega.ecommerce pl.com.bottega.support pl.com.bottega.cqrs.command">
		<context:exclude-filter type="annotation" expression="org.springframework.stereotype.Controller" />
	</context:component-scan>

	<context:property-placeholder location="classpath:jdbc.properties" />

	<tx:annotation-driven transaction-manager="transactionManager" />

	<bean class="org.springframework.orm.jpa.support.PersistenceAnnotationBeanPostProcessor" />

	<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource" p:driverClassName="${jdbc.driverClassName}"
		p:url="${jdbc.url}" />

	<bean id="transactionManager" class="org.springframework.orm.jpa.JpaTransactionManager"
		p:entityManagerFactory-ref="entityManagerFactory" />

	<bean id="entityManagerFactory" class="org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean"
		p:dataSource-ref="dataSource" p:jpaVendorAdapter-ref="jpaAdapter">
		<property name="loadTimeWeaver">
			<bean class="org.springframework.instrument.classloading.InstrumentationLoadTimeWeaver" />
		</property>
		<!-- isolation level problem -->
		<property name="jpaDialect">
            <bean class="pl.com.bottega.testutils.HibernateExtendedJpaDialect"/>
        </property>
		<property name="persistenceUnitName" value="defaultPU" />
	</bean>

	<bean id="jdbcTemplate" class="org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate">
		<constructor-arg ref="dataSource" />
	</bean>

	<bean id="jpaAdapter" class="org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter" p:database="${jpa.database}"
		p:showSql="${jpa.showSql}" />
</beans>
```

## File: `src/main/resources/import.sql`
```sql
--
-- Copyright 2011-2014 the original author or authors.
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--     http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
--

insert into Client(aggregateId, aggregateStatus, version, name) values('1', 0, 1, 'client 1');
insert into Product(aggregateId, aggregateStatus, version, name, productType, currencyCode, denomination) values('p1', 0, 1, 'product 1', 'STANDARD', 'EUR', 10);
insert into Product(aggregateId, aggregateStatus, version, name, productType, currencyCode, denomination) values('p2', 0, 1, 'product 2', 'STANDARD', 'EUR', 20);
```

## File: `src/main/resources/jdbc.properties`
```
#
# Copyright 2011-2014 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

jdbc.driverClassName=org.hsqldb.jdbc.JDBCDriver 
jdbc.url=jdbc:hsqldb:mem:.
jpa.database=HSQL
jpa.showSql=true
```

## File: `src/main/resources/log4j.properties`
```
#
# Copyright 2011-2014 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

log4j.rootCategory=DEBUG, O

# Stdout
log4j.appender.O=org.apache.log4j.ConsoleAppender
log4j.appender.O.layout=org.apache.log4j.PatternLayout
log4j.appender.O.layout.ConversionPattern=[%d{ISO8601}]%5p%6.6r[%t]%x - %C.%M(%F:%L) - %m%n

#
log4j.logger.org.apache=WARN
log4j.logger.freemarker=WARN

# Hibernate
log4j.logger.org.hibernate=WARN
log4j.logger.org.hibernate.pretty=ERROR
#log4j.logger.org.hibernate.type=TRACE

# Spring
log4j.logger.org.springframework=WARN

# Application
log4j.logger.pl.com.bottega=TRACE
```

## File: `src/main/resources/META-INF/persistence.xml`
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!--

    Copyright 2011-2014 the original author or authors.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

-->
<persistence xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/persistence http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd"
	version="2.0" xmlns="http://java.sun.com/xml/ns/persistence">

	<persistence-unit name="defaultPU"
		transaction-type="RESOURCE_LOCAL">
		<properties>
			<property name="hibernate.hbm2ddl.auto" value="create" />
			<property name="hibernate.dialect" value="org.hibernate.dialect.HSQLDialect"/>
		</properties>
	</persistence-unit>
</persistence>
```

## File: `src/test/java/pl/com/bottega/ecommerce/ExampleServiceIfYouActuallyWantToUseCommands.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce;

import javax.inject.Inject;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.annotation.DirtiesContext.ClassMode;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import pl.com.bottega.cqrs.command.Gate;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sales.acceptancetests.AuthenticationTestHelper;
import pl.com.bottega.ecommerce.sales.application.api.command.AddProdctCommand;
import pl.com.bottega.ecommerce.sales.application.api.command.OrderDetailsCommand;
import pl.com.bottega.ecommerce.sales.application.api.service.OrderingService;
import pl.com.bottega.ecommerce.sales.domain.offer.Offer;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderFinder;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:/functionalTestsContext.xml")
@DirtiesContext(classMode = ClassMode.AFTER_EACH_TEST_METHOD)
@ActiveProfiles("test")
public class ExampleServiceIfYouActuallyWantToUseCommands {

	@Inject
	private Gate gate;
	
	@Inject
	OrderingService orderingService;

	@Inject
	OrderFinder orderFinder;

	@Inject
	AuthenticationTestHelper authenticationHelper;

	@Before
	public void givenImAuthenticated() throws Exception {
		authenticationHelper.asBuyer();
	}

	@After
	public void tearDown() throws Exception {
		authenticationHelper.deauthenticate();
	}
	
	@Test
	public void shouldPurchaseProducts(){
		AggregateId orderId = orderingService.createOrder();
		
		AddProdctCommand cmd = new AddProdctCommand(orderId, new AggregateId("p1"), 1);		
		gate.dispatch(cmd);
		
		Offer offer = orderingService.calculateOffer(orderId);
		
		orderingService.confirm(orderId, new OrderDetailsCommand(), offer);
	}
}
```

## File: `src/test/java/pl/com/bottega/ecommerce/sales/acceptancetests/AuthenticationTestHelper.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.acceptancetests;

import javax.inject.Inject;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

import pl.com.bottega.ecommerce.system.application.SystemContext;

@Component
@Profile("test")
public class AuthenticationTestHelper {

	@Inject
	private SystemContext systemContext;

	public void asBuyer() {
		
	}

	public void asSeller() {
	}

	// TODO chagne to rule and run it after each test
	public void deauthenticate() {
	}

}
```

## File: `src/test/java/pl/com/bottega/ecommerce/sales/acceptancetests/OrderingTest.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.acceptancetests;

import javax.inject.Inject;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.annotation.DirtiesContext.ClassMode;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sales.application.api.command.OrderDetailsCommand;
import pl.com.bottega.ecommerce.sales.application.api.service.OfferChangedExcpetion;
import pl.com.bottega.ecommerce.sales.application.api.service.OrderingService;
import pl.com.bottega.ecommerce.sales.domain.offer.Offer;
import pl.com.bottega.ecommerce.sales.readmodel.orders.OrderFinder;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:/functionalTestsContext.xml")
@DirtiesContext(classMode = ClassMode.AFTER_EACH_TEST_METHOD)
@ActiveProfiles("test")
public class OrderingTest {

	@Inject
	OrderingService orderingService;

	@Inject
	OrderFinder orderFinder;

	@Inject
	AuthenticationTestHelper authenticationHelper;

	@Before
	public void givenImAuthenticated() throws Exception {
		authenticationHelper.asBuyer();
	}

	@After
	public void tearDown() throws Exception {
		authenticationHelper.deauthenticate();
	}
	
	@Test
	public void shouldPurchaseProducts(){
		AggregateId orderId = orderingService.createOrder();
		orderingService.addProduct(orderId, new AggregateId("p1"), 1);
		orderingService.addProduct(orderId, new AggregateId("p2"), 20);
		Offer offer = orderingService.calculateOffer(orderId);
		
		orderingService.confirm(orderId, new OrderDetailsCommand(), offer);
	}
	
	@Test
	public void canNotPurchaseIfOfferChanged(){
		AggregateId orderId = orderingService.createOrder();
		orderingService.addProduct(orderId, new AggregateId("p1"), 1);
		orderingService.addProduct(orderId, new AggregateId("p2"), 20);
		
		Offer offer = orderingService.calculateOffer(orderId);
		//change order 
		orderingService.addProduct(orderId, new AggregateId("p2"), 30);
		//confirm obsolete offer
		try{
			orderingService.confirm(orderId, new OrderDetailsCommand(), offer);
			Assert.fail();
		}
		catch(OfferChangedExcpetion e){}
	}
}
```

## File: `src/test/java/pl/com/bottega/ecommerce/sales/domain/productscatalog/ProductObjectMother.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.productscatalog;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.sharedkernel.Money;

public class ProductObjectMother {

	public static Product someProduct(){
		return new Product(AggregateId.generate(), new Money(10.0), "product 1", ProductType.STANDARD);
	}
}
```

## File: `src/test/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservationObjectMother.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.reservation;

import java.util.Date;

import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.AggregateId;
import pl.com.bottega.ecommerce.canonicalmodel.publishedlanguage.ClientData;
import pl.com.bottega.ecommerce.sales.domain.reservation.Reservation.ReservationStatus;

public class ReservationObjectMother {

	public static Reservation emptyReservation() {
		return new Reservation(AggregateId.generate(), ReservationStatus.OPENED, new ClientData(AggregateId.generate(),  "client 1"), new Date());
	}
}
```

## File: `src/test/java/pl/com/bottega/ecommerce/sales/domain/reservation/ReservationTest.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.ecommerce.sales.domain.reservation;

import org.junit.Assert;
import org.junit.Test;

import pl.com.bottega.ddd.annotations.domain.Invariant;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.Product;
import pl.com.bottega.ecommerce.sales.domain.productscatalog.ProductObjectMother;

public class ReservationTest {

	@Invariant("duplicates")
	@Test
	public void shouldIncreaseQuantityWhenAddingAlreadyAddedProduct(){
		//given
		Reservation reservation = ReservationObjectMother.emptyReservation();
		Product product = ProductObjectMother.someProduct();
		reservation.add(product, 1);
		//when
		reservation.add(product, 1);
		//then
		Assert.assertEquals(1, reservation.getReservedProducts().size());
		Assert.assertEquals(2, reservation.getReservedProducts().get(0).getQuantity());
	}

	
}
```

## File: `src/test/java/pl/com/bottega/testutils/HibernateExtendedJpaDialect.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.testutils;

import java.sql.Connection;
import java.sql.SQLException;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceException;

import org.hibernate.Session;
import org.hibernate.jdbc.Work;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.jdbc.datasource.DataSourceUtils;
import org.springframework.orm.jpa.vendor.HibernateJpaDialect;
import org.springframework.transaction.TransactionDefinition;
import org.springframework.transaction.TransactionException;
 
/**
 * Solution for @ Transactional(isolation = Isolation.SERIALIZABLE) problem
 * 
 * http://amitstechblog.wordpress.com/2011/05/31/supporting-custom-isolation-levels-with-jpa/
 *
 */
@SuppressWarnings("serial")
public class HibernateExtendedJpaDialect extends HibernateJpaDialect {
 
    private Logger logger = LoggerFactory.getLogger(HibernateExtendedJpaDialect.class);
 
    /**
     * This method is overridden to set custom isolation levels on the connection
     * @param entityManager
     * @param definition
     * @return
     * @throws PersistenceException
     * @throws SQLException
     * @throws TransactionException
     */
    @Override
    public Object beginTransaction(final EntityManager entityManager,
            final TransactionDefinition definition) throws PersistenceException,
            SQLException, TransactionException {
        Session session = (Session) entityManager.getDelegate();
        if (definition.getTimeout() != TransactionDefinition.TIMEOUT_DEFAULT) {
            getSession(entityManager).getTransaction().setTimeout(definition.getTimeout());
        }
 
        entityManager.getTransaction().begin();
        logger.debug("Transaction started");
 
        session.doWork(new Work() {
 
            public void execute(Connection connection) throws SQLException {
                logger.debug("The connection instance is {}", connection);
                logger.debug("The isolation level of the connection is {} and the isolation level set on the transaction is {}",
                        connection.getTransactionIsolation(), definition.getIsolationLevel());
                DataSourceUtils.prepareConnectionForTransaction(connection, definition);
            }
        });
 
        return prepareTransaction(entityManager, definition.isReadOnly(), definition.getName());
    }
 
}
```

## File: `src/test/java/pl/com/bottega/testutils/SimpleMapScope.java`
```java
/*
 * Copyright 2011-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package pl.com.bottega.testutils;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.ObjectFactory;
import org.springframework.beans.factory.config.Scope;

public class SimpleMapScope implements Scope {

	/**
	 * This map contains for each bean name or ID the created object. The
	 * objects are created with a spring object factory.
	 */
	private final Map<String, Object> objectMap = new HashMap<String, Object>();

	/**
	 * {@inheritDoc}
	 */
	public Object get(String theName, ObjectFactory<?> theObjectFactory) {
		Object object = objectMap.get(theName);
		if (null == object) {
			object = theObjectFactory.getObject();
			objectMap.put(theName, object);
		}
		return object;
	}

	/**
	 * {@inheritDoc}
	 */
	public String getConversationId() {
		return null;
	}

	/**
	 * {@inheritDoc}
	 */
	public void registerDestructionCallback(final String theName,
			final Runnable theCallback) {
		// nothing to do ... this is optional and not required
	}

	/**
	 * {@inheritDoc}
	 */
	public Object remove(final String theName) {
		return objectMap.remove(theName);
	}

	@Override
	public Object resolveContextualObject(String arg0) {
		// TODO Auto-generated method stub
		return null;
	}

}
```

## File: `src/test/resources/functionalTestsContext.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--

    Copyright 2011-2014 the original author or authors.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

-->
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

	<import resource="classpath:/configurationContext.xml" />

	<!-- fake Session and Request Scope impl - needed for testing Session Scoped Beans -->
	<bean class="org.springframework.beans.factory.config.CustomScopeConfigurer">
		<property name="scopes">
			<map>
				<entry key="session">
					<bean class="pl.com.bottega.testutils.SimpleMapScope" />
				</entry>
				<entry key="request">
					<bean class="pl.com.bottega.testutils.SimpleMapScope" />
				</entry>
			</map>
		</property>
	</bean>
</beans>
```

