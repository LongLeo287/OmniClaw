---
id: github.com-victorsteven-food-app-server-1ebfdf87-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:40.330223
---

# KNOWLEDGE EXTRACT: github.com_victorsteven_food-app-server_1ebfdf87
> **Extracted on:** 2026-04-01 15:22:48
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524478/github.com_victorsteven_food-app-server_1ebfdf87

---

## File: `.env`
```
#Postgres
APP_ENV=local
API_PORT=8888
DB_HOST=127.0.0.1
DB_DRIVER=postgres
ACCESS_SECRET=98hbun98h
REFRESH_SECRET=786dfdbjhsb
DB_USER=steven
DB_PASSWORD=password
DB_NAME=food-app
DB_PORT=5432

#Mysql
#DB_HOST=127.0.0.1
#DB_DRIVER=mysql
#DB_USER=steven
#DB_PASSWORD=here
#DB_NAME=food-app
#DB_PORT=3306


#Postgres Test DB
TEST_DB_DRIVER=postgres
TEST_DB_HOST=127.0.0.1
TEST_DB_PASSWORD=password
TEST_DB_USER=steven
TEST_DB_NAME=food-app-test
TEST_DB_PORT=5432

#Redis
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_PASSWORD=


#DO_SPACES_KEY=your-space-key
#DO_SPACES_SECRET=secret
#DO_SPACES_TOKEN=token
#DO_SPACES_ENDPOINT=url
#DO_SPACES_REGION=region
#DO_SPACES_URL=photo_url







```

## File: `.gitignore`
```
.idea
```

## File: `README.md`
```markdown
[![CircleCI](https://circleci.com/gh/victorsteven/food-app-server.svg?style=svg)](https://circleci.com/gh/victorsteven/food-app-server)

An article was written about this project [here](https://dev.to/stevensunflash/using-domain-driven-design-ddd-in-golang-3ee5)

A Frontend was also built with Javascript(VueJS) and deployed to netlify. This is the [url](https://food-app-ddd.netlify.com)

Get frontend github repository [here](https://github.com/victorsteven/food-app-client)
```

## File: `go.mod`
```
module food-app

go 1.13

require (
	github.com/aws/aws-sdk-go v1.29.30
	github.com/badoux/checkmail v0.0.0-20181210160741-9661bd69e9ad
	github.com/dgrijalva/jwt-go v3.2.0+incompatible
	github.com/gin-gonic/gin v1.5.0
	github.com/go-redis/redis/v7 v7.0.0-beta.6
	github.com/jinzhu/gorm v1.9.12
	github.com/joho/godotenv v1.3.0
	github.com/minio/minio-go/v6 v6.0.50
	github.com/myesui/uuid v1.0.0 // indirect
	github.com/stretchr/testify v1.4.0
	github.com/twinj/uuid v1.0.0
	golang.org/x/crypto v0.0.0-20191205180655-e7c4368fe9dd
	gopkg.in/stretchr/testify.v1 v1.2.2 // indirect
)
```

## File: `go.sum`
```
github.com/aws/aws-sdk-go v1.29.30 h1:HEEb7p5H850+hKVLRif2fWpaoJe5ZkZ5WUJwJ+CKWV4=
github.com/aws/aws-sdk-go v1.29.30/go.mod h1:1KvfttTE3SPKMpo8g2c6jL3ZKfXtFvKscTgahTma5Xg=
github.com/badoux/checkmail v0.0.0-20181210160741-9661bd69e9ad h1:kXfVkP8xPSJXzicomzjECcw6tv1Wl9h1lNenWBfNKdg=
github.com/badoux/checkmail v0.0.0-20181210160741-9661bd69e9ad/go.mod h1:r5ZalvRl3tXevRNJkwIB6DC4DD3DMjIlY9NEU1XGoaQ=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/denisenkom/go-mssqldb v0.0.0-20191124224453-732737034ffd h1:83Wprp6ROGeiHFAP8WJdI2RoxALQYgdllERc3N5N2DM=
github.com/denisenkom/go-mssqldb v0.0.0-20191124224453-732737034ffd/go.mod h1:xbL0rPBG9cCiLr28tMa8zpbdarY27NDyej4t/EjAShU=
github.com/dgrijalva/jwt-go v3.2.0+incompatible h1:7qlOGliEKZXTDg6OTjfoBKDXWrumCAMpl/TFQ4/5kLM=
github.com/dgrijalva/jwt-go v3.2.0+incompatible/go.mod h1:E3ru+11k8xSBh+hMPgOLZmtrrCbhqsmaPHjLKYnJCaQ=
github.com/dustin/go-humanize v1.0.0/go.mod h1:HtrtbFcZ19U5GC7JDqmcUSB87Iq5E25KnS6fMYU6eOk=
github.com/erikstmartin/go-testdb v0.0.0-20160219214506-8d10e4a1bae5 h1:Yzb9+7DPaBjB8zlTR87/ElzFsnQfuHnVUVqpZZIcV5Y=
github.com/erikstmartin/go-testdb v0.0.0-20160219214506-8d10e4a1bae5/go.mod h1:a2zkGnVExMxdzMo3M0Hi/3sEU+cWnZpSni0O6/Yb/P0=
github.com/fsnotify/fsnotify v1.4.7 h1:IXs+QLmnXW2CcXuY+8Mzv/fWEsPGWxqefPtCP5CnV9I=
github.com/fsnotify/fsnotify v1.4.7/go.mod h1:jwhsz4b93w/PPRr/qN1Yymfu8t87LnFCMoQvtojpjFo=
github.com/gin-contrib/sse v0.1.0 h1:Y/yl/+YNO8GZSjAhjMsSuLt29uWRFHdHYUb5lYOV9qE=
github.com/gin-contrib/sse v0.1.0/go.mod h1:RHrZQHXnP2xjPF+u1gW/2HnVO7nvIa9PG3Gm+fLHvGI=
github.com/gin-gonic/gin v1.5.0 h1:fi+bqFAx/oLK54somfCtEZs9HeH1LHVoEPUgARpTqyc=
github.com/gin-gonic/gin v1.5.0/go.mod h1:Nd6IXA8m5kNZdNEHMBd93KT+mdY3+bewLgRvmCsR2Do=
github.com/go-playground/locales v0.12.1 h1:2FITxuFt/xuCNP1Acdhv62OzaCiviiE4kotfhkmOqEc=
github.com/go-playground/locales v0.12.1/go.mod h1:IUMDtCfWo/w/mtMfIE/IG2K+Ey3ygWanZIBtBW0W2TM=
github.com/go-playground/universal-translator v0.16.0 h1:X++omBR/4cE2MNg91AoC3rmGrCjJ8eAeUP/K/EKx4DM=
github.com/go-playground/universal-translator v0.16.0/go.mod h1:1AnU7NaIRDWWzGEKwgtJRd2xk99HeFyHw3yid4rvQIY=
github.com/go-redis/redis/v7 v7.0.0-beta.6 h1:ApjPvZNUF+/oVHwrTBQsVOwex5v/WapUUR4bOL2kMFA=
github.com/go-redis/redis/v7 v7.0.0-beta.6/go.mod h1:JDNMw23GTyLNC4GZu9njt15ctBQVn7xjRfnwdHj/Dcg=
github.com/go-sql-driver/mysql v1.4.1 h1:g24URVg0OFbNUTx9qqY1IRZ9D9z3iPyi5zKhQZpNwpA=
github.com/go-sql-driver/mysql v1.4.1/go.mod h1:zAC/RDZ24gD3HViQzih4MyKcchzm+sOG5ZlKdlhCg5w=
github.com/go-sql-driver/mysql v1.5.0 h1:ozyZYNQW3x3HtqT1jira07DN2PArx2v7/mN66gGcHOs=
github.com/go-sql-driver/mysql v1.5.0/go.mod h1:DCzpHaOWr8IXmIStZouvnhqoel9Qv2LBy8hT2VhHyBg=
github.com/golang-sql/civil v0.0.0-20190719163853-cb61b32ac6fe h1:lXe2qZdvpiX5WZkZR4hgp4KJVfY3nMkvmwbVkpv1rVY=
github.com/golang-sql/civil v0.0.0-20190719163853-cb61b32ac6fe/go.mod h1:8vg3r2VgvsThLBIFL93Qb5yWzgyZWhEmBwUJWevAkK0=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.2 h1:6nsPYzhq5kReh6QImI3k5qWzO4PEbvbIW2cwSfR/6xs=
github.com/golang/protobuf v1.3.2/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/google/gofuzz v1.0.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/gopherjs/gopherjs v0.0.0-20181017120253-0766667cb4d1 h1:EGx4pi6eqNxGaHF6qqu48+N2wcFQ5qg5FXgOdqsJ5d8=
github.com/gopherjs/gopherjs v0.0.0-20181017120253-0766667cb4d1/go.mod h1:wJfORRmW1u3UXTncJ5qlYoELFm8eSnnEO6hX4iZ3EWY=
github.com/hpcloud/tail v1.0.0 h1:nfCOvKYfkgYP8hkirhJocXT2+zOD8yUNjXaWfTlyFKI=
github.com/hpcloud/tail v1.0.0/go.mod h1:ab1qPbhIpdTxEkNHXyeSf5vhxWSCs/tWer42PpOxQnU=
github.com/jinzhu/gorm v1.9.12 h1:Drgk1clyWT9t9ERbzHza6Mj/8FY/CqMyVzOiHviMo6Q=
github.com/jinzhu/gorm v1.9.12/go.mod h1:vhTjlKSJUTWNtcbQtrMBFCxy7eXTzeCAzfL5fBZT/Qs=
github.com/jinzhu/inflection v1.0.0 h1:K317FqzuhWc8YvSVlFMCCUb36O/S9MCKRDI7QkRKD/E=
github.com/jinzhu/inflection v1.0.0/go.mod h1:h+uFLlag+Qp1Va5pdKtLDYj+kHp5pxUVkryuEj+Srlc=
github.com/jinzhu/now v1.0.1 h1:HjfetcXq097iXP0uoPCdnM4Efp5/9MsM0/M+XOTeR3M=
github.com/jinzhu/now v1.0.1/go.mod h1:d3SSVoowX0Lcu0IBviAWJpolVfI5UJVZZ7cO71lE/z8=
github.com/jmespath/go-jmespath v0.0.0-20180206201540-c2b33e8439af h1:pmfjZENx5imkbgOkpRUYLnmbU7UEFbjtDA2hxJ1ichM=
github.com/jmespath/go-jmespath v0.0.0-20180206201540-c2b33e8439af/go.mod h1:Nht3zPeWKUH0NzdCt2Blrr5ys8VGpn0CEB0cQHVjt7k=
github.com/joho/godotenv v1.3.0 h1:Zjp+RcGpHhGlrMbJzXTrZZPrWj+1vfm90La1wgB6Bhc=
github.com/joho/godotenv v1.3.0/go.mod h1:7hK45KPybAkOC6peb+G5yklZfMxEjkZhHbwpqxOKXbg=
github.com/json-iterator/go v1.1.7 h1:KfgG9LzI+pYjr4xvmz/5H4FXjokeP+rlHLhv3iH62Fo=
github.com/json-iterator/go v1.1.7/go.mod h1:KdQUCv79m/52Kvf8AW2vK1V8akMuk1QjK/uOdHXbAo4=
github.com/jtolds/gls v4.20.0+incompatible h1:xdiiI2gbIgH/gLH7ADydsJ1uDOEzR8yvV7C0MuV77Wo=
github.com/jtolds/gls v4.20.0+incompatible/go.mod h1:QJZ7F/aHp+rZTRtaJ1ow/lLfFfVYBRgL+9YlvaHOwJU=
github.com/konsorten/go-windows-terminal-sequences v1.0.1/go.mod h1:T0+1ngSBFLxvqU3pZ+m/2kptfBszLMUkC4ZK/EgS/cQ=
github.com/kr/pretty v0.1.0 h1:L/CwN0zerZDmRFUapSPitk6f+Q3+0za1rQkzVuMiMFI=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/leodido/go-urn v1.1.0 h1:Sm1gr51B1kKyfD2BlRcLSiEkffoG96g6TPv6eRoEiB8=
github.com/leodido/go-urn v1.1.0/go.mod h1:+cyI34gQWZcE1eQU7NVgKkkzdXDQHr1dBMtdAPozLkw=
github.com/lib/pq v1.1.1 h1:sJZmqHoEaY7f+NPP8pgLB/WxulyR3fewgCM2qaSlBb4=
github.com/lib/pq v1.1.1/go.mod h1:5WUZQaWbwv1U+lTReE5YruASi9Al49XbQIvNi/34Woo=
github.com/mattn/go-isatty v0.0.9 h1:d5US/mDsogSGW37IV293h//ZFaeajb69h+EHFsv2xGg=
github.com/mattn/go-isatty v0.0.9/go.mod h1:YNRxwqDuOph6SZLI9vUUz6OYw3QyUt7WiY2yME+cCiQ=
github.com/mattn/go-sqlite3 v2.0.1+incompatible h1:xQ15muvnzGBHpIpdrNi1DA5x0+TcBZzsIDwmw9uTHzw=
github.com/mattn/go-sqlite3 v2.0.1+incompatible/go.mod h1:FPy6KqzDD04eiIsT53CuJW3U88zkxoIYsOqkbpncsNc=
github.com/minio/minio-go/v6 v6.0.50 h1:sOUAJG2NeXRCEsZ2eGctoPwaLCwPdlPuZ0blMVrLswo=
github.com/minio/minio-go/v6 v6.0.50/go.mod h1:qD0lajrGW49lKZLtXKtCB4X/qkMf0a5tBvN2PaZg7Gg=
github.com/minio/sha256-simd v0.1.1 h1:5QHSlgo3nt5yKOJrC7W8w7X+NFl8cMPZm96iu8kKUJU=
github.com/minio/sha256-simd v0.1.1/go.mod h1:B5e1o+1/KgNmWrSQK08Y6Z1Vb5pwIktudl0J58iy0KM=
github.com/mitchellh/go-homedir v1.1.0 h1:lukF9ziXFxDFPkA1vsr5zpc1XuPDn/wFntq5mG+4E0Y=
github.com/mitchellh/go-homedir v1.1.0/go.mod h1:SfyaCUpYCn1Vlf4IUYiD9fPX4A5wJrkLzIz1N1q0pr0=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421 h1:ZqeYNhU3OHLH3mGKHDcjJRFFRrJa6eAM5H+CtDdOsPc=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/reflect2 v0.0.0-20180701023420-4b7aa43c6742 h1:Esafd1046DLDQ0W1YjYsBW+p8U2u7vzgW2SQVmlNazg=
github.com/modern-go/reflect2 v0.0.0-20180701023420-4b7aa43c6742/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/myesui/uuid v1.0.0 h1:xCBmH4l5KuvLYc5L7AS7SZg9/jKdIFubM7OVoLqaQUI=
github.com/myesui/uuid v1.0.0/go.mod h1:2CDfNgU0LR8mIdO8vdWd8i9gWWxLlcoIGGpSNgafq84=
github.com/onsi/ginkgo v1.6.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+WWjE=
github.com/onsi/ginkgo v1.10.1 h1:q/mM8GF/n0shIN8SaAZ0V+jnLPzen6WIVZdiwrRlMlo=
github.com/onsi/ginkgo v1.10.1/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+WWjE=
github.com/onsi/gomega v1.7.0 h1:XPnZz8VVBHjVsy1vzJmRwIcSwiUO+JFfrv/xGiigmME=
github.com/onsi/gomega v1.7.0/go.mod h1:ex+gbHU/CVuBBDIJjb2X0qEXbFg53c61hWP/1CpauHY=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/sirupsen/logrus v1.4.2/go.mod h1:tLMulIdttU9McNUspp0xgXVQah82FyeX6MwdIuYE2rE=
github.com/smartystreets/assertions v0.0.0-20180927180507-b2de0cb4f26d h1:zE9ykElWQ6/NYmHa3jpm/yHnI4xSofP+UP6SpjHcSeM=
github.com/smartystreets/assertions v0.0.0-20180927180507-b2de0cb4f26d/go.mod h1:OnSkiWE9lh6wB0YB77sQom3nweQdgAjqCqsofrRNTgc=
github.com/smartystreets/goconvey v0.0.0-20190330032615-68dc04aab96a h1:pa8hGb/2YqsZKovtsgrwcDH1RZhVbTKCjLp47XpqCDs=
github.com/smartystreets/goconvey v0.0.0-20190330032615-68dc04aab96a/go.mod h1:syvi0/a8iFYH4r/RixwvyeAJjdLS9QV7WQ/tjFTllLA=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.1.1/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0 h1:2E4SXV/wtOkTonXsotYi4li6zVWxYlZuYNCXe9XRJyk=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/twinj/uuid v1.0.0 h1:fzz7COZnDrXGTAOHGuUGYd6sG+JMq+AoE7+Jlu0przk=
github.com/twinj/uuid v1.0.0/go.mod h1:mMgcE1RHFUFqe5AfiwlINXisXfDGro23fWdPUfOMjRY=
github.com/ugorji/go v1.1.7 h1:/68gy2h+1mWMrwZFeD1kQialdSzAb432dtpeJ42ovdo=
github.com/ugorji/go v1.1.7/go.mod h1:kZn38zHttfInRq0xu/PH0az30d+z6vm202qpg1oXVMw=
github.com/ugorji/go/codec v1.1.7 h1:2SvQaVZ1ouYrrKKwoSk2pzd4A9evlKJb9oTL+OaLUSs=
github.com/ugorji/go/codec v1.1.7/go.mod h1:Ax+UKWsSmolVDwsd+7N3ZtXu+yMGCf907BLYF3GoBXY=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190325154230-a5d413f7728c/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190513172903-22d7a77e9e5f/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20191205180655-e7c4368fe9dd h1:GGJVjV8waZKRHrgwvtH66z9ZGVurTD1MT0n1Bb+q4aM=
golang.org/x/crypto v0.0.0-20191205180655-e7c4368fe9dd/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/net v0.0.0-20180724234803-3673e40ba225/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180906233101-161cd47e91fd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190522155817-f3200d17e092/go.mod h1:HSz+uSET+XFnRR8LxR5pz3Of3rY3CfYBVs4xY44aLks=
golang.org/x/net v0.0.0-20190923162816-aa69164e4478 h1:l5EDrHhldLYb3ZRHDUhXF7Om7MvYXnkV9/iQNo1lX6g=
golang.org/x/net v0.0.0-20190923162816-aa69164e4478/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200202094626-16171245cfb2 h1:CCH4IOTTfewWjGOlSp+zGcjutRKlBEZQ6wTn8ozI/nI=
golang.org/x/net v0.0.0-20200202094626-16171245cfb2/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20180909124046-d0be0721c37e/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190422165155-953cdadca894/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190813064441-fde4db37ae7a h1:aYOabOQFp6Vj6W1F80affTUvO9UxmJRx8K0gsfABByQ=
golang.org/x/sys v0.0.0-20190813064441-fde4db37ae7a/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191010194322-b09406accb47 h1:/XfQ9z7ib8eEJX2hdgFTZJ/ntt0swNk5oYBziWeTCvY=
golang.org/x/sys v0.0.0-20191010194322-b09406accb47/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.2 h1:tW2bmiBqwgJj/UpqtC8EpXEZVYOwU0yG4iWbprSVAcs=
golang.org/x/text v0.3.2/go.mod h1:bEr9sfX3Q8Zfm5fL9x+3itogRgK3+ptLWKqgva+5dAk=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190328211700-ab21143f2384/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
google.golang.org/appengine v1.4.0 h1:/wp5JvzpHIxhs/dumFmF7BXTf3Z+dd4uXta4kVyO508=
google.golang.org/appengine v1.4.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15 h1:YR8cESwS4TdDjEe65xsg0ogRM/Nc3DYOhEAlW+xobZo=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/fsnotify.v1 v1.4.7 h1:xOHLXZwVvI9hhs+cLKq5+I5onOuwQLhQwiu63xxlHs4=
gopkg.in/fsnotify.v1 v1.4.7/go.mod h1:Tz8NjZHkW78fSQdbUxIjBTcgA1z1m8ZHf0WmKUhAMys=
gopkg.in/go-playground/assert.v1 v1.2.1 h1:xoYuJVE7KT85PYWrN730RguIQO0ePzVRfFMXadIrXTM=
gopkg.in/go-playground/assert.v1 v1.2.1/go.mod h1:9RXL0bg/zibRAgZUYszZSwO/z8Y/a8bDuhia5mkpMnE=
gopkg.in/go-playground/validator.v9 v9.29.1 h1:SvGtYmN60a5CVKTOzMSyfzWDeZRxRuGvRQyEAKbw1xc=
gopkg.in/go-playground/validator.v9 v9.29.1/go.mod h1:+c9/zcJMFNgbLvly1L1V+PpxWdVbfP1avr/N00E2vyQ=
gopkg.in/ini.v1 v1.42.0 h1:7N3gPTt50s8GuLortA00n8AqRTk75qOP98+mTPpgzRk=
gopkg.in/ini.v1 v1.42.0/go.mod h1:pNLf8WUiyNEtQjuu5G5vTm06TEv9tsIgeAvK8hOrP4k=
gopkg.in/stretchr/testify.v1 v1.2.2 h1:yhQC6Uy5CqibAIlk1wlusa/MJ3iAN49/BsR/dCCKz3M=
gopkg.in/stretchr/testify.v1 v1.2.2/go.mod h1:QI5V/q6UbPmuhtm10CaFZxED9NreB8PnFYN9JcR6TxU=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7 h1:uRGJdciOHaEIrze2W8Q3AKkepLTh2hOroT7a+7czfdQ=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7/go.mod h1:dt/ZhP58zS4L8KSrWDmTeBkI65Dw0HsyUHuEVlX15mw=
gopkg.in/yaml.v2 v2.2.1/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.2 h1:ZCJp+EgiOT7lHqUV2J862kp8Qj64Jo6az82+3Td9dZw=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.4 h1:/eiJrUcujPVeJ3xlSWaiNi3uSVmDGBK1pDHUHAnao1I=
gopkg.in/yaml.v2 v2.2.4/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
```

## File: `main.go`
```go
package main

import (
	"food-app/infrastructure/auth"
	"food-app/infrastructure/persistence"
	"food-app/interfaces"
	"food-app/interfaces/fileupload"
	"food-app/interfaces/middleware"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"log"
	"os"
)

func init() {
	//To load our environmental variables.
	if err := godotenv.Load(); err != nil {
		log.Println("no env gotten")
	}
}

func main() {

	dbdriver := os.Getenv("DB_DRIVER")
	host := os.Getenv("DB_HOST")
	password := os.Getenv("DB_PASSWORD")
	user := os.Getenv("DB_USER")
	dbname := os.Getenv("DB_NAME")
	port := os.Getenv("DB_PORT")

	//redis details
	redis_host := os.Getenv("REDIS_HOST")
	redis_port := os.Getenv("REDIS_PORT")
	redis_password := os.Getenv("REDIS_PASSWORD")


	services, err := persistence.NewRepositories(dbdriver, user, password, port, host, dbname)
	if err != nil {
		panic(err)
	}
	defer services.Close()
	services.Automigrate()

	redisService, err := auth.NewRedisDB(redis_host, redis_port, redis_password)
	if err != nil {
		log.Fatal(err)
	}

	tk := auth.NewToken()
	fd := fileupload.NewFileUpload()

	users := interfaces.NewUsers(services.User, redisService.Auth, tk)
	foods := interfaces.NewFood(services.Food, services.User, fd, redisService.Auth, tk)
	authenticate := interfaces.NewAuthenticate(services.User, redisService.Auth, tk)

	r := gin.Default()
	r.Use(middleware.CORSMiddleware()) //For CORS

	//user routes
	r.POST("/users", users.SaveUser)
	r.GET("/users", users.GetUsers)
	r.GET("/users/:user_id", users.GetUser)

	//post routes
	r.POST("/food", middleware.AuthMiddleware(), middleware.MaxSizeAllowed(8192000), foods.SaveFood)
	r.PUT("/food/:food_id", middleware.AuthMiddleware(), middleware.MaxSizeAllowed(8192000), foods.UpdateFood)
	r.GET("/food/:food_id", foods.GetFoodAndCreator)
	r.DELETE("/food/:food_id", middleware.AuthMiddleware(), foods.DeleteFood)
	r.GET("/food", foods.GetAllFood)

	//authentication routes
	r.POST("/login", authenticate.Login)
	r.POST("/logout", authenticate.Logout)
	r.POST("/refresh", authenticate.Refresh)


	//Starting the application
	app_port := os.Getenv("PORT") //using heroku host
	if app_port == "" {
		app_port = "8888" //localhost
	}
	log.Fatal(r.Run(":"+app_port))
}
```

## File: `application/food_app.go`
```go
package application

import (
	"food-app/domain/entity"
	"food-app/domain/repository"
)

type foodApp struct {
	fr repository.FoodRepository
}


var _ FoodAppInterface = &foodApp{}

type FoodAppInterface interface {
	SaveFood(*entity.Food) (*entity.Food, map[string]string)
	GetAllFood() ([]entity.Food, error)
	GetFood(uint64) (*entity.Food, error)
	UpdateFood(*entity.Food) (*entity.Food, map[string]string)
	DeleteFood(uint64) error
}

func (f *foodApp) SaveFood(food *entity.Food) (*entity.Food, map[string]string) {
	return f.fr.SaveFood(food)
}

func (f *foodApp) GetAllFood() ([]entity.Food, error) {
	return f.fr.GetAllFood()
}

func (f *foodApp) GetFood(foodId uint64) (*entity.Food, error) {
	return f.fr.GetFood(foodId)
}

func (f *foodApp) UpdateFood(food *entity.Food) (*entity.Food, map[string]string) {
	return f.fr.UpdateFood(food)
}

func (f *foodApp) DeleteFood(foodId uint64) error {
	return f.fr.DeleteFood(foodId)
}
```

## File: `application/food_app_test.go`
```go
package application

import (
	"food-app/domain/entity"
	"github.com/stretchr/testify/assert"
	"testing"
)

//IF YOU HAVE TIME, YOU CAN TEST ALL THE METHODS FAILURES

type fakeFoodRepo struct{}

var (
	saveFoodRepo   func(*entity.Food) (*entity.Food, map[string]string)
	getFoodRepo    func(uint64) (*entity.Food, error)
	getAllFoodRepo func() ([]entity.Food, error)
	updateFoodRepo func(*entity.Food) (*entity.Food, map[string]string)
	deleteFoodRepo func(uint64) error
)

func (f *fakeFoodRepo) SaveFood(food *entity.Food) (*entity.Food, map[string]string) {
	return saveFoodRepo(food)
}
func (f *fakeFoodRepo) GetFood(foodId uint64) (*entity.Food, error) {
	return getFoodRepo(foodId)
}
func (f *fakeFoodRepo) GetAllFood() ([]entity.Food, error) {
	return getAllFoodRepo()
}
func (f *fakeFoodRepo) UpdateFood(food *entity.Food) (*entity.Food, map[string]string) {
	return updateFoodRepo(food)
}
func (f *fakeFoodRepo) DeleteFood(foodId uint64) error {
	return deleteFoodRepo(foodId)
}

//var fakeFood repository.FoodRepository = &fakeFoodRepo{} //this is where the real implementation is swap with our fake implementation
var foodAppFake FoodAppInterface = &fakeFoodRepo{} //this is where the real implementation is swap with our fake implementation

func TestSaveFood_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	saveFoodRepo = func(user *entity.Food) (*entity.Food, map[string]string) {
		return &entity.Food{
			ID:          1,
			Title:       "food title",
			Description: "food description",
			UserID:      1,
		}, nil
	}
	food := &entity.Food{
		ID:          1,
		Title:       "food title",
		Description: "food description",
		UserID:      1,
	}
	f, err := foodAppFake.SaveFood(food)
	assert.Nil(t, err)
	assert.EqualValues(t, f.Title, "food title")
	assert.EqualValues(t, f.Description, "food description")
	assert.EqualValues(t, f.UserID, 1)
}

func TestGetFood_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	getFoodRepo = func(foodId uint64) (*entity.Food, error) {
		return &entity.Food{
			ID:          1,
			Title:       "food title",
			Description: "food description",
			UserID:      1,
		}, nil
	}
	foodId := uint64(1)
	f, err := foodAppFake.GetFood(foodId)
	assert.Nil(t, err)
	assert.EqualValues(t, f.Title, "food title")
	assert.EqualValues(t, f.Description, "food description")
	assert.EqualValues(t, f.UserID, 1)
}

func TestAllFood_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	getAllFoodRepo = func() ([]entity.Food, error) {
		return []entity.Food{
			{
				ID:          1,
				Title:       "food title first",
				Description: "food description first",
				UserID:      1,
			},
			{
				ID:          2,
				Title:       "food title second",
				Description: "food description second",
				UserID:      1,
			},
		}, nil
	}
	f, err := foodAppFake.GetAllFood()
	assert.Nil(t, err)
	assert.EqualValues(t, len(f), 2)
}

func TestUpdateFood_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	updateFoodRepo = func(user *entity.Food) (*entity.Food, map[string]string) {
		return &entity.Food{
			ID:          1,
			Title:       "food title update",
			Description: "food description update",
			UserID:      1,
		}, nil
	}
	food := &entity.Food{
		ID:          1,
		Title:       "food title update",
		Description: "food description update",
		UserID:      1,
	}
	f, err := foodAppFake.UpdateFood(food)
	assert.Nil(t, err)
	assert.EqualValues(t, f.Title, "food title update")
	assert.EqualValues(t, f.Description, "food description update")
	assert.EqualValues(t, f.UserID, 1)
}

func TestDeleteFood_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	deleteFoodRepo = func(foodId uint64) error {
		return nil
	}
	foodId := uint64(1)
	err := foodAppFake.DeleteFood(foodId)
	assert.Nil(t, err)
}
```

## File: `application/user_app.go`
```go
package application

import (
	"food-app/domain/entity"
	"food-app/domain/repository"
)

type userApp struct {
	us repository.UserRepository
}

//UserApp implements the UserAppInterface
var _ UserAppInterface = &userApp{}

type UserAppInterface interface {
	SaveUser(*entity.User) (*entity.User, map[string]string)
	GetUsers() ([]entity.User, error)
	GetUser(uint64) (*entity.User, error)
	GetUserByEmailAndPassword(*entity.User) (*entity.User, map[string]string)
}

func (u *userApp) SaveUser(user *entity.User) (*entity.User, map[string]string) {
	return u.us.SaveUser(user)
}

func (u *userApp) GetUser(userId uint64) (*entity.User, error) {
	return u.us.GetUser(userId)
}

func (u *userApp) GetUsers() ([]entity.User, error) {
	return u.us.GetUsers()
}

func (u *userApp) GetUserByEmailAndPassword(user *entity.User) (*entity.User, map[string]string) {
	return u.us.GetUserByEmailAndPassword(user)
}
```

## File: `application/user_app_test.go`
```go
package application

import (
	"food-app/domain/entity"
	"github.com/stretchr/testify/assert"
	"testing"
)

//IF YOU HAVE TIME, YOU CAN TEST ALL THE METHODS FAILURES

var (
	saveUserRepo                func(*entity.User) (*entity.User, map[string]string)
	getUserRepo                 func(userId uint64) (*entity.User, error)
	getUsersRepo                func() ([]entity.User, error)
	getUserEmailAndPasswordRepo func(*entity.User) (*entity.User, map[string]string)
)

type fakeUserRepo struct{}

func (u *fakeUserRepo) SaveUser(user *entity.User) (*entity.User, map[string]string) {
	return saveUserRepo(user)
}
func (u *fakeUserRepo) GetUser(userId uint64) (*entity.User, error) {
	return getUserRepo(userId)
}
func (u *fakeUserRepo) GetUsers() ([]entity.User, error) {
	return getUsersRepo()
}
func (u *fakeUserRepo) GetUserByEmailAndPassword(user *entity.User) (*entity.User, map[string]string) {
	return getUserEmailAndPasswordRepo(user)
}

var userAppFake UserAppInterface = &fakeUserRepo{} //this is where the real implementation is swap with our fake implementation

func TestSaveUser_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	saveUserRepo = func(user *entity.User) (*entity.User, map[string]string) {
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
			Email:     "steven@example.com",
			Password:  "password",
		}, nil
	}
	user := &entity.User{
		ID:        1,
		FirstName: "victor",
		LastName:  "steven",
		Email:     "steven@example.com",
		Password:  "password",
	}
	u, err := userAppFake.SaveUser(user)
	assert.Nil(t, err)
	assert.EqualValues(t, u.FirstName, "victor")
	assert.EqualValues(t, u.LastName, "steven")
	assert.EqualValues(t, u.Email, "steven@example.com")
}

func TestGetUser_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	getUserRepo = func(userId uint64) (*entity.User, error) {
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
			Email:     "steven@example.com",
			Password:  "password",
		}, nil
	}
	userId := uint64(1)
	u, err := userAppFake.GetUser(userId)
	assert.Nil(t, err)
	assert.EqualValues(t, u.FirstName, "victor")
	assert.EqualValues(t, u.LastName, "steven")
	assert.EqualValues(t, u.Email, "steven@example.com")
}

func TestGetUsers_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	getUsersRepo = func() ([]entity.User, error) {
		return []entity.User{
			{
				ID:        1,
				FirstName: "victor",
				LastName:  "steven",
				Email:     "steven@example.com",
				Password:  "password",
			},
			{
				ID:        2,
				FirstName: "kobe",
				LastName:  "bryant",
				Email:     "kobe@example.com",
				Password:  "password",
			},
		}, nil
	}
	users, err := userAppFake.GetUsers()
	assert.Nil(t, err)
	assert.EqualValues(t, len(users), 2)
}

func TestGetUserByEmailAndPassword_Success(t *testing.T) {
	//Mock the response coming from the infrastructure
	getUserEmailAndPasswordRepo = func(user *entity.User) (*entity.User, map[string]string) {
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
			Email:     "steven@example.com",
			Password:  "password",
		}, nil
	}
	user := &entity.User{
		ID:        1,
		FirstName: "victor",
		LastName:  "steven",
		Email:     "steven@example.com",
		Password:  "password",
	}
	u, err := userAppFake.GetUserByEmailAndPassword(user)
	assert.Nil(t, err)
	assert.EqualValues(t, u.FirstName, "victor")
	assert.EqualValues(t, u.LastName, "steven")
	assert.EqualValues(t, u.Email, "steven@example.com")
}
```

## File: `domain/entity/food.go`
```go
package entity

import (
	"html"
	"strings"
	"time"
)

type Food struct {
	ID          uint64     `gorm:"primary_key;auto_increment" json:"id"`
	UserID      uint64     `gorm:"size:100;not null;" json:"user_id"`
	Title       string     `gorm:"size:100;not null;unique" json:"title"`
	Description string     `gorm:"text;not null;" json:"description"`
	FoodImage   string     `gorm:"size:255;null;" json:"food_image"`
	CreatedAt   time.Time  `gorm:"default:CURRENT_TIMESTAMP" json:"created_at"`
	UpdatedAt   time.Time  `gorm:"default:CURRENT_TIMESTAMP" json:"updated_at"`
	DeletedAt   *time.Time `json:"deleted_at"`
}

func (f *Food) BeforeSave() {
	f.Title = html.EscapeString(strings.TrimSpace(f.Title))
}

func (f *Food) Prepare() {
	f.Title = html.EscapeString(strings.TrimSpace(f.Title))
	f.CreatedAt = time.Now()
	f.UpdatedAt = time.Now()
}

func (f *Food) Validate(action string) map[string]string {
	var errorMessages = make(map[string]string)

	switch strings.ToLower(action) {
	case "update":
		if f.Title == "" || f.Title == "null" {
			errorMessages["title_required"] = "title is required"
		}
		if f.Description == "" || f.Description == "null" {
			errorMessages["desc_required"] = "description is required"
		}
	default:
		if f.Title == "" || f.Title == "null" {
			errorMessages["title_required"] = "title is required"
		}
		if f.Description == "" || f.Description == "null" {
			errorMessages["desc_required"] = "description is required"
		}
	}
	return errorMessages
}
```

## File: `domain/entity/user.go`
```go
package entity

import (
	"food-app/infrastructure/security"
	"github.com/badoux/checkmail"
	"html"
	"strings"
	"time"
)

type User struct {
	ID        uint64     `gorm:"primary_key;auto_increment" json:"id"`
	FirstName string     `gorm:"size:100;not null;" json:"first_name"`
	LastName  string     `gorm:"size:100;not null;" json:"last_name"`
	Email     string     `gorm:"size:100;not null;unique" json:"email"`
	Password  string     `gorm:"size:100;not null;" json:"password"`
	CreatedAt time.Time  `gorm:"default:CURRENT_TIMESTAMP" json:"created_at"`
	UpdatedAt time.Time  `gorm:"default:CURRENT_TIMESTAMP" json:"updated_at"`
	DeletedAt *time.Time `json:"deleted_at,omitempty"`
}

type PublicUser struct {
	ID        uint64 `gorm:"primary_key;auto_increment" json:"id"`
	FirstName string `gorm:"size:100;not null;" json:"first_name"`
	LastName  string `gorm:"size:100;not null;" json:"last_name"`
}

//BeforeSave is a gorm hook
func (u *User) BeforeSave() error {
	hashPassword, err := security.Hash(u.Password)
	if err != nil {
		return err
	}
	u.Password = string(hashPassword)
	return nil
}

type Users []User

//So that we dont expose the user's email address and password to the world
func (users Users) PublicUsers() []interface{} {
	result := make([]interface{}, len(users))
	for index, user := range users {
		result[index] = user.PublicUser()
	}
	return result
}

//So that we dont expose the user's email address and password to the world
func (u *User) PublicUser() interface{} {
	return &PublicUser{
		ID:        u.ID,
		FirstName: u.FirstName,
		LastName:  u.LastName,
	}
}

func (u *User) Prepare() {
	u.FirstName = html.EscapeString(strings.TrimSpace(u.FirstName))
	u.LastName = html.EscapeString(strings.TrimSpace(u.LastName))
	u.Email = html.EscapeString(strings.TrimSpace(u.Email))
	u.CreatedAt = time.Now()
	u.UpdatedAt = time.Now()
}

func (u *User) Validate(action string) map[string]string {
	var errorMessages = make(map[string]string)
	var err error

	switch strings.ToLower(action) {
	case "update":
		if u.Email == "" {
			errorMessages["email_required"] = "email required"
		}
		if u.Email != "" {
			if err = checkmail.ValidateFormat(u.Email); err != nil {
				errorMessages["invalid_email"] = "email email"
			}
		}

	case "login":
		if u.Password == "" {
			errorMessages["password_required"] = "password is required"
		}
		if u.Email == "" {
			errorMessages["email_required"] = "email is required"
		}
		if u.Email != "" {
			if err = checkmail.ValidateFormat(u.Email); err != nil {
				errorMessages["invalid_email"] = "please provide a valid email"
			}
		}
	case "forgotpassword":
		if u.Email == "" {
			errorMessages["email_required"] = "email required"
		}
		if u.Email != "" {
			if err = checkmail.ValidateFormat(u.Email); err != nil {
				errorMessages["invalid_email"] = "please provide a valid email"
			}
		}
	default:
		if u.FirstName == "" {
			errorMessages["firstname_required"] = "first name is required"
		}
		if u.LastName == "" {
			errorMessages["lastname_required"] = "last name is required"
		}
		if u.Password == "" {
			errorMessages["password_required"] = "password is required"
		}
		if u.Password != "" && len(u.Password) < 6 {
			errorMessages["invalid_password"] = "password should be at least 6 characters"
		}
		if u.Email == "" {
			errorMessages["email_required"] = "email is required"
		}
		if u.Email != "" {
			if err = checkmail.ValidateFormat(u.Email); err != nil {
				errorMessages["invalid_email"] = "please provide a valid email"
			}
		}
	}
	return errorMessages
}
```

## File: `domain/repository/food_repository.go`
```go
package repository

import "food-app/domain/entity"

type FoodRepository interface {
	SaveFood(*entity.Food) (*entity.Food, map[string]string)
	GetFood(uint64) (*entity.Food, error)
	GetAllFood() ([]entity.Food, error)
	UpdateFood(*entity.Food) (*entity.Food, map[string]string)
	DeleteFood(uint64) error
}
```

## File: `domain/repository/user_repository.go`
```go
package repository

import (
	"food-app/domain/entity"
)

type UserRepository interface {
	SaveUser(*entity.User) (*entity.User, map[string]string)
	GetUser(uint64) (*entity.User, error)
	GetUsers() ([]entity.User, error)
	GetUserByEmailAndPassword(*entity.User) (*entity.User, map[string]string)
}
```

## File: `infrastructure/auth/auth.go`
```go
package auth

import (
	"errors"
	"fmt"
	"github.com/go-redis/redis/v7"
	"strconv"
	"time"
)

type AuthInterface interface {
	CreateAuth(uint64, *TokenDetails) error
	FetchAuth(string) (uint64, error)
	DeleteRefresh(string) error
	DeleteTokens(*AccessDetails) error
}

type ClientData struct {
	client *redis.Client
}

var _ AuthInterface = &ClientData{}

func NewAuth(client *redis.Client) *ClientData {
	return &ClientData{client: client}
}

type AccessDetails struct {
	TokenUuid string
	UserId    uint64
}

type TokenDetails struct {
	AccessToken  string
	RefreshToken string
	TokenUuid    string
	RefreshUuid  string
	AtExpires    int64
	RtExpires    int64
}

//Save token metadata to Redis
func (tk *ClientData) CreateAuth(userid uint64, td *TokenDetails) error {
	at := time.Unix(td.AtExpires, 0) //converting Unix to UTC(to Time object)
	rt := time.Unix(td.RtExpires, 0)
	now := time.Now()

	atCreated, err := tk.client.Set(td.TokenUuid, strconv.Itoa(int(userid)), at.Sub(now)).Result()
	if err != nil {
		return err
	}
	rtCreated, err := tk.client.Set(td.RefreshUuid, strconv.Itoa(int(userid)), rt.Sub(now)).Result()
	if err != nil {
		return err
	}
	if atCreated == "0" || rtCreated == "0" {
		return errors.New("no record inserted")
	}
	return nil
}

//Check the metadata saved
func (tk *ClientData) FetchAuth(tokenUuid string) (uint64, error) {
	userid, err := tk.client.Get(tokenUuid).Result()
	if err != nil {
		return 0, err
	}
	userID, _ := strconv.ParseUint(userid, 10, 64)
	return userID, nil
}

//Once a user row in the token table
func (tk *ClientData) DeleteTokens(authD *AccessDetails) error {
	//get the refresh uuid
	refreshUuid := fmt.Sprintf("%s++%d", authD.TokenUuid, authD.UserId)
	//delete access token
	deletedAt, err := tk.client.Del(authD.TokenUuid).Result()
	if err != nil {
		return err
	}
	//delete refresh token
	deletedRt, err := tk.client.Del(refreshUuid).Result()
	if err != nil {
		return err
	}
	//When the record is deleted, the return value is 1
	if deletedAt != 1 || deletedRt != 1 {
		return errors.New("something went wrong")
	}
	return nil
}

func (tk *ClientData) DeleteRefresh(refreshUuid string) error {
	//delete refresh token
	deleted, err := tk.client.Del(refreshUuid).Result()
	if err != nil || deleted == 0 {
		return err
	}
	return nil
}
```

## File: `infrastructure/auth/redisdb.go`
```go
package auth

import "github.com/go-redis/redis/v7"


type RedisService struct {
	Auth   AuthInterface
	Client *redis.Client
}

func NewRedisDB(host, port, password string) (*RedisService, error) {
	redisClient := redis.NewClient(&redis.Options{
		Addr:     host + ":" + port,
		Password: password,
		DB:       0,
	})
	return &RedisService{
		Auth:   NewAuth(redisClient),
		Client: redisClient,
	}, nil
}
```

## File: `infrastructure/auth/token.go`
```go
package auth

import (
	"fmt"
	"github.com/dgrijalva/jwt-go"
	"github.com/twinj/uuid"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)


type Token struct{}

func NewToken() *Token {
	return &Token{}
}

type TokenInterface interface {
	CreateToken(userid uint64) (*TokenDetails, error)
	ExtractTokenMetadata(*http.Request) (*AccessDetails, error)
}

//Token implements the TokenInterface
var _ TokenInterface = &Token{}

func (t *Token) CreateToken(userid uint64) (*TokenDetails, error) {
	td := &TokenDetails{}
	td.AtExpires = time.Now().Add(time.Minute * 15).Unix()
	td.TokenUuid = uuid.NewV4().String()

	td.RtExpires = time.Now().Add(time.Hour * 24 * 7).Unix()
	td.RefreshUuid = td.TokenUuid + "++" + strconv.Itoa(int(userid))

	var err error
	//Creating Access Token
	atClaims := jwt.MapClaims{}
	atClaims["authorized"] = true
	atClaims["access_uuid"] = td.TokenUuid
	atClaims["user_id"] = userid
	atClaims["exp"] = td.AtExpires
	at := jwt.NewWithClaims(jwt.SigningMethodHS256, atClaims)
	td.AccessToken, err = at.SignedString([]byte(os.Getenv("ACCESS_SECRET")))
	if err != nil {
		return nil, err
	}
	//Creating Refresh Token
	rtClaims := jwt.MapClaims{}
	rtClaims["refresh_uuid"] = td.RefreshUuid
	rtClaims["user_id"] = userid
	rtClaims["exp"] = td.RtExpires
	rt := jwt.NewWithClaims(jwt.SigningMethodHS256, rtClaims)
	td.RefreshToken, err = rt.SignedString([]byte(os.Getenv("REFRESH_SECRET")))
	if err != nil {
		return nil, err
	}
	return td, nil
}

func TokenValid(r *http.Request) error {
	token, err := VerifyToken(r)
	if err != nil {
		return err
	}
	if _, ok := token.Claims.(jwt.Claims); !ok && !token.Valid {
		return err
	}
	return nil
}

func VerifyToken(r *http.Request) (*jwt.Token, error) {
	tokenString := ExtractToken(r)
	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		//Make sure that the token method conform to "SigningMethodHMAC"
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
		}
		return []byte(os.Getenv("ACCESS_SECRET")), nil
	})
	if err != nil {
		return nil, err
	}
	return token, nil
}

//get the token from the request body
func ExtractToken(r *http.Request) string {
	bearToken := r.Header.Get("Authorization")
	strArr := strings.Split(bearToken, " ")
	if len(strArr) == 2 {
		return strArr[1]
	}
	return ""
}

func (t *Token) ExtractTokenMetadata(r *http.Request) (*AccessDetails, error) {
	fmt.Println("WE ENTERED METADATA")
	token, err := VerifyToken(r)
	if err != nil {
		return nil, err
	}
	claims, ok := token.Claims.(jwt.MapClaims)
	if ok && token.Valid {
		accessUuid, ok := claims["access_uuid"].(string)
		if !ok {
			return nil, err
		}
		userId, err := strconv.ParseUint(fmt.Sprintf("%.f", claims["user_id"]), 10, 64)
		if err != nil {
			return nil, err
		}
		return &AccessDetails{
			TokenUuid: accessUuid,
			UserId:    userId,
		}, nil
	}
	return nil, err
}
```

## File: `infrastructure/persistence/db.go`
```go
package persistence

import (
	"fmt"
	"food-app/domain/entity"
	"food-app/domain/repository"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

type Repositories struct {
	User repository.UserRepository
	Food repository.FoodRepository
	db   *gorm.DB
}

func NewRepositories(Dbdriver, DbUser, DbPassword, DbPort, DbHost, DbName string) (*Repositories, error) {
	DBURL := fmt.Sprintf("host=%s port=%s user=%s dbname=%s sslmode=disable password=%s", DbHost, DbPort, DbUser, DbName, DbPassword)
	db, err := gorm.Open(Dbdriver, DBURL)
	if err != nil {
		return nil, err
	}
	db.LogMode(true)

	return &Repositories{
		User: NewUserRepository(db),
		Food: NewFoodRepository(db),
		db:   db,
	}, nil
}

//closes the  database connection
func (s *Repositories) Close() error {
	return s.db.Close()
}

//This migrate all tables
func (s *Repositories) Automigrate() error {
	return s.db.AutoMigrate(&entity.User{}, &entity.Food{}).Error
}
```

## File: `infrastructure/persistence/food_repository.go`
```go
package persistence

import (
	"errors"
	"food-app/domain/entity"
	"food-app/domain/repository"
	"github.com/jinzhu/gorm"
	"os"
	"strings"
)


type FoodRepo struct {
	db *gorm.DB
}

func NewFoodRepository(db *gorm.DB) *FoodRepo {
	return &FoodRepo{db}
}

//FoodRepo implements the repository.FoodRepository interface
var _ repository.FoodRepository = &FoodRepo{}

func (r *FoodRepo) SaveFood(food *entity.Food) (*entity.Food, map[string]string) {
	dbErr := map[string]string{}
	//The images are uploaded to digital ocean spaces. So we need to prepend the url. This might not be your use case, if you are not uploading image to Digital Ocean.
	food.FoodImage = os.Getenv("DO_SPACES_URL") + food.FoodImage

	err := r.db.Debug().Create(&food).Error
	if err != nil {
		//since our title is unique
		if strings.Contains(err.Error(), "duplicate") || strings.Contains(err.Error(), "Duplicate") {
			dbErr["unique_title"] = "food title already taken"
			return nil, dbErr
		}
		//any other db error
		dbErr["db_error"] = "database error"
		return nil, dbErr
	}
	return food, nil
}

func (r *FoodRepo) GetFood(id uint64) (*entity.Food, error) {
	var food entity.Food
	err := r.db.Debug().Where("id = ?", id).Take(&food).Error
	if err != nil {
		return nil, errors.New("database error, please try again")
	}
	if gorm.IsRecordNotFoundError(err) {
		return nil, errors.New("food not found")
	}
	return &food, nil
}

func (r *FoodRepo) GetAllFood() ([]entity.Food, error) {
	var foods []entity.Food
	err := r.db.Debug().Limit(100).Order("created_at desc").Find(&foods).Error
	if err != nil {
		return nil, err
	}
	if gorm.IsRecordNotFoundError(err) {
		return nil, errors.New("user not found")
	}
	return foods, nil
}

func (r *FoodRepo) UpdateFood(food *entity.Food) (*entity.Food, map[string]string) {
	dbErr := map[string]string{}
	err := r.db.Debug().Save(&food).Error
	if err != nil {
		//since our title is unique
		if strings.Contains(err.Error(), "duplicate") || strings.Contains(err.Error(), "Duplicate") {
			dbErr["unique_title"] = "title already taken"
			return nil, dbErr
		}
		//any other db error
		dbErr["db_error"] = "database error"
		return nil, dbErr
	}
	return food, nil
}

func (r *FoodRepo) DeleteFood(id uint64) error {
	var food entity.Food
	err := r.db.Debug().Where("id = ?", id).Delete(&food).Error
	if err != nil {
		return errors.New("database error, please try again")
	}
	return nil
}
```

## File: `infrastructure/persistence/food_repository_test.go`
```go
package persistence

import (
	"food-app/domain/entity"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestSaveFood_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	var food = entity.Food{}
	food.Title = "food title"
	food.Description = "food description"
	food.UserID = 1

	repo := NewFoodRepository(conn)

	f, saveErr := repo.SaveFood(&food)
	assert.Nil(t, saveErr)
	assert.EqualValues(t, f.Title, "food title")
	assert.EqualValues(t, f.Description, "food description")
	assert.EqualValues(t, f.UserID, 1)
}

//Failure can be due to duplicate email, etc
//Here, we will attempt saving a food that is already saved
func TestSaveFood_Failure(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	//seed the food
	_, err = seedFood(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	var food = entity.Food{}
	food.Title = "food title"
	food.Description = "food desc"
	food.UserID = 1

	repo := NewFoodRepository(conn)
	f, saveErr := repo.SaveFood(&food)

	dbMsg := map[string]string{
		"unique_title": "food title already taken",
	}
	assert.Nil(t, f)
	assert.EqualValues(t, dbMsg, saveErr)
}

func TestGetFood_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	food, err := seedFood(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	repo := NewFoodRepository(conn)

	f, saveErr := repo.GetFood(food.ID)

	assert.Nil(t, saveErr)
	assert.EqualValues(t, f.Title, food.Title)
	assert.EqualValues(t, f.Description, food.Description)
	assert.EqualValues(t, f.UserID, food.UserID)
}

func TestGetAllFood_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	_, err = seedFoods(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	repo := NewFoodRepository(conn)
	foods, getErr := repo.GetAllFood()

	assert.Nil(t, getErr)
	assert.EqualValues(t, len(foods), 2)
}

func TestUpdateFood_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	food, err := seedFood(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	//updating
	food.Title = "food title update"
	food.Description = "food description update"

	repo := NewFoodRepository(conn)
	f, updateErr := repo.UpdateFood(food)

	assert.Nil(t, updateErr)
	assert.EqualValues(t, f.ID, 1)
	assert.EqualValues(t, f.Title, "food title update")
	assert.EqualValues(t, f.Description, "food description update")
	assert.EqualValues(t, f.UserID, 1)
}

//Duplicate title error
func TestUpdateFood_Failure(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	foods, err := seedFoods(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	var secondFood entity.Food

	//get the second food title
	for _, v := range foods {
		if v.ID == 1 {
			continue
		}
		secondFood = v
	}
	secondFood.Title = "first food" //this title belongs to the first food already, so the second food cannot use it
	secondFood.Description = "New description"

	repo := NewFoodRepository(conn)
	f, updateErr := repo.UpdateFood(&secondFood)

	dbMsg := map[string]string{
		"unique_title": "title already taken",
	}
	assert.NotNil(t, updateErr)
	assert.Nil(t, f)
	assert.EqualValues(t, dbMsg, updateErr)
}

func TestDeleteFood_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	food, err := seedFood(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	repo := NewFoodRepository(conn)

	deleteErr := repo.DeleteFood(food.ID)

	assert.Nil(t, deleteErr)
}
```

## File: `infrastructure/persistence/setup_test.go`
```go
package persistence

import (
	"fmt"
	"food-app/domain/entity"
	"github.com/jinzhu/gorm"
	"github.com/joho/godotenv"
	"log"
	"os"
)

func DBConn() (*gorm.DB, error) {
	if _, err := os.Stat("./../../.env"); !os.IsNotExist(err) {
		var err error
		err = godotenv.Load(os.ExpandEnv("./../../.env"))
		if err != nil {
			log.Fatalf("Error getting env %v\n", err)
		}
		return LocalDatabase()
	}
	return CIBuild()
}

//Circle CI DB
func CIBuild() (*gorm.DB, error) {
	var err error
	DBURL := fmt.Sprintf("host=%s port=%s user=%s dbname=%s sslmode=disable password=%s", "127.0.0.1", "5432", "steven", "food-app-test", "password")
	conn, err := gorm.Open("postgres", DBURL)
	if err != nil {
		log.Fatal("This is the error:", err)
	}
	return conn, nil
}

//Local DB
func LocalDatabase() (*gorm.DB, error) {
	dbdriver := os.Getenv("TEST_DB_DRIVER")
	host := os.Getenv("TEST_DB_HOST")
	password := os.Getenv("TEST_DB_PASSWORD")
	user := os.Getenv("TEST_DB_USER")
	dbname := os.Getenv("TEST_DB_NAME")
	port := os.Getenv("TEST_DB_PORT")

	DBURL := fmt.Sprintf("host=%s port=%s user=%s dbname=%s sslmode=disable password=%s", host, port, user, dbname, password)
	conn, err := gorm.Open(dbdriver, DBURL)
	if err != nil {
		return nil, err
	} else {
		log.Println("CONNECTED TO: ", dbdriver)
	}

	err = conn.DropTableIfExists(&entity.User{}, &entity.Food{}).Error
	if err != nil {
		return nil, err
	}
	err = conn.Debug().AutoMigrate(
		entity.User{},
		entity.Food{},
	).Error
	if err != nil {
		return nil, err
	}
	return conn, nil
}

func seedUser(db *gorm.DB) (*entity.User, error) {
	user := &entity.User{
		ID:        1,
		FirstName: "vic",
		LastName:  "stev",
		Email:     "steven@example.com",
		Password:  "password",
		DeletedAt: nil,
	}
	err := db.Create(&user).Error
	if err != nil {
		return nil, err
	}
	return user, nil
}

func seedUsers(db *gorm.DB) ([]entity.User, error) {
	users := []entity.User{
		{
			ID:        1,
			FirstName: "vic",
			LastName:  "stev",
			Email:     "steven@example.com",
			Password:  "password",
			DeletedAt: nil,
		},
		{
			ID:        2,
			FirstName: "kobe",
			LastName:  "bryant",
			Email:     "kobe@example.com",
			Password:  "password",
			DeletedAt: nil,
		},
	}
	for _, v := range users {
		err := db.Create(&v).Error
		if err != nil {
			return nil, err
		}
	}
	return users, nil
}

func seedFood(db *gorm.DB) (*entity.Food, error) {
	food := &entity.Food{
		ID:          1,
		Title:       "food title",
		Description: "food desc",
		UserID:      1,
	}
	err := db.Create(&food).Error
	if err != nil {
		return nil, err
	}
	return food, nil
}

func seedFoods(db *gorm.DB) ([]entity.Food, error) {
	foods := []entity.Food{
		{
			ID:          1,
			Title:       "first food",
			Description: "first desc",
			UserID:      1,
		},
		{
			ID:          2,
			Title:       "second food",
			Description: "second desc",
			UserID:      1,
		},
	}
	for _, v := range foods {
		err := db.Create(&v).Error
		if err != nil {
			return nil, err
		}
	}
	return foods, nil
}
```

## File: `infrastructure/persistence/user_repository.go`
```go
package persistence

import (
	"errors"
	"food-app/domain/entity"
	"food-app/domain/repository"
	"food-app/infrastructure/security"
	"github.com/jinzhu/gorm"
	"golang.org/x/crypto/bcrypt"
	"strings"
)

type UserRepo struct {
	db *gorm.DB
}

func NewUserRepository(db *gorm.DB) *UserRepo {
	return &UserRepo{db}
}
//UserRepo implements the repository.UserRepository interface
var _ repository.UserRepository = &UserRepo{}

func (r *UserRepo) SaveUser(user *entity.User) (*entity.User, map[string]string) {
	dbErr := map[string]string{}
	err := r.db.Debug().Create(&user).Error
	if err != nil {
		//If the email is already taken
		if strings.Contains(err.Error(), "duplicate") || strings.Contains(err.Error(), "Duplicate") {
			dbErr["email_taken"] = "email already taken"
			return nil, dbErr
		}
		//any other db error
		dbErr["db_error"] = "database error"
		return nil, dbErr
	}
	return user, nil
}

func (r *UserRepo) GetUser(id uint64) (*entity.User, error) {
	var user entity.User
	err := r.db.Debug().Where("id = ?", id).Take(&user).Error
	if err != nil {
		return nil, err
	}
	if gorm.IsRecordNotFoundError(err) {
		return nil, errors.New("user not found")
	}
	return &user, nil
}

func (r *UserRepo) GetUsers() ([]entity.User, error) {
	var users []entity.User
	err := r.db.Debug().Find(&users).Error
	if err != nil {
		return nil, err
	}
	if gorm.IsRecordNotFoundError(err) {
		return nil, errors.New("user not found")
	}
	return users, nil
}

func (r *UserRepo) GetUserByEmailAndPassword(u *entity.User) (*entity.User, map[string]string) {
	var user entity.User
	dbErr := map[string]string{}
	err := r.db.Debug().Where("email = ?", u.Email).Take(&user).Error
	if gorm.IsRecordNotFoundError(err) {
		dbErr["no_user"] = "user not found"
		return nil, dbErr
	}
	if err != nil {
		dbErr["db_error"] = "database error"
		return nil, dbErr
	}
	//Verify the password
	err = security.VerifyPassword(user.Password, u.Password)
	if err != nil && err == bcrypt.ErrMismatchedHashAndPassword {
		dbErr["incorrect_password"] = "incorrect password"
		return nil, dbErr
	}
	return &user, nil
}
```

## File: `infrastructure/persistence/user_repository_test.go`
```go
package persistence

import (
	"food-app/domain/entity"
	"github.com/stretchr/testify/assert"
	"testing"
)

//SINCE WE ARE SPINNING UP A DATABASE, THE TESTS HERE ARE INTEGRATION TESTS

//YOU CAN TEST METHOD FAILURES IF YOU HAVE TIME, TO IMPROVE COVERAGE.

func TestSaveUser_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	var user = entity.User{}
	user.Email = "steven@example.com"
	user.FirstName = "victoria"
	user.LastName = "steven"
	user.Password = "password"

	repo := NewUserRepository(conn)

	u, saveErr := repo.SaveUser(&user)
	assert.Nil(t, saveErr)
	assert.EqualValues(t, u.Email, "steven@example.com")
	assert.EqualValues(t, u.FirstName, "victoria")
	assert.EqualValues(t, u.LastName, "steven")
	//The pasword is supposed to be hashed, so, it should not the same the one we passed:
	assert.NotEqual(t, u.Password, "password")
}

//Failure can be due to duplicate email, etc
//Here, we will attempt saving a user that is already saved
func TestSaveUser_Failure(t *testing.T) {

	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	//seed the user
	_, err = seedUser(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	var user = entity.User{}
	user.Email = "steven@example.com"
	user.FirstName = "Kedu"
	user.LastName = "Nwanne"
	user.Password = "password"

	repo := NewUserRepository(conn)
	u, saveErr := repo.SaveUser(&user)
	dbMsg := map[string]string{
		"email_taken": "email already taken",
	}
	assert.Nil(t, u)
	assert.EqualValues(t, dbMsg, saveErr)
}

func TestGetUser_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	//seed the user
	user, err := seedUser(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	repo := NewUserRepository(conn)
	u, getErr := repo.GetUser(user.ID)

	assert.Nil(t, getErr)
	assert.EqualValues(t, u.Email, "steven@example.com")
	assert.EqualValues(t, u.FirstName, "vic")
	assert.EqualValues(t, u.LastName, "stev")
}

func TestGetUsers_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	//seed the users
	_, err = seedUsers(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	repo := NewUserRepository(conn)
	users, getErr := repo.GetUsers()

	assert.Nil(t, getErr)
	assert.EqualValues(t, len(users), 2)
}

func TestGetUserByEmailAndPassword_Success(t *testing.T) {
	conn, err := DBConn()
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	//seed the user
	u, err := seedUser(conn)
	if err != nil {
		t.Fatalf("want non error, got %#v", err)
	}
	var user = &entity.User{
		Email:    "steven@example.com",
		Password: "password",
	}
	repo := NewUserRepository(conn)
	u, getErr := repo.GetUserByEmailAndPassword(user)

	assert.Nil(t, getErr)
	assert.EqualValues(t, u.Email, user.Email)
	//Note, the user password from the database should not be equal to a plane password, because that one is hashed
	assert.NotEqual(t, u.Password, user.Password)
}
```

## File: `infrastructure/security/password.go`
```go
package security

import "golang.org/x/crypto/bcrypt"

func Hash(password string) ([]byte, error) {

	return bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
}

func VerifyPassword(hashedPassword, password string) error {

	return bcrypt.CompareHashAndPassword([]byte(hashedPassword), []byte(password))

}
```

## File: `interfaces/food_handler.go`
```go
package interfaces

import (
	"fmt"
	"food-app/application"
	"food-app/domain/entity"
	"food-app/infrastructure/auth"
	"food-app/interfaces/fileupload"
	"github.com/gin-gonic/gin"
	"net/http"
	"os"
	"strconv"
	"time"
)

type Food struct {
	foodApp    application.FoodAppInterface
	userApp    application.UserAppInterface
	fileUpload fileupload.UploadFileInterface
	tk         auth.TokenInterface
	rd         auth.AuthInterface
}

//Food constructor
func NewFood(fApp application.FoodAppInterface, uApp application.UserAppInterface, fd fileupload.UploadFileInterface, rd auth.AuthInterface, tk auth.TokenInterface) *Food {
	return &Food{
		foodApp:    fApp,
		userApp:    uApp,
		fileUpload: fd,
		rd:         rd,
		tk:         tk,
	}
}

func (fo *Food) SaveFood(c *gin.Context) {
	//check is the user is authenticated first
	metadata, err := fo.tk.ExtractTokenMetadata(c.Request)
	if err != nil {
		c.JSON(http.StatusUnauthorized, "unauthorized")
		return
	}
	//lookup the metadata in redis:
	userId, err := fo.rd.FetchAuth(metadata.TokenUuid)
	if err != nil {
		c.JSON(http.StatusUnauthorized, "unauthorized")
		return
	}
	//We we are using a frontend(vuejs), our errors need to have keys for easy checking, so we use a map to hold our errors
	var saveFoodError = make(map[string]string)

	title := c.PostForm("title")
	description := c.PostForm("description")
	if fmt.Sprintf("%T", title) != "string" || fmt.Sprintf("%T", description) != "string" {
		c.JSON(http.StatusUnprocessableEntity, gin.H{
			"invalid_json": "Invalid json",
		})
		return
	}
	//We initialize a new food for the purpose of validating: in case the payload is empty or an invalid data type is used
	emptyFood := entity.Food{}
	emptyFood.Title = title
	emptyFood.Description = description
	saveFoodError = emptyFood.Validate("")
	if len(saveFoodError) > 0 {
		c.JSON(http.StatusUnprocessableEntity, saveFoodError)
		return
	}
	file, err := c.FormFile("food_image")
	if err != nil {
		saveFoodError["invalid_file"] = "a valid file is required"
		c.JSON(http.StatusUnprocessableEntity, saveFoodError)
		return
	}
	//check if the user exist
	_, err = fo.userApp.GetUser(userId)
	if err != nil {
		c.JSON(http.StatusBadRequest, "user not found, unauthorized")
		return
	}
	uploadedFile, err := fo.fileUpload.UploadFile(file)
	if err != nil {
		saveFoodError["upload_err"] = err.Error() //this error can be any we defined in the UploadFile method
		c.JSON(http.StatusUnprocessableEntity, saveFoodError)
		return
	}
	var food = entity.Food{}
	food.UserID = userId
	food.Title = title
	food.Description = description
	food.FoodImage = uploadedFile
	savedFood, saveErr := fo.foodApp.SaveFood(&food)
	if saveErr != nil {
		c.JSON(http.StatusInternalServerError, saveErr)
		return
	}
	c.JSON(http.StatusCreated, savedFood)
}

func (fo *Food) UpdateFood(c *gin.Context) {
	//Check if the user is authenticated first
	metadata, err := fo.tk.ExtractTokenMetadata(c.Request)
	if err != nil {
		c.JSON(http.StatusUnauthorized, "Unauthorized")
		return
	}
	//lookup the metadata in redis:
	userId, err := fo.rd.FetchAuth(metadata.TokenUuid)
	if err != nil {
		c.JSON(http.StatusUnauthorized, "unauthorized")
		return
	}
	//We we are using a frontend(vuejs), our errors need to have keys for easy checking, so we use a map to hold our errors
	var updateFoodError = make(map[string]string)

	foodId, err := strconv.ParseUint(c.Param("food_id"), 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, "invalid request")
		return
	}
	//Since it is a multipart form data we sent, we will do a manual check on each item
	title := c.PostForm("title")
	description := c.PostForm("description")
	if fmt.Sprintf("%T", title) != "string" || fmt.Sprintf("%T", description) != "string" {
		c.JSON(http.StatusUnprocessableEntity, "Invalid json")
	}
	//We initialize a new food for the purpose of validating: in case the payload is empty or an invalid data type is used
	emptyFood := entity.Food{}
	emptyFood.Title = title
	emptyFood.Description = description
	updateFoodError = emptyFood.Validate("update")
	if len(updateFoodError) > 0 {
		c.JSON(http.StatusUnprocessableEntity, updateFoodError)
		return
	}
	user, err := fo.userApp.GetUser(userId)
	if err != nil {
		c.JSON(http.StatusBadRequest, "user not found, unauthorized")
		return
	}

	//check if the food exist:
	food, err := fo.foodApp.GetFood(foodId)
	if err != nil {
		c.JSON(http.StatusNotFound, err.Error())
		return
	}
	//if the user id doesnt match with the one we have, dont update. This is the case where an authenticated user tries to update someone else post using postman, curl, etc
	if user.ID != food.UserID {
		c.JSON(http.StatusUnauthorized, "you are not the owner of this food")
		return
	}
	//Since this is an update request,  a new image may or may not be given.
	// If not image is given, an error occurs. We know this that is why we ignored the error and instead check if the file is nil.
	// if not nil, we process the file by calling the "UploadFile" method.
	// if nil, we used the old one whose path is saved in the database
	file, _ := c.FormFile("food_image")
	if file != nil {
		food.FoodImage, err = fo.fileUpload.UploadFile(file)
		//since i am using Digital Ocean(DO) Spaces to save image, i am appending my DO url here. You can comment this line since you may be using Digital Ocean Spaces.
		food.FoodImage = os.Getenv("DO_SPACES_URL") + food.FoodImage
		if err != nil {
			c.JSON(http.StatusUnprocessableEntity, gin.H{
				"upload_err": err.Error(),
			})
			return
		}
	}
	//we dont need to update user's id
	food.Title = title
	food.Description = description
	food.UpdatedAt = time.Now()
	updatedFood, dbUpdateErr := fo.foodApp.UpdateFood(food)
	if dbUpdateErr != nil {
		c.JSON(http.StatusInternalServerError, dbUpdateErr)
		return
	}
	c.JSON(http.StatusOK, updatedFood)
}

func (fo *Food) GetAllFood(c *gin.Context) {
	allfood, err := fo.foodApp.GetAllFood()
	if err != nil {
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusOK, allfood)
}

func (fo *Food) GetFoodAndCreator(c *gin.Context) {
	foodId, err := strconv.ParseUint(c.Param("food_id"), 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, "invalid request")
		return
	}
	food, err := fo.foodApp.GetFood(foodId)
	if err != nil {
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	user, err := fo.userApp.GetUser(food.UserID)
	if err != nil {
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	foodAndUser := map[string]interface{}{
		"food":    food,
		"creator": user.PublicUser(),
	}
	c.JSON(http.StatusOK, foodAndUser)
}

func (fo *Food) DeleteFood(c *gin.Context) {
	metadata, err := fo.tk.ExtractTokenMetadata(c.Request)
	if err != nil {
		c.JSON(http.StatusUnauthorized, "Unauthorized")
		return
	}
	foodId, err := strconv.ParseUint(c.Param("food_id"), 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, "invalid request")
		return
	}
	_, err = fo.userApp.GetUser(metadata.UserId)
	if err != nil {
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	err = fo.foodApp.DeleteFood(foodId)
	if err != nil {
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusOK, "food deleted")
}
```

## File: `interfaces/food_handler_test.go`
```go
package interfaces

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"food-app/domain/entity"
	"food-app/infrastructure/auth"
	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/assert"
	"io"
	"mime/multipart"
	"net/http"
	"net/http/httptest"
	"os"
	"strconv"
	"testing"
)

//IF YOU HAVE TIME, YOU CAN TEST ALL FAILURE CASES TO IMPROVE COVERAGE

func Test_SaveFood_Invalid_Data(t *testing.T) {
	//Mock extracting metadata
	fakeToken.ExtractTokenMetadataFn = func(r *http.Request) (*auth.AccessDetails, error) {
		return &auth.AccessDetails{
			TokenUuid: "0237817a-1546-4ca3-96a4-17621c237f6b",
			UserId:    1,
		}, nil
	}
	//Mocking the fetching of token metadata from redis
	fakeAuth.FetchAuthFn = func(uuid string) (uint64, error) {
		return 1, nil
	}
	samples := []struct {
		inputJSON  string
		statusCode int
	}{
		{
			//when the title is empty
			inputJSON:  `{"title": "", "description": "the desc"}`,
			statusCode: 422,
		},
		{
			//the description is empty
			inputJSON:  `{"title": "the title", "description": ""}`,
			statusCode: 422,
		},
		{
			//both the title and the description are empty
			inputJSON:  `{"title": "", "description": ""}`,
			statusCode: 422,
		},
		{
			//When invalid data is passed, e.g, instead of an integer, a string is passed
			inputJSON:  `{"title": 12344, "description": "the desc"}`,
			statusCode: 422,
		},
		{
			//When invalid data is passed, e.g, instead of an integer, a string is passed
			inputJSON:  `{"title": "hello title", "description": 3242342}`,
			statusCode: 422,
		},
	}

	for _, v := range samples {
		//use a valid token that has not expired. This token was created to live forever, just for test purposes with the user id of 1. This is so that it can always be used to run tests
		token := "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjgyYTM3YWE5LTI4MGMtNDQ2OC04M2RmLTZiOGYyMDIzODdkMyIsImF1dGhvcml6ZWQiOnRydWUsInVzZXJfaWQiOjF9.ESelxq-UHormgXUwRNe4_Elz2i__9EKwCXPsNCyKV5o"
		tokenString := fmt.Sprintf("Bearer %v", token)

		r := gin.Default()
		r.POST("/food", f.SaveFood)
		req, err := http.NewRequest(http.MethodPost, "/food", bytes.NewBufferString(v.inputJSON))
		if err != nil {
			t.Errorf("this is the error: %v\n", err)
		}
		req.Header.Set("Authorization", tokenString)

		rr := httptest.NewRecorder()
		r.ServeHTTP(rr, req)

		validationErr := make(map[string]string)

		err = json.Unmarshal(rr.Body.Bytes(), &validationErr)
		if err != nil {
			t.Errorf("error unmarshalling error %s\n", err)
		}
		assert.Equal(t, rr.Code, v.statusCode)

		if validationErr["title_required"] != "" {
			assert.Equal(t, validationErr["title_required"], "title is required")
		}
		if validationErr["description_required"] != "" {
			assert.Equal(t, validationErr["description_required"], "description is required")
		}
		if validationErr["title_required"] != "" && validationErr["description_required"] != "" {
			assert.Equal(t, validationErr["title_required"], "title is required")
			assert.Equal(t, validationErr["description_required"], "description is required")
		}
		if validationErr["invalid_json"] != "" {
			assert.Equal(t, validationErr["invalid_json"], "invalid json")
		}
	}
}

func TestSaverFood_Success(t *testing.T) {

	//Mock extracting metadata
	fakeToken.ExtractTokenMetadataFn = func(r *http.Request) (*auth.AccessDetails, error) {
		return &auth.AccessDetails{
			TokenUuid: "0237817a-1546-4ca3-96a4-17621c237f6b",
			UserId:    1,
		}, nil
	}
	//Mocking the fetching of token metadata from redis
	fakeAuth.FetchAuthFn = func(uuid string) (uint64, error) {
		return 1, nil
	}
	userApp.GetUserFn = func(uint64) (*entity.User, error) {
		//remember we are running sensitive info such as email and password
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
		}, nil
	}
	//Mocking file upload to DigitalOcean
	fakeUpload.UploadFileFn = func(file *multipart.FileHeader) (string, error) {
		return "dbdbf-dhbfh-bfy34-34jh-fd.jpg", nil //this is fabricated
	}
	//Mocking The Food return from db
	foodApp.SaveFoodFn = func(*entity.Food) (*entity.Food, map[string]string) {
		return &entity.Food{
			ID:          1,
			UserID:      1,
			Title:       "Food title",
			Description: "Food description",
			FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd.jpg",
		}, nil
	}
	image := "./../utils/test_images/amala.jpg" //this is where the image is located
	file, err := os.Open(image)
	if err != nil {
		t.Errorf("Cannot open file: %s\n", err)
	}
	defer file.Close()

	//Create a buffer to store our request body as bytes
	var requestBody bytes.Buffer

	//Create a multipart writer
	multipartWriter := multipart.NewWriter(&requestBody)

	//Initialize the file field
	fileWriter, err := multipartWriter.CreateFormFile("food_image", "amala.jpg")
	if err != nil {
		t.Errorf("Cannot write file: %s\n", err)
	}
	//Copy the actual content to the file field's writer, though this is not needed, since files are sent to DigitalOcean
	_, err = io.Copy(fileWriter, file)
	if err != nil {
		t.Errorf("Cannot copy file: %s\n", err)
	}
	//Add the title and the description fields
	fileWriter, err = multipartWriter.CreateFormField("title")
	if err != nil {
		t.Errorf("Cannot write title: %s\n", err)
	}
	_, err = fileWriter.Write([]byte("Food title"))
	if err != nil {
		t.Errorf("Cannot write title value: %s\n", err)
	}
	fileWriter, err = multipartWriter.CreateFormField("description")
	if err != nil {
		t.Errorf("Cannot write description: %s\n", err)
	}
	_, err = fileWriter.Write([]byte("Food description"))
	if err != nil {
		t.Errorf("Cannot write description value: %s\n", err)
	}
	//Close the multipart writer so it writes the ending boundary
	multipartWriter.Close()

	//This can be anything, since we have already mocked the method that checks if the token is valid or not and have told it what to return for us.
	token := "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjgyYTM3YWE5LTI4MGMtNDQ2OC04M2RmLTZiOGYyMDIzODdkMyIsImF1dGhvcml6ZWQiOnRydWUsInVzZXJfaWQiOjF9.ESelxq-UHormgXUwRNe4_Elz2i__9EKwCXPsNCyKV5o"

	tokenString := fmt.Sprintf("Bearer %v", token)

	req, err := http.NewRequest(http.MethodPost, "/food", &requestBody)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	r := gin.Default()
	r.POST("/food", f.SaveFood)
	req.Header.Set("Authorization", tokenString)
	req.Header.Set("Content-Type", multipartWriter.FormDataContentType()) //this is important
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	var food = entity.Food{}
	err = json.Unmarshal(rr.Body.Bytes(), &food)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	assert.Equal(t, rr.Code, 201)
	assert.EqualValues(t, food.ID, 1)
	assert.EqualValues(t, food.UserID, 1)
	assert.EqualValues(t, food.Title, "Food title")
	assert.EqualValues(t, food.Description, "Food description")
	assert.EqualValues(t, food.FoodImage, "dbdbf-dhbfh-bfy34-34jh-fd.jpg")
}

//When wrong token is provided
func TestSaverFood_Unauthorized(t *testing.T) {
	//Mock extracting metadata
	fakeToken.ExtractTokenMetadataFn = func(r *http.Request) (*auth.AccessDetails, error) {
		return nil, errors.New("unauthorized")
	}

	image := "./../utils/test_images/amala.jpg" //this is where the image is located
	file, err := os.Open(image)
	if err != nil {
		t.Errorf("Cannot open file: %s\n", err)
	}
	defer file.Close()

	//Create a buffer to store our request body as bytes
	var requestBody bytes.Buffer

	//Create a multipart writer
	multipartWriter := multipart.NewWriter(&requestBody)

	//Initialize the file field
	fileWriter, err := multipartWriter.CreateFormFile("food_image", "amala.jpg")
	if err != nil {
		t.Errorf("Cannot write file: %s\n", err)
	}
	//Copy the actual content to the file field's writer, though this is not needed, since files are sent to DigitalOcean
	_, err = io.Copy(fileWriter, file)
	if err != nil {
		t.Errorf("Cannot copy file: %s\n", err)
	}
	//Add the title and the description fields
	fileWriter, err = multipartWriter.CreateFormField("title")
	if err != nil {
		t.Errorf("Cannot write title: %s\n", err)
	}
	_, err = fileWriter.Write([]byte("Food title"))
	if err != nil {
		t.Errorf("Cannot write title value: %s\n", err)
	}
	fileWriter, err = multipartWriter.CreateFormField("description")
	if err != nil {
		t.Errorf("Cannot write description: %s\n", err)
	}
	_, err = fileWriter.Write([]byte("Food description"))
	if err != nil {
		t.Errorf("Cannot write description value: %s\n", err)
	}
	//Close the multipart writer so it writes the ending boundary
	multipartWriter.Close()

	token := "wrong-token-string"

	tokenString := fmt.Sprintf("Bearer %v", token)

	req, err := http.NewRequest(http.MethodPost, "/food", &requestBody)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	r := gin.Default()
	r.POST("/food", f.SaveFood)
	req.Header.Set("Authorization", tokenString)
	req.Header.Set("Content-Type", multipartWriter.FormDataContentType()) //this is important
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	var errResp = ""
	err = json.Unmarshal(rr.Body.Bytes(), &errResp)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	assert.Equal(t, rr.Code, 401)
	assert.EqualValues(t, errResp, "unauthorized")
}

func TestGetAllFood_Success(t *testing.T) {
	//application.FoodApp = &fakeFoodApp{} //make it possible to change real method with fake

	//Return Food to check for, with our mock
	foodApp.GetAllFoodFn = func() ([]entity.Food, error) {
		return []entity.Food{
			{
				ID:          1,
				UserID:      1,
				Title:       "Food title",
				Description: "Food description",
				FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd.jpg",
			},
			{
				ID:          2,
				UserID:      2,
				Title:       "Food title second",
				Description: "Food description second",
				FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd-second.jpg",
			},
		}, nil
	}
	req, err := http.NewRequest(http.MethodGet, "/food", nil)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	r := gin.Default()
	r.GET("/food", f.GetAllFood)
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	var food []entity.Food
	err = json.Unmarshal(rr.Body.Bytes(), &food)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	assert.Equal(t, rr.Code, 200)
	assert.EqualValues(t, len(food), 2)
}

func TestGetFoodAndCreator_Success(t *testing.T) {

	userApp.GetUserFn = func(uint64) (*entity.User, error) {
		//remember we are running sensitive info such as email and password
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
		}, nil
	}
	//Return Food to check for, with our mock
	foodApp.GetFoodFn = func(uint64) (*entity.Food, error) {
		return &entity.Food{
			ID:          1,
			UserID:      1,
			Title:       "Food title",
			Description: "Food description",
			FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd.jpg",
		}, nil
	}
	foodID := strconv.Itoa(1)
	req, err := http.NewRequest(http.MethodGet, "/food/"+foodID, nil)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	r := gin.Default()
	r.GET("/food/:food_id", f.GetFoodAndCreator)
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	var foodAndCreator = make(map[string]interface{})
	err = json.Unmarshal(rr.Body.Bytes(), &foodAndCreator)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	food := foodAndCreator["food"].(map[string]interface{})
	creator := foodAndCreator["creator"].(map[string]interface{})

	assert.Equal(t, rr.Code, 200)

	assert.EqualValues(t, food["title"], "Food title")
	assert.EqualValues(t, food["description"], "Food description")
	assert.EqualValues(t, food["food_image"], "dbdbf-dhbfh-bfy34-34jh-fd.jpg")

	assert.EqualValues(t, creator["first_name"], "victor")
	assert.EqualValues(t, creator["last_name"], "steven")
}

func TestUpdateFood_Success_With_File(t *testing.T) {

	//Mock extracting metadata
	fakeToken.ExtractTokenMetadataFn = func(r *http.Request) (*auth.AccessDetails, error) {
		return &auth.AccessDetails{
			TokenUuid: "0237817a-1546-4ca3-96a4-17621c237f6b",
			UserId:    1,
		}, nil
	}
	//Mocking the fetching of token metadata from redis
	fakeAuth.FetchAuthFn = func(uuid string) (uint64, error) {
		return 1, nil
	}
	userApp.GetUserFn = func(uint64) (*entity.User, error) {
		//remember we are running sensitive info such as email and password
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
		}, nil
	}
	//Return Food to check for, with our mock
	foodApp.GetFoodFn = func(uint64) (*entity.Food, error) {
		return &entity.Food{
			ID:          1,
			UserID:      1,
			Title:       "Food title",
			Description: "Food description",
			FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd.jpg",
		}, nil
	}
	//Mocking The Food return from db
	foodApp.UpdateFoodFn = func(*entity.Food) (*entity.Food, map[string]string) {
		return &entity.Food{
			ID:          1,
			UserID:      1,
			Title:       "Food title updated",
			Description: "Food description updated",
			FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd-updated.jpg",
		}, nil
	}

	//Mocking file upload to DigitalOcean
	fakeUpload.UploadFileFn = func(file *multipart.FileHeader) (string, error) {
		return "dbdbf-dhbfh-bfy34-34jh-fd-updated.jpg", nil //this is fabricated
	}

	image := "./../utils/test_images/new_meal.jpeg" //this is where the image is located
	file, err := os.Open(image)
	if err != nil {
		t.Errorf("Cannot open file: %s\n", err)
	}
	defer file.Close()

	//Create a buffer to store our request body as bytes
	var requestBody bytes.Buffer

	//Create a multipart writer
	multipartWriter := multipart.NewWriter(&requestBody)

	//Initialize the file field
	fileWriter, err := multipartWriter.CreateFormFile("food_image", "new_meal.jpeg")
	if err != nil {
		t.Errorf("Cannot write file: %s\n", err)
	}
	//Copy the actual content to the file field's writer, though this is not needed, since files are sent to DigitalOcean
	_, err = io.Copy(fileWriter, file)
	if err != nil {
		t.Errorf("Cannot copy file: %s\n", err)
	}
	//Add the title and the description fields
	fileWriter, err = multipartWriter.CreateFormField("title")
	if err != nil {
		t.Errorf("Cannot write title: %s\n", err)
	}
	_, err = fileWriter.Write([]byte("Food title updated"))
	if err != nil {
		t.Errorf("Cannot write title value: %s\n", err)
	}
	fileWriter, err = multipartWriter.CreateFormField("description")
	if err != nil {
		t.Errorf("Cannot write description: %s\n", err)
	}
	_, err = fileWriter.Write([]byte("Food description updated"))
	if err != nil {
		t.Errorf("Cannot write description value: %s\n", err)
	}
	//Close the multipart writer so it writes the ending boundary
	multipartWriter.Close()

	//This can be anything, since we have already mocked the method that checks if the token is valid or not and have told it what to return for us.
	token := "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjgyYTM3YWE5LTI4MGMtNDQ2OC04M2RmLTZiOGYyMDIzODdkMyIsImF1dGhvcml6ZWQiOnRydWUsInVzZXJfaWQiOjF9.ESelxq-UHormgXUwRNe4_Elz2i__9EKwCXPsNCyKV5o"

	tokenString := fmt.Sprintf("Bearer %v", token)

	foodID := strconv.Itoa(1)
	req, err := http.NewRequest(http.MethodPut, "/food/"+foodID, &requestBody)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	r := gin.Default()
	r.PUT("/food/:food_id", f.UpdateFood)
	req.Header.Set("Authorization", tokenString)
	req.Header.Set("Content-Type", multipartWriter.FormDataContentType()) //this is important
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	var food = entity.Food{}
	err = json.Unmarshal(rr.Body.Bytes(), &food)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	assert.Equal(t, rr.Code, 200)
	assert.EqualValues(t, food.ID, 1)
	assert.EqualValues(t, food.UserID, 1)
	assert.EqualValues(t, food.Title, "Food title updated")
	assert.EqualValues(t, food.Description, "Food description updated")
	assert.EqualValues(t, food.FoodImage, "dbdbf-dhbfh-bfy34-34jh-fd-updated.jpg")
}

//This is where file is not updated. A user can choose not to update file, in that case, the old file will still be used
func TestUpdateFood_Success_Without_File(t *testing.T) {

	//Mock extracting metadata
	fakeToken.ExtractTokenMetadataFn = func(r *http.Request) (*auth.AccessDetails, error) {
		return &auth.AccessDetails{
			TokenUuid: "0237817a-1546-4ca3-96a4-17621c237f6b",
			UserId:    1,
		}, nil
	}
	//Mocking the fetching of token metadata from redis
	fakeAuth.FetchAuthFn = func(uuid string) (uint64, error) {
		return 1, nil
	}
	userApp.GetUserFn = func(uint64) (*entity.User, error) {
		//remember we are running sensitive info such as email and password
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
		}, nil
	}
	//Return Food to check for, with our mock
	foodApp.GetFoodFn = func(uint64) (*entity.Food, error) {
		return &entity.Food{
			ID:          1,
			UserID:      1,
			Title:       "Food title",
			Description: "Food description",
			FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd-old-file.jpg",
		}, nil
	}
	//Mocking The Food return from db
	foodApp.UpdateFoodFn = func(*entity.Food) (*entity.Food, map[string]string) {
		return &entity.Food{
			ID:          1,
			UserID:      1,
			Title:       "Food title updated",
			Description: "Food description updated",
			FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd-old-file.jpg",
		}, nil
	}

	//Mocking file upload to DigitalOcean
	fakeUpload.UploadFileFn = func(file *multipart.FileHeader) (string, error) {
		return "dbdbf-dhbfh-bfy34-34jh-fd-old-file.jpg", nil //this is fabricated
	}

	//Create a buffer to store our request body as bytes
	var requestBody bytes.Buffer

	//Create a multipart writer
	multipartWriter := multipart.NewWriter(&requestBody)

	//Add the title and the description fields
	fileWriter, err := multipartWriter.CreateFormField("title")
	if err != nil {
		t.Errorf("Cannot write title: %s\n", err)
	}
	_, err = fileWriter.Write([]byte("Food title updated"))
	if err != nil {
		t.Errorf("Cannot write title value: %s\n", err)
	}
	fileWriter, err = multipartWriter.CreateFormField("description")
	if err != nil {
		t.Errorf("Cannot write description: %s\n", err)
	}
	_, err = fileWriter.Write([]byte("Food description updated"))
	if err != nil {
		t.Errorf("Cannot write description value: %s\n", err)
	}
	//Close the multipart writer so it writes the ending boundary
	multipartWriter.Close()

	//This can be anything, since we have already mocked the method that checks if the token is valid or not and have told it what to return for us.
	token := "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjgyYTM3YWE5LTI4MGMtNDQ2OC04M2RmLTZiOGYyMDIzODdkMyIsImF1dGhvcml6ZWQiOnRydWUsInVzZXJfaWQiOjF9.ESelxq-UHormgXUwRNe4_Elz2i__9EKwCXPsNCyKV5o"

	tokenString := fmt.Sprintf("Bearer %v", token)

	foodID := strconv.Itoa(1)
	req, err := http.NewRequest(http.MethodPut, "/food/"+foodID, &requestBody)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	r := gin.Default()
	r.PUT("/food/:food_id", f.UpdateFood)
	req.Header.Set("Authorization", tokenString)
	req.Header.Set("Content-Type", multipartWriter.FormDataContentType()) //this is important
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	var food = entity.Food{}
	err = json.Unmarshal(rr.Body.Bytes(), &food)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	assert.Equal(t, rr.Code, 200)
	assert.EqualValues(t, food.ID, 1)
	assert.EqualValues(t, food.UserID, 1)
	assert.EqualValues(t, food.Title, "Food title updated")
	assert.EqualValues(t, food.Description, "Food description updated")
	assert.EqualValues(t, food.FoodImage, "dbdbf-dhbfh-bfy34-34jh-fd-old-file.jpg")
}

func TestUpdateFood_Invalid_Data(t *testing.T) {

	//Mock extracting metadata
	fakeToken.ExtractTokenMetadataFn = func(r *http.Request) (*auth.AccessDetails, error) {
		return &auth.AccessDetails{
			TokenUuid: "0237817a-1546-4ca3-96a4-17621c237f6b",
			UserId:    1,
		}, nil
	}
	//Mocking the fetching of token metadata from redis
	fakeAuth.FetchAuthFn = func(uuid string) (uint64, error) {
		return 1, nil
	}

	samples := []struct {
		inputJSON  string
		statusCode int
	}{
		{
			//when the title is empty
			inputJSON:  `{"title": "", "description": "the desc"}`,
			statusCode: 422,
		},
		{
			//the description is empty
			inputJSON:  `{"title": "the title", "description": ""}`,
			statusCode: 422,
		},
		{
			//both the title and the description are empty
			inputJSON:  `{"title": "", "description": ""}`,
			statusCode: 422,
		},
		{
			//When invalid data is passed, e.g, instead of an integer, a string is passed
			inputJSON:  `{"title": 12344, "description": "the desc"}`,
			statusCode: 422,
		},
		{
			//When invalid data is passed, e.g, instead of an integer, a string is passed
			inputJSON:  `{"title": "hello sir", "description": 3242342}`,
			statusCode: 422,
		},
	}

	for _, v := range samples {

		//use a valid token that has not expired. This token was created to live forever, just for test purposes with the user id of 1. This is so that it can always be used to run tests
		token := "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjgyYTM3YWE5LTI4MGMtNDQ2OC04M2RmLTZiOGYyMDIzODdkMyIsImF1dGhvcml6ZWQiOnRydWUsInVzZXJfaWQiOjF9.ESelxq-UHormgXUwRNe4_Elz2i__9EKwCXPsNCyKV5o"
		tokenString := fmt.Sprintf("Bearer %v", token)

		foodID := strconv.Itoa(1)

		r := gin.Default()
		r.POST("/food/:food_id", f.UpdateFood)
		req, err := http.NewRequest(http.MethodPost, "/food/"+foodID, bytes.NewBufferString(v.inputJSON))
		if err != nil {
			t.Errorf("this is the error: %v\n", err)
		}
		req.Header.Set("Authorization", tokenString)

		rr := httptest.NewRecorder()
		r.ServeHTTP(rr, req)

		validationErr := make(map[string]string)

		err = json.Unmarshal(rr.Body.Bytes(), &validationErr)
		if err != nil {
			t.Errorf("error unmarshalling error %s\n", err)
		}
		assert.Equal(t, rr.Code, v.statusCode)

		if validationErr["title_required"] != "" {
			assert.Equal(t, validationErr["title_required"], "title is required")
		}
		if validationErr["description_required"] != "" {
			assert.Equal(t, validationErr["description_required"], "description is required")
		}
		if validationErr["title_required"] != "" && validationErr["description_required"] != "" {
			assert.Equal(t, validationErr["title_required"], "title is required")
			assert.Equal(t, validationErr["description_required"], "description is required")
		}
		if validationErr["invalid_json"] != "" {
			assert.Equal(t, validationErr["invalid_json"], "invalid json")
		}
	}
}

func TestDeleteFood_Success(t *testing.T) {
	//Mock extracting metadata
	fakeToken.ExtractTokenMetadataFn = func(r *http.Request) (*auth.AccessDetails, error) {
		return &auth.AccessDetails{
			TokenUuid: "0237817a-1546-4ca3-96a4-17621c237f6b",
			UserId:    1,
		}, nil
	}
	//Mocking the fetching of token metadata from redis
	fakeAuth.FetchAuthFn = func(uuid string) (uint64, error) {
		return 1, nil
	}
	//Return Food to check for, with our mock
	foodApp.GetFoodFn = func(uint64) (*entity.Food, error) {
		return &entity.Food{
			ID:          1,
			UserID:      1,
			Title:       "Food title",
			Description: "Food description",
			FoodImage:   "dbdbf-dhbfh-bfy34-34jh-fd-old-file.jpg",
		}, nil
	}
	userApp.GetUserFn = func(uint64) (*entity.User, error) {
		//remember we are running sensitive info such as email and password
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
		}, nil
	}
	//The deleted food mock:
	foodApp.DeleteFoodFn = func(uint64) error {
		return nil
	}

	//This can be anything, since we have already mocked the method that checks if the token is valid or not and have told it what to return for us.
	token := "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjgyYTM3YWE5LTI4MGMtNDQ2OC04M2RmLTZiOGYyMDIzODdkMyIsImF1dGhvcml6ZWQiOnRydWUsInVzZXJfaWQiOjF9.ESelxq-UHormgXUwRNe4_Elz2i__9EKwCXPsNCyKV5o"

	tokenString := fmt.Sprintf("Bearer %v", token)

	foodId := strconv.Itoa(1)
	req, err := http.NewRequest(http.MethodDelete, "/food/"+foodId, nil)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	r := gin.Default()
	r.DELETE("/food/:food_id", f.DeleteFood)
	req.Header.Set("Authorization", tokenString)
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	response := ""

	err = json.Unmarshal(rr.Body.Bytes(), &response)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	assert.Equal(t, rr.Code, 200)
	assert.EqualValues(t, response, "food deleted")
}
```

## File: `interfaces/handler_setup_test.go`
```go
package interfaces

import "food-app/utils/mock"

var (
	userApp    mock.UserAppInterface
	foodApp    mock.FoodAppInterface
	fakeUpload mock.UploadFileInterface
	fakeAuth   mock.AuthInterface
	fakeToken  mock.TokenInterface

	s  = NewUsers(&userApp, &fakeAuth, &fakeToken)                       //We use all mocked data here
	f  = NewFood(&foodApp, &userApp, &fakeUpload, &fakeAuth, &fakeToken) //We use all mocked data here
	au = NewAuthenticate(&userApp, &fakeAuth, &fakeToken)                //We use all mocked data here

)
```

## File: `interfaces/login_handler.go`
```go
package interfaces

import (
	"fmt"
	"food-app/application"
	"food-app/domain/entity"
	"food-app/infrastructure/auth"
	"github.com/dgrijalva/jwt-go"
	"github.com/gin-gonic/gin"
	"net/http"
	"os"
	"strconv"
)

type Authenticate struct {
	us application.UserAppInterface
	rd auth.AuthInterface
	tk auth.TokenInterface
}

//Authenticate constructor
func NewAuthenticate(uApp application.UserAppInterface, rd auth.AuthInterface, tk auth.TokenInterface) *Authenticate {
	return &Authenticate{
		us: uApp,
		rd: rd,
		tk: tk,
	}
}

func (au *Authenticate) Login(c *gin.Context) {
	var user *entity.User
	var tokenErr = map[string]string{}

	if err := c.ShouldBindJSON(&user); err != nil {
		c.JSON(http.StatusUnprocessableEntity, "Invalid json provided")
		return
	}
	//validate request:
	validateUser := user.Validate("login")
	if len(validateUser) > 0 {
		c.JSON(http.StatusUnprocessableEntity, validateUser)
		return
	}
	u, userErr := au.us.GetUserByEmailAndPassword(user)
	if userErr != nil {
		c.JSON(http.StatusInternalServerError, userErr)
		return
	}
	ts, tErr := au.tk.CreateToken(u.ID)
	if tErr != nil {
		tokenErr["token_error"] = tErr.Error()
		c.JSON(http.StatusUnprocessableEntity, tErr.Error())
		return
	}
	saveErr := au.rd.CreateAuth(u.ID, ts)
	if saveErr != nil {
		c.JSON(http.StatusInternalServerError, saveErr.Error())
		return
	}
	userData := make(map[string]interface{})
	userData["access_token"] = ts.AccessToken
	userData["refresh_token"] = ts.RefreshToken
	userData["id"] = u.ID
	userData["first_name"] = u.FirstName
	userData["last_name"] = u.LastName

	c.JSON(http.StatusOK, userData)
}

func (au *Authenticate) Logout(c *gin.Context) {
	//check is the user is authenticated first
	metadata, err := au.tk.ExtractTokenMetadata(c.Request)
	if err != nil {
		c.JSON(http.StatusUnauthorized, "Unauthorized")
		return
	}
	//if the access token exist and it is still valid, then delete both the access token and the refresh token
	deleteErr := au.rd.DeleteTokens(metadata)
	if deleteErr != nil {
		c.JSON(http.StatusUnauthorized, deleteErr.Error())
		return
	}
	c.JSON(http.StatusOK, "Successfully logged out")
}

//Refresh is the function that uses the refresh_token to generate new pairs of refresh and access tokens.
func (au *Authenticate) Refresh(c *gin.Context) {
	mapToken := map[string]string{}
	if err := c.ShouldBindJSON(&mapToken); err != nil {
		c.JSON(http.StatusUnprocessableEntity, err.Error())
		return
	}
	refreshToken := mapToken["refresh_token"]

	//verify the token
	token, err := jwt.Parse(refreshToken, func(token *jwt.Token) (interface{}, error) {
		//Make sure that the token method conform to "SigningMethodHMAC"
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
		}
		return []byte(os.Getenv("REFRESH_SECRET")), nil
	})
	//any error may be due to token expiration
	if err != nil {
		c.JSON(http.StatusUnauthorized, err.Error())
		return
	}
	//is token valid?
	if _, ok := token.Claims.(jwt.Claims); !ok && !token.Valid {
		c.JSON(http.StatusUnauthorized, err)
		return
	}
	//Since token is valid, get the uuid:
	claims, ok := token.Claims.(jwt.MapClaims)
	if ok && token.Valid {
		refreshUuid, ok := claims["refresh_uuid"].(string) //convert the interface to string
		if !ok {
			c.JSON(http.StatusUnprocessableEntity, "Cannot get uuid")
			return
		}
		userId, err := strconv.ParseUint(fmt.Sprintf("%.f", claims["user_id"]), 10, 64)
		if err != nil {
			c.JSON(http.StatusUnprocessableEntity, "Error occurred")
			return
		}
		//Delete the previous Refresh Token
		delErr := au.rd.DeleteRefresh(refreshUuid)
		if delErr != nil { //if any goes wrong
			c.JSON(http.StatusUnauthorized, "unauthorized")
			return
		}
		//Create new pairs of refresh and access tokens
		ts, createErr := au.tk.CreateToken(userId)
		if createErr != nil {
			c.JSON(http.StatusForbidden, createErr.Error())
			return
		}
		//save the tokens metadata to redis
		saveErr := au.rd.CreateAuth(userId, ts)
		if saveErr != nil {
			c.JSON(http.StatusForbidden, saveErr.Error())
			return
		}
		tokens := map[string]string{
			"access_token":  ts.AccessToken,
			"refresh_token": ts.RefreshToken,
		}
		c.JSON(http.StatusCreated, tokens)
	} else {
		c.JSON(http.StatusUnauthorized, "refresh token expired")
	}
}
```

## File: `interfaces/login_handler_test.go`
```go
package interfaces

import (
	"bytes"
	"encoding/json"
	"fmt"
	"food-app/domain/entity"
	"food-app/infrastructure/auth"
	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/assert"
	"net/http"
	"net/http/httptest"
	"os"
	"testing"
)

//IF YOU HAVE TIME, YOU CAN TEST ALL FAILURE CASES TO IMPROVE COVERAGE

//We dont need to mock the application layer, because we won't get there. So we will use table test to cover all validation errors
func Test_Login_Invalid_Data(t *testing.T) {
	samples := []struct {
		inputJSON  string
		statusCode int
	}{
		{
			//empty email
			inputJSON:  `{"email": "","password": "password"}`,
			statusCode: 422,
		},
		{
			//empty password
			inputJSON:  `{"email": "steven@example.com","password": ""}`,
			statusCode: 422,
		},
		{
			//invalid email
			inputJSON:  `{"email": "stevenexample.com","password": ""}`,
			statusCode: 422,
		},
	}

	for _, v := range samples {

		r := gin.Default()
		r.POST("/login", au.Login)
		req, err := http.NewRequest(http.MethodPost, "/login", bytes.NewBufferString(v.inputJSON))
		if err != nil {
			t.Errorf("this is the error: %v\n", err)
		}
		rr := httptest.NewRecorder()
		r.ServeHTTP(rr, req)

		validationErr := make(map[string]string)

		err = json.Unmarshal(rr.Body.Bytes(), &validationErr)
		if err != nil {
			t.Errorf("error unmarshalling error %s\n", err)
		}
		assert.Equal(t, rr.Code, v.statusCode)

		if validationErr["email_required"] != "" {
			assert.Equal(t, validationErr["email_required"], "email is required")
		}
		if validationErr["invalid_email"] != "" {
			assert.Equal(t, validationErr["invalid_email"], "please provide a valid email")
		}
		if validationErr["password_required"] != "" {
			assert.Equal(t, validationErr["password_required"], "password is required")
		}
	}
}

func Test_Login_Success(t *testing.T) {

	userApp.GetUserByEmailAndPasswordFn = func(*entity.User) (*entity.User, map[string]string) {
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
		}, nil
	}
	fakeToken.CreateTokenFn = func(userid uint64) (*auth.TokenDetails, error) {
		return &auth.TokenDetails{
			AccessToken:  "this-is-the-access-token",
			RefreshToken: "this-is-the-refresh-token",
			TokenUuid:    "dfsdf-342-34-23-4234-234",
			RefreshUuid:  "sfd-3234-sdfew-34234-df3",
			AtExpires:    12345,
			RtExpires:    1234555,
		}, nil
	}
	fakeAuth.CreateAuthFn = func(uint64, *auth.TokenDetails) error {
		return nil
	}

	inputJSON := `{"email": "steven@example.com","password": "password"}`
	r := gin.Default()
	r.POST("/login", au.Login)
	req, err := http.NewRequest(http.MethodPost, "/login", bytes.NewBufferString(inputJSON))
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	fmt.Println("The response: ", string(rr.Body.Bytes()))

	response := make(map[string]interface{})

	err = json.Unmarshal(rr.Body.Bytes(), &response)
	if err != nil {
		t.Errorf("error unmarshalling error %s\n", err)
	}
	assert.Equal(t, rr.Code, http.StatusOK)
	assert.EqualValues(t, response["access_token"], "this-is-the-access-token")
	assert.EqualValues(t, response["refresh_token"], "this-is-the-refresh-token")
	assert.EqualValues(t, response["first_name"], "victor")
	assert.EqualValues(t, response["last_name"], "steven")
}

func TestLogout_Success(t *testing.T) {
	//Mock extracting metadata
	fakeToken.ExtractTokenMetadataFn = func(r *http.Request) (*auth.AccessDetails, error) {
		return &auth.AccessDetails{
			TokenUuid: "0237817a-1546-4ca3-96a4-17621c237f6b",
			UserId:    1,
		}, nil
	}
	//Mock the methods that Logout depend on
	fakeAuth.DeleteTokensFn = func(*auth.AccessDetails) error {
		return nil
	}
	//This can be anything, since we have already mocked the method that checks if the token is valid or not and have told it what to return for us.
	token := "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6IjgyYTM3YWE5LTI4MGMtNDQ2OC04M2RmLTZiOGYyMDIzODdkMyIsImF1dGhvcml6ZWQiOnRydWUsInVzZXJfaWQiOjF9.ESelxq-UHormgXUwRNe4_Elz2i__9EKwCXPsNCyKV5o"

	tokenString := fmt.Sprintf("Bearer %v", token)

	req, err := http.NewRequest(http.MethodPost, "/logout", nil)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	r := gin.Default()
	r.POST("/logout", au.Logout)
	req.Header.Set("Authorization", tokenString)
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	response := ""
	err = json.Unmarshal(rr.Body.Bytes(), &response)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	assert.EqualValues(t, rr.Code, http.StatusOK)
	assert.EqualValues(t, response, "Successfully logged out")
}

func TestRefresh_Success(t *testing.T) {

	fakeAuth.DeleteRefreshFn = func(string) error {
		return nil
	}
	fakeToken.CreateTokenFn = func(userid uint64) (*auth.TokenDetails, error) {
		return &auth.TokenDetails{
			AccessToken:  "this-is-the-NEW-access-token",
			RefreshToken: "this-is-the-NEW-refresh-token",
			TokenUuid:    "dfsdf-342-34-23-4234-234",
			RefreshUuid:  "sfd-3234-sdfew-34234-df3",
			AtExpires:    12345,
			RtExpires:    1234555,
		}, nil
	}
	fakeAuth.CreateAuthFn = func(uint64, *auth.TokenDetails) error {
		return nil
	}

	r := gin.Default()
	r.POST("/refresh", au.Refresh)

	//Note that since we will be cheking this token, A secret is needed. THis secret was used to create the token,
	//lets set it, so that this test can retrieve it. Setting it this way we save us from importing the .env, which we dont really need.
	os.Setenv("REFRESH_SECRET", "786dfdbjhsb")

	inputJSON := `{
		"refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWZyZXNoX3V1aWQiOiI4MzJjODgyMS0wMzUyLTRjN2EtOTZjNi04MzM5YzBlZjJkZTkrKzE0IiwidXNlcl9pZCI6MTR9.Sd6IOmvbgwf825jlQxt7A-sDpOK1vubUVoxCQuvtC_A"
		}`
	req, err := http.NewRequest(http.MethodPost, "/refresh", bytes.NewBufferString(inputJSON))
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	fmt.Println("the response: ", string(rr.Body.Bytes()))

	tokens := make(map[string]string)
	err = json.Unmarshal(rr.Body.Bytes(), &tokens)
	if err != nil {
		t.Errorf("cannot unmarshal response: %v\n", err)
	}
	assert.Equal(t, 201, rr.Code)
	assert.EqualValues(t, "this-is-the-NEW-access-token", tokens["access_token"])
	assert.EqualValues(t, "this-is-the-NEW-refresh-token", tokens["refresh_token"])
}
```

## File: `interfaces/user_handler.go`
```go
package interfaces

import (
	"food-app/application"
	"food-app/domain/entity"
	"food-app/infrastructure/auth"
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
)

//Users struct defines the dependencies that will be used
type Users struct {
	us application.UserAppInterface
	rd auth.AuthInterface
	tk auth.TokenInterface
}

//Users constructor
func NewUsers(us application.UserAppInterface, rd auth.AuthInterface, tk auth.TokenInterface) *Users {
	return &Users{
		us: us,
		rd: rd,
		tk: tk,
	}
}

func (s *Users) SaveUser(c *gin.Context) {
	var user entity.User
	if err := c.ShouldBindJSON(&user); err != nil {
		c.JSON(http.StatusUnprocessableEntity, gin.H{
			"invalid_json": "invalid json",
		})
		return
	}
	//validate the request:
	validateErr := user.Validate("")
	if len(validateErr) > 0 {
		c.JSON(http.StatusUnprocessableEntity, validateErr)
		return
	}
	newUser, err := s.us.SaveUser(&user)
	if err != nil {
		c.JSON(http.StatusInternalServerError, err)
		return
	}
	c.JSON(http.StatusCreated, newUser.PublicUser())
}

func (s *Users) GetUsers(c *gin.Context) {
	users := entity.Users{} //customize user
	var err error
	//us, err = application.UserApp.GetUsers()
	users, err = s.us.GetUsers()
	if err != nil {
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusOK, users.PublicUsers())
}

func (s *Users) GetUser(c *gin.Context) {
	userId, err := strconv.ParseUint(c.Param("user_id"), 10, 64)
	if err != nil {
		c.JSON(http.StatusBadRequest, err.Error())
		return
	}
	user, err := s.us.GetUser(userId)
	if err != nil {
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusOK, user.PublicUser())
}
```

## File: `interfaces/user_handler_test.go`
```go
package interfaces

import (
	"bytes"
	"encoding/json"
	"fmt"
	"food-app/domain/entity"
	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/assert"
	"net/http"
	"net/http/httptest"
	"strconv"
	"testing"
)

//IF YOU HAVE TIME, YOU CAN TEST ALL FAILURE CASES TO IMPROVE COVERAGE

func TestSaveUser_Success(t *testing.T) {
	userApp.SaveUserFn = func(*entity.User) (*entity.User, map[string]string) {
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
		}, nil
	}

	r := gin.Default()
	r.POST("/users", s.SaveUser)
	inputJSON := `{
		"first_name": "victor",
		"last_name": "steven",
		"email": "steven@example.com",
		"password": "password"
	}`
	req, err := http.NewRequest(http.MethodPost, "/users", bytes.NewBufferString(inputJSON))
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	user := &entity.User{}

	err = json.Unmarshal(rr.Body.Bytes(), &user)

	assert.Equal(t, rr.Code, 201)
	assert.EqualValues(t, user.FirstName, "victor")
	assert.EqualValues(t, user.LastName, "steven")
}

//We dont need to mock the application layer, because we won't get there. So we will use table test to cover all validation errors
func Test_SaveUser_Invalidating_Data(t *testing.T) {
	samples := []struct {
		inputJSON  string
		statusCode int
	}{
		{
			inputJSON:  `{"first_name": "", "last_name": "steven","email": "steven@example.com","password": "password"}`,
			statusCode: 422,
		},
		{
			inputJSON:  `{"first_name": "victor", "last_name": "","email": "steven@example.com","password": "password"}`,
			statusCode: 422,
		},
		{
			inputJSON:  `{"first_name": "victor", "last_name": "steven","email": "","password": "password"}`,
			statusCode: 422,
		},
		{
			inputJSON:  `{"first_name": "victor", "last_name": "steven","email": "steven@example.com","password": ""}`,
			statusCode: 422,
		},
		{
			//invalid email
			inputJSON:  `{"email": "stevenexample.com","password": ""}`,
			statusCode: 422,
		},
		{
			//When instead a string an integer is supplied, When attempting to unmarshal input to the user struct, it will fail
			inputJSON:  `{"first_name": 1234, "last_name": "steven","email": "steven@example.com","password": "password"}`,
			statusCode: 422,
		},
	}

	for _, v := range samples {

		r := gin.Default()
		r.POST("/users", s.SaveUser)
		req, err := http.NewRequest(http.MethodPost, "/users", bytes.NewBufferString(v.inputJSON))
		if err != nil {
			t.Errorf("this is the error: %v\n", err)
		}
		rr := httptest.NewRecorder()
		r.ServeHTTP(rr, req)

		validationErr := make(map[string]string)

		err = json.Unmarshal(rr.Body.Bytes(), &validationErr)
		if err != nil {
			t.Errorf("error unmarshalling error %s\n", err)
		}
		fmt.Println("validator error: ", validationErr)
		assert.Equal(t, rr.Code, v.statusCode)

		if validationErr["email_required"] != "" {
			assert.Equal(t, validationErr["email_required"], "email is required")
		}
		if validationErr["invalid_email"] != "" {
			assert.Equal(t, validationErr["invalid_email"], "please provide a valid email")
		}
		if validationErr["firstname_required"] != "" {
			assert.Equal(t, validationErr["firstname_required"], "first name is required")
		}
		if validationErr["lastname_required"] != "" {
			assert.Equal(t, validationErr["lastname_required"], "last name is required")
		}
		if validationErr["password_required"] != "" {
			assert.Equal(t, validationErr["password_required"], "password is required")
		}
		if validationErr["invalid_json"] != "" {
			assert.Equal(t, validationErr["invalid_json"], "invalid json")
		}
	}
}

//One of such db error is invalid email, it return that from the application and test.
func TestSaveUser_DB_Error(t *testing.T) {
	//application.UserApp = &fakeUserApp{}
	userApp.SaveUserFn = func(*entity.User) (*entity.User, map[string]string) {
		return nil, map[string]string{
			"email_taken": "email already taken",
		}
	}
	r := gin.Default()
	r.POST("/users", s.SaveUser)
	inputJSON := `{
		"first_name": "victor",
		"last_name": "steven",
		"email": "steven@example.com",
		"password": "password"
	}`
	req, err := http.NewRequest(http.MethodPost, "/users", bytes.NewBufferString(inputJSON))
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	dbErr := make(map[string]string)
	err = json.Unmarshal(rr.Body.Bytes(), &dbErr)
	if err != nil {
		t.Errorf("cannot unmarshall payload to errMap: %s\n", err)
	}
	assert.Equal(t, rr.Code, 500)
	assert.EqualValues(t, dbErr["email_taken"], "email already taken")
}

////////////////////////////////////////////////////////////////

//GetUsers Test
func TestGetUsers_Success(t *testing.T) {
	userApp.GetUsersFn = func() ([]entity.User, error) {
		//remember we are running sensitive info such as email and password
		return []entity.User{
			{
				ID:        1,
				FirstName: "victor",
				LastName:  "steven",
			},
			{
				ID:        2,
				FirstName: "mike",
				LastName:  "ken",
			},
		}, nil
	}
	r := gin.Default()
	r.GET("/users", s.GetUsers)

	req, err := http.NewRequest(http.MethodGet, "/users", nil)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	var users []entity.User

	err = json.Unmarshal(rr.Body.Bytes(), &users)

	assert.Equal(t, rr.Code, 200)
	assert.EqualValues(t, len(users), 2)
}

///////////////////////////////////////////////////////////////

//GetUser Test
func TestGetUser_Success(t *testing.T) {
	//application.UserApp = &fakeUserApp{}
	userApp.GetUserFn = func(uint64) (*entity.User, error) {
		//remember we are running sensitive info such as email and password
		return &entity.User{
			ID:        1,
			FirstName: "victor",
			LastName:  "steven",
		}, nil
	}
	r := gin.Default()
	userId := strconv.Itoa(1)
	r.GET("/users/:user_id", s.GetUser)

	req, err := http.NewRequest(http.MethodGet, "/users/"+userId, nil)
	if err != nil {
		t.Errorf("this is the error: %v\n", err)
	}
	rr := httptest.NewRecorder()
	r.ServeHTTP(rr, req)

	var user *entity.User

	err = json.Unmarshal(rr.Body.Bytes(), &user)

	assert.Equal(t, rr.Code, 200)
	assert.EqualValues(t, user.FirstName, "victor")
	assert.EqualValues(t, user.LastName, "steven")
}
```

## File: `interfaces/fileupload/fileformat.go`
```go
package fileupload

import (
	"github.com/twinj/uuid"
	"path"
)

func FormatFile(fn string) string {

	ext := path.Ext(fn)
	u := uuid.NewV4()

	newFileName := u.String() + ext

	return newFileName
}
```

## File: `interfaces/fileupload/fileupload.go`
```go
package fileupload

import (
	"bytes"
	"errors"
	"fmt"
	"github.com/minio/minio-go/v6"
	"log"
	"mime/multipart"
	"net/http"
	"os"
	"strings"
)

func NewFileUpload() *fileUpload {
	return &fileUpload{}
}

type fileUpload struct{}

type UploadFileInterface interface {
	UploadFile(file *multipart.FileHeader) (string, error)
}

//So what is exposed is Uploader
var _ UploadFileInterface = &fileUpload{}

//func (fu *fileUpload) UploadFilex(file *multipart.FileHeader) (string, error) {
//	f, err := file.Open()
//	if err != nil {
//		return "", errors.New("cannot open file")
//	}
//	defer f.Close()
//
//	size := file.Size
//	//The image should not be more than 500KB
//	fmt.Println("the size: ", size)
//	if size > int64(512000) {
//		return "", errors.New("sorry, please upload an Image of 500KB or less")
//	}
//	//only the first 512 bytes are used to sniff the content type of a file,
//	//so, so no need to read the entire bytes of a file.
//	buffer := make([]byte, size)
//	f.Read(buffer)
//	fileType := http.DetectContentType(buffer)
//	//if the image is valid
//	if !strings.HasPrefix(fileType, "image") {
//		return "", errors.New("please upload a valid image")
//	}
//	fileBytes := bytes.NewReader(buffer)
//	filePath := FormatFile(file.Filename)
//	path := "/profile-photos/" + filePath
//
//	params := &s3.PutObjectInput{
//		Bucket:        aws.String("chodapi"), //this is the name i saved the bucket that contains the image
//		Key:           aws.String(path),
//		Body:          fileBytes,
//		ContentLength: aws.Int64(size),
//		ContentType:   aws.String(fileType),
//		ACL:           aws.String("public-read"),
//	}
//	s3Config := &aws.Config{
//		Credentials: credentials.NewStaticCredentials(
//			os.Getenv("DO_SPACES_KEY"), os.Getenv("DO_SPACES_SECRET"), os.Getenv("DO_SPACES_TOKEN")),
//		Endpoint: aws.String(os.Getenv("DO_SPACES_ENDPOINT")),
//		Region:   aws.String(os.Getenv("DO_SPACES_REGION")),
//	}
//	newSession := session.New(s3Config)
//	s3Client := s3.New(newSession)
//
//	_, err = s3Client.PutObject(params)
//	if err != nil {
//		fmt.Println("actual error: ", err)
//		return "", errors.New("something went wrong uploading image")
//	}
//	return filePath, nil
//}

func (fu *fileUpload) UploadFile(file *multipart.FileHeader) (string, error) {
	f, err := file.Open()
	if err != nil {
		return "", errors.New("cannot open file")
	}
	defer f.Close()

	size := file.Size
	//The image should not be more than 500KB
	fmt.Println("the size: ", size)
	if size > int64(512000) {
		return "", errors.New("sorry, please upload an Image of 500KB or less")
	}
	//only the first 512 bytes are used to sniff the content type of a file,
	//so, so no need to read the entire bytes of a file.
	buffer := make([]byte, size)
	f.Read(buffer)
	fileType := http.DetectContentType(buffer)
	//if the image is valid
	if !strings.HasPrefix(fileType, "image") {
		return "", errors.New("please upload a valid image")
	}
	filePath := FormatFile(file.Filename)

	accessKey := os.Getenv("DO_SPACES_KEY")
	secKey := os.Getenv("DO_SPACES_SECRET")
	endpoint := os.Getenv("DO_SPACES_ENDPOINT")
	ssl := true

	// Initiate a client using DigitalOcean Spaces.
	client, err := minio.New(endpoint, accessKey, secKey, ssl)
	if err != nil {
		log.Fatal(err)
	}
	fileBytes := bytes.NewReader(buffer)
	cacheControl := "max-age=31536000"
	// make it public
	userMetaData := map[string]string{"x-amz-acl": "public-read"}
	n, err := client.PutObject("chodapi", filePath, fileBytes, size, minio.PutObjectOptions{ContentType: fileType, CacheControl: cacheControl, UserMetadata: userMetaData})
	if err != nil {
		fmt.Println("the error", err)
		return "", errors.New("something went wrong")
	}
	fmt.Println("Successfully uploaded bytes: ", n)
	return filePath, nil
}
```

## File: `interfaces/middleware/middleware.go`
```go
package middleware

import (
	"bytes"
	"food-app/infrastructure/auth"
	"github.com/gin-gonic/gin"
	"io/ioutil"
	"net/http"
)

func AuthMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		err := auth.TokenValid(c.Request)
		if err != nil {
			c.JSON(http.StatusUnauthorized, gin.H{
				"status": http.StatusUnauthorized,
				"error":  err.Error(),
			})
			c.Abort()
			return
		}
		c.Next()
	}
}

func CORSMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
		c.Writer.Header().Set("Access-Control-Allow-Credentials", "true")
		c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With")
		c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS, GET, PUT, PATCH, DELETE")

		if c.Request.Method == "OPTIONS" {
			c.AbortWithStatus(204)
			return
		}
		c.Next()
	}
}

//Avoid a large file from loading into memory
//If the file size is greater than 8MB dont allow it to even load into memory and waste our time.
func MaxSizeAllowed(n int64) gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Request.Body = http.MaxBytesReader(c.Writer, c.Request.Body, n)
		buff, errRead := c.GetRawData()
		if errRead != nil {
			//c.JSON(http.StatusRequestEntityTooLarge,"too large")
			c.JSON(http.StatusRequestEntityTooLarge, gin.H{
				"status":     http.StatusRequestEntityTooLarge,
				"upload_err": "too large: upload an image less than 8MB",
			})
			c.Abort()
			return
		}
		buf := bytes.NewBuffer(buff)
		c.Request.Body = ioutil.NopCloser(buf)
	}
}
```

## File: `utils/mock/mock.go`
```go
package mock

import (
	"food-app/domain/entity"
	"food-app/infrastructure/auth"
	"mime/multipart"
	"net/http"
)

//UserAppInterface is a mock user app interface
type UserAppInterface struct {
	SaveUserFn                  func(*entity.User) (*entity.User, map[string]string)
	GetUsersFn                  func() ([]entity.User, error)
	GetUserFn                   func(uint64) (*entity.User, error)
	GetUserByEmailAndPasswordFn func(*entity.User) (*entity.User, map[string]string)
}

//SaveUser calls the SaveUserFn
func (u *UserAppInterface) SaveUser(user *entity.User) (*entity.User, map[string]string) {
	return u.SaveUserFn(user)
}

//GetUsersFn calls the GetUsers
func (u *UserAppInterface) GetUsers() ([]entity.User, error) {
	return u.GetUsersFn()
}

//GetUserFn calls the GetUser
func (u *UserAppInterface) GetUser(userId uint64) (*entity.User, error) {
	return u.GetUserFn(userId)
}

//GetUserByEmailAndPasswordFn calls the GetUserByEmailAndPassword
func (u *UserAppInterface) GetUserByEmailAndPassword(user *entity.User) (*entity.User, map[string]string) {
	return u.GetUserByEmailAndPasswordFn(user)
}

//FoodAppInterface is a mock food app interface
type FoodAppInterface struct {
	SaveFoodFn   func(*entity.Food) (*entity.Food, map[string]string)
	GetAllFoodFn func() ([]entity.Food, error)
	GetFoodFn    func(uint64) (*entity.Food, error)
	UpdateFoodFn func(*entity.Food) (*entity.Food, map[string]string)
	DeleteFoodFn func(uint64) error
}

func (f *FoodAppInterface) SaveFood(food *entity.Food) (*entity.Food, map[string]string) {
	return f.SaveFoodFn(food)
}
func (f *FoodAppInterface) GetAllFood() ([]entity.Food, error) {
	return f.GetAllFoodFn()
}
func (f *FoodAppInterface) GetFood(foodId uint64) (*entity.Food, error) {
	return f.GetFoodFn(foodId)
}
func (f *FoodAppInterface) UpdateFood(food *entity.Food) (*entity.Food, map[string]string) {
	return f.UpdateFoodFn(food)
}
func (f *FoodAppInterface) DeleteFood(foodId uint64) error {
	return f.DeleteFoodFn(foodId)
}

//AuthInterface is a mock auth interface
type AuthInterface struct {
	CreateAuthFn    func(uint64, *auth.TokenDetails) error
	FetchAuthFn     func(string) (uint64, error)
	DeleteRefreshFn func(string) error
	DeleteTokensFn  func(*auth.AccessDetails) error
}

func (f *AuthInterface) DeleteRefresh(refreshUuid string) error {
	return f.DeleteRefreshFn(refreshUuid)
}
func (f *AuthInterface) DeleteTokens(authD *auth.AccessDetails) error {
	return f.DeleteTokensFn(authD)
}
func (f *AuthInterface) FetchAuth(uuid string) (uint64, error) {
	return f.FetchAuthFn(uuid)
}
func (f *AuthInterface) CreateAuth(userId uint64, authD *auth.TokenDetails) error {
	return f.CreateAuthFn(userId, authD)
}

//TokenInterface is a mock token interface
type TokenInterface struct {
	CreateTokenFn          func(userId uint64) (*auth.TokenDetails, error)
	ExtractTokenMetadataFn func(*http.Request) (*auth.AccessDetails, error)
}

func (f *TokenInterface) CreateToken(userid uint64) (*auth.TokenDetails, error) {
	return f.CreateTokenFn(userid)
}
func (f *TokenInterface) ExtractTokenMetadata(r *http.Request) (*auth.AccessDetails, error) {
	return f.ExtractTokenMetadataFn(r)
}

type UploadFileInterface struct {
	UploadFileFn func(file *multipart.FileHeader) (string, error)
}

func (up *UploadFileInterface) UploadFile(file *multipart.FileHeader) (string, error) {
	return up.UploadFileFn(file)
}

```

