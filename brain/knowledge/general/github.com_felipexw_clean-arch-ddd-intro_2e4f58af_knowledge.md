---
id: github.com-felipexw-clean-arch-ddd-intro-2e4f58af-
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:49.758366
---

# KNOWLEDGE EXTRACT: github.com_felipexw_clean-arch-ddd-intro_2e4f58af
> **Extracted on:** 2026-04-01 10:11:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520723/github.com_felipexw_clean-arch-ddd-intro_2e4f58af

---

## File: `.gitignore`
```
Thumbs.db
.DS_Store
.gradle
build/
target/
out/
bin/
.idea
*.iml
*.ipr
*.iws
.project
.settings
.classpath
.factorypath
```

## File: `README.md`
```markdown
# Clean Architecture with Domain Driven Design (DDD)
O objetivo desse projeto é apresentar, de forma didática, alguns dos principais conceitos de Clean Architecture, juntamente com Domain-Driven Design (DDD) com Micronaut.

## Problema
Esse problema veio de origem do curso [Java e Domain Driven Design: Apresentando os conceitos](https://www.alura.com.br/curso-online-java-domain-driven-design-conceitos), com algumas modificações.

### Enunciado
Imagine um software em um contexto acadêmico, onde será necessário **matricular alunos** e **indicar alunos**.
- **indicar alunos**: quando um aluno indica uma pessoa como possível aluno (que não está matriculada, evidentemente), o aluno que indicou acaba recebendo alguma pontuação para isso. Com uma determinada pontuação acumulada, ele pode trocar os pontos por algum curso, ou algo do semelhante. A pessoa indicada recebe um e-mail contendo as informações para se matricular na próxima turma, bem como um determinado desconto na taxa da matrícula.
- **matricular alunos**: ao matricular um novo aluno em um curso, deve ser considerado se o que mesmo não foi indicado. Em caso positivo, o mesmo deverá receber um desconto na matricula. Do contrário, é o valor integral.

## Entendendo e aplicando os conceitos DDD
Alguns conceitos são necessários para melhor entendimento do desenho da solução. São eles:

- **Use cases/commands/queries/actions**: Representam as features identificadas na modelagem.
- **Entities**: Tudo aquilo que pode ser identificado por alguma propriedade única (ex: pessoa é uma entidade, pois todas possuem um CPF - cadastro de pessoa física).
- **Value objects**: São classes que não possuem identidade, porém possuem alguma lógica de funcionamento (ex: uma classe `Address`)
- **Domain events**: São eventos que são disparados ao executar um caso de uso (ex: `StudentRegistered`).
- **Bounded contexts**: São contextos que delimitam o espaço de um problema.
- **Event storming**: Eventos em que atores, casos de etc, agregados, contextos, etc. são identificados. Evento importante para que os os devs e o pessoal de negócio definam um linguagem única (ubíqua) para utilização durante o desenvolvimento.
- **Business invariantes**: são regras de negócio.
- **Actors**: são aqueles que interagem diretamente com os casos de uso (ex: `Student`).

## Clean architecture
![alt](https://github.com/felipexw/clean-arch-ddd-intro/blob/master/brain/knowledge/docs_legacy/clear_arch.PNG)

## Estrutura do projeto
![alt](https://github.com/felipexw/clean-arch-ddd-intro/blob/master/brain/knowledge/docs_legacy/packages.PNG)

A estrutura do projeto ficou da seguinte maneira:
``` 
   /academic
      /application
      /domain
      /infrastructure
   /email
      /application
      /domain
      /infrastructure
   /gamefification
      /application
      /domain
      /infrastructure
   /shared
      /application
      /domain
      /infrastructure
```

O primeiro nível representa o domínio, ou seja, foram identificados 4 domínios: academic (acadêmico), email, gamification (pontuação), shared (compartilhado). Em cada domínio, há basicamente 3 pacotes: 
- *application*: lógica de aplicação (ex: `StudentController` do Micronaut). E a camada de **entrada/saída com o mundo externo**.
- *domain*: **toda a lógica de negócio** e casos de usos (também conhecidos como `commands`e `queries` dentro do DDD, ou `actions`).
- *infrastructure*: camada de infraestrutura que **dá suporte para a camada de domínio** (ex: implementação concreta de algum repositório ou alguma classe que tenha dependência com algum framework ou algo do gênero).

### References
- [Clean Architecture by Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com.br/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)
- [Java e Clean Architecture: Descomplicando arquitetura de software](https://www.alura.com.br/curso-online-java-clean-architecture)
- [Java e Domain Driven Design: Apresentando os conceitos](https://www.alura.com.br/curso-online-java-domain-driven-design-conceitos)
```

## File: `build.gradle`
```
plugins {
    id("com.github.johnrengelman.shadow") version "6.1.0"
    id("io.micronaut.application") version "1.4.2"
}

version = "0.1"
group = "com.github.felpexw"

repositories {
    mavenCentral()
}

micronaut {
    runtime("netty")
    testRuntime("junit5")
    processing {
        incremental(true)
        annotations("com.github.felpexw.*")
    }
}

dependencies {
    annotationProcessor("org.projectlombok:lombok")
    implementation("io.micronaut:micronaut-http-client")
    implementation("io.micronaut:micronaut-runtime")
    implementation("javax.annotation:javax.annotation-api")
    compileOnly("org.projectlombok:lombok")
    implementation("io.micronaut:micronaut-validation")
    runtimeOnly("ch.qos.logback:logback-classic")
    
    //Test deps
   	testImplementation("org.mockito:mockito-core")
    // https://mvnrepository.com/artifact/org.mockito/mockito-inline
	testImplementation group: 'org.mockito', name: 'mockito-inline', version: '3.9.0'
    
    
    // https://mvnrepository.com/artifact/org.assertj/assertj-core
	testImplementation group: 'org.assertj', name: 'assertj-core', version: '3.19.0'
    // https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-params
	testImplementation group: 'org.junit.jupiter', name: 'junit-jupiter-params', version: '5.7.1'
    
}


application {
    mainClass.set("com.github.felpexw.Application")
}
java {
    sourceCompatibility = JavaVersion.toVersion("15")
    targetCompatibility = JavaVersion.toVersion("15")
}



```

## File: `gradle.properties`
```
micronautVersion=2.4.2
```

## File: `gradlew`
```
#!/usr/bin/env sh

#
# Copyright 2015 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

##############################################################################
##
##  Gradle start up script for UN*X
##
##############################################################################

# Attempt to set APP_HOME
# Resolve links: $0 may be a link
PRG="$0"
# Need this for relative symlinks.
while [ -h "$PRG" ] ; do
    ls=`ls -ld "$PRG"`
    link=`expr "$ls" : '.*-> \(.*\)$'`
    if expr "$link" : '/.*' > /dev/null; then
        PRG="$link"
    else
        PRG=`dirname "$PRG"`"/$link"
    fi
done
SAVED="`pwd`"
cd "`dirname \"$PRG\"`/" >/dev/null
APP_HOME="`pwd -P`"
cd "$SAVED" >/dev/null

APP_NAME="Gradle"
APP_BASE_NAME=`basename "$0"`

# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS='"-Xmx64m" "-Xms64m"'

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD="maximum"

warn () {
    echo "$*"
}

die () {
    echo
    echo "$*"
    echo
    exit 1
}

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
nonstop=false
case "`uname`" in
  CYGWIN* )
    cygwin=true
    ;;
  Darwin* )
    darwin=true
    ;;
  MINGW* )
    msys=true
    ;;
  NONSTOP* )
    nonstop=true
    ;;
esac

CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar


# Determine the Java command to use to start the JVM.
if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        # IBM's JDK on AIX uses strange locations for the executables
        JAVACMD="$JAVA_HOME/jre/sh/java"
    else
        JAVACMD="$JAVA_HOME/bin/java"
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD="java"
    which java >/dev/null 2>&1 || die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
fi

# Increase the maximum file descriptors if we can.
if [ "$cygwin" = "false" -a "$darwin" = "false" -a "$nonstop" = "false" ] ; then
    MAX_FD_LIMIT=`ulimit -H -n`
    if [ $? -eq 0 ] ; then
        if [ "$MAX_FD" = "maximum" -o "$MAX_FD" = "max" ] ; then
            MAX_FD="$MAX_FD_LIMIT"
        fi
        ulimit -n $MAX_FD
        if [ $? -ne 0 ] ; then
            warn "Could not set maximum file descriptor limit: $MAX_FD"
        fi
    else
        warn "Could not query maximum file descriptor limit: $MAX_FD_LIMIT"
    fi
fi

# For Darwin, add options to specify how the application appears in the dock
if $darwin; then
    GRADLE_OPTS="$GRADLE_OPTS \"-Xdock:name=$APP_NAME\" \"-Xdock:icon=$APP_HOME/media/gradle.icns\""
fi

# For Cygwin or MSYS, switch paths to Windows format before running java
if [ "$cygwin" = "true" -o "$msys" = "true" ] ; then
    APP_HOME=`cygpath --path --mixed "$APP_HOME"`
    CLASSPATH=`cygpath --path --mixed "$CLASSPATH"`
    
    JAVACMD=`cygpath --unix "$JAVACMD"`

    # We build the pattern for arguments to be converted via cygpath
    ROOTDIRSRAW=`find -L / -maxdepth 1 -mindepth 1 -type d 2>/dev/null`
    SEP=""
    for dir in $ROOTDIRSRAW ; do
        ROOTDIRS="$ROOTDIRS$SEP$dir"
        SEP="|"
    done
    OURCYGPATTERN="(^($ROOTDIRS))"
    # Add a user-defined pattern to the cygpath arguments
    if [ "$GRADLE_CYGPATTERN" != "" ] ; then
        OURCYGPATTERN="$OURCYGPATTERN|($GRADLE_CYGPATTERN)"
    fi
    # Now convert the arguments - kludge to limit ourselves to /bin/sh
    i=0
    for arg in "$@" ; do
        CHECK=`echo "$arg"|egrep -c "$OURCYGPATTERN" -`
        CHECK2=`echo "$arg"|egrep -c "^-"`                                 ### Determine if an option

        if [ $CHECK -ne 0 ] && [ $CHECK2 -eq 0 ] ; then                    ### Added a condition
            eval `echo args$i`=`cygpath --path --ignore --mixed "$arg"`
        else
            eval `echo args$i`="\"$arg\""
        fi
        i=`expr $i + 1`
    done
    case $i in
        0) set -- ;;
        1) set -- "$args0" ;;
        2) set -- "$args0" "$args1" ;;
        3) set -- "$args0" "$args1" "$args2" ;;
        4) set -- "$args0" "$args1" "$args2" "$args3" ;;
        5) set -- "$args0" "$args1" "$args2" "$args3" "$args4" ;;
        6) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" ;;
        7) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" ;;
        8) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" ;;
        9) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" "$args8" ;;
    esac
fi

# Escape application args
save () {
    for i do printf %s\\n "$i" | sed "s/'/'\\\\''/g;1s/^/'/;\$s/\$/' \\\\/" ; done
    echo " "
}
APP_ARGS=`save "$@"`

# Collect all arguments for the java command, following the shell quoting and substitution rules
eval set -- $DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS "\"-Dorg.gradle.appname=$APP_BASE_NAME\"" -classpath "\"$CLASSPATH\"" org.gradle.wrapper.GradleWrapperMain "$APP_ARGS"

exec "$JAVACMD" "$@"
```

## File: `gradlew.bat`
```
@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  Gradle startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%

@rem Resolve any "." and ".." in APP_HOME to make it shorter.
for %%i in ("%APP_HOME%") do set APP_HOME=%%~fi

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS="-Xmx64m" "-Xms64m"

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windows variants

if not "%OS%" == "Windows_NT" goto win9xME_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar


@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %CMD_LINE_ARGS%

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable GRADLE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%GRADLE_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
```

## File: `micronaut-cli.yml`
```yaml
applicationType: default
defaultPackage: com.github.felpexw
testFramework: junit
sourceLanguage: java
buildTool: gradle
features: [annotation-api, app-name, gradle, http-client, java, java-application, junit, logback, lombok, netty-server, readme, shade, yaml]
```

## File: `settings.gradle`
```
rootProject.name="clean-arch-ddd-intro"
```

## File: `gradle/wrapper/gradle-wrapper.properties`
```
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-6.8-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

## File: `src/main/java/com/github/felpexw/Application.java`
```java
package com.github.felpexw;

import io.micronaut.runtime.Micronaut;

public class Application {

	public static void main(String[] args) {
		Micronaut.run(Application.class, args);
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/application/controller/StudentController.java`
```java
package com.github.felpexw.academic.application.controller;

import javax.inject.Inject;

import com.github.felpexw.academic.application.dto.StudentInputDto;
import com.github.felpexw.academic.domain.command.IndicateStudentToClassRoomCommand;
import com.github.felpexw.academic.domain.command.RegisterStudentToClassCommand;
import com.github.felpexw.academic.domain.listener.StudentRegisteredToClassRoomEventListener;
import com.github.felpexw.academic.domain.repository.StudentIndicationRepository;
import com.github.felpexw.gamification.domain.listener.GamificationStudentIndicatedToClassRoomListener;
import com.github.felpexw.shared.domain.common.DomainEventPublisher;
import com.github.felpexw.shared.domain.listener.StudentIndicatedToClassRoomListener;

import io.micronaut.http.HttpResponse;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;

@Controller("/students")
	public class StudentController {

	@Inject
	private StudentIndicationRepository studentIndicationRepository;

	@Inject
	private IndicateStudentToClassRoomCommand indicateSudentPort;

	@Inject
	private DomainEventPublisher publisher;

	@Inject
	private RegisterStudentToClassCommand registerStudentPort;

	@Post(uri = "/indications", consumes = MediaType.APPLICATION_JSON, processes = MediaType.TEXT_PLAIN)
	public HttpResponse<String> indicateStudent(@Body StudentInputDto studentInputDto) {
		initListeners();
		indicateSudentPort.indicateStudent(studentInputDto.student());
		return HttpResponse.ok("Student indicated Sucessfully");
	}

	private void initListeners() {
		publisher.addEventListener(
				new StudentRegisteredToClassRoomEventListener(studentIndicationRepository, publisher));
		publisher.addEventListener(new StudentIndicatedToClassRoomListener());
		publisher.addEventListener(new GamificationStudentIndicatedToClassRoomListener());
	}

	@Post(uri = "/registrations", consumes = MediaType.APPLICATION_JSON, processes = MediaType.TEXT_PLAIN)
	public HttpResponse<String> registerStudent(@Body StudentInputDto studentInputDto) {
		initListeners();
		registerStudentPort.registerStudentToClassRoom(studentInputDto.student());

		return HttpResponse.ok("Student registered sucessfully");
	}
}
```

## File: `src/main/java/com/github/felpexw/academic/application/dto/StudentInputDto.java`
```java
package com.github.felpexw.academic.application.dto;

import javax.validation.Valid;
import javax.validation.constraints.NotEmpty;

import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.academic.domain.model.Student;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Builder
@Valid
@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class StudentInputDto {

	@NotEmpty
	private String cpf;

	@NotEmpty
	private String name;

	public Student student() {
		return Student.builder()//
				.name(name)//
				.cpf(new CPF(cpf))//
				.build();
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/domain/command/IndicateStudentToClassRoomCommand.java`
```java
package com.github.felpexw.academic.domain.command;

import javax.inject.Inject;
import javax.inject.Singleton;

import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.StudentIndicationRepository;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@RequiredArgsConstructor
@Singleton
@Slf4j
public class IndicateStudentToClassRoomCommand {

	@Inject
	private final StudentIndicationRepository repository;;

	public void indicateStudent(Student student) {
		log.info("Indicating student " + student.getCpf().getNumber());

		repository.indicate(student);

		log.info("Student " + student.getCpf().getNumber() + " indicated.");
	}
}
```

## File: `src/main/java/com/github/felpexw/academic/domain/command/NotifyProfessorAboutNewStudentToClassRooCommand.java`
```java
package com.github.felpexw.academic.domain.command;

import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.ProfessorNotifyerRepository;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@RequiredArgsConstructor
@Slf4j
public class NotifyProfessorAboutNewStudentToClassRooCommand {

	private ProfessorNotifyerRepository service;

	public void notify(Student student) {
		log.info(String.format("\n professor has been just notified about the new student. CPF: %s",
				student.getCpf().getNumber()));

		service.notifyProfessor(student);
	}
}
```

## File: `src/main/java/com/github/felpexw/academic/domain/command/RegisterStudentToClassCommand.java`
```java
package com.github.felpexw.academic.domain.command;

import javax.inject.Inject;
import javax.inject.Singleton;

import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomEvent;
import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.ClassRoomRepository;
import com.github.felpexw.shared.domain.common.DomainEventPublisher;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Singleton
public class RegisterStudentToClassCommand {
	@Inject
	private final DomainEventPublisher publisher;

	@Inject
	private final ClassRoomRepository repository;

	public void registerStudentToClassRoom(Student student) {
		try {
			Thread.sleep(1500);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		repository.registerStudent(student);
		publisher.publish(new StudentRegisteredToClassRoomEvent(student.getCpf()));
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/domain/event/StudentRegisteredToClassRoomByIndicationEvent.java`
```java
package com.github.felpexw.academic.domain.event;

import java.util.Map;

import com.github.felpexw.shared.domain.common.DomainEvent;
import com.github.felpexw.shared.domain.common.DomainEventType;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class StudentRegisteredToClassRoomByIndicationEvent implements DomainEvent{
	
	private final String cpf;
	
	@Override
	public Map<String, String> info() {
		return Map.of("cpf", cpf);
	}

	@Override
	public DomainEventType eventType() {
		return DomainEventType.STUDENT_REGISTERED_TO_CLASS_ROOM_BY_INDICATION_EVENT;
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/domain/event/StudentRegisteredToClassRoomEvent.java`
```java
package com.github.felpexw.academic.domain.event;

import java.util.Map;

import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.shared.domain.common.DomainEvent;
import com.github.felpexw.shared.domain.common.DomainEventType;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class StudentRegisteredToClassRoomEvent implements DomainEvent {

	private final CPF cpf;

	@Override
	public Map<String, String> info() {
		return Map.of("cpf", cpf.getNumber());
	}

	@Override
	public DomainEventType eventType() {
		return DomainEventType.STUDENT_REGISTERED_TO_CLASS_ROOM;
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/domain/exception/InvalidCpfException.java`
```java
package com.github.felpexw.academic.domain.exception;

public class InvalidCpfException extends RuntimeException {

	/**
	 * 
	 */
	private static final long serialVersionUID = 4272952226134501263L;

	public InvalidCpfException(String message) {
		super(message);
	}
}
```

## File: `src/main/java/com/github/felpexw/academic/domain/listener/StudentRegisteredToClassRoomEventListener.java`
```java
package com.github.felpexw.academic.domain.listener;

import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomByIndicationEvent;
import com.github.felpexw.academic.domain.repository.StudentIndicationRepository;
import com.github.felpexw.shared.domain.common.DomainEvent;
import com.github.felpexw.shared.domain.common.DomainEventListener;
import com.github.felpexw.shared.domain.common.DomainEventPublisher;
import com.github.felpexw.shared.domain.common.DomainEventType;

import lombok.EqualsAndHashCode;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@EqualsAndHashCode(of = "identification", callSuper = false)
public class StudentRegisteredToClassRoomEventListener extends DomainEventListener {

	private final StudentIndicationRepository repository;
	private final DomainEventPublisher publisher;
	private String identification;

	public StudentRegisteredToClassRoomEventListener(StudentIndicationRepository repository,
			DomainEventPublisher publisher) {
		this.identification = this.identification();
		this.repository = repository;
		this.publisher = publisher;
	}

	@Override
	public void reactTo(DomainEvent evt) {
		log.info(String.format("\n===\n [StudentRegisteredToClassRoomEventListener:%s]:: %s", evt.when(),
				evt.compileInfo()));

		try {
			Thread.sleep(1250);
		} catch (InterruptedException e) {
			log.error(e.getMessage());
		}

		final String ID = evt.info().get("cpf");
		if (repository.itWasIndicated(ID)) {
			publisher.publish(new StudentRegisteredToClassRoomByIndicationEvent(ID));
		}

	}

	@Override
	public String identification() {
		return this.getClass().getName();
	}

	@Override
	public Boolean canRun(DomainEvent evt) {
		return evt.eventType() == DomainEventType.STUDENT_REGISTERED_TO_CLASS_ROOM;
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/domain/model/CPF.java`
```java
package com.github.felpexw.academic.domain.model;

import com.github.felpexw.academic.domain.exception.InvalidCpfException;

import lombok.EqualsAndHashCode;
import lombok.Getter;

@EqualsAndHashCode(of = "number")
@Getter
public class CPF {

	private final String number;

	public CPF(String number) {
		if (number == null || !number.matches("\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}")) {
			throw new InvalidCpfException("CPF document it's not valid!");
		}
		this.number = number;
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/domain/model/Student.java`
```java
package com.github.felpexw.academic.domain.model;

import lombok.Builder;
import lombok.EqualsAndHashCode;
import lombok.Generated;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
@EqualsAndHashCode(of = "cpf")
@Generated
@Builder
public class Student {

	private final CPF cpf;
	private final String name;

}
```

## File: `src/main/java/com/github/felpexw/academic/domain/repository/ClassRoomRepository.java`
```java
package com.github.felpexw.academic.domain.repository;

import com.github.felpexw.academic.domain.model.Student;

public interface ClassRoomRepository {
	
	void registerStudent(Student student);
}
```

## File: `src/main/java/com/github/felpexw/academic/domain/repository/ProfessorNotifyerRepository.java`
```java
package com.github.felpexw.academic.domain.repository;

import com.github.felpexw.academic.domain.model.Student;

public interface ProfessorNotifyerRepository {

	void notifyProfessor(Student student);

}
```

## File: `src/main/java/com/github/felpexw/academic/domain/repository/StudentIndicationRepository.java`
```java
package com.github.felpexw.academic.domain.repository;

import com.github.felpexw.academic.domain.model.Student;

public interface StudentIndicationRepository {

	void indicate(Student student);

	Boolean itWasIndicated(String cpf);

}
```

## File: `src/main/java/com/github/felpexw/academic/infrastructure/repository/ClassRoomRepositoryInMemory.java`
```java
package com.github.felpexw.academic.infrastructure.repository;

import java.util.HashMap;
import java.util.Map;

import javax.inject.Singleton;

import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.ClassRoomRepository;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@RequiredArgsConstructor
@Singleton
@Slf4j
public class ClassRoomRepositoryInMemory implements ClassRoomRepository {

	private Map<String, Student> students = new HashMap<>();

	@Override
	public void registerStudent(Student student) {
		log.info("Registering");
		students.put(student.getCpf().getNumber(), student);
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/infrastructure/repository/ProfessorNotifyerRepositoryImpl.java`
```java
package com.github.felpexw.academic.infrastructure.repository;

import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.ProfessorNotifyerRepository;


public class ProfessorNotifyerRepositoryImpl implements ProfessorNotifyerRepository {

	@Override
	public void notifyProfessor(Student student) {
		// some business logic.
	}

}
```

## File: `src/main/java/com/github/felpexw/academic/infrastructure/repository/StudentIndicationRepositoryInMemory.java`
```java
package com.github.felpexw.academic.infrastructure.repository;

import java.util.HashMap;
import java.util.Map;

import javax.inject.Singleton;

import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.StudentIndicationRepository;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Singleton
public class StudentIndicationRepositoryInMemory implements StudentIndicationRepository {
	
	private final Map<String, Student> indications = new HashMap<>();

	@Override
	public void indicate(Student student) {
		indications.put(student.getCpf().getNumber(), student);
	}

	@Override
	public Boolean itWasIndicated(String cpf) {
		return indications.containsKey(cpf);
	}

}
```

## File: `src/main/java/com/github/felpexw/email/domain/listener/SendEmailToStudentListener.java`
```java
package com.github.felpexw.email.domain.listener;

import com.github.felpexw.shared.domain.common.DomainEvent;
import com.github.felpexw.shared.domain.common.DomainEventListener;
import com.github.felpexw.shared.domain.common.DomainEventType;

import lombok.EqualsAndHashCode;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@EqualsAndHashCode(of = "identification", callSuper = false)
public class SendEmailToStudentListener extends DomainEventListener {

	private String identification;

	public SendEmailToStudentListener() {
		this.identification = identification();
	}

	@Override
	public void reactTo(DomainEvent evt) {
		log.info("\n===\n SendEmailToStudentListener:: Enviando email ....");

		try {
			Thread.sleep(1250);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		log.info("E-mail enviado com sucesso");
	}

	@Override
	public String identification() {
		return this.getClass().getName();
	}

	@Override
	public Boolean canRun(DomainEvent evt) {
		return evt.eventType() == DomainEventType.STUDENT_INDICATED_TO_CLASS_ROOM_EVENT;
	}

}
```

## File: `src/main/java/com/github/felpexw/gamification/domain/command/GenerateStudentBadgeCommand.java`
```java
package com.github.felpexw.gamification.domain.command;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class GenerateStudentBadgeCommand {

	public void generate() {
		try {
			Thread.sleep(1250);
		} catch (InterruptedException e) {
			log.error(e.getMessage());
			e.printStackTrace();
		}

		log.info("Badge generated");
	}

}
```

## File: `src/main/java/com/github/felpexw/gamification/domain/listener/GamificationStudentIndicatedToClassRoomListener.java`
```java
package com.github.felpexw.gamification.domain.listener;

import com.github.felpexw.shared.domain.common.DomainEvent;
import com.github.felpexw.shared.domain.common.DomainEventListener;
import com.github.felpexw.shared.domain.common.DomainEventType;

import lombok.EqualsAndHashCode;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@EqualsAndHashCode(of = "identification", callSuper = false)
public class GamificationStudentIndicatedToClassRoomListener extends DomainEventListener {
	
	private String identification;
	
	public GamificationStudentIndicatedToClassRoomListener() {
		this.identification = this.identification();
	}
	
	@Override
	public void reactTo(DomainEvent evt) {
		log.info(String.format(
				"\n===\n [GamificationStudentIndicatedToClassRoomListener-%s]:: Atualizando os game points na base... CPF: %s",
				evt.when(), evt.info().get("cpf")));
	}

	@Override
	public Boolean canRun(DomainEvent evt) {
		return evt.eventType() == DomainEventType.STUDENT_REGISTERED_TO_CLASS_ROOM_BY_INDICATION_EVENT;
	}

	@Override
	public String identification() {
		return this.getClass().getName();
	}



}
```

## File: `src/main/java/com/github/felpexw/gamification/domain/repository/StudentBadgeRepository.java`
```java
package com.github.felpexw.gamification.domain.repository;

public interface StudentBadgeRepository {
	
	void incrementBadgePoints(String cpf, Integer badgePoint);
}
```

## File: `src/main/java/com/github/felpexw/gamification/infrastructure/StudentBadgeRepositoryInMemory.java`
```java
package com.github.felpexw.gamification.infrastructure;

import java.util.Map;

import com.github.felpexw.gamification.domain.repository.StudentBadgeRepository;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class StudentBadgeRepositoryInMemory implements StudentBadgeRepository {

	private final Map<String, Integer> studentPoints;

	@Override
	public void incrementBadgePoints(String cpf, Integer badgePoint) {
		Integer points = badgePoint;

		if (studentPoints.containsKey(cpf)) {
			final Integer oldPoints = studentPoints.get(cpf);
			points += oldPoints;
		}

		studentPoints.put(cpf, points);
	}

}
```

## File: `src/main/java/com/github/felpexw/shared/domain/common/DomainEvent.java`
```java
package com.github.felpexw.shared.domain.common;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Map;
import java.util.stream.Collectors;

public interface DomainEvent {

	Map<String, String> info();

	default String compileInfo() {
		final Map<String, String> info = info();

		return String.join(": ", info.keySet()//
				.stream()//
				.map(key -> {
					return String.format("key: %s, value: %s", key, info.get(key));
				})//
				.collect(Collectors.toList()));
	}

	DomainEventType eventType();

	default String when() {
		return DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss").format(LocalDateTime.now());
	}
}
```

## File: `src/main/java/com/github/felpexw/shared/domain/common/DomainEventListener.java`
```java
package com.github.felpexw.shared.domain.common;

public abstract class DomainEventListener {

	public abstract void reactTo(DomainEvent evt);

	public abstract Boolean canRun(DomainEvent evt);

	public abstract String identification();

	public void run(DomainEvent evt) {
		if (canRun(evt))
			reactTo(evt);
	}
}
```

## File: `src/main/java/com/github/felpexw/shared/domain/common/DomainEventPublisher.java`
```java
package com.github.felpexw.shared.domain.common;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import javax.inject.Singleton;

import lombok.AllArgsConstructor;
import lombok.Builder;

@AllArgsConstructor
@Builder
@Singleton
public class DomainEventPublisher {

	private final Set<DomainEventListener> events = new HashSet<>();

	public void addEventListener(DomainEventListener listener) {
		this.events.add(listener);
	}

	public Set<DomainEventListener> listeners() {
		return Set.copyOf(new ArrayList<>(events));
	}

	public void publish(DomainEvent evt) {
		this.events.stream().forEach(listener -> listener.run(evt));
	}
}
```

## File: `src/main/java/com/github/felpexw/shared/domain/common/DomainEventType.java`
```java
package com.github.felpexw.shared.domain.common;

public enum DomainEventType {

	STUDENT_REGISTERED_TO_CLASS_ROOM, //
	STUDENT_INDICATED_TO_CLASS_ROOM_EVENT,//
	STUDENT_REGISTERED_TO_CLASS_ROOM_BY_INDICATION_EVENT;
}
```

## File: `src/main/java/com/github/felpexw/shared/domain/event/StudentIndicatedToClassRoomEvent.java`
```java
package com.github.felpexw.shared.domain.event;

import java.util.Map;

import com.github.felpexw.shared.domain.common.DomainEvent;
import com.github.felpexw.shared.domain.common.DomainEventType;

import lombok.EqualsAndHashCode;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@EqualsAndHashCode(of = "cpf", callSuper = false)
public class StudentIndicatedToClassRoomEvent implements DomainEvent {

	private final String cpf;

	@Override
	public Map<String, String> info() {
		return Map.of("cpf", cpf);
	}

	@Override
	public DomainEventType eventType() {
		return DomainEventType.STUDENT_INDICATED_TO_CLASS_ROOM_EVENT;
	}

}
```

## File: `src/main/java/com/github/felpexw/shared/domain/listener/StudentIndicatedToClassRoomListener.java`
```java
package com.github.felpexw.shared.domain.listener;

import com.github.felpexw.shared.domain.common.DomainEvent;
import com.github.felpexw.shared.domain.common.DomainEventListener;
import com.github.felpexw.shared.domain.common.DomainEventType;

import lombok.EqualsAndHashCode;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@EqualsAndHashCode(of = "identification", callSuper = false)
public class StudentIndicatedToClassRoomListener extends DomainEventListener {

	private String identification;

	public StudentIndicatedToClassRoomListener() {
		this.identification = this.identification();
	}

	@Override
	public void reactTo(DomainEvent evt) {
		log.info(String.format("\n===\n [StudentIndicatedToClassRoomListener-%s]:: Enviando email para o estudante...",
				evt.when()));

		try {
			// simulating business logic.
			Thread.sleep(1500);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public String identification() {
		return this.getClass().getName();
	}

	@Override
	public Boolean canRun(DomainEvent evt) {
		return evt.eventType() == DomainEventType.STUDENT_INDICATED_TO_CLASS_ROOM_EVENT;
	}

}
```

## File: `src/main/resources/application.yml`
```yaml
micronaut:
  application:
    name: cleanArchDddIntro
```

## File: `src/main/resources/logback.xml`
```xml
<configuration>

    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <withJansi>false</withJansi>
        <!-- encoders are assigned the type
             ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
        <encoder>
            <pattern>%cyan(%d{HH:mm:ss.SSS}) %gray([%thread]) %highlight(%-5level) %magenta(%logger{36}) - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="info">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>
```

## File: `src/test/java/com/github/felpexw/CleanArchDddIntroTest.java`
```java
package com.github.felpexw;

import io.micronaut.runtime.EmbeddedApplication;
import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

import javax.inject.Inject;

@MicronautTest
class CleanArchDddIntroTest {

    @Inject
    EmbeddedApplication<?> application;

    @Test
    void testItWorks() {
        Assertions.assertTrue(application.isRunning());
    }

}
```

## File: `src/test/java/com/github/felpexw/academic/application/dto/StudentInputDtoTest.java`
```java
package com.github.felpexw.academic.application.dto;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.academic.domain.model.Student;

@DisplayName("[ACADEMIC.application] Student input dto")
class StudentInputDtoTest {

	@Test
	@DisplayName("Parse test")
	void test() {
		final StudentInputDto input = StudentInputDto.builder()//
				.name("Nome")//
				.cpf("111.111.111-11")//
				.build();
		final Student expectedStudent = new Student(new CPF("111.111.111-11"), "Nome");
		final Student actualStudent = input.student();

		Assertions.assertThat(actualStudent).isEqualTo(expectedStudent);
	}

}
```

## File: `src/test/java/com/github/felpexw/academic/domain/command/IndicateStudentToClassRoomCommandTest.java`
```java
package com.github.felpexw.academic.domain.command;

import static org.mockito.Mockito.atMostOnce;
import static org.mockito.Mockito.mockConstruction;
import static org.mockito.Mockito.verify;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockedConstruction;
import org.mockito.MockitoAnnotations;

import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.StudentIndicationRepository;
import com.github.felpexw.shared.domain.common.DomainEventPublisher;
import com.github.felpexw.shared.domain.event.StudentIndicatedToClassRoomEvent;

@DisplayName("[ACADEMIC] Student indication to class room")
class IndicateStudentToClassRoomCommandTest {

	@BeforeEach
	void init() {
		MockitoAnnotations.openMocks(this);
	}

	@Mock
	private DomainEventPublisher mockPublisher;

	@Mock
	private StudentIndicationRepository mockRepository;

	@InjectMocks
	private IndicateStudentToClassRoomCommand indicateStudentToClassRoomCommand;

	@Test
	@DisplayName("When a new student has been indicated to a class, it should triggers an event to another subscriber, and should store this information in the repository")
	void indicateSuccessTest() {
		// setup

		try (MockedConstruction<StudentIndicatedToClassRoomEvent> mockConstruction2 = mockConstruction(
				StudentIndicatedToClassRoomEvent.class)) {

			final Student student = new Student(new CPF("060.116.331-21"), "Juvenal");

			final StudentIndicatedToClassRoomEvent studentIndicatedToClassRoomEvt = new StudentIndicatedToClassRoomEvent(
					student.getCpf().getNumber());

			// action
			indicateStudentToClassRoomCommand.indicateStudent(student);

			// verify
			verify(mockRepository, atMostOnce()).indicate(student);
			verify(mockPublisher, atMostOnce()).publish(studentIndicatedToClassRoomEvt);
		}
	}

}
```

## File: `src/test/java/com/github/felpexw/academic/domain/command/NotifyProfessorAboutNewStudentToClassRooCommandTest.java`
```java
package com.github.felpexw.academic.domain.command;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import static org.mockito.Mockito.*;

import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.ProfessorNotifyerRepository;
import com.github.felpexw.academic.shared.BaseTest;

@DisplayName("[ACADEMIC] Professor notifiyer")
class NotifyProfessorAboutNewStudentToClassRooCommandTest extends BaseTest {

	@Mock
	private ProfessorNotifyerRepository mockService;

	@InjectMocks
	private NotifyProfessorAboutNewStudentToClassRooCommand notifyProfessorCommand;

	@Test
	@DisplayName("When a new student enters the class, the professor should be notified")
	void notifyProfessor() {
		final Student student = new Student(new CPF("060.116.331-12"), "John Doe");
		notifyProfessorCommand.notify(student);

		verify(mockService).notifyProfessor(student);
	}

}
```

## File: `src/test/java/com/github/felpexw/academic/domain/command/RegisterStudentToClassCommandTest.java`
```java
package com.github.felpexw.academic.domain.command;

import static org.mockito.Mockito.atMostOnce;
import static org.mockito.Mockito.mockConstruction;
import static org.mockito.Mockito.verify;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockedConstruction;

import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomEvent;
import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.domain.repository.ClassRoomRepository;
import com.github.felpexw.academic.shared.BaseTest;
import com.github.felpexw.shared.domain.common.DomainEventPublisher;

@DisplayName("[ACADEMIC] Register student to class room use case")
class RegisterStudentToClassCommandTest extends BaseTest {

	@Mock
	private ClassRoomRepository mockRepository;

	@Mock
	private DomainEventPublisher mockPublisher;

	@InjectMocks
	private RegisterStudentToClassCommand registerStudent;

	@Test
	@DisplayName("Register student to the class room")
	void registerStudentTest() {
		try (MockedConstruction<StudentRegisteredToClassRoomEvent> mockConstruction2 = mockConstruction(
				StudentRegisteredToClassRoomEvent.class)) {
			final Student student = new Student(new CPF("123.456.789-12"), "Student stub");
			final StudentRegisteredToClassRoomEvent mockEvt = new StudentRegisteredToClassRoomEvent(student.getCpf());

			registerStudent.registerStudentToClassRoom(student);

			verify(mockRepository, atMostOnce()).registerStudent(student);
			verify(mockPublisher, atMostOnce()).publish(mockEvt);
		}

	}

}
```

## File: `src/test/java/com/github/felpexw/academic/domain/event/StudentRegisteredToClassRoomByIndicationEventTest.java`
```java
package com.github.felpexw.academic.domain.event;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import com.github.felpexw.shared.domain.common.DomainEventType;

@DisplayName("[ACADEMIC] Student registered to class room event indication")
class StudentRegisteredToClassRoomByIndicationEventTest {

	private StudentRegisteredToClassRoomByIndicationEvent evt = new StudentRegisteredToClassRoomByIndicationEvent(
			"123.456.789-12");

	@Test
	@DisplayName("Event type")
	void eventTypeTest() {
		Assertions.assertThat(evt.eventType())
				.isEqualTo(DomainEventType.STUDENT_REGISTERED_TO_CLASS_ROOM_BY_INDICATION_EVENT);
	}

	@Test
	@DisplayName("Event type")
	void infoTest() {
		Assertions.assertThat(evt.info()).hasSize(1);
		Assertions.assertThat(evt.info().containsKey("cpf")).isTrue();
		Assertions.assertThat(evt.info().containsKey("cpf")).isTrue();
		Assertions.assertThat(evt.info().get("cpf")).isEqualTo("123.456.789-12");
	}

}
```

## File: `src/test/java/com/github/felpexw/academic/domain/listener/StudentRegisteredToClassRoomEventListenerTest.java`
```java
package com.github.felpexw.academic.domain.listener;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.atMostOnce;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockedConstruction;
import org.mockito.Mockito;

import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomByIndicationEvent;
import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomEvent;
import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.academic.domain.repository.StudentIndicationRepository;
import com.github.felpexw.academic.shared.BaseTest;
import com.github.felpexw.shared.domain.common.DomainEventPublisher;
import com.github.felpexw.shared.domain.event.StudentIndicatedToClassRoomEvent;

@DisplayName("[ACADEMIC] Student registered to a class room event listener")
class StudentRegisteredToClassRoomEventListenerTest extends BaseTest {

	@Mock
	private StudentIndicationRepository mockRepository;

	@Mock
	private DomainEventPublisher mockPublisher;

	@InjectMocks
	StudentRegisteredToClassRoomEventListener eventListener;

	@Test
	@DisplayName("React to")
	void reactToTest() {
		try (MockedConstruction<StudentRegisteredToClassRoomByIndicationEvent> mockConstruction = Mockito
				.mockConstruction(StudentRegisteredToClassRoomByIndicationEvent.class)) {
			final CPF cpf = new CPF("123.456.789-12");
			final StudentRegisteredToClassRoomEvent evt = new StudentRegisteredToClassRoomEvent(cpf);

			when(mockRepository.itWasIndicated(cpf.getNumber())).thenReturn(true);

			final StudentRegisteredToClassRoomByIndicationEvent studentRegisteredToClassRoomByIndicationEvt = new StudentRegisteredToClassRoomByIndicationEvent(
					"123.123.123-12");

			eventListener.reactTo(evt);

			verify(mockRepository, atMostOnce()).itWasIndicated(cpf.getNumber());
			verify(mockPublisher, atMostOnce()).publish(studentRegisteredToClassRoomByIndicationEvt);

		}

	}

	@Test
	@DisplayName("Can run")
	void canRun() {
		assertThat(eventListener.canRun(new StudentRegisteredToClassRoomEvent(null))).isTrue();
		assertThat(eventListener.canRun(new StudentIndicatedToClassRoomEvent(null))).isFalse();
	}

}
```

## File: `src/test/java/com/github/felpexw/academic/infrastructure/repository/ClassRoomRepositoryInMemoryTest.java`
```java
package com.github.felpexw.academic.infrastructure.repository;

import static org.mockito.Mockito.atMostOnce;
import static org.mockito.Mockito.verify;

import java.util.Map;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;

import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.shared.BaseTest;

@DisplayName("[ACADEMIC] Class room repository")
class ClassRoomRepositoryInMemoryTest extends BaseTest {

	@Mock
	private Map<String, Student> mockStudents;

	@InjectMocks
	private ClassRoomRepositoryInMemory repository;

	@Test
	@DisplayName("Register student to repo")
	void registerStudentTest() {
		final Student student = new Student(new CPF("123.123.123-12"), null);

		repository.registerStudent(student);

		verify(mockStudents, atMostOnce()).put(student.getCpf().getNumber(), student);
	}

}
```

## File: `src/test/java/com/github/felpexw/academic/infrastructure/repository/StudentIndicationRepositoryInMemoryTest.java`
```java
package com.github.felpexw.academic.infrastructure.repository;

import static org.mockito.Mockito.atMostOnce;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.util.Map;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;

import com.github.felpexw.academic.domain.model.CPF;
import com.github.felpexw.academic.domain.model.Student;
import com.github.felpexw.academic.shared.BaseTest;

@DisplayName("[ACADEMIC] Student indication repository in memory")
class StudentIndicationRepositoryInMemoryTest extends BaseTest {

	@Mock
	private Map<String, Student> mockIndications;

	@InjectMocks
	private StudentIndicationRepositoryInMemory repository;

	@Test
	@DisplayName("[ACADEMIC] Student has been indicated")
	void indicateTest() {
		final Student student = new Student(new CPF("123.123.123-12"), "Sebastian");

		repository.indicate(student);

		verify(mockIndications, atMostOnce()).put("123.123.123-12", student);
	}

	@Test
	@DisplayName("Student has been indicated")
	void itWasIndicatedTest() {
		when(mockIndications.containsKey("cpf")).thenReturn(true);

		repository.itWasIndicated("cpf");

		verify(mockIndications, atMostOnce()).containsKey("cpf");
	}

}
```

## File: `src/test/java/com/github/felpexw/academic/shared/BaseTest.java`
```java
package com.github.felpexw.academic.shared;

import org.junit.jupiter.api.BeforeEach;
import org.mockito.MockitoAnnotations;

public class BaseTest {

	@BeforeEach
	final void init() {
		MockitoAnnotations.openMocks(this);
	}

}
```

## File: `src/test/java/com/github/felpexw/email/comand/SendEmailToStudentIndicatedCommandTest.java`
```java
package com.github.felpexw.email.comand;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import com.github.felpexw.email.domain.command.SendEmailToStudentIndicatedCommand;

@DisplayName("[EMAIL] Sending email to someone use case")
class SendEmailToStudentIndicatedCommandTest {

	private SendEmailToStudentIndicatedCommand sendEmailUseCase = new SendEmailToStudentIndicatedCommand();

	@Test
	@DisplayName("[DUMMY TEST] sending email to sommeone test")
	void sendEmailTest() {
		sendEmailUseCase.sendEmail("123123");
	}

}
```

## File: `src/test/java/com/github/felpexw/email/listener/SendEmailToStudentListenerTest.java`
```java
package com.github.felpexw.email.listener;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomByIndicationEvent;
import com.github.felpexw.academic.shared.BaseTest;
import com.github.felpexw.email.domain.listener.SendEmailToStudentListener;
import com.github.felpexw.shared.domain.event.StudentIndicatedToClassRoomEvent;

@DisplayName("[EMAIL] Send email to someone event listener")
class SendEmailToStudentListenerTest extends BaseTest {

	private SendEmailToStudentListener evtListener = new SendEmailToStudentListener();

	@Test
	@DisplayName("Can run")
	void canRunTest() {
		assertThat(evtListener.canRun(new StudentIndicatedToClassRoomEvent(null))).isTrue();
		assertThat(evtListener.canRun(new StudentRegisteredToClassRoomByIndicationEvent(null))).isFalse();
	}

	@Test
	@DisplayName("[DUMMY TEST] Can run")
	void reactToTest() {
		evtListener.reactTo(new StudentIndicatedToClassRoomEvent(null));
	}

}
```

## File: `src/test/java/com/github/felpexw/gamification/domain/command/GenerateStudentBadgeCommandTest.java`
```java
package com.github.felpexw.gamification.domain.command;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("[GAMIFICATION] Generate student badge command")
class GenerateStudentBadgeCommandTest {

	@Test
	@DisplayName("[DUMMY TEST] generate")
	void generateDummyTest() {
		new GenerateStudentBadgeCommand().generate();
	}

}
```

## File: `src/test/java/com/github/felpexw/gamification/domain/listener/GamificationStudentIndicatedToClassRoomListenerTest.java`
```java
package com.github.felpexw.gamification.domain.listener;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomByIndicationEvent;
import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomEvent;
import com.github.felpexw.academic.domain.model.CPF;

@DisplayName("[GAMEFICIATION DOMAIN] Student indicated to class room listener")
class GamificationStudentIndicatedToClassRoomListenerTest {
	private GamificationStudentIndicatedToClassRoomListener listener = new GamificationStudentIndicatedToClassRoomListener();

	@Test
	@DisplayName("[DUMMY TEST] react to")
	void reactToTest() {
		listener.reactTo(new StudentRegisteredToClassRoomEvent(new CPF("123.456.789-12")));
	}

	@Test
	@DisplayName("Can run")
	void canRunTestd() {
		assertThat(listener.canRun(new StudentRegisteredToClassRoomByIndicationEvent(null))).isTrue();
		assertThat(listener.canRun(new StudentRegisteredToClassRoomEvent(null))).isFalse();
	}

}
```

## File: `src/test/java/com/github/felpexw/gamification/infrastructure/StudentBadgeRepositoryInMemoryTest.java`
```java
package com.github.felpexw.gamification.infrastructure;

import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.util.Map;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;

import com.github.felpexw.academic.shared.BaseTest;

@DisplayName("[GAMEFICIATION] Student badge repository in memory")
class StudentBadgeRepositoryInMemoryTest extends BaseTest {

	@Mock
	private Map<String, Integer> mockStudentPoints;

	@InjectMocks
	private StudentBadgeRepositoryInMemory repository;

	@Test
	@DisplayName("[GAMEFICIATION] Increment badge points")
	void incrementBadgePointsTest() {
		when(mockStudentPoints.containsKey("key"))//
		.thenReturn(true)//
		.thenReturn(false);
		
		when(mockStudentPoints.get("key")).thenReturn(10);

		repository.incrementBadgePoints("key", 10);
		repository.incrementBadgePoints("key", 15);

		verify(mockStudentPoints, times(1)).put("key", 20);
		verify(mockStudentPoints, times(1)).put("key", 15);
	}

}
```

## File: `src/test/java/com/github/felpexw/shared/domain/common/DomainEventPublisherTest.java`
```java
package com.github.felpexw.shared.domain.common;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import com.github.felpexw.academic.shared.BaseTest;

@DisplayName("[ACADEMIC] Publish events and add event listeners handler")
class DomainEventPublisherTest extends BaseTest {

	private final DomainEventPublisher publisher = new DomainEventPublisher();

	@Test
	@DisplayName("Add event listener to the publisher")
	void addEventListenerTest() {
		final DomainEventListener evt = mock(DomainEventListener.class);
		publisher.addEventListener(evt);

		assertThat(publisher.listeners()).hasSize(1);
	}

}
```

## File: `src/test/java/com/github/felpexw/shared/domain/event/StudentIndicatedToClassRoomEventTest.java`
```java
package com.github.felpexw.shared.domain.event;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import com.github.felpexw.academic.shared.BaseTest;
import com.github.felpexw.shared.domain.common.DomainEventType;

@DisplayName("[SHARED] Student indicated to class room event")
class StudentIndicatedToClassRoomEventTest extends BaseTest {

	private final StudentIndicatedToClassRoomEvent evt = new StudentIndicatedToClassRoomEvent("123.456.789-12");

	@Test
	@DisplayName("Test if the indicated to class room event information it's returning as expected")
	void infoTest() {
		assertThat(evt.info()).hasSize(1);
		assertThat(evt.info()).containsKey("cpf");
		assertThat(evt.info().get("cpf")).isEqualTo("123.456.789-12");
	}

	@Test
	@DisplayName("Test if it's returning the right event type")
	void eventTypeTest() {
		assertThat(evt.eventType()).isEqualTo(DomainEventType.STUDENT_INDICATED_TO_CLASS_ROOM_EVENT);
	}

	@Test
	@DisplayName("Test if compile name it's corret")
	public void compileInfoTest() {
		assertThat(evt.compileInfo()).isEqualTo("key: cpf, value: 123.456.789-12");
	}
}
```

## File: `src/test/java/com/github/felpexw/shared/domain/listener/StudentIndicatedToClassRoomListenerTest.java`
```java
package com.github.felpexw.shared.domain.listener;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;

import com.github.felpexw.academic.domain.event.StudentRegisteredToClassRoomByIndicationEvent;
import com.github.felpexw.academic.shared.BaseTest;
import com.github.felpexw.shared.domain.event.StudentIndicatedToClassRoomEvent;

@DisplayName("[SHARED] Student has been indicated to a class room listener")
class StudentIndicatedToClassRoomListenerTest extends BaseTest {

	@InjectMocks
	private StudentIndicatedToClassRoomListener listener;

	@Test
	@DisplayName("When a new student has been registered, it sould only listen to this event.")
	void canRunTest() {
		assertTrue(listener.canRun(new StudentIndicatedToClassRoomEvent("123.456.789-12")), () -> "assert true ok");
		assertFalse(listener.canRun(new StudentRegisteredToClassRoomByIndicationEvent("123.456.789-12")),
				() -> "assert false ok");
	}

	@Test
	@DisplayName("Dummy test")
	public void dummyTest() {
		listener.reactTo(new StudentIndicatedToClassRoomEvent("123.123.123-12"));
	}

}
```

