---
id: php
type: knowledge
owner: OA_Triage
---
# php
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <a href="https://codely.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://codely.com/logo/codely_logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://codely.com/logo/codely_logo-light.svg">
      <img alt="Codely logo" src="https://codely.com/logo/codely_logo.svg">
    </picture>
  </a>
</p>

<h1 align="center">
  🐘🎯 Hexagonal Architecture, DDD & CQRS in PHP
</h1>

<p align="center">
    <a href="https://github.com/CodelyTV"><img src="https://img.shields.io/badge/Codely-OS-green.svg?style=flat-square" alt="Codely Open Source projects"/></a>
    <a href="http://pro.codely.tv"><img src="https://img.shields.io/badge/CodelyTV-PRO-black.svg?style=flat-square" alt="CodelyTV Courses"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Symfony-7-purple.svg?style=flat-square&logo=symfony" alt="Symfony 7"/></a>
    <a href="https://shepherd.dev/github/CodelyTV/php-ddd-example"><img src="https://shepherd.dev/github/CodelyTV/php-ddd-example/coverage.svg" alt="Type Coverage"/></a>
    <a href="https://github.com/CodelyTV/php-ddd-example/actions"><img src="https://github.com/CodelyTV/php-ddd-example/workflows/CI/badge.svg?branch=master" alt="CI pipeline status" /></a>
</p>

<p align="center">
  Example of a <strong>PHP application using Domain-Driven Design (DDD) and Command Query Responsibility Segregation
  (CQRS) principles</strong> keeping the code as simple as possible.
  <br />
  <br />
  Take a look, play and have fun with this.
  <a href="https://github.com/CodelyTV/php-ddd-example/stargazers">Stars are welcome 😊</a>
  <br />
  <br />
  <a href="https://www.youtube.com/watch?v=1kaP39W80zQ">View Demo</a>
  ·
  <a href="https://github.com/CodelyTV/php-ddd-example/issues">Report a bug</a>
  ·
  <a href="https://github.com/CodelyTV/php-ddd-example/issues">Request a feature</a>
</p>

## 🚀 Environment Setup

### 🐳 Needed tools

1. [Install Docker](https://www.docker.com/get-started)
2. Clone this project: `git clone https://github.com/CodelyTV/php-ddd-example php-ddd-example`
3. Move to the project folder: `cd php-ddd-example`

### 🛠️ Environment configuration

1. Create a local environment file (`cp .env .env.local`) if you want to modify any parameter

### 🔥 Application execution

1. Install all the dependencies and bring up the project with Docker executing: `make build`
2. Then you'll have 3 apps available (2 APIs and 1 Frontend):
   1. [Mooc Backend](apps/mooc/backend): http://localhost:8030/health-check
   2. [Backoffice Backend](apps/backoffice/backend): http://localhost:8040/health-check
   3. [Backoffice Frontend](apps/backoffice/frontend): http://localhost:8041/health-check

### ✅ Tests execution

1. Install the dependencies if you haven't done it previously: `make deps`
2. Execute PHPUnit and Behat tests: `make test`

## 👩‍💻 Project explanation

This project tries to be a MOOC (Massive Open Online Course) platform. It's decoupled from any framework, but it has
some Symfony and Laravel implementations.

### ⛱️ Bounded Contexts

- [Mooc](src/Mooc): Place to look in if you wanna see some code 🙂. Massive Open Online Courses public platform with users, videos, notifications, and so on.
- [Backoffice](src/Backoffice): Here you'll find the use cases needed by the Customer Support department in order to manage users, courses, videos, and so on.

### 🎯 Hexagonal Architecture

This repository follows the Hexagonal Architecture pattern. Also, it's structured using `modules`.
With this, we can see that the current structure of a Bounded Context is:

```scala
$ tree -L 4 src

src
|-- Mooc // Company subdomain / Bounded Context: Features related to one of the company business lines / products
|   `-- Videos // Some Module inside the Mooc context
|       |-- Application
|       |   |-- Create // Inside the application layer all is structured by actions
|       |   |   |-- CreateVideoCommand.php
|       |   |   |-- CreateVideoCommandHandler.php
|       |   |   `-- VideoCreator.php
|       |   |-- Find
|       |   |-- Trim
|       |   `-- Update
|       |-- Domain
|       |   |-- Video.php // The Aggregate of the Module
|       |   |-- VideoCreatedDomainEvent.php // A Domain Event
|       |   |-- VideoFinder.php
|       |   |-- VideoId.php
|       |   |-- VideoNotFound.php
|       |   |-- VideoRepository.php // The `Interface` of the repository is inside Domain
|       |   |-- VideoTitle.php
|       |   |-- VideoType.php
|       |   |-- VideoUrl.php
|       |   `-- Videos.php // A collection of our Aggregate
|       `-- Infrastructure // The infrastructure of our module
|           |-- DependencyInjection
|           `-- Persistence
|               `--MySqlVideoRepository.php // An implementation of the repository
`-- Shared // Shared Kernel: Common infrastructure and domain shared between the different Bounded Contexts
    |-- Domain
    `-- Infrastructure
```

#### Repository pattern

Our repositories try to be as simple as possible usually only containing 2 methods `search` and `save`.
If we need some query with more filters we use the `Specification` pattern also known as `Criteria` pattern. So we add a
`searchByCriteria` method.

You can see an example [here](src/Mooc/Courses/Domain/CourseRepository.php)
and its implementation [here](src/Mooc/Courses/Infrastructure/Persistence/DoctrineCourseRepository.php).

### Aggregates

You can see an example of an aggregate [here](src/Mooc/Courses/Domain/Course.php). All aggregates should
extend the [AggregateRoot](src/Shared/Domain/Aggregate/AggregateRoot.php).

### Command Bus

There is 1 implementations of the [command bus](src/Shared/Domain/Bus/Command/CommandBus.php).
1. [Sync](src/Shared/Infrastructure/Bus/Command/InMemorySymfonyCommandBus.php) using the Symfony Message Bus.


### Query Bus

The [Query Bus](src/Shared/Infrastructure/Bus/Query/InMemorySymfonyQueryBus.php) uses the Symfony Message Bus.

### Event Bus

The [Event Bus](src/Shared/Infrastructure/Bus/Event/InMemory/InMemorySymfonyEventBus.php) uses the Symfony Message Bus.
The [MySql Bus](src/Shared/Infrastructure/Bus/Event/MySql/MySqlDoctrineEventBus.php) uses a MySql+Pulling as a bus.
The [RabbitMQ Bus](src/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqEventBus.php) uses RabbitMQ C extension.

## 📱 Monitoring

Every time a domain event is published it's exported to Prometheus. You can access to the Prometheus panel [here](http://localhost:9999/).

## 🤔 Contributing

There are some things missing (add swagger, improve documentation...), feel free to add this if you want! If you want
some guidelines feel free to contact us :)

## 🤩 Extra

This code was shown in the [From framework coupled code to #microservices through #DDD](http://codely.tv/blog/screencasts/codigo-acoplado-framework-microservicios-ddd) talk and doubts where answered in the [DDD y CQRS: Preguntas Frecuentes](https://codely.com/blog/ddd-cqrs-preguntas-frecuentes) video.


🎥 Used in the CodelyTV Pro courses:

- [🇪🇸 DDD in PHP](https://pro.codely.tv/library/ddd-en-php/about/)
- [🇪🇸 Arquitectura Hexagonal](https://pro.codely.tv/library/arquitectura-hexagonal/66748/about/)
- [🇪🇸 CQRS: Command Query Responsibility Segregation](https://pro.codely.tv/library/cqrs-command-query-responsibility-segregation-3719e4aa/62554/about/)
- [🇪🇸 Comunicación entre microservicios: Event-Driven Architecture](https://pro.codely.tv/library/comunicacion-entre-microservicios-event-driven-architecture/74823/about/)

## 🌐 remember to visit our courses

- [Courses codely](https://codely.com/cursos)

```

### File: composer.json
```json
{
  "name": "codelytv/php-ddd-example",
  "license": "MIT",
  "type": "project",
  "description": "An example project applying Domain-Driven Design, Hexagonal Architecture and CQRS in a Monorepository",
  "require": {
    "php": "^8.3",

    "ext-amqp": "*",
    "ext-apcu": "*",
    "ext-json": "*",
    "ext-zend-opcache": "*",
    "ext-pdo": "*",

    "symfony/framework-bundle": "^7",
    "symfony/messenger": "^7",
    "symfony/dotenv": "^7",
    "symfony/yaml": "^7",
    "symfony/twig-bundle": "^7",
    "symfony/validator": "^7",
    "symfony/cache": "^7",

    "lambdish/phunctional": "^2",

    "ramsey/uuid": "^4",

    "doctrine/dbal": "^3",
    "doctrine/orm": "^2",

    "ocramius/proxy-manager": "^2",
    "laminas/laminas-zendframework-bridge": "^1",

    "elasticsearch/elasticsearch": "^7",
    "monolog/monolog": "^3",

    "promphp/prometheus_client_php": "^2.7.2"
  },
  "require-dev": {
    "ext-xdebug": "*",

    "roave/security-advisories": "dev-master",

    "behat/behat": "^3.13",
    "friends-of-behat/mink-extension": "2.7.5",
    "friends-of-behat/symfony-extension": "2.6.0",
    "behat/mink-browserkit-driver": "2.2.0",

    "phpunit/phpunit": "^9",
    "mockery/mockery": "^1",

    "fakerphp/faker": "^1",

    "symfony/error-handler": "^7",

    "symplify/easy-coding-standard": "^12.0",
    "vimeo/psalm": "^5.15",
    "rector/rector": "^0.18.12",
    "psalm/plugin-mockery": "^1.1",
    "psalm/plugin-symfony": "^5.0",
    "psalm/plugin-phpunit": "^0.18.4",
    "phpstan/phpstan": "^1.10",
    "phpat/phpat": "^0.10.10",
    "phpmd/phpmd": "^2.14",
    "codelytv/coding-style": "^1.1"
  },
  "autoload": {
    "psr-4": {
      "CodelyTv\\Apps\\Mooc\\Backend\\": "apps/mooc/backend/src",
      "CodelyTv\\Apps\\Mooc\\Frontend\\": "apps/mooc/frontend/src",

      "CodelyTv\\Apps\\Backoffice\\Backend\\": "apps/backoffice/backend/src",
      "CodelyTv\\Apps\\Backoffice\\Frontend\\": "apps/backoffice/frontend/src",

      "CodelyTv\\": ["src"]
    }
  },
  "autoload-dev": {
    "psr-4": {
      "CodelyTv\\Tests\\": ["tests"]
    }
  },
  "minimum-stability": "RC",
  "config": {
    "allow-plugins": {
      "ocramius/package-versions": true
    }
  }
}

```

### File: ecs.php
```php
<?php

declare(strict_types=1);

use CodelyTv\CodingStyle;
use PhpCsFixer\Fixer\ClassNotation\FinalClassFixer;
use Symplify\EasyCodingStandard\Config\ECSConfig;

return function (ECSConfig $ecsConfig): void {
	$ecsConfig->paths([__DIR__ . '/apps', __DIR__ . '/src', __DIR__ . '/tests', ]);

	$ecsConfig->sets([CodingStyle::DEFAULT]);

	$ecsConfig->skip([
		FinalClassFixer::class => [
			__DIR__ . '/apps/backoffice/backend/src/BackofficeBackendKernel.php',
			__DIR__ . '/apps/backoffice/frontend/src/BackofficeFrontendKernel.php',
			__DIR__ . '/apps/mooc/backend/src/MoocBackendKernel.php',
			__DIR__ . '/src/Shared/Infrastructure/Bus/Event/InMemory/InMemorySymfonyEventBus.php',
		],
		__DIR__ . '/apps/backoffice/backend/var',
		__DIR__ . '/apps/backoffice/frontend/var',
		__DIR__ . '/apps/mooc/backend/var',
		__DIR__ . '/apps/mooc/frontend/var',
	]);
};

```

### File: rector.php
```php
<?php

declare(strict_types=1);

use Rector\Config\RectorConfig;
use Rector\Set\ValueObject\LevelSetList;
use Rector\Set\ValueObject\SetList;

return static function (RectorConfig $rectorConfig): void {
    $rectorConfig->paths([
        __DIR__ . '/apps',
        __DIR__ . '/src',
        __DIR__ . '/tests',
    ]);

    $rectorConfig->sets([
        LevelSetList::UP_TO_PHP_82,
        SetList::TYPE_DECLARATION
    ]);

    $rectorConfig->skip([
        __DIR__ . '/apps/backoffice/backend/var',
        __DIR__ . '/apps/backoffice/frontend/var',
        __DIR__ . '/apps/mooc/backend/var',
        __DIR__ . '/apps/mooc/frontend/var',
    ]);
};

```

### File: apps\bootstrap.php
```php
<?php

declare(strict_types=1);

use Symfony\Component\Dotenv\Dotenv;

$rootPath = dirname(__DIR__);

require $rootPath . '/vendor/autoload.php';

(new Dotenv())->loadEnv($rootPath . '/.env');

$_SERVER += $_ENV;
$_SERVER['APP_ENV'] = $_ENV['APP_ENV'] = ($_SERVER['APP_ENV'] ?? $_ENV['APP_ENV'] ?? null) ?: 'dev';
$_SERVER['APP_DEBUG'] ??= $_ENV['APP_DEBUG'] ?? $_SERVER['APP_ENV'] !== 'prod';
$_SERVER['APP_DEBUG'] = $_ENV['APP_DEBUG'] =
	(int) $_SERVER['APP_DEBUG'] || filter_var($_SERVER['APP_DEBUG'], FILTER_VALIDATE_BOOLEAN) ? '1' : '0';

```

### File: tests\Mooc\MoocArchitectureTest.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc;

use CodelyTv\Tests\Shared\Infrastructure\ArchitectureTest;
use PHPat\Selector\Selector;
use PHPat\Test\Builder\Rule;
use PHPat\Test\PHPat;

final class MoocArchitectureTest
{
	public function test_mooc_domain_should_only_import_itself_and_shared(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Domain/', true))
			->canOnlyDependOn()
			->classes(...array_merge(ArchitectureTest::languageClasses(), [
				// Itself
				Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Domain/', true),
				// Shared
				Selector::inNamespace('CodelyTv\Shared\Domain'),
			]))
			->because('mooc domain can only import itself and shared domain');
	}

	public function test_mooc_application_should_only_import_itself_and_domain(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Application/', true))
			->canOnlyDependOn()
			->classes(...array_merge(ArchitectureTest::languageClasses(), [
				// Itself
				Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Application/', true),
				Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Domain/', true),
				// Shared
				Selector::inNamespace('CodelyTv\Shared'),
			]))
			->because('mooc application can only import itself and shared');
	}

	public function test_mooc_infrastructure_should_not_import_other_contexts_beside_shared(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('CodelyTv\Mooc'))
			->shouldNotDependOn()
			->classes(Selector::inNamespace('CodelyTv'))
			->excluding(
				// Itself
				Selector::inNamespace('CodelyTv\Mooc'),
				// Shared
				Selector::inNamespace('CodelyTv\Shared'),
			);
	}
}

```

### File: tests\Shared\SharedArchitectureTest.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared;

use CodelyTv\Backoffice\Auth\Application\Authenticate\AuthenticateUserCommand;
use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use CodelyTv\Shared\Domain\Bus\Query\Response;
use CodelyTv\Tests\Shared\Infrastructure\ArchitectureTest;
use CodelyTv\Tests\Shared\Infrastructure\Doctrine\MySqlDatabaseCleaner;
use PHPat\Selector\Selector;
use PHPat\Test\Builder\Rule;
use PHPat\Test\PHPat;
use Ramsey\Uuid\Uuid;

final class SharedArchitectureTest
{
	public function test_shared_domain_should_not_import_from_outside(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('CodelyTv\Shared\Domain'))
			->canOnlyDependOn()
			->classes(...array_merge(ArchitectureTest::languageClasses(), [
				// Itself
				Selector::inNamespace('CodelyTv\Shared\Domain'),
				// Dependencies treated as domain
				Selector::classname(Uuid::class),
			]))
			->because('shared domain cannot import from outside');
	}

	public function test_shared_infrastructure_should_not_import_from_other_contexts(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('CodelyTv\Shared\Infrastructure'))
			->shouldNotDependOn()
			->classes(Selector::inNamespace('CodelyTv'))
			->excluding(
				// Itself
				Selector::inNamespace('CodelyTv\Shared'),
				// This need to be refactored
				Selector::classname(MySqlDatabaseCleaner::class),
				Selector::classname(AuthenticateUserCommand::class),
				Selector::inNamespace('CodelyTv\Backoffice\Auth'),
			);
	}

	public function test_all_use_cases_can_only_have_one_public_method(): Rule
	{
		return PHPat::rule()
			->classes(
				Selector::classname('/^CodelyTv\\\\.+\\\\.+\\\\Application\\\\.+\\\\(?!.*(?:Command|Query)$).*$/', true)
			)
			->excluding(
				Selector::implements(Response::class),
				Selector::implements(DomainEventSubscriber::class),
				Selector::inNamespace('/.*\\\\Tests\\\\.*/', true)
			)
			->shouldHaveOnlyOnePublicMethod();
	}
}

```

### File: etc\databases\backoffice\courses.json
```json
{
  "mappings": {
    "courses": {
      "properties": {
        "id": {
          "type": "keyword",
          "index": true
        },
        "name": {
          "type": "text",
          "index": true
        },
        "duration": {
          "type": "text",
          "index": true
        }
      }
    }
  }
}

```

### File: src\Shared\Domain\Assert.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use InvalidArgumentException;

final class Assert
{
	public static function arrayOf(string $class, array $items): void
	{
		foreach ($items as $item) {
			self::instanceOf($class, $item);
		}
	}

	public static function instanceOf(string $class, mixed $item): void
	{
		if (!$item instanceof $class) {
			throw new InvalidArgumentException(sprintf('The object <%s> is not an instance of <%s>', $class, $item::class));
		}
	}
}

```

### File: src\Shared\Domain\Collection.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use ArrayIterator;
use Countable;
use IteratorAggregate;
use Traversable;

/** @template-implements IteratorAggregate<mixed>*/
abstract class Collection implements Countable, IteratorAggregate
{
	public function __construct(private readonly array $items)
	{
		Assert::arrayOf($this->type(), $items);
	}

	abstract protected function type(): string;

	final public function getIterator(): Traversable
	{
		return new ArrayIterator($this->items());
	}

	final public function count(): int
	{
		return count($this->items());
	}

	protected function items(): array
	{
		return $this->items;
	}
}

```

### File: src\Shared\Domain\DomainError.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use DomainException;

abstract class DomainError extends DomainException
{
	public function __construct()
	{
		parent::__construct($this->errorMessage());
	}

	abstract public function errorCode(): string;

	abstract protected function errorMessage(): string;
}

```

### File: src\Shared\Domain\Logger.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

interface Logger
{
	public function info(string $message, array $context = []): void;

	public function warning(string $message, array $context = []): void;

	public function critical(string $message, array $context = []): void;
}

```

### File: src\Shared\Domain\Monitoring.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

interface Monitoring
{
	public function incrementCounter(int $times): void;

	public function incrementGauge(int $times): void;

	public function decrementGauge(int $times): void;

	public function setGauge(int $value): void;

	public function observeHistogram(int $value, array $labels = []): void;
}

```

### File: src\Shared\Domain\RandomNumberGenerator.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

interface RandomNumberGenerator
{
	public function generate(): int;
}

```

### File: src\Shared\Domain\Second.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use CodelyTv\Shared\Domain\ValueObject\IntValueObject;

final class Second extends IntValueObject {}

```

### File: src\Shared\Domain\SecondsInterval.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use DomainException;

final readonly class SecondsInterval
{
	public function __construct(private Second $from, private Second $to)
	{
		$this->ensureIntervalEndsAfterStart($from, $to);
	}

	public static function fromValues(int $from, int $to): self
	{
		return new self(new Second($from), new Second($to));
	}

	private function ensureIntervalEndsAfterStart(Second $from, Second $to): void
	{
		if ($from->isBiggerThan($to)) {
			throw new DomainException('To is bigger than from');
		}
	}
}

```

### File: src\Shared\Domain\Utils.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use DateTimeImmutable;
use DateTimeInterface;
use function Lambdish\Phunctional\filter;

final class Utils
{
	public static function dateToString(DateTimeInterface $date): string
	{
		return $date->format(DateTimeInterface::ATOM);
	}

	public static function stringToDate(string $date): DateTimeImmutable
	{
		return new DateTimeImmutable($date);
	}

	public static function jsonEncode(array $values): string
	{
		return json_encode($values, JSON_THROW_ON_ERROR);
	}

	public static function jsonDecode(string $json): array
	{
		return json_decode($json, true, flags: JSON_THROW_ON_ERROR);
	}

	public static function toSnakeCase(string $text): string
	{
		return ctype_lower($text) ? $text : strtolower((string) preg_replace('/([^A-Z\s])([A-Z])/', '$1_$2', $text));
	}

	public static function toCamelCase(string $text): string
	{
		return lcfirst(str_replace('_', '', ucwords($text, '_')));
	}

	public static function dot(array $array, string $prepend = ''): array
	{
		$results = [];
		foreach ($array as $key => $value) {
			if (is_array($value) && !empty($value)) {
				$results = array_merge($results, self::dot($value, $prepend . $key . '.'));
			} else {
				$results[$prepend . $key] = $value;
			}
		}

		return $results;
	}

	public static function filesIn(string $path, string $fileType): array
	{
		return filter(
			static fn (string $possibleModule): false | string => strstr($possibleModule, $fileType),
			scandir($path)
		);
	}

	public static function iterableToArray(iterable $iterable): array
	{
		if (is_array($iterable)) {
			return $iterable;
		}

		return iterator_to_array($iterable);
	}
}

```

### File: src\Shared\Domain\UuidGenerator.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

interface UuidGenerator
{
	public function generate(): string;
}

```

### File: src\Shared\Infrastructure\PhpRandomNumberGenerator.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure;

use CodelyTv\Shared\Domain\RandomNumberGenerator;

final class PhpRandomNumberGenerator implements RandomNumberGenerator
{
	public function generate(): int
	{
		return random_int(1, 5);
	}
}

```

### File: src\Shared\Infrastructure\RamseyUuidGenerator.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure;

use CodelyTv\Shared\Domain\UuidGenerator;
use Ramsey\Uuid\Uuid;

final class RamseyUuidGenerator implements UuidGenerator
{
	public function generate(): string
	{
		return Uuid::uuid4()->toString();
	}
}

```

### File: tests\Backoffice\Auth\AuthModuleUnitTestCase.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Auth;

use CodelyTv\Backoffice\Auth\Domain\AuthRepository;
use CodelyTv\Backoffice\Auth\Domain\AuthUser;
use CodelyTv\Backoffice\Auth\Domain\AuthUsername;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\UnitTestCase;
use Mockery\MockInterface;

abstract class AuthModuleUnitTestCase extends UnitTestCase
{
	private AuthRepository | MockInterface | null $repository = null;

	protected function shouldSearch(AuthUsername $username, AuthUser $authUser = null): void
	{
		$this->repository()
			->shouldReceive('search')
			->with($this->similarTo($username))
			->once()
			->andReturn($authUser);
	}

	protected function repository(): AuthRepository | MockInterface
	{
		return $this->repository ??= $this->mock(AuthRepository::class);
	}
}

```

### File: tests\Backoffice\Courses\BackofficeCoursesModuleInfrastructureTestCase.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Courses;

use CodelyTv\Backoffice\Courses\Infrastructure\Persistence\ElasticsearchBackofficeCourseRepository;
use CodelyTv\Backoffice\Courses\Infrastructure\Persistence\MySqlBackofficeCourseRepository;
use CodelyTv\Tests\Backoffice\Shared\Infraestructure\PhpUnit\BackofficeContextInfrastructureTestCase;
use Doctrine\ORM\EntityManager;

abstract class BackofficeCoursesModuleInfrastructureTestCase extends BackofficeContextInfrastructureTestCase
{
	protected function mySqlRepository(): MySqlBackofficeCourseRepository
	{
		return new MySqlBackofficeCourseRepository($this->service(EntityManager::class));
	}

	protected function elasticRepository(): ElasticsearchBackofficeCourseRepository
	{
		return $this->service(ElasticsearchBackofficeCourseRepository::class);
	}
}

```

### File: tests\Mooc\Courses\CoursesModuleInfrastructureTestCase.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses;

use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Tests\Mooc\Shared\Infrastructure\PhpUnit\MoocContextInfrastructureTestCase;

abstract class CoursesModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase
{
	protected function repository(): CourseRepository
	{
		return $this->service(CourseRepository::class);
	}
}

```

### File: tests\Mooc\Courses\CoursesModuleUnitTestCase.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses;

use CodelyTv\Mooc\Courses\Domain\Course;
use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\UnitTestCase;
use Mockery\MockInterface;

abstract class CoursesModuleUnitTestCase extends UnitTestCase
{
	private CourseRepository | MockInterface | null $repository = null;

	protected function shouldSave(Course $course): void
	{
		$this->repository()
			->shouldReceive('save')
			->with($this->similarTo($course))
			->once()
			->andReturnNull();
	}

	protected function shouldSearch(CourseId $id, ?Course $course): void
	{
		$this->repository()
			->shouldReceive('search')
			->with($this->similarTo($id))
			->once()
			->andReturn($course);
	}

	protected function repository(): CourseRepository | MockInterface
	{
		return $this->repository ??= $this->mock(CourseRepository::class);
	}
}

```

### File: tests\Mooc\Steps\StepsModuleInfrastructureTestCase.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps;

use CodelyTv\Mooc\Steps\Domain\StepRepository;
use CodelyTv\Tests\Mooc\Shared\Infrastructure\PhpUnit\MoocContextInfrastructureTestCase;

abstract class StepsModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase
{
	protected function repository(): StepRepository
	{
		return $this->service(StepRepository::class);
	}
}

```

### File: tests\Shared\Domain\DuplicatorMother.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

use ReflectionObject;
use ReflectionProperty;

use function Lambdish\Phunctional\each;

final class DuplicatorMother
{
	public static function with(mixed $object, array $newParams): mixed
	{
		$duplicated = clone $object;
		$reflection = new ReflectionObject($duplicated);

		each(
			static function (ReflectionProperty $property) use ($duplicated, $newParams): void {
				if (isset($newParams[$property->getName()])) {
					$property->setAccessible(true);
					$property->setValue($duplicated, $newParams[$property->getName()]);
				}
			},
			$reflection->getProperties()
		);

		return $duplicated;
	}
}

```

### File: tests\Shared\Domain\IntegerMother.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

final class IntegerMother
{
	public static function create(): int
	{
		return self::between(1);
	}

	public static function between(int $min, int $max = PHP_INT_MAX): int
	{
		return MotherCreator::random()->numberBetween($min, $max);
	}

	public static function lessThan(int $max): int
	{
		return self::between(1, $max);
	}
}

```

### File: tests\Shared\Domain\MotherCreator.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

use Faker\Factory;
use Faker\Generator;

final class MotherCreator
{
	private static ?Generator $faker = null;

	public static function random(): Generator
	{
		return self::$faker ??= Factory::create();
	}
}

```

### File: tests\Shared\Domain\RandomElementPicker.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

final class RandomElementPicker
{
	public static function from(mixed ...$elements): mixed
	{
		return MotherCreator::random()->randomElement($elements);
	}
}

```

### File: tests\Shared\Domain\Repeater.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

use function Lambdish\Phunctional\repeat;

final class Repeater
{
	public static function repeat(callable $function, int $quantity): array
	{
		return repeat($function, $quantity);
	}

	public static function random(callable $function): array
	{
		return self::repeat($function, IntegerMother::lessThan(5));
	}
}

```

### File: tests\Shared\Domain\TestUtils.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

use CodelyTv\Tests\Shared\Infrastructure\Mockery\CodelyTvMatcherIsSimilar;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Constraint\CodelyTvConstraintIsSimilar;

final class TestUtils
{
	public static function isSimilar(mixed $expected, mixed $actual): bool
	{
		$constraint = new CodelyTvConstraintIsSimilar($expected);

		return $constraint->evaluate($actual, '', true);
	}

	public static function assertSimilar(mixed $expected, mixed $actual): void
	{
		$constraint = new CodelyTvConstraintIsSimilar($expected);

		$constraint->evaluate($actual);
	}

	public static function similarTo(mixed $value, float $delta = 0.0): CodelyTvMatcherIsSimilar
	{
		return new CodelyTvMatcherIsSimilar($value, $delta);
	}
}

```

### File: tests\Shared\Domain\UuidMother.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

final class UuidMother
{
	public static function create(): string
	{
		return MotherCreator::random()->unique()->uuid;
	}
}

```

### File: tests\Shared\Domain\WordMother.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

final class WordMother
{
	public static function create(): string
	{
		return MotherCreator::random()->word;
	}
}

```

### File: tests\Shared\Infrastructure\ArchitectureTest.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure;

use ArrayIterator;
use BackedEnum;
use Countable;
use DateTimeImmutable;
use DateTimeInterface;
use DomainException;
use InvalidArgumentException;
use IteratorAggregate;
use PHPat\Selector\Selector;
use RuntimeException;
use Stringable;
use Throwable;
use Traversable;

final class ArchitectureTest
{
	public static function languageClasses(): array
	{
		return [
			Selector::classname(Throwable::class),
			Selector::classname(InvalidArgumentException::class),
			Selector::classname(RuntimeException::class),
			Selector::classname(DateTimeImmutable::class),
			Selector::classname(DateTimeInterface::class),
			Selector::classname(DomainException::class),
			Selector::classname(Stringable::class),
			Selector::classname(BackedEnum::class),
			Selector::classname(Countable::class),
			Selector::classname(IteratorAggregate::class),
			Selector::classname(Traversable::class),
			Selector::classname(ArrayIterator::class),
		];
	}
}

```

### File: tests\Shared\Infrastructure\ConstantRandomNumberGenerator.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure;

use CodelyTv\Shared\Domain\RandomNumberGenerator;

final class ConstantRandomNumberGenerator implements RandomNumberGenerator
{
	public function generate(): int
	{
		return 1;
	}
}

```

### File: src\Backoffice\Auth\Domain\AuthPassword.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class AuthPassword extends StringValueObject
{
	public function isEquals(self $other): bool
	{
		return $this->value() === $other->value();
	}
}

```

### File: src\Backoffice\Auth\Domain\AuthRepository.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

interface AuthRepository
{
	public function search(AuthUsername $username): ?AuthUser;
}

```

### File: src\Backoffice\Auth\Domain\AuthUser.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

final readonly class AuthUser
{
	public function __construct(private AuthUsername $username, private AuthPassword $password) {}

	public function passwordMatches(AuthPassword $password): bool
	{
		return $this->password->isEquals($password);
	}

	public function username(): AuthUsername
	{
		return $this->username;
	}
}

```

### File: src\Backoffice\Auth\Domain\AuthUsername.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class AuthUsername extends StringValueObject {}

```

### File: src\Backoffice\Auth\Domain\InvalidAuthCredentials.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

use RuntimeException;

final class InvalidAuthCredentials extends RuntimeException
{
	public function __construct(AuthUsername $username)
	{
		parent::__construct(sprintf('The credentials for <%s> are invalid', $username->value()));
	}
}

```

### File: src\Backoffice\Auth\Domain\InvalidAuthUsername.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

use RuntimeException;

final class InvalidAuthUsername extends RuntimeException
{
	public function __construct(AuthUsername $username)
	{
		parent::__construct(sprintf('The user <%s> does not exists', $username->value()));
	}
}

```

### File: src\Backoffice\Courses\Application\BackofficeCourseResponse.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application;

final readonly class BackofficeCourseResponse
{
	public function __construct(private string $id, private string $name, private string $duration) {}

	public function id(): string
	{
		return $this->id;
	}

	public function name(): string
	{
		return $this->name;
	}

	public function duration(): string
	{
		return $this->duration;
	}
}

```

### File: src\Backoffice\Courses\Application\BackofficeCoursesResponse.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application;

use CodelyTv\Shared\Domain\Bus\Query\Response;

final class BackofficeCoursesResponse implements Response
{
	private readonly array $courses;

	public function __construct(BackofficeCourseResponse ...$courses)
	{
		$this->courses = $courses;
	}

	public function courses(): array
	{
		return $this->courses;
	}
}

```

### File: src\Backoffice\Courses\Domain\BackofficeCourse.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Domain;

use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

final class BackofficeCourse extends AggregateRoot
{
	public function __construct(private readonly string $id, private readonly string $name, private readonly string $duration) {}

	public static function fromPrimitives(array $primitives): self
	{
		return new self($primitives['id'], $primitives['name'], $primitives['duration']);
	}

	public function toPrimitives(): array
	{
		return [
			'id' => $this->id,
			'name' => $this->name,
			'duration' => $this->duration,
		];
	}

	public function id(): string
	{
		return $this->id;
	}

	public function name(): string
	{
		return $this->name;
	}

	public function duration(): string
	{
		return $this->duration;
	}
}

```

### File: src\Backoffice\Courses\Domain\BackofficeCourseRepository.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Domain;

use CodelyTv\Shared\Domain\Criteria\Criteria;

interface BackofficeCourseRepository
{
	public function save(BackofficeCourse $course): void;

	public function searchAll(): array;

	public function matching(Criteria $criteria): array;
}

```

### File: src\Mooc\Courses\Domain\Course.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

final class Course extends AggregateRoot
{
	public function __construct(private readonly CourseId $id, private CourseName $name, private readonly CourseDuration $duration) {}

	public static function create(CourseId $id, CourseName $name, CourseDuration $duration): self
	{
		$course = new self($id, $name, $duration);

		$course->record(new CourseCreatedDomainEvent($id->value(), $name->value(), $duration->value()));

		return $course;
	}

	public function id(): CourseId
	{
		return $this->id;
	}

	public function name(): CourseName
	{
		return $this->name;
	}

	public function duration(): CourseDuration
	{
		return $this->duration;
	}

	public function rename(CourseName $newName): void
	{
		$this->name = $newName;
	}
}

```

### File: src\Mooc\Courses\Domain\CourseCreatedDomainEvent.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

final class CourseCreatedDomainEvent extends DomainEvent
{
	public function __construct(
		string $id,
		private readonly string $name,
		private readonly string $duration,
		string $eventId = null,
		string $occurredOn = null
	) {
		parent::__construct($id, $eventId, $occurredOn);
	}

	public static function eventName(): string
	{
		return 'course.created';
	}

	public static function fromPrimitives(
		string $aggregateId,
		array $body,
		string $eventId,
		string $occurredOn
	): DomainEvent {
		return new self($aggregateId, $body['name'], $body['duration'], $eventId, $occurredOn);
	}

	public function toPrimitives(): array
	{
		return [
			'name' => $this->name,
			'duration' => $this->duration,
		];
	}

	public function name(): string
	{
		return $this->name;
	}

	public function duration(): string
	{
		return $this->duration;
	}
}

```

### File: src\Mooc\Courses\Domain\CourseDuration.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class CourseDuration extends StringValueObject {}

```

### File: src\Mooc\Courses\Domain\CourseName.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class CourseName extends StringValueObject {}

```

### File: src\Mooc\Courses\Domain\CourseNotExist.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\DomainError;

final class CourseNotExist extends DomainError
{
	public function __construct(private readonly CourseId $id)
	{
		parent::__construct();
	}

	public function errorCode(): string
	{
		return 'course_not_exist';
	}

	protected function errorMessage(): string
	{
		return sprintf('The course <%s> does not exist', $this->id->value());
	}
}

```

### File: src\Mooc\Courses\Domain\CourseRepository.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;

interface CourseRepository
{
	public function save(Course $course): void;

	public function search(CourseId $id): ?Course;
}

```

### File: src\Mooc\Steps\Domain\Step.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

abstract class Step extends AggregateRoot
{
	public function __construct(
		public readonly StepId $id,
		private readonly StepTitle $title,
		private readonly StepDuration $duration
	) {}
}

```

### File: src\Mooc\Steps\Domain\StepDuration.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

use CodelyTv\Shared\Domain\ValueObject\IntValueObject;

final class StepDuration extends IntValueObject {}

```

### File: src\Mooc\Steps\Domain\StepId.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

use CodelyTv\Shared\Domain\ValueObject\Uuid;

final class StepId extends Uuid {}

```

### File: src\Mooc\Steps\Domain\StepRepository.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

interface StepRepository
{
	public function save(Step $step): void;

	public function search(StepId $id): ?Step;

	public function delete(Step $step): void;
}

```

### File: src\Mooc\Steps\Domain\StepTitle.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class StepTitle extends StringValueObject {}

```

### File: src\Mooc\Videos\Domain\Video.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Mooc\Shared\Domain\Videos\VideoUrl;
use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

final class Video extends AggregateRoot
{
	public function __construct(
		private readonly VideoId $id,
		private readonly VideoType $type,
		private VideoTitle $title,
		private readonly VideoUrl $url,
		private readonly CourseId $courseId
	) {}

	public static function create(
		VideoId $id,
		VideoType $type,
		VideoTitle $title,
		VideoUrl $url,
		CourseId $courseId
	): self {
		$video = new self($id, $type, $title, $url, $courseId);

		$video->record(
			new VideoCreatedDomainEvent($id->value(), $type->value, $title->value(), $url->value(), $courseId->value())
		);

		return $video;
	}

	public function updateTitle(VideoTitle $newTitle): void
	{
		$this->title = $newTitle;
	}

	public function id(): VideoId
	{
		return $this->id;
	}

	public function type(): VideoType
	{
		return $this->type;
	}

	public function title(): VideoTitle
	{
		return $this->title;
	}

	public function url(): VideoUrl
	{
		return $this->url;
	}

	public function courseId(): CourseId
	{
		return $this->courseId;
	}
}

```

### File: src\Mooc\Videos\Domain\VideoCreatedDomainEvent.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

final class VideoCreatedDomainEvent extends DomainEvent
{
	public function __construct(
		string $id,
		private readonly string $type,
		private readonly string $title,
		private readonly string $url,
		private readonly string $courseId,
		string $eventId = null,
		string $occurredOn = null
	) {
		parent::__construct($id, $eventId, $occurredOn);
	}

	public static function eventName(): string
	{
		return 'video.created';
	}

	public static function fromPrimitives(
		string $aggregateId,
		array $body,
		string $eventId,
		string $occurredOn
	): self {
		return new self(
			$aggregateId,
			$body['type'],
			$body['title'],
			$body['url'],
			$body['course_id'],
			$eventId,
			$occurredOn
		);
	}

	public function toPrimitives(): array
	{
		return [
			'type' => $this->type,
			'title' => $this->title,
			'url' => $this->url,
			'course_id' => $this->courseId,
		];
	}
}

```

### File: src\Mooc\Videos\Domain\VideoFinder.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

final readonly class VideoFinder
{
	public function __construct(private VideoRepository $repository) {}

	public function __invoke(VideoId $id): Video
	{
		$video = $this->repository->search($id);

		if ($video === null) {
			throw new VideoNotFound($id);
		}

		return $video;
	}
}

```

### File: src\Mooc\Videos\Domain\VideoId.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\ValueObject\Uuid;

final class VideoId extends Uuid {}

```

### File: src\Mooc\Videos\Domain\VideoNotFound.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\DomainError;

final class VideoNotFound extends DomainError
{
	public function __construct(private readonly VideoId $id)
	{
		parent::__construct();
	}

	public function errorCode(): string
	{
		return 'video_not_found';
	}

	protected function errorMessage(): string
	{
		return sprintf('The video <%s> has not been found', $this->id->value());
	}
}

```

### File: src\Mooc\Videos\Domain\VideoRepository.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\Criteria\Criteria;

interface VideoRepository
{
	public function save(Video $video): void;

	public function search(VideoId $id): ?Video;

	public function searchByCriteria(Criteria $criteria): Videos;
}

```

### File: src\Mooc\Videos\Domain\Videos.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\Collection;

final class Videos extends Collection
{
	protected function type(): string
	{
		return Video::class;
	}
}

```

### File: src\Mooc\Videos\Domain\VideoTitle.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class VideoTitle extends StringValueObject {}

```

### File: src\Mooc\Videos\Domain\VideoType.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

enum VideoType: string
{
	case SCREENCAST = 'screencast';
	case INTERVIEW = 'interview';
}

```

### File: src\Shared\Infrastructure\Bus\CallableFirstParameterExtractor.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus;

use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use LogicException;
use ReflectionClass;
use ReflectionMethod;
use ReflectionNamedType;

use function Lambdish\Phunctional\map;
use function Lambdish\Phunctional\reduce;
use function Lambdish\Phunctional\reindex;

final class CallableFirstParameterExtractor
{
	public static function forCallables(iterable $callables): array
	{
		return map(self::unflatten(), reindex(self::classExtractor(new self()), $callables));
	}

	public static function forPipedCallables(iterable $callables): array
	{
		return reduce(self::pipedCallablesReducer(), $callables, []);
	}

	private static function classExtractor(self $parameterExtractor): callable
	{
		return static fn (object $handler): ?string => $parameterExtractor->extract($handler);
	}

	private static function pipedCallablesReducer(): callable
	{
		return static function (array $subscribers, DomainEventSubscriber $subscriber): array {
			$subscribedEvents = $subscriber::subscribedTo();

			foreach ($subscribedEvents as $subscribedEvent) {
				$subscribers[$subscribedEvent][] = $subscriber;
			}

			return $subscribers;
		};
	}

	private static function unflatten(): callable
	{
		return static fn (mixed $value): array => [$value];
	}

	public function extract(object $class): ?string
	{
		$reflector = new ReflectionClass($class);
		$method = $reflector->getMethod('__invoke');

		if ($this->hasOnlyOneParameter($method)) {
			return $this->firstParameterClassFrom($method);
		}

		return null;
	}

	private function firstParameterClassFrom(ReflectionMethod $method): string
	{
		/** @var ReflectionNamedType|null $fistParameterType */
		$fistParameterType = $method->getParameters()[0]->getType();

		if ($fistParameterType === null) {
			throw new LogicException('Missing type hint for the first parameter of __invoke');
		}

		return $fistParameterType->getName();
	}

	private function hasOnlyOneParameter(ReflectionMethod $method): bool
	{
		return $method->getNumberOfParameters() === 1;
	}
}

```

### File: src\Shared\Infrastructure\Cdc\DatabaseMutationAction.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Cdc;

enum DatabaseMutationAction: string
{
	case INSERT = 'INSERT';
	case UPDATE = 'UPDATE';
	case DELETE = 'DELETE';
}

```

### File: src\Shared\Infrastructure\Cdc\DatabaseMutationToDomainEvent.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Cdc;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

interface DatabaseMutationToDomainEvent
{
	/** @return DomainEvent[] */
	public function transform(array $data): array;

	public function tableName(): string;

	public function mutationAction(): DatabaseMutationAction;
}

```

### File: src\Shared\Infrastructure\Doctrine\DatabaseConnections.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Doctrine;

use CodelyTv\Shared\Domain\Utils;
use CodelyTv\Tests\Shared\Infrastructure\Doctrine\MySqlDatabaseCleaner;
use Doctrine\ORM\EntityManager;

use function Lambdish\Phunctional\apply;
use function Lambdish\Phunctional\each;

final class DatabaseConnections
{
	private readonly array $connections;

	public function __construct(iterable $connections)
	{
		$this->connections = Utils::iterableToArray($connections);
	}

	public function clear(): void
	{
		each(fn (EntityManager $entityManager) => $entityManager->clear(), $this->connections);
	}

	public function truncate(): void
	{
		apply(new MySqlDatabaseCleaner(), array_values($this->connections));
	}
}

```

### File: src\Shared\Infrastructure\Doctrine\DoctrineEntityManagerFactory.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Doctrine;

use CodelyTv\Shared\Infrastructure\Doctrine\Dbal\DbalCustomTypesRegistrar;
use Doctrine\Common\EventManager;
use Doctrine\DBAL\DriverManager;
use Doctrine\DBAL\Platforms\MariaDBPlatform;
use Doctrine\DBAL\Schema\DefaultSchemaManagerFactory;
use Doctrine\DBAL\Schema\MySQLSchemaManager;
use Doctrine\ORM\Configuration;
use Doctrine\ORM\EntityManager;
use Doctrine\ORM\Mapping\Driver\SimplifiedXmlDriver;
use Doctrine\ORM\ORMSetup;
use RuntimeException;

use function Lambdish\Phunctional\dissoc;

final class DoctrineEntityManagerFactory
{
	private static array $sharedPrefixes = [
		__DIR__ . '/../../../Shared/Infrastructure/Persistence/Mappings' => 'CodelyTv\Shared\Domain',
	];

	public static function create(
		array $parameters,
		array $contextPrefixes,
		bool $isDevMode,
		string $schemaFile,
		array $dbalCustomTypesClasses
	): EntityManager {
		if ($isDevMode) {
			self::generateDatabaseIfNotExists($parameters, $schemaFile);
		}

		DbalCustomTypesRegistrar::register($dbalCustomTypesClasses);

		$config = self::createConfiguration($contextPrefixes, $isDevMode);
		$eventManager = new EventManager();

		return new EntityManager(
			DriverManager::getConnection($parameters, $config, $eventManager),
			$config,
			$eventManager
		);
	}

	private static function generateDatabaseIfNotExists(array $parameters, string $schemaFile): void
	{
		self::ensureSchemaFileExists($schemaFile);

		$databaseName = $parameters['dbname'];
		$parametersWithoutDatabaseName = dissoc($parameters, 'dbname');
		$connection = DriverManager::getConnection($parametersWithoutDatabaseName);
		$platform = new MariaDBPlatform();
		$schemaManager = new MySQLSchemaManager($connection, $platform);

		if (!self::databaseExists($databaseName, $schemaManager)) {
			$schemaManager->createDatabase($databaseName);

			$connection->executeStatement(sprintf('USE %s', $databaseName));
			$connection->executeStatement(file_get_contents(realpath($schemaFile)));
		}

		$connection->close();
	}

	private static function databaseExists(string $databaseName, MySQLSchemaManager $schemaManager): bool
	{
		return in_array($databaseName, $schemaManager->listDatabases(), true);
	}

	private static function ensureSchemaFileExists(string $schemaFile): void
	{
		if (!file_exists($schemaFile)) {
			throw new RuntimeException(sprintf('The file <%s> does not exist', $schemaFile));
		}
	}

	private static function createConfiguration(array $contextPrefixes, bool $isDevMode): Configuration
	{
		$config = ORMSetup::createConfiguration($isDevMode);

		$config->setMetadataDriverImpl(new SimplifiedXmlDriver(array_merge(self::$sharedPrefixes, $contextPrefixes)));
		$config->setSchemaManagerFactory(new DefaultSchemaManagerFactory());

		return $config;
	}
}

```

### File: src\Shared\Infrastructure\Logger\MonologLogger.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Logger;

use CodelyTv\Shared\Domain\Logger;

final readonly class MonologLogger implements Logger
{
	public function __construct(private \Monolog\Logger $logger) {}

	public function info(string $message, array $context = []): void
	{
		$this->logger->info($message, $context);
	}

	public function warning(string $message, array $context = []): void
	{
		$this->logger->warning($message, $context);
	}

	public function critical(string $message, array $context = []): void
	{
		$this->logger->critical($message, $context);
	}
}

```

### File: src\Shared\Infrastructure\Monitoring\PrometheusMonitor.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Monitoring;

use Prometheus\CollectorRegistry;
use Prometheus\Storage\APC;

final readonly class PrometheusMonitor
{
	private CollectorRegistry $registry;

	public function __construct()
	{
		$this->registry = new CollectorRegistry(new APC());
	}

	public function registry(): CollectorRegistry
	{
		return $this->registry;
	}
}

```

### File: src\Shared\Infrastructure\Symfony\AddJsonBodyToRequestListener.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\RequestEvent;
use Symfony\Component\HttpKernel\Exception\HttpException;

final class AddJsonBodyToRequestListener
{
	public function onKernelRequest(RequestEvent $event): void
	{
		$request = $event->getRequest();
		$requestContents = $request->getContent();

		if (!empty($requestContents) && $this->containsHeader($request, 'Content-Type', 'application/json')) {
			$jsonData = json_decode($requestContents, true, 512, JSON_THROW_ON_ERROR);
			if (!$jsonData) {
				throw new HttpException(Response::HTTP_BAD_REQUEST, 'Invalid json data');
			}
			$jsonDataLowerCase = [];
			foreach ($jsonData as $key => $value) {
				$jsonDataLowerCase[preg_replace_callback(
					'/_(.)/',
					static fn ($matches): string => strtoupper((string) $matches[1]),
					(string) $key
				)] = $value;
			}
			$request->request->replace($jsonDataLowerCase);
		}
	}

	private function containsHeader(Request $request, string $name, string $value): bool
	{
		return str_starts_with((string) $request->headers->get($name), $value);
	}
}

```

### File: src\Shared\Infrastructure\Symfony\ApiController.php
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use CodelyTv\Shared\Domain\Bus\Command\Command;
use CodelyTv\Shared\Domain\Bus\Command\CommandBus;
use CodelyTv\Shared\Domain\Bus\Query\Query;
use CodelyTv\Shared\Domain\Bus\Query\QueryBus;
use CodelyTv\Shared\Domain\Bus\Query\Response;

use function Lambdish\Phunctional\each;

abstract class ApiController
{
	public function __construct(
		private readonly QueryBus $queryBus,
		private readonly CommandBus $commandBus,
		ApiExceptionsHttpStatusCodeMapping $exceptionHandler
	) {
		each(
			fn (int $httpCode, string $exceptionClass) => $exceptionHandler->register($exceptionClass, $httpCode),
			$this->exceptions()
		);
	}

	abstract protected function exceptions(): array;

	protected function ask(Query $query): ?Response
	{
		return $this->queryBus->ask($query);
	}

	protected function dispatch(Command $command): void
	{
		$this->commandBus->dispatch($command);
	}
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
