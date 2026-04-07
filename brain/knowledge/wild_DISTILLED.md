---
id: wild
type: knowledge
owner: OA_Triage
---
# wild
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Wild Workouts

Wild Workouts is an **example Go DDD** project that we created to show how to build Go applications that are **easy to develop, maintain, and fun to work with, especially in the long term!**

*The idea for this series, is to apply DDD by refactoring. This process is in progress! Please check articles, to know the current progress.*

No application is perfect from the beginning. With over a dozen coming articles, we will uncover what issues you can find in the current implementation. We will also show how to fix these issues and achieve clean implementation by refactoring.

### Articles

#### "Too modern" application

1. [**Too modern Go application? Building a serverless application with Google Cloud Run and Firebase**](https://threedots.tech/post/serverless-cloud-run-firebase-modern-go-application/?utm_source=github.com) _[[v1.0]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v1.0)_
2. [**A complete Terraform setup of a serverless application on Google Cloud Run and Firebase**](https://threedots.tech/post/complete-setup-of-serverless-application/?utm_source=github.com) _[[v1.1]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v1.1)_
3. [**Robust gRPC communication on Google Cloud Run (but not only!)**](https://threedots.tech/post/robust-grpc-google-cloud-run/?utm_source=github.com) _[[v1.2]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v1.2)_
4. [**You should not build your own authentication. Let Firebase do it for you.**](https://threedots.tech/post/firebase-cloud-run-authentication/?utm_source=github.com) _[[v1.3]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v1.3)_

#### Refactoring

5. [**Business Applications in Go: Things to know about DRY**](https://threedots.tech/post/things-to-know-about-dry/?utm_source=github.com) _[[v2.0]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v2.0)_
6. [**When microservices in Go are not enough: introduction to DDD Lite**](https://threedots.tech/post/ddd-lite-in-go-introduction/?utm_source=github.com) _[[v2.1]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v2.1)_
7. [**Repository pattern: painless way to simplify your Go service logic**](https://threedots.tech/post/repository-pattern-in-go/?utm_source=github.com) _[[v2.2]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v2.2)_
8. [**4 practical principles of high-quality database integration tests in Go**](https://threedots.tech/post/database-integration-testing/?utm_source=github.com) _[[v2.3]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v2.3)_
9. [**Introducing Clean Architecture by refactoring a Go project**](https://threedots.tech/post/introducing-clean-architecture/?utm_source=github.com) _[[v2.4]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v2.4)_
10. [**Introducing basic CQRS by refactoring**](https://threedots.tech/post/basic-cqrs-in-go/?utm_source=github.com) _[[v2.5]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v2.5)_
11. [**Combining DDD, CQRS, and Clean Architecture**](https://threedots.tech/post/ddd-cqrs-clean-architecture-combined/?utm_source=github.com)
12. [**Microservices test architecture. Can you sleep well without end-to-end tests?**](https://threedots.tech/post/microservices-test-architecture/?utm_source=github.com) _[[v2.6]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v2.6)_
13. [**Repository secure by design: how to sleep better without fear of security vulnerabilities**](https://threedots.tech/post/repository-secure-by-design/?utm_source=github.com)
14. [**Running integration tests on Google Cloud Build using docker-compose**](https://threedots.tech/post/running-integration-tests-on-google-cloud-build/?utm_source=github.com) _[[v2.7]](https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/releases/tag/v2.7)_
15. *More articles are on the way!*

### Community

We're building a Discord community focused on modern business applications. It's the place to discuss hard topics, request a review, or ask if something's not clear. [Come join us!](https://discord.gg/kTVsGjPYDn)

### Directories

- [api](api/) OpenAPI and gRPC definitions
- [docker](docker/) Dockerfiles
- [internal](internal/) application code
- [scripts](scripts/) deployment and development scripts
- [terraform](terraform/) - infrastructure definition
- [web](web/) - frontend JavaScript code

### Live Demo

The example application is available at [https://threedotslabs-wildworkouts.web.app/](https://threedotslabs-wildworkouts.web.app/).

### Running locally

```go
> docker-compose up

# ...

web_1             |  INFO  Starting development server...
web_1             |  DONE  Compiled successfully in 6315ms11:18:26 AM
web_1             |
web_1             |
web_1             |   App running at:
web_1             |   - Local:   http://localhost:8080/
web_1             |
web_1             |   It seems you are running Vue CLI inside a container.
web_1             |   Access the dev server via http://localhost:<your container's external mapped port>/
web_1             |
web_1             |   Note that the development build is not optimized.
web_1             |   To create a production build, run yarn build.
```

### Google Cloud Deployment

```go
> cd terraform/
> make

Fill all required parameters:
	project [current: wild-workouts project]:       # <----- put your Wild Workouts Google Cloud project name here (it will be created) 
	user [current: email@gmail.com]:                # <----- put your Google (Gmail, G-suite etc.) e-mail here
	billing_account [current: My billing account]:  # <----- your billing account name, can be found here https://console.cloud.google.com/billing
	region [current: europe-west1]: 
	firebase_location [current: europe-west]: 

# it may take a couple of minutes...

The setup is almost done!

Now you need to enable Email/Password provider in the Firebase console.
To do this, visit https://console.firebase.google.com/u/0/project/[your-project]/authentication/providers

You can also downgrade the subscription plan to Spark (it's set to Blaze by default).
The Spark plan is completely free and has all features needed for running this project.

Congratulations! Your project should be available at: https://[your-project].web.app

If it's not, check if the build finished successfully: https://console.cloud.google.com/cloud-build/builds?project=[your-project]

If you need help, feel free to contact us at https://threedots.tech
```

### Screenshots

![Wild Workouts login](.github/login.png)
![Wild Workouts trainer's schedule](.github/schedule.png)
![Wild Workouts schedule training](.github/new-training.png)

```

### File: terraform\README.md
```md
## Required software

* Terraform
* gcloud CLI
* Docker (with daemon running)

This setup was tested on the following versions:

```
Terraform v0.12.24

Google Cloud SDK 290.0.1
alpha 2019.05.17
beta 2019.05.17
core 2020.04.24
```

## Setup

1. Authorize in gcloud CLI.

This projects aims for setup as easy as possible. Default application login is not recommended for production use.

```
gcloud auth login
gcloud auth application-default login
```

2. Run make. While terraform is running, you will be asked to confirm applying changes. Answer wih `yes`.

```bash
make
```

You will be asked to pick a region for Cloud Run and Firebase. If you want to use Cloud Run region different than
`europe-west1`, you need to **commit** changes in following files:

- `./scripts/deploy.sh`
- `./web/firebase.json`

3. Make sure you enable `Email/Password` authentication provider in Firebase as described in the `make` output.

a. Open FireBase console: https://console.firebase.google.com
b. Choose `Wild Workouts` project
c. Go to `Authentication`
d. Choose `Sign-in method` tab
e. Click on `Email/Password`, switch to `Enabled` and click `Save`.

## Cloud builds

Go to https://console.cloud.google.com/cloud-build/builds to see your recent builds.

## Destroy

If you want to tear down the project, run `make destroy`.

If you want to create it again, make sure to:
* Use different project name.
* Remove `terraform.tfstate` file.

```

### File: web\package.json
```json
{
  "name": "wild-workouts",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint"
  },
  "dependencies": {
    "@babel/compat-data": "^7.9.0",
    "@babel/core": "^7.18.2",
    "@fullcalendar/core": "^4.4.2",
    "@fullcalendar/daygrid": "^4.4.2",
    "@fullcalendar/interaction": "^4.4.0",
    "@fullcalendar/list": "^4.4.0",
    "@fullcalendar/timegrid": "^4.4.0",
    "@fullcalendar/vue": "^4.4.0",
    "babel-loader": "^8.2.5",
    "bootstrap": "^4.4.1",
    "core-js": "^3.22.6",
    "firebase": "^7.14.0",
    "firebase-auth": "^0.1.2",
    "jquery": "^3.4.1",
    "jsonwebtoken": "^8.5.1",
    "node-sass": "^4.13.1",
    "popper.js": "^1.16.1",
    "sass-loader": "^8.0.2",
    "superagent": "^5.2.2",
    "vue": "^2.6.11",
    "vue-router": "^3.1.6",
    "vue-toast-notification": "^0.2.0",
    "vuejs-dialog": "^1.4.1",
    "@babel/preset-env": "^7.10.2"
  },
  "devDependencies": {
    "@vue/cli-plugin-babel": "~4.2.0",
    "@vue/cli-plugin-eslint": "~4.2.0",
    "@vue/cli-service": "~4.2.0",
    "babel-eslint": "^10.0.3",
    "eslint": "^6.7.2",
    "eslint-plugin-vue": "^6.1.2",
    "vue-template-compiler": "^2.6.11"
  },
  "eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "parserOptions": {
      "parser": "babel-eslint"
    },
    "rules": {}
  },
  "browserslist": [
    "> 1%",
    "last 2 versions"
  ]
}

```

### File: web\src\repositories\clients\trainer\src\index.js
```js
/**
 * Wild Workouts trainer
 * TODO
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Error from './model/Error';
import Hour from './model/Hour';
import HourUpdate from './model/HourUpdate';
import ModelDate from './model/ModelDate';
import DefaultApi from './api/DefaultApi';


/**
* TODO.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var WildWorkoutsTrainer = require('index'); // See note below*.
* var xxxSvc = new WildWorkoutsTrainer.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new WildWorkoutsTrainer.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new WildWorkoutsTrainer.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new WildWorkoutsTrainer.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The Hour model constructor.
     * @property {module:model/Hour}
     */
    Hour,

    /**
     * The HourUpdate model constructor.
     * @property {module:model/HourUpdate}
     */
    HourUpdate,

    /**
     * The ModelDate model constructor.
     * @property {module:model/ModelDate}
     */
    ModelDate,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};

```

### File: web\src\repositories\clients\trainings\src\index.js
```js
/**
 * Wild Workouts trainings
 * TODO
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Error from './model/Error';
import PostTraining from './model/PostTraining';
import Training from './model/Training';
import Trainings from './model/Trainings';
import DefaultApi from './api/DefaultApi';


/**
* TODO.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var WildWorkoutsTrainings = require('index'); // See note below*.
* var xxxSvc = new WildWorkoutsTrainings.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new WildWorkoutsTrainings.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new WildWorkoutsTrainings.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new WildWorkoutsTrainings.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The PostTraining model constructor.
     * @property {module:model/PostTraining}
     */
    PostTraining,

    /**
     * The Training model constructor.
     * @property {module:model/Training}
     */
    Training,

    /**
     * The Trainings model constructor.
     * @property {module:model/Trainings}
     */
    Trainings,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};

```

### File: web\src\repositories\clients\users\src\index.js
```js
/**
 * Wild Workouts users
 * TODO
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Error from './model/Error';
import User from './model/User';
import DefaultApi from './api/DefaultApi';


/**
* TODO.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var WildWorkoutsUsers = require('index'); // See note below*.
* var xxxSvc = new WildWorkoutsUsers.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new WildWorkoutsUsers.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new WildWorkoutsUsers.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new WildWorkoutsUsers.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The User model constructor.
     * @property {module:model/User}
     */
    User,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};

```

### File: cloudbuild.yaml
```yaml
steps:
- id: common-lint
  name: golang
  entrypoint: ./scripts/lint.sh
  args: ['common', '-install']
- id: trainer-lint
  name: golang
  entrypoint: ./scripts/lint.sh
  args: ['trainer', '-install']
- id: trainings-lint
  name: golang
  entrypoint: ./scripts/lint.sh
  args: ['trainings', '-install']
- id: users-lint
  name: golang
  entrypoint: ./scripts/lint.sh
  args: ['users', '-install']

- id: trainer-docker
  name: gcr.io/cloud-builders/docker
  entrypoint: ./scripts/build-docker.sh
  args: ["trainer", "$PROJECT_ID"]
  waitFor: [trainer-lint]
- id: trainings-docker
  name: gcr.io/cloud-builders/docker
  entrypoint: ./scripts/build-docker.sh
  args: ["trainings", "$PROJECT_ID"]
  waitFor: [trainings-lint]
- id: users-docker
  name: gcr.io/cloud-builders/docker
  entrypoint: ./scripts/build-docker.sh
  args: ["users", "$PROJECT_ID"]
  waitFor: [users-lint]

- id: docker-compose
  name: 'docker/compose:1.19.0'
  args: ['-f', 'docker-compose.yml', '-f', 'docker-compose.ci.yml', 'up', '-d']
  env:
    - 'PROJECT_ID=$PROJECT_ID'
  waitFor: [trainer-docker, trainings-docker, users-docker]

- id: common-tests
  name: golang
  entrypoint: ./scripts/test.sh
  args: ["common", ".test.ci.env"]
  waitFor: [docker-compose]
- id: trainer-tests
  name: golang
  entrypoint: ./scripts/test.sh
  args: ["trainer", ".test.ci.env"]
  waitFor: [docker-compose]
- id: trainings-tests
  name: golang
  entrypoint: ./scripts/test.sh
  args: ["trainings", ".test.ci.env"]
  waitFor: [docker-compose]
- id: users-tests
  name: golang
  entrypoint: ./scripts/test.sh
  args: ["users", ".test.ci.env"]
  waitFor: [docker-compose]
- id: e2e-tests
  name: golang
  entrypoint: ./scripts/test.sh
  args: ["common", ".e2e.ci.env"]
  waitFor: [trainer-tests, trainings-tests, users-tests]

- id: docker-compose-down
  name: 'docker/compose:1.19.0'
  args: ['-f', 'docker-compose.yml', '-f', 'docker-compose.ci.yml', 'down']
  env:
    - 'PROJECT_ID=$PROJECT_ID'
  waitFor: [e2e-tests]

- id: trainer-http-deploy
  name: gcr.io/cloud-builders/gcloud
  entrypoint: ./scripts/deploy.sh
  args: [trainer, http, "$PROJECT_ID"]
  waitFor: [e2e-tests]
- id: trainer-grpc-deploy
  name: gcr.io/cloud-builders/gcloud
  entrypoint: ./scripts/deploy.sh
  args: [trainer, grpc, "$PROJECT_ID"]
  waitFor: [e2e-tests]
- id: trainings-http-deploy
  name: gcr.io/cloud-builders/gcloud
  entrypoint: ./scripts/deploy.sh
  args: [trainings, http, "$PROJECT_ID"]
  waitFor: [e2e-tests]
- id: users-http-deploy
  name: gcr.io/cloud-builders/gcloud
  entrypoint: ./scripts/deploy.sh
  args: [users, http, "$PROJECT_ID"]
  waitFor: [e2e-tests]
- id: users-grpc-deploy
  name: gcr.io/cloud-builders/gcloud
  entrypoint: ./scripts/deploy.sh
  args: [users, grpc, "$PROJECT_ID"]
  waitFor: [e2e-tests]

- id: web-deps
  name: node:12.16.2
  entrypoint: yarn
  args: [install]
  dir: web
  waitFor: ['-']
- id: openapi-js
  name: openapitools/openapi-generator-cli:v4.3.0
  entrypoint: "./scripts/openapi-js.sh"
  waitFor: ['-']
- id: web-build
  name: node:12.16.2
  entrypoint: yarn
  args: [build]
  dir: web
  waitFor: [web-deps, openapi-js]
- name: gcr.io/$PROJECT_ID/firebase
  args: ['deploy', '--project=$PROJECT_ID']
  dir: web
  waitFor: [web-build]

options:
  env:
  - 'GO111MODULE=on'
  machineType: 'N1_HIGHCPU_8'

images:
- 'gcr.io/$PROJECT_ID/trainer'
- 'gcr.io/$PROJECT_ID/trainings'
- 'gcr.io/$PROJECT_ID/users'

```

### File: scripts\build-docker.sh
```sh
#!/bin/bash
readonly service="$1"
readonly project_id="$2"

docker build -t "gcr.io/$project_id/$service" "./internal" -f "./docker/app-prod/Dockerfile" --build-arg "SERVICE=$service"
docker push "gcr.io/$project_id/$service"

```

### File: scripts\deploy.sh
```sh
#!/bin/bash
readonly service="$1"
readonly server_to_run="$2"
readonly project_id="$3"

gcloud run deploy "$service-$server_to_run" \
    --image "gcr.io/$project_id/$service" \
    --region europe-west1 \
    --platform managed

```

### File: scripts\lint.sh
```sh
#!/bin/bash
set -e

if [ "$2" == "-install" ]; then
  curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.43.0
  go install github.com/roblaszczak/go-cleanarch@latest
fi

readonly service="$1"

cd "./internal/$service"
golangci-lint run
```

### File: scripts\openapi-http.sh
```sh
#!/bin/bash
set -e

readonly service="$1"
readonly output_dir="$2"
readonly package="$3"

go tool oapi-codegen -generate types -o "$output_dir/openapi_types.gen.go" -package "$package" "api/openapi/$service.yml"
go tool oapi-codegen -generate chi-server -o "$output_dir/openapi_api.gen.go" -package "$package" "api/openapi/$service.yml"
go tool oapi-codegen -generate types -o "internal/common/client/$service/openapi_types.gen.go" -package "$service" "api/openapi/$service.yml"
go tool oapi-codegen -generate client -o "internal/common/client/$service/openapi_client_gen.go" -package "$service" "api/openapi/$service.yml"

```

### File: scripts\openapi-js.sh
```sh
#!/bin/bash
set -e

readonly service="$1"

docker run --rm --env "JAVA_OPTS=-Dlog.level=error" -v "${PWD}:/local" \
  "openapitools/openapi-generator-cli:v4.3.0" generate \
  -i "/local/api/openapi/$service.yml" \
  -g javascript \
  -o "/local/web/src/repositories/clients/$service"

```

### File: scripts\proto.sh
```sh
#!/bin/bash
set -e

readonly service="$1"

protoc \
  --proto_path=api/protobuf "api/protobuf/$service.proto" \
  "--go_out=internal/common/genproto/$service" --go_opt=paths=source_relative \
  --go-grpc_opt=require_unimplemented_servers=false \
  "--go-grpc_out=internal/common/genproto/$service" --go-grpc_opt=paths=source_relative
```

### File: scripts\test.sh
```sh
#!/bin/bash
set -e

readonly service="$1"
readonly env_file="$2"

cd "./internal/$service"
env $(cat "../../.env" "../../$env_file" | grep -Ev '^#' | xargs) go test -count=1 -p=8 -parallel=8 -race ./...

```

### File: terraform\set-envs.sh
```sh
#!/bin/bash
readonly env_prefix=TF_VAR_
readonly example_file=.env.example
readonly target_file=.env
readonly default_region=europe-west1
readonly default_firebase_location=europe-west

answer=""

function ask() {
    local var="$1"
    local example="$2"
    local current="$3"

    local name=${var/$env_prefix/}

    if [ -n "$current" ]; then
        hint="current: $current"
    else
        hint="example: $example"
    fi

    answer=""

    while [ -z "$answer" ]; do
        echo -ne "\t$name [$hint]: " 
        read -r answer </dev/tty

        if [ -z "$answer" ] && [ -n "$current" ]; then
            answer="$current"
            break
        fi
    done
}

if [ -f "$target_file" ]; then
    source "$target_file"
fi

if [ -z "$TF_VAR_user" ]; then
    readonly current_user=$(gcloud auth list --filter="status:ACTIVE" --format="value(account)")

    echo "Active gcloud account: $current_user"
    echo
    echo "Hit Enter if you want to continue with this account."
    echo "Otherwise, cancel with Ctrl+C and login with:"
    echo -e "\tgcloud auth login"
    echo
    echo "Or set active account with:"
    echo -e "\tgcloud config set account 'ACCOUNT'"
    echo
    echo "Remember to add application-default credentials with:"
    echo -e "\tgcloud auth application-default login"

    read

    TF_VAR_user="$current_user"
fi

if [ -z "$TF_VAR_billing_account" ]; then
    readonly current_billing_account=$(gcloud beta billing accounts list --filter="open=true" --format="value(displayName)" --limit 1)

    echo "Found billing account: $current_billing_account"
    TF_VAR_billing_account="$current_billing_account"
fi

if [ -z "$TF_VAR_region" ]; then
    TF_VAR_region="$default_region"
fi

if [ -z "$TF_VAR_firebase_location" ]; then
    TF_VAR_firebase_location="$default_firebase_location"
fi

echo
echo "You need to pick a region where Cloud Run is available!"
echo "See full list of supported regions: https://cloud.google.com/run/docs/locations"
echo "See available Firebase locations here: https://firebase.google.com/docs/projects/locations"
echo

echo "Fill all required parameters:"

new_content=""

while IFS= read -r line; do
    var=$(echo "$line" | cut -d= -f1)
    example=$(echo "$line" | cut -d= -f2)
    current="${!var}"

    ask "$var" "$example" "$current"

    new_content+="export $var=\"$answer\"\n"
done < <(cut -d' ' -f2 "$example_file")

echo
echo "Saving to $target_file:"
echo -en "$new_content" | tee "$target_file"

```

### File: web\babel.config.js
```js
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ]
}

```

### File: web\firebase.json
```json
{
  "hosting": {
    "public": "dist",
    "ignore": [
      "__/**",
      "**/.*"
    ],
    "rewrites": [
      {
        "source": "/api/trainer{,/**}",
        "run": {
          "serviceId": "trainer-http",
          "region": "europe-west1"
        }
      },
      {
        "source": "/api/trainings{,/**}",
        "run": {
          "serviceId": "trainings-http",
          "region": "europe-west1"
        }
      },
      {
        "source": "/api/users{,/**}",
        "run": {
          "serviceId": "users-http",
          "region": "europe-west1"
        }
      },
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}

```

### File: web\vue.config.js
```js
module.exports = {
    runtimeCompiler: true,
    devServer: {
        progress: false
    }
}
```

### File: web\webpack.config.js
```js
module.exports = {
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    'sass-loader'
                ]
            }
        ]
    },
}
```

### File: docker\app\entrypoint.sh
```sh
#!/bin/bash
sed -i "s|\$SERVICE|$SERVICE|g" /reflex.conf
reflex -c /reflex.conf

```

### File: docker\app\start.sh
```sh
cd $SERVICE && go run .

```

### File: docker\web\start.sh
```sh
set -ex

yarn install
yarn serve
```

### File: internal\users\firestore.go
```go
package main

import (
	"context"
	"errors"

	"cloud.google.com/go/firestore"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

type UserModel struct {
	Balance     int
	DisplayName string
	Role        string
	LastIP      string
}

type db struct {
	firestoreClient *firestore.Client
}

func (d db) usersCollection() *firestore.CollectionRef {
	return d.firestoreClient.Collection("users")
}

func (d db) UserDocumentRef(userID string) *firestore.DocumentRef {
	return d.usersCollection().Doc(userID)
}

func (d db) GetUser(ctx context.Context, userID string) (UserModel, error) {
	doc, err := d.UserDocumentRef(userID).Get(ctx)

	if err != nil && status.Code(err) != codes.NotFound {
		return UserModel{}, err
	}
	if err != nil && status.Code(err) == codes.NotFound {
		return UserModel{
			Balance: 0,
		}, nil
	}

	var user UserModel
	err = doc.DataTo(&user)
	if err != nil {
		return UserModel{}, err
	}

	return user, nil
}

func (d db) UpdateBalance(ctx context.Context, userID string, amountChange int) error {
	return d.firestoreClient.RunTransaction(ctx, func(ctx context.Context, tx *firestore.Transaction) error {
		var user UserModel

		userDoc, err := tx.Get(d.UserDocumentRef(userID))
		if err != nil && status.Code(err) != codes.NotFound {
			return err
		}
		if err != nil && status.Code(err) == codes.NotFound {
			user = UserModel{
				Balance: 0,
			}
		} else {
			if err := userDoc.DataTo(&user); err != nil {
				return err
			}
		}

		user.Balance += amountChange
		if user.Balance < 0 {
			return errors.New("balance cannot be smaller than 0")
		}

		return tx.Set(userDoc.Ref, user)
	})
}

const lastIPField = "LastIP"

func (d db) UpdateLastIP(ctx context.Context, userID string, lastIP string) error {
	updates := []firestore.Update{
		{
			Path:  lastIPField,
			Value: lastIP,
		},
	}

	docRef := d.UserDocumentRef(userID)

	_, err := docRef.Update(ctx, updates)
	userNotExist := status.Code(err) == codes.NotFound

	if userNotExist {
		_, err := docRef.Set(ctx, map[string]string{lastIPField: lastIP})
		return err
	}

	return err
}

```

### File: internal\users\fixtures.go
```go
package main

import (
	"context"
	"os"
	"strconv"
	"time"

	firebase "firebase.google.com/go/v4"
	"firebase.google.com/go/v4/auth"
	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/client"
	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/genproto/users"
	"github.com/pkg/errors"
	"github.com/sirupsen/logrus"
	"google.golang.org/api/option"
)

func loadFixtures() {
	start := time.Now()
	logrus.Debug("Waiting for users service")

	working := client.WaitForUsersService(time.Minute * 30)
	if !working {
		logrus.Error("Users gRPC service is not up")
		return
	}

	logrus.WithField("after", time.Since(start)).Debug("Users service is available")

	var attendeeUUIDs []string
	var err error
	if mockAuth, _ := strconv.ParseBool(os.Getenv("MOCK_AUTH")); !mockAuth {
		for {
			attendeeUUIDs, err = createFirebaseUsers()
			if err == nil {
				logrus.Debug("Firestore users created")
				break
			}

			logrus.WithError(err).Warn("Unable to create Firestore user")
			time.Sleep(10 * time.Second)
		}
	} else {
		// ugly copy from web/src/repositories/user.js
		attendeeUUIDs = []string{"2"}
	}

	for {
		err = setAttendeeTrainingsAmount(attendeeUUIDs)
		if err == nil {
			break
		}

		logrus.WithError(err).Warn("Unable to set users credits")
		time.Sleep(10 * time.Second)
	}

	logrus.WithField("after", time.Since(start)).Debug("Users fixtures loaded")
}

func createFirebaseUsers() ([]string, error) {
	var attendeeUUIDs []string

	var opts []option.ClientOption
	if file := os.Getenv("SERVICE_ACCOUNT_FILE"); file != "" {
		opts = append(opts, option.WithCredentialsFile(file))
	}

	config := &firebase.Config{ProjectID: os.Getenv("GCP_PROJECT")}
	firebaseApp, err := firebase.NewApp(context.Background(), config, opts...)
	if err != nil {
		return nil, err
	}

	authClient, err := firebaseApp.Auth(context.Background())
	if err != nil {
		return nil, err
	}

	usersToCreate := []struct {
		Email       string
		DisplayName string
		Role        string
	}{
		{

			Email:       "trainer@threedots.tech",
			DisplayName: "Trainer",
			Role:        "trainer",
		},
		{
			Email:       "attendee@threedots.tech",
			DisplayName: "Mariusz Pudzianowski",
			Role:        "attendee",
		},
		{
			Email:       "attendee2@threedots.tech",
			DisplayName: "Arnold Schwarzenegger",
			Role:        "attendee",
		},
	}

	for _, user := range usersToCreate {
		userToCreate := (&auth.UserToCreate{}).
			Email(user.Email).
			Password("123456").
			DisplayName(user.DisplayName)

		createdUser, err := authClient.CreateUser(context.Background(), userToCreate)
		if err != nil && auth.IsEmailAlreadyExists(err) {
			existingUser, err := authClient.GetUserByEmail(context.Background(), user.Email)
			if err != nil {
				return nil, errors.Wrap(err, "unable to get created user")
			}
			if user.Role == "attendee" {
				attendeeUUIDs = append(attendeeUUIDs, existingUser.UID)
			}
			continue
		}
		if err != nil {
			return nil, err
		}

		err = authClient.SetCustomUserClaims(context.Background(), createdUser.UID, map[string]interface{}{
			"role": user.Role,
		})
		if err != nil {
			return nil, err
		}

		if user.Role == "attendee" {
			attendeeUUIDs = append(attendeeUUIDs, createdUser.UID)
		}
	}

	return attendeeUUIDs, nil
}

func setAttendeeTrainingsAmount(attendeeUUIDs []string) error {
	usersClient, usersClose, err := client.NewUsersClient()
	if err != nil {
		logrus.WithError(err).Error("Unable to set trainings amount")
	}
	defer func() {
		_ = usersClose()
	}()

	for _, attendeeUUID := range attendeeUUIDs {
		resp, err := usersClient.GetTrainingBalance(context.Background(), &users.GetTrainingBalanceRequest{
			UserId: attendeeUUID,
		})
		if err != nil {
			return err
		}

		if resp.Amount > 0 {
			logrus.WithFields(logrus.Fields{
				"attendee_uuid": attendeeUUID,
				"credits":       resp.Amount,
			}).Debug("Attendee have credits already")
			continue
		}

		_, err = usersClient.UpdateTrainingBalance(context.Background(), &users.UpdateTrainingBalanceRequest{
			UserId:       attendeeUUID,
			AmountChange: 20,
		})
		if err != nil {
			return err
		}

		logrus.WithField("attendee_uuid", attendeeUUID).Debug("Credits set to attendee")
	}

	return nil
}

```

### File: internal\users\grpc.go
```go
package main

import (
	"context"
	"fmt"

	"github.com/golang/protobuf/ptypes/empty"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/genproto/users"
)

type GrpcServer struct {
	db db
}

func (g GrpcServer) GetTrainingBalance(ctx context.Context, request *users.GetTrainingBalanceRequest) (*users.GetTrainingBalanceResponse, error) {
	user, err := g.db.GetUser(ctx, request.UserId)
	if err != nil {
		return nil, status.Error(codes.Internal, err.Error())
	}

	return &users.GetTrainingBalanceResponse{Amount: int64(user.Balance)}, nil
}

func (g GrpcServer) UpdateTrainingBalance(
	ctx context.Context,
	req *users.UpdateTrainingBalanceRequest,
) (*empty.Empty, error) {
	err := g.db.UpdateBalance(ctx, req.UserId, int(req.AmountChange))
	if err != nil {
		return nil, status.Error(codes.Internal, fmt.Sprintf("failed to update balance: %s", err))
	}

	return &empty.Empty{}, nil
}

```

### File: internal\users\http.go
```go
package main

import (
	"net"
	"net/http"

	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/auth"
	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/server/httperr"
	"github.com/go-chi/render"
)

type HttpServer struct {
	db db
}

func (h HttpServer) GetCurrentUser(w http.ResponseWriter, r *http.Request) {
	authUser, err := auth.UserFromCtx(r.Context())
	if err != nil {
		httperr.RespondWithSlugError(err, w, r)
		return
	}

	host, _, err := net.SplitHostPort(r.RemoteAddr)
	if err == nil {
		err = h.db.UpdateLastIP(r.Context(), authUser.UUID, host)
		if err != nil {
			httperr.InternalError("internal-server-error", err, w, r)
			return
		}
	}

	user, err := h.db.GetUser(r.Context(), authUser.UUID)
	if err != nil {
		httperr.InternalError("cannot-get-user", err, w, r)
		return
	}

	userResponse := User{
		DisplayName: authUser.DisplayName,
		Balance:     user.Balance,
		Role:        authUser.Role,
	}

	render.Respond(w, r, userResponse)
}

```

### File: internal\users\main.go
```go
package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	"strings"

	"cloud.google.com/go/firestore"
	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/genproto/users"
	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/logs"
	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/server"
	"github.com/go-chi/chi/v5"
	"google.golang.org/grpc"
)

func main() {
	logs.Init()

	ctx := context.Background()
	firestoreClient, err := firestore.NewClient(ctx, os.Getenv("GCP_PROJECT"))
	if err != nil {
		panic(err)
	}
	firebaseDB := db{firestoreClient}

	serverType := strings.ToLower(os.Getenv("SERVER_TO_RUN"))
	switch serverType {
	case "http":
		go loadFixtures()

		server.RunHTTPServer(func(router chi.Router) http.Handler {
			return HandlerFromMux(HttpServer{firebaseDB}, router)
		})
	case "grpc":
		server.RunGRPCServer(func(server *grpc.Server) {
			svc := GrpcServer{firebaseDB}
			users.RegisterUsersServiceServer(server, svc)
		})
	default:
		panic(fmt.Sprintf("server type '%s' is not supported", serverType))
	}
}

```

### File: internal\users\openapi_api.gen.go
```go
// Package main provides primitives to interact with the openapi HTTP API.
//
// Code generated by github.com/deepmap/oapi-codegen version v1.16.2 DO NOT EDIT.
package main

import (
	"context"
	"fmt"
	"net/http"

	"github.com/go-chi/chi/v5"
)

// ServerInterface represents all server handlers.
type ServerInterface interface {

	// (GET /users/current)
	GetCurrentUser(w http.ResponseWriter, r *http.Request)
}

// Unimplemented server implementation that returns http.StatusNotImplemented for each endpoint.

type Unimplemented struct{}

// (GET /users/current)
func (_ Unimplemented) GetCurrentUser(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusNotImplemented)
}

// ServerInterfaceWrapper converts contexts to parameters.
type ServerInterfaceWrapper struct {
	Handler            ServerInterface
	HandlerMiddlewares []MiddlewareFunc
	ErrorHandlerFunc   func(w http.ResponseWriter, r *http.Request, err error)
}

type MiddlewareFunc func(http.Handler) http.Handler

// GetCurrentUser operation middleware
func (siw *ServerInterfaceWrapper) GetCurrentUser(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()

	ctx = context.WithValue(ctx, BearerAuthScopes, []string{})

	handler := http.Handler(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		siw.Handler.GetCurrentUser(w, r)
	}))

	for _, middleware := range siw.HandlerMiddlewares {
		handler = middleware(handler)
	}

	handler.ServeHTTP(w, r.WithContext(ctx))
}

type UnescapedCookieParamError struct {
	ParamName string
	Err       error
}

func (e *UnescapedCookieParamError) Error() string {
	return fmt.Sprintf("error unescaping cookie parameter '%s'", e.ParamName)
}

func (e *UnescapedCookieParamError) Unwrap() error {
	return e.Err
}

type UnmarshalingParamError struct {
	ParamName string
	Err       error
}

func (e *UnmarshalingParamError) Error() string {
	return fmt.Sprintf("Error unmarshaling parameter %s as JSON: %s", e.ParamName, e.Err.Error())
}

func (e *UnmarshalingParamError) Unwrap() error {
	return e.Err
}

type RequiredParamError struct {
	ParamName string
}

func (e *RequiredParamError) Error() string {
	return fmt.Sprintf("Query argument %s is required, but not found", e.ParamName)
}

type RequiredHeaderError struct {
	ParamName string
	Err       error
}

func (e *RequiredHeaderError) Error() string {
	return fmt.Sprintf("Header parameter %s is required, but not found", e.ParamName)
}

func (e *RequiredHeaderError) Unwrap() error {
	return e.Err
}

type InvalidParamFormatError struct {
	ParamName string
	Err       error
}

func (e *InvalidParamFormatError) Error() string {
	return fmt.Sprintf("Invalid format for parameter %s: %s", e.ParamName, e.Err.Error())
}

func (e *InvalidParamFormatError) Unwrap() error {
	return e.Err
}

type TooManyValuesForParamError struct {
	ParamName string
	Count     int
}

func (e *TooManyValuesForParamError) Error() string {
	return fmt.Sprintf("Expected one value for %s, got %d", e.ParamName, e.Count)
}

// Handler creates http.Handler with routing matching OpenAPI spec.
func Handler(si ServerInterface) http.Handler {
	return HandlerWithOptions(si, ChiServerOptions{})
}

type ChiServerOptions struct {
	BaseURL          string
	BaseRouter       chi.Router
	Middlewares      []MiddlewareFunc
	ErrorHandlerFunc func(w http.ResponseWriter, r *http.Request, err error)
}

// HandlerFromMux creates http.Handler with routing matching OpenAPI spec based on the provided mux.
func HandlerFromMux(si ServerInterface, r chi.Router) http.Handler {
	return HandlerWithOptions(si, ChiServerOptions{
		BaseRouter: r,
	})
}

func HandlerFromMuxWithBaseURL(si ServerInterface, r chi.Router, baseURL string) http.Handler {
	return HandlerWithOptions(si, ChiServerOptions{
		BaseURL:    baseURL,
		BaseRouter: r,
	})
}

// HandlerWithOptions creates http.Handler with additional options
func HandlerWithOptions(si ServerInterface, options ChiServerOptions) http.Handler {
	r := options.BaseRouter

	if r == nil {
		r = chi.NewRouter()
	}
	if options.ErrorHandlerFunc == nil {
		options.ErrorHandlerFunc = func(w http.ResponseWriter, r *http.Request, err error) {
			http.Error(w, err.Error(), http.StatusBadRequest)
		}
	}
	wrapper := ServerInterfaceWrapper{
		Handler:            si,
		HandlerMiddlewares: options.Middlewares,
		ErrorHandlerFunc:   options.ErrorHandlerFunc,
	}

	r.Group(func(r chi.Router) {
		r.Get(options.BaseURL+"/users/current", wrapper.GetCurrentUser)
	})

	return r
}

```

### File: internal\users\openapi_types.gen.go
```go
// Package main provides primitives to interact with the openapi HTTP API.
//
// Code generated by github.com/deepmap/oapi-codegen version v1.16.2 DO NOT EDIT.
package main

const (
	BearerAuthScopes = "bearerAuth.Scopes"
)

// User defines model for User.
type User struct {
	Balance     int    `json:"balance"`
	DisplayName string `json:"displayName"`
	Role        string `json:"role"`
}

```

### File: web\public\index.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title>Wilds Workouts</title>
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app">
      <router-view></router-view>
    </div>
    <!-- built files will be auto injected -->
  </body>
</html>

```

### File: web\src\date.js
```js
export function formatDate(d) {
    return d.getFullYear().toString() + "-" + ((d.getMonth() + 1).toString().length == 2 ? (d.getMonth() + 1).toString() : "0" + (d.getMonth() + 1).toString()) + "-" + (d.getDate().toString().length == 2 ? d.getDate().toString() : "0" + d.getDate().toString());
}

export function formatHour(d) {
    return (d.getHours().toString().length == 2 ? d.getHours().toString() : "0" + d.getHours().toString()) + ":" + ((parseInt(d.getMinutes() / 5) * 5).toString().length == 2 ? (parseInt(d.getMinutes() / 5) * 5).toString() : "0" + (parseInt(d.getMinutes() / 5) * 5).toString());
}

export function formatDateTime(d) {
    return formatDate(d) + " " + formatHour(d)
}


```

### File: web\src\firebase.js
```js
import firebase from "firebase";

export function loadFirebaseConfig() {
    // from https://firebase.google.com/docs/hosting/reserved-urls?authuser=2
    // in dev env, web/public/__/firebase/init.json will be loaded
    return fetch('/__/firebase/init.json').then(async response => {
        firebase.initializeApp(await response.json());
    })
}

```

### File: web\src\main.js
```js
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import './assets/main.css'

import Vue from 'vue'

import VueRouter from 'vue-router'
import VueDialog from "vuejs-dialog"
import 'vuejs-dialog/dist/vuejs-dialog.min.css';
import VueToast from 'vue-toast-notification'
import 'vue-toast-notification/dist/theme-sugar.css'
import TrainingsList from './pages/TrainingsList'
import Calendar from './pages/Calendar'
import ScheduleTraining from './pages/ScheduleTraining'
import Login from './pages/Login'
import SetSchedule from './pages/SetSchedule'
import {loadFirebaseConfig} from "./firebase";
import {Auth, setApiClientsAuth} from "./repositories/auth";

Vue.use(VueRouter)

Vue.use(VueDialog, {
    html: true,
    loader: false,
    okText: 'Proceed',
    cancelText: 'Cancel',
    animation: 'fade'
})

Vue.use(VueToast, {
    position: 'top-right',
    duration: 5000,
})

Vue.config.productionTip = false


const routes = [
    {
        path: '/',
        redirect: 'login'
    },
    {
        path: '/login',
        component: Login,
        name: 'login',
    },
    {
        path: '/trainings',
        component: TrainingsList,
        name: 'trainingsList',
    },
    {
        path: '/calendar',
        component: Calendar,
        name: 'calendar',

    },
    {
        path: '/trainings/schedule',
        component: ScheduleTraining,
        name: 'scheduleTraining',
    },
    {
        path: '/trainings/reschedule/:trainingID',
        component: ScheduleTraining,
        name: 'rescheduleTraining',
    },
    {
        path: '/trainings/propose-new-date/:trainingID',
        component: ScheduleTraining,
        name: 'proposeNewDate',
        props: {isPropose: true},
    },
    {
        path: '/trainer/set-schedule',
        component: SetSchedule,
        name: 'setSchedule',
    },
]

const router = new VueRouter({
    routes,
    mode: 'history',
})

const app = new Vue({
    router,
})


loadFirebaseConfig()
    .then(function () {
        return Auth.waitForAuthReady()
    })
    .then(function () {
        return Auth.getJwtToken(false)
    })
    .then(token => {
        setApiClientsAuth(token)
    })
    .finally(function () {
        app.$mount('#app')
    })


```

### File: internal\common\auth\http.go
```go
package auth

import (
	"context"
	"net/http"
	"strings"

	"firebase.google.com/go/v4/auth"
	commonerrors "github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/errors"
	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/server/httperr"
)

type FirebaseHttpMiddleware struct {
	AuthClient *auth.Client
}

func (a FirebaseHttpMiddleware) Middleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		ctx := r.Context()

		bearerToken := a.tokenFromHeader(r)
		if bearerToken == "" {
			httperr.Unauthorised("empty-bearer-token", nil, w, r)
			return
		}

		token, err := a.AuthClient.VerifyIDToken(ctx, bearerToken)
		if err != nil {
			httperr.Unauthorised("unable-to-verify-jwt", err, w, r)
			return
		}

		// it's always a good idea to use custom type as context value (in this case ctxKey)
		// because nobody from the outside of the package will be able to override/read this value
		ctx = context.WithValue(ctx, userContextKey, User{
			UUID:        token.UID,
			Email:       token.Claims["email"].(string),
			Role:        token.Claims["role"].(string),
			DisplayName: token.Claims["name"].(string),
		})
		r = r.WithContext(ctx)

		next.ServeHTTP(w, r)
	})
}

func (a FirebaseHttpMiddleware) tokenFromHeader(r *http.Request) string {
	headerValue := r.Header.Get("Authorization")

	if len(headerValue) > 7 && strings.ToLower(headerValue[0:6]) == "bearer" {
		return headerValue[7:]
	}

	return ""
}

type User struct {
	UUID  string
	Email string
	Role  string

	DisplayName string
}

type ctxKey int

const (
	userContextKey ctxKey = iota
)

var (
	// if we expect that the user of the function may be interested with concrete error,
	// it's a good idea to provide variable with this error
	NoUserInContextError = commonerrors.NewAuthorizationError("no user in context", "no-user-found")
)

func UserFromCtx(ctx context.Context) (User, error) {
	u, ok := ctx.Value(userContextKey).(User)
	if ok {
		return u, nil
	}

	return User{}, NoUserInContextError
}

```

### File: internal\common\auth\http_mock.go
```go
package auth

import (
	"context"
	"net/http"

	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/server/httperr"
	"github.com/dgrijalva/jwt-go"
	"github.com/dgrijalva/jwt-go/request"
)

// HttpMockMiddleware is used in the local environment (which doesn't depend on Firebase)
func HttpMockMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		var claims jwt.MapClaims
		token, err := request.ParseFromRequest(
			r,
			request.AuthorizationHeaderExtractor,
			func(token *jwt.Token) (i interface{}, e error) {
				return []byte("mock_secret"), nil
			},
			request.WithClaims(&claims),
		)
		if err != nil {
			httperr.BadRequest("unable-to-get-jwt", err, w, r)
			return
		}

		if !token.Valid {
			httperr.BadRequest("invalid-jwt", nil, w, r)
			return
		}

		ctx := context.WithValue(r.Context(), userContextKey, User{
			UUID:        claims["user_uuid"].(string),
			Email:       claims["email"].(string),
			Role:        claims["role"].(string),
			DisplayName: claims["name"].(string),
		})
		r = r.WithContext(ctx)

		next.ServeHTTP(w, r)
	})
}

```

### File: internal\common\client\auth.go
```go
package client

import (
	"context"
	"fmt"
	"strings"

	"cloud.google.com/go/compute/metadata"
	"github.com/pkg/errors"
	"google.golang.org/grpc/credentials"
)

type metadataServerToken struct {
	serviceURL string
}

func newMetadataServerToken(grpcAddr string) credentials.PerRPCCredentials {
	// based on https://cloud.google.com/run/docs/authenticating/service-to-service#go
	// service need to have https prefix without port
	serviceURL := "https://" + strings.Split(grpcAddr, ":")[0]

	return metadataServerToken{serviceURL}
}

// GetRequestMetadata is called on every request, so we are sure that token is always not expired
func (t metadataServerToken) GetRequestMetadata(ctx context.Context, in ...string) (map[string]string, error) {
	// based on https://cloud.google.com/run/docs/authenticating/service-to-service#go
	tokenURL := fmt.Sprintf("/instance/service-accounts/default/identity?audience=%s", t.serviceURL)
	idToken, err := metadata.Get(tokenURL)
	if err != nil {
		return nil, errors.Wrap(err, "cannot query id token for gRPC")
	}

	return map[string]string{
		"authorization": "Bearer " + idToken,
	}, nil
}

func (metadataServerToken) RequireTransportSecurity() bool {
	return true
}

```

### File: internal\common\client\grpc.go
```go
package client

import (
	"crypto/tls"
	"crypto/x509"
	"os"
	"strconv"
	"time"

	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/genproto/trainer"
	"github.com/ThreeDotsLabs/wild-workouts-go-ddd-example/internal/common/genproto/users"
	"github.com/pkg/errors"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

func NewTrainerClient() (client trainer.TrainerServiceClient, close func() error, err error) {
	grpcAddr := os.Getenv("TRAINER_GRPC_ADDR")
	if grpcAddr == "" {
		return nil, func() error { return nil }, errors.New("empty env TRAINER_GRPC_ADDR")
	}

	opts, err := grpcDialOpts(grpcAddr)
	if err != nil {
		return nil, func() error { return nil }, err
	}

	conn, err := grpc.Dial(grpcAddr, opts...)
	if err != nil {
		return nil, func() error { return nil }, err
	}

	return trainer.NewTrainerServiceClient(conn), conn.Close, nil
}

func WaitForTrainerService(timeout time.Duration) bool {
	return waitForPort(os.Getenv("TRAINER_GRPC_ADDR"), timeout)
}

func NewUsersClient() (client users.UsersServiceClient, close func() error, err error) {
	grpcAddr := os.Getenv("USERS_GRPC_ADDR")
	if grpcAddr == "" {
		return nil, func() error { return nil }, errors.New("empty env USERS_GRPC_ADDR")
	}

	opts, err := grpcDialOpts(grpcAddr)
	if err != nil {
		return nil, func() error { return nil }, err
	}

	conn, err := grpc.Dial(grpcAddr, opts...)
	if err != nil {
		return nil, func() error { return nil }, err
	}

	return users.NewUsersServiceClient(conn), conn.Close, nil
}

func WaitForUsersService(timeout time.Duration) bool {
	return waitForPort(os.Getenv("USERS_GRPC_ADDR"), timeout)
}

func grpcDialOpts(grpcAddr string) ([]grpc.DialOption, error) {
	if noTLS, _ := strconv.ParseBool(os.Getenv("GRPC_NO_TLS")); noTLS {
		return []grpc.DialOption{grpc.WithInsecure()}, nil
	}

	systemRoots, err := x509.SystemCertPool()
	if err != nil {
		return nil, errors.Wrap(err, "cannot load root CA cert")
	}
	creds := credentials.NewTLS(&tls.Config{
		RootCAs:    systemRoots,
		MinVersion: tls.VersionTLS12,
	})

	return []grpc.DialOption{
		grpc.WithTransportCredentials(creds),
		grpc.WithPerRPCCredentials(newMetadataServerToken(grpcAddr)),
	}, nil
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
