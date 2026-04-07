---
id: php-ddd-cargo-sample
type: knowledge
owner: OA_Triage
---
# php-ddd-cargo-sample
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# PHP DDD Cargo Sample

PHP 7 port of the cargo sample used in Eric Evans Domain-Driven Design book

[![Scrutinizer Quality Score](https://scrutinizer-ci.com/g/codeliner/php-ddd-cargo-sample/badges/quality-score.png?s=d68042d97e40904ec369e137b60a1076509298f8)](https://scrutinizer-ci.com/g/codeliner/php-ddd-cargo-sample/)
[![Build Status](https://travis-ci.org/codeliner/php-ddd-cargo-sample.png?branch=master)](https://travis-ci.org/codeliner/php-ddd-cargo-sample)

## Cargo Sample Reloaded

After two years of inactivity a new version of the PHP DDD Cargo Sample is available [2015/12/07].
The new version is a complete rewrite of the cargo sample using cutting edge technology.

### tl;dr
Click [here](https://github.com/codeliner/php-ddd-cargo-sample/pull/22#issuecomment-162734730) :smile:

### What Is New?

- [x] PHP 7 with strict scalar type hints
- [x] PSR-7 & PSR-15 middleware layer using [zend-expressive](https://github.com/zendframework/zend-expressive)
- [x] Doctrine ORM ^2.5 [Embeddables](http://doctrine-orm.readthedocs.org/projects/doctrine-orm/en/latest/tutorials/embeddables.html)
- [x] PHPUnit ^5.0
- [x] Behat ^3.0
- [x] Single Page UI using [riot.js](http://riotjs.com/)

## Goal of the Project

We want to show the PHP 7 way of implementing Domain-Driven Design with the help of
the original Cargo sample used in Eric Evans book
`Domain-Driven Design: Tackling Complexity in the Heart of Software`.
This has also been done using Java, C#, Ruby and other programming languages.

It is not the one way to apply DDD and only covers the tactical part of DDD.
However, the cargo sample should help you understand the theory
and gives you a starting point. Also see the [Caveats](http://dddsample.sourceforge.net/) of the
java implementation. The same applies for our version.

## Installation
* [Standalone](https://github.com/codeliner/php-ddd-cargo-sample/blob/master/docs/installation.md)
* [Dockerized](https://github.com/codeliner/php-ddd-cargo-sample/blob/master/docs/installation-docker.md)

## Structure
The [annotated project overview](https://github.com/codeliner/php-ddd-cargo-sample/blob/master/docs/structure.md)
gives you an idea of the system structure.

## PHP 5.6 compatible Version
Looking for a PHP 5.6 compatible version of the cargo sample? [@josecelano](https://github.com/josecelano) has downgraded his fork.
You can find it [here](https://github.com/josecelano/php-ddd-cargo-sample).

## Support
If you have any problems with the application please open a [GitHub issue](https://github.com/codeliner/php-ddd-cargo-sample/issues?state=open).
Same applies if you have a question or a feature wish.

## Contributing
Contributions of any kind are welcome. The PHP 7 DDD cargo sample aims to help people understand the tactical design part of DDD.
So we'd be very happy if you tell your friends about it, link it in discussions and mention it on twitter.
If you've found a bug or have an idea for an improvement, just submit a PR like usual.

## Behavior Driven Design
All features of the application are described in feature files. You can find them in
the [features folder](https://github.com/codeliner/php-ddd-cargo-sample/tree/master/features) of the project.
We make use of [Behat](http://behat.org/) and [Mink](http://mink.behat.org/) to test our
business expectations.

You can run the feature tests by navigating to the project root and start the selenium server shipped with the sample app:
`java -jar selenium-server-standalone-2.46.0.jar`
After the server started successfully open another console, navigate to project root again and run Behat with the command `php bin/behat`.

*Note: If it does not work, check that the behat file is executable.

## Unit Tests
Unit Tests are of course also available. You can find them in [CargoBackend/tests](https://github.com/codeliner/php-ddd-cargo-sample/tree/master/CargoBackend/tests).
Got to the directory and simply run `phpunit`.

## Sponsoring
[![prooph software](https://github.com/codeliner/php-ddd-cargo-sample/blob/master/docs/assets/prooph-software-logo.png)](http://prooph.de)

This brand new cargo sample version is sponsored by prooph software GmbH. You can follow us on [twitter](https://twitter.com/prooph_software)

## Become A Member
If you want to share your experience with other DDD enthusiasts or want to ask a question about DDD then the [DDDinPHP google group](https://groups.google.com/forum/#!forum/dddinphp) is good place to do so.

You can find more DDD stuff like interesting articles and related libraries on the [PhpFriendsOfDdd/state-of-the-union](https://github.com/PhpFriendsOfDdd/state-of-the-union) project.

```

### File: composer.json
```json
{
    "name": "prooph/php-ddd-cargo-sample",
    "description": "PHP DDD Cargo Sample v2",
    "license": "BSD-3-Clause",
    "keywords": [
        "PHP7",
        "PSR7",
        "DDD"
    ],
    "homepage": "https://github.com/codeliner/php-ddd-cargo-sample",
    "authors": [
        {
            "name": "Alexander Miertsch",
            "email": "contact@prooph.de",
            "homepage": "http://prooph.de/"
        }
    ],
    "require": {
        "php": ">=7.1",
        "beberlei/assert": "^2.4",
        "doctrine/migrations": "^1.5",
        "doctrine/orm": "^2.5.11",
        "filp/whoops": "^1.1",
        "psr/http-server-middleware": "^1.0",
        "middlewares/payload": "^2.1",
        "psr/container": "^1.0",
        "ramsey/uuid": "^3.7.1",
        "ramsey/uuid-doctrine": "^1.0",
        "roave/security-advisories": "dev-master",
        "sandrokeil/interop-config": "^0.3.1",
        "zendframework/zend-config": "^3.1",
        "zendframework/zend-config-aggregator": "^1.1",
        "zendframework/zend-diactoros": "^2.0",
        "zendframework/zend-expressive": "^3.2",
        "zendframework/zend-expressive-aurarouter": "^3.0",
        "zendframework/zend-servicemanager": "^3.0",
        "zendframework/zend-stdlib": "^3.1"
    },
    "require-dev": {
        "behat/behat": "^3.0",
        "behat/mink": "^1.6",
        "behat/mink-extension": "*",
        "behat/mink-goutte-driver": "*",
        "behat/mink-selenium2-driver": "*",
        "malukenho/kawaii-gherkin": "^0.1.2",
        "phpunit/phpunit": "^5.0",
        "zendframework/zend-component-installer": "^2.1",
        "zendframework/zend-expressive-migration": "^0.1.3",
        "zendframework/zend-expressive-tooling": "^1.0"
    },
    "autoload": {
        "psr-4": {
            "Codeliner\\CargoUI\\": "CargoUI/src",
            "Codeliner\\CargoBackend\\": "CargoBackend/src",
            "Codeliner\\GraphTraversalBackend\\": "GraphTraversalBackend/src",
            "Codeliner\\CargoFeature\\": "features/bootstrap"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "CodelinerTest\\CargoBackend\\": "CargoBackend/tests",
            "CodelinerTest\\GraphTraversalBackend\\": "GraphTraversalBackend/tests"
        }
    },
    "config": {
        "bin-dir": "bin/",
        "sort-packages": true
    },
    "scripts": {
        "expressive": "expressive"
    }
}

```

### File: LICENSE.txt
```txt
Copyright (c) 2013, Alexander Miertsch contact@prooph.de
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

    * Neither the name of Alexander Miertsch nor the names of its
      contributors may be used to endorse or promote products derived from this
      software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```

### File: bin\migrations.php
```php
<?php
/*
 * This file is part of prooph/proophessor.
 * (c) 2014-2015 prooph software GmbH <contact@prooph.de>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 * 
 * Date: 9/5/15 - 10:10 PM
 */
/**
 * This makes our life easier when dealing with paths. Everything is relative
 * to the application root now.
 */
chdir(dirname(__DIR__));

// Setup autoloading
require 'vendor/autoload.php';

$container = require 'config/container.php';

/** @var \Doctrine\ORM\EntityManager $em */
$em = $container->get('doctrine.entitymanager.orm_default');

$cli = new \Symfony\Component\Console\Application('Doctrine Command Line Interface', \Doctrine\DBAL\Migrations\MigrationsVersion::VERSION());

$helperSet = new \Symfony\Component\Console\Helper\HelperSet();

$helperSet->set(new \Symfony\Component\Console\Helper\QuestionHelper(), 'dialog');

$helperSet->set(
    new \Doctrine\ORM\Tools\Console\Helper\EntityManagerHelper(
        $em
    ),
    'em'
);

$helperSet->set(
    new \Doctrine\DBAL\Tools\Console\Helper\ConnectionHelper(
        $em->getConnection()
    ),
    'connection'
);

$cli->setCatchExceptions(true);
$cli->setHelperSet($helperSet);

$cli->addCommands(array(
    // Migrations Commands
    new \Doctrine\DBAL\Migrations\Tools\Console\Command\ExecuteCommand(),
    new \Doctrine\DBAL\Migrations\Tools\Console\Command\GenerateCommand(),
    new \Doctrine\DBAL\Migrations\Tools\Console\Command\LatestCommand(),
    new \Doctrine\DBAL\Migrations\Tools\Console\Command\MigrateCommand(),
    new \Doctrine\DBAL\Migrations\Tools\Console\Command\StatusCommand(),
    new \Doctrine\DBAL\Migrations\Tools\Console\Command\VersionCommand(),
    new \Doctrine\DBAL\Migrations\Tools\Console\Command\DiffCommand()
));

$cli->run();






```

### File: config\config.php
```php
<?php

use Zend\ConfigAggregator\ConfigAggregator;
use Zend\Stdlib\ArrayUtils;
use Zend\Stdlib\Glob;

/**
 * Configuration files are loaded in a specific order. First ``global.php`` and afterwards ``local.php``. This way
 * local settings overwrite global settings.
 *
 * The configuration can be cached. This can be done by setting ``config_cache_enabled`` to ``true``.
 *
 * The configuration is stored in json so it is not depended on 3rd party libraries. Feel free to use something else
 * like Zend\Config\Writer to write PHP arrays.
 *
 * Obviously, if you use closures in your config you can't cache it.
 */

$cachedConfigFile = __DIR__ . '/../data/cache/app_config.php';

$config = [];
if (is_file($cachedConfigFile)) {
    // Try to load the cached config
    $config = json_decode(file_get_contents($cachedConfigFile), true);
} else {
    $aggregator = new ConfigAggregator([
        \Zend\Expressive\ConfigProvider::class,
        \Zend\Expressive\Router\ConfigProvider::class,
        \Zend\HttpHandlerRunner\ConfigProvider::class
    ]);

    $config = $aggregator->getMergedConfig();

    // Load configuration from autoload path
    foreach (Glob::glob(__DIR__ .'/autoload/{{,*.}global,{,*.}local}.php', Glob::GLOB_BRACE) as $file) {
        $config = ArrayUtils::merge($config, include $file);
    }

    // Cache config if enabled
    if (isset($config['config_cache_enabled']) && $config['config_cache_enabled'] === true) {
        file_put_contents($cachedConfigFile, json_encode($config));
    }
}

// Return an ArrayObject so we can inject the config as a service in Aura.Di
// and still use array checks like ``is_array``.
return new \ArrayObject($config, \ArrayObject::ARRAY_AS_PROPS);

```

### File: config\container.php
```php
<?php

use Zend\ServiceManager\ServiceManager;

return (function(): ServiceManager {
    $config = require __DIR__ .'/config.php';
    $dependencies = $config['dependencies'];
    $dependencies['services']['config'] = $config;

    // Build container
    return new ServiceManager($dependencies);
})();

```

### File: config\pipeline.php
```php
<?php

return function(\Zend\Expressive\Application $app): void {
    $app->pipe(\Zend\Stratigility\Middleware\OriginalMessages::class);
//    $app->pipe(\Zend\Stratigility\Middleware\ErrorHandler::class);
    $app->pipe(\Middlewares\JsonPayload::class);

    $app->pipe(\Zend\Expressive\Router\Middleware\RouteMiddleware::class);

    $app->pipe(\Zend\Expressive\Router\Middleware\ImplicitHeadMiddleware::class);
    $app->pipe(\Zend\Expressive\Router\Middleware\ImplicitOptionsMiddleware::class);

    $app->pipe(\Zend\Expressive\Router\Middleware\DispatchMiddleware::class);

    $app->pipe(\Zend\Expressive\Handler\NotFoundHandler::class);
};

```

### File: config\routes.php
```php
<?php

return function (\Zend\Expressive\Application $app): void {
    $app->get('/', \Codeliner\CargoUI\Main::class);
    $app->get('/api/locations', \Codeliner\CargoBackend\Http\Action\GetLocations::class);
    $app->get('/api/cargos', \Codeliner\CargoBackend\Http\Action\GetCargos::class);
    $app->post('/api/cargos', \Codeliner\CargoBackend\Http\Action\CreateCargo::class);
    $app->get('/api/cargos/{trackingId}', \Codeliner\CargoBackend\Http\Action\GetCargo::class)
        ->setOptions([
            'tokens' => [
                'trackingId' => '[\\w+-]{36,36}',
            ],
        ]);
    $app->put('/api/cargos/{trackingId}', \Codeliner\CargoBackend\Http\Action\UpdateCargo::class)
        ->setOptions([
            'tokens' => [
                'trackingId' => '[\\w+-]{36,36}',
            ],
        ]);
    $app->get('/api/cargos/{trackingId}/routecandidates', \Codeliner\CargoBackend\Http\Action\GetRouteCandidates::class)
        ->setOptions([
            'tokens' => [
                'trackingId' => '[\\w+-]{36,36}',
            ],
        ]);
};

```

### File: docs\installation-docker.md
```md
# Installation

## Requirements

docker + docker-compose

Installation instructions can be found here:
1. [Docker](https://docs.docker.com/engine/installation)
2. [Docker composer](https://docs.docker.com/compose/install)

## Let's begin

Before we can run application with docker we need to install composer dependencies.

```bash
docker run -v `pwd`:/var/www -w /var/www prooph/composer:7.1 install
```

After it ends we can run application with docker. First create a copy of `.env.dist`

```bash
cp .env.dist .env
```

If needed change values inside it and run application:

```bash
$ docker-compose up -d
```

## Open app

```
http://localhost:NGINX_PORT_FROM_.ENV_FILE
```

```

### File: docs\installation.md
```md
# Installation

## Requirements

You need >=PHP 7.1

## Using Git and Composer (recommended)

Clone the repository and manually invoke `composer` using the shipped
`composer.phar`:

    cd my/www/dir
    git clone https://github.com/codeliner/php-ddd-cargo-sample.git
    cd php-ddd-cargo-sample
    php composer.phar self-update
    php composer.phar install

(The `self-update` directive is to ensure you have an up-to-date `composer.phar`
available.)

## Setup a Database

Our sample works with a MySql database so you need a running MySql Server and an
empty test database called `cargo_sample`.

The cargo sample ships with [doctrine/migrations](https://github.com/doctrine/migrations) to create the schema. But before we can run the migrations we
need to configure a database connection.

Copy and rename the [config/autoload/local.php.dist](https://github.com/codeliner/php-ddd-cargo-sample/blob/master/config/autoload/local.php.dist) to `local.php`
and fill in your database credentials.

Now run `php bin/migrations.php migrations:migrate` in a terminal (Command must be invoked in project root)

## Web Server Setup

### Apache Setup

To setup apache, setup a virtual host to point to the public/ directory of the
project and you should be ready to go! It should look something like below:

    <VirtualHost *:80>
        ServerName cargo-sample.localhost
        DocumentRoot /path/to/php-ddd-cargo-sample/public
        SetEnv APPLICATION_ENV "development"
        <Directory /path/to/php-ddd-cargo-sample/public>
            DirectoryIndex index.php
            AllowOverride All
            Order allow,deny
            Allow from all
        </Directory>
    </VirtualHost>

### nginx & php-fpm

    server {

        root /path/to/php-ddd-cargo-sample/public;
        index index.html index.htm index.php;

        server_name cargo-sample.localhost;

        location / {
            try_files $uri $uri/ /index.php$is_args$args;
        }

        location ~ .*\.(php|phtml)?$ {
            include fastcgi_params;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_param APPLICATION_ENV development;
            fastcgi_pass unix:/var/run/php5-fpm.sock;
            fastcgi_index index.php;
        }

        location ~ .*\.(git|jpg|jpeg|png|bmp|swf|ico)?$ {
            expires 30d;
        }

        location ~ .*\.(js|css)?$ {
            expires 1h;
        }

        location ~ /\.ht {
            deny all;
        }
    }

### PHP Build-In Webserver

Run `php -S 0.0.0.0:8080 -t public/ # then browse to http://localhost:8080/`


## Permissions

The application needs write access for the `data/` dir and all sub folders.

```

### File: docs\structure.md
```md
# Annotated Project Structure

```
+-- CargoBackend                   # Cargo Booking Context
|  +-- src                             # Production source code
|  |  +-- Application                      # Application layer
|  |  |  +-- Booking                           # Booking Application Service
|  |  |  +-- Exception                         # Application related exceptions
|  |  +-- Http
|  |  |  |  +-- Action                         # REST API Endpoints (as PSR-7)
|  |  +-- Container                            # Namespace for all service factories
|  |  |  +-- ...                               # Same sub structure as in src
|  |  +-- Infrastructure                   # Infrastructure layer
|  |  |  +-- Persistence                       # Persistence module
|  |  |  |  +-- Doctrine                       # Doctrine integration
|  |  |  |  |  +-- ORM                         # Doctrine xml configs
|  |  |  |  |  +-- Type                        # Custom Doctrine types
|  |  |  |  |  +-- DoctrineCargoRepository.php # CargoRepository implementation
|  |  |  |  +-- Transaction                    # Transaction handling
|  |  |  +-- Routing                           # Routing Context Translation Adapter
|  |  +-- Model                            # Domain layer
|  |  |  +-- Cargo                             # Cargo Aggregate
|  |  |  +-- Routing                           # Routing Service contract
|  +-- tests                           # Cargo Unit Tests
+-- CargoUI                        # User Interface module 
|  +-- src                             # Server-side source code
|  |  +-- Container                        # Service factories
|  |  +-- Main.php                         # PSR-7 Middleware to serve home page
|  |  +-- RiotCompiler.php                 # riot.js tags compiler written in PHP
|  +-- view                            # riot.js tags with combined HTML5 and JS
+-- GraphTraversalBackend          # Simulated Routing Context (Supporting Sub-Domain)
+-- bin                            # CLI scripts
|  +-- migrations.php                  # Doctrine migrations CLI tool
|  +-- ...                             # All vendor CLI tools will be installed here too
+-- config                         # System configuration
|  +-- autoload                        # All configs in this dir are loaded automatically
|  |  +-- local.php.dist               # Rename to local.php and align database config
|  |  +-- ...                          # All other configs are ready to use
|  +-- config.php                      # Config autoload script
|  +-- container.php                   # Container initialization script
|  +-- behat.yml.dist                  # Rename to behat.yml and align base_url to run behat tests
+-- data                           # Mainly used for caching, make sure webserver has write access!
+-- docs                           # Documentation
+-- features                       # Behat Features
+-- migrations                     # Database migration scripts used by Doctrine Migrations
+-- public                         # Public root of the project
|  +-- index.php                       # PHP boostrap file for all non static routes
|  +-- ...                             # All static files like css, global JS, images, etc.
+-- vendor                         # Composer installation root for all vendor libs
+-- .travis.yml                    # Configuration for travis-ci
+-- composer.json                  # Composer config
+-- composer.lock                  # Composer lock of all installed vendor libs
+-- composer.phar                  # Executable Composer Phar Archiv
+-- LICENCE.txt                    # Licence file
+-- migrations.xml                 # Doctrine Migrations config
+-- README.md                      # Project readme
+-- selenium-server-standalone-2.46.0.jar  # Selenium Server executable run it with java -jar ... 
```

```

### File: migrations\Version20151206122755.php
```php
<?php

namespace Codeliner\CargoBackend\Migrations;

use Doctrine\DBAL\Migrations\AbstractMigration;
use Doctrine\DBAL\Schema\Schema;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
class Version20151206122755 extends AbstractMigration
{
    /**
     * @param Schema $schema
     */
    public function up(Schema $schema)
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->abortIf($this->connection->getDatabasePlatform()->getName() != 'mysql', 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('CREATE TABLE cargo (tracking_id CHAR(36) NOT NULL COMMENT \'(DC2Type:cargo_tracking_id)\', origin VARCHAR(255) NOT NULL, route_origin VARCHAR(255) DEFAULT NULL, route_destination VARCHAR(255) DEFAULT NULL, itinerary_legs LONGTEXT DEFAULT NULL, PRIMARY KEY(tracking_id)) DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ENGINE = InnoDB');
    }

    /**
     * @param Schema $schema
     */
    public function down(Schema $schema)
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->abortIf($this->connection->getDatabasePlatform()->getName() != 'mysql', 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('DROP TABLE cargo');
    }
}

```

### File: public\index.php
```php
<?php

declare(strict_types=1);

// Delegate static file requests back to the PHP built-in webserver
if (PHP_SAPI === 'cli-server' && $_SERVER['SCRIPT_FILENAME'] !== __FILE__) {
    return false;
}

chdir(dirname(__DIR__));
require 'vendor/autoload.php';

/**
 * Self-called anonymous function that creates its own scope and keep the global namespace clean.
 */
(function () {
    /** @var \Psr\Container\ContainerInterface $container */
    $container = require 'config/container.php';

    /** @var \Zend\Expressive\Application $app */
    $app = $container->get(\Zend\Expressive\Application::class);
    $factory = $container->get(\Zend\Expressive\MiddlewareFactory::class);

    // Execute programmatic/declarative middleware pipeline and routing
    // configuration statements
    (require 'config/pipeline.php')($app, $factory, $container);
    (require 'config/routes.php')($app, $factory, $container);

    $app->run();
})();

```

### File: features\bootstrap\FeatureContext.php
```php
<?php
namespace Codeliner\CargoFeature;

use Behat\MinkExtension\Context\MinkContext;

//
// Require 3rd-party libraries here:
//
//   require_once 'PHPUnit/Autoload.php';
//   require_once 'PHPUnit/Framework/Assert/Functions.php';
//

/**
 * Features context.
 */
class FeatureContext extends MinkContext
{
    /**
     * @var \Interop\Container\ContainerInterface
     */
    private static $container;
    
    /**
     * Initializes context.
     * Every scenario gets it's own context object.
     *
     * @param array $parameters context parameters (set them up through behat.yml)
     */
    public function __construct()
    {
        // Initialize your context here
    }

    /**
     * @BeforeSuite
     */
    static public function iniializeContainer(): void
    {
        if (self::$container === null) {
            self::$container = require __DIR__ . '/../../config/container.php';
        }
    }
    
    /**
     * @BeforeFeature
     */
    public static function clearDatabase(): void
    {
        $em = self::$container->get('doctrine.entitymanager.orm_default');
        $q = $em->createQuery('delete from Codeliner\CargoBackend\Model\Cargo\Cargo');
        $q->execute();
    }
    
    /**
     * @Given /^I click the submit button$/
     */
    public function iClickTheSubmitButton(): void
    {
        $session = $this->getSession();
        $page = $session->getPage();
        
        $submit = $page->find('css', 'form input[type=submit]');
        
        if ($submit) {
            $submit->click();
        } else {
            throw new \RuntimeException("Can not find the submit btn");
        }
    }

    /**
     * @Then /^I should wait until I see "([^"]*)"$/
     */
    public function iShouldSeeAvailableRoutes(string $arg1): void
    {
        $this->getSession()->wait(5000, '(0 === jQuery.active)');

        $this->assertElementOnPage($arg1);
    }
    
    /**
     * @When /^I click on first item in the list "([^"]*)"$/
     */
    public function iClickOnFirstItemInTheList(string $arg1): void
    {
        $session = $this->getSession();
        $page = $session->getPage();
        
        $ul = $page->find('css', '#cargo-list');
        
        $li = $ul->find('css', 'li');
        
        $li->find('css', 'a')->click();
    }

    /**
     * @When /^I follow first "([^"]*)" link$/
     */
    public function iFollowFirstLink(string $arg1): void
    {
        $page = $this->getSession()->getPage();

        $link = $page->find('css', $arg1);

        if ($link) {
            $link->click();
        }
    }
    
    /**
     * @Given /^I wait until I am on page "(?P<page>[^"]+)"$/
     */
    public function iWaitUntilIAmOnPage(string $page): void
    {
        $matchingFound = false;
        
        for($i=1;$i++;$i<=5) {
            if (strpos($this->getSession()->getCurrentUrl(), $this->locatePath($page)) !== false) {
                $matchingFound = true;
                break;
            }
            sleep(1);
        }
        
        if (!$matchingFound) {
            throw new \Exception('Stoped waiting, timelimit reached!');
        }
    }

}

```

### File: public\css\bootstrap-theme.css
```css
.btn-default,
.btn-primary,
.btn-success,
.btn-info,
.btn-warning,
.btn-danger {
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 1px 1px rgba(0, 0, 0, 0.075);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 1px 1px rgba(0, 0, 0, 0.075);
}

.btn-default:active,
.btn-primary:active,
.btn-success:active,
.btn-info:active,
.btn-warning:active,
.btn-danger:active,
.btn-default.active,
.btn-primary.active,
.btn-success.active,
.btn-info.active,
.btn-warning.active,
.btn-danger.active {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
          box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}

.btn:active,
.btn.active {
  background-image: none;
}

.btn-default {
  text-shadow: 0 1px 0 #fff;
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#ffffff), to(#e6e6e6));
  background-image: -webkit-linear-gradient(top, #ffffff, 0%, #e6e6e6, 100%);
  background-image: -moz-linear-gradient(top, #ffffff 0%, #e6e6e6 100%);
  background-image: linear-gradient(to bottom, #ffffff 0%, #e6e6e6 100%);
  background-repeat: repeat-x;
  border-color: #e0e0e0;
  border-color: #ccc;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#ffe6e6e6', GradientType=0);
}

.btn-default:active,
.btn-default.active {
  background-color: #e6e6e6;
  border-color: #e0e0e0;
}

.btn-primary {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#428bca), to(#3071a9));
  background-image: -webkit-linear-gradient(top, #428bca, 0%, #3071a9, 100%);
  background-image: -moz-linear-gradient(top, #428bca 0%, #3071a9 100%);
  background-image: linear-gradient(to bottom, #428bca 0%, #3071a9 100%);
  background-repeat: repeat-x;
  border-color: #2d6ca2;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff3071a9', GradientType=0);
}

.btn-primary:active,
.btn-primary.active {
  background-color: #3071a9;
  border-color: #2d6ca2;
}

.btn-success {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#5cb85c), to(#449d44));
  background-image: -webkit-linear-gradient(top, #5cb85c, 0%, #449d44, 100%);
  background-image: -moz-linear-gradient(top, #5cb85c 0%, #449d44 100%);
  background-image: linear-gradient(to bottom, #5cb85c 0%, #449d44 100%);
  background-repeat: repeat-x;
  border-color: #419641;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5cb85c', endColorstr='#ff449d44', GradientType=0);
}

.btn-success:active,
.btn-success.active {
  background-color: #449d44;
  border-color: #419641;
}

.btn-warning {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#f0ad4e), to(#ec971f));
  background-image: -webkit-linear-gradient(top, #f0ad4e, 0%, #ec971f, 100%);
  background-image: -moz-linear-gradient(top, #f0ad4e 0%, #ec971f 100%);
  background-image: linear-gradient(to bottom, #f0ad4e 0%, #ec971f 100%);
  background-repeat: repeat-x;
  border-color: #eb9316;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff0ad4e', endColorstr='#ffec971f', GradientType=0);
}

.btn-warning:active,
.btn-warning.active {
  background-color: #ec971f;
  border-color: #eb9316;
}

.btn-danger {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#d9534f), to(#c9302c));
  background-image: -webkit-linear-gradient(top, #d9534f, 0%, #c9302c, 100%);
  background-image: -moz-linear-gradient(top, #d9534f 0%, #c9302c 100%);
  background-image: linear-gradient(to bottom, #d9534f 0%, #c9302c 100%);
  background-repeat: repeat-x;
  border-color: #c12e2a;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9534f', endColorstr='#ffc9302c', GradientType=0);
}

.btn-danger:active,
.btn-danger.active {
  background-color: #c9302c;
  border-color: #c12e2a;
}

.btn-info {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#5bc0de), to(#31b0d5));
  background-image: -webkit-linear-gradient(top, #5bc0de, 0%, #31b0d5, 100%);
  background-image: -moz-linear-gradient(top, #5bc0de 0%, #31b0d5 100%);
  background-image: linear-gradient(to bottom, #5bc0de 0%, #31b0d5 100%);
  background-repeat: repeat-x;
  border-color: #2aabd2;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff31b0d5', GradientType=0);
}

.btn-info:active,
.btn-info.active {
  background-color: #31b0d5;
  border-color: #2aabd2;
}

.thumbnail,
.img-thumbnail {
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.075);
          box-shadow: 0 1px 2px rgba(0, 0, 0, 0.075);
}

.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus,
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  background-color: #357ebd;
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#428bca), to(#357ebd));
  background-image: -webkit-linear-gradient(top, #428bca, 0%, #357ebd, 100%);
  background-image: -moz-linear-gradient(top, #428bca 0%, #357ebd 100%);
  background-image: linear-gradient(to bottom, #428bca 0%, #357ebd 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff357ebd', GradientType=0);
}

.navbar {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#ffffff), to(#f8f8f8));
  background-image: -webkit-linear-gradient(top, #ffffff, 0%, #f8f8f8, 100%);
  background-image: -moz-linear-gradient(top, #ffffff 0%, #f8f8f8 100%);
  background-image: linear-gradient(to bottom, #ffffff 0%, #f8f8f8 100%);
  background-repeat: repeat-x;
  border-radius: 4px;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#fff8f8f8', GradientType=0);
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 1px 5px rgba(0, 0, 0, 0.075);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 1px 5px rgba(0, 0, 0, 0.075);
}

.navbar .navbar-nav > .active > a {
  background-color: #f8f8f8;
}

.navbar-brand,
.navbar-nav > li > a {
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.25);
}

.navbar-inverse {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#3c3c3c), to(#222222));
  background-image: -webkit-linear-gradient(top, #3c3c3c, 0%, #222222, 100%);
  background-image: -moz-linear-gradient(top, #3c3c3c 0%, #222222 100%);
  background-image: linear-gradient(to bottom, #3c3c3c 0%, #222222 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff3c3c3c', endColorstr='#ff222222', GradientType=0);
}

.navbar-inverse .navbar-nav > .active > a {
  background-color: #222222;
}

.navbar-inverse .navbar-brand,
.navbar-inverse .navbar-nav > li > a {
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
}

.navbar-static-top,
.navbar-fixed-top,
.navbar-fixed-bottom {
  border-radius: 0;
}

.alert {
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.2);
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.25), 0 1px 2px rgba(0, 0, 0, 0.05);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.25), 0 1px 2px rgba(0, 0, 0, 0.05);
}

.alert-success {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#dff0d8), to(#c8e5bc));
  background-image: -webkit-linear-gradient(top, #dff0d8, 0%, #c8e5bc, 100%);
  background-image: -moz-linear-gradient(top, #dff0d8 0%, #c8e5bc 100%);
  background-image: linear-gradient(to bottom, #dff0d8 0%, #c8e5bc 100%);
  background-repeat: repeat-x;
  border-color: #b2dba1;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffdff0d8', endColorstr='#ffc8e5bc', GradientType=0);
}

.alert-info {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#d9edf7), to(#b9def0));
  background-image: -webkit-linear-gradient(top, #d9edf7, 0%, #b9def0, 100%);
  background-image: -moz-linear-gradient(top, #d9edf7 0%, #b9def0 100%);
  background-image: linear-gradient(to bottom, #d9edf7 0%, #b9def0 100%);
  background-repeat: repeat-x;
  border-color: #9acfea;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9edf7', endColorstr='#ffb9def0', GradientType=0);
}

.alert-warning {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#fcf8e3), to(#f8efc0));
  background-image: -webkit-linear-gradient(top, #fcf8e3, 0%, #f8efc0, 100%);
  background-image: -moz-linear-gradient(top, #fcf8e3 0%, #f8efc0 100%);
  background-image: linear-gradient(to bottom, #fcf8e3 0%, #f8efc0 100%);
  background-repeat: repeat-x;
  border-color: #f5e79e;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffcf8e3', endColorstr='#fff8efc0', GradientType=0);
}

.alert-danger {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#f2dede), to(#e7c3c3));
  background-image: -webkit-linear-gradient(top, #f2dede, 0%, #e7c3c3, 100%);
  background-image: -moz-linear-gradient(top, #f2dede 0%, #e7c3c3 100%);
  background-image: linear-gradient(to bottom, #f2dede 0%, #e7c3c3 100%);
  background-repeat: repeat-x;
  border-color: #dca7a7;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2dede', endColorstr='#ffe7c3c3', GradientType=0);
}

.progress {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#ebebeb), to(#f5f5f5));
  background-image: -webkit-linear-gradient(top, #ebebeb, 0%, #f5f5f5, 100%);
  background-image: -moz-linear-gradient(top, #ebebeb 0%, #f5f5f5 100%);
  background-image: linear-gradient(to bottom, #ebebeb 0%, #f5f5f5 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffebebeb', endColorstr='#fff5f5f5', GradientType=0);
}

.progress-bar {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#428bca), to(#3071a9));
  background-image: -webkit-linear-gradient(top, #428bca, 0%, #3071a9, 100%);
  background-image: -moz-linear-gradient(top, #428bca 0%, #3071a9 100%);
  background-image: linear-gradient(to bottom, #428bca 0%, #3071a9 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff3071a9', GradientType=0);
}

.progress-bar-success {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#5cb85c), to(#449d44));
  background-image: -webkit-linear-gradient(top, #5cb85c, 0%, #449d44, 100%);
  background-image: -moz-linear-gradient(top, #5cb85c 0%, #449d44 100%);
  background-image: linear-gradient(to bottom, #5cb85c 0%, #449d44 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5cb85c', endColorstr='#ff449d44', GradientType=0);
}

.progress-bar-info {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#5bc0de), to(#31b0d5));
  background-image: -webkit-linear-gradient(top, #5bc0de, 0%, #31b0d5, 100%);
  background-image: -moz-linear-gradient(top, #5bc0de 0%, #31b0d5 100%);
  background-image: linear-gradient(to bottom, #5bc0de 0%, #31b0d5 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff31b0d5', GradientType=0);
}

.progress-bar-warning {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#f0ad4e), to(#ec971f));
  background-image: -webkit-linear-gradient(top, #f0ad4e, 0%, #ec971f, 100%);
  background-image: -moz-linear-gradient(top, #f0ad4e 0%, #ec971f 100%);
  background-image: linear-gradient(to bottom, #f0ad4e 0%, #ec971f 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff0ad4e', endColorstr='#ffec971f', GradientType=0);
}

.progress-bar-danger {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#d9534f), to(#c9302c));
  background-image: -webkit-linear-gradient(top, #d9534f, 0%, #c9302c, 100%);
  background-image: -moz-linear-gradient(top, #d9534f 0%, #c9302c 100%);
  background-image: linear-gradient(to bottom, #d9534f 0%, #c9302c 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9534f', endColorstr='#ffc9302c', GradientType=0);
}

.list-group {
  border-radius: 4px;
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.075);
          box-shadow: 0 1px 2px rgba(0, 0, 0, 0.075);
}

.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  text-shadow: 0 -1px 0 #3071a9;
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#428bca), to(#3278b3));
  background-image: -webkit-linear-gradient(top, #428bca, 0%, #3278b3, 100%);
  background-image: -moz-linear-gradient(top, #428bca 0%, #3278b3 100%);
  background-image: linear-gradient(to bottom, #428bca 0%, #3278b3 100%);
  background-repeat: repeat-x;
  border-color: #3278b3;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff3278b3', GradientType=0);
}

.panel {
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
          box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.panel-default > .panel-heading {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#f5f5f5), to(#e8e8e8));
  background-image: -webkit-linear-gradient(top, #f5f5f5, 0%, #e8e8e8, 100%);
  background-image: -moz-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image: linear-gradient(to bottom, #f5f5f5 0%, #e8e8e8 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5', endColorstr='#ffe8e8e8', GradientType=0);
}

.panel-primary > .panel-heading {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#428bca), to(#357ebd));
  background-image: -webkit-linear-gradient(top, #428bca, 0%, #357ebd, 100%);
  background-image: -moz-linear-gradient(top, #428bca 0%, #357ebd 100%);
  background-image: linear-gradient(to bottom, #428bca 0%, #357ebd 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff357ebd', GradientType=0);
}

.panel-success > .panel-heading {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#dff0d8), to(#d0e9c6));
  background-image: -webkit-linear-gradient(top, #dff0d8, 0%, #d0e9c6, 100%);
  background-image: -moz-linear-gradient(top, #dff0d8 0%, #d0e9c6 100%);
  background-image: linear-gradient(to bottom, #dff0d8 0%, #d0e9c6 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffdff0d8', endColorstr='#ffd0e9c6', GradientType=0);
}

.panel-info > .panel-heading {
  background-image: -webkit-gradient(linear, left 0%, left 100%, from(#d9edf7), to(#c4e3f3));
  background-image: -webkit-linear-gradient(top, #d9edf7, 0%, #c4e3f3, 100%);
  background-image: -moz-linear-gradient(top, #d9edf7 0%, #c4e3f3 100%);
  background-image: linear-gradient(to bottom, #d9edf7 0%, #c4e3f3 100%);
  background-repeat: repeat-x;
  filter: progi
... [TRUNCATED]
```

### File: public\css\bootstrap-theme.min.css
```css
.btn-default,.btn-primary,.btn-success,.btn-info,.btn-warning,.btn-danger{text-shadow:0 -1px 0 rgba(0,0,0,0.2);-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,0.15),0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 0 rgba(255,255,255,0.15),0 1px 1px rgba(0,0,0,0.075)}.btn-default:active,.btn-primary:active,.btn-success:active,.btn-info:active,.btn-warning:active,.btn-danger:active,.btn-default.active,.btn-primary.active,.btn-success.active,.btn-info.active,.btn-warning.active,.btn-danger.active{-webkit-box-shadow:inset 0 3px 5px rgba(0,0,0,0.125);box-shadow:inset 0 3px 5px rgba(0,0,0,0.125)}.btn:active,.btn.active{background-image:none}.btn-default{text-shadow:0 1px 0 #fff;background-image:-webkit-gradient(linear,left 0,left 100%,from(#fff),to(#e6e6e6));background-image:-webkit-linear-gradient(top,#fff,0%,#e6e6e6,100%);background-image:-moz-linear-gradient(top,#fff 0,#e6e6e6 100%);background-image:linear-gradient(to bottom,#fff 0,#e6e6e6 100%);background-repeat:repeat-x;border-color:#e0e0e0;border-color:#ccc;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff',endColorstr='#ffe6e6e6',GradientType=0)}.btn-default:active,.btn-default.active{background-color:#e6e6e6;border-color:#e0e0e0}.btn-primary{background-image:-webkit-gradient(linear,left 0,left 100%,from(#428bca),to(#3071a9));background-image:-webkit-linear-gradient(top,#428bca,0%,#3071a9,100%);background-image:-moz-linear-gradient(top,#428bca 0,#3071a9 100%);background-image:linear-gradient(to bottom,#428bca 0,#3071a9 100%);background-repeat:repeat-x;border-color:#2d6ca2;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca',endColorstr='#ff3071a9',GradientType=0)}.btn-primary:active,.btn-primary.active{background-color:#3071a9;border-color:#2d6ca2}.btn-success{background-image:-webkit-gradient(linear,left 0,left 100%,from(#5cb85c),to(#449d44));background-image:-webkit-linear-gradient(top,#5cb85c,0%,#449d44,100%);background-image:-moz-linear-gradient(top,#5cb85c 0,#449d44 100%);background-image:linear-gradient(to bottom,#5cb85c 0,#449d44 100%);background-repeat:repeat-x;border-color:#419641;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5cb85c',endColorstr='#ff449d44',GradientType=0)}.btn-success:active,.btn-success.active{background-color:#449d44;border-color:#419641}.btn-warning{background-image:-webkit-gradient(linear,left 0,left 100%,from(#f0ad4e),to(#ec971f));background-image:-webkit-linear-gradient(top,#f0ad4e,0%,#ec971f,100%);background-image:-moz-linear-gradient(top,#f0ad4e 0,#ec971f 100%);background-image:linear-gradient(to bottom,#f0ad4e 0,#ec971f 100%);background-repeat:repeat-x;border-color:#eb9316;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff0ad4e',endColorstr='#ffec971f',GradientType=0)}.btn-warning:active,.btn-warning.active{background-color:#ec971f;border-color:#eb9316}.btn-danger{background-image:-webkit-gradient(linear,left 0,left 100%,from(#d9534f),to(#c9302c));background-image:-webkit-linear-gradient(top,#d9534f,0%,#c9302c,100%);background-image:-moz-linear-gradient(top,#d9534f 0,#c9302c 100%);background-image:linear-gradient(to bottom,#d9534f 0,#c9302c 100%);background-repeat:repeat-x;border-color:#c12e2a;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9534f',endColorstr='#ffc9302c',GradientType=0)}.btn-danger:active,.btn-danger.active{background-color:#c9302c;border-color:#c12e2a}.btn-info{background-image:-webkit-gradient(linear,left 0,left 100%,from(#5bc0de),to(#31b0d5));background-image:-webkit-linear-gradient(top,#5bc0de,0%,#31b0d5,100%);background-image:-moz-linear-gradient(top,#5bc0de 0,#31b0d5 100%);background-image:linear-gradient(to bottom,#5bc0de 0,#31b0d5 100%);background-repeat:repeat-x;border-color:#2aabd2;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de',endColorstr='#ff31b0d5',GradientType=0)}.btn-info:active,.btn-info.active{background-color:#31b0d5;border-color:#2aabd2}.thumbnail,.img-thumbnail{-webkit-box-shadow:0 1px 2px rgba(0,0,0,0.075);box-shadow:0 1px 2px rgba(0,0,0,0.075)}.dropdown-menu>li>a:hover,.dropdown-menu>li>a:focus,.dropdown-menu>.active>a,.dropdown-menu>.active>a:hover,.dropdown-menu>.active>a:focus{background-color:#357ebd;background-image:-webkit-gradient(linear,left 0,left 100%,from(#428bca),to(#357ebd));background-image:-webkit-linear-gradient(top,#428bca,0%,#357ebd,100%);background-image:-moz-linear-gradient(top,#428bca 0,#357ebd 100%);background-image:linear-gradient(to bottom,#428bca 0,#357ebd 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca',endColorstr='#ff357ebd',GradientType=0)}.navbar{background-image:-webkit-gradient(linear,left 0,left 100%,from(#fff),to(#f8f8f8));background-image:-webkit-linear-gradient(top,#fff,0%,#f8f8f8,100%);background-image:-moz-linear-gradient(top,#fff 0,#f8f8f8 100%);background-image:linear-gradient(to bottom,#fff 0,#f8f8f8 100%);background-repeat:repeat-x;border-radius:4px;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff',endColorstr='#fff8f8f8',GradientType=0);-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,0.15),0 1px 5px rgba(0,0,0,0.075);box-shadow:inset 0 1px 0 rgba(255,255,255,0.15),0 1px 5px rgba(0,0,0,0.075)}.navbar .navbar-nav>.active>a{background-color:#f8f8f8}.navbar-brand,.navbar-nav>li>a{text-shadow:0 1px 0 rgba(255,255,255,0.25)}.navbar-inverse{background-image:-webkit-gradient(linear,left 0,left 100%,from(#3c3c3c),to(#222));background-image:-webkit-linear-gradient(top,#3c3c3c,0%,#222,100%);background-image:-moz-linear-gradient(top,#3c3c3c 0,#222 100%);background-image:linear-gradient(to bottom,#3c3c3c 0,#222 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff3c3c3c',endColorstr='#ff222222',GradientType=0)}.navbar-inverse .navbar-nav>.active>a{background-color:#222}.navbar-inverse .navbar-brand,.navbar-inverse .navbar-nav>li>a{text-shadow:0 -1px 0 rgba(0,0,0,0.25)}.navbar-static-top,.navbar-fixed-top,.navbar-fixed-bottom{border-radius:0}.alert{text-shadow:0 1px 0 rgba(255,255,255,0.2);-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,0.25),0 1px 2px rgba(0,0,0,0.05);box-shadow:inset 0 1px 0 rgba(255,255,255,0.25),0 1px 2px rgba(0,0,0,0.05)}.alert-success{background-image:-webkit-gradient(linear,left 0,left 100%,from(#dff0d8),to(#c8e5bc));background-image:-webkit-linear-gradient(top,#dff0d8,0%,#c8e5bc,100%);background-image:-moz-linear-gradient(top,#dff0d8 0,#c8e5bc 100%);background-image:linear-gradient(to bottom,#dff0d8 0,#c8e5bc 100%);background-repeat:repeat-x;border-color:#b2dba1;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffdff0d8',endColorstr='#ffc8e5bc',GradientType=0)}.alert-info{background-image:-webkit-gradient(linear,left 0,left 100%,from(#d9edf7),to(#b9def0));background-image:-webkit-linear-gradient(top,#d9edf7,0%,#b9def0,100%);background-image:-moz-linear-gradient(top,#d9edf7 0,#b9def0 100%);background-image:linear-gradient(to bottom,#d9edf7 0,#b9def0 100%);background-repeat:repeat-x;border-color:#9acfea;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9edf7',endColorstr='#ffb9def0',GradientType=0)}.alert-warning{background-image:-webkit-gradient(linear,left 0,left 100%,from(#fcf8e3),to(#f8efc0));background-image:-webkit-linear-gradient(top,#fcf8e3,0%,#f8efc0,100%);background-image:-moz-linear-gradient(top,#fcf8e3 0,#f8efc0 100%);background-image:linear-gradient(to bottom,#fcf8e3 0,#f8efc0 100%);background-repeat:repeat-x;border-color:#f5e79e;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffcf8e3',endColorstr='#fff8efc0',GradientType=0)}.alert-danger{background-image:-webkit-gradient(linear,left 0,left 100%,from(#f2dede),to(#e7c3c3));background-image:-webkit-linear-gradient(top,#f2dede,0%,#e7c3c3,100%);background-image:-moz-linear-gradient(top,#f2dede 0,#e7c3c3 100%);background-image:linear-gradient(to bottom,#f2dede 0,#e7c3c3 100%);background-repeat:repeat-x;border-color:#dca7a7;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2dede',endColorstr='#ffe7c3c3',GradientType=0)}.progress{background-image:-webkit-gradient(linear,left 0,left 100%,from(#ebebeb),to(#f5f5f5));background-image:-webkit-linear-gradient(top,#ebebeb,0%,#f5f5f5,100%);background-image:-moz-linear-gradient(top,#ebebeb 0,#f5f5f5 100%);background-image:linear-gradient(to bottom,#ebebeb 0,#f5f5f5 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffebebeb',endColorstr='#fff5f5f5',GradientType=0)}.progress-bar{background-image:-webkit-gradient(linear,left 0,left 100%,from(#428bca),to(#3071a9));background-image:-webkit-linear-gradient(top,#428bca,0%,#3071a9,100%);background-image:-moz-linear-gradient(top,#428bca 0,#3071a9 100%);background-image:linear-gradient(to bottom,#428bca 0,#3071a9 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca',endColorstr='#ff3071a9',GradientType=0)}.progress-bar-success{background-image:-webkit-gradient(linear,left 0,left 100%,from(#5cb85c),to(#449d44));background-image:-webkit-linear-gradient(top,#5cb85c,0%,#449d44,100%);background-image:-moz-linear-gradient(top,#5cb85c 0,#449d44 100%);background-image:linear-gradient(to bottom,#5cb85c 0,#449d44 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5cb85c',endColorstr='#ff449d44',GradientType=0)}.progress-bar-info{background-image:-webkit-gradient(linear,left 0,left 100%,from(#5bc0de),to(#31b0d5));background-image:-webkit-linear-gradient(top,#5bc0de,0%,#31b0d5,100%);background-image:-moz-linear-gradient(top,#5bc0de 0,#31b0d5 100%);background-image:linear-gradient(to bottom,#5bc0de 0,#31b0d5 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de',endColorstr='#ff31b0d5',GradientType=0)}.progress-bar-warning{background-image:-webkit-gradient(linear,left 0,left 100%,from(#f0ad4e),to(#ec971f));background-image:-webkit-linear-gradient(top,#f0ad4e,0%,#ec971f,100%);background-image:-moz-linear-gradient(top,#f0ad4e 0,#ec971f 100%);background-image:linear-gradient(to bottom,#f0ad4e 0,#ec971f 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff0ad4e',endColorstr='#ffec971f',GradientType=0)}.progress-bar-danger{background-image:-webkit-gradient(linear,left 0,left 100%,from(#d9534f),to(#c9302c));background-image:-webkit-linear-gradient(top,#d9534f,0%,#c9302c,100%);background-image:-moz-linear-gradient(top,#d9534f 0,#c9302c 100%);background-image:linear-gradient(to bottom,#d9534f 0,#c9302c 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9534f',endColorstr='#ffc9302c',GradientType=0)}.list-group{border-radius:4px;-webkit-box-shadow:0 1px 2px rgba(0,0,0,0.075);box-shadow:0 1px 2px rgba(0,0,0,0.075)}.list-group-item.active,.list-group-item.active:hover,.list-group-item.active:focus{text-shadow:0 -1px 0 #3071a9;background-image:-webkit-gradient(linear,left 0,left 100%,from(#428bca),to(#3278b3));background-image:-webkit-linear-gradient(top,#428bca,0%,#3278b3,100%);background-image:-moz-linear-gradient(top,#428bca 0,#3278b3 100%);background-image:linear-gradient(to bottom,#428bca 0,#3278b3 100%);background-repeat:repeat-x;border-color:#3278b3;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca',endColorstr='#ff3278b3',GradientType=0)}.panel{-webkit-box-shadow:0 1px 2px rgba(0,0,0,0.05);box-shadow:0 1px 2px rgba(0,0,0,0.05)}.panel-default>.panel-heading{background-image:-webkit-gradient(linear,left 0,left 100%,from(#f5f5f5),to(#e8e8e8));background-image:-webkit-linear-gradient(top,#f5f5f5,0%,#e8e8e8,100%);background-image:-moz-linear-gradient(top,#f5f5f5 0,#e8e8e8 100%);background-image:linear-gradient(to bottom,#f5f5f5 0,#e8e8e8 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5',endColorstr='#ffe8e8e8',GradientType=0)}.panel-primary>.panel-heading{background-image:-webkit-gradient(linear,left 0,left 100%,from(#428bca),to(#357ebd));background-image:-webkit-linear-gradient(top,#428bca,0%,#357ebd,100%);background-image:-moz-linear-gradient(top,#428bca 0,#357ebd 100%);background-image:linear-gradient(to bottom,#428bca 0,#357ebd 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca',endColorstr='#ff357ebd',GradientType=0)}.panel-success>.panel-heading{background-image:-webkit-gradient(linear,left 0,left 100%,from(#dff0d8),to(#d0e9c6));background-image:-webkit-linear-gradient(top,#dff0d8,0%,#d0e9c6,100%);background-image:-moz-linear-gradient(top,#dff0d8 0,#d0e9c6 100%);background-image:linear-gradient(to bottom,#dff0d8 0,#d0e9c6 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffdff0d8',endColorstr='#ffd0e9c6',GradientType=0)}.panel-info>.panel-heading{background-image:-webkit-gradient(linear,left 0,left 100%,from(#d9edf7),to(#c4e3f3));background-image:-webkit-linear-gradient(top,#d9edf7,0%,#c4e3f3,100%);background-image:-moz-linear-gradient(top,#d9edf7 0,#c4e3f3 100%);background-image:linear-gradient(to bottom,#d9edf7 0,#c4e3f3 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9edf7',endColorstr='#ffc4e3f3',GradientType=0)}.panel-warning>.panel-heading{background-image:-webkit-gradient(linear,left 0,left 100%,from(#fcf8e3),to(#faf2cc));background-image:-webkit-linear-gradient(top,#fcf8e3,0%,#faf2cc,100%);background-image:-moz-linear-gradient(top,#fcf8e3 0,#faf2cc 100%);background-image:linear-gradient(to bottom,#fcf8e3 0,#faf2cc 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffcf8e3',endColorstr='#fffaf2cc',GradientType=0)}.panel-danger>.panel-heading{background-image:-webkit-gradient(linear,left 0,left 100%,from(#f2dede),to(#ebcccc));background-image:-webkit-linear-gradient(top,#f2dede,0%,#ebcccc,100%);background-image:-moz-linear-gradient(top,#f2dede 0,#ebcccc 100%);background-image:linear-gradient(to bottom,#f2dede 0,#ebcccc 100%);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2dede',endColorstr='#ffebcccc',GradientType=0)}.well{background-image:-webkit-gradient(linear,left 0,left 100%,from(#e8e8e8),to(#f5f5f5));background-image:-webkit-linear-gradient(top,#e8e8e8,0%,#f5f5f5,100%);background-image:-moz-linear-gradient(top,#e8e8e8 0,#f5f5f5 100%);background-image:linear-gradient(to bottom,#e8e8e8 0,#f5f5f5 100%);background-repeat:repeat-x;border-color:#dcdcdc;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffe8e8e8',endColorstr='#fff5f5f5',GradientType=0);-webkit-box-shadow:inset 0 1px 3px rgba(0,0,0,0.05),0 1px 0 rgba(255,255,255,0.1);box-shadow:inset 0 1px 3px rgba(0,0,0,0.05),0 1px 0 rgba(255,255,255,0.1)}
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
