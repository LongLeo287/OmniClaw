---
id: repo-fetched-api-093339
type: knowledge
owner: OA
registered_at: 2026-04-05T03:27:28.849260
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_api_093339

## Assimilation Report
Auto-cloned repository: FETCHED_api_093339

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Talos Pioneers Backend

Talos Pioneers is the backend API for a blueprint sharing platform for **Arknights Endfield**. The platform allows players to create, share, like, and comment on game blueprints (base designs/builds) using shareable codes that can be pasted directly into the game. Users can organize blueprints into collections, upload new blueprints, and interact with the community through comments and likes.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Environment Variables](#environment-variables)
- [Database](#database)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Features & Models](#features--models)
- [Development](#development)
- [Testing](#testing)
- [Permissions & Roles](#permissions--roles)
- [Additional Information](#additional-information)

## Tech Stack

- **Framework**: Laravel 12
- **PHP**: 8.2+
- **Database**: SQLite
- **Authentication**: Laravel Sanctum (Cookied Based)
- **OAuth**: Laravel Socialite (Discord, Google)
- **Testing**: Pest PHP 4
- **Code Style**: Laravel Pint
- **Frontend**: Vite, Tailwind CSS 4
- **Content Moderation**: OpenAI API
- **Media Management**: Spatie Media Library
- **Permissions**: Spatie Laravel Permission
- **Other Packages**:
  - Spatie Tags
  - Spatie Translatable
  - Spatie Query Builder
  - Spatie Sluggable
  - BeyondCode Comments
  - Laravel Magic Link

## Prerequisites

Before you begin, ensure you have the following installed:

- **PHP** 8.2 or higher
- **Composer** (PHP dependency manager)
- **Node.js** and **npm** (for frontend assets)
- **SQLite** (for development) or another supported database (MySQL, PostgreSQL)
- **OpenAI API Key** (optional, for content moderation)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd backend
```

### 2. Install Dependencies

Install PHP dependencies:

```bash
composer install
```

Install Node.js dependencies:

```bash
npm install
```

### 3. Environment Configuration

Copy the environment file:

```bash
cp .env.example .env
```

Generate the application key:

```bash
php artisan key:generate
```

### 4. Configure Environment Variables

Edit the `.env` file with your configuration. See [Environment Variables](#environment-variables) section for details.

### 5. Database Setup

Create the database file (if using SQLite):

```bash
touch database/database.sqlite
```

Run migrations:

```bash
php artisan migrate
```

Seed the database with initial data:

```bash
php artisan db:seed
```

This will seed:
- Roles and permissions (Admin, Moderator, User)
- Initial tags

### 6. Build Frontend Assets

For development:

```bash
npm run dev
```

For production:

```bash
npm run build
```

### 7. Quick Setup (Alternative)

You can use the provided setup script that handles most of the above:

```bash
composer run setup
```

This script will:
- Install Composer dependencies
- Copy `.env.example` to `.env` if it doesn't exist
- Generate application key
- Run migrations
- Install npm dependencies
- Build frontend assets

## Environment Variables

### Required Variables

```env
APP_NAME="Talos Pioneers"
APP_ENV=local
APP_KEY=                    # Generated via `php artisan key:generate`
APP_DEBUG=true
APP_URL=http://localhost:8000

DB_CONNECTION=sqlite
DB_DATABASE=database/database.sqlite  # For SQLite
```

### Optional Variables

#### Sanctum Configuration

```env
SANCTUM_STATEFUL_DOMAINS=localhost,localhost:3000,127.0.0.1,127.0.0.1:8000
```

#### OAuth Providers

```env
DISCORD_CLIENT_ID=
DISCORD_CLIENT_SECRET=
DISCORD_REDIRECT_URI=http://localhost:8000/auth/discord/callback
DISCORD_AVATAR_GIF=false
DISCORD_EXTENSION_DEFAULT=webp
```

```env
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=
```

#### OpenAI (Content Moderation)

```env
OPENAI_API_KEY=
AUTO_MOD_ENABLED=true
```

#### Frontend URL

```env
FRONTEND_URL=http://localhost:3000
```

## Database

### Migrations

Run migrations:

```bash
php artisan migrate
```

### Seeders

The application includes the following seeders:

- **RolePermissionSeeder**: Creates roles (Admin, Moderator, User) and permissions
- **TagSeeder**: Seeds initial blueprint tags

Run all seeders:

```bash
php artisan db:seed
```

Run a specific seeder:

```bash
php artisan db:seed --class=RolePermissionSeeder
```

### Database Structure

Key tables:
- `users` - User accounts
- `blueprints` - Game blueprints (base designs)
- `blueprint_collections` - Collections of blueprints
- `blueprint_likes` - User likes on blueprints
- `blueprint_copies` - Blueprint copy tracking
- `blueprint_facilities` - Blueprint-facility relationships
- `blueprint_item_inputs` - Blueprint input items
- `blueprint_item_outputs` - Blueprint output items
- `comments` - Comments on blueprints
- `facilities` - Game facilities
- `items` - Game items
- `tags` - Tags for categorization
- `model_has_tags` - Tag relationships
- `roles` - User roles
- `permissions` - Permissions
- `model_has_permissions` - Permission assignments

## API Endpoints

All API endpoints are versioned under `/api/v1/`. Authentication is handled via Laravel Sanctum tokens.

### Authentication (Web Routes)

These routes handle user authentication:

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | User login (email/password) |
| POST | `/register` | User registration |
| GET | `/auth/{provider}/redirect` | OAuth provider redirect (e.g., Discord) |
| GET | `/auth/{provider}/callback` | OAuth provider callback |

### Public API Endpoints (v1)

These endpoints are publicly accessible:

#### Blueprints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/blueprints` | List published blueprints (with filtering, sorting, pagination) |
| GET | `/api/v1/blueprints/{id}` | Get blueprint details |

**Query Parameters for `/api/v1/blueprints`**:
- `filter[region]` - Filter by region (valley_iv, wuling)
- `filter[version]` - Filter by game version (cbt_3)
- `filter[is_anonymous]` - Filter anonymous blueprints (true/false)
- `filter[author_id]` - Filter by author ID
- `filter[facility]` - Filter by facility slugs (comma-separated)
- `filter[item_input]` - Filter by input item slugs (comma-separated)
- `filter[item_output]` - Filter by output item slugs (comma-separated)
- `filter[tags.id]` - Filter by tag IDs (comma-separated)
- `sort` - Sort by: `created_at`, `updated_at`, `title`, `likes_count`, `copies_count`
- `page` - Page number for pagination

#### Collections

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/collections` | List collections |
| GET | `/api/v1/collections/{id}` | Get collection details |

#### Facilities

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/facilities` | List facilities |
| GET | `/api/v1/facilities/{slug}` | Get facility details by slug |

#### Items

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/items` | List items |
| GET | `/api/v1/items/{slug}` | Get item details by slug |

#### Tags

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/tags` | List tags |

#### Comments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/blueprints/{blueprint}/comments` | List comments for a blueprint |
| GET | `/api/v1/blueprints/{blueprint}/comments/{comment}` | Get a specific comment |

### Authenticated API Endpoints (v1)

These endpoints require authentication via Sanctum token. Include the token in the `Authorization` header:

```
Authorization: Bearer {token}
```

#### Profile

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/profile` | Get authenticated user's profile |
| PUT | `/api/v1/profile` | Update authenticated user's profile |

#### Blueprints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/blueprints` | Create a new blueprint |
| PUT | `/api/v1/blueprints/{id}` | Update a blueprint (own or with permission) |
| DELETE | `/api/v1/blueprints/{id}` | Delete a blueprint (own or with permission) |
| POST | `/api/v1/blueprints/{blueprint}/like` | Like/unlike a blueprint |
| POST | `/api/v1/blueprints/{blueprint}/copy` | Copy a blueprint (track usage) |

#### My Blueprints & Collections

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/my/blueprints` | Get authenticated user's blueprints |
| GET | `/api/v1/my/collections` | Get authenticated user's collections |

#### Collections

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/collections` | Create a new collection |
| PUT | `/api/v1/collections/{id}` | Update a collection (own or with permission) |
| DELETE | `/api/v1/collections/{id}` | Delete a collection (own or with permission) |

#### Comments

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/blueprints/{blueprint}/comments` | Create a comment on a blueprint |
| PUT | `/api/v1/blueprints/{blueprint}/comments/{comment}` | Update a comment (own or with permission) |
| DELETE | `/api/v1/blueprints/{blueprint}/comments/{comment}` | Delete a comment (own or with permission) |

#### Tags

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/tags` | Create a tag (requires permission) |
| PUT | `/api/v1/tags/{id}` | Update a tag (requires permission) |
| DELETE | `/api/v1/tags/{id}` | Delete a tag (requires permission) |

#### Users (Admin/Moderator)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/users/{user}/upgrade-to-moderator` | Upgrade a user to moderator role (requires permission) |

### Utility Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/user` | Get authenticated user (Sanctum) |
| GET | `/up` | Health check endpoint |

## Authentication

### Sanctum Token Authentication

The API uses Laravel Sanctum for token-based authentication. After logging in via `/login` or OAuth, you'll receive a token that should be included in subsequent requests:

```http
Authorization: Bearer {your-token-here}
```

### OAuth Providers

The application supports OAuth authentication via Discord and Google, the process is the same :

1. Register your application with Discord and Google
2. Configure `.env` variables based on .env.example
3. Set the redirect URI to: `http://your-domain/auth/{provider}/callback`
4. Users can authenticate via: `GET /auth/{provider}/redirect`

### Magic Link Authentication

The application includes support for magic link authentication via `cesargb/laravel-magiclink`. Users can request a magic link to log in without a password.

## Features & Models

### Blueprints

Blueprints are the core entity representing game base designs/builds. Each blueprint includes:

- **Code**: Shareable code that can be pasted into Arknights Endfield
- **Title**: Blueprint title
- **Description**: Optional description
- **Status**: `draft`, `published`, or `archived`
- **Version**: Game version (currently `cbt_3`)
- **Region**: Game region (`valley_iv` or `wuling`)
- **Facilities**: Associated facilities with quantities
- **Item Inputs**: Required input items with quantities
- **Item Outputs**: Produced output items with quantities
- **Tags**: Categorization tags
- **Gallery**: Media images
- **Is Anonymous**: Option to post anonymously
- **Creator**: User who created the blueprint
- **Likes**: Users who liked the blueprint
- **Copies**: Copy tracking for usage statistics

### Blueprint Collections

Collections allow users to organize multiple blueprints into groups. Collections can be:
- Public or private
- Shared with the community
- Managed by the creator or moderators/admins

### Comments

Users can comment on blueprints. Comments support:
- Auto-moderation (via OpenAI)
- Auto-approval for trusted users
- Editing and deletion by comment author or moderators

### Tags

Tags are used to categorize blueprints. Tags can be:
- Created by users with `manage_tags` permission
- Applied to blueprints
- Filtered in blueprint listings

### Facilities and Items

Game data from Arknights Endfield:
- **Facilities**: Production facilities in the game
- **Items**: Materials, currency, and other game items
- Both support translations for multi-language support
- Used in blueprints to define inputs/outputs

### User Roles and Permissions

The application uses a role-based permission system:

#### Roles

- **Admin**: Full access to all features
- **Moderator**: Can manage all blueprints, collections, and comments
- **User**: Standard user with basic permissions

#### Permissions

- `manage_tags` - Create, update, delete tags
- `upgrade_users` - Upgrade users to moderator
- `manage_all_blueprints` - Manage any blueprint (not just own)
- `manage_all_collections` - Manage any collection (not just own)
- `manage_comments` - Manage any comment (not just own)

### Content Moderation

The application includes OpenAI-powered content moderation for:
- Blueprint titles and descriptions
- Blueprint gallery images
- Comments

Moderation can be enabled/disabled via `AUTO_MOD_ENABLED` environment variable.

## Development

### Running the Development Server

Use the provided development script that runs multiple services concurrently:

```bash
composer run dev
```

This runs:
- Laravel development server (`php artisan serve`)
- Queue worker (`php artisan queue:listen`)
- Log viewer (`php artisan pail`)
- Vite dev server (`npm run dev`)

### Running Individual Services

**Laravel Server:**
```bash
php artisan serve
```

**Queue Worker:**
```bash
php artisan queue:work
```

**Vite Dev Server:**
```bash
npm run dev
```

### Code Formatting

Format code using Laravel Pint:

```bash
vendor/bin/pint
```

Format only changed files:

```bash
vendor/bin/pint --dirty
```

### Queue Processing

The application uses Laravel queues for background jobs. Run the queue worker:

```bash
php artisan queue:work
```

Or use the queue listener:

```bash
php artisan queue:listen
```

### Logging

View logs in real-time:

```bash
php artisan pail
```

Logs are stored in `storage/logs/laravel.log`.

### Database Commands

**Create a migration:**
```bash
php artisan make:migration create_example_table
```

**Create a model with migration:**
```bash
php artisan make:model Example -m
```

**Create a seeder:**
```bash
php artisan make:seeder ExampleSeeder
```

## Testing

The application uses **Pest PHP 4** for testing.

### Running Tests

Run all tests:

```bash
php artisan test
```

Run a specific test file:

```bash
php artisan test tests/Feature/BlueprintControllerTest.php
```

Run tests matching a filter:

```bash
php artisan test --filter=BlueprintController
```

### Test Structure

- **Feature Tests**: Located in `tests/Feature/
... [TRUNCATED]
```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for api
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .junie\guidelines.md
```md
<laravel-boost-guidelines>
=== foundation rules ===

# Laravel Boost Guidelines

The Laravel Boost guidelines are specifically curated by Laravel maintainers for this application. These guidelines should be followed closely to enhance the user's satisfaction building Laravel applications.

## Foundational Context
This application is a Laravel application and its main Laravel ecosystems package & versions are below. You are an expert with them all. Ensure you abide by these specific packages & versions.

- php - 8.4.14
- laravel/framework (LARAVEL) - v12
- laravel/prompts (PROMPTS) - v0
- laravel/sanctum (SANCTUM) - v4
- laravel/socialite (SOCIALITE) - v5
- laravel/mcp (MCP) - v0
- laravel/pint (PINT) - v1
- laravel/sail (SAIL) - v1
- pestphp/pest (PEST) - v4
- phpunit/phpunit (PHPUNIT) - v12
- tailwindcss (TAILWINDCSS) - v4

## Conventions
- You must follow all existing code conventions used in this application. When creating or editing a file, check sibling files for the correct structure, approach, naming.
- Use descriptive names for variables and methods. For example, `isRegisteredForDiscounts`, not `discount()`.
- Check for existing components to reuse before writing a new one.

## Verification Scripts
- Do not create verification scripts or tinker when tests cover that functionality and prove it works. Unit and feature tests are more important.

## Application Structure & Architecture
- Stick to existing directory structure - don't create new base folders without approval.
- Do not change the application's dependencies without approval.

## Frontend Bundling
- If the user doesn't see a frontend change reflected in the UI, it could mean they need to run `npm run build`, `npm run dev`, or `composer run dev`. Ask them.

## Replies
- Be concise in your explanations - focus on what's important rather than explaining obvious details.

## Documentation Files
- You must only create documentation files if explicitly requested by the user.


=== boost rules ===

## Laravel Boost
- Laravel Boost is an MCP server that comes with powerful tools designed specifically for this application. Use them.

## Artisan
- Use the `list-artisan-commands` tool when you need to call an Artisan command to double check the available parameters.

## URLs
- Whenever you share a project URL with the user you should use the `get-absolute-url` tool to ensure you're using the correct scheme, domain / IP, and port.

## Tinker / Debugging
- You should use the `tinker` tool when you need to execute PHP to debug code or query Eloquent models directly.
- Use the `database-query` tool when you only need to read from the database.

## Reading Browser Logs With the `browser-logs` Tool
- You can read browser logs, errors, and exceptions using the `browser-logs` tool from Boost.
- Only recent browser logs will be useful - ignore old logs.

## Searching Documentation (Critically Important)
- Boost comes with a powerful `search-docs` tool you should use before any other approaches. This tool automatically passes a list of installed packages and their versions to the remote Boost API, so it returns only version-specific documentation specific for the user's circumstance. You should pass an array of packages to filter on if you know you need docs for particular packages.
- The 'search-docs' tool is perfect for all Laravel related packages, including Laravel, Inertia, Livewire, Filament, Tailwind, Pest, Nova, Nightwatch, etc.
- You must use this tool to search for Laravel-ecosystem documentation before falling back to other approaches.
- Search the documentation before making code changes to ensure we are taking the correct approach.
- Use multiple, broad, simple, topic based queries to start. For example: `['rate limiting', 'routing rate limiting', 'routing']`.
- Do not add package names to queries - package information is already shared. For example, use `test resource table`, not `filament 4 test resource table`.

### Available Search Syntax
- You can and should pass multiple queries at once. The most relevant results will be returned first.

1. Simple Word Searches with auto-stemming - query=authentication - finds 'authenticate' and 'auth'
2. Multiple Words (AND Logic) - query=rate limit - finds knowledge containing both "rate" AND "limit"
3. Quoted Phrases (Exact Position) - query="infinite scroll" - Words must be adjacent and in that order
4. Mixed Queries - query=middleware "rate limit" - "middleware" AND exact phrase "rate limit"
5. Multiple Queries - queries=["authentication", "middleware"] - ANY of these terms


=== php rules ===

## PHP

- Always use curly braces for control structures, even if it has one line.

### Constructors
- Use PHP 8 constructor property promotion in `__construct()`.
    - <code-snippet>public function __construct(public GitHub $github) { }</code-snippet>
- Do not allow empty `__construct()` methods with zero parameters.

### Type Declarations
- Always use explicit return type declarations for methods and functions.
- Use appropriate PHP type hints for method parameters.

<code-snippet name="Explicit Return Types and Method Params" lang="php">
protected function isAccessible(User $user, ?string $path = null): bool
{
    ...
}
</code-snippet>

## Comments
- Prefer PHPDoc blocks over comments. Never use comments within the code itself unless there is something _very_ complex going on.

## PHPDoc Blocks
- Add useful array shape type definitions for arrays when appropriate.

## Enums
- Typically, keys in an Enum should be TitleCase. For example: `FavoritePerson`, `BestLake`, `Monthly`.


=== laravel/core rules ===

## Do Things the Laravel Way

- Use `php artisan make:` commands to create new files (i.e. migrations, controllers, models, etc.). You can list available Artisan commands using the `list-artisan-commands` tool.
- If you're creating a generic PHP class, use `artisan make:class`.
- Pass `--no-interaction` to all Artisan commands to ensure they work without user input. You should also pass the correct `--options` to ensure correct behavior.

### Database
- Always use proper Eloquent relationship methods with return type hints. Prefer relationship methods over raw queries or manual joins.
- Use Eloquent models and relationships before suggesting raw database queries
- Avoid `DB::`; prefer `Model::query()`. Generate code that leverages Laravel's ORM capabilities rather than bypassing them.
- Generate code that prevents N+1 query problems by using eager loading.
- Use Laravel's query builder for very complex database operations.

### Model Creation
- When creating new models, create useful factories and seeders for them too. Ask the user if they need any other things, using `list-artisan-commands` to check the available options to `php artisan make:model`.

### APIs & Eloquent Resources
- For APIs, default to using Eloquent API Resources and API versioning unless existing API routes do not, then you should follow existing application convention.

### Controllers & Validation
- Always create Form Request classes for validation rather than inline validation in controllers. Include both validation rules and custom error messages.
- Check sibling Form Requests to see if the application uses array or string based validation rules.

### Queues
- Use queued jobs for time-consuming operations with the `ShouldQueue` interface.

### Authentication & Authorization
- Use Laravel's built-in authentication and authorization features (gates, policies, Sanctum, etc.).

### URL Generation
- When generating links to other pages, prefer named routes and the `route()` function.

### Configuration
- Use environment variables only in configuration files - never use the `env()` function directly outside of config files. Always use `config('app.name')`, not `env('APP_NAME')`.

### Testing
- When creating models for tests, use the factories for the models. Check if the factory has custom states that can be used before manually setting up the model.
- Faker: Use methods such as `$this->faker->word()` or `fake()->randomDigit()`. Follow existing conventions whether to use `$this->faker` or `fake()`.
- When creating tests, make use of `php artisan make:test [options] <name>` to create a feature test, and pass `--unit` to create a unit test. Most tests should be feature tests.

### Vite Error
- If you receive an "Illuminate\Foundation\ViteException: Unable to locate file in Vite manifest" error, you can run `npm run build` or ask the user to run `npm run dev` or `composer run dev`.


=== laravel/v12 rules ===

## Laravel 12

- Use the `search-docs` tool to get version specific documentation.
- Since Laravel 11, Laravel has a new streamlined file structure which this project uses.

### Laravel 12 Structure
- No middleware files in `app/Http/Middleware/`.
- `bootstrap/app.php` is the file to register middleware, exceptions, and routing files.
- `bootstrap/providers.php` contains application specific service providers.
- **No app\Console\Kernel.php** - use `bootstrap/app.php` or `routes/console.php` for console configuration.
- **Commands auto-register** - files in `app/Console/Commands/` are automatically available and do not require manual registration.

### Database
- When modifying a column, the migration must include all of the attributes that were previously defined on the column. Otherwise, they will be dropped and lost.
- Laravel 11 allows limiting eagerly loaded records natively, without external packages: `$query->latest()->limit(10);`.

### Models
- Casts can and likely should be set in a `casts()` method on a model rather than the `$casts` property. Follow existing conventions from other models.


=== pint/core rules ===

## Laravel Pint Code Formatter

- You must run `vendor/bin/pint --dirty` before finalizing changes to ensure your code matches the project's expected style.
- Do not run `vendor/bin/pint --test`, simply run `vendor/bin/pint` to fix any formatting issues.


=== pest/core rules ===

## Pest

### Testing
- If you need to verify a feature is working, write or update a Unit / Feature test.

### Pest Tests
- All tests must be written using Pest. Use `php artisan make:test --pest <name>`.
- You must not remove any tests or test files from the tests directory without approval. These are not temporary or helper files - these are core to the application.
- Tests should test all of the happy paths, failure paths, and weird paths.
- Tests live in the `tests/Feature` and `tests/Unit` directories.
- Pest tests look and behave like this:
<code-snippet name="Basic Pest Test Example" lang="php">
it('is true', function () {
    expect(true)->toBeTrue();
});
</code-snippet>

### Running Tests
- Run the minimal number of tests using an appropriate filter before finalizing code edits.
- To run all tests: `php artisan test`.
- To run all tests in a file: `php artisan test tests/Feature/ExampleTest.php`.
- To filter on a particular test name: `php artisan test --filter=testName` (recommended after making a change to a related file).
- When the tests relating to your changes are passing, ask the user if they would like to run the entire test suite to ensure everything is still passing.

### Pest Assertions
- When asserting status codes on a response, use the specific method like `assertForbidden` and `assertNotFound` instead of using `assertStatus(403)` or similar, e.g.:
<code-snippet name="Pest Example Asserting postJson Response" lang="php">
it('returns all', function () {
    $response = $this->postJson('/api/docs', []);

    $response->assertSuccessful();
});
</code-snippet>

### Mocking
- Mocking can be very helpful when appropriate.
- When mocking, you can use the `Pest\Laravel\mock` Pest function, but always import it via `use function Pest\Laravel\mock;` before using it. Alternatively, you can use `$this->mock()` if existing tests do.
- You can also create partial mocks using the same import or self method.

### Datasets
- Use datasets in Pest to simplify tests which have a lot of duplicated data. This is often the case when testing validation rules, so consider going with this solution when writing tests for validation rules.

<code-snippet name="Pest Dataset Example" lang="php">
it('has emails', function (string $email) {
    expect($email)->not->toBeEmpty();
})->with([
    'james' => 'james@laravel.com',
    'taylor' => 'taylor@laravel.com',
]);
</code-snippet>


=== pest/v4 rules ===

## Pest 4

- Pest v4 is a huge upgrade to Pest and offers: browser testing, smoke testing, visual regression testing, test sharding, and faster type coverage.
- Browser testing is incredibly powerful and useful for this project.
- Browser tests should live in `tests/Browser/`.
- Use the `search-docs` tool for detailed guidance on utilizing these features.

### Browser Testing
- You can use Laravel features like `Event::fake()`, `assertAuthenticated()`, and model factories within Pest v4 browser tests, as well as `RefreshDatabase` (when needed) to ensure a clean state for each test.
- Interact with the page (click, type, scroll, select, submit, drag-and-drop, touch gestures, etc.) when appropriate to complete the test.
- If requested, test on multiple browsers (Chrome, Firefox, Safari).
- If requested, test on different devices and viewports (like iPhone 14 Pro, tablets, or custom breakpoints).
- Switch color schemes (light/dark mode) when appropriate.
- Take screenshots or pause tests for debugging when appropriate.

### Example Tests

<code-snippet name="Pest Browser Test Example" lang="php">
it('may reset the password', function () {
    Notification::fake();

    $this->actingAs(User::factory()->create());

    $page = visit('/sign-in'); // Visit on a real browser...

    $page->assertSee('Sign In')
        ->assertNoJavascriptErrors() // or ->assertNoConsoleLogs()
        ->click('Forgot Password?')
        ->fill('email', 'nuno@laravel.com')
        ->click('Send Reset Link')
        ->assertSee('We have emailed your password reset link!')

    Notification::assertSent(ResetPassword::class);
});
</code-snippet>

<code-snippet name="Pest Smoke Testing Example" lang="php">
$pages = visit(['/', '/about', '/contact']);

$pages->assertNoJavascriptErrors()->assertNoConsoleLogs();
</code-snippet>


=== tailwindcss/core rules ===

## Tailwind Core

- Use Tailwind CSS classes to style HTML, check and use existing tailwind conventions within the project before writing your own.
- Offer to extract repeated patterns into components that match the project's conventions (i.e. Blade, JSX, Vue, etc..)
- Think through class placement, order, priority, and defaults - remove redundant classes, add classes to parent or child carefully to limit repetition, group elements logically
- You can use the `search-docs` tool to get exact examples from the official documentation when needed.

### Spacing
- When listing items, use gap utilities for spacing, don't use margins.

    <code-snippet name="Valid Flex Gap Spacing Example" lang="html">
        <div class="flex gap-8">
  
... [TRUNCATED]
```

