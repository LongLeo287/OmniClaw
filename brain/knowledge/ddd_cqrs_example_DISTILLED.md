---
id: ddd-cqrs-example
type: knowledge
owner: OA_Triage
---
# ddd-cqrs-example
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: Readme.md
```md
### About
This is an example of implementation and my vision of **practical** CQRS, DDD, ADR, hexagonal architecture and directory structure.
Project has entities `Task` and `User`.
All UI is the REST endpoints.

### What is done
* Hexagonal Architecture (`Ports` directory for external endpoints)
* CQRS (based on symfony messenger component command/query buses with middlewares)
* DDD: directory structure (used sensiolabs-de/deptrac to control layers dependencies)
* DDD: core bounded context
* DDD: domain events implementation
* DDD: example of specification in User entity that requires a db query

### To do
* Add another bounded context
* Add anti-corruption layer for interaction between contexts

### My assumptions
* I placed entities public getters and private setters into the traits with *GS suffix to make entities a little bit clear (phpstorm tracks fine all references to entity classes) anyway you can put getters with setters in the same class
* Unfortunately mysql has a poor performance with primary uuids. Of course prefer application generated uuid if database supports them.

### How to install the project
* `bash setup_env.sh dev` - to setup .env.local docker/.env
* `make dc_up` - docker-compose up 
* `make setup_dev` - composer install, migrations and so on
* `make run php bin/console app:create-user` - create a user
* `http://127.0.0.1:888/api/doc` `https://127.0.0.1:444/api/doc` - api doc

### Some words about docker
In project is used workplace container for code manipulations, CI or building. It was created for preventing of pollution
of working containers (php-fpm) of unused in request, building tools like nodejs, composer, dev libs and so on.
Also was created a local user based on host machine user PUID PGID to resolve conflicts with file permissions.

`make dev` - jump into workplace container

### CI
```
make dev
//in container execute
make analyze
```

### Implementation
Used symfony messenger component to create transactional command bus, query bus and event bus.
Query model represented by DTOs. Domain and Command layers are covered by unit tests. 

```
├── Core (Core bounded context)
│   ├── Application
│   │   ├── Command
│   │   │   ├── AuthToken
│   │   │   ├── Task
│   │   │   └── User
│   │   ├── Query
│   │       └── Task
│   ├── Domain
│   │   └── Model
│   │       ├── Task
│   │       └── User
│   ├── Infrastructure
│   │   └── Repository
│   └── Ports
│       ├── Cli
│       └── Rest
└── Shared
    ├── Domain
    └── Infrastructure

```



```

### File: composer.json
```json
{
    "type": "project",
    "license": "proprietary",
    "require": {
        "php": "7.4.*",
        "ext-ctype": "*",
        "ext-iconv": "*",
        "ext-json": "*",
        "ext-pdo": "*",
        "lexik/jwt-authentication-bundle": "^2.10",
        "nelmio/api-doc-bundle": "^4.1",
        "sensiolabs/security-checker": "^6.0",
        "symfony/asset": "5.0.*",
        "symfony/console": "5.0.*",
        "symfony/dotenv": "5.0.*",
        "symfony/flex": "^1.3.1",
        "symfony/framework-bundle": "5.0.*",
        "symfony/messenger": "5.0.*",
        "symfony/orm-pack": "^1.0",
        "symfony/security-bundle": "5.0.*",
        "symfony/serializer-pack": "^1.0",
        "symfony/twig-pack": "^1.0",
        "symfony/yaml": "5.0.*",
        "webmozart/assert": "^1.8"
    },
    "require-dev": {
        "phpstan/phpstan": "^0.12.25",
        "phpstan/phpstan-doctrine": "^0.12.13",
        "phpstan/phpstan-phpunit": "^0.12.8",
        "phpstan/phpstan-strict-rules": "^0.12.2",
        "phpstan/phpstan-symfony": "^0.12.6",
        "phpstan/phpstan-webmozart-assert": "^0.12.4",
        "phpunit/phpunit": "^9.1",
        "sebastian/phpcpd": "^5.0",
        "sensiolabs-de/deptrac-shim": "^0.7.1",
        "symfony/debug-pack": "^1.0",
        "symfony/maker-bundle": "^1.18",
        "symfony/test-pack": "^1.0"
    },
    "config": {
        "preferred-install": {
            "*": "dist"
        },
        "sort-packages": true
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "App\\Tests\\": "tests/"
        }
    },
    "replace": {
        "paragonie/random_compat": "2.*",
        "symfony/polyfill-ctype": "*",
        "symfony/polyfill-iconv": "*",
        "symfony/polyfill-php72": "*",
        "symfony/polyfill-php71": "*",
        "symfony/polyfill-php70": "*",
        "symfony/polyfill-php56": "*"
    },
    "scripts": {
        "auto-scripts": {
            "cache:clear": "symfony-cmd",
            "assets:install %PUBLIC_DIR%": "symfony-cmd",
            "security-checker security:check": "script"
        },
        "post-install-cmd": [
            "@auto-scripts"
        ],
        "post-update-cmd": [
            "@auto-scripts"
        ]
    },
    "conflict": {
        "symfony/symfony": "*"
    },
    "extra": {
        "symfony": {
            "allow-contrib": false,
            "require": "5.0.*"
        }
    }
}

```

### File: depfile.yaml
```yaml
paths:
  - ./src
exclude_files:
  - Kernel.php
layers:
  - name: CoreApplication
    collectors:
      - type: className
        regex: .*App\\Core\\Application\\(?!Query).*
  - name: CoreDomain
    collectors:
      - type: className
        regex: .*App\\Core\\Domain\\.*
  - name: CoreInfrastructure
    collectors:
      - type: className
        regex: .*App\\Core\\Infrastructure\\.*
  - name: CorePorts
    collectors:
      - type: className
        regex: .*App\\Core\\Ports\\.*
  - name: SharedDomain
    collectors:
      - type: className
        regex: .*App\\Shared\\Domain\\.*
  - name: SharedInfrastructure
    collectors:
      - type: className
        regex: .*App\\Shared\\Infrastructure\\.*
ruleset:
  CoreApplication:
    - CoreDomain
    - SharedDomain
  CoreDomain:
    - SharedDomain
  CorePorts:
    - CoreApplication
    - CoreInfrastructure
    - SharedInfrastructure
  CoreInfrastructure:
    - CoreDomain
  SharedDomain: ~
  SharedInfrastructure:
    - SharedDomain
```

### File: setup_env.sh
```sh
#!/usr/bin/env bash

if [ -z "$1" ]
then
  echo 'Enter the environment by first argument [dev, prod, test]'
  exit 1
fi

#docker
PUID=$(id -u)
PGID=$(id -g)
DB_ROOT_PASSWORD=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 6 ; echo '')
DB_PASSWORD=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 6 ; echo '')

#app
APP_ENV=dev
APP_SECRET=$(xxd -l 16 -p /dev/random)
DATABASE_URL="mysql:\/\/task:${DB_PASSWORD}@db:3306\/task?serverVersion=8.0"

#docker
cp ./docker/.env.dist ./docker/.env && \
sed -i "s/^PUID=.*/PUID=${PUID}/g" ./docker/.env && \
sed -i "s/^PGID=.*/PGID=${PGID}/g" ./docker/.env && \
sed -i "s/^DB_ROOT_PASSWORD=.*/DB_ROOT_PASSWORD=${DB_ROOT_PASSWORD}/g" ./docker/.env && \
sed -i "s/^DB_PASSWORD=.*/DB_PASSWORD=${DB_PASSWORD}/g" ./docker/.env

#application
cp .env .env.local && \
sed -i "s/^APP_ENV=.*/APP_ENV=${APP_ENV}/g" .env.local && \
sed -i "s/^APP_SECRET=.*/APP_SECRET=${APP_SECRET}/g" .env.local && \
sed -i "s/^DATABASE_URL=.*/DATABASE_URL=${DATABASE_URL}/g" .env.local

#jwt keys
mkdir -p config/jwt && \
openssl genpkey -out config/jwt/private.pem -aes256 -algorithm rsa -pkeyopt rsa_keygen_bits:4096 && \
openssl pkey -in config/jwt/private.pem -out config/jwt/public.pem -pubout

echo -n "Enter PEM password to save in .env.local: "
read -s JWT_PASSPHRASE
sed -i "s/^JWT_PASSPHRASE=.*/JWT_PASSPHRASE=${JWT_PASSPHRASE}/g" .env.local

```

### File: config\bootstrap.php
```php
<?php

use Symfony\Component\Dotenv\Dotenv;

require dirname(__DIR__).'/vendor/autoload.php';

if (!class_exists(Dotenv::class)) {
    throw new LogicException('Please run "composer require symfony/dotenv" to load the ".env" files configuring the application.');
}

// Load cached env vars if the .env.local.php file exists
// Run "composer dump-env prod" to create it (requires symfony/flex >=1.2)
if (is_array($env = @include dirname(__DIR__).'/.env.local.php') && (!isset($env['APP_ENV']) || ($_SERVER['APP_ENV'] ?? $_ENV['APP_ENV'] ?? $env['APP_ENV']) === $env['APP_ENV'])) {
    (new Dotenv(false))->populate($env);
} else {
    // load all the .env files
    (new Dotenv(false))->loadEnv(dirname(__DIR__).'/.env');
}

$_SERVER += $_ENV;
$_SERVER['APP_ENV'] = $_ENV['APP_ENV'] = ($_SERVER['APP_ENV'] ?? $_ENV['APP_ENV'] ?? null) ?: 'dev';
$_SERVER['APP_DEBUG'] = $_SERVER['APP_DEBUG'] ?? $_ENV['APP_DEBUG'] ?? 'prod' !== $_SERVER['APP_ENV'];
$_SERVER['APP_DEBUG'] = $_ENV['APP_DEBUG'] = (int) $_SERVER['APP_DEBUG'] || filter_var($_SERVER['APP_DEBUG'], FILTER_VALIDATE_BOOLEAN) ? '1' : '0';

```

### File: config\bundles.php
```php
<?php

return [
    Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true],
    Doctrine\Bundle\DoctrineBundle\DoctrineBundle::class => ['all' => true],
    Doctrine\Bundle\MigrationsBundle\DoctrineMigrationsBundle::class => ['all' => true],
    Symfony\Bundle\MakerBundle\MakerBundle::class => ['dev' => true],
    Symfony\Bundle\TwigBundle\TwigBundle::class => ['all' => true],
    Twig\Extra\TwigExtraBundle\TwigExtraBundle::class => ['all' => true],
    Symfony\Bundle\WebProfilerBundle\WebProfilerBundle::class => ['dev' => true, 'test' => true],
    Symfony\Bundle\MonologBundle\MonologBundle::class => ['all' => true],
    Symfony\Bundle\DebugBundle\DebugBundle::class => ['dev' => true, 'test' => true],
    Symfony\Bundle\SecurityBundle\SecurityBundle::class => ['all' => true],
    Lexik\Bundle\JWTAuthenticationBundle\LexikJWTAuthenticationBundle::class => ['all' => true],
    Nelmio\ApiDocBundle\NelmioApiDocBundle::class => ['all' => true],
];

```

### File: config\routes.yaml
```yaml
api_login_check:
    path: /api/login_check
```

### File: config\services.yaml
```yaml
# This file is the entry point to configure your own services.
# Files in the packages/ subdirectory configure your dependencies.

# Put parameters here that don't need to change on each machine where the app is deployed
# https://symfony.com/doc/current/best_practices/configuration.html#application-related-configuration
parameters:

services:
    # default configuration for services in *this* file
    _defaults:
        autowire: true      # Automatically injects dependencies in your services.
        autoconfigure: true # Automatically registers your services as commands, event subscribers, etc.

    # makes classes in src/ available to be used as services
    # this creates a service per class whose id is the fully-qualified class name
    App\:
        resource: '../src/*'
        exclude:
            - '../src/Shared/Infrastructure/Migration'

    App\Core\Ports\Rest\:
        resource: '../src/Core/Ports/Rest'
        tags: ['controller.service_arguments']

    command_handlers:
        namespace: App\Core\Application\Command\
        resource: '%kernel.project_dir%/src/Core/Application/Command/*/*/*CommandHandler.php'
        autoconfigure: false
        tags:
            - { name: messenger.message_handler, bus: command.bus }

    query_handlers:
        namespace: App\Core\Application\Query\
        resource: '%kernel.project_dir%/src/Core/Application/Query/*/*/*QueryHandler.php'
        autoconfigure: false
        tags:
            - { name: messenger.message_handler, bus: query.bus }

    event_handlers:
        namespace: App\Core\Application\
        resource: '%kernel.project_dir%/src/Core/Application/**/*EventHandler.php'
        autoconfigure: false
        tags:
            - { name: messenger.message_handler, bus: event.bus }

    App\Shared\Infrastructure\Doctrine\DomainEventSubscriber:
        tags: [{name: 'doctrine.event_subscriber'}]

```

### File: public\index.php
```php
<?php

use App\Kernel;
use Symfony\Component\ErrorHandler\Debug;
use Symfony\Component\HttpFoundation\Request;

require dirname(__DIR__).'/config/bootstrap.php';

if ($_SERVER['APP_DEBUG']) {
    umask(0000);

    Debug::enable();
}

if ($trustedProxies = $_SERVER['TRUSTED_PROXIES'] ?? false) {
    Request::setTrustedProxies(explode(',', $trustedProxies), Request::HEADER_X_FORWARDED_ALL ^ Request::HEADER_X_FORWARDED_HOST);
}

if ($trustedHosts = $_SERVER['TRUSTED_HOSTS'] ?? false) {
    Request::setTrustedHosts([$trustedHosts]);
}

$kernel = new Kernel($_SERVER['APP_ENV'], (bool) $_SERVER['APP_DEBUG']);
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);

```

### File: src\Kernel.php
```php
<?php

declare(strict_types=1);

namespace App;

use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\Config\Loader\LoaderInterface;
use Symfony\Component\Config\Resource\FileResource;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\HttpKernel\Kernel as BaseKernel;
use Symfony\Component\Routing\RouteCollectionBuilder;

class Kernel extends BaseKernel
{
    use MicroKernelTrait;

    private const CONFIG_EXTS = '.{php,xml,yaml,yml}';

    public function registerBundles(): iterable
    {
        $contents = require $this->getProjectDir() . '/config/bundles.php';
        foreach ($contents as $class => $envs) {
            if ($envs[$this->environment] ?? $envs['all'] ?? false) {
                yield new $class();
            }
        }
    }

    public function getProjectDir(): string
    {
        return \dirname(__DIR__);
    }

    protected function configureContainer(ContainerBuilder $container, LoaderInterface $loader): void
    {
        $container->addResource(new FileResource($this->getProjectDir() . '/config/bundles.php'));
        $container->setParameter('container.dumper.inline_class_loader', \PHP_VERSION_ID < 70400 || $this->debug);
        $container->setParameter('container.dumper.inline_factories', true);
        $confDir = $this->getProjectDir() . '/config';

        $loader->load($confDir . '/{packages}/*' . self::CONFIG_EXTS, 'glob');
        $loader->load($confDir . '/{packages}/' . $this->environment . '/*' . self::CONFIG_EXTS, 'glob');
        $loader->load($confDir . '/{services}' . self::CONFIG_EXTS, 'glob');
        $loader->load($confDir . '/{services}_' . $this->environment . self::CONFIG_EXTS, 'glob');
    }

    protected function configureRoutes(RouteCollectionBuilder $routes): void
    {
        $confDir = $this->getProjectDir() . '/config';

        $routes->import($confDir . '/{routes}/' . $this->environment . '/*' . self::CONFIG_EXTS, '/', 'glob');
        $routes->import($confDir . '/{routes}/*' . self::CONFIG_EXTS, '/', 'glob');
        $routes->import($confDir . '/{routes}' . self::CONFIG_EXTS, '/', 'glob');
    }
}

```

### File: tests\bootstrap.php
```php
<?php

use Symfony\Component\Dotenv\Dotenv;

require dirname(__DIR__).'/vendor/autoload.php';

if (file_exists(dirname(__DIR__).'/config/bootstrap.php')) {
    require dirname(__DIR__).'/config/bootstrap.php';
} elseif (method_exists(Dotenv::class, 'bootEnv')) {
    (new Dotenv())->bootEnv(dirname(__DIR__).'/.env');
}

```

### File: config\packages\cache.yaml
```yaml
framework:
    cache:
        # Unique name of your app: used to compute stable namespaces for cache keys.
        #prefix_seed: your_vendor_name/app_name

        # The "app" cache stores to the filesystem by default.
        # The data in this cache should persist between deploys.
        # Other options include:

        # Redis
        #app: cache.adapter.redis
        #default_redis_provider: redis://localhost

        # APCu (not recommended with heavy random-write workloads as memory fragmentation can cause perf issues)
        #app: cache.adapter.apcu

        # Namespaced pools use the above "app" backend by default
        #pools:
            #my.dedicated.cache: null

```

### File: config\packages\doctrine.yaml
```yaml
doctrine:
    dbal:
        url: '%env(resolve:DATABASE_URL)%'
        mapping_types:
            enum: string
    orm:
        auto_generate_proxy_classes: true
        naming_strategy: doctrine.orm.naming_strategy.underscore_number_aware
        auto_mapping: true
        mappings:
            App:
                is_bundle: false
                type: annotation
                dir: '%kernel.project_dir%/src/Core/Domain/Model'
                prefix: 'App\Core\Domain\Model'
                alias: App

```

### File: config\packages\doctrine_migrations.yaml
```yaml
doctrine_migrations:
    dir_name: '%kernel.project_dir%/src/Shared/Infrastructure/Migration'
    # namespace is arbitrary but should be different from App\Migrations
    # as migrations classes should NOT be autoloaded
    namespace: DoctrineMigrations

```

### File: config\packages\framework.yaml
```yaml
framework:
    secret: '%env(APP_SECRET)%'
    #csrf_protection: true
    #http_method_override: true

    # Enables session support. Note that the session will ONLY be started if you read or write from it.
    # Remove or comment this section to explicitly disable session support.
    session:
        handler_id: null
        cookie_secure: auto
        cookie_samesite: lax

    #esi: true
    #fragments: true
    php_errors:
        log: true

    serializer:
        name_converter: 'serializer.name_converter.camel_case_to_snake_case'
        mapping:
            paths:
                - '%kernel.project_dir%/src/Core/Ports/Rest/SerializerMapping'

```

### File: config\packages\lexik_jwt_authentication.yaml
```yaml
lexik_jwt_authentication:
    secret_key: '%env(resolve:JWT_SECRET_KEY)%'
    public_key: '%env(resolve:JWT_PUBLIC_KEY)%'
    pass_phrase: '%env(JWT_PASSPHRASE)%'

```

### File: config\packages\messenger.yaml
```yaml
framework:
    messenger:
        default_bus: event.bus
        buses:
            command.bus:
                middleware:
                    - doctrine_transaction
            query.bus:
            event.bus:
                default_middleware: allow_no_handlers

```

### File: config\packages\nelmio_api_doc.yaml
```yaml
nelmio_api_doc:
    models: { use_jms: false }
    documentation:
        info:
            title: My App
            description: This is an awesome app!
            version: 1.0.0
        securityDefinitions:
            Bearer:
                type: apiKey
                description: 'Value: Bearer {jwt}'
                name: Authorization
                in: header
        security:
            - Bearer: []
    areas: # to filter documented areas
        path_patterns:
            - ^/api(?!/doc$) # Accepts routes under /api except /api/doc

```

### File: config\packages\routing.yaml
```yaml
framework:
    router:
        utf8: true

```

### File: config\packages\security.yaml
```yaml
security:
    encoders:
        App\Core\Domain\Model\User\User:
            algorithm: auto

    providers:
        app_user_provider:
            entity:
                class: App\Core\Domain\Model\User\User
                property: username
    firewalls:
        api_doc:
            pattern:  ^/api/doc
            stateless: true
            anonymous: true
        create_token:
            pattern:  ^/api/auth-token
            stateless: true
            anonymous: true
        login:
            pattern:  ^/api/login
            stateless: true
            anonymous: true
            json_login:
                check_path:               /api/login_check
                success_handler:          lexik_jwt_authentication.handler.authentication_success
                failure_handler:          lexik_jwt_authentication.handler.authentication_failure

        api:
            pattern:   ^/api
            stateless: true
            guard:
                authenticators:
                    - lexik_jwt_authentication.jwt_token_authenticator

    access_control:
        - { path: ^/api/login, roles: IS_AUTHENTICATED_ANONYMOUSLY }
        - { path: ^/api/auth-token, roles: IS_AUTHENTICATED_ANONYMOUSLY }
        - { path: ^/api/doc, roles: IS_AUTHENTICATED_ANONYMOUSLY }
        - { path: ^/api,       roles: IS_AUTHENTICATED_FULLY }

```

### File: config\packages\security_checker.yaml
```yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true

    SensioLabs\Security\SecurityChecker: null

    SensioLabs\Security\Command\SecurityCheckerCommand: null

```

### File: config\packages\twig.yaml
```yaml
twig:
    default_path: '%kernel.project_dir%/templates'

```

### File: config\packages\test\framework.yaml
```yaml
framework:
    test: true
    session:
        storage_id: session.storage.mock_file

```

### File: config\packages\test\monolog.yaml
```yaml
monolog:
    handlers:
        main:
            type: fingers_crossed
            action_level: error
            handler: nested
            excluded_http_codes: [404, 405]
            channels: ["!event"]
        nested:
            type: stream
            path: "%kernel.logs_dir%/%kernel.environment%.log"
            level: debug

```

### File: config\packages\test\twig.yaml
```yaml
twig:
    strict_variables: true

```

### File: config\packages\test\web_profiler.yaml
```yaml
web_profiler:
    toolbar: false
    intercept_redirects: false

framework:
    profiler: { collect: false }

```

