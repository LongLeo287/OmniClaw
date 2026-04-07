---
id: google-drive-laravel-integrate
type: knowledge
owner: OA_Triage
---
# google-drive-laravel-integrate
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Google Drive Laravel

The free Laravel package to help you manage your Google Drive

## Use Cases

- CRUD files and folders on your Google Drive
- Upload and download without normal Google Drive exceeded limits

## Features

- Dynamic Google Service credentials from config/google-service.php
- Dynamic Google Drive properties from config/google-drive.php
- Easy to CRUD files and folders on your Google Drive with a simple line code

## Know issues

- This package uses the latest official SDK, libraries and methods from Google then it might be large (around 30mb for dependency package google/apiclient) for shared hosting.
- Please consider your server's environment before using this package.
- However, we still recommend that you follow the latest writing style for Google libraries to ensure safety, compliance, CI/CD and most importantly if you are using services

## Requirements

- **PHP**: 8.1 or higher
- **Laravel** 9.0 or higher

## Quick Start

If you prefer to install this package into your own Laravel application, please follow the installation steps below

## Installation

#### Step 1. Install a Laravel project if you don't have one already

https://laravel.com/docs/installation

#### Step 2. Require the current package using composer:

```bash
composer require funnydevjsc/google-drive-laravel-integrate
```

#### Step 3. Create a Google Service credentials:

- As our guide at https://github.com/funnydevjsc/google-client-laravel-integrate.

#### Step 4. Publish the controller file and config file

```bash
php artisan vendor:publish --provider="FunnyDev\GoogleDrive\GoogleDriveServiceProvider" --tag="funnydev-google-drive"
```

If publishing files fails, please create corresponding files at the path `config/google-drive.php` from this package.

#### Step 5. Update the various config settings in the published config file:

- After publishing the package assets a configuration file will be located at <code>config/google-drive.php</code>.
- Find your Google Drive parent folder ID and fill into <code>config/google-drive.php</code> file like this (your files and folders might be uploaded and managed within this parent folder):

<img src="screenshots/google-drive-create-parent-folder-sample.png">

<img src="screenshots/google-drive-get-parent-folder-id-sample.png">

## Testing

``` php
use FunnyDev\GoogleDrive\GoogleDriveSdk;

class TestDrive
{
    /**
     * Handle the event.
     * @throws \Exception
     */
    public function handle(): void
    {
        $drive = new GoogleDriveSdk();
        
        $folderId = $drive->createFolder('test', config('google-drive.parent_folder_id'));
        
        $fileId = $drive->uploadFile(
            $folderId,
            'file_uploaded.txt',
            file_get_contents(storage_path('file.txt')),
            'text/plain'
        );
        
        $drive->shareResource($fileId, 'test@example.com', 'writer');
        
        $file = $drive->downloadFile($fileId);
        file_put_contents(storage_path('file_downloaded.txt'), $file);
        
        if ($drive->deleteResource($fileId)) {
            echo 'Deleted file';
        }
    }
}
```

## Feedback

Respect us in the [Laravel Việt Nam](https://www.facebook.com/groups/167363136987053)

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) for details.

### Security

If you discover any security related issues, please email contact@funnydev.vn or use the issue tracker.

## Credits

- [Funny Dev., Jsc](https://github.com/funnydevjsc)
- [All Contributors](../../contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

```

### File: composer.json
```json
{
    "name": "funnydevjsc/google-drive-laravel-integrate",
    "description": "Laravel package for Google Drive management",
    "type": "library",
    "license": "MIT",
    "version": "1.0.5",
    "autoload": {
        "psr-4": {
            "FunnyDev\\GoogleDrive\\": "src/"
        }
    },
    "authors": [
        {
            "name": "Funny dev., Jsc",
            "email": "contact@funnydev.vn",
            "homepage": "https://github.com/funnydevjsc"
        }
    ],
    "homepage": "https://github.com/funnydevjsc/google-drive-laravel-integrate",
    "keywords": ["Laravel", "package", "drive", "google", "gdrive"],
    "require": {
        "php": "^8.1|^8.2|^8.3|^8.4",
        "funnydevjsc/google-client-laravel-integrate": "^1.0"
    },
    "require-dev": {
    "illuminate/support": "^8.83",
    "illuminate/http": "^8.83",
    "illuminate/routing": "^8.83",
    "illuminate/console": "^8.83",
    "phpunit/phpunit": "^10.5"
  },
  "scripts": {
    "test": "vendor/bin/phpunit"
  },
    "extra": {
        "laravel": {
            "providers": [
                "FunnyDev\\GoogleDrive\\GoogleDriveServiceProvider"
            ]
        }
    },
    "minimum-stability": "stable",
    "prefer-stable": true
}

```

### File: CONTRIBUTING.md
```md
# Contributing

Contributions are **welcome** and will be fully **credited**.

Please read and understand the contribution guide before creating an issue or pull request.

## Etiquette

This project is open source, and as such, the maintainers give their free time to build and maintain the source code
held within. They make the code freely available in the hope that it will be of use to other developers. It would be
extremely unfair for them to suffer abuse or anger for their hard work.

Please be considerate towards maintainers when raising issues or presenting pull requests. Let's show the
world that developers are civilized and selfless people.

It's the duty of the maintainer to ensure that all submissions to the project are of sufficient
quality to benefit the project. Many developers have different skillsets, strengths, and weaknesses. Respect the maintainer's decision, and do not be upset or abusive if your submission is not used.

## Viability

When requesting or submitting new features, first consider whether it might be useful to others. Open
source projects are used by many developers, who may have entirely different needs to your own. Think about
whether or not your feature is likely to be used by other users of the project.

## Procedure

Before filing an issue:

- Attempt to replicate the problem, to ensure that it wasn't a coincidental incident.
- Check to make sure your feature suggestion isn't already present within the project.
- Check the pull requests tab to ensure that the bug doesn't have a fix in progress.
- Check the pull requests tab to ensure that the feature isn't already in progress.

Before submitting a pull request:

- Check the codebase to ensure that your feature doesn't already exist.
- Check the pull requests to ensure that another person hasn't already submitted the feature or fix.

## Requirements

If the project maintainer has any additional requirements, you will find them listed here.

- **[PSR-12 Coding Standard](https://www.php-fig.org/psr/psr-12/)** - The easiest way to apply the conventions is to install [Laravel Pint](https://laravel.com/docs/10.x/pint) and [setting the preset to psr12](https://laravel.com/docs/10.x/pint#presets)

- **Add tests!** - Your patch won't be accepted if it doesn't have tests.

- **Document any change in behaviour** - Make sure the `README.md` and any other relevant documentation are kept up-to-date.

- **Consider our release cycle** - We try to follow [SemVer v2.0.0](https://semver.org/). Randomly breaking public APIs is not an option.

- **One pull request per feature** - If you want to do more than one thing, send multiple pull requests.

- **Send coherent history** - Make sure each individual commit in your pull request is meaningful. If you had to make multiple intermediate commits while developing, please [squash them](https://www.git-scm.com/book/en/v2/Git-Tools-Rewriting-History#Changing-Multiple-Commit-Messages) before submitting.

**Happy coding**!

```

### File: LICENSE.md
```md
MIT License

Copyright (c) 2023 Venture Drake

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### File: config\google-drive.php
```php
<?php

return [
    'parent_folder_id' => env('GOOGLE_DRIVE_PARENT_FOLDER_ID')
];
```

### File: src\GoogleDriveSdk.php
```php
<?php

namespace FunnyDev\GoogleDrive;

use FunnyDev\GoogleClient\GoogleServiceClient;
use Google\Client;
use Google\Service\Drive;
use Google\Service\Drive\DriveFile;
use Google\Service\Drive\Permission;
use Google\Service\Exception as GoogleException;
use GuzzleHttp\Psr7\Utils;
use Exception;

class GoogleDriveSdk
{
    public Client $client;
    protected Drive $drive;

    /**
     * @throws Exception
     * @throws GoogleException
     */
    public function __construct(array $credentials=null, string $credentials_path=null)
    {
        $this->client = (new GoogleServiceClient($credentials, $credentials_path))->instance();
        $this->client->addScope(Drive::DRIVE);
        $this->drive = new Drive($this->client);
    }

    /**
     * @throws GoogleException
     */
    public function createFolder(string $name, string $parentFolderId=''): string
    {
        $folderMetadata = [
            'name' => $name,
            'mimeType' => 'application/vnd.google-apps.folder',
        ];
        if ($parentFolderId) {
            $folderMetadata['parents'] = [$parentFolderId];
        }
        $fileMetadata = new Drive\DriveFile($folderMetadata);
        $folder = $this->drive->files->create($fileMetadata, array('fields' => 'id', 'supportsAllDrives' => true));
        return $folder->id;
    }
    
    /**
     * @throws GoogleException
     */
    public function readFolder(string $folderId): array
    {
        $files = array();
        $pageToken = null;
        do {
            $response = $this->drive->files->listFiles(array(
                'q' => '',
                'spaces' => 'drive',
                'pageToken' => $pageToken,
                'fields' => 'nextPageToken, files(id, name)',
            ));
            if (!empty($response->files)) {
                $files[] = $response->files;
            }
            if (isset($response->pageToken) && $response->pageToken) {
                $pageToken = $response->pageToken;
            } else {
                $pageToken = null;
            }
        } while ($pageToken != null);
        return array_merge(...$files);
    }

    /**
     * @throws GoogleException
     */
    public function deleteResource(string $resourceId): bool
    {
        return boolval($this->drive->files->delete($resourceId, ['supportsAllDrives' => true]));
    }

    /**
     * @throws GoogleException
     */
    public function shareResource(string $resourceId, string $email, string $role='writer'): void
    {
        $this->drive->permissions->create($resourceId, new Permission([
            'type' => 'user',
            'role' => $role,
            'emailAddress' => $email,
        ]), ['sendNotificationEmail' => false, 'supportsAllDrives' => true]);
    }



    /**
     * @throws GoogleException
     */
    public function uploadFile(string $parentFolderId, string $name, mixed $content, string $mimeType='application/octet-stream'): string {
        $fileMetadata = new Drive\DriveFile(array(
            'name' => $name,
            'parents' => array($parentFolderId)
        ));
        $file = $this->drive->files->create($fileMetadata, array('data' => $content, 'mimeType' => $mimeType, 'uploadType' => 'multipart', 'fields' => 'id', 'supportsAllDrives' => true));
        return $file->id;
    }

    /**
     * @throws GoogleException
     */
    public function moveFile(string $fileId, string $newParentFolderId): bool
    {
        $emptyFileMetadata = new DriveFile();
        $file = $this->drive->files->get($fileId, array('fields' => 'parents'));
        $previousParents = join(',', $file->parents);
        $file = $this->drive->files->update($fileId, $emptyFileMetadata, array(
            'addParents' => $newParentFolderId,
            'removeParents' => $previousParents,
            'fields' => 'id, parents',
            'supportsAllDrives' => true
        ));
        return !!empty($file->parents);
    }

    /**
     * @throws GoogleException
     */
    public function downloadFile(string $fileId): mixed
    {
        $response = $this->drive->files->get($fileId, ['alt' => 'media']);
        return $response->getBody()->getContents();
    }

    /**
     * @throws GoogleException
     */
    public function streamDownloadFile(string $fileId, string $fileName, string $mimeType = 'application/octet-stream', mixed $range=null)
    {
        ini_set('zlib.output_compression', 'Off');
        if (function_exists('apache_setenv')) {
            apache_setenv('no-gzip', '1');
        }
        ini_set('output_buffering', 'Off');
        ini_set('implicit_flush', 1);

        $response = $this->drive->files->get($fileId, ['alt' => 'media']);
        $fileStream = Utils::streamFor($response->getBody());
        $fileSize = $fileStream->getSize();

        if (!$range) {
            $range = request()->header('Range');
        }
        if ($range) {
            preg_match('/bytes=(\d+)-(\d+)?/', $range, $matches);
            $start = intval($matches[1]);
            $end = isset($matches[2]) ? intval($matches[2]) : $fileSize - 1;

            $fileStream->seek($start);
            $length = ($end - $start) + 1;

            return response()->stream(function () use ($fileStream, $length) {
                echo $fileStream->read($length);
                flush();
            }, 206, [
                'Content-Type' => $mimeType,
                'Content-Length' => $length,
                'Content-Range' => "bytes $start-$end/$fileSize",
                'Accept-Ranges' => 'bytes',
            ]);
        }

        return response()->stream(function () use ($fileStream) {
            while (!$fileStream->eof()) {
                echo $fileStream->read(1024 * 64);
                flush();
            }
        }, 200, [
            'Content-Type' => $mimeType,
            'Content-Length' => $fileSize,
            'Content-Disposition' => 'attachment; filename="' . $fileName . '"',
            'Accept-Ranges' => 'bytes',
        ]);
    }

    /**
     * @throws GoogleException
     */
    public function streamDownloadVideoToHls(string $fileId, string $fileName='stream', int $splitSeconds=10): mixed
    {
        ini_set('zlib.output_compression', 'Off');
        if (function_exists('apache_setenv')) {
            apache_setenv('no-gzip', '1');
        }
        ini_set('output_buffering', 'Off');
        ini_set('implicit_flush', 1);

        $response = $this->drive->files->get($fileId, ['alt' => 'media']);
        $fileStream = Utils::streamFor($response->getBody());

        $cmd = "ffmpeg -i pipe:0 -c:v copy -c:a copy -f hls -hls_time '.$splitSeconds.' -hls_playlist_type vod pipe:1";
        $descriptors = [
            ['pipe', 'r'],
            ['pipe', 'w'],
            ['pipe', 'w']
        ];

        $process = proc_open($cmd, $descriptors, $pipes);

        if (is_resource($process)) {
            while (!$fileStream->eof()) {
                fwrite($pipes[0], $fileStream->read(1024 * 8));
            }
            fclose($pipes[0]);

            return response()->stream(function () use ($pipes, $process) {
                while (!feof($pipes[1])) {
                    echo fread($pipes[1], 1024 * 8);
                    flush();
                }

                fclose($pipes[1]);
                fclose($pipes[2]);
                proc_close($process);
            }, 200, [
                'Content-Type' => 'application/vnd.apple.mpegurl',
                'Content-Disposition' => 'inline; filename="'.$fileName.'.m3u8"',
            ]);
        }

        return false;
    }

    /**
     * @throws GoogleException
     */
    public function emptyTrash(): bool
    {
        return boolval($this->drive->files->emptyTrash(['supportsAllDrives' => true]));
    }
}

```

### File: src\GoogleDriveServiceProvider.php
```php
<?php

namespace FunnyDev\GoogleDrive;

use Illuminate\Support\Facades\Artisan;
use Illuminate\Support\ServiceProvider;

class GoogleDriveServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any package services.
     *
     * @return void
     */
    public function boot(): void
    {
        $this->publishes([
            __DIR__ . '/../config/google-drive.php' => config_path('google-drive.php'),
        ], 'funnydev-google-drive');

        try {
            if (!file_exists(config_path('google-drive.php'))) {
                $this->commands([
                    \Illuminate\Foundation\Console\VendorPublishCommand::class,
                ]);

                Artisan::call('vendor:publish', ['--provider' => 'FunnyDev\\GoogleDrive\\GoogleDriveServiceProvider', '--tag' => ['funnydev-google-drive']]);
            }
        } catch (\Exception $e) {}
    }

    /**
     * Register any package services.
     *
     * @return void
     */
    public function register(): void
    {
        $this->mergeConfigFrom(
            __DIR__ . '/../config/google-drive.php', 'google-drive'
        );
        $this->app->singleton(\FunnyDev\GoogleDrive\GoogleDriveSdk::class, function () {
            return new \FunnyDev\GoogleDrive\GoogleDriveSdk;
        });
    }
}

```

### File: tests\GoogleDriveSdkTest.php
```php
<?php

use FunnyDev\GoogleDrive\GoogleDriveSdk;
use Google\Service\Drive;
use Google\Service\Drive\Permission as GooglePermission;
use PHPUnit\Framework\TestCase;

class GoogleDriveSdkTest extends TestCase
{
    private function makeSdkWithDrive(Drive $drive): GoogleDriveSdk
    {
        $ref = new ReflectionClass(GoogleDriveSdk::class);
        /** @var GoogleDriveSdk $sdk */
        $sdk = $ref->newInstanceWithoutConstructor();
        $prop = $ref->getProperty('drive');
        $prop->setAccessible(true);
        $prop->setValue($sdk, $drive);
        return $sdk;
    }

    public function testCreateFolderReturnsId(): void
    {
        $files = new FakeFilesResource();
        $permissions = new FakePermissionsResource();
        $drive = new Drive([]);
        $drive->files = $files;
        $drive->permissions = $permissions;

        $sdk = $this->makeSdkWithDrive($drive);

        $id = $sdk->createFolder('test-folder', 'parent-1');

        $this->assertNotEmpty($id);
        $this->assertSame('create', $files->lastCall['method'] ?? null);
        $this->assertSame(['fields' => 'id', 'supportsAllDrives' => true], $files->lastCall['params'] ?? null);
    }

    public function testReadFolderAggregatesPages(): void
    {
        $files = new FakeFilesResource();
        $files->setListPages([
            (object) ['files' => [(object)['id' => 'f1', 'name' => 'A']], 'pageToken' => 't2'],
            (object) ['files' => [(object)['id' => 'f2', 'name' => 'B']], 'pageToken' => null],
        ]);
        $drive = new Drive([]);
        $drive->files = $files;
        $drive->permissions = new FakePermissionsResource();

        $sdk = $this->makeSdkWithDrive($drive);

        $result = $sdk->readFolder('ignored-folder-id');

        $this->assertCount(2, $result);
        $this->assertEquals('f1', $result[0]->id);
        $this->assertEquals('f2', $result[1]->id);
    }

    public function testUploadFileReturnsId(): void
    {
        $files = new FakeFilesResource();
        $drive = new Drive([]);
        $drive->files = $files;
        $drive->permissions = new FakePermissionsResource();

        $sdk = $this->makeSdkWithDrive($drive);

        $id = $sdk->uploadFile('parent-1', 'file.txt', 'CONTENT', 'text/plain');

        $this->assertNotEmpty($id);
        $this->assertSame('create', $files->lastCall['method'] ?? null);
        $this->assertSame('multipart', $files->lastCall['params']['uploadType'] ?? null);
    }

    public function testMoveFileReturnsFalsePerCurrentLogic(): void
    {
        $files = new FakeFilesResource();
        $files->setFileParents('file-1', ['old-parent']);
        $drive = new Drive([]);
        $drive->files = $files;
        $drive->permissions = new FakePermissionsResource();

        $sdk = $this->makeSdkWithDrive($drive);

        $result = $sdk->moveFile('file-1', 'new-parent');

        // With stub returning non-empty parents after update, the current implementation returns false
        $this->assertFalse($result);
        $this->assertSame('update', $files->lastCall['method'] ?? null);
        $this->assertSame('new-parent', $files->lastCall['params']['addParents'] ?? null);
    }

    public function testDownloadFileReturnsExactContent(): void
    {
        $files = new FakeFilesResource();
        $files->setFileContent('file-1', 'HELLO-WORLD');
        $drive = new Drive([]);
        $drive->files = $files;
        $drive->permissions = new FakePermissionsResource();

        $sdk = $this->makeSdkWithDrive($drive);

        $content = $sdk->downloadFile('file-1');
        $this->assertSame('HELLO-WORLD', $content);
    }

    public function testDeleteResourceReturnsTrue(): void
    {
        $files = new FakeFilesResource();
        $drive = new Drive([]);
        $drive->files = $files;
        $drive->permissions = new FakePermissionsResource();

        $sdk = $this->makeSdkWithDrive($drive);

        $this->assertTrue($sdk->deleteResource('x-id'));
        $this->assertSame('x-id', $files->lastCall['id'] ?? null);
    }

    public function testShareResourceCallsPermissionsCreate(): void
    {
        $files = new FakeFilesResource();
        $permissions = new FakePermissionsResource();
        $drive = new Drive([]);
        $drive->files = $files;
        $drive->permissions = $permissions;

        $sdk = $this->makeSdkWithDrive($drive);

        $sdk->shareResource('rid-1', 'user@example.com', 'reader');

        $this->assertNotNull($permissions->lastCreateArgs);
        $this->assertSame('rid-1', $permissions->lastCreateArgs['resourceId']);
        $this->assertInstanceOf(GooglePermission::class, $permissions->lastCreateArgs['permission']);
        /** @var GooglePermission $perm */
        $perm = $permissions->lastCreateArgs['permission'];
        $this->assertSame('user@example.com', $perm->emailAddress);
        $this->assertSame('reader', $perm->role);
        $this->assertSame(['sendNotificationEmail' => false, 'supportsAllDrives' => true], $permissions->lastCreateArgs['params']);
    }

    public function testEmptyTrashReturnsTrue(): void
    {
        $files = new FakeFilesResource();
        $drive = new Drive([]);
        $drive->files = $files;
        $drive->permissions = new FakePermissionsResource();

        $sdk = $this->makeSdkWithDrive($drive);

        $this->assertTrue($sdk->emptyTrash());
    }
}

// ----------------------------
// Test Doubles for Google Drive Resources
// ----------------------------

class FakeFilesResource
{
    public array $lastCall = [];
    private array $listPages = [];
    private int $listIndex = 0;
    private array $fileParents = [];
    private array $fileContents = [];

    public function setListPages(array $pages): void
    {
        $this->listPages = $pages;
        $this->listIndex = 0;
    }

    public function setFileParents(string $fileId, array $parents): void
    {
        $this->fileParents[$fileId] = $parents;
    }

    public function setFileContent(string $fileId, string $content): void
    {
        $this->fileContents[$fileId] = $content;
    }

    public function create($fileMetadata, array $params = [])
    {
        $this->lastCall = ['method' => 'create', 'params' => $params, 'metadata' => $fileMetadata];
        return (object)['id' => uniqid('id_', true)];
    }

    public function listFiles(array $params = [])
    {
        $this->lastCall = ['method' => 'listFiles', 'params' => $params];
        if ($this->listIndex < count($this->listPages)) {
            return $this->listPages[$this->listIndex++];
        }
        return (object)['files' => [], 'pageToken' => null];
    }

    public function get(string $fileId, array $params = [])
    {
        $this->lastCall = ['method' => 'get', 'id' => $fileId, 'params' => $params];
        if (isset($params['alt']) && $params['alt'] === 'media') {
            $content = $this->fileContents[$fileId] ?? '';
            return new FakeResponse($content);
        }
        $parents = $this->fileParents[$fileId] ?? [];
        return (object)['parents' => $parents];
    }

    public function update(string $fileId, $fileMetadata, array $params = [])
    {
        $this->lastCall = ['method' => 'update', 'id' => $fileId, 'params' => $params];
        // Simulate new parents applied
        $parents = [];
        if (!empty($params['addParents'])) {
            $parents = array_map('trim', explode(',', (string)$params['addParents']));
        }
        return (object)['parents' => $parents];
    }

    public function delete(string $fileId, array $params = [])
    {
        $this->lastCall = ['method' => 'delete', 'id' => $fileId, 'params' => $params];
        return 1;
    }

    public function emptyTrash(array $params = [])
    {
        $this->lastCall = ['method' => 'emptyTrash', 'params' => $params];
        return 1;
    }
}

class FakePermissionsResource
{
    public ?array $lastCreateArgs = null;

    public function create(string $resourceId, GooglePermission $permission, array $params = [])
    {
        $this->lastCreateArgs = [
            'resourceId' => $resourceId,
            'permission' => $permission,
            'params' => $params,
        ];
        return (object)['id' => uniqid('perm_', true)];
    }
}

class FakeResponse
{
    private FakeBody $body;

    public function __construct(string $content)
    {
        $this->body = new FakeBody($content);
    }

    public function getBody(): FakeBody
    {
        return $this->body;
    }
}

class FakeBody
{
    private string $content;

    public function __construct(string $content)
    {
        $this->content = $content;
    }

    public function getContents(): string
    {
        return $this->content;
    }
}

```

