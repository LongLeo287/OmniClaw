---
id: github.com-jankaritech-bsdateserver-c47b2eb2-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:11.273238
---

# KNOWLEDGE EXTRACT: github.com_JankariTech_bsDateServer_c47b2eb2
> **Extracted on:** 2026-04-01 17:05:21
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525488/github.com_JankariTech_bsDateServer_c47b2eb2

---

## File: `bsDateServer_test.go`
```go
package main

import (
    "fmt"
    "github.com/cucumber/godog"
    "io/ioutil"
    "net/http"
    "strings"
)

var host = "http://localhost:10000"

var res *http.Response

func aRequestIsSentToTheEndpoint(method, endpoint string) error {
    var reader = strings.NewReader("")
    var request, err = http.NewRequest(method, host+endpoint, reader)
    if err != nil {
        return fmt.Errorf("could not create request %s", err.Error())
    }

    res, err = http.DefaultClient.Do(request)
    if err != nil {
        return fmt.Errorf("could not send request %s", err.Error())
    }
    return nil
}

func theHTTPresponseCodeShouldBe(expectedCode int) error {
    if expectedCode != res.StatusCode {
        return fmt.Errorf("status code not as expected! Expected '%d', got '%d'", expectedCode, res.StatusCode)
    }
    return nil
}

func theResponseContentShouldBe(expectedContent string) error {
    body, _ := ioutil.ReadAll(res.Body)
    if expectedContent != strings.TrimSpace(string(body)) {
        return fmt.Errorf("response content not as expected! Expected '%s', got '%s'", expectedContent, string(body))
    }
    return nil
}

func FeatureContext(ctx *godog.ScenarioContext) {
    ctx.Step(`^a "([^"]*)" request is sent to the endpoint "([^"]*)"$`, aRequestIsSentToTheEndpoint)
    ctx.Step(`^the HTTP-response code should be "(\d+)"$`, theHTTPresponseCodeShouldBe)
    ctx.Step(`^the response content should be "([^"]*)"$`, theResponseContentShouldBe)
}
```

## File: `go.mod`
```
module github.com/JankariTech/bsDateServer

go 1.19

require (
	github.com/JankariTech/GoBikramSambat v0.0.0-20200507040640-7d5f1ba6f8da
	github.com/cucumber/godog v0.12.6
	github.com/gorilla/mux v1.7.3
)

require (
	github.com/cucumber/gherkin-go/v19 v19.0.3 // indirect
	github.com/cucumber/messages-go/v16 v16.0.1 // indirect
	github.com/gofrs/uuid v4.2.0+incompatible // indirect
	github.com/hashicorp/go-immutable-radix v1.3.1 // indirect
	github.com/hashicorp/go-memdb v1.3.2 // indirect
	github.com/hashicorp/golang-lru v0.5.4 // indirect
	github.com/magiconair/properties v1.8.1 // indirect
	github.com/spf13/pflag v1.0.5 // indirect
)
```

## File: `go.sum`
```
github.com/JankariTech/GoBikramSambat v0.0.0-20200507040640-7d5f1ba6f8da h1:qEOzI/BqfQNLgAlZz6QBoDqwU3DllxOcdVHLywRGnM4=
github.com/JankariTech/GoBikramSambat v0.0.0-20200507040640-7d5f1ba6f8da/go.mod h1:G9Lmhh0BqLSVcTyYg2FfDcr8U9iHlhapo4EPD9KpGAk=
github.com/cpuguy83/go-md2man/v2 v2.0.1/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
github.com/cucumber/gherkin-go/v19 v19.0.3 h1:mMSKu1077ffLbTJULUfM5HPokgeBcIGboyeNUof1MdE=
github.com/cucumber/gherkin-go/v19 v19.0.3/go.mod h1:jY/NP6jUtRSArQQJ5h1FXOUgk5fZK24qtE7vKi776Vw=
github.com/cucumber/godog v0.12.6 h1:3IToXviU45G7FgijwTk/LdB4iojn8zUFDfQLj4MMiHc=
github.com/cucumber/godog v0.12.6/go.mod h1:Y02TTpimPXDb70PnG6M3zpODXm1+bjCsuZzcW76xAww=
github.com/cucumber/messages-go/v16 v16.0.0/go.mod h1:EJcyR5Mm5ZuDsKJnT2N9KRnBK30BGjtYotDKpwQ0v6g=
github.com/cucumber/messages-go/v16 v16.0.1 h1:fvkpwsLgnIm0qugftrw2YwNlio+ABe2Iu94Ap8GMYIY=
github.com/cucumber/messages-go/v16 v16.0.1/go.mod h1:EJcyR5Mm5ZuDsKJnT2N9KRnBK30BGjtYotDKpwQ0v6g=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/gofrs/uuid v4.0.0+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/gofrs/uuid v4.2.0+incompatible h1:yyYWMnhkhrKwwr8gAOcOCYxOOscHgDS9yZgBrnJfGa0=
github.com/gofrs/uuid v4.2.0+incompatible/go.mod h1:b2aQJv3Z4Fp6yNu3cdSllBxTCLRxnplIgP/c0N/04lM=
github.com/gopherjs/gopherjs v0.0.0-20181017120253-0766667cb4d1 h1:EGx4pi6eqNxGaHF6qqu48+N2wcFQ5qg5FXgOdqsJ5d8=
github.com/gopherjs/gopherjs v0.0.0-20181017120253-0766667cb4d1/go.mod h1:wJfORRmW1u3UXTncJ5qlYoELFm8eSnnEO6hX4iZ3EWY=
github.com/gorilla/mux v1.7.3 h1:gnP5JzjVOuiZD07fKKToCAOjS0yOpj/qPETTXCCS6hw=
github.com/gorilla/mux v1.7.3/go.mod h1:1lud6UwP+6orDFRuTfBEV8e9/aOM/c4fVVCaMa2zaAs=
github.com/hashicorp/go-immutable-radix v1.3.0/go.mod h1:0y9vanUI8NX6FsYoO3zeMjhV/C5i9g4Q3DwcSNZ4P60=
github.com/hashicorp/go-immutable-radix v1.3.1 h1:DKHmCUm2hRBK510BaiZlwvpD40f8bJFeZnpfm2KLowc=
github.com/hashicorp/go-immutable-radix v1.3.1/go.mod h1:0y9vanUI8NX6FsYoO3zeMjhV/C5i9g4Q3DwcSNZ4P60=
github.com/hashicorp/go-memdb v1.3.2 h1:RBKHOsnSszpU6vxq80LzC2BaQjuuvoyaQbkLTf7V7g8=
github.com/hashicorp/go-memdb v1.3.2/go.mod h1:Mluclgwib3R93Hk5fxEfiRhB+6Dar64wWh71LpNSe3g=
github.com/hashicorp/go-uuid v1.0.0/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/go-uuid v1.0.2 h1:cfejS+Tpcp13yd5nYHWDI6qVCny6wyX2Mt5SGur2IGE=
github.com/hashicorp/go-uuid v1.0.2/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/golang-lru v0.5.0/go.mod h1:/m3WP610KZHVQ1SGc6re/UDhFvYD7pJ4Ao+sR/qLZy8=
github.com/hashicorp/golang-lru v0.5.4 h1:YDjusn29QI/Das2iO9M0BHnIbxPeyuCHsjMW+lJfyTc=
github.com/hashicorp/golang-lru v0.5.4/go.mod h1:iADmTwqILo4mZ8BN3D2Q6+9jd8WM5uGBxy+E8yxSoD4=
github.com/inconshreveable/mousetrap v1.0.0/go.mod h1:PxqpIevigyE2G7u3NXJIT2ANytuPF1OarO4DADm73n8=
github.com/jtolds/gls v4.20.0+incompatible h1:xdiiI2gbIgH/gLH7ADydsJ1uDOEzR8yvV7C0MuV77Wo=
github.com/jtolds/gls v4.20.0+incompatible/go.mod h1:QJZ7F/aHp+rZTRtaJ1ow/lLfFfVYBRgL+9YlvaHOwJU=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/magiconair/properties v1.8.1 h1:ZC2Vc7/ZFkGmsVC9KvOjumD+G5lXy2RtTKyzRKO2BQ4=
github.com/magiconair/properties v1.8.1/go.mod h1:PppfXfuXeibc/6YijjN8zIbojt8czPbwD3XqdrwzmxQ=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/smartystreets/assertions v0.0.0-20180927180507-b2de0cb4f26d h1:zE9ykElWQ6/NYmHa3jpm/yHnI4xSofP+UP6SpjHcSeM=
github.com/smartystreets/assertions v0.0.0-20180927180507-b2de0cb4f26d/go.mod h1:OnSkiWE9lh6wB0YB77sQom3nweQdgAjqCqsofrRNTgc=
github.com/smartystreets/goconvey v1.6.4 h1:fv0U8FUIMPNf1L9lnHLvLhgicrIVChEkdzIKYqbNC9s=
github.com/smartystreets/goconvey v1.6.4/go.mod h1:syvi0/a8iFYH4r/RixwvyeAJjdLS9QV7WQ/tjFTllLA=
github.com/spf13/cobra v1.4.0/go.mod h1:Wo4iy3BUC+X2Fybo0PDqwJIv3dNRiZLHQymsfxlB84g=
github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.1 h1:5TQK59W5E3v0r2duFAb7P95B6hEeOyEnHRa8MjYSMTY=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/tools v0.0.0-20190328211700-ab21143f2384/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `main.go`
```go
package main

import (
	"fmt"
	"github.com/JankariTech/GoBikramSambat"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"strconv"
	"strings"
)

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Bikram Sambat Server")
}

func getAdFromBs(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	if r.Method != "GET" {
		http.Error(w, "Could not create " + r.Method + " request ", http.StatusBadRequest)
		return
	}
	dateString := vars["date"]
	var splitedDate = strings.Split(dateString, "-")
	if len(splitedDate) < 3 || len(splitedDate) > 3 {
		http.Error(w, "not a valid date", http.StatusBadRequest)
		return
	} else {
		day, _ := strconv.Atoi(splitedDate[2])
		month, _ := strconv.Atoi(splitedDate[1])
		year, _ := strconv.Atoi(splitedDate[0])
		date, err := bsdate.New(day, month, year)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		gregorianDate, _ := date.GetGregorianDate()
		fmt.Fprintf(w, gregorianDate.Format("2006-01-02"))
	}
}

func getBsFromAd(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	if r.Method != "GET" {
		http.Error(w, "Could not create " + r.Method + " request ", http.StatusBadRequest)
		return
	}
	dateString := vars["date"]
	var splitedDate = strings.Split(dateString, "-")
	if len(splitedDate) < 3 || len(splitedDate) > 3 {
		http.Error(w, "cannot convert date, invalid or missing data", http.StatusBadRequest)
		return
	}
	day, _ := strconv.Atoi(splitedDate[2])
	month, _ := strconv.Atoi(splitedDate[1])
	year, _ := strconv.Atoi(splitedDate[0])
	bsDate, err := bsdate.NewFromGregorian(day, month, year)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	fmt.Fprintf(w, "%d-%02d-%02d", bsDate.GetYear(), bsDate.GetMonth(), bsDate.GetDay())
}

func handleRequests() {
	myRouter := mux.NewRouter().StrictSlash(true)
	myRouter.HandleFunc("/", homePage)
	myRouter.HandleFunc("/ad-from-bs/{date}", getAdFromBs)
	myRouter.HandleFunc("/bs-from-ad/{date}", getBsFromAd)
	log.Fatal(http.ListenAndServe(":10000", myRouter))
}

func main() {
	handleRequests()
}
```

## File: `features/ad-to-bs-conversion.feature`
```
Feature: convert dates from AD to BS using an API
  As an app-developer in Nepal
  I want to be able to send AD dates to an API endpoint and receive the corresponding BS dates
  So that I have a simple way to convert AD to BS dates, that can be used in other apps

  Scenario Outline: converting a valid AD date
    When a "GET" request is sent to the endpoint "/bs-from-ad/<ad-date>"
    Then the HTTP-response code should be "200"
    And the response content should be "<bs-date>"
    Examples:
      | ad-date    | bs-date    |
      | 2003-07-17 | 2060-04-01 |
      | 1983-04-14 | 2040-01-01 |
      | 1984-04-12 | 2040-12-30 |
      | 2020-02-29 | 2076-11-17 |
      | 2020-01-31 | 2076-10-17 |

  Scenario Outline: converting an invalid AD date
    When a "GET" request is sent to the endpoint "/bs-from-ad/<ad-date>"
    Then the HTTP-response code should be "400"
    And the response content should be "cannot convert date, invalid or missing data"
    Examples:
      | ad-date       |
      | 97-04         |
      | 97-04-08      |
      | aeiou         |
      | 1984-04-31    |
      | 1987-04-05-01 |
      | 2022-02-29    |

  Scenario Outline: unhandled request types
    When a "<type>" request is sent to the endpoint "/bs-from-ad/<ad-date>"
    Then the HTTP-response code should be "400"
    And the response content should be "<response>"
    Examples:
      | type | ad-date    | response                      |
      | POST | 97-04      | Could not create POST request |
      | PUT  | 97-04      | Could not create PUT request  |
      | POST | 2020-02-29 | Could not create POST request |
      | PUT  | 2020-02-29 | Could not create PUT request  |
```

## File: `features/bs-to-ad-convertion.feature`
```
Feature: convert dates from BS to AD using an API
  As an app-developer in Nepal
  I want to be able to send BS dates to an API endpoint and receive the corresponding AD dates
  So that I have a simple way to convert BS to AD dates, that can be used in other apps

  Scenario Outline: converting a valid BS date
    When a "GET" request is sent to the endpoint "/ad-from-bs/<bs-date>"
    Then the HTTP-response code should be "200"
    And the response content should be "<ad-date>"
    Examples:
      | bs-date    | ad-date    |
      | 2060-04-01 | 2003-07-17 |
      | 2040-01-01 | 1983-04-14 |
      | 2040-12-30 | 1984-04-12 |

  Scenario Outline: converting an invalid BS date
    When a "GET" request is sent to the endpoint "/ad-from-bs/<bs-date>"
    Then the HTTP-response code should be "400"
    And the response content should be "not a valid date"
    Examples:
      | bs-date       |
      | 2060-14-01    |
      | 40-01-01      |
      | date          |
      | 1987-04-05-01 |

  Scenario Outline: unhandled request types
    When a "<type>" request is sent to the endpoint "/ad-from-bs/<bs-date>"
    Then the HTTP-response code should be "400"
    And the response content should be "<response>"
    Examples:
      | type | bs-date    | response                      |
      | POST | 87-04      | Could not create POST request |
      | PUT  | 87-04      | Could not create PUT request  |
      | POST | 2040-12-30 | Could not create POST request |
      | PUT  | 2040-12-30 | Could not create PUT request  |
```

