---
id: github.com-syndtr-goleveldb-1a153aea-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:25.277568
---

# KNOWLEDGE EXTRACT: github.com_syndtr_goleveldb_1a153aea
> **Extracted on:** 2026-04-01 12:55:13
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522123/github.com_syndtr_goleveldb_1a153aea

---

## File: `.golangci.yml`
```yaml
linters-settings:
  gocritic:
    disabled-checks:
      - ifElseChain
      - elseif

linters:
  enable:
    - gofmt
    - gocritic
    - unconvert
```

## File: `.travis.yml`
```yaml
language: go

before_install:
  - curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.46.2

go:
  - 1.14.x
  - 1.18.x
  - tip

script:
  - go vet ./...
  - golangci-lint run
  - go test -short -timeout 1h ./...
  - go test -timeout 30m -race -run "TestDB_(Concurrent|GoleveldbIssue74)" ./leveldb
```

## File: `LICENSE`
```
Copyright 2012 Suryandaru Triandana <syndtr@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## File: `README.md`
```markdown
This is an implementation of the [LevelDB key/value database](https://github.com/google/leveldb) in the [Go programming language](https://go.dev).

[![Build Status](https://app.travis-ci.com/syndtr/goleveldb.svg?branch=master)](https://app.travis-ci.com/syndtr/goleveldb)

Installation
-----------

	go get github.com/syndtr/goleveldb/leveldb

Requirements
-----------

* Need at least `go1.14` or newer.

Usage
-----------

Create or open a database:
```go
// The returned DB instance is safe for concurrent use. Which mean that all
// DB's methods may be called concurrently from multiple goroutine.
db, err := leveldb.OpenFile("path/to/db", nil)
...
defer db.Close()
...
```
Read or modify the database content:
```go
// Remember that the contents of the returned slice should not be modified.
data, err := db.Get([]byte("key"), nil)
...
err = db.Put([]byte("key"), []byte("value"), nil)
...
err = db.Delete([]byte("key"), nil)
...
```

Iterate over database content:
```go
iter := db.NewIterator(nil, nil)
for iter.Next() {
	// Remember that the contents of the returned slice should not be modified, and
	// only valid until the next call to Next.
	key := iter.Key()
	value := iter.Value()
	...
}
iter.Release()
err = iter.Error()
...
```
Seek-then-Iterate:
```go
iter := db.NewIterator(nil, nil)
for ok := iter.Seek(key); ok; ok = iter.Next() {
	// Use key/value.
	...
}
iter.Release()
err = iter.Error()
...
```
Iterate over subset of database content:
```go
iter := db.NewIterator(&util.Range{Start: []byte("foo"), Limit: []byte("xoo")}, nil)
for iter.Next() {
	// Use key/value.
	...
}
iter.Release()
err = iter.Error()
...
```
Iterate over subset of database content with a particular prefix:
```go
iter := db.NewIterator(util.BytesPrefix([]byte("foo-")), nil)
for iter.Next() {
	// Use key/value.
	...
}
iter.Release()
err = iter.Error()
...
```
Batch writes:
```go
batch := new(leveldb.Batch)
batch.Put([]byte("foo"), []byte("value"))
batch.Put([]byte("bar"), []byte("another value"))
batch.Delete([]byte("baz"))
err = db.Write(batch, nil)
...
```
Use bloom filter:
```go
o := &opt.Options{
	Filter: filter.NewBloomFilter(10),
}
db, err := leveldb.OpenFile("path/to/db", o)
...
defer db.Close()
...
```
Documentation
-----------

You can read package documentation [here](https://pkg.go.dev/github.com/syndtr/goleveldb).
```

## File: `go.mod`
```
module github.com/syndtr/goleveldb

go 1.14

require (
	github.com/fsnotify/fsnotify v1.5.4 // indirect
	github.com/golang/snappy v0.0.4
	github.com/onsi/ginkgo v1.16.5
	github.com/onsi/gomega v1.19.0
	github.com/stretchr/testify v1.7.2
	golang.org/x/net v0.0.0-20220607020251-c690dde0001d // indirect
	golang.org/x/xerrors v0.0.0-20220517211312-f3a8303e98df // indirect
)
```

## File: `go.sum`
```
github.com/chzyer/logex v1.1.10/go.mod h1:+Ywpsq7O8HXn0nuIou7OrIPyXbp3wmkHB+jjWRnGsAI=
github.com/chzyer/readline v0.0.0-20180603132655-2972be24d48e/go.mod h1:nSuG5e5PlCu98SY8svDHJxuZscDgtXS6KTTbou5AhLI=
github.com/chzyer/test v0.0.0-20180213035817-a1ea475d72b1/go.mod h1:Q3SI9o4m/ZMnBNeIyt5eFwwo7qiLfzFZmjNmxjkiQlU=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/fsnotify/fsnotify v1.4.7/go.mod h1:jwhsz4b93w/PPRr/qN1Yymfu8t87LnFCMoQvtojpjFo=
github.com/fsnotify/fsnotify v1.4.9/go.mod h1:znqG4EE+3YCdAaPaxE2ZRY/06pZUdp0tY4IgpuI1SZQ=
github.com/fsnotify/fsnotify v1.5.4 h1:jRbGcIw6P2Meqdwuo0H1p6JVLbL5DHKAKlYndzMwVZI=
github.com/fsnotify/fsnotify v1.5.4/go.mod h1:OVB6XrOHzAwXMpEM7uPOzcehqUV2UqJxmVXmkdnm1bU=
github.com/go-task/slim-sprig v0.0.0-20210107165309-348f09dbbbc0/go.mod h1:fyg7847qk6SyHyPtNmDHnmrv/HOrqktSC+C9fM+CJOE=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.4.0-rc.1/go.mod h1:ceaxUfeHdC40wWswd/P6IGgMaK3YpKi5j83Wpe3EHw8=
github.com/golang/protobuf v1.4.0-rc.1.0.20200221234624-67d41d38c208/go.mod h1:xKAWHe0F5eneWXFV3EuXVDTCmh+JuBKY0li0aMyXATA=
github.com/golang/protobuf v1.4.0-rc.2/go.mod h1:LlEzMj4AhA7rCAGe4KMBDvJI+AwstrUpVNzEA03Pprs=
github.com/golang/protobuf v1.4.0-rc.4.0.20200313231945-b860323f09d0/go.mod h1:WU3c8KckQ9AFe+yFwt9sWVRKCVIyN9cPHBJSNnbL67w=
github.com/golang/protobuf v1.4.0/go.mod h1:jodUvKwWbYaEsadDk5Fwe5c77LiNKVO9IDvqG2KuDX0=
github.com/golang/protobuf v1.4.2/go.mod h1:oDoupMAO8OvCJWAcko0GGGIgR6R6ocIYbsSw735rRwI=
github.com/golang/protobuf v1.5.0/go.mod h1:FsONVRAS9T7sI+LIUmWTfcYkHO4aIWwzhcaSAoJOfIk=
github.com/golang/protobuf v1.5.2 h1:ROPKBNFfQgOUMifHyP+KYbvpjbdoFNs+aK7DXlji0Tw=
github.com/golang/protobuf v1.5.2/go.mod h1:XVQd3VNwM+JqD3oG2Ue2ip4fOMUkwXdXDdiuN0vRsmY=
github.com/golang/snappy v0.0.4 h1:yAGX7huGHXlcLOEtBnF4w7FQwA26wojNCwOYAEhLjQM=
github.com/golang/snappy v0.0.4/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
github.com/google/go-cmp v0.3.0/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.3.1/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.4.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.5 h1:Khx7svrCpmxxtHBq5j2mp/xVjsi8hQMfNLvJFAlrGgU=
github.com/google/go-cmp v0.5.5/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/pprof v0.0.0-20210407192527-94a9f03dee38/go.mod h1:kpwsk12EmLew5upagYY7GY0pfYCcupk39gWOCRROcvE=
github.com/hpcloud/tail v1.0.0/go.mod h1:ab1qPbhIpdTxEkNHXyeSf5vhxWSCs/tWer42PpOxQnU=
github.com/ianlancetaylor/demangle v0.0.0-20200824232613-28f6c0f3b639/go.mod h1:aSSvb/t6k1mPoxDqO4vJh6VOCGPwU4O0C2/Eqndh1Sc=
github.com/nxadm/tail v1.4.4/go.mod h1:kenIhsEOeOJmVchQTgglprH7qJGnHDVpk1VPCcaMI8A=
github.com/nxadm/tail v1.4.8 h1:nPr65rt6Y5JFSKQO7qToXr7pePgD6Gwiw05lkbyAQTE=
github.com/nxadm/tail v1.4.8/go.mod h1:+ncqLTQzXmGhMZNUePPaPqPvBxHAIsmXswZKocGu+AU=
github.com/onsi/ginkgo v1.6.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+WWjE=
github.com/onsi/ginkgo v1.12.1/go.mod h1:zj2OWP4+oCPe1qIXoGWkgMRwljMUYCdkwsT2108oapk=
github.com/onsi/ginkgo v1.16.4/go.mod h1:dX+/inL/fNMqNlz0e9LfyB9TswhZpCVdJM/Z6Vvnwo0=
github.com/onsi/ginkgo v1.16.5 h1:8xi0RTUf59SOSfEtZMvwTvXYMzG4gV23XVHOZiXNtnE=
github.com/onsi/ginkgo v1.16.5/go.mod h1:+E8gABHa3K6zRBolWtd+ROzc/U5bkGt0FwiG042wbpU=
github.com/onsi/ginkgo/v2 v2.1.3 h1:e/3Cwtogj0HA+25nMP1jCMDIf8RtRYbGwGGuBIFztkc=
github.com/onsi/ginkgo/v2 v2.1.3/go.mod h1:vw5CSIxN1JObi/U8gcbwft7ZxR2dgaR70JSE3/PpL4c=
github.com/onsi/gomega v1.7.1/go.mod h1:XdKZgCCFLUoM/7CFJVPcG8C1xQ1AJ0vpAezJrB7JYyY=
github.com/onsi/gomega v1.10.1/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
github.com/onsi/gomega v1.17.0/go.mod h1:HnhC7FXeEQY45zxNK3PPoIUhzk/80Xly9PcubAlGdZY=
github.com/onsi/gomega v1.19.0 h1:4ieX6qQjPP/BfC3mpsAtIGGlxTWPeA3Inl/7DtXw1tw=
github.com/onsi/gomega v1.19.0/go.mod h1:LY+I3pBVzYsTBU1AnDwOSxaYi9WoWiqgwooUqq9yPro=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.5.1/go.mod h1:5W2xD1RspED5o8YsWQXVCued0rvSQ+mT+I5cxcmMvtA=
github.com/stretchr/testify v1.7.2 h1:4jaiDzPyXQvSd7D0EjG45355tLlV3VOECpq10pLC+8s=
github.com/stretchr/testify v1.7.2/go.mod h1:R6va5+xMeoiuVRoj+gSkQ7d3FALtqAAGI1FQKckRals=
github.com/yuin/goldmark v1.2.1/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/net v0.0.0-20180906233101-161cd47e91fd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200520004742-59133d7f0dd7/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20201021035429-f5854403a974/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20210428140749-89ef3d95e781/go.mod h1:OJAsFXCWl8Ukc7SiCT/9KSuxbyM7479/AVlXFRxuMCk=
golang.org/x/net v0.0.0-20220225172249-27dd8689420f/go.mod h1:CfG3xpIq0wQ8r1q4Su4UZFWDARRcnwPjda9FqA0JpMk=
golang.org/x/net v0.0.0-20220607020251-c690dde0001d h1:4SFsTMi4UahlKoloni7L4eYzhFRifURQLw+yv0QDCx8=
golang.org/x/net v0.0.0-20220607020251-c690dde0001d/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20180909124046-d0be0721c37e/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190904154756-749cb33beabd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191005200804-aed5e4c7ecf9/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191120155948-bd437916bb0e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191204072324-ce4227a45e2e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200323222414-85ca7c5b95cd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200930185726-fdedc70b468f/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210112080510-489259a85091/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210423082822-04245dca01da/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20211216021012-1d35b9e2eb4e/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220412211240-33da011f77ad/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a h1:dGzPydgVsqGcTRVwiLJ1jVbufYwmzD3LfVPLKsKg+0k=
golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/term v0.0.0-20210927222741-03fcf44c2211/go.mod h1:jbD1KX2456YbFQfuXm/mYQcufACuNUgVhRMnK/tPxf8=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.6/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.7 h1:olpwvP2KacW1ZWvsR7uQhoyTYvKAupfQrRGBFM352Gk=
golang.org/x/text v0.3.7/go.mod h1:u+2+/6zg+i71rQMx5EYifcz6MCKuco9NR6JIITiCfzQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20201224043029-2b0845dc783e h1:4nW4NLDYnU28ojHaHO8OVxFHk/aQ33U01a9cjED+pzE=
golang.org/x/tools v0.0.0-20201224043029-2b0845dc783e/go.mod h1:emZCQorbCU4vsT4fOWvOPXz4eW1wZW4PmDk9uLelYpA=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20220517211312-f3a8303e98df h1:5Pf6pFKu98ODmgnpvkJ3kFUOQGGLIzLIkbzUHp47618=
golang.org/x/xerrors v0.0.0-20220517211312-f3a8303e98df/go.mod h1:K8+ghG5WaK9qNqU5K3HdILfMLy1f3aNYFI/wnl100a8=
google.golang.org/protobuf v0.0.0-20200109180630-ec00e32a8dfd/go.mod h1:DFci5gLYBciE7Vtevhsrf46CRTquxDuWsQurQQe4oz8=
google.golang.org/protobuf v0.0.0-20200221191635-4d8936d0db64/go.mod h1:kwYJMbMJ01Woi6D6+Kah6886xMZcty6N08ah7+eCXa0=
google.golang.org/protobuf v0.0.0-20200228230310-ab0ca4ff8a60/go.mod h1:cfTl7dwQJ+fmap5saPgwCLgHXTUD7jkjRqWcaiX5VyM=
google.golang.org/protobuf v1.20.1-0.20200309200217-e05f789c0967/go.mod h1:A+miEFZTKqfCUM6K7xSMQL9OKL/b6hQv+e19PK+JZNE=
google.golang.org/protobuf v1.21.0/go.mod h1:47Nbq4nVaFHyn7ilMalzfO3qCViNmqZ2kzikPIcrTAo=
google.golang.org/protobuf v1.23.0/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.26.0-rc.1/go.mod h1:jlhhOSvTdKEhbULTjvd4ARK9grFBp09yW+WbY/TyQbw=
google.golang.org/protobuf v1.26.0 h1:bxAC2xTBsZGibn2RTntX0oH50xLsqy1OxA9tTL3p/lk=
google.golang.org/protobuf v1.26.0/go.mod h1:9q0QmTI4eRPtz6boOQmLYwt+qCgq0jsYwAQnmE0givc=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/fsnotify.v1 v1.4.7/go.mod h1:Tz8NjZHkW78fSQdbUxIjBTcgA1z1m8ZHf0WmKUhAMys=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7 h1:uRGJdciOHaEIrze2W8Q3AKkepLTh2hOroT7a+7czfdQ=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7/go.mod h1:dt/ZhP58zS4L8KSrWDmTeBkI65Dw0HsyUHuEVlX15mw=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.4/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.3.0/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.4.0 h1:D8xgwECY7CYvx+Y2n4sBz93Jn9JRvxdiyyo8CTfuKaY=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `leveldb/batch.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"encoding/binary"
	"fmt"
	"io"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/memdb"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

// ErrBatchCorrupted records reason of batch corruption. This error will be
// wrapped with errors.ErrCorrupted.
type ErrBatchCorrupted struct {
	Reason string
}

func (e *ErrBatchCorrupted) Error() string {
	return fmt.Sprintf("leveldb: batch corrupted: %s", e.Reason)
}

func newErrBatchCorrupted(reason string) error {
	return errors.NewErrCorrupted(storage.FileDesc{}, &ErrBatchCorrupted{reason})
}

const (
	batchHeaderLen = 8 + 4
	batchGrowLimit = 3000
)

// BatchReplay wraps basic batch operations.
type BatchReplay interface {
	Put(key, value []byte)
	Delete(key []byte)
}

type batchIndex struct {
	keyType            keyType
	keyPos, keyLen     int
	valuePos, valueLen int
}

func (index batchIndex) k(data []byte) []byte {
	return data[index.keyPos : index.keyPos+index.keyLen]
}

func (index batchIndex) v(data []byte) []byte {
	if index.valueLen != 0 {
		return data[index.valuePos : index.valuePos+index.valueLen]
	}
	return nil
}

// Batch is a write batch.
type Batch struct {
	data  []byte
	index []batchIndex

	// internalLen is sums of key/value pair length plus 8-bytes internal key.
	internalLen int

	// growLimit is the threshold in order to slow down the memory allocation
	// for batch when the number of accumulated entries exceeds value.
	//
	// batchGrowLimit is used as the default threshold if it's not configured.
	growLimit int
}

func (b *Batch) grow(n int) {
	o := len(b.data)
	if cap(b.data)-o < n {
		limit := batchGrowLimit
		if b.growLimit > 0 {
			limit = b.growLimit
		}
		div := 1
		if len(b.index) > limit {
			div = len(b.index) / limit
		}
		ndata := make([]byte, o, o+n+o/div)
		copy(ndata, b.data)
		b.data = ndata
	}
}

func (b *Batch) appendRec(kt keyType, key, value []byte) {
	n := 1 + binary.MaxVarintLen32 + len(key)
	if kt == keyTypeVal {
		n += binary.MaxVarintLen32 + len(value)
	}
	b.grow(n)
	index := batchIndex{keyType: kt}
	o := len(b.data)
	data := b.data[:o+n]
	data[o] = byte(kt)
	o++
	o += binary.PutUvarint(data[o:], uint64(len(key)))
	index.keyPos = o
	index.keyLen = len(key)
	o += copy(data[o:], key)
	if kt == keyTypeVal {
		o += binary.PutUvarint(data[o:], uint64(len(value)))
		index.valuePos = o
		index.valueLen = len(value)
		o += copy(data[o:], value)
	}
	b.data = data[:o]
	b.index = append(b.index, index)
	b.internalLen += index.keyLen + index.valueLen + 8
}

// Put appends 'put operation' of the given key/value pair to the batch.
// It is safe to modify the contents of the argument after Put returns but not
// before.
func (b *Batch) Put(key, value []byte) {
	b.appendRec(keyTypeVal, key, value)
}

// Delete appends 'delete operation' of the given key to the batch.
// It is safe to modify the contents of the argument after Delete returns but
// not before.
func (b *Batch) Delete(key []byte) {
	b.appendRec(keyTypeDel, key, nil)
}

// Dump dumps batch contents. The returned slice can be loaded into the
// batch using Load method.
// The returned slice is not its own copy, so the contents should not be
// modified.
func (b *Batch) Dump() []byte {
	return b.data
}

// Load loads given slice into the batch. Previous contents of the batch
// will be discarded.
// The given slice will not be copied and will be used as batch buffer, so
// it is not safe to modify the contents of the slice.
func (b *Batch) Load(data []byte) error {
	return b.decode(data, -1)
}

// Replay replays batch contents.
func (b *Batch) Replay(r BatchReplay) error {
	for _, index := range b.index {
		switch index.keyType {
		case keyTypeVal:
			r.Put(index.k(b.data), index.v(b.data))
		case keyTypeDel:
			r.Delete(index.k(b.data))
		}
	}
	return nil
}

// Len returns number of records in the batch.
func (b *Batch) Len() int {
	return len(b.index)
}

// Reset resets the batch.
func (b *Batch) Reset() {
	b.data = b.data[:0]
	b.index = b.index[:0]
	b.internalLen = 0
}

func (b *Batch) replayInternal(fn func(i int, kt keyType, k, v []byte) error) error {
	for i, index := range b.index {
		if err := fn(i, index.keyType, index.k(b.data), index.v(b.data)); err != nil {
			return err
		}
	}
	return nil
}

func (b *Batch) append(p *Batch) {
	ob := len(b.data)
	oi := len(b.index)
	b.data = append(b.data, p.data...)
	b.index = append(b.index, p.index...)
	b.internalLen += p.internalLen

	// Updating index offset.
	if ob != 0 {
		for ; oi < len(b.index); oi++ {
			index := &b.index[oi]
			index.keyPos += ob
			if index.valueLen != 0 {
				index.valuePos += ob
			}
		}
	}
}

func (b *Batch) decode(data []byte, expectedLen int) error {
	b.data = data
	b.index = b.index[:0]
	b.internalLen = 0
	err := decodeBatch(data, func(i int, index batchIndex) error {
		b.index = append(b.index, index)
		b.internalLen += index.keyLen + index.valueLen + 8
		return nil
	})
	if err != nil {
		return err
	}
	if expectedLen >= 0 && len(b.index) != expectedLen {
		return newErrBatchCorrupted(fmt.Sprintf("invalid records length: %d vs %d", expectedLen, len(b.index)))
	}
	return nil
}

func (b *Batch) putMem(seq uint64, mdb *memdb.DB) error {
	var ik []byte
	for i, index := range b.index {
		ik = makeInternalKey(ik, index.k(b.data), seq+uint64(i), index.keyType)
		if err := mdb.Put(ik, index.v(b.data)); err != nil {
			return err
		}
	}
	return nil
}

func newBatch() interface{} {
	return &Batch{}
}

// MakeBatch returns empty batch with preallocated buffer.
func MakeBatch(n int) *Batch {
	return &Batch{data: make([]byte, 0, n)}
}

// BatchConfig contains the config options for batch.
type BatchConfig struct {
	// InitialCapacity is the batch initial capacity to preallocate.
	//
	// The default value is 0.
	InitialCapacity int

	// GrowLimit is the limit (in terms of entry) of how much buffer
	// can grow each cycle.
	//
	// Initially the buffer will grow twice its current size until
	// GrowLimit threshold is reached, after that the buffer will grow
	// up to GrowLimit each cycle. This buffer grow size in bytes is
	// loosely calculated from average entry size multiplied by GrowLimit.
	//
	// Generally, the memory allocation step is larger if this value
	// is configured large, vice versa.
	//
	// The default value is 3000.
	GrowLimit int
}

// MakeBatchWithConfig initializes a batch object with the given configs.
func MakeBatchWithConfig(config *BatchConfig) *Batch {
	var batch = new(Batch)
	if config != nil {
		if config.InitialCapacity > 0 {
			batch.data = make([]byte, 0, config.InitialCapacity)
		}
		if config.GrowLimit > 0 {
			batch.growLimit = config.GrowLimit
		}
	}
	return batch
}

func decodeBatch(data []byte, fn func(i int, index batchIndex) error) error {
	var index batchIndex
	for i, o := 0, 0; o < len(data); i++ {
		// Key type.
		index.keyType = keyType(data[o])
		if index.keyType > keyTypeVal {
			return newErrBatchCorrupted(fmt.Sprintf("bad record: invalid type %#x", uint(index.keyType)))
		}
		o++

		// Key.
		x, n := binary.Uvarint(data[o:])
		o += n
		if n <= 0 || o+int(x) > len(data) {
			return newErrBatchCorrupted("bad record: invalid key length")
		}
		index.keyPos = o
		index.keyLen = int(x)
		o += index.keyLen

		// Value.
		if index.keyType == keyTypeVal {
			x, n = binary.Uvarint(data[o:])
			o += n
			if n <= 0 || o+int(x) > len(data) {
				return newErrBatchCorrupted("bad record: invalid value length")
			}
			index.valuePos = o
			index.valueLen = int(x)
			o += index.valueLen
		} else {
			index.valuePos = 0
			index.valueLen = 0
		}

		if err := fn(i, index); err != nil {
			return err
		}
	}
	return nil
}

func decodeBatchToMem(data []byte, expectSeq uint64, mdb *memdb.DB) (seq uint64, batchLen int, err error) {
	seq, batchLen, err = decodeBatchHeader(data)
	if err != nil {
		return 0, 0, err
	}
	if seq < expectSeq {
		return 0, 0, newErrBatchCorrupted("invalid sequence number")
	}
	data = data[batchHeaderLen:]
	var ik []byte
	var decodedLen int
	err = decodeBatch(data, func(i int, index batchIndex) error {
		if i >= batchLen {
			return newErrBatchCorrupted("invalid records length")
		}
		ik = makeInternalKey(ik, index.k(data), seq+uint64(i), index.keyType)
		if err := mdb.Put(ik, index.v(data)); err != nil {
			return err
		}
		decodedLen++
		return nil
	})
	if err == nil && decodedLen != batchLen {
		err = newErrBatchCorrupted(fmt.Sprintf("invalid records length: %d vs %d", batchLen, decodedLen))
	}
	return
}

func encodeBatchHeader(dst []byte, seq uint64, batchLen int) []byte {
	dst = ensureBuffer(dst, batchHeaderLen)
	binary.LittleEndian.PutUint64(dst, seq)
	binary.LittleEndian.PutUint32(dst[8:], uint32(batchLen))
	return dst
}

func decodeBatchHeader(data []byte) (seq uint64, batchLen int, err error) {
	if len(data) < batchHeaderLen {
		return 0, 0, newErrBatchCorrupted("too short")
	}

	seq = binary.LittleEndian.Uint64(data)
	batchLen = int(binary.LittleEndian.Uint32(data[8:]))
	if batchLen < 0 {
		return 0, 0, newErrBatchCorrupted("invalid records length")
	}
	return
}

func batchesLen(batches []*Batch) int {
	batchLen := 0
	for _, batch := range batches {
		batchLen += batch.Len()
	}
	return batchLen
}

func writeBatchesWithHeader(wr io.Writer, batches []*Batch, seq uint64) error {
	if _, err := wr.Write(encodeBatchHeader(nil, seq, batchesLen(batches))); err != nil {
		return err
	}
	for _, batch := range batches {
		if _, err := wr.Write(batch.data); err != nil {
			return err
		}
	}
	return nil
}
```

## File: `leveldb/batch_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"bytes"
	"fmt"
	"math/rand"
	"testing"
	"testing/quick"

	"github.com/syndtr/goleveldb/leveldb/testutil"
)

func TestBatchHeader(t *testing.T) {
	f := func(seq uint64, length uint32) bool {
		encoded := encodeBatchHeader(nil, seq, int(length))
		decSeq, decLength, err := decodeBatchHeader(encoded)
		return err == nil && decSeq == seq && decLength == int(length)
	}
	config := &quick.Config{
		Rand: testutil.NewRand(),
	}
	if err := quick.Check(f, config); err != nil {
		t.Error(err)
	}
}

type batchKV struct {
	kt   keyType
	k, v []byte
}

func TestBatch(t *testing.T) {
	var (
		kvs         []batchKV
		internalLen int
	)
	batch := new(Batch)
	rbatch := new(Batch)
	abatch := new(Batch)
	testBatch := func(i int, kt keyType, k, v []byte) error {
		kv := kvs[i]
		if kv.kt != kt {
			return fmt.Errorf("invalid key type, index=%d: %d vs %d", i, kv.kt, kt)
		}
		if !bytes.Equal(kv.k, k) {
			return fmt.Errorf("invalid key, index=%d", i)
		}
		if !bytes.Equal(kv.v, v) {
			return fmt.Errorf("invalid value, index=%d", i)
		}
		return nil
	}
	f := func(ktr uint8, k, v []byte) bool {
		kt := keyType(ktr % 2)
		if kt == keyTypeVal {
			batch.Put(k, v)
			rbatch.Put(k, v)
			kvs = append(kvs, batchKV{kt: kt, k: k, v: v})
			internalLen += len(k) + len(v) + 8
		} else {
			batch.Delete(k)
			rbatch.Delete(k)
			kvs = append(kvs, batchKV{kt: kt, k: k})
			internalLen += len(k) + 8
		}
		if batch.Len() != len(kvs) {
			t.Logf("batch.Len: %d vs %d", len(kvs), batch.Len())
			return false
		}
		if batch.internalLen != internalLen {
			t.Logf("abatch.internalLen: %d vs %d", internalLen, batch.internalLen)
			return false
		}
		if len(kvs)%1000 == 0 {
			if err := batch.replayInternal(testBatch); err != nil {
				t.Logf("batch.replayInternal: %v", err)
				return false
			}

			abatch.append(rbatch)
			rbatch.Reset()
			if abatch.Len() != len(kvs) {
				t.Logf("abatch.Len: %d vs %d", len(kvs), abatch.Len())
				return false
			}
			if abatch.internalLen != internalLen {
				t.Logf("abatch.internalLen: %d vs %d", internalLen, abatch.internalLen)
				return false
			}
			if err := abatch.replayInternal(testBatch); err != nil {
				t.Logf("abatch.replayInternal: %v", err)
				return false
			}

			nbatch := new(Batch)
			if err := nbatch.Load(batch.Dump()); err != nil {
				t.Logf("nbatch.Load: %v", err)
				return false
			}
			if nbatch.Len() != len(kvs) {
				t.Logf("nbatch.Len: %d vs %d", len(kvs), nbatch.Len())
				return false
			}
			if nbatch.internalLen != internalLen {
				t.Logf("nbatch.internalLen: %d vs %d", internalLen, nbatch.internalLen)
				return false
			}
			if err := nbatch.replayInternal(testBatch); err != nil {
				t.Logf("nbatch.replayInternal: %v", err)
				return false
			}
		}
		if len(kvs)%10000 == 0 {
			nbatch := new(Batch)
			if err := batch.Replay(nbatch); err != nil {
				t.Logf("batch.Replay: %v", err)
				return false
			}
			if nbatch.Len() != len(kvs) {
				t.Logf("nbatch.Len: %d vs %d", len(kvs), nbatch.Len())
				return false
			}
			if nbatch.internalLen != internalLen {
				t.Logf("nbatch.internalLen: %d vs %d", internalLen, nbatch.internalLen)
				return false
			}
			if err := nbatch.replayInternal(testBatch); err != nil {
				t.Logf("nbatch.replayInternal: %v", err)
				return false
			}
		}
		return true
	}
	config := &quick.Config{
		MaxCount: 40000,
		Rand:     testutil.NewRand(),
	}
	if err := quick.Check(f, config); err != nil {
		t.Error(err)
	}
	t.Logf("length=%d internalLen=%d", len(kvs), internalLen)
}

func BenchmarkDefaultBatchWrite(b *testing.B) {
	benchmarkBatchWrite(b, nil)
}

func BenchmarkFastAllocationBatchWrite(b *testing.B) {
	benchmarkBatchWrite(b, &BatchConfig{
		GrowLimit: 10 * batchGrowLimit,
	})
}

func benchmarkBatchWrite(b *testing.B, config *BatchConfig) {
	var (
		keys [][]byte
		vals [][]byte
		r    = rand.New(rand.NewSource(1337))
	)
	for i := 0; i < 50000; i++ {
		keys = append(keys, randomString(r, 32))
		vals = append(vals, randomString(r, 100))
	}
	b.ResetTimer()
	for round := 0; round < b.N; round++ {
		batch := MakeBatchWithConfig(config)
		for i := 0; i < len(keys); i++ {
			batch.Put(keys[i], vals[i])
		}
	}
	b.ReportAllocs()
}
```

## File: `leveldb/bench_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"bytes"
	"fmt"
	"math/rand"
	"os"
	"path/filepath"
	"runtime"
	"sync/atomic"
	"testing"

	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

func randomString(r *rand.Rand, n int) []byte {
	b := new(bytes.Buffer)
	for i := 0; i < n; i++ {
		b.WriteByte(' ' + byte(r.Intn(95)))
	}
	return b.Bytes()
}

func compressibleStr(r *rand.Rand, frac float32, n int) []byte {
	nn := int(float32(n) * frac)
	rb := randomString(r, nn)
	b := make([]byte, 0, n+nn)
	for len(b) < n {
		b = append(b, rb...)
	}
	return b[:n]
}

type valueGen struct {
	src []byte
	pos int
}

func newValueGen(frac float32) *valueGen {
	v := new(valueGen)
	r := rand.New(rand.NewSource(301))
	v.src = make([]byte, 0, 1048576+100)
	for len(v.src) < 1048576 {
		v.src = append(v.src, compressibleStr(r, frac, 100)...)
	}
	return v
}

func (v *valueGen) get(n int) []byte {
	if v.pos+n > len(v.src) {
		v.pos = 0
	}
	v.pos += n
	return v.src[v.pos-n : v.pos]
}

var benchDB = filepath.Join(os.TempDir(), fmt.Sprintf("goleveldbbench-%d", os.Getuid()))

type dbBench struct {
	b    *testing.B
	stor storage.Storage
	db   *DB

	o  *opt.Options
	ro *opt.ReadOptions
	wo *opt.WriteOptions

	keys, values [][]byte
}

func openDBBench(b *testing.B, noCompress bool) *dbBench {
	_, err := os.Stat(benchDB)
	if err == nil {
		err = os.RemoveAll(benchDB)
		if err != nil {
			b.Fatal("cannot remove old db: ", err)
		}
	}

	p := &dbBench{
		b:  b,
		o:  &opt.Options{},
		ro: &opt.ReadOptions{},
		wo: &opt.WriteOptions{},
	}
	p.stor, err = storage.OpenFile(benchDB, false)
	if err != nil {
		b.Fatal("cannot open stor: ", err)
	}
	if noCompress {
		p.o.Compression = opt.NoCompression
	}

	p.db, err = Open(p.stor, p.o)
	if err != nil {
		b.Fatal("cannot open db: ", err)
	}

	return p
}

func (p *dbBench) reopen() {
	p.db.Close()
	var err error
	p.db, err = Open(p.stor, p.o)
	if err != nil {
		p.b.Fatal("Reopen: got error: ", err)
	}
}

func (p *dbBench) populate(n int) {
	p.keys, p.values = make([][]byte, n), make([][]byte, n)
	v := newValueGen(0.5)
	for i := range p.keys {
		p.keys[i], p.values[i] = []byte(fmt.Sprintf("%016d", i)), v.get(100)
	}
}

func (p *dbBench) randomize() {
	m := len(p.keys)
	times := m * 2
	r1, r2 := rand.New(rand.NewSource(0xdeadbeef)), rand.New(rand.NewSource(0xbeefface))
	for n := 0; n < times; n++ {
		i, j := r1.Int()%m, r2.Int()%m
		if i == j {
			continue
		}
		p.keys[i], p.keys[j] = p.keys[j], p.keys[i]
		p.values[i], p.values[j] = p.values[j], p.values[i]
	}
}

func (p *dbBench) writes(perBatch int) {
	b := p.b
	db := p.db

	n := len(p.keys)
	m := n / perBatch
	if n%perBatch > 0 {
		m++
	}
	batches := make([]Batch, m)
	j := 0
	for i := range batches {
		first := true
		for ; j < n && ((j+1)%perBatch != 0 || first); j++ {
			first = false
			batches[i].Put(p.keys[j], p.values[j])
		}
	}
	runtime.GC()

	b.ResetTimer()
	b.StartTimer()
	for i := range batches {
		err := db.Write(&(batches[i]), p.wo)
		if err != nil {
			b.Fatal("write failed: ", err)
		}
	}
	b.StopTimer()
	b.SetBytes(116)
}

func (p *dbBench) gc() {
	p.keys, p.values = nil, nil
	runtime.GC()
}

func (p *dbBench) puts() {
	b := p.b
	db := p.db

	b.ResetTimer()
	b.StartTimer()
	for i := range p.keys {
		err := db.Put(p.keys[i], p.values[i], p.wo)
		if err != nil {
			b.Fatal("put failed: ", err)
		}
	}
	b.StopTimer()
	b.SetBytes(116)
}

func (p *dbBench) fill() {
	b := p.b
	db := p.db

	perBatch := 10000
	batch := new(Batch)
	for i, n := 0, len(p.keys); i < n; {
		first := true
		for ; i < n && ((i+1)%perBatch != 0 || first); i++ {
			first = false
			batch.Put(p.keys[i], p.values[i])
		}
		err := db.Write(batch, p.wo)
		if err != nil {
			b.Fatal("write failed: ", err)
		}
		batch.Reset()
	}
}

func (p *dbBench) gets() {
	b := p.b
	db := p.db

	b.ResetTimer()
	for i := range p.keys {
		_, err := db.Get(p.keys[i], p.ro)
		if err != nil {
			b.Error("got error: ", err)
		}
	}
	b.StopTimer()
}

func (p *dbBench) seeks() {
	b := p.b

	iter := p.newIter()
	defer iter.Release()
	b.ResetTimer()
	for i := range p.keys {
		if !iter.Seek(p.keys[i]) {
			b.Error("value not found for: ", string(p.keys[i]))
		}
	}
	b.StopTimer()
}

func (p *dbBench) newIter() iterator.Iterator {
	iter := p.db.NewIterator(nil, p.ro)
	err := iter.Error()
	if err != nil {
		p.b.Fatal("cannot create iterator: ", err)
	}
	return iter
}

func (p *dbBench) close() {
	if bp, err := p.db.GetProperty("leveldb.blockpool"); err == nil {
		p.b.Log("Block pool stats: ", bp)
	}
	p.db.Close()
	p.stor.Close()
	os.RemoveAll(benchDB)
	p.db = nil
	p.keys = nil
	p.values = nil
	runtime.GC()
}

func BenchmarkDBWrite(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.writes(1)
	p.close()
}

func BenchmarkDBWriteBatch(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.writes(1000)
	p.close()
}

func BenchmarkDBWriteUncompressed(b *testing.B) {
	p := openDBBench(b, true)
	p.populate(b.N)
	p.writes(1)
	p.close()
}

func BenchmarkDBWriteBatchUncompressed(b *testing.B) {
	p := openDBBench(b, true)
	p.populate(b.N)
	p.writes(1000)
	p.close()
}

func BenchmarkDBWriteRandom(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.randomize()
	p.writes(1)
	p.close()
}

func BenchmarkDBWriteRandomSync(b *testing.B) {
	p := openDBBench(b, false)
	p.wo.Sync = true
	p.populate(b.N)
	p.writes(1)
	p.close()
}

func BenchmarkDBOverwrite(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.writes(1)
	p.writes(1)
	p.close()
}

func BenchmarkDBOverwriteRandom(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.writes(1)
	p.randomize()
	p.writes(1)
	p.close()
}

func BenchmarkDBPut(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.puts()
	p.close()
}

func BenchmarkDBRead(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.gc()

	iter := p.newIter()
	b.ResetTimer()
	for iter.Next() {
	}
	iter.Release()
	b.StopTimer()
	b.SetBytes(116)
	p.close()
}

func BenchmarkDBReadGC(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()

	iter := p.newIter()
	b.ResetTimer()
	for iter.Next() {
	}
	iter.Release()
	b.StopTimer()
	b.SetBytes(116)
	p.close()
}

func BenchmarkDBReadUncompressed(b *testing.B) {
	p := openDBBench(b, true)
	p.populate(b.N)
	p.fill()
	p.gc()

	iter := p.newIter()
	b.ResetTimer()
	for iter.Next() {
	}
	iter.Release()
	b.StopTimer()
	b.SetBytes(116)
	p.close()
}

func BenchmarkDBReadTable(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.reopen()
	p.gc()

	iter := p.newIter()
	b.ResetTimer()
	for iter.Next() {
	}
	iter.Release()
	b.StopTimer()
	b.SetBytes(116)
	p.close()
}

func BenchmarkDBReadReverse(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.gc()

	iter := p.newIter()
	b.ResetTimer()
	iter.Last()
	for iter.Prev() {
	}
	iter.Release()
	b.StopTimer()
	b.SetBytes(116)
	p.close()
}

func BenchmarkDBReadReverseTable(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.reopen()
	p.gc()

	iter := p.newIter()
	b.ResetTimer()
	iter.Last()
	for iter.Prev() {
	}
	iter.Release()
	b.StopTimer()
	b.SetBytes(116)
	p.close()
}

func BenchmarkDBSeek(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.seeks()
	p.close()
}

func BenchmarkDBSeekRandom(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.randomize()
	p.seeks()
	p.close()
}

func BenchmarkDBGet(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.gets()
	p.close()
}

func BenchmarkDBGetRandom(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.randomize()
	p.gets()
	p.close()
}

func BenchmarkDBReadConcurrent(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.gc()
	defer p.close()

	b.ResetTimer()
	b.SetBytes(116)

	b.RunParallel(func(pb *testing.PB) {
		iter := p.newIter()
		defer iter.Release()
		for pb.Next() && iter.Next() {
		}
	})
}

func BenchmarkDBReadConcurrent2(b *testing.B) {
	p := openDBBench(b, false)
	p.populate(b.N)
	p.fill()
	p.gc()
	defer p.close()

	b.ResetTimer()
	b.SetBytes(116)

	var dir uint32
	b.RunParallel(func(pb *testing.PB) {
		iter := p.newIter()
		defer iter.Release()
		if atomic.AddUint32(&dir, 1)%2 == 0 {
			for pb.Next() && iter.Next() {
			}
		} else {
			if pb.Next() && iter.Last() {
				for pb.Next() && iter.Prev() {
				}
			}
		}
	})
}
```

## File: `leveldb/comparer.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"github.com/syndtr/goleveldb/leveldb/comparer"
)

type iComparer struct {
	ucmp comparer.Comparer
}

func (icmp *iComparer) uName() string {
	return icmp.ucmp.Name()
}

func (icmp *iComparer) uCompare(a, b []byte) int {
	return icmp.ucmp.Compare(a, b)
}

func (icmp *iComparer) uSeparator(dst, a, b []byte) []byte {
	return icmp.ucmp.Separator(dst, a, b)
}

func (icmp *iComparer) uSuccessor(dst, b []byte) []byte {
	return icmp.ucmp.Successor(dst, b)
}

func (icmp *iComparer) Name() string {
	return icmp.uName()
}

func (icmp *iComparer) Compare(a, b []byte) int {
	x := icmp.uCompare(internalKey(a).ukey(), internalKey(b).ukey())
	if x == 0 {
		if m, n := internalKey(a).num(), internalKey(b).num(); m > n {
			return -1
		} else if m < n {
			return 1
		}
	}
	return x
}

func (icmp *iComparer) Separator(dst, a, b []byte) []byte {
	ua, ub := internalKey(a).ukey(), internalKey(b).ukey()
	dst = icmp.uSeparator(dst, ua, ub)
	if dst != nil && len(dst) < len(ua) && icmp.uCompare(ua, dst) < 0 {
		// Append earliest possible number.
		return append(dst, keyMaxNumBytes...)
	}
	return nil
}

func (icmp *iComparer) Successor(dst, b []byte) []byte {
	ub := internalKey(b).ukey()
	dst = icmp.uSuccessor(dst, ub)
	if dst != nil && len(dst) < len(ub) && icmp.uCompare(ub, dst) < 0 {
		// Append earliest possible number.
		return append(dst, keyMaxNumBytes...)
	}
	return nil
}
```

## File: `leveldb/corrupt_test.go`
```go
// Copyright (c) 2013, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"bytes"
	"fmt"
	"io"
	"math/rand"
	"testing"
	"time"

	"github.com/syndtr/goleveldb/leveldb/filter"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

const ctValSize = 1000

type dbCorruptHarness struct {
	dbHarness
}

func newDbCorruptHarnessWopt(t *testing.T, o *opt.Options) *dbCorruptHarness {
	h := new(dbCorruptHarness)
	h.init(t, o)
	return h
}

func newDbCorruptHarness(t *testing.T) *dbCorruptHarness {
	return newDbCorruptHarnessWopt(t, &opt.Options{
		BlockCacheCapacity: 100,
		Strict:             opt.StrictJournalChecksum,
	})
}

func (h *dbCorruptHarness) recover() {
	p := &h.dbHarness
	t := p.t

	var err error
	p.db, err = Recover(h.stor, h.o)
	if err != nil {
		t.Fatal("Repair: got error: ", err)
	}
}

func (h *dbCorruptHarness) build(n int) {
	p := &h.dbHarness
	t := p.t
	db := p.db

	batch := new(Batch)
	for i := 0; i < n; i++ {
		batch.Reset()
		batch.Put(tkey(i), tval(i, ctValSize))
		err := db.Write(batch, p.wo)
		if err != nil {
			t.Fatal("write error: ", err)
		}
	}
}

func (h *dbCorruptHarness) buildShuffled(n int, rnd *rand.Rand) {
	p := &h.dbHarness
	t := p.t
	db := p.db

	batch := new(Batch)
	for i := range rnd.Perm(n) {
		batch.Reset()
		batch.Put(tkey(i), tval(i, ctValSize))
		err := db.Write(batch, p.wo)
		if err != nil {
			t.Fatal("write error: ", err)
		}
	}
}

func (h *dbCorruptHarness) deleteRand(n, max int, rnd *rand.Rand) {
	p := &h.dbHarness
	t := p.t
	db := p.db

	batch := new(Batch)
	for i := 0; i < n; i++ {
		batch.Reset()
		batch.Delete(tkey(rnd.Intn(max)))
		err := db.Write(batch, p.wo)
		if err != nil {
			t.Fatal("write error: ", err)
		}
	}
}

func (h *dbCorruptHarness) corrupt(ft storage.FileType, fi, offset, n int) {
	p := &h.dbHarness
	t := p.t

	fds, _ := p.stor.List(ft)
	sortFds(fds)
	if fi < 0 {
		fi = len(fds) - 1
	}
	if fi >= len(fds) {
		t.Fatalf("no such file with type %q with index %d", ft, fi)
	}

	fd := fds[fi]
	r, err := h.stor.Open(fd)
	if err != nil {
		t.Fatal("cannot open file: ", err)
	}
	x, err := r.Seek(0, 2)
	if err != nil {
		t.Fatal("cannot query file size: ", err)
	}
	m := int(x)
	if _, err := r.Seek(0, 0); err != nil {
		t.Fatal(err)
	}

	if offset < 0 {
		if -offset > m {
			offset = 0
		} else {
			offset = m + offset
		}
	}
	if offset > m {
		offset = m
	}
	if offset+n > m {
		n = m - offset
	}

	buf := make([]byte, m)
	_, err = io.ReadFull(r, buf)
	if err != nil {
		t.Fatal("cannot read file: ", err)
	}
	r.Close()

	for i := 0; i < n; i++ {
		buf[offset+i] ^= 0x80
	}

	err = h.stor.Remove(fd)
	if err != nil {
		t.Fatal("cannot remove old file: ", err)
	}
	w, err := h.stor.Create(fd)
	if err != nil {
		t.Fatal("cannot create new file: ", err)
	}
	_, err = w.Write(buf)
	if err != nil {
		t.Fatal("cannot write new file: ", err)
	}
	w.Close()
}

func (h *dbCorruptHarness) forceRemoveAll(ft storage.FileType) {
	fds, err := h.stor.List(ft)
	if err != nil {
		h.t.Fatal("get files: ", err)
	}
	for _, fd := range fds {
		if err := h.stor.ForceRemove(fd); err != nil {
			h.t.Error("remove file: ", err)
		}
	}
}

func (h *dbCorruptHarness) removeOne(ft storage.FileType) {
	fds, err := h.stor.List(ft)
	if err != nil {
		h.t.Fatal("get files: ", err)
	}
	fd := fds[rand.Intn(len(fds))]
	h.t.Logf("removing file @%d", fd.Num)
	if err := h.stor.Remove(fd); err != nil {
		h.t.Error("remove file: ", err)
	}
}

func (h *dbCorruptHarness) check(min, max int) {
	p := &h.dbHarness
	t := p.t
	db := p.db

	var n, badk, badv, missed, good int
	iter := db.NewIterator(nil, p.ro)
	for iter.Next() {
		k := 0
		fmt.Sscanf(string(iter.Key()), "%d", &k)
		if k < n {
			badk++
			continue
		}
		missed += k - n
		n = k + 1
		if !bytes.Equal(iter.Value(), tval(k, ctValSize)) {
			badv++
		} else {
			good++
		}
	}
	err := iter.Error()
	iter.Release()
	t.Logf("want=%d..%d got=%d badkeys=%d badvalues=%d missed=%d, err=%v",
		min, max, good, badk, badv, missed, err)
	if good < min || good > max {
		t.Errorf("good entries number not in range")
	}
}

func TestCorruptDB_Journal(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.build(100)
	h.check(100, 100)
	h.closeDB()
	h.corrupt(storage.TypeJournal, -1, 19, 1)
	h.corrupt(storage.TypeJournal, -1, 32*1024+1000, 1)

	h.openDB()
	h.check(36, 36)
}

func TestCorruptDB_Table(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.build(100)
	h.compactMem()
	h.compactRangeAt(0, "", "")
	h.compactRangeAt(1, "", "")
	h.closeDB()
	h.corrupt(storage.TypeTable, -1, 100, 1)

	h.openDB()
	h.check(99, 99)
}

func TestCorruptDB_TableIndex(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.build(10000)
	h.compactMem()
	h.closeDB()
	h.corrupt(storage.TypeTable, -1, -2000, 500)

	h.openDB()
	h.check(5000, 9999)
}

func TestCorruptDB_MissingManifest(t *testing.T) {
	rnd := rand.New(rand.NewSource(0x0badda7a))
	h := newDbCorruptHarnessWopt(t, &opt.Options{
		BlockCacheCapacity: 100,
		Strict:             opt.StrictJournalChecksum,
		WriteBuffer:        1000 * 60,
	})
	defer h.close()

	h.build(1000)
	h.compactMem()
	h.buildShuffled(1000, rnd)
	h.compactMem()
	h.deleteRand(500, 1000, rnd)
	h.compactMem()
	h.buildShuffled(1000, rnd)
	h.compactMem()
	h.deleteRand(500, 1000, rnd)
	h.compactMem()
	h.buildShuffled(1000, rnd)
	h.compactMem()
	h.closeDB()

	h.forceRemoveAll(storage.TypeManifest)
	h.openAssert(false)

	h.recover()
	h.check(1000, 1000)
	h.build(1000)
	h.compactMem()
	h.compactRange("", "")
	h.closeDB()

	h.recover()
	h.check(1000, 1000)
}

func TestCorruptDB_SequenceNumberRecovery(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.put("foo", "v1")
	h.put("foo", "v2")
	h.put("foo", "v3")
	h.put("foo", "v4")
	h.put("foo", "v5")
	h.closeDB()

	h.recover()
	h.getVal("foo", "v5")
	h.put("foo", "v6")
	h.getVal("foo", "v6")

	h.reopenDB()
	h.getVal("foo", "v6")
}

func TestCorruptDB_SequenceNumberRecoveryTable(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.put("foo", "v1")
	h.put("foo", "v2")
	h.put("foo", "v3")
	h.compactMem()
	h.put("foo", "v4")
	h.put("foo", "v5")
	h.compactMem()
	h.closeDB()

	h.recover()
	h.getVal("foo", "v5")
	h.put("foo", "v6")
	h.getVal("foo", "v6")

	h.reopenDB()
	h.getVal("foo", "v6")
}

func TestCorruptDB_CorruptedManifest(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.put("foo", "hello")
	h.compactMem()
	h.compactRange("", "")
	h.closeDB()
	h.corrupt(storage.TypeManifest, -1, 0, 1000)
	h.openAssert(false)

	h.recover()
	h.getVal("foo", "hello")
}

func TestCorruptDB_CompactionInputError(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.build(10)
	h.compactMem()
	h.closeDB()
	h.corrupt(storage.TypeTable, -1, 100, 1)

	h.openDB()
	h.check(9, 9)

	h.build(10000)
	h.check(10000, 10000)
}

func TestCorruptDB_UnrelatedKeys(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.build(10)
	h.compactMem()
	h.closeDB()
	h.corrupt(storage.TypeTable, -1, 100, 1)

	h.openDB()
	h.put(string(tkey(1000)), string(tval(1000, ctValSize)))
	h.getVal(string(tkey(1000)), string(tval(1000, ctValSize)))
	h.compactMem()
	h.getVal(string(tkey(1000)), string(tval(1000, ctValSize)))
}

func TestCorruptDB_Level0NewerFileHasOlderSeqnum(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.put("a", "v1")
	h.put("b", "v1")
	h.compactMem()
	h.put("a", "v2")
	h.put("b", "v2")
	h.compactMem()
	h.put("a", "v3")
	h.put("b", "v3")
	h.compactMem()
	h.put("c", "v0")
	h.put("d", "v0")
	h.compactMem()
	h.compactRangeAt(1, "", "")
	h.closeDB()

	h.recover()
	h.getVal("a", "v3")
	h.getVal("b", "v3")
	h.getVal("c", "v0")
	h.getVal("d", "v0")
}

func TestCorruptDB_RecoverInvalidSeq_Issue53(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.put("a", "v1")
	h.put("b", "v1")
	h.compactMem()
	h.put("a", "v2")
	h.put("b", "v2")
	h.compactMem()
	h.put("a", "v3")
	h.put("b", "v3")
	h.compactMem()
	h.put("c", "v0")
	h.put("d", "v0")
	h.compactMem()
	h.compactRangeAt(0, "", "")
	h.closeDB()

	h.recover()
	h.getVal("a", "v3")
	h.getVal("b", "v3")
	h.getVal("c", "v0")
	h.getVal("d", "v0")
}

func TestCorruptDB_MissingTableFiles(t *testing.T) {
	h := newDbCorruptHarness(t)
	defer h.close()

	h.put("a", "v1")
	h.put("b", "v1")
	h.compactMem()
	h.put("c", "v2")
	h.put("d", "v2")
	h.compactMem()
	h.put("e", "v3")
	h.put("f", "v3")
	h.closeDB()

	h.removeOne(storage.TypeTable)
	h.openAssert(false)
}

func TestCorruptDB_RecoverTable(t *testing.T) {
	h := newDbCorruptHarnessWopt(t, &opt.Options{
		WriteBuffer:         112 * opt.KiB,
		CompactionTableSize: 90 * opt.KiB,
		Filter:              filter.NewBloomFilter(10),
	})
	defer h.close()

	h.build(1000)
	h.compactMem()
	h.compactRangeAt(0, "", "")
	h.compactRangeAt(1, "", "")
	seq := h.db.seq
	time.Sleep(100 * time.Millisecond) // Wait lazy reference finish tasks
	h.closeDB()
	h.corrupt(storage.TypeTable, 0, 1000, 1)
	h.corrupt(storage.TypeTable, 3, 10000, 1)
	// Corrupted filter shouldn't affect recovery.
	h.corrupt(storage.TypeTable, 3, 113888, 10)
	h.corrupt(storage.TypeTable, -1, 20000, 1)

	h.recover()
	if h.db.seq != seq {
		t.Errorf("invalid seq, want=%d got=%d", seq, h.db.seq)
	}
	h.check(985, 985)
}
```

## File: `leveldb/db.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"container/list"
	"fmt"
	"io"
	"os"
	"runtime"
	"strings"
	"sync"
	"sync/atomic"
	"time"

	"github.com/syndtr/goleveldb/leveldb/cache"
	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/journal"
	"github.com/syndtr/goleveldb/leveldb/memdb"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/table"
	"github.com/syndtr/goleveldb/leveldb/util"
)

// DB is a LevelDB database.
type DB struct {
	// Need 64-bit alignment.
	seq uint64

	// Stats. Need 64-bit alignment.
	cWriteDelay            int64 // The cumulative duration of write delays
	cWriteDelayN           int32 // The cumulative number of write delays
	inWritePaused          int32 // The indicator whether write operation is paused by compaction
	aliveSnaps, aliveIters int32

	// Compaction statistic
	memComp       uint32 // The cumulative number of memory compaction
	level0Comp    uint32 // The cumulative number of level0 compaction
	nonLevel0Comp uint32 // The cumulative number of non-level0 compaction
	seekComp      uint32 // The cumulative number of seek compaction

	// Session.
	s *session

	// MemDB.
	memMu           sync.RWMutex
	memPool         chan *memdb.DB
	mem, frozenMem  *memDB
	journal         *journal.Writer
	journalWriter   storage.Writer
	journalFd       storage.FileDesc
	frozenJournalFd storage.FileDesc
	frozenSeq       uint64

	// Snapshot.
	snapsMu   sync.Mutex
	snapsList *list.List

	// Write.
	batchPool    sync.Pool
	writeMergeC  chan writeMerge
	writeMergedC chan bool
	writeLockC   chan struct{}
	writeAckC    chan error
	writeDelay   time.Duration
	writeDelayN  int
	tr           *Transaction

	// Compaction.
	compCommitLk     sync.Mutex
	tcompCmdC        chan cCmd
	tcompPauseC      chan chan<- struct{}
	mcompCmdC        chan cCmd
	compErrC         chan error
	compPerErrC      chan error
	compErrSetC      chan error
	compWriteLocking bool
	compStats        cStats
	memdbMaxLevel    int // For testing.

	// Close.
	closeW sync.WaitGroup
	closeC chan struct{}
	closed uint32
	closer io.Closer
}

func openDB(s *session) (*DB, error) {
	s.log("db@open opening")
	start := time.Now()
	db := &DB{
		s: s,
		// Initial sequence
		seq: s.stSeqNum,
		// MemDB
		memPool: make(chan *memdb.DB, 1),
		// Snapshot
		snapsList: list.New(),
		// Write
		batchPool:    sync.Pool{New: newBatch},
		writeMergeC:  make(chan writeMerge),
		writeMergedC: make(chan bool),
		writeLockC:   make(chan struct{}, 1),
		writeAckC:    make(chan error),
		// Compaction
		tcompCmdC:   make(chan cCmd),
		tcompPauseC: make(chan chan<- struct{}),
		mcompCmdC:   make(chan cCmd),
		compErrC:    make(chan error),
		compPerErrC: make(chan error),
		compErrSetC: make(chan error),
		// Close
		closeC: make(chan struct{}),
	}

	// Read-only mode.
	readOnly := s.o.GetReadOnly()

	if readOnly {
		// Recover journals (read-only mode).
		if err := db.recoverJournalRO(); err != nil {
			return nil, err
		}
	} else {
		// Recover journals.
		if err := db.recoverJournal(); err != nil {
			return nil, err
		}

		// Remove any obsolete files.
		if err := db.checkAndCleanFiles(); err != nil {
			// Close journal.
			if db.journal != nil {
				db.journal.Close()
				db.journalWriter.Close()
			}
			return nil, err
		}
	}

	// Doesn't need to be included in the wait group.
	go db.compactionError()
	go db.mpoolDrain()

	if readOnly {
		if err := db.SetReadOnly(); err != nil {
			return nil, err
		}
	} else {
		db.closeW.Add(2)
		go db.tCompaction()
		go db.mCompaction()
		// go db.jWriter()
	}

	s.logf("db@open done T·%v", time.Since(start))

	runtime.SetFinalizer(db, (*DB).Close)
	return db, nil
}

// Open opens or creates a DB for the given storage.
// The DB will be created if not exist, unless ErrorIfMissing is true.
// Also, if ErrorIfExist is true and the DB exist Open will returns
// os.ErrExist error.
//
// Open will return an error with type of ErrCorrupted if corruption
// detected in the DB. Use errors.IsCorrupted to test whether an error is
// due to corruption. Corrupted DB can be recovered with Recover function.
//
// The returned DB instance is safe for concurrent use.
// The DB must be closed after use, by calling Close method.
func Open(stor storage.Storage, o *opt.Options) (db *DB, err error) {
	s, err := newSession(stor, o)
	if err != nil {
		return
	}
	defer func() {
		if err != nil {
			s.close()
			s.release()
		}
	}()

	err = s.recover()
	if err != nil {
		if !os.IsNotExist(err) || s.o.GetErrorIfMissing() || s.o.GetReadOnly() {
			return
		}
		err = s.create()
		if err != nil {
			return
		}
	} else if s.o.GetErrorIfExist() {
		err = os.ErrExist
		return
	}

	return openDB(s)
}

// OpenFile opens or creates a DB for the given path.
// The DB will be created if not exist, unless ErrorIfMissing is true.
// Also, if ErrorIfExist is true and the DB exist OpenFile will returns
// os.ErrExist error.
//
// OpenFile uses standard file-system backed storage implementation as
// described in the leveldb/storage package.
//
// OpenFile will return an error with type of ErrCorrupted if corruption
// detected in the DB. Use errors.IsCorrupted to test whether an error is
// due to corruption. Corrupted DB can be recovered with Recover function.
//
// The returned DB instance is safe for concurrent use.
// The DB must be closed after use, by calling Close method.
func OpenFile(path string, o *opt.Options) (db *DB, err error) {
	stor, err := storage.OpenFile(path, o.GetReadOnly())
	if err != nil {
		return
	}
	db, err = Open(stor, o)
	if err != nil {
		stor.Close()
	} else {
		db.closer = stor
	}
	return
}

// Recover recovers and opens a DB with missing or corrupted manifest files
// for the given storage. It will ignore any manifest files, valid or not.
// The DB must already exist or it will returns an error.
// Also, Recover will ignore ErrorIfMissing and ErrorIfExist options.
//
// The returned DB instance is safe for concurrent use.
// The DB must be closed after use, by calling Close method.
func Recover(stor storage.Storage, o *opt.Options) (db *DB, err error) {
	s, err := newSession(stor, o)
	if err != nil {
		return
	}
	defer func() {
		if err != nil {
			s.close()
			s.release()
		}
	}()

	err = recoverTable(s, o)
	if err != nil {
		return
	}
	return openDB(s)
}

// RecoverFile recovers and opens a DB with missing or corrupted manifest files
// for the given path. It will ignore any manifest files, valid or not.
// The DB must already exist or it will returns an error.
// Also, Recover will ignore ErrorIfMissing and ErrorIfExist options.
//
// RecoverFile uses standard file-system backed storage implementation as described
// in the leveldb/storage package.
//
// The returned DB instance is safe for concurrent use.
// The DB must be closed after use, by calling Close method.
func RecoverFile(path string, o *opt.Options) (db *DB, err error) {
	stor, err := storage.OpenFile(path, false)
	if err != nil {
		return
	}
	db, err = Recover(stor, o)
	if err != nil {
		stor.Close()
	} else {
		db.closer = stor
	}
	return
}

func recoverTable(s *session, o *opt.Options) error {
	o = dupOptions(o)
	// Mask StrictReader, lets StrictRecovery doing its job.
	o.Strict &= ^opt.StrictReader

	// Get all tables and sort it by file number.
	fds, err := s.stor.List(storage.TypeTable)
	if err != nil {
		return err
	}
	sortFds(fds)

	var (
		maxSeq                                                            uint64
		recoveredKey, goodKey, corruptedKey, corruptedBlock, droppedTable int

		// We will drop corrupted table.
		strict = o.GetStrict(opt.StrictRecovery)
		noSync = o.GetNoSync()

		rec   = &sessionRecord{}
		bpool = util.NewBufferPool(o.GetBlockSize() + 5)
	)
	buildTable := func(iter iterator.Iterator) (tmpFd storage.FileDesc, size int64, err error) {
		tmpFd = s.newTemp()
		writer, err := s.stor.Create(tmpFd)
		if err != nil {
			return
		}
		defer func() {
			if cerr := writer.Close(); cerr != nil {
				if err == nil {
					err = cerr
				} else {
					err = fmt.Errorf("error recovering table (%v); error closing (%v)", err, cerr)
				}
			}
			if err != nil {
				if rerr := s.stor.Remove(tmpFd); rerr != nil {
					err = fmt.Errorf("error recovering table (%v); error removing (%v)", err, rerr)
				}
				tmpFd = storage.FileDesc{}
			}
		}()

		// Copy entries.
		tw := table.NewWriter(writer, o, nil, 0)
		for iter.Next() {
			key := iter.Key()
			if validInternalKey(key) {
				err = tw.Append(key, iter.Value())
				if err != nil {
					return
				}
			}
		}
		err = iter.Error()
		if err != nil && !errors.IsCorrupted(err) {
			return
		}
		err = tw.Close()
		if err != nil {
			return
		}
		if !noSync {
			err = writer.Sync()
			if err != nil {
				return
			}
		}
		size = int64(tw.BytesLen())
		return
	}
	recoverTable := func(fd storage.FileDesc) error {
		s.logf("table@recovery recovering @%d", fd.Num)
		reader, err := s.stor.Open(fd)
		if err != nil {
			return err
		}
		var closed bool
		defer func() {
			if !closed {
				reader.Close()
			}
		}()

		// Get file size.
		size, err := reader.Seek(0, 2)
		if err != nil {
			return err
		}

		var (
			tSeq                                     uint64
			tgoodKey, tcorruptedKey, tcorruptedBlock int
			imin, imax                               []byte
		)
		tr, err := table.NewReader(reader, size, fd, nil, bpool, o)
		if err != nil {
			return err
		}
		iter := tr.NewIterator(nil, nil)
		if itererr, ok := iter.(iterator.ErrorCallbackSetter); ok {
			itererr.SetErrorCallback(func(err error) {
				if errors.IsCorrupted(err) {
					s.logf("table@recovery block corruption @%d %q", fd.Num, err)
					tcorruptedBlock++
				}
			})
		}

		// Scan the table.
		for iter.Next() {
			key := iter.Key()
			_, seq, _, kerr := parseInternalKey(key)
			if kerr != nil {
				tcorruptedKey++
				continue
			}
			tgoodKey++
			if seq > tSeq {
				tSeq = seq
			}
			if imin == nil {
				imin = append([]byte(nil), key...)
			}
			imax = append(imax[:0], key...)
		}
		if err := iter.Error(); err != nil && !errors.IsCorrupted(err) {
			iter.Release()
			return err
		}
		iter.Release()

		goodKey += tgoodKey
		corruptedKey += tcorruptedKey
		corruptedBlock += tcorruptedBlock

		if strict && (tcorruptedKey > 0 || tcorruptedBlock > 0) {
			droppedTable++
			s.logf("table@recovery dropped @%d Gk·%d Ck·%d Cb·%d S·%d Q·%d", fd.Num, tgoodKey, tcorruptedKey, tcorruptedBlock, size, tSeq)
			return nil
		}

		if tgoodKey > 0 {
			if tcorruptedKey > 0 || tcorruptedBlock > 0 {
				// Rebuild the table.
				s.logf("table@recovery rebuilding @%d", fd.Num)
				iter := tr.NewIterator(nil, nil)
				tmpFd, newSize, err := buildTable(iter)
				iter.Release()
				if err != nil {
					return err
				}
				closed = true
				reader.Close()
				if err := s.stor.Rename(tmpFd, fd); err != nil {
					return err
				}
				size = newSize
			}
			if tSeq > maxSeq {
				maxSeq = tSeq
			}
			recoveredKey += tgoodKey
			// Add table to level 0.
			rec.addTable(0, fd.Num, size, imin, imax)
			s.logf("table@recovery recovered @%d Gk·%d Ck·%d Cb·%d S·%d Q·%d", fd.Num, tgoodKey, tcorruptedKey, tcorruptedBlock, size, tSeq)
		} else {
			droppedTable++
			s.logf("table@recovery unrecoverable @%d Ck·%d Cb·%d S·%d", fd.Num, tcorruptedKey, tcorruptedBlock, size)
		}

		return nil
	}

	// Recover all tables.
	if len(fds) > 0 {
		s.logf("table@recovery F·%d", len(fds))

		// Mark file number as used.
		s.markFileNum(fds[len(fds)-1].Num)

		for _, fd := range fds {
			if err := recoverTable(fd); err != nil {
				return err
			}
		}

		s.logf("table@recovery recovered F·%d N·%d Gk·%d Ck·%d Q·%d", len(fds), recoveredKey, goodKey, corruptedKey, maxSeq)
	}

	// Set sequence number.
	rec.setSeqNum(maxSeq)

	// Create new manifest.
	if err := s.create(); err != nil {
		return err
	}

	// Commit.
	return s.commit(rec, false)
}

func (db *DB) recoverJournal() error {
	// Get all journals and sort it by file number.
	rawFds, err := db.s.stor.List(storage.TypeJournal)
	if err != nil {
		return err
	}
	sortFds(rawFds)

	// Journals that will be recovered.
	var fds []storage.FileDesc
	for _, fd := range rawFds {
		if fd.Num >= db.s.stJournalNum || fd.Num == db.s.stPrevJournalNum {
			fds = append(fds, fd)
		}
	}

	var (
		ofd storage.FileDesc // Obsolete file.
		rec = &sessionRecord{}
	)

	// Recover journals.
	if len(fds) > 0 {
		db.logf("journal@recovery F·%d", len(fds))

		// Mark file number as used.
		db.s.markFileNum(fds[len(fds)-1].Num)

		var (
			// Options.
			strict      = db.s.o.GetStrict(opt.StrictJournal)
			checksum    = db.s.o.GetStrict(opt.StrictJournalChecksum)
			writeBuffer = db.s.o.GetWriteBuffer()

			jr       *journal.Reader
			mdb      = memdb.New(db.s.icmp, writeBuffer)
			buf      = &util.Buffer{}
			batchSeq uint64
			batchLen int
		)

		for _, fd := range fds {
			db.logf("journal@recovery recovering @%d", fd.Num)

			fr, err := db.s.stor.Open(fd)
			if err != nil {
				return err
			}

			// Create or reset journal reader instance.
			if jr == nil {
				jr = journal.NewReader(fr, dropper{db.s, fd}, strict, checksum)
			} else {
				// Ignore the error here
				_ = jr.Reset(fr, dropper{db.s, fd}, strict, checksum)
			}

			// Flush memdb and remove obsolete journal file.
			if !ofd.Zero() {
				if mdb.Len() > 0 {
					if _, err := db.s.flushMemdb(rec, mdb, 0); err != nil {
						fr.Close()
						return err
					}
				}

				rec.setJournalNum(fd.Num)
				rec.setSeqNum(db.seq)
				if err := db.s.commit(rec, false); err != nil {
					fr.Close()
					return err
				}
				rec.resetAddedTables()

				if err := db.s.stor.Remove(ofd); err != nil {
					fr.Close()
					return err
				}
				ofd = storage.FileDesc{}
			}

			// Replay journal to memdb.
			mdb.Reset()
			for {
				r, err := jr.Next()
				if err != nil {
					if err == io.EOF {
						break
					}

					fr.Close()
					return errors.SetFd(err, fd)
				}

				buf.Reset()
				if _, err := buf.ReadFrom(r); err != nil {
					if err == io.ErrUnexpectedEOF {
						// This is error returned due to corruption, with strict == false.
						continue
					}

					fr.Close()
					return errors.SetFd(err, fd)
				}
				batchSeq, batchLen, err = decodeBatchToMem(buf.Bytes(), db.seq, mdb)
				if err != nil {
					if !strict && errors.IsCorrupted(err) {
						db.s.logf("journal error: %v (skipped)", err)
						// We won't apply sequence number as it might be corrupted.
						continue
					}

					fr.Close()
					return errors.SetFd(err, fd)
				}

				// Save sequence number.
				db.seq = batchSeq + uint64(batchLen)

				// Flush it if large enough.
				if mdb.Size() >= writeBuffer {
					if _, err := db.s.flushMemdb(rec, mdb, 0); err != nil {
						fr.Close()
						return err
					}

					mdb.Reset()
				}
			}

			fr.Close()
			ofd = fd
		}

		// Flush the last memdb.
		if mdb.Len() > 0 {
			if _, err := db.s.flushMemdb(rec, mdb, 0); err != nil {
				return err
			}
		}
	}

	// Create a new journal.
	if _, err := db.newMem(0); err != nil {
		return err
	}

	// Commit.
	rec.setJournalNum(db.journalFd.Num)
	rec.setSeqNum(db.seq)
	if err := db.s.commit(rec, false); err != nil {
		// Close journal on error.
		if db.journal != nil {
			db.journal.Close()
			db.journalWriter.Close()
		}
		return err
	}

	// Remove the last obsolete journal file.
	if !ofd.Zero() {
		if err := db.s.stor.Remove(ofd); err != nil {
			return err
		}
	}

	return nil
}

func (db *DB) recoverJournalRO() error {
	// Get all journals and sort it by file number.
	rawFds, err := db.s.stor.List(storage.TypeJournal)
	if err != nil {
		return err
	}
	sortFds(rawFds)

	// Journals that will be recovered.
	var fds []storage.FileDesc
	for _, fd := range rawFds {
		if fd.Num >= db.s.stJournalNum || fd.Num == db.s.stPrevJournalNum {
			fds = append(fds, fd)
		}
	}

	var (
		// Options.
		strict      = db.s.o.GetStrict(opt.StrictJournal)
		checksum    = db.s.o.GetStrict(opt.StrictJournalChecksum)
		writeBuffer = db.s.o.GetWriteBuffer()

		mdb = memdb.New(db.s.icmp, writeBuffer)
	)

	// Recover journals.
	if len(fds) > 0 {
		db.logf("journal@recovery RO·Mode F·%d", len(fds))

		var (
			jr       *journal.Reader
			buf      = &util.Buffer{}
			batchSeq uint64
			batchLen int
		)

		for _, fd := range fds {
			db.logf("journal@recovery recovering @%d", fd.Num)

			fr, err := db.s.stor.Open(fd)
			if err != nil {
				return err
			}

			// Create or reset journal reader instance.
			if jr == nil {
				jr = journal.NewReader(fr, dropper{db.s, fd}, strict, checksum)
			} else {
				if err := jr.Reset(fr, dropper{db.s, fd}, strict, checksum); err != nil {
					return err
				}
			}

			// Replay journal to memdb.
			for {
				r, err := jr.Next()
				if err != nil {
					if err == io.EOF {
						break
					}

					fr.Close()
					return errors.SetFd(err, fd)
				}

				buf.Reset()
				if _, err := buf.ReadFrom(r); err != nil {
					if err == io.ErrUnexpectedEOF {
						// This is error returned due to corruption, with strict == false.
						continue
					}

					fr.Close()
					return errors.SetFd(err, fd)
				}
				batchSeq, batchLen, err = decodeBatchToMem(buf.Bytes(), db.seq, mdb)
				if err != nil {
					if !strict && errors.IsCorrupted(err) {
						db.s.logf("journal error: %v (skipped)", err)
						// We won't apply sequence number as it might be corrupted.
						continue
					}

					fr.Close()
					return errors.SetFd(err, fd)
				}

				// Save sequence number.
				db.seq = batchSeq + uint64(batchLen)
			}

			fr.Close()
		}
	}

	// Set memDB.
	db.mem = &memDB{db: db, DB: mdb, ref: 1}

	return nil
}

func memGet(mdb *memdb.DB, ikey internalKey, icmp *iComparer) (ok bool, mv []byte, err error) {
	mk, mv, err := mdb.Find(ikey)
	if err == nil {
		ukey, _, kt, kerr := parseInternalKey(mk)
		if kerr != nil {
			// Shouldn't have had happen.
			panic(kerr)
		}
		if icmp.uCompare(ukey, ikey.ukey()) == 0 {
			if kt == keyTypeDel {
				return true, nil, ErrNotFound
			}
			return true, mv, nil

		}
	} else if err != ErrNotFound {
		return true, nil, err
	}
	return
}

func (db *DB) get(auxm *memdb.DB, auxt tFiles, key []byte, seq uint64, ro *opt.ReadOptions) (value []byte, err error) {
	ikey := makeInternalKey(nil, key, seq, keyTypeSeek)

	if auxm != nil {
		if ok, mv, me := memGet(auxm, ikey, db.s.icmp); ok {
			return append([]byte(nil), mv...), me
		}
	}

	em, fm := db.getMems()
	for _, m := range [...]*memDB{em, fm} {
		if m == nil {
			continue
		}
		defer m.decref()

		if ok, mv, me := memGet(m.DB, ikey, db.s.icmp); ok {
			return append([]byte(nil), mv...), me
		}
	}

	v := db.s.version()
	value, cSched, err := v.get(auxt, ikey, ro, false)
	v.release()
	if cSched {
		// Trigger table compaction.
		db.compTrigger(db.tcompCmdC)
	}
	return
}

func nilIfNotFound(err error) error {
	if err == ErrNotFound {
		return nil
	}
	return err
}

func (db *DB) has(auxm *memdb.DB, auxt tFiles, key []byte, seq uint64, ro *opt.ReadOptions) (ret bool, err error) {
	ikey := makeInternalKey(nil, key, seq, keyTypeSeek)

	if auxm != nil {
		if ok, _, me := memGet(auxm, ikey, db.s.icmp); ok {
			return me == nil, nilIfNotFound(me)
		}
	}

	em, fm := db.getMems()
	for _, m := range [...]*memDB{em, fm} {
		if m == nil {
			continue
		}
		defer m.decref()

		if ok, _, me := memGet(m.DB, ikey, db.s.icmp); ok {
			return me == nil, nilIfNotFound(me)
		}
	}

	v := db.s.version()
	_, cSched, err := v.get(auxt, ikey, ro, true)
	v.release()
	if cSched {
		// Trigger table compaction.
		db.compTrigger(db.tcompCmdC)
	}
	if err == nil {
		ret = true
	} else if err == ErrNotFound {
		err = nil
	}
	return
}

// Get gets the value for the given key. It returns ErrNotFound if the
// DB does not contains the key.
//
// The returned slice is its own copy, it is safe to modify the contents
// of the returned slice.
// It is safe to modify the contents of the argument after Get returns.
func (db *DB) Get(key []byte, ro *opt.ReadOptions) (value []byte, err error) {
	err = db.ok()
	if err != nil {
		return
	}

	se := db.acquireSnapshot()
	defer db.releaseSnapshot(se)
	return db.get(nil, nil, key, se.seq, ro)
}

// Has returns true if the DB does contains the given key.
//
// It is safe to modify the contents of the argument after Has returns.
func (db *DB) Has(key []byte, ro *opt.ReadOptions) (ret bool, err error) {
	err = db.ok()
	if err != nil {
		return
	}

	se := db.acquireSnapshot()
	defer db.releaseSnapshot(se)
	return db.has(nil, nil, key, se.seq, ro)
}

// NewIterator returns an iterator for the latest snapshot of the
// underlying DB.
// The returned iterator is not safe for concurrent use, but it is safe to use
// multiple iterators concurrently, with each in a dedicated goroutine.
// It is also safe to use an iterator concurrently with modifying its
// underlying DB. The resultant key/value pairs are guaranteed to be
// consistent.
//
// Slice allows slicing the iterator to only contains keys in the given
// range. A nil Range.Start is treated as a key before all keys in the
// DB. And a nil Range.Limit is treated as a key after all keys in
// the DB.
//
// WARNING: Any slice returned by interator (e.g. slice returned by calling
// Iterator.Key() or Iterator.Key() methods), its content should not be modified
// unless noted otherwise.
//
// The iterator must be released after use, by calling Release method.
//
// Also read Iterator documentation of the leveldb/iterator package.
func (db *DB) NewIterator(slice *util.Range, ro *opt.ReadOptions) iterator.Iterator {
	if err := db.ok(); err != nil {
		return iterator.NewEmptyIterator(err)
	}

	se := db.acquireSnapshot()
	defer db.releaseSnapshot(se)
	// Iterator holds 'version' lock, 'version' is immutable so snapshot
	// can be released after iterator created.
	return db.newIterator(nil, nil, se.seq, slice, ro)
}

// GetSnapshot returns a latest snapshot of the underlying DB. A snapshot
// is a frozen snapshot of a DB state at a particular point in time. The
// content of snapshot are guaranteed to be consistent.
//
// The snapshot must be released after use, by calling Release method.
func (db *DB) GetSnapshot() (*Snapshot, error) {
	if err := db.ok(); err != nil {
		return nil, err
	}

	return db.newSnapshot(), nil
}

// GetProperty returns value of the given property name.
//
// Property names:
//	leveldb.num-files-at-level{n}
//		Returns the number of files at level 'n'.
//	leveldb.stats
//		Returns statistics of the underlying DB.
//	leveldb.iostats
//		Returns statistics of effective disk read and write.
//	leveldb.writedelay
//		Returns cumulative write delay caused by compaction.
//	leveldb.sstables
//		Returns sstables list for each level.
//	leveldb.blockpool
//		Returns block pool stats.
//	leveldb.cachedblock
//		Returns size of cached block.
//	leveldb.openedtables
//		Returns number of opened tables.
//	leveldb.alivesnaps
//		Returns number of alive snapshots.
//	leveldb.aliveiters
//		Returns number of alive iterators.
func (db *DB) GetProperty(name string) (value string, err error) {
	err = db.ok()
	if err != nil {
		return
	}

	const prefix = "leveldb."
	if !strings.HasPrefix(name, prefix) {
		return "", ErrNotFound
	}
	p := name[len(prefix):]

	v := db.s.version()
	defer v.release()

	numFilesPrefix := "num-files-at-level"
	switch {
	case strings.HasPrefix(p, numFilesPrefix):
		var level uint
		var rest string
		n, _ := fmt.Sscanf(p[len(numFilesPrefix):], "%d%s", &level, &rest)
		if n != 1 {
			err = ErrNotFound
		} else {
			value = fmt.Sprint(v.tLen(int(level)))
		}
	case p == "stats":
		value = "Compactions\n" +
			" Level |   Tables   |    Size(MB)   |    Time(sec)  |    Read(MB)   |   Write(MB)\n" +
			"-------+------------+---------------+---------------+---------------+---------------\n"
		var totalTables int
		var totalSize, totalRead, totalWrite int64
		var totalDuration time.Duration
		for level, tables := range v.levels {
			duration, read, write := db.compStats.getStat(level)
			if len(tables) == 0 && duration == 0 {
				continue
			}
			totalTables += len(tables)
			totalSize += tables.size()
			totalRead += read
			totalWrite += write
			totalDuration += duration
			value += fmt.Sprintf(" %3d   | %10d | %13.5f | %13.5f | %13.5f | %13.5f\n",
				level, len(tables), float64(tables.size())/1048576.0, duration.Seconds(),
				float64(read)/1048576.0, float64(write)/1048576.0)
		}
		value += "-------+------------+---------------+---------------+---------------+---------------\n"
		value += fmt.Sprintf(" Total | %10d | %13.5f | %13.5f | %13.5f | %13.5f\n",
			totalTables, float64(totalSize)/1048576.0, totalDuration.Seconds(),
			float64(totalRead)/1048576.0, float64(totalWrite)/1048576.0)
	case p == "compcount":
		value = fmt.Sprintf("MemComp:%d Level0Comp:%d NonLevel0Comp:%d SeekComp:%d", atomic.LoadUint32(&db.memComp), atomic.LoadUint32(&db.level0Comp), atomic.LoadUint32(&db.nonLevel0Comp), atomic.LoadUint32(&db.seekComp))
	case p == "iostats":
		value = fmt.Sprintf("Read(MB):%.5f Write(MB):%.5f",
			float64(db.s.stor.reads())/1048576.0,
			float64(db.s.stor.writes())/1048576.0)
	case p == "writedelay":
		writeDelayN, writeDelay := atomic.LoadInt32(&db.cWriteDelayN), time.Duration(atomic.LoadInt64(&db.cWriteDelay))
		paused := atomic.LoadInt32(&db.inWritePaused) == 1
		value = fmt.Sprintf("DelayN:%d Delay:%s Paused:%t", writeDelayN, writeDelay, paused)
	case p == "sstables":
		for level, tables := range v.levels {
			value += fmt.Sprintf("--- level %d ---\n", level)
			for _, t := range tables {
				value += fmt.Sprintf("%d:%d[%q .. %q]\n", t.fd.Num, t.size, t.imin, t.imax)
			}
		}
	case p == "blockpool":
		value = fmt.Sprintf("%v", db.s.tops.blockBuffer)
	case p == "cachedblock":
		if db.s.tops.blockCache != nil {
			value = fmt.Sprintf("%d", db.s.tops.blockCache.Size())
		} else {
			value = "<nil>"
		}
	case p == "openedtables":
		value = fmt.Sprintf("%d", db.s.tops.fileCache.Size())
	case p == "alivesnaps":
		value = fmt.Sprintf("%d", atomic.LoadInt32(&db.aliveSnaps))
	case p == "aliveiters":
		value = fmt.Sprintf("%d", atomic.LoadInt32(&db.aliveIters))
	default:
		err = ErrNotFound
	}

	return
}

// DBStats is database statistics.
type DBStats struct {
	WriteDelayCount    int32
	WriteDelayDuration time.Duration
	WritePaused        bool

	AliveSnapshots int32
	AliveIterators int32

	IOWrite uint64
	IORead  uint64

	BlockCacheSize    int
	OpenedTablesCount int

	FileCache  cache.Stats
	BlockCache cache.Stats

	LevelSizes        Sizes
	LevelTablesCounts []int
	LevelRead         Sizes
	LevelWrite        Sizes
	LevelDurations    []time.Duration

	MemComp       uint32
	Level0Comp    uint32
	NonLevel0Comp uint32
	SeekComp      uint32
}

// Stats populates s with database statistics.
func (db *DB) Stats(s *DBStats) error {
	err := db.ok()
	if err != nil {
		return err
	}

	s.IORead = db.s.stor.reads()
	s.IOWrite = db.s.stor.writes()
	s.WriteDelayCount = atomic.LoadInt32(&db.cWriteDelayN)
	s.WriteDelayDuration = time.Duration(atomic.LoadInt64(&db.cWriteDelay))
	s.WritePaused = atomic.LoadInt32(&db.inWritePaused) == 1

	s.OpenedTablesCount = db.s.tops.fileCache.Size()
	if db.s.tops.blockCache != nil {
		s.BlockCacheSize = db.s.tops.blockCache.Size()
	} else {
		s.BlockCacheSize = 0
	}

	s.FileCache = db.s.tops.fileCache.GetStats()
	if db.s.tops.blockCache != nil {
		s.BlockCache = db.s.tops.blockCache.GetStats()
	} else {
		s.BlockCache = cache.Stats{}
	}

	s.AliveIterators = atomic.LoadInt32(&db.aliveIters)
	s.AliveSnapshots = atomic.LoadInt32(&db.aliveSnaps)

	s.LevelDurations = s.LevelDurations[:0]
	s.LevelRead = s.LevelRead[:0]
	s.LevelWrite = s.LevelWrite[:0]
	s.LevelSizes = s.LevelSizes[:0]
	s.LevelTablesCounts = s.LevelTablesCounts[:0]

	v := db.s.version()
	defer v.release()

	for level, tables := range v.levels {
		duration, read, write := db.compStats.getStat(level)

		s.LevelDurations = append(s.LevelDurations, duration)
		s.LevelRead = append(s.LevelRead, read)
		s.LevelWrite = append(s.LevelWrite, write)
		s.LevelSizes = append(s.LevelSizes, tables.size())
		s.LevelTablesCounts = append(s.LevelTablesCounts, len(tables))
	}
	s.MemComp = atomic.LoadUint32(&db.memComp)
	s.Level0Comp = atomic.LoadUint32(&db.level0Comp)
	s.NonLevel0Comp = atomic.LoadUint32(&db.nonLevel0Comp)
	s.SeekComp = atomic.LoadUint32(&db.seekComp)
	return nil
}

// SizeOf calculates approximate sizes of the given key ranges.
// The length of the returned sizes are equal with the length of the given
// ranges. The returned sizes measure storage space usage, so if the user
// data compresses by a factor of ten, the returned sizes will be one-tenth
// the size of the corresponding user data size.
// The results may not include the sizes of recently written data.
func (db *DB) SizeOf(ranges []util.Range) (Sizes, error) {
	if err := db.ok(); err != nil {
		return nil, err
	}

	v := db.s.version()
	defer v.release()

	sizes := make(Sizes, 0, len(ranges))
	for _, r := range ranges {
		imin := makeInternalKey(nil, r.Start, keyMaxSeq, keyTypeSeek)
		imax := makeInternalKey(nil, r.Limit, keyMaxSeq, keyTypeSeek)
		start, err := v.offsetOf(imin)
		if err != nil {
			return nil, err
		}
		limit, err := v.offsetOf(imax)
		if err != nil {
			return nil, err
		}
		var size int64
		if limit >= start {
			size = limit - start
		}
		sizes = append(sizes, size)
	}

	return sizes, nil
}

// Close closes the DB. This will also releases any outstanding snapshot,
// abort any in-flight compaction and discard open transaction.
//
// It is not safe to close a DB until all outstanding iterators are released.
// It is valid to call Close multiple times. Other methods should not be
// called after the DB has been closed.
func (db *DB) Close() error {
	if !db.setClosed() {
		return ErrClosed
	}

	start := time.Now()
	db.log("db@close closing")

	// Clear the finalizer.
	runtime.SetFinalizer(db, nil)

	// Get compaction error.
	var err error
	select {
	case err = <-db.compErrC:
		if err == ErrReadOnly {
			err = nil
		}
	default:
	}

	// Signal all goroutines.
	close(db.closeC)

	// Discard open transaction.
	if db.tr != nil {
		db.tr.Discard()
	}

	// Acquire writer lock.
	db.writeLockC <- struct{}{}

	// Wait for all gorotines to exit.
	db.closeW.Wait()

	// Closes journal.
	if db.journal != nil {
		db.journal.Close()
		db.journalWriter.Close()
		db.journal = nil
		db.journalWriter = nil
	}

	if db.writeDelayN > 0 {
		db.logf("db@write was delayed N·%d T·%v", db.writeDelayN, db.writeDelay)
	}

	// Close session.
	db.s.close()
	db.logf("db@close done T·%v", time.Since(start))
	db.s.release()

	if db.closer != nil {
		if err1 := db.closer.Close(); err == nil {
			err = err1
		}
		db.closer = nil
	}

	// Clear memdbs.
	db.clearMems()

	return err
}
```

## File: `leveldb/db_compaction.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

var (
	errCompactionTransactExiting = errors.New("leveldb: compaction transact exiting")
)

type cStat struct {
	duration time.Duration
	read     int64
	write    int64
}

func (p *cStat) add(n *cStatStaging) {
	p.duration += n.duration
	p.read += n.read
	p.write += n.write
}

func (p *cStat) get() (duration time.Duration, read, write int64) {
	return p.duration, p.read, p.write
}

type cStatStaging struct {
	start    time.Time
	duration time.Duration
	on       bool
	read     int64
	write    int64
}

func (p *cStatStaging) startTimer() {
	if !p.on {
		p.start = time.Now()
		p.on = true
	}
}

func (p *cStatStaging) stopTimer() {
	if p.on {
		p.duration += time.Since(p.start)
		p.on = false
	}
}

type cStats struct {
	lk    sync.Mutex
	stats []cStat
}

func (p *cStats) addStat(level int, n *cStatStaging) {
	p.lk.Lock()
	if level >= len(p.stats) {
		newStats := make([]cStat, level+1)
		copy(newStats, p.stats)
		p.stats = newStats
	}
	p.stats[level].add(n)
	p.lk.Unlock()
}

func (p *cStats) getStat(level int) (duration time.Duration, read, write int64) {
	p.lk.Lock()
	defer p.lk.Unlock()
	if level < len(p.stats) {
		return p.stats[level].get()
	}
	return
}

func (db *DB) compactionError() {
	var err error
noerr:
	// No error.
	for {
		select {
		case err = <-db.compErrSetC:
			switch {
			case err == nil:
			case err == ErrReadOnly, errors.IsCorrupted(err):
				goto hasperr
			default:
				goto haserr
			}
		case <-db.closeC:
			return
		}
	}
haserr:
	// Transient error.
	for {
		select {
		case db.compErrC <- err:
		case err = <-db.compErrSetC:
			switch {
			case err == nil:
				goto noerr
			case err == ErrReadOnly, errors.IsCorrupted(err):
				goto hasperr
			default:
			}
		case <-db.closeC:
			return
		}
	}
hasperr:
	// Persistent error.
	for {
		select {
		case db.compErrC <- err:
		case db.compPerErrC <- err:
		case db.writeLockC <- struct{}{}:
			// Hold write lock, so that write won't pass-through.
			db.compWriteLocking = true
		case <-db.closeC:
			if db.compWriteLocking {
				// We should release the lock or Close will hang.
				<-db.writeLockC
			}
			return
		}
	}
}

type compactionTransactCounter int

func (cnt *compactionTransactCounter) incr() {
	*cnt++
}

type compactionTransactInterface interface {
	run(cnt *compactionTransactCounter) error
	revert() error
}

func (db *DB) compactionTransact(name string, t compactionTransactInterface) {
	defer func() {
		if x := recover(); x != nil {
			if x == errCompactionTransactExiting {
				if err := t.revert(); err != nil {
					db.logf("%s revert error %q", name, err)
				}
			}
			panic(x)
		}
	}()

	const (
		backoffMin = 1 * time.Second
		backoffMax = 8 * time.Second
		backoffMul = 2 * time.Second
	)
	var (
		backoff  = backoffMin
		backoffT = time.NewTimer(backoff)
		lastCnt  = compactionTransactCounter(0)

		disableBackoff = db.s.o.GetDisableCompactionBackoff()
	)
	for n := 0; ; n++ {
		// Check whether the DB is closed.
		if db.isClosed() {
			db.logf("%s exiting", name)
			db.compactionExitTransact()
		} else if n > 0 {
			db.logf("%s retrying N·%d", name, n)
		}

		// Execute.
		cnt := compactionTransactCounter(0)
		err := t.run(&cnt)
		if err != nil {
			db.logf("%s error I·%d %q", name, cnt, err)
		}

		// Set compaction error status.
		select {
		case db.compErrSetC <- err:
		case perr := <-db.compPerErrC:
			if err != nil {
				db.logf("%s exiting (persistent error %q)", name, perr)
				db.compactionExitTransact()
			}
		case <-db.closeC:
			db.logf("%s exiting", name)
			db.compactionExitTransact()
		}
		if err == nil {
			return
		}
		if errors.IsCorrupted(err) {
			db.logf("%s exiting (corruption detected)", name)
			db.compactionExitTransact()
		}

		if !disableBackoff {
			// Reset backoff duration if counter is advancing.
			if cnt > lastCnt {
				backoff = backoffMin
				lastCnt = cnt
			}

			// Backoff.
			backoffT.Reset(backoff)
			if backoff < backoffMax {
				backoff *= backoffMul
				if backoff > backoffMax {
					backoff = backoffMax
				}
			}
			select {
			case <-backoffT.C:
			case <-db.closeC:
				db.logf("%s exiting", name)
				db.compactionExitTransact()
			}
		}
	}
}

type compactionTransactFunc struct {
	runFunc    func(cnt *compactionTransactCounter) error
	revertFunc func() error
}

func (t *compactionTransactFunc) run(cnt *compactionTransactCounter) error {
	return t.runFunc(cnt)
}

func (t *compactionTransactFunc) revert() error {
	if t.revertFunc != nil {
		return t.revertFunc()
	}
	return nil
}

func (db *DB) compactionTransactFunc(name string, run func(cnt *compactionTransactCounter) error, revert func() error) {
	db.compactionTransact(name, &compactionTransactFunc{run, revert})
}

func (db *DB) compactionExitTransact() {
	panic(errCompactionTransactExiting)
}

func (db *DB) compactionCommit(name string, rec *sessionRecord) {
	db.compCommitLk.Lock()
	defer db.compCommitLk.Unlock() // Defer is necessary.
	db.compactionTransactFunc(name+"@commit", func(cnt *compactionTransactCounter) error {
		return db.s.commit(rec, true)
	}, nil)
}

func (db *DB) memCompaction() {
	mdb := db.getFrozenMem()
	if mdb == nil {
		return
	}
	defer mdb.decref()

	db.logf("memdb@flush N·%d S·%s", mdb.Len(), shortenb(int64(mdb.Size())))

	// Don't compact empty memdb.
	if mdb.Len() == 0 {
		db.logf("memdb@flush skipping")
		// drop frozen memdb
		db.dropFrozenMem()
		return
	}

	// Pause table compaction.
	resumeC := make(chan struct{})
	select {
	case db.tcompPauseC <- (chan<- struct{})(resumeC):
	case <-db.compPerErrC:
		close(resumeC)
		resumeC = nil
	case <-db.closeC:
		db.compactionExitTransact()
	}

	var (
		rec        = &sessionRecord{}
		stats      = &cStatStaging{}
		flushLevel int
	)

	// Generate tables.
	db.compactionTransactFunc("memdb@flush", func(cnt *compactionTransactCounter) (err error) {
		stats.startTimer()
		flushLevel, err = db.s.flushMemdb(rec, mdb.DB, db.memdbMaxLevel)
		stats.stopTimer()
		return
	}, func() error {
		for _, r := range rec.addedTables {
			db.logf("memdb@flush revert @%d", r.num)
			if err := db.s.stor.Remove(storage.FileDesc{Type: storage.TypeTable, Num: r.num}); err != nil {
				return err
			}
		}
		return nil
	})

	rec.setJournalNum(db.journalFd.Num)
	rec.setSeqNum(db.frozenSeq)

	// Commit.
	stats.startTimer()
	db.compactionCommit("memdb", rec)
	stats.stopTimer()

	db.logf("memdb@flush committed F·%d T·%v", len(rec.addedTables), stats.duration)

	// Save compaction stats
	for _, r := range rec.addedTables {
		stats.write += r.size
	}
	db.compStats.addStat(flushLevel, stats)
	atomic.AddUint32(&db.memComp, 1)

	// Drop frozen memdb.
	db.dropFrozenMem()

	// Resume table compaction.
	if resumeC != nil {
		select {
		case <-resumeC:
			close(resumeC)
		case <-db.closeC:
			db.compactionExitTransact()
		}
	}

	// Trigger table compaction.
	db.compTrigger(db.tcompCmdC)
}

type tableCompactionBuilder struct {
	db    *DB
	s     *session
	c     *compaction
	rec   *sessionRecord
	stat1 *cStatStaging

	snapHasLastUkey bool
	snapLastUkey    []byte
	snapLastSeq     uint64
	snapIter        int
	snapKerrCnt     int
	snapDropCnt     int

	kerrCnt int
	dropCnt int

	minSeq    uint64
	strict    bool
	tableSize int

	tw *tWriter
}

func (b *tableCompactionBuilder) appendKV(key, value []byte) error {
	// Create new table if not already.
	if b.tw == nil {
		// Check for pause event.
		if b.db != nil {
			select {
			case ch := <-b.db.tcompPauseC:
				b.db.pauseCompaction(ch)
			case <-b.db.closeC:
				b.db.compactionExitTransact()
			default:
			}
		}

		// Create new table.
		var err error
		b.tw, err = b.s.tops.create(b.tableSize)
		if err != nil {
			return err
		}
	}

	// Write key/value into table.
	return b.tw.append(key, value)
}

func (b *tableCompactionBuilder) needFlush() bool {
	return b.tw.tw.BytesLen() >= b.tableSize
}

func (b *tableCompactionBuilder) flush() error {
	t, err := b.tw.finish()
	if err != nil {
		return err
	}
	b.rec.addTableFile(b.c.sourceLevel+1, t)
	b.stat1.write += t.size
	b.s.logf("table@build created L%d@%d N·%d S·%s %q:%q", b.c.sourceLevel+1, t.fd.Num, b.tw.tw.EntriesLen(), shortenb(t.size), t.imin, t.imax)
	b.tw = nil
	return nil
}

func (b *tableCompactionBuilder) cleanup() error {
	if b.tw != nil {
		if err := b.tw.drop(); err != nil {
			return err
		}
		b.tw = nil
	}
	return nil
}

func (b *tableCompactionBuilder) run(cnt *compactionTransactCounter) (err error) {
	snapResumed := b.snapIter > 0
	hasLastUkey := b.snapHasLastUkey // The key might has zero length, so this is necessary.
	lastUkey := append([]byte(nil), b.snapLastUkey...)
	lastSeq := b.snapLastSeq
	b.kerrCnt = b.snapKerrCnt
	b.dropCnt = b.snapDropCnt
	// Restore compaction state.
	b.c.restore()

	defer func() {
		if cerr := b.cleanup(); cerr != nil {
			if err == nil {
				err = cerr
			} else {
				err = fmt.Errorf("tableCompactionBuilder error: %v, cleanup error (%v)", err, cerr)
			}
		}
	}()

	b.stat1.startTimer()
	defer b.stat1.stopTimer()

	iter := b.c.newIterator()
	defer iter.Release()
	for i := 0; iter.Next(); i++ {
		// Incr transact counter.
		cnt.incr()

		// Skip until last state.
		if i < b.snapIter {
			continue
		}

		resumed := false
		if snapResumed {
			resumed = true
			snapResumed = false
		}

		ikey := iter.Key()
		ukey, seq, kt, kerr := parseInternalKey(ikey)

		if kerr == nil {
			shouldStop := !resumed && b.c.shouldStopBefore(ikey)

			if !hasLastUkey || b.s.icmp.uCompare(lastUkey, ukey) != 0 {
				// First occurrence of this user key.

				// Only rotate tables if ukey doesn't hop across.
				if b.tw != nil && (shouldStop || b.needFlush()) {
					if err := b.flush(); err != nil {
						return err
					}

					// Creates snapshot of the state.
					b.c.save()
					b.snapHasLastUkey = hasLastUkey
					b.snapLastUkey = append(b.snapLastUkey[:0], lastUkey...)
					b.snapLastSeq = lastSeq
					b.snapIter = i
					b.snapKerrCnt = b.kerrCnt
					b.snapDropCnt = b.dropCnt
				}

				hasLastUkey = true
				lastUkey = append(lastUkey[:0], ukey...)
				lastSeq = keyMaxSeq
			}

			switch {
			case lastSeq <= b.minSeq:
				// Dropped because newer entry for same user key exist
				fallthrough // (A)
			case kt == keyTypeDel && seq <= b.minSeq && b.c.baseLevelForKey(lastUkey):
				// For this user key:
				// (1) there is no data in higher levels
				// (2) data in lower levels will have larger seq numbers
				// (3) data in layers that are being compacted here and have
				//     smaller seq numbers will be dropped in the next
				//     few iterations of this loop (by rule (A) above).
				// Therefore this deletion marker is obsolete and can be dropped.
				lastSeq = seq
				b.dropCnt++
				continue
			default:
				lastSeq = seq
			}
		} else {
			if b.strict {
				return kerr
			}

			// Don't drop corrupted keys.
			hasLastUkey = false
			lastUkey = lastUkey[:0]
			lastSeq = keyMaxSeq
			b.kerrCnt++
		}

		if err := b.appendKV(ikey, iter.Value()); err != nil {
			return err
		}
	}

	if err := iter.Error(); err != nil {
		return err
	}

	// Finish last table.
	if b.tw != nil && !b.tw.empty() {
		return b.flush()
	}
	return nil
}

func (b *tableCompactionBuilder) revert() error {
	for _, at := range b.rec.addedTables {
		b.s.logf("table@build revert @%d", at.num)
		if err := b.s.stor.Remove(storage.FileDesc{Type: storage.TypeTable, Num: at.num}); err != nil {
			return err
		}
	}
	return nil
}

func (db *DB) tableCompaction(c *compaction, noTrivial bool) {
	defer c.release()

	rec := &sessionRecord{}
	rec.addCompPtr(c.sourceLevel, c.imax)

	if !noTrivial && c.trivial() {
		t := c.levels[0][0]
		db.logf("table@move L%d@%d -> L%d", c.sourceLevel, t.fd.Num, c.sourceLevel+1)
		rec.delTable(c.sourceLevel, t.fd.Num)
		rec.addTableFile(c.sourceLevel+1, t)
		db.compactionCommit("table-move", rec)
		return
	}

	var stats [2]cStatStaging
	for i, tables := range c.levels {
		for _, t := range tables {
			stats[i].read += t.size
			// Insert deleted tables into record
			rec.delTable(c.sourceLevel+i, t.fd.Num)
		}
	}
	sourceSize := stats[0].read + stats[1].read
	minSeq := db.minSeq()
	db.logf("table@compaction L%d·%d -> L%d·%d S·%s Q·%d", c.sourceLevel, len(c.levels[0]), c.sourceLevel+1, len(c.levels[1]), shortenb(sourceSize), minSeq)

	b := &tableCompactionBuilder{
		db:        db,
		s:         db.s,
		c:         c,
		rec:       rec,
		stat1:     &stats[1],
		minSeq:    minSeq,
		strict:    db.s.o.GetStrict(opt.StrictCompaction),
		tableSize: db.s.o.GetCompactionTableSize(c.sourceLevel + 1),
	}
	db.compactionTransact("table@build", b)

	// Commit.
	stats[1].startTimer()
	db.compactionCommit("table", rec)
	stats[1].stopTimer()

	resultSize := stats[1].write
	db.logf("table@compaction committed F%s S%s Ke·%d D·%d T·%v", sint(len(rec.addedTables)-len(rec.deletedTables)), sshortenb(resultSize-sourceSize), b.kerrCnt, b.dropCnt, stats[1].duration)

	// Save compaction stats
	for i := range stats {
		db.compStats.addStat(c.sourceLevel+1, &stats[i])
	}
	switch c.typ {
	case level0Compaction:
		atomic.AddUint32(&db.level0Comp, 1)
	case nonLevel0Compaction:
		atomic.AddUint32(&db.nonLevel0Comp, 1)
	case seekCompaction:
		atomic.AddUint32(&db.seekComp, 1)
	}
}

func (db *DB) tableRangeCompaction(level int, umin, umax []byte) error {
	db.logf("table@compaction range L%d %q:%q", level, umin, umax)
	if level >= 0 {
		if c := db.s.getCompactionRange(level, umin, umax, true); c != nil {
			db.tableCompaction(c, true)
		}
	} else {
		// Retry until nothing to compact.
		for {
			compacted := false

			// Scan for maximum level with overlapped tables.
			v := db.s.version()
			m := 1
			for i := m; i < len(v.levels); i++ {
				tables := v.levels[i]
				if tables.overlaps(db.s.icmp, umin, umax, false) {
					m = i
				}
			}
			v.release()

			for level := 0; level < m; level++ {
				if c := db.s.getCompactionRange(level, umin, umax, false); c != nil {
					db.tableCompaction(c, true)
					compacted = true
				}
			}

			if !compacted {
				break
			}
		}
	}

	return nil
}

func (db *DB) tableAutoCompaction() {
	if c := db.s.pickCompaction(); c != nil {
		db.tableCompaction(c, false)
	}
}

func (db *DB) tableNeedCompaction() bool {
	v := db.s.version()
	defer v.release()
	return v.needCompaction()
}

// resumeWrite returns an indicator whether we should resume write operation if enough level0 files are compacted.
func (db *DB) resumeWrite() bool {
	v := db.s.version()
	defer v.release()
	return v.tLen(0) < db.s.o.GetWriteL0PauseTrigger()
}

func (db *DB) pauseCompaction(ch chan<- struct{}) {
	select {
	case ch <- struct{}{}:
	case <-db.closeC:
		db.compactionExitTransact()
	}
}

type cCmd interface {
	ack(err error)
}

type cAuto struct {
	// Note for table compaction, an non-empty ackC represents it's a compaction waiting command.
	ackC chan<- error
}

func (r cAuto) ack(err error) {
	if r.ackC != nil {
		defer func() {
			_ = recover()
		}()
		r.ackC <- err
	}
}

type cRange struct {
	level    int
	min, max []byte
	ackC     chan<- error
}

func (r cRange) ack(err error) {
	if r.ackC != nil {
		defer func() {
			_ = recover()
		}()
		r.ackC <- err
	}
}

// This will trigger auto compaction but will not wait for it.
func (db *DB) compTrigger(compC chan<- cCmd) {
	select {
	case compC <- cAuto{}:
	default:
	}
}

// This will trigger auto compaction and/or wait for all compaction to be done.
func (db *DB) compTriggerWait(compC chan<- cCmd) (err error) {
	ch := make(chan error)
	defer close(ch)
	// Send cmd.
	select {
	case compC <- cAuto{ch}:
	case err = <-db.compErrC:
		return
	case <-db.closeC:
		return ErrClosed
	}
	// Wait cmd.
	select {
	case err = <-ch:
	case err = <-db.compErrC:
	case <-db.closeC:
		return ErrClosed
	}
	return err
}

// Send range compaction request.
func (db *DB) compTriggerRange(compC chan<- cCmd, level int, min, max []byte) (err error) {
	ch := make(chan error)
	defer close(ch)
	// Send cmd.
	select {
	case compC <- cRange{level, min, max, ch}:
	case err := <-db.compErrC:
		return err
	case <-db.closeC:
		return ErrClosed
	}
	// Wait cmd.
	select {
	case err = <-ch:
	case err = <-db.compErrC:
	case <-db.closeC:
		return ErrClosed
	}
	return err
}

func (db *DB) mCompaction() {
	var x cCmd

	defer func() {
		if x := recover(); x != nil {
			if x != errCompactionTransactExiting {
				panic(x)
			}
		}
		if x != nil {
			x.ack(ErrClosed)
		}
		db.closeW.Done()
	}()

	for {
		select {
		case x = <-db.mcompCmdC:
			switch x.(type) {
			case cAuto:
				db.memCompaction()
				x.ack(nil)
				x = nil
			default:
				panic("leveldb: unknown command")
			}
		case <-db.closeC:
			return
		}
	}
}

func (db *DB) tCompaction() {
	var (
		x     cCmd
		waitQ []cCmd
	)

	defer func() {
		if x := recover(); x != nil {
			if x != errCompactionTransactExiting {
				panic(x)
			}
		}
		for i := range waitQ {
			waitQ[i].ack(ErrClosed)
			waitQ[i] = nil
		}
		if x != nil {
			x.ack(ErrClosed)
		}
		db.closeW.Done()
	}()

	for {
		if db.tableNeedCompaction() {
			select {
			case x = <-db.tcompCmdC:
			case ch := <-db.tcompPauseC:
				db.pauseCompaction(ch)
				continue
			case <-db.closeC:
				return
			default:
			}
			// Resume write operation as soon as possible.
			if len(waitQ) > 0 && db.resumeWrite() {
				for i := range waitQ {
					waitQ[i].ack(nil)
					waitQ[i] = nil
				}
				waitQ = waitQ[:0]
			}
		} else {
			for i := range waitQ {
				waitQ[i].ack(nil)
				waitQ[i] = nil
			}
			waitQ = waitQ[:0]
			select {
			case x = <-db.tcompCmdC:
			case ch := <-db.tcompPauseC:
				db.pauseCompaction(ch)
				continue
			case <-db.closeC:
				return
			}
		}
		if x != nil {
			switch cmd := x.(type) {
			case cAuto:
				if cmd.ackC != nil {
					// Check the write pause state before caching it.
					if db.resumeWrite() {
						x.ack(nil)
					} else {
						waitQ = append(waitQ, x)
					}
				}
			case cRange:
				x.ack(db.tableRangeCompaction(cmd.level, cmd.min, cmd.max))
			default:
				panic("leveldb: unknown command")
			}
			x = nil
		}
		db.tableAutoCompaction()
	}
}
```

## File: `leveldb/db_iter.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"math/rand"
	"runtime"
	"sync"
	"sync/atomic"

	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/util"
)

type memdbReleaser struct {
	once sync.Once
	m    *memDB
}

func (mr *memdbReleaser) Release() {
	mr.once.Do(func() {
		mr.m.decref()
	})
}

func (db *DB) newRawIterator(auxm *memDB, auxt tFiles, slice *util.Range, ro *opt.ReadOptions) iterator.Iterator {
	strict := opt.GetStrict(db.s.o.Options, ro, opt.StrictReader)
	em, fm := db.getMems()
	v := db.s.version()

	tableIts := v.getIterators(slice, ro)
	n := len(tableIts) + len(auxt) + 3
	its := make([]iterator.Iterator, 0, n)

	if auxm != nil {
		ami := auxm.NewIterator(slice)
		ami.SetReleaser(&memdbReleaser{m: auxm})
		its = append(its, ami)
	}
	for _, t := range auxt {
		its = append(its, v.s.tops.newIterator(t, slice, ro))
	}

	emi := em.NewIterator(slice)
	emi.SetReleaser(&memdbReleaser{m: em})
	its = append(its, emi)
	if fm != nil {
		fmi := fm.NewIterator(slice)
		fmi.SetReleaser(&memdbReleaser{m: fm})
		its = append(its, fmi)
	}
	its = append(its, tableIts...)
	mi := iterator.NewMergedIterator(its, db.s.icmp, strict)
	mi.SetReleaser(&versionReleaser{v: v})
	return mi
}

func (db *DB) newIterator(auxm *memDB, auxt tFiles, seq uint64, slice *util.Range, ro *opt.ReadOptions) *dbIter {
	var islice *util.Range
	if slice != nil {
		islice = &util.Range{}
		if slice.Start != nil {
			islice.Start = makeInternalKey(nil, slice.Start, keyMaxSeq, keyTypeSeek)
		}
		if slice.Limit != nil {
			islice.Limit = makeInternalKey(nil, slice.Limit, keyMaxSeq, keyTypeSeek)
		}
	}
	rawIter := db.newRawIterator(auxm, auxt, islice, ro)
	iter := &dbIter{
		db:              db,
		icmp:            db.s.icmp,
		iter:            rawIter,
		seq:             seq,
		strict:          opt.GetStrict(db.s.o.Options, ro, opt.StrictReader),
		disableSampling: db.s.o.GetDisableSeeksCompaction() || db.s.o.GetIteratorSamplingRate() <= 0,
		key:             make([]byte, 0),
		value:           make([]byte, 0),
	}
	if !iter.disableSampling {
		iter.samplingGap = db.iterSamplingRate()
	}
	atomic.AddInt32(&db.aliveIters, 1)
	runtime.SetFinalizer(iter, (*dbIter).Release)
	return iter
}

func (db *DB) iterSamplingRate() int {
	return rand.Intn(2 * db.s.o.GetIteratorSamplingRate())
}

type dir int

const (
	dirReleased dir = iota - 1
	dirSOI
	dirEOI
	dirBackward
	dirForward
)

// dbIter represent an interator states over a database session.
type dbIter struct {
	db              *DB
	icmp            *iComparer
	iter            iterator.Iterator
	seq             uint64
	strict          bool
	disableSampling bool

	samplingGap int
	dir         dir
	key         []byte
	value       []byte
	err         error
	releaser    util.Releaser
}

func (i *dbIter) sampleSeek() {
	if i.disableSampling {
		return
	}

	ikey := i.iter.Key()
	i.samplingGap -= len(ikey) + len(i.iter.Value())
	for i.samplingGap < 0 {
		i.samplingGap += i.db.iterSamplingRate()
		i.db.sampleSeek(ikey)
	}
}

func (i *dbIter) setErr(err error) {
	i.err = err
	i.key = nil
	i.value = nil
}

func (i *dbIter) iterErr() {
	if err := i.iter.Error(); err != nil {
		i.setErr(err)
	}
}

func (i *dbIter) Valid() bool {
	return i.err == nil && i.dir > dirEOI
}

func (i *dbIter) First() bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	if i.iter.First() {
		i.dir = dirSOI
		return i.next()
	}
	i.dir = dirEOI
	i.iterErr()
	return false
}

func (i *dbIter) Last() bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	if i.iter.Last() {
		return i.prev()
	}
	i.dir = dirSOI
	i.iterErr()
	return false
}

func (i *dbIter) Seek(key []byte) bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	ikey := makeInternalKey(nil, key, i.seq, keyTypeSeek)
	if i.iter.Seek(ikey) {
		i.dir = dirSOI
		return i.next()
	}
	i.dir = dirEOI
	i.iterErr()
	return false
}

func (i *dbIter) next() bool {
	for {
		if ukey, seq, kt, kerr := parseInternalKey(i.iter.Key()); kerr == nil {
			i.sampleSeek()
			if seq <= i.seq {
				switch kt {
				case keyTypeDel:
					// Skip deleted key.
					i.key = append(i.key[:0], ukey...)
					i.dir = dirForward
				case keyTypeVal:
					if i.dir == dirSOI || i.icmp.uCompare(ukey, i.key) > 0 {
						i.key = append(i.key[:0], ukey...)
						i.value = append(i.value[:0], i.iter.Value()...)
						i.dir = dirForward
						return true
					}
				}
			}
		} else if i.strict {
			i.setErr(kerr)
			break
		}
		if !i.iter.Next() {
			i.dir = dirEOI
			i.iterErr()
			break
		}
	}
	return false
}

func (i *dbIter) Next() bool {
	if i.dir == dirEOI || i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	if !i.iter.Next() || (i.dir == dirBackward && !i.iter.Next()) {
		i.dir = dirEOI
		i.iterErr()
		return false
	}
	return i.next()
}

func (i *dbIter) prev() bool {
	i.dir = dirBackward
	del := true
	if i.iter.Valid() {
		for {
			if ukey, seq, kt, kerr := parseInternalKey(i.iter.Key()); kerr == nil {
				i.sampleSeek()
				if seq <= i.seq {
					if !del && i.icmp.uCompare(ukey, i.key) < 0 {
						return true
					}
					del = (kt == keyTypeDel)
					if !del {
						i.key = append(i.key[:0], ukey...)
						i.value = append(i.value[:0], i.iter.Value()...)
					}
				}
			} else if i.strict {
				i.setErr(kerr)
				return false
			}
			if !i.iter.Prev() {
				break
			}
		}
	}
	if del {
		i.dir = dirSOI
		i.iterErr()
		return false
	}
	return true
}

func (i *dbIter) Prev() bool {
	if i.dir == dirSOI || i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	switch i.dir {
	case dirEOI:
		return i.Last()
	case dirForward:
		for i.iter.Prev() {
			if ukey, _, _, kerr := parseInternalKey(i.iter.Key()); kerr == nil {
				i.sampleSeek()
				if i.icmp.uCompare(ukey, i.key) < 0 {
					goto cont
				}
			} else if i.strict {
				i.setErr(kerr)
				return false
			}
		}
		i.dir = dirSOI
		i.iterErr()
		return false
	}

cont:
	return i.prev()
}

func (i *dbIter) Key() []byte {
	if i.err != nil || i.dir <= dirEOI {
		return nil
	}
	return i.key
}

func (i *dbIter) Value() []byte {
	if i.err != nil || i.dir <= dirEOI {
		return nil
	}
	return i.value
}

func (i *dbIter) Release() {
	if i.dir != dirReleased {
		// Clear the finalizer.
		runtime.SetFinalizer(i, nil)

		if i.releaser != nil {
			i.releaser.Release()
			i.releaser = nil
		}

		i.dir = dirReleased
		i.key = nil
		i.value = nil
		i.iter.Release()
		i.iter = nil
		atomic.AddInt32(&i.db.aliveIters, -1)
		i.db = nil
	}
}

func (i *dbIter) SetReleaser(releaser util.Releaser) {
	if i.dir == dirReleased {
		panic(util.ErrReleased)
	}
	if i.releaser != nil && releaser != nil {
		panic(util.ErrHasReleaser)
	}
	i.releaser = releaser
}

func (i *dbIter) Error() error {
	return i.err
}
```

## File: `leveldb/db_snapshot.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"container/list"
	"fmt"
	"runtime"
	"sync"
	"sync/atomic"

	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/util"
)

type snapshotElement struct {
	seq uint64
	ref int
	e   *list.Element
}

// Acquires a snapshot, based on latest sequence.
func (db *DB) acquireSnapshot() *snapshotElement {
	db.snapsMu.Lock()
	defer db.snapsMu.Unlock()

	seq := db.getSeq()

	if e := db.snapsList.Back(); e != nil {
		se := e.Value.(*snapshotElement)
		if se.seq == seq {
			se.ref++
			return se
		} else if seq < se.seq {
			panic("leveldb: sequence number is not increasing")
		}
	}
	se := &snapshotElement{seq: seq, ref: 1}
	se.e = db.snapsList.PushBack(se)
	return se
}

// Releases given snapshot element.
func (db *DB) releaseSnapshot(se *snapshotElement) {
	db.snapsMu.Lock()
	defer db.snapsMu.Unlock()

	se.ref--
	if se.ref == 0 {
		db.snapsList.Remove(se.e)
		se.e = nil
	} else if se.ref < 0 {
		panic("leveldb: Snapshot: negative element reference")
	}
}

// Gets minimum sequence that not being snapshotted.
func (db *DB) minSeq() uint64 {
	db.snapsMu.Lock()
	defer db.snapsMu.Unlock()

	if e := db.snapsList.Front(); e != nil {
		return e.Value.(*snapshotElement).seq
	}

	return db.getSeq()
}

// Snapshot is a DB snapshot.
type Snapshot struct {
	db       *DB
	elem     *snapshotElement
	mu       sync.RWMutex
	released bool
}

// Creates new snapshot object.
func (db *DB) newSnapshot() *Snapshot {
	snap := &Snapshot{
		db:   db,
		elem: db.acquireSnapshot(),
	}
	atomic.AddInt32(&db.aliveSnaps, 1)
	runtime.SetFinalizer(snap, (*Snapshot).Release)
	return snap
}

func (snap *Snapshot) String() string {
	return fmt.Sprintf("leveldb.Snapshot{%d}", snap.elem.seq)
}

// Get gets the value for the given key. It returns ErrNotFound if
// the DB does not contains the key.
//
// The caller should not modify the contents of the returned slice, but
// it is safe to modify the contents of the argument after Get returns.
func (snap *Snapshot) Get(key []byte, ro *opt.ReadOptions) (value []byte, err error) {
	snap.mu.RLock()
	defer snap.mu.RUnlock()
	if snap.released {
		err = ErrSnapshotReleased
		return
	}
	err = snap.db.ok()
	if err != nil {
		return
	}
	return snap.db.get(nil, nil, key, snap.elem.seq, ro)
}

// Has returns true if the DB does contains the given key.
//
// It is safe to modify the contents of the argument after Get returns.
func (snap *Snapshot) Has(key []byte, ro *opt.ReadOptions) (ret bool, err error) {
	snap.mu.RLock()
	defer snap.mu.RUnlock()
	if snap.released {
		err = ErrSnapshotReleased
		return
	}
	err = snap.db.ok()
	if err != nil {
		return
	}
	return snap.db.has(nil, nil, key, snap.elem.seq, ro)
}

// NewIterator returns an iterator for the snapshot of the underlying DB.
// The returned iterator is not safe for concurrent use, but it is safe to use
// multiple iterators concurrently, with each in a dedicated goroutine.
// It is also safe to use an iterator concurrently with modifying its
// underlying DB. The resultant key/value pairs are guaranteed to be
// consistent.
//
// Slice allows slicing the iterator to only contains keys in the given
// range. A nil Range.Start is treated as a key before all keys in the
// DB. And a nil Range.Limit is treated as a key after all keys in
// the DB.
//
// WARNING: Any slice returned by interator (e.g. slice returned by calling
// Iterator.Key() or Iterator.Value() methods), its content should not be
// modified unless noted otherwise.
//
// The iterator must be released after use, by calling Release method.
// Releasing the snapshot doesn't mean releasing the iterator too, the
// iterator would be still valid until released.
//
// Also read Iterator documentation of the leveldb/iterator package.
func (snap *Snapshot) NewIterator(slice *util.Range, ro *opt.ReadOptions) iterator.Iterator {
	snap.mu.Lock()
	defer snap.mu.Unlock()
	if snap.released {
		return iterator.NewEmptyIterator(ErrSnapshotReleased)
	}
	if err := snap.db.ok(); err != nil {
		return iterator.NewEmptyIterator(err)
	}
	// Since iterator already hold version ref, it doesn't need to
	// hold snapshot ref.
	return snap.db.newIterator(nil, nil, snap.elem.seq, slice, ro)
}

// Release releases the snapshot. This will not release any returned
// iterators, the iterators would still be valid until released or the
// underlying DB is closed.
//
// Other methods should not be called after the snapshot has been released.
func (snap *Snapshot) Release() {
	snap.mu.Lock()
	defer snap.mu.Unlock()

	if !snap.released {
		// Clear the finalizer.
		runtime.SetFinalizer(snap, nil)

		snap.released = true
		snap.db.releaseSnapshot(snap.elem)
		atomic.AddInt32(&snap.db.aliveSnaps, -1)
		snap.db = nil
		snap.elem = nil
	}
}
```

## File: `leveldb/db_state.go`
```go
// Copyright (c) 2013, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"errors"
	"sync/atomic"
	"time"

	"github.com/syndtr/goleveldb/leveldb/journal"
	"github.com/syndtr/goleveldb/leveldb/memdb"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

var (
	errHasFrozenMem = errors.New("has frozen mem")
)

type memDB struct {
	db *DB
	*memdb.DB
	ref int32
}

func (m *memDB) getref() int32 {
	return atomic.LoadInt32(&m.ref)
}

func (m *memDB) incref() {
	atomic.AddInt32(&m.ref, 1)
}

func (m *memDB) decref() {
	if ref := atomic.AddInt32(&m.ref, -1); ref == 0 {
		// Only put back memdb with std capacity.
		if m.Capacity() == m.db.s.o.GetWriteBuffer() {
			m.Reset()
			m.db.mpoolPut(m.DB)
		}
		m.db = nil
		m.DB = nil
	} else if ref < 0 {
		panic("negative memdb ref")
	}
}

// Get latest sequence number.
func (db *DB) getSeq() uint64 {
	return atomic.LoadUint64(&db.seq)
}

// Atomically adds delta to seq.
func (db *DB) addSeq(delta uint64) {
	atomic.AddUint64(&db.seq, delta)
}

func (db *DB) setSeq(seq uint64) {
	atomic.StoreUint64(&db.seq, seq)
}

func (db *DB) sampleSeek(ikey internalKey) {
	v := db.s.version()
	if v.sampleSeek(ikey) {
		// Trigger table compaction.
		db.compTrigger(db.tcompCmdC)
	}
	v.release()
}

func (db *DB) mpoolPut(mem *memdb.DB) {
	if !db.isClosed() {
		select {
		case db.memPool <- mem:
		default:
		}
	}
}

func (db *DB) mpoolGet(n int) *memDB {
	var mdb *memdb.DB
	select {
	case mdb = <-db.memPool:
	default:
	}
	if mdb == nil || mdb.Capacity() < n {
		mdb = memdb.New(db.s.icmp, maxInt(db.s.o.GetWriteBuffer(), n))
	}
	return &memDB{
		db: db,
		DB: mdb,
	}
}

func (db *DB) mpoolDrain() {
	ticker := time.NewTicker(30 * time.Second)
	for {
		select {
		case <-ticker.C:
			select {
			case <-db.memPool:
			default:
			}
		case <-db.closeC:
			ticker.Stop()
			// Make sure the pool is drained.
			select {
			case <-db.memPool:
			case <-time.After(time.Second):
			}
			close(db.memPool)
			return
		}
	}
}

// Create new memdb and froze the old one; need external synchronization.
// newMem only called synchronously by the writer.
func (db *DB) newMem(n int) (mem *memDB, err error) {
	fd := storage.FileDesc{Type: storage.TypeJournal, Num: db.s.allocFileNum()}
	w, err := db.s.stor.Create(fd)
	if err != nil {
		db.s.reuseFileNum(fd.Num)
		return
	}

	db.memMu.Lock()
	defer db.memMu.Unlock()

	if db.frozenMem != nil {
		return nil, errHasFrozenMem
	}

	if db.journal == nil {
		db.journal = journal.NewWriter(w)
	} else {
		if err := db.journal.Reset(w); err != nil {
			return nil, err
		}
		if err := db.journalWriter.Close(); err != nil {
			return nil, err
		}
		db.frozenJournalFd = db.journalFd
	}
	db.journalWriter = w
	db.journalFd = fd
	db.frozenMem = db.mem
	mem = db.mpoolGet(n)
	mem.incref() // for self
	mem.incref() // for caller
	db.mem = mem
	// The seq only incremented by the writer. And whoever called newMem
	// should hold write lock, so no need additional synchronization here.
	db.frozenSeq = db.seq
	return
}

// Get all memdbs.
func (db *DB) getMems() (e, f *memDB) {
	db.memMu.RLock()
	defer db.memMu.RUnlock()
	if db.mem != nil {
		db.mem.incref()
	} else if !db.isClosed() {
		panic("nil effective mem")
	}
	if db.frozenMem != nil {
		db.frozenMem.incref()
	}
	return db.mem, db.frozenMem
}

// Get effective memdb.
func (db *DB) getEffectiveMem() *memDB {
	db.memMu.RLock()
	defer db.memMu.RUnlock()
	if db.mem != nil {
		db.mem.incref()
	} else if !db.isClosed() {
		panic("nil effective mem")
	}
	return db.mem
}

// Get frozen memdb.
func (db *DB) getFrozenMem() *memDB {
	db.memMu.RLock()
	defer db.memMu.RUnlock()
	if db.frozenMem != nil {
		db.frozenMem.incref()
	}
	return db.frozenMem
}

// Drop frozen memdb; assume that frozen memdb isn't nil.
func (db *DB) dropFrozenMem() {
	db.memMu.Lock()
	if err := db.s.stor.Remove(db.frozenJournalFd); err != nil {
		db.logf("journal@remove removing @%d %q", db.frozenJournalFd.Num, err)
	} else {
		db.logf("journal@remove removed @%d", db.frozenJournalFd.Num)
	}
	db.frozenJournalFd = storage.FileDesc{}
	db.frozenMem.decref()
	db.frozenMem = nil
	db.memMu.Unlock()
}

// Clear mems ptr; used by DB.Close().
func (db *DB) clearMems() {
	db.memMu.Lock()
	db.mem = nil
	db.frozenMem = nil
	db.memMu.Unlock()
}

// Set closed flag; return true if not already closed.
func (db *DB) setClosed() bool {
	return atomic.CompareAndSwapUint32(&db.closed, 0, 1)
}

// Check whether DB was closed.
func (db *DB) isClosed() bool {
	return atomic.LoadUint32(&db.closed) != 0
}

// Check read ok status.
func (db *DB) ok() error {
	if db.isClosed() {
		return ErrClosed
	}
	return nil
}
```

## File: `leveldb/db_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"bytes"
	"container/list"
	crand "crypto/rand"
	"encoding/binary"
	"fmt"
	"math/rand"
	"os"
	"path/filepath"
	"runtime"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"
	"unsafe"

	"github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/comparer"
	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/filter"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/testutil"
	"github.com/syndtr/goleveldb/leveldb/util"
)

func tkey(i int) []byte {
	return []byte(fmt.Sprintf("%016d", i))
}

func tval(seed, n int) []byte {
	r := rand.New(rand.NewSource(int64(seed)))
	return randomString(r, n)
}

func testingLogger(t *testing.T) func(log string) {
	return func(log string) {
		t.Log(log)
	}
}

func testingPreserveOnFailed(t *testing.T) func() (preserve bool, err error) {
	return func() (preserve bool, err error) {
		preserve = t.Failed()
		return
	}
}

type dbHarness struct {
	t *testing.T

	stor *testutil.Storage
	db   *DB
	o    *opt.Options
	ro   *opt.ReadOptions
	wo   *opt.WriteOptions
}

func newDbHarnessWopt(t *testing.T, o *opt.Options) *dbHarness {
	h := new(dbHarness)
	h.init(t, o)
	return h
}

func newDbHarness(t *testing.T) *dbHarness {
	return newDbHarnessWopt(t, &opt.Options{DisableLargeBatchTransaction: true})
}

func (h *dbHarness) init(t *testing.T, o *opt.Options) {
	gomega.RegisterTestingT(t)
	h.t = t
	h.stor = testutil.NewStorage()
	h.stor.OnLog(testingLogger(t))
	h.stor.OnClose(testingPreserveOnFailed(t))
	h.o = o
	h.ro = nil
	h.wo = nil

	if err := h.openDB0(); err != nil {
		// So that it will come after fatal message.
		defer h.stor.Close()
		h.t.Fatal("Open (init): got error: ", err)
	}
}

func (h *dbHarness) openDB0() (err error) {
	h.t.Log("opening DB")
	h.db, err = Open(h.stor, h.o)
	return
}

func (h *dbHarness) openDB() {
	if err := h.openDB0(); err != nil {
		h.t.Fatal("Open: got error: ", err)
	}
}

func (h *dbHarness) closeDB0() error {
	h.t.Log("closing DB")
	return h.db.Close()
}

func (h *dbHarness) closeDB() {
	if h.db != nil {
		if err := h.closeDB0(); err != nil && err != ErrClosed {
			h.t.Error("Close: got error: ", err)
		}
	}
	h.stor.CloseCheck()
	runtime.GC()
}

func (h *dbHarness) reopenDB() {
	if h.db != nil {
		h.closeDB()
	}
	h.openDB()
}

func (h *dbHarness) close() {
	if h.db != nil {
		if err := h.closeDB0(); err != nil && err != ErrClosed {
			h.t.Error("Close: got error: ", err)
		}
		h.db = nil
	}
	h.stor.Close()
	h.stor = nil
	runtime.GC()
}

func (h *dbHarness) openAssert(want bool) {
	db, err := Open(h.stor, h.o)
	if err != nil {
		if want {
			h.t.Error("Open: assert: got error: ", err)
		} else {
			h.t.Log("Open: assert: got error (expected): ", err)
		}
	} else {
		if !want {
			h.t.Error("Open: assert: expect error")
		}
		db.Close()
	}
}

func (h *dbHarness) write(batch *Batch) {
	if err := h.db.Write(batch, h.wo); err != nil {
		h.t.Error("Write: got error: ", err)
	}
}

func (h *dbHarness) put(key, value string) {
	if err := h.db.Put([]byte(key), []byte(value), h.wo); err != nil {
		h.t.Error("Put: got error: ", err)
	}
}

func (h *dbHarness) putMulti(n int, low, hi string) {
	for i := 0; i < n; i++ {
		h.put(low, "begin")
		h.put(hi, "end")
		h.compactMem()
	}
}

func (h *dbHarness) maxNextLevelOverlappingBytes(want int64) {
	t := h.t
	db := h.db

	var (
		maxOverlaps int64
		maxLevel    int
	)
	v := db.s.version()
	if len(v.levels) > 2 {
		for i, tt := range v.levels[1 : len(v.levels)-1] {
			level := i + 1
			next := v.levels[level+1]
			for _, t := range tt {
				r := next.getOverlaps(nil, db.s.icmp, t.imin.ukey(), t.imax.ukey(), false)
				sum := r.size()
				if sum > maxOverlaps {
					maxOverlaps = sum
					maxLevel = level
				}
			}
		}
	}
	v.release()

	if maxOverlaps > want {
		t.Errorf("next level most overlapping bytes is more than %d, got=%d level=%d", want, maxOverlaps, maxLevel)
	} else {
		t.Logf("next level most overlapping bytes is %d, level=%d want=%d", maxOverlaps, maxLevel, want)
	}
}

func (h *dbHarness) delete(key string) {
	t := h.t
	db := h.db

	err := db.Delete([]byte(key), h.wo)
	if err != nil {
		t.Error("Delete: got error: ", err)
	}
}

func (h *dbHarness) assertNumKeys(want int) {
	iter := h.db.NewIterator(nil, h.ro)
	defer iter.Release()
	got := 0
	for iter.Next() {
		got++
	}
	if err := iter.Error(); err != nil {
		h.t.Error("assertNumKeys: ", err)
	}
	if want != got {
		h.t.Errorf("assertNumKeys: want=%d got=%d", want, got)
	}
}

func (h *dbHarness) getr(db Reader, key string, expectFound bool) (found bool, v []byte) {
	t := h.t
	v, err := db.Get([]byte(key), h.ro)
	switch err {
	case ErrNotFound:
		if expectFound {
			t.Errorf("Get: key '%s' not found, want found", key)
		}
	case nil:
		found = true
		if !expectFound {
			t.Errorf("Get: key '%s' found, want not found", key)
		}
	default:
		t.Error("Get: got error: ", err)
	}
	return
}

func (h *dbHarness) get(key string, expectFound bool) (found bool, v []byte) {
	return h.getr(h.db, key, expectFound)
}

func (h *dbHarness) getValr(db Reader, key, value string) {
	t := h.t
	found, r := h.getr(db, key, true)
	if !found {
		return
	}
	rval := string(r)
	if rval != value {
		t.Errorf("Get: invalid value, got '%s', want '%s'", rval, value)
	}
}

func (h *dbHarness) getVal(key, value string) {
	h.getValr(h.db, key, value)
}

func (h *dbHarness) allEntriesFor(key, want string) {
	t := h.t
	db := h.db
	s := db.s

	ikey := makeInternalKey(nil, []byte(key), keyMaxSeq, keyTypeVal)
	iter := db.newRawIterator(nil, nil, nil, nil)
	if !iter.Seek(ikey) && iter.Error() != nil {
		t.Error("AllEntries: error during seek, err: ", iter.Error())
		return
	}
	res := "[ "
	first := true
	for iter.Valid() {
		if ukey, _, kt, kerr := parseInternalKey(iter.Key()); kerr == nil {
			if s.icmp.uCompare(ikey.ukey(), ukey) != 0 {
				break
			}
			if !first {
				res += ", "
			}
			first = false
			switch kt {
			case keyTypeVal:
				res += string(iter.Value())
			case keyTypeDel:
				res += "DEL"
			}
		} else {
			if !first {
				res += ", "
			}
			first = false
			res += "CORRUPTED"
		}
		iter.Next()
	}
	if !first {
		res += " "
	}
	res += "]"
	if res != want {
		t.Errorf("AllEntries: assert failed for key %q, got=%q want=%q", key, res, want)
	}
}

// Return a string that contains all key,value pairs in order,
// formatted like "(k1->v1)(k2->v2)".
func (h *dbHarness) getKeyVal(want string) {
	t := h.t
	db := h.db

	s, err := db.GetSnapshot()
	if err != nil {
		t.Fatal("GetSnapshot: got error: ", err)
	}
	res := ""
	iter := s.NewIterator(nil, nil)
	for iter.Next() {
		res += fmt.Sprintf("(%s->%s)", string(iter.Key()), string(iter.Value()))
	}
	iter.Release()

	if res != want {
		t.Errorf("GetKeyVal: invalid key/value pair, got=%q want=%q", res, want)
	}
	s.Release()
}

func (h *dbHarness) waitCompaction() {
	t := h.t
	db := h.db
	if err := db.compTriggerWait(db.tcompCmdC); err != nil {
		t.Error("compaction error: ", err)
	}
}

func (h *dbHarness) waitMemCompaction() {
	t := h.t
	db := h.db

	if err := db.compTriggerWait(db.mcompCmdC); err != nil {
		t.Error("compaction error: ", err)
	}
}

func (h *dbHarness) compactMem() {
	t := h.t
	db := h.db

	t.Log("starting memdb compaction")

	db.writeLockC <- struct{}{}
	defer func() {
		<-db.writeLockC
	}()

	if _, err := db.rotateMem(0, true); err != nil {
		t.Error("compaction error: ", err)
	}

	if h.totalTables() == 0 {
		t.Error("zero tables after mem compaction")
	}

	t.Log("memdb compaction done")
}

func (h *dbHarness) compactRangeAtErr(level int, min, max string, wanterr bool) {
	t := h.t
	db := h.db

	var _min, _max []byte
	if min != "" {
		_min = []byte(min)
	}
	if max != "" {
		_max = []byte(max)
	}

	t.Logf("starting table range compaction: level=%d, min=%q, max=%q", level, min, max)

	if err := db.compTriggerRange(db.tcompCmdC, level, _min, _max); err != nil {
		if wanterr {
			t.Log("CompactRangeAt: got error (expected): ", err)
		} else {
			t.Error("CompactRangeAt: got error: ", err)
		}
	} else if wanterr {
		t.Error("CompactRangeAt: expect error")
	}

	t.Log("table range compaction done")
}

func (h *dbHarness) compactRangeAt(level int, min, max string) {
	h.compactRangeAtErr(level, min, max, false)
}

func (h *dbHarness) compactRange(min, max string) {
	t := h.t
	db := h.db

	t.Logf("starting DB range compaction: min=%q, max=%q", min, max)

	var r util.Range
	if min != "" {
		r.Start = []byte(min)
	}
	if max != "" {
		r.Limit = []byte(max)
	}
	if err := db.CompactRange(r); err != nil {
		t.Error("CompactRange: got error: ", err)
	}

	t.Log("DB range compaction done")
}

func (h *dbHarness) sizeOf(start, limit string) int64 {
	sz, err := h.db.SizeOf([]util.Range{
		{Start: []byte(start), Limit: []byte(limit)},
	})
	if err != nil {
		h.t.Error("SizeOf: got error: ", err)
	}
	return sz.Sum()
}

func (h *dbHarness) sizeAssert(start, limit string, low, hi int64) {
	sz := h.sizeOf(start, limit)
	if sz < low || sz > hi {
		h.t.Errorf("sizeOf %q to %q not in range, want %d - %d, got %d",
			shorten(start), shorten(limit), low, hi, sz)
	}
}

func (h *dbHarness) getSnapshot() (s *Snapshot) {
	s, err := h.db.GetSnapshot()
	if err != nil {
		h.t.Fatal("GetSnapshot: got error: ", err)
	}
	return
}

func (h *dbHarness) getTablesPerLevel() string {
	res := ""
	nz := 0
	v := h.db.s.version()
	for level, tables := range v.levels {
		if level > 0 {
			res += ","
		}
		res += fmt.Sprint(len(tables))
		if len(tables) > 0 {
			nz = len(res)
		}
	}
	v.release()
	return res[:nz]
}

func (h *dbHarness) tablesPerLevel(want string) {
	res := h.getTablesPerLevel()
	if res != want {
		h.t.Errorf("invalid tables len, want=%s, got=%s", want, res)
	}
}

func (h *dbHarness) totalTables() (n int) {
	v := h.db.s.version()
	for _, tables := range v.levels {
		n += len(tables)
	}
	v.release()
	return
}

type keyValue interface {
	Key() []byte
	Value() []byte
}

func testKeyVal(t *testing.T, kv keyValue, want string) {
	res := string(kv.Key()) + "->" + string(kv.Value())
	if res != want {
		t.Errorf("invalid key/value, want=%q, got=%q", want, res)
	}
}

func numKey(num int) string {
	return fmt.Sprintf("key%06d", num)
}

var testingBloomFilter = filter.NewBloomFilter(10)

func truno(t *testing.T, o *opt.Options, f func(h *dbHarness)) {
	for i := 0; i < 4; i++ {
		func() {
			switch i {
			case 0:
			case 1:
				if o == nil {
					o = &opt.Options{
						DisableLargeBatchTransaction: true,
						Filter:                       testingBloomFilter,
					}
				} else {
					old := o
					o = &opt.Options{}
					*o = *old
					o.Filter = testingBloomFilter
				}
			case 2:
				if o == nil {
					o = &opt.Options{
						DisableLargeBatchTransaction: true,
						Compression:                  opt.NoCompression,
					}
				} else {
					old := o
					o = &opt.Options{}
					*o = *old
					o.Compression = opt.NoCompression
				}
			}
			h := newDbHarnessWopt(t, o)
			defer h.close()
			if i == 3 {
				h.reopenDB()
			}
			f(h)
		}()
	}
}

func trun(t *testing.T, f func(h *dbHarness)) {
	truno(t, nil, f)
}

func testAligned(t *testing.T, name string, offset uintptr) {
	if offset%8 != 0 {
		t.Errorf("field %s offset is not 64-bit aligned", name)
	}
}

func Test_FieldsAligned(t *testing.T) {
	p1 := new(DB) //nolint:staticcheck
	testAligned(t, "DB.seq", unsafe.Offsetof(p1.seq))
	p2 := new(session) //nolint:staticcheck
	testAligned(t, "session.stNextFileNum", unsafe.Offsetof(p2.stNextFileNum))
	testAligned(t, "session.stJournalNum", unsafe.Offsetof(p2.stJournalNum))
	testAligned(t, "session.stPrevJournalNum", unsafe.Offsetof(p2.stPrevJournalNum))
	testAligned(t, "session.stSeqNum", unsafe.Offsetof(p2.stSeqNum))
}

func TestDB_Locking(t *testing.T) {
	h := newDbHarness(t)
	defer h.stor.Close()
	h.openAssert(false)
	h.closeDB()
	h.openAssert(true)
}

func TestDB_Empty(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.get("foo", false)

		h.reopenDB()
		h.get("foo", false)
	})
}

func TestDB_ReadWrite(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.put("foo", "v1")
		h.getVal("foo", "v1")
		h.put("bar", "v2")
		h.put("foo", "v3")
		h.getVal("foo", "v3")
		h.getVal("bar", "v2")

		h.reopenDB()
		h.getVal("foo", "v3")
		h.getVal("bar", "v2")
	})
}

func TestDB_PutDeleteGet(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.put("foo", "v1")
		h.getVal("foo", "v1")
		h.put("foo", "v2")
		h.getVal("foo", "v2")
		h.delete("foo")
		h.get("foo", false)

		h.reopenDB()
		h.get("foo", false)
	})
}

func TestDB_EmptyBatch(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.get("foo", false)
	err := h.db.Write(new(Batch), h.wo)
	if err != nil {
		t.Error("writing empty batch yield error: ", err)
	}
	h.get("foo", false)
}

func TestDB_GetFromFrozen(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		WriteBuffer:                  100100,
	})
	defer h.close()

	h.put("foo", "v1")
	h.getVal("foo", "v1")

	h.stor.Stall(testutil.ModeSync, storage.TypeTable) // Block sync calls
	h.put("k1", strings.Repeat("x", 100000))           // Fill memtable
	h.put("k2", strings.Repeat("y", 100000))           // Trigger compaction
	for i := 0; h.db.getFrozenMem() == nil && i < 100; i++ {
		time.Sleep(10 * time.Microsecond)
	}
	if h.db.getFrozenMem() == nil {
		h.stor.Release(testutil.ModeSync, storage.TypeTable)
		t.Fatal("No frozen mem")
	}
	h.getVal("foo", "v1")
	h.stor.Release(testutil.ModeSync, storage.TypeTable) // Release sync calls

	h.reopenDB()
	h.getVal("foo", "v1")
	h.get("k1", true)
	h.get("k2", true)
}

func TestDB_GetFromTable(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.put("foo", "v1")
		h.compactMem()
		h.getVal("foo", "v1")
	})
}

func TestDB_GetSnapshot(t *testing.T) {
	trun(t, func(h *dbHarness) {
		bar := strings.Repeat("b", 200)
		h.put("foo", "v1")
		h.put(bar, "v1")

		snap, err := h.db.GetSnapshot()
		if err != nil {
			t.Fatal("GetSnapshot: got error: ", err)
		}

		h.put("foo", "v2")
		h.put(bar, "v2")

		h.getVal("foo", "v2")
		h.getVal(bar, "v2")
		h.getValr(snap, "foo", "v1")
		h.getValr(snap, bar, "v1")

		h.compactMem()

		h.getVal("foo", "v2")
		h.getVal(bar, "v2")
		h.getValr(snap, "foo", "v1")
		h.getValr(snap, bar, "v1")

		snap.Release()

		h.reopenDB()
		h.getVal("foo", "v2")
		h.getVal(bar, "v2")
	})
}

func TestDB_GetLevel0Ordering(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.db.memdbMaxLevel = 2

		for i := 0; i < 4; i++ {
			h.put("bar", fmt.Sprintf("b%d", i))
			h.put("foo", fmt.Sprintf("v%d", i))
			h.compactMem()
		}
		h.getVal("foo", "v3")
		h.getVal("bar", "b3")

		v := h.db.s.version()
		t0len := v.tLen(0)
		v.release()
		if t0len < 2 {
			t.Errorf("level-0 tables is less than 2, got %d", t0len)
		}

		h.reopenDB()
		h.getVal("foo", "v3")
		h.getVal("bar", "b3")
	})
}

func TestDB_GetOrderedByLevels(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.put("foo", "v1")
		h.compactMem()
		h.compactRange("a", "z")
		h.getVal("foo", "v1")
		h.put("foo", "v2")
		h.compactMem()
		h.getVal("foo", "v2")
	})
}

func TestDB_GetPicksCorrectFile(t *testing.T) {
	trun(t, func(h *dbHarness) {
		// Arrange to have multiple files in a non-level-0 level.
		h.put("a", "va")
		h.compactMem()
		h.compactRange("a", "b")
		h.put("x", "vx")
		h.compactMem()
		h.compactRange("x", "y")
		h.put("f", "vf")
		h.compactMem()
		h.compactRange("f", "g")

		h.getVal("a", "va")
		h.getVal("f", "vf")
		h.getVal("x", "vx")

		h.compactRange("", "")
		h.getVal("a", "va")
		h.getVal("f", "vf")
		h.getVal("x", "vx")
	})
}

func TestDB_GetEncountersEmptyLevel(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.db.memdbMaxLevel = 2

		// Arrange for the following to happen:
		//   * sstable A in level 0
		//   * nothing in level 1
		//   * sstable B in level 2
		// Then do enough Get() calls to arrange for an automatic compaction
		// of sstable A.  A bug would cause the compaction to be marked as
		// occurring at level 1 (instead of the correct level 0).

		// Step 1: First place sstables in levels 0 and 2
		for i := 0; ; i++ {
			if i >= 100 {
				t.Fatal("could not fill levels-0 and level-2")
			}
			v := h.db.s.version()
			if v.tLen(0) > 0 && v.tLen(2) > 0 {
				v.release()
				break
			}
			v.release()
			h.put("a", "begin")
			h.put("z", "end")
			h.compactMem()

			h.getVal("a", "begin")
			h.getVal("z", "end")
		}

		// Step 2: clear level 1 if necessary.
		h.compactRangeAt(1, "", "")
		h.tablesPerLevel("1,0,1")

		h.getVal("a", "begin")
		h.getVal("z", "end")

		// Step 3: read a bunch of times
		for i := 0; i < 200; i++ {
			h.get("missing", false)
		}

		// Step 4: Wait for compaction to finish
		h.waitCompaction()

		v := h.db.s.version()
		if v.tLen(0) > 0 {
			t.Errorf("level-0 tables more than 0, got %d", v.tLen(0))
		}
		v.release()

		h.getVal("a", "begin")
		h.getVal("z", "end")
	})
}

func TestDB_IterMultiWithDelete(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.put("a", "va")
		h.put("b", "vb")
		h.put("c", "vc")
		h.delete("b")
		h.get("b", false)

		iter := h.db.NewIterator(nil, nil)
		iter.Seek([]byte("c"))
		testKeyVal(t, iter, "c->vc")
		iter.Prev()
		testKeyVal(t, iter, "a->va")
		iter.Release()

		h.compactMem()

		iter = h.db.NewIterator(nil, nil)
		iter.Seek([]byte("c"))
		testKeyVal(t, iter, "c->vc")
		iter.Prev()
		testKeyVal(t, iter, "a->va")
		iter.Release()
	})
}

func TestDB_IteratorPinsRef(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.put("foo", "hello")

	// Get iterator that will yield the current contents of the DB.
	iter := h.db.NewIterator(nil, nil)

	// Write to force compactions
	h.put("foo", "newvalue1")
	for i := 0; i < 100; i++ {
		h.put(numKey(i), strings.Repeat(fmt.Sprintf("v%09d", i), 100000/10))
	}
	h.put("foo", "newvalue2")

	iter.First()
	testKeyVal(t, iter, "foo->hello")
	if iter.Next() {
		t.Errorf("expect eof")
	}
	iter.Release()
}

func TestDB_Recover(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.put("foo", "v1")
		h.put("baz", "v5")

		h.reopenDB()
		h.getVal("foo", "v1")

		h.getVal("foo", "v1")
		h.getVal("baz", "v5")
		h.put("bar", "v2")
		h.put("foo", "v3")

		h.reopenDB()
		h.getVal("foo", "v3")
		h.put("foo", "v4")
		h.getVal("foo", "v4")
		h.getVal("bar", "v2")
		h.getVal("baz", "v5")
	})
}

func TestDB_RecoverWithEmptyJournal(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.put("foo", "v1")
		h.put("foo", "v2")

		h.reopenDB()
		h.reopenDB()
		h.put("foo", "v3")

		h.reopenDB()
		h.getVal("foo", "v3")
	})
}

func TestDB_RecoverDuringMemtableCompaction(t *testing.T) {
	truno(t, &opt.Options{DisableLargeBatchTransaction: true, WriteBuffer: 1000000}, func(h *dbHarness) {

		h.stor.Stall(testutil.ModeSync, storage.TypeTable)
		h.put("big1", strings.Repeat("x", 10000000))
		h.put("big2", strings.Repeat("y", 1000))
		h.put("bar", "v2")
		h.stor.Release(testutil.ModeSync, storage.TypeTable)

		h.reopenDB()
		h.getVal("bar", "v2")
		h.getVal("big1", strings.Repeat("x", 10000000))
		h.getVal("big2", strings.Repeat("y", 1000))
	})
}

func TestDB_MinorCompactionsHappen(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{DisableLargeBatchTransaction: true, WriteBuffer: 10000})
	defer h.close()

	n := 500

	key := func(i int) string {
		return fmt.Sprintf("key%06d", i)
	}

	for i := 0; i < n; i++ {
		h.put(key(i), key(i)+strings.Repeat("v", 1000))
	}

	for i := 0; i < n; i++ {
		h.getVal(key(i), key(i)+strings.Repeat("v", 1000))
	}

	h.reopenDB()
	for i := 0; i < n; i++ {
		h.getVal(key(i), key(i)+strings.Repeat("v", 1000))
	}
}

func TestDB_RecoverWithLargeJournal(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.put("big1", strings.Repeat("1", 200000))
	h.put("big2", strings.Repeat("2", 200000))
	h.put("small3", strings.Repeat("3", 10))
	h.put("small4", strings.Repeat("4", 10))
	h.tablesPerLevel("")

	// Make sure that if we re-open with a small write buffer size that
	// we flush table files in the middle of a large journal file.
	h.o.WriteBuffer = 100000
	h.reopenDB()
	h.getVal("big1", strings.Repeat("1", 200000))
	h.getVal("big2", strings.Repeat("2", 200000))
	h.getVal("small3", strings.Repeat("3", 10))
	h.getVal("small4", strings.Repeat("4", 10))
	v := h.db.s.version()
	if v.tLen(0) <= 1 {
		t.Errorf("tables-0 less than one")
	}
	v.release()
}

func TestDB_CompactionsGenerateMultipleFiles(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		WriteBuffer:                  10000000,
		Compression:                  opt.NoCompression,
	})
	defer h.close()

	v := h.db.s.version()
	if v.tLen(0) > 0 {
		t.Errorf("level-0 tables more than 0, got %d", v.tLen(0))
	}
	v.release()

	n := 80

	// Write 8MB (80 values, each 100K)
	for i := 0; i < n; i++ {
		h.put(numKey(i), strings.Repeat(fmt.Sprintf("v%09d", i), 100000/10))
	}

	// Reopening moves updates to level-0
	h.reopenDB()
	h.compactRangeAt(0, "", "")

	v = h.db.s.version()
	if v.tLen(0) > 0 {
		t.Errorf("level-0 tables more than 0, got %d", v.tLen(0))
	}
	if v.tLen(1) <= 1 {
		t.Errorf("level-1 tables less than 1, got %d", v.tLen(1))
	}
	v.release()

	for i := 0; i < n; i++ {
		h.getVal(numKey(i), strings.Repeat(fmt.Sprintf("v%09d", i), 100000/10))
	}
}

func TestDB_RepeatedWritesToSameKey(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{DisableLargeBatchTransaction: true, WriteBuffer: 100000})
	defer h.close()

	maxTables := h.o.GetWriteL0PauseTrigger() + 7

	value := strings.Repeat("v", 2*h.o.GetWriteBuffer())
	for i := 0; i < 5*maxTables; i++ {
		h.put("key", value)
		n := h.totalTables()
		if n > maxTables {
			t.Errorf("total tables exceed %d, got=%d, iter=%d", maxTables, n, i)
		}
	}
}

func TestDB_RepeatedWritesToSameKeyAfterReopen(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		WriteBuffer:                  100000,
	})
	defer h.close()

	h.reopenDB()

	maxTables := h.o.GetWriteL0PauseTrigger() + 7

	value := strings.Repeat("v", 2*h.o.GetWriteBuffer())
	for i := 0; i < 5*maxTables; i++ {
		h.put("key", value)
		n := h.totalTables()
		if n > maxTables {
			t.Errorf("total tables exceed %d, got=%d, iter=%d", maxTables, n, i)
		}
	}
}

func TestDB_SparseMerge(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{DisableLargeBatchTransaction: true, Compression: opt.NoCompression})
	defer h.close()

	h.putMulti(7, "A", "Z")

	// Suppose there is:
	//    small amount of data with prefix A
	//    large amount of data with prefix B
	//    small amount of data with prefix C
	// and that recent updates have made small changes to all three prefixes.
	// Check that we do not do a compaction that merges all of B in one shot.
	h.put("A", "va")
	value := strings.Repeat("x", 1000)
	for i := 0; i < 100000; i++ {
		h.put(fmt.Sprintf("B%010d", i), value)
	}
	h.put("C", "vc")
	h.compactMem()
	h.compactRangeAt(0, "", "")
	h.waitCompaction()

	// Make sparse update
	h.put("A", "va2")
	h.put("B100", "bvalue2")
	h.put("C", "vc2")
	h.compactMem()

	h.waitCompaction()
	h.maxNextLevelOverlappingBytes(20 * 1048576)
	h.compactRangeAt(0, "", "")
	h.waitCompaction()
	h.maxNextLevelOverlappingBytes(20 * 1048576)
	h.compactRangeAt(1, "", "")
	h.waitCompaction()
	h.maxNextLevelOverlappingBytes(20 * 1048576)
}

func TestDB_SizeOf(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		Compression:                  opt.NoCompression,
		WriteBuffer:                  10000000,
	})
	defer h.close()

	h.sizeAssert("", "xyz", 0, 0)
	h.reopenDB()
	h.sizeAssert("", "xyz", 0, 0)

	// Write 8MB (80 values, each 100K)
	n := 80
	s1 := 100000
	s2 := 105000

	for i := 0; i < n; i++ {
		h.put(numKey(i), strings.Repeat(fmt.Sprintf("v%09d", i), s1/10))
	}

	// 0 because SizeOf() does not account for memtable space
	h.sizeAssert("", numKey(50), 0, 0)

	for r := 0; r < 3; r++ {
		h.reopenDB()

		for cs := 0; cs < n; cs += 10 {
			for i := 0; i < n; i += 10 {
				h.sizeAssert("", numKey(i), int64(s1*i), int64(s2*i))
				h.sizeAssert("", numKey(i)+".suffix", int64(s1*(i+1)), int64(s2*(i+1)))
				h.sizeAssert(numKey(i), numKey(i+10), int64(s1*10), int64(s2*10))
			}

			h.sizeAssert("", numKey(50), int64(s1*50), int64(s2*50))
			h.sizeAssert("", numKey(50)+".suffix", int64(s1*50), int64(s2*50))

			h.compactRangeAt(0, numKey(cs), numKey(cs+9))
		}

		v := h.db.s.version()
		if v.tLen(0) != 0 {
			t.Errorf("level-0 tables was not zero, got %d", v.tLen(0))
		}
		if v.tLen(1) == 0 {
			t.Error("level-1 tables was zero")
		}
		v.release()
	}
}

func TestDB_SizeOf_MixOfSmallAndLarge(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		Compression:                  opt.NoCompression,
	})
	defer h.close()

	sizes := []int64{
		10000,
		10000,
		100000,
		10000,
		100000,
		10000,
		300000,
		10000,
	}

	for i, n := range sizes {
		h.put(numKey(i), strings.Repeat(fmt.Sprintf("v%09d", i), int(n)/10))
	}

	for r := 0; r < 3; r++ {
		h.reopenDB()

		var x int64
		for i, n := range sizes {
			y := x
			if i > 0 {
				y += 1000
			}
			h.sizeAssert("", numKey(i), x, y)
			x += n
		}

		h.sizeAssert(numKey(3), numKey(5), 110000, 111000)

		h.compactRangeAt(0, "", "")
	}
}

func TestDB_Snapshot(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.put("foo", "v1")
		s1 := h.getSnapshot()
		h.put("foo", "v2")
		s2 := h.getSnapshot()
		h.put("foo", "v3")
		s3 := h.getSnapshot()
		h.put("foo", "v4")

		h.getValr(s1, "foo", "v1")
		h.getValr(s2, "foo", "v2")
		h.getValr(s3, "foo", "v3")
		h.getVal("foo", "v4")

		s3.Release()
		h.getValr(s1, "foo", "v1")
		h.getValr(s2, "foo", "v2")
		h.getVal("foo", "v4")

		s1.Release()
		h.getValr(s2, "foo", "v2")
		h.getVal("foo", "v4")

		s2.Release()
		h.getVal("foo", "v4")
	})
}

func TestDB_SnapshotList(t *testing.T) {
	db := &DB{snapsList: list.New()}
	e0a := db.acquireSnapshot()
	e0b := db.acquireSnapshot()
	db.seq = 1
	e1 := db.acquireSnapshot()
	db.seq = 2
	e2 := db.acquireSnapshot()

	if db.minSeq() != 0 {
		t.Fatalf("invalid sequence number, got=%d", db.minSeq())
	}
	db.releaseSnapshot(e0a)
	if db.minSeq() != 0 {
		t.Fatalf("invalid sequence number, got=%d", db.minSeq())
	}
	db.releaseSnapshot(e2)
	if db.minSeq() != 0 {
		t.Fatalf("invalid sequence number, got=%d", db.minSeq())
	}
	db.releaseSnapshot(e0b)
	if db.minSeq() != 1 {
		t.Fatalf("invalid sequence number, got=%d", db.minSeq())
	}
	e2 = db.acquireSnapshot()
	if db.minSeq() != 1 {
		t.Fatalf("invalid sequence number, got=%d", db.minSeq())
	}
	db.releaseSnapshot(e1)
	if db.minSeq() != 2 {
		t.Fatalf("invalid sequence number, got=%d", db.minSeq())
	}
	db.releaseSnapshot(e2)
	if db.minSeq() != 2 {
		t.Fatalf("invalid sequence number, got=%d", db.minSeq())
	}
}

func TestDB_HiddenValuesAreRemoved(t *testing.T) {
	trun(t, func(h *dbHarness) {
		s := h.db.s

		m := 2
		h.db.memdbMaxLevel = m

		h.put("foo", "v1")
		h.compactMem()
		v := s.version()
		num := v.tLen(m)
		v.release()
		if num != 1 {
			t.Errorf("invalid level-%d len, want=1 got=%d", m, num)
		}

		// Place a table at level last-1 to prevent merging with preceding mutation
		h.put("a", "begin")
		h.put("z", "end")
		h.compactMem()
		v = s.version()
		if v.tLen(m) != 1 {
			t.Errorf("invalid level-%d len, want=1 got=%d", m, v.tLen(m))
		}
		if v.tLen(m-1) != 1 {
			t.Errorf("invalid level-%d len, want=1 got=%d", m-1, v.tLen(m-1))
		}
		v.release()

		h.delete("foo")
		h.put("foo", "v2")
		h.allEntriesFor("foo", "[ v2, DEL, v1 ]")
		h.compactMem()
		h.allEntriesFor("foo", "[ v2, DEL, v1 ]")
		h.compactRangeAt(m-2, "", "z")
		// DEL eliminated, but v1 remains because we aren't compacting that level
		// (DEL can be eliminated because v2 hides v1).
		h.allEntriesFor("foo", "[ v2, v1 ]")
		h.compactRangeAt(m-1, "", "")
		// Merging last-1 w/ last, so we are the base level for "foo", so
		// DEL is removed.  (as is v1).
		h.allEntriesFor("foo", "[ v2 ]")
	})
}

func TestDB_DeletionMarkers2(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()
	s := h.db.s

	m := 2
	h.db.memdbMaxLevel = m

	h.put("foo", "v1")
	h.compactMem()
	v := s.version()
	num := v.tLen(m)
	v.release()
	if num != 1 {
		t.Errorf("invalid level-%d len, want=1 got=%d", m, num)
	}

	// Place a table at level last-1 to prevent merging with preceding mutation
	h.put("a", "begin")
	h.put("z", "end")
	h.compactMem()
	v = s.version()
	if v.tLen(m) != 1 {
		t.Errorf("invalid level-%d len, want=1 got=%d", m, v.tLen(m))
	}
	if v.tLen(m-1) != 1 {
		t.Errorf("invalid level-%d len, want=1 got=%d", m-1, v.tLen(m-1))
	}
	v.release()

	h.delete("foo")
	h.allEntriesFor("foo", "[ DEL, v1 ]")
	h.compactMem() // Moves to level last-2
	h.allEntriesFor("foo", "[ DEL, v1 ]")
	h.compactRangeAt(m-2, "", "")
	// DEL kept: "last" file overlaps
	h.allEntriesFor("foo", "[ DEL, v1 ]")
	h.compactRangeAt(m-1, "", "")
	// Merging last-1 w/ last, so we are the base level for "foo", so
	// DEL is removed.  (as is v1).
	h.allEntriesFor("foo", "[ ]")
}

func TestDB_CompactionTableOpenError(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		OpenFilesCacheCapacity:       -1,
	})
	defer h.close()

	h.db.memdbMaxLevel = 2

	im := 10
	jm := 10
	for r := 0; r < 2; r++ {
		for i := 0; i < im; i++ {
			for j := 0; j < jm; j++ {
				h.put(fmt.Sprintf("k%d,%d", i, j), fmt.Sprintf("v%d,%d", i, j))
			}
			h.compactMem()
		}
	}

	if n := h.totalTables(); n != im*2 {
		t.Errorf("total tables is %d, want %d", n, im*2)
	}

	h.stor.EmulateError(testutil.ModeOpen, storage.TypeTable, errors.New("open error during table compaction"))
	go func() {
		if err := h.db.CompactRange(util.Range{}); err != nil && err != ErrClosed {
			t.Error("CompactRange error: ", err)
		}
	}()
	if err := h.db.compTriggerWait(h.db.tcompCmdC); err != nil {
		t.Log("compaction error: ", err)
	}
	if err := h.closeDB0(); err != nil {
		t.Error("Close: got error: ", err)
	}
	h.openDB()
	h.stor.EmulateError(testutil.ModeOpen, storage.TypeTable, nil)

	for i := 0; i < im; i++ {
		for j := 0; j < jm; j++ {
			h.getVal(fmt.Sprintf("k%d,%d", i, j), fmt.Sprintf("v%d,%d", i, j))
		}
	}
}

func TestDB_OverlapInLevel0(t *testing.T) {
	trun(t, func(h *dbHarness) {
		h.db.memdbMaxLevel = 2

		// Fill levels 1 and 2 to disable the pushing of new memtables to levels > 0.
		h.put("100", "v100")
		h.put("999", "v999")
		h.compactMem()
		h.delete("100")
		h.delete("999")
		h.compactMem()
		h.tablesPerLevel("0,1,1")

		// Make files spanning the following ranges in level-0:
		//  files[0]  200 .. 900
		//  files[1]  300 .. 500
		// Note that files are sorted by min key.
		h.put("300", "v300")
		h.put("500", "v500")
		h.compactMem()
		h.put("200", "v200")
		h.put("600", "v600")
		h.put("900", "v900")
		h.compactMem()
		h.tablesPerLevel("2,1,1")

		// Compact away the placeholder files we created initially
		h.compactRangeAt(1, "", "")
		h.compactRangeAt(2, "", "")
		h.tablesPerLevel("2")

		// Do a memtable compaction.  Before bug-fix, the compaction would
		// not detect the overlap with level-0 files and would incorrectly place
		// the deletion in a deeper level.
		h.delete("600")
		h.compactMem()
		h.tablesPerLevel("3")
		h.get("600", false)
	})
}

func TestDB_L0_CompactionBug_Issue44_a(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.reopenDB()
	h.put("b", "v")
	h.reopenDB()
	h.delete("b")
	h.delete("a")
	h.reopenDB()
	h.delete("a")
	h.reopenDB()
	h.put("a", "v")
	h.reopenDB()
	h.reopenDB()
	h.getKeyVal("(a->v)")
	h.waitCompaction()
	h.getKeyVal("(a->v)")
}

func TestDB_L0_CompactionBug_Issue44_b(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.reopenDB()
	h.put("", "")
	h.reopenDB()
	h.delete("e")
	h.put("", "")
	h.reopenDB()
	h.put("c", "cv")
	h.reopenDB()
	h.put("", "")
	h.reopenDB()
	h.put("", "")
	h.waitCompaction()
	h.reopenDB()
	h.put("d", "dv")
	h.reopenDB()
	h.put("", "")
	h.reopenDB()
	h.delete("d")
	h.delete("b")
	h.reopenDB()
	h.getKeyVal("(->)(c->cv)")
	h.waitCompaction()
	h.getKeyVal("(->)(c->cv)")
}

func TestDB_SingleEntryMemCompaction(t *testing.T) {
	trun(t, func(h *dbHarness) {
		for i := 0; i < 10; i++ {
			h.put("big", strings.Repeat("v", opt.DefaultWriteBuffer))
			h.compactMem()
			h.put("key", strings.Repeat("v", opt.DefaultBlockSize))
			h.compactMem()
			h.put("k", "v")
			h.compactMem()
			h.put("", "")
			h.compactMem()
			h.put("verybig", strings.Repeat("v", opt.DefaultWriteBuffer*2))
			h.compactMem()
		}
	})
}

func TestDB_ManifestWriteError(t *testing.T) {
	for i := 0; i < 2; i++ {
		func() {
			h := newDbHarness(t)
			defer h.close()

			h.put("foo", "bar")
			h.getVal("foo", "bar")

			// Mem compaction (will succeed)
			h.compactMem()
			h.getVal("foo", "bar")
			v := h.db.s.version()
			if n := v.tLen(0); n != 1 {
				t.Errorf("invalid total tables, want=1 got=%d", n)
			}
			v.release()

			if i == 0 {
				h.stor.EmulateError(testutil.ModeWrite, storage.TypeManifest, errors.New("manifest write error"))
			} else {
				h.stor.EmulateError(testutil.ModeSync, storage.TypeManifest, errors.New("manifest sync error"))
			}

			// Merging compaction (will fail)
			h.compactRangeAtErr(0, "", "", true)

			h.db.Close()
			h.stor.EmulateError(testutil.ModeWrite, storage.TypeManifest, nil)
			h.stor.EmulateError(testutil.ModeSync, storage.TypeManifest, nil)

			// Should not lose data
			h.openDB()
			h.getVal("foo", "bar")
		}()
	}
}

func assertErr(t *testing.T, err error, wanterr bool) {
	if err != nil {
		if wanterr {
			t.Log("AssertErr: got error (expected): ", err)
		} else {
			t.Error("AssertErr: got error: ", err)
		}
	} else if wanterr {
		t.Error("AssertErr: expect error")
	}
}

func TestDB_ClosedIsClosed(t *testing.T) {
	h := newDbHarness(t)
	db := h.db

	var iter, iter2 iterator.Iterator
	var snap *Snapshot
	func() {
		defer h.close()

		h.put("k", "v")
		h.getVal("k", "v")

		iter = db.NewIterator(nil, h.ro)
		iter.Seek([]byte("k"))
		testKeyVal(t, iter, "k->v")

		var err error
		snap, err = db.GetSnapshot()
		if err != nil {
			t.Fatal("GetSnapshot: got error: ", err)
		}

		h.getValr(snap, "k", "v")

		iter2 = snap.NewIterator(nil, h.ro)
		iter2.Seek([]byte("k"))
		testKeyVal(t, iter2, "k->v")

		h.put("foo", "v2")
		h.delete("foo")

		// closing DB
		iter.Release()
		iter2.Release()
	}()

	assertErr(t, db.Put([]byte("x"), []byte("y"), h.wo), true)
	_, err := db.Get([]byte("k"), h.ro)
	assertErr(t, err, true)

	if iter.Valid() {
		t.Errorf("iter.Valid should false")
	}
	assertErr(t, iter.Error(), false)
	testKeyVal(t, iter, "->")
	if iter.Seek([]byte("k")) {
		t.Errorf("iter.Seek should false")
	}
	assertErr(t, iter.Error(), true)

	assertErr(t, iter2.Error(), false)

	_, err = snap.Get([]byte("k"), h.ro)
	assertErr(t, err, true)

	_, err = db.GetSnapshot()
	assertErr(t, err, true)

	iter3 := db.NewIterator(nil, h.ro)
	assertErr(t, iter3.Error(), true)

	iter3 = snap.NewIterator(nil, h.ro)
	assertErr(t, iter3.Error(), true)

	assertErr(t, db.Delete([]byte("k"), h.wo), true)

	_, err = db.GetProperty("leveldb.stats")
	assertErr(t, err, true)

	_, err = db.SizeOf([]util.Range{{Start: []byte("a"), Limit: []byte("z")}})
	assertErr(t, err, true)

	assertErr(t, db.CompactRange(util.Range{}), true)

	assertErr(t, db.Close(), true)
}

type numberComparer struct{}

func (numberComparer) num(x []byte) (n int) {
	fmt.Sscan(string(x[1:len(x)-1]), &n)
	return
}

func (numberComparer) Name() string {
	return "test.NumberComparer"
}

func (p numberComparer) Compare(a, b []byte) int {
	return p.num(a) - p.num(b)
}

func (numberComparer) Separator(dst, a, b []byte) []byte { return nil }
func (numberComparer) Successor(dst, b []byte) []byte    { return nil }

func TestDB_CustomComparer(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		Comparer:                     numberComparer{},
		WriteBuffer:                  1000,
	})
	defer h.close()

	h.put("[10]", "ten")
	h.put("[0x14]", "twenty")
	for i := 0; i < 2; i++ {
		h.getVal("[10]", "ten")
		h.getVal("[0xa]", "ten")
		h.getVal("[20]", "twenty")
		h.getVal("[0x14]", "twenty")
		h.get("[15]", false)
		h.get("[0xf]", false)
		h.compactMem()
		h.compactRange("[0]", "[9999]")
	}

	for n := 0; n < 2; n++ {
		for i := 0; i < 100; i++ {
			v := fmt.Sprintf("[%d]", i*10)
			h.put(v, v)
		}
		h.compactMem()
		h.compactRange("[0]", "[1000000]")
	}
}

func TestDB_ManualCompaction(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.db.memdbMaxLevel = 2

	h.putMulti(3, "p", "q")
	h.tablesPerLevel("1,1,1")

	// Compaction range falls before files
	h.compactRange("", "c")
	h.tablesPerLevel("1,1,1")

	// Compaction range falls after files
	h.compactRange("r", "z")
	h.tablesPerLevel("1,1,1")

	// Compaction range overlaps files
	h.compactRange("p1", "p9")
	h.tablesPerLevel("0,0,1")

	// Populate a different range
	h.putMulti(3, "c", "e")
	h.tablesPerLevel("1,1,2")

	// Compact just the new range
	h.compactRange("b", "f")
	h.tablesPerLevel("0,0,2")

	// Compact all
	h.putMulti(1, "a", "z")
	h.tablesPerLevel("0,1,2")
	h.compactRange("", "")
	h.tablesPerLevel("0,0,1")
}

func TestDB_BloomFilter(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		DisableBlockCache:            true,
		Filter:                       filter.NewBloomFilter(10),
	})
	defer h.close()

	key := func(i int) string {
		return fmt.Sprintf("key%06d", i)
	}

	const n = 10000

	// Populate multiple layers
	for i := 0; i < n; i++ {
		h.put(key(i), key(i))
	}
	h.compactMem()
	h.compactRange("a", "z")
	for i := 0; i < n; i += 100 {
		h.put(key(i), key(i))
	}
	h.compactMem()

	// Prevent auto compactions triggered by seeks
	h.stor.Stall(testutil.ModeSync, storage.TypeTable)

	// Lookup present keys. Should rarely read from small sstable.
	h.stor.ResetCounter(testutil.ModeRead, storage.TypeTable)
	for i := 0; i < n; i++ {
		h.getVal(key(i), key(i))
	}
	cnt, _ := h.stor.Counter(testutil.ModeRead, storage.TypeTable)
	t.Logf("lookup of %d present keys yield %d sstable I/O reads", n, cnt)
	if min, max := n, n+2*n/100; cnt < min || cnt > max {
		t.Errorf("num of sstable I/O reads of present keys not in range of %d - %d, got %d", min, max, cnt)
	}

	// Lookup missing keys. Should rarely read from either sstable.
	h.stor.ResetCounter(testutil.ModeRead, storage.TypeTable)
	for i := 0; i < n; i++ {
		h.get(key(i)+".missing", false)
	}
	cnt, _ = h.stor.Counter(testutil.ModeRead, storage.TypeTable)
	t.Logf("lookup of %d missing keys yield %d sstable I/O reads", n, cnt)
	if max := 3 * n / 100; cnt > max {
		t.Errorf("num of sstable I/O reads of missing keys was more than %d, got %d", max, cnt)
	}

	h.stor.Release(testutil.ModeSync, storage.TypeTable)
}

func TestDB_Concurrent(t *testing.T) {
	const n, secs, maxkey = 4, 6, 1000
	h := newDbHarness(t)
	defer h.close()

	runtime.GOMAXPROCS(runtime.NumCPU())

	var (
		closeWg sync.WaitGroup
		stop    uint32
		cnt     [n]uint32
	)

	for i := 0; i < n; i++ {
		closeWg.Add(1)
		go func(i int) {
			var put, get, found uint
			defer func() {
				t.Logf("goroutine %d stopped after %d ops, put=%d get=%d found=%d missing=%d",
					i, cnt[i], put, get, found, get-found)
				closeWg.Done()
			}()

			rnd := rand.New(rand.NewSource(int64(1000 + i)))
			for atomic.LoadUint32(&stop) == 0 {
				x := cnt[i]

				k := rnd.Intn(maxkey)
				kstr := fmt.Sprintf("%016d", k)

				if (rnd.Int() % 2) > 0 {
					put++
					h.put(kstr, fmt.Sprintf("%d.%d.%-1000d", k, i, x))
				} else {
					get++
					v, err := h.db.Get([]byte(kstr), h.ro)
					if err == nil {
						found++
						rk, ri, rx := 0, -1, uint32(0)
						fmt.Sscanf(string(v), "%d.%d.%d", &rk, &ri, &rx)
						if rk != k {
							t.Errorf("invalid key want=%d got=%d", k, rk)
						}
						if ri < 0 || ri >= n {
							t.Error("invalid goroutine number: ", ri)
						} else {
							tx := atomic.LoadUint32(&(cnt[ri]))
							if rx > tx {
								t.Errorf("invalid seq number, %d > %d ", rx, tx)
							}
						}
					} else if err != ErrNotFound {
						t.Error("Get: got error: ", err)
						return
					}
				}
				atomic.AddUint32(&cnt[i], 1)
			}
		}(i)
	}

	time.Sleep(secs * time.Second)
	atomic.StoreUint32(&stop, 1)
	closeWg.Wait()
}

func TestDB_ConcurrentIterator(t *testing.T) {
	const n, n2 = 4, 1000
	h := newDbHarnessWopt(t, &opt.Options{DisableLargeBatchTransaction: true, WriteBuffer: 30})
	defer h.close()

	runtime.GOMAXPROCS(runtime.NumCPU())

	var (
		closeWg sync.WaitGroup
		stop    uint32
	)

	for i := 0; i < n; i++ {
		closeWg.Add(1)
		go func(i int) {
			for k := 0; atomic.LoadUint32(&stop) == 0; k++ {
				h.put(fmt.Sprintf("k%d", k), fmt.Sprintf("%d.%d.", k, i)+strings.Repeat("x", 10))
			}
			closeWg.Done()
		}(i)
	}

	for i := 0; i < n; i++ {
		closeWg.Add(1)
		go func(i int) {
			for k := 1000000; k < 0 || atomic.LoadUint32(&stop) == 0; k-- {
				h.put(fmt.Sprintf("k%d", k), fmt.Sprintf("%d.%d.", k, i)+strings.Repeat("x", 10))
			}
			closeWg.Done()
		}(i)
	}

	cmp := comparer.DefaultComparer
	for i := 0; i < n2; i++ {
		closeWg.Add(1)
		go func(i int) {
			it := h.db.NewIterator(nil, nil)
			var pk []byte
			for it.Next() {
				kk := it.Key()
				if cmp.Compare(kk, pk) <= 0 {
					t.Errorf("iter %d: %q is successor of %q", i, pk, kk)
				}
				pk = append(pk[:0], kk...)
				var k, vk, vi int
				if n, err := fmt.Sscanf(string(it.Key()), "k%d", &k); err != nil {
					t.Errorf("iter %d: Scanf error on key %q: %v", i, it.Key(), err)
				} else if n < 1 {
					t.Errorf("iter %d: Cannot parse key %q", i, it.Key())
				}
				if n, err := fmt.Sscanf(string(it.Value()), "%d.%d", &vk, &vi); err != nil {
					t.Errorf("iter %d: Scanf error on value %q: %v", i, it.Value(), err)
				} else if n < 2 {
					t.Errorf("iter %d: Cannot parse value %q", i, it.Value())
				}

				if vk != k {
					t.Errorf("iter %d: invalid value i=%d, want=%d got=%d", i, vi, k, vk)
				}
			}
			if err := it.Error(); err != nil {
				t.Errorf("iter %d: Got error: %v", i, err)
			}
			it.Release()
			closeWg.Done()
		}(i)
	}

	atomic.StoreUint32(&stop, 1)
	closeWg.Wait()
}

func TestDB_ConcurrentWrite(t *testing.T) {
	const n, bk, niter = 10, 3, 10000
	h := newDbHarness(t)
	defer h.close()

	runtime.GOMAXPROCS(runtime.NumCPU())

	var wg sync.WaitGroup
	for i := 0; i < n; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			for k := 0; k < niter; k++ {
				kstr := fmt.Sprintf("put-%d.%d", i, k)
				vstr := fmt.Sprintf("v%d", k)
				h.put(kstr, vstr)
				// Key should immediately available after put returns.
				h.getVal(kstr, vstr)
			}
		}(i)
	}
	for i := 0; i < n; i++ {
		wg.Add(1)
		batch := &Batch{}
		go func(i int) {
			defer wg.Done()
			for k := 0; k < niter; k++ {
				batch.Reset()
				for j := 0; j < bk; j++ {
					batch.Put([]byte(fmt.Sprintf("batch-%d.%d.%d", i, k, j)), []byte(fmt.Sprintf("v%d", k)))
				}
				h.write(batch)
				// Key should immediately available after put returns.
				for j := 0; j < bk; j++ {
					h.getVal(fmt.Sprintf("batch-%d.%d.%d", i, k, j), fmt.Sprintf("v%d", k))
				}
			}
		}(i)
	}
	wg.Wait()
}

func TestDB_CreateReopenDbOnFile(t *testing.T) {
	dbpath := filepath.Join(os.TempDir(), fmt.Sprintf("goleveldbtestCreateReopenDbOnFile-%d", os.Getuid()))
	if err := os.RemoveAll(dbpath); err != nil {
		t.Fatal("cannot remove old db: ", err)
	}
	defer os.RemoveAll(dbpath)

	for i := 0; i < 3; i++ {
		stor, err := storage.OpenFile(dbpath, false)
		if err != nil {
			t.Fatalf("(%d) cannot open storage: %s", i, err)
		}
		db, err := Open(stor, nil)
		if err != nil {
			t.Fatalf("(%d) cannot open db: %s", i, err)
		}
		if err := db.Put([]byte("foo"), []byte("bar"), nil); err != nil {
			t.Fatalf("(%d) cannot write to db: %s", i, err)
		}
		if err := db.Close(); err != nil {
			t.Fatalf("(%d) cannot close db: %s", i, err)
		}
		if err := stor.Close(); err != nil {
			t.Fatalf("(%d) cannot close storage: %s", i, err)
		}
	}
}

func TestDB_CreateReopenDbOnFile2(t *testing.T) {
	dbpath := filepath.Join(os.TempDir(), fmt.Sprintf("goleveldbtestCreateReopenDbOnFile2-%d", os.Getuid()))
	if err := os.RemoveAll(dbpath); err != nil {
		t.Fatal("cannot remove old db: ", err)
	}
	defer os.RemoveAll(dbpath)

	for i := 0; i < 3; i++ {
		db, err := OpenFile(dbpath, nil)
		if err != nil {
			t.Fatalf("(%d) cannot open db: %s", i, err)
		}
		if err := db.Put([]byte("foo"), []byte("bar"), nil); err != nil {
			t.Fatalf("(%d) cannot write to db: %s", i, err)
		}
		if err := db.Close(); err != nil {
			t.Fatalf("(%d) cannot close db: %s", i, err)
		}
	}
}

func TestDB_DeletionMarkersOnMemdb(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.put("foo", "v1")
	h.compactMem()
	h.delete("foo")
	h.get("foo", false)
	h.getKeyVal("")
}

func TestDB_LeveldbIssue178(t *testing.T) {
	nKeys := (opt.DefaultCompactionTableSize / 30) * 5
	key1 := func(i int) string {
		return fmt.Sprintf("my_key_%d", i)
	}
	key2 := func(i int) string {
		return fmt.Sprintf("my_key_%d_xxx", i)
	}

	// Disable compression since it affects the creation of layers and the
	// code below is trying to test against a very specific scenario.
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		Compression:                  opt.NoCompression,
	})
	defer h.close()

	// Create first key range.
	batch := new(Batch)
	for i := 0; i < nKeys; i++ {
		batch.Put([]byte(key1(i)), []byte("value for range 1 key"))
	}
	h.write(batch)

	// Create second key range.
	batch.Reset()
	for i := 0; i < nKeys; i++ {
		batch.Put([]byte(key2(i)), []byte("value for range 2 key"))
	}
	h.write(batch)

	// Delete second key range.
	batch.Reset()
	for i := 0; i < nKeys; i++ {
		batch.Delete([]byte(key2(i)))
	}
	h.write(batch)
	h.waitMemCompaction()

	// Run manual compaction.
	h.compactRange(key1(0), key1(nKeys-1))

	// Checking the keys.
	h.assertNumKeys(nKeys)
}

func TestDB_LeveldbIssue200(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.put("1", "b")
	h.put("2", "c")
	h.put("3", "d")
	h.put("4", "e")
	h.put("5", "f")

	iter := h.db.NewIterator(nil, h.ro)

	// Add an element that should not be reflected in the iterator.
	h.put("25", "cd")

	iter.Seek([]byte("5"))
	assertBytes(t, []byte("5"), iter.Key())
	iter.Prev()
	assertBytes(t, []byte("4"), iter.Key())
	iter.Prev()
	assertBytes(t, []byte("3"), iter.Key())
	iter.Next()
	assertBytes(t, []byte("4"), iter.Key())
	iter.Next()
	assertBytes(t, []byte("5"), iter.Key())
}

func TestDB_GoleveldbIssue74(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		WriteBuffer:                  1 * opt.MiB,
	})
	defer h.close()

	const n, dur = 10000, 5 * time.Second

	runtime.GOMAXPROCS(runtime.NumCPU())

	until := time.Now().Add(dur)
	wg := new(sync.WaitGroup)
	wg.Add(2)
	var done uint32
	go func() {
		var i int
		defer func() {
			t.Logf("WRITER DONE #%d", i)
			atomic.StoreUint32(&done, 1)
			wg.Done()
		}()

		b := new(Batch)
		for ; time.Now().Before(until) && atomic.LoadUint32(&done) == 0; i++ {
			if t.Failed() {
				return
			}

			iv := fmt.Sprintf("VAL%010d", i)
			for k := 0; k < n; k++ {
				key := fmt.Sprintf("KEY%06d", k)
				b.Put([]byte(key), []byte(key+iv))
				b.Put([]byte(fmt.Sprintf("PTR%06d", k)), []byte(key))
			}
			h.write(b)

			b.Reset()
			snap := h.getSnapshot()
			iter := snap.NewIterator(util.BytesPrefix([]byte("PTR")), nil)
			var k int
			for ; iter.Next(); k++ {
				if t.Failed() {
					return
				}

				ptrKey := iter.Key()
				key := iter.Value()

				if _, err := snap.Get(ptrKey, nil); err != nil {
					t.Errorf("WRITER #%d snapshot.Get %q: %v", i, ptrKey, err)
					return
				}
				if value, err := snap.Get(key, nil); err != nil {
					t.Errorf("WRITER #%d snapshot.Get %q: %v", i, key, err)
					return
				} else if string(value) != string(key)+iv {
					t.Errorf("WRITER #%d snapshot.Get %q got invalid value, want %q got %q", i, key, string(key)+iv, value)
					return
				}

				b.Delete(key)
				b.Delete(ptrKey)
			}
			h.write(b)
			iter.Release()
			snap.Release()
			if k != n {
				t.Errorf("#%d %d != %d", i, k, n)
			}
		}
	}()
	go func() {
		var i int
		defer func() {
			t.Logf("READER DONE #%d", i)
			atomic.StoreUint32(&done, 1)
			wg.Done()
		}()
		for ; time.Now().Before(until) && atomic.LoadUint32(&done) == 0; i++ {
			if t.Failed() {
				return
			}

			snap := h.getSnapshot()
			iter := snap.NewIterator(util.BytesPrefix([]byte("PTR")), nil)
			var prevValue string
			var k int
			for ; iter.Next(); k++ {
				if t.Failed() {
					return
				}

				ptrKey := iter.Key()
				key := iter.Value()

				if _, err := snap.Get(ptrKey, nil); err != nil {
					t.Errorf("READER #%d snapshot.Get %q: %v", i, ptrKey, err)
					return
				}

				if value, err := snap.Get(key, nil); err != nil {
					t.Errorf("READER #%d snapshot.Get %q: %v", i, key, err)
					return
				} else if prevValue != "" && string(value) != string(key)+prevValue {
					t.Errorf("READER #%d snapshot.Get %q got invalid value, want %q got %q", i, key, string(key)+prevValue, value)
					return
				} else {
					prevValue = string(value[len(key):])
				}
			}
			iter.Release()
			snap.Release()
			if k > 0 && k != n {
				t.Errorf("#%d %d != %d", i, k, n)
			}
		}
	}()
	wg.Wait()
}

func TestDB_GetProperties(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	_, err := h.db.GetProperty("leveldb.num-files-at-level")
	if err == nil {
		t.Error("GetProperty() failed to detect missing level")
	}

	_, err = h.db.GetProperty("leveldb.num-files-at-level0")
	if err != nil {
		t.Error("got unexpected error", err)
	}

	_, err = h.db.GetProperty("leveldb.num-files-at-level0x")
	if err == nil {
		t.Error("GetProperty() failed to detect invalid level")
	}
}

func TestDB_GoleveldbIssue72and83(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		WriteBuffer:                  1 * opt.MiB,
		OpenFilesCacheCapacity:       3,
	})
	defer h.close()

	const n, wn, dur = 10000, 100, 30 * time.Second

	runtime.GOMAXPROCS(runtime.NumCPU())

	randomData := func(prefix byte, i int) []byte {
		data := make([]byte, 1+4+32+64+32)
		_, err := crand.Reader.Read(data[1 : len(data)-8])
		if err != nil {
			panic(err)
		}
		data[0] = prefix
		binary.LittleEndian.PutUint32(data[len(data)-8:], uint32(i))
		binary.LittleEndian.PutUint32(data[len(data)-4:], util.NewCRC(data[:len(data)-4]).Value())
		return data
	}

	keys := make([][]byte, n)
	for i := range keys {
		keys[i] = randomData(1, 0)
	}

	until := time.Now().Add(dur)
	wg := new(sync.WaitGroup)
	wg.Add(3)
	var done uint32
	go func() {
		i := 0
		defer func() {
			t.Logf("WRITER DONE #%d", i)
			wg.Done()
		}()

		b := new(Batch)
		for ; i < wn && atomic.LoadUint32(&done) == 0; i++ {
			if t.Failed() {
				return
			}

			b.Reset()
			for _, k1 := range keys {
				k2 := randomData(2, i)
				b.Put(k2, randomData(42, i))
				b.Put(k1, k2)
			}
			if err := h.db.Write(b, h.wo); err != nil {
				atomic.StoreUint32(&done, 1)
				t.Errorf("WRITER #%d db.Write: %v", i, err)
				return
			}
		}
	}()
	go func() {
		var i int
		defer func() {
			t.Logf("READER0 DONE #%d", i)
			atomic.StoreUint32(&done, 1)
			wg.Done()
		}()
		for ; time.Now().Before(until) && atomic.LoadUint32(&done) == 0; i++ {
			if t.Failed() {
				return
			}

			snap := h.getSnapshot()
			seq := snap.elem.seq
			if seq == 0 {
				snap.Release()
				continue
			}
			iter := snap.NewIterator(util.BytesPrefix([]byte{1}), nil)
			writei := int(seq/(n*2) - 1)
			var k int
			for ; iter.Next(); k++ {
				if t.Failed() {
					return
				}

				k1 := iter.Key()
				k2 := iter.Value()
				k1checksum0 := binary.LittleEndian.Uint32(k1[len(k1)-4:])
				k1checksum1 := util.NewCRC(k1[:len(k1)-4]).Value()
				if k1checksum0 != k1checksum1 {
					t.Errorf("READER0 #%d.%d W#%d invalid K1 checksum: %#x != %#x", i, k, writei, k1checksum0, k1checksum0)
					return
				}
				k2checksum0 := binary.LittleEndian.Uint32(k2[len(k2)-4:])
				k2checksum1 := util.NewCRC(k2[:len(k2)-4]).Value()
				if k2checksum0 != k2checksum1 {
					t.Errorf("READER0 #%d.%d W#%d invalid K2 checksum: %#x != %#x", i, k, writei, k2checksum0, k2checksum1)
					return
				}
				kwritei := int(binary.LittleEndian.Uint32(k2[len(k2)-8:]))
				if writei != kwritei {
					t.Errorf("READER0 #%d.%d W#%d invalid write iteration num: %d", i, k, writei, kwritei)
					return
				}
				if _, err := snap.Get(k2, nil); err != nil {
					t.Errorf("READER0 #%d.%d W#%d snap.Get: %v\nk1: %x\n -> k2: %x", i, k, writei, err, k1, k2)
					return
				}
			}
			if err := iter.Error(); err != nil {
				t.Errorf("READER0 #%d.%d W#%d snap.Iterator: %v", i, k, writei, err)
				return
			}
			iter.Release()
			snap.Release()
			if k > 0 && k != n {
				t.Errorf("READER0 #%d W#%d short read, got=%d want=%d", i, writei, k, n)
			}
		}
	}()
	go func() {
		var i int
		defer func() {
			t.Logf("READER1 DONE #%d", i)
			atomic.StoreUint32(&done, 1)
			wg.Done()
		}()
		for ; time.Now().Before(until) && atomic.LoadUint32(&done) == 0; i++ {
			if t.Failed() {
				return
			}

			iter := h.db.NewIterator(nil, nil)
			seq := iter.(*dbIter).seq
			if seq == 0 {
				iter.Release()
				continue
			}
			writei := int(seq/(n*2) - 1)
			var k int
			for ok := iter.Last(); ok; ok = iter.Prev() {
				k++
			}
			if err := iter.Error(); err != nil {
				t.Errorf("READER1 #%d.%d W#%d db.Iterator: %v", i, k, writei, err)
				return
			}
			iter.Release()
			if m := (writei+1)*n + n; k != m {
				t.Errorf("READER1 #%d W#%d short read, got=%d want=%d", i, writei, k, m)
				return
			}
		}
	}()

	wg.Wait()
}

func TestDB_TransientError(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		WriteBuffer:                  128 * opt.KiB,
		OpenFilesCacheCapacity:       3,
		DisableCompactionBackoff:     true,
	})
	defer h.close()

	const (
		nSnap = 20
		nKey  = 10000
	)

	var (
		snaps [nSnap]*Snapshot
		b     = &Batch{}
	)
	for i := range snaps {
		vtail := fmt.Sprintf("VAL%030d", i)
		b.Reset()
		for k := 0; k < nKey; k++ {
			key := fmt.Sprintf("KEY%8d", k)
			b.Put([]byte(key), []byte(key+vtail))
		}
		h.stor.EmulateError(testutil.ModeOpen|testutil.ModeRead, storage.TypeTable, errors.New("table transient read error"))
		if err := h.db.Write(b, nil); err != nil {
			t.Logf("WRITE #%d error: %v", i, err)
			h.stor.EmulateError(testutil.ModeOpen|testutil.ModeRead, storage.TypeTable, nil)
			for {
				if err := h.db.Write(b, nil); err == nil {
					break
				} else if errors.IsCorrupted(err) {
					t.Fatalf("WRITE #%d corrupted: %v", i, err)
				}
			}
		}

		snaps[i] = h.db.newSnapshot()
		b.Reset()
		for k := 0; k < nKey; k++ {
			key := fmt.Sprintf("KEY%8d", k)
			b.Delete([]byte(key))
		}
		h.stor.EmulateError(testutil.ModeOpen|testutil.ModeRead, storage.TypeTable, errors.New("table transient read error"))
		if err := h.db.Write(b, nil); err != nil {
			t.Logf("WRITE #%d  error: %v", i, err)
			h.stor.EmulateError(testutil.ModeOpen|testutil.ModeRead, storage.TypeTable, nil)
			for {
				if err := h.db.Write(b, nil); err == nil {
					break
				} else if errors.IsCorrupted(err) {
					t.Fatalf("WRITE #%d corrupted: %v", i, err)
				}
			}
		}
	}
	h.stor.EmulateError(testutil.ModeOpen|testutil.ModeRead, storage.TypeTable, nil)

	runtime.GOMAXPROCS(runtime.NumCPU())

	rnd := rand.New(rand.NewSource(0xecafdaed))
	wg := &sync.WaitGroup{}
	for i, snap := range snaps {
		wg.Add(2)

		go func(i int, snap *Snapshot, sk []int) {
			defer wg.Done()

			vtail := fmt.Sprintf("VAL%030d", i)
			for _, k := range sk {
				if t.Failed() {
					return
				}

				key := fmt.Sprintf("KEY%8d", k)
				xvalue, err := snap.Get([]byte(key), nil)
				if err != nil {
					t.Errorf("READER_GET #%d SEQ=%d K%d error: %v", i, snap.elem.seq, k, err)
					return
				}
				value := key + vtail
				if !bytes.Equal([]byte(value), xvalue) {
					t.Errorf("READER_GET #%d SEQ=%d K%d invalid value: want %q, got %q", i, snap.elem.seq, k, value, xvalue)
					return
				}
			}
		}(i, snap, rnd.Perm(nKey))

		go func(i int, snap *Snapshot) {
			defer wg.Done()

			vtail := fmt.Sprintf("VAL%030d", i)
			iter := snap.NewIterator(nil, nil)
			defer iter.Release()
			for k := 0; k < nKey; k++ {
				if t.Failed() {
					return
				}

				if !iter.Next() {
					if err := iter.Error(); err != nil {
						t.Errorf("READER_ITER #%d K%d error: %v", i, k, err)
						return
					}
					t.Errorf("READER_ITER #%d K%d eoi", i, k)
					return
				}
				key := fmt.Sprintf("KEY%8d", k)
				xkey := iter.Key()
				if !bytes.Equal([]byte(key), xkey) {
					t.Errorf("READER_ITER #%d K%d invalid key: want %q, got %q", i, k, key, xkey)
					return
				}
				value := key + vtail
				xvalue := iter.Value()
				if !bytes.Equal([]byte(value), xvalue) {
					t.Errorf("READER_ITER #%d K%d invalid value: want %q, got %q", i, k, value, xvalue)
					return
				}
			}
		}(i, snap)
	}

	wg.Wait()
}

func TestDB_UkeyShouldntHopAcrossTable(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		WriteBuffer:                  112 * opt.KiB,
		CompactionTableSize:          90 * opt.KiB,
		CompactionExpandLimitFactor:  1,
	})
	defer h.close()

	const (
		nSnap = 190
		nKey  = 140
	)

	var (
		snaps [nSnap]*Snapshot
		b     = &Batch{}
	)
	for i := range snaps {
		vtail := fmt.Sprintf("VAL%030d", i)
		b.Reset()
		for k := 0; k < nKey; k++ {
			key := fmt.Sprintf("KEY%08d", k)
			b.Put([]byte(key), []byte(key+vtail))
		}
		if err := h.db.Write(b, nil); err != nil {
			t.Fatalf("WRITE #%d error: %v", i, err)
		}

		snaps[i] = h.db.newSnapshot()
		b.Reset()
		for k := 0; k < nKey; k++ {
			key := fmt.Sprintf("KEY%08d", k)
			b.Delete([]byte(key))
		}
		if err := h.db.Write(b, nil); err != nil {
			t.Fatalf("WRITE #%d  error: %v", i, err)
		}
	}

	h.compactMem()

	h.waitCompaction()
	for level, tables := range h.db.s.stVersion.levels {
		for _, table := range tables {
			t.Logf("L%d@%d %q:%q", level, table.fd.Num, table.imin, table.imax)
		}
	}

	h.compactRangeAt(0, "", "")
	h.waitCompaction()
	for level, tables := range h.db.s.stVersion.levels {
		for _, table := range tables {
			t.Logf("L%d@%d %q:%q", level, table.fd.Num, table.imin, table.imax)
		}
	}
	h.compactRangeAt(1, "", "")
	h.waitCompaction()
	for level, tables := range h.db.s.stVersion.levels {
		for _, table := range tables {
			t.Logf("L%d@%d %q:%q", level, table.fd.Num, table.imin, table.imax)
		}
	}
	runtime.GOMAXPROCS(runtime.NumCPU())

	wg := &sync.WaitGroup{}
	for i, snap := range snaps {
		wg.Add(1)

		go func(i int, snap *Snapshot) {
			defer wg.Done()

			vtail := fmt.Sprintf("VAL%030d", i)
			for k := 0; k < nKey; k++ {
				if t.Failed() {
					return
				}

				key := fmt.Sprintf("KEY%08d", k)
				xvalue, err := snap.Get([]byte(key), nil)
				if err != nil {
					t.Errorf("READER_GET #%d SEQ=%d K%d error: %v", i, snap.elem.seq, k, err)
					return
				}
				value := key + vtail
				if !bytes.Equal([]byte(value), xvalue) {
					t.Errorf("READER_GET #%d SEQ=%d K%d invalid value: want %q, got %q", i, snap.elem.seq, k, value, xvalue)
					return
				}
			}
		}(i, snap)
	}

	wg.Wait()
}

func TestDB_TableCompactionBuilder(t *testing.T) {
	gomega.RegisterTestingT(t)
	stor := testutil.NewStorage()
	stor.OnLog(testingLogger(t))
	stor.OnClose(testingPreserveOnFailed(t))
	defer stor.Close()

	const nSeq = 99

	o := &opt.Options{
		DisableLargeBatchTransaction: true,
		WriteBuffer:                  112 * opt.KiB,
		CompactionTableSize:          43 * opt.KiB,
		CompactionExpandLimitFactor:  1,
		CompactionGPOverlapsFactor:   1,
		DisableBlockCache:            true,
	}
	s, err := newSession(stor, o)
	if err != nil {
		t.Fatal(err)
	}
	if err := s.create(); err != nil {
		t.Fatal(err)
	}
	defer s.close()
	var (
		seq        uint64
		targetSize = 5 * o.CompactionTableSize
		value      = bytes.Repeat([]byte{'0'}, 100)
	)
	for i := 0; i < 2; i++ {
		tw, err := s.tops.create(0)
		if err != nil {
			t.Fatal(err)
		}
		for k := 0; tw.tw.BytesLen() < targetSize; k++ {
			key := []byte(fmt.Sprintf("%09d", k))
			seq += nSeq - 1
			for x := uint64(0); x < nSeq; x++ {
				if err := tw.append(makeInternalKey(nil, key, seq-x, keyTypeVal), value); err != nil {
					t.Fatal(err)
				}
			}
		}
		tf, err := tw.finish()
		if err != nil {
			t.Fatal(err)
		}
		rec := &sessionRecord{}
		rec.addTableFile(i, tf)
		if err := s.commit(rec, false); err != nil {
			t.Fatal(err)
		}
	}

	// Build grandparent.
	v := s.version()
	c := newCompaction(s, v, 1, append(tFiles{}, v.levels[1]...), undefinedCompaction)
	rec := &sessionRecord{}
	b := &tableCompactionBuilder{
		s:         s,
		c:         c,
		rec:       rec,
		stat1:     new(cStatStaging),
		minSeq:    0,
		strict:    true,
		tableSize: o.CompactionTableSize/3 + 961,
	}
	if err := b.run(new(compactionTransactCounter)); err != nil {
		t.Fatal(err)
	}
	for _, t := range c.levels[0] {
		rec.delTable(c.sourceLevel, t.fd.Num)
	}
	if err := s.commit(rec, false); err != nil {
		t.Fatal(err)
	}
	c.release()

	// Build level-1.
	v = s.version()
	c = newCompaction(s, v, 0, append(tFiles{}, v.levels[0]...), undefinedCompaction)
	rec = &sessionRecord{}
	b = &tableCompactionBuilder{
		s:         s,
		c:         c,
		rec:       rec,
		stat1:     new(cStatStaging),
		minSeq:    0,
		strict:    true,
		tableSize: o.CompactionTableSize,
	}
	if err := b.run(new(compactionTransactCounter)); err != nil {
		t.Fatal(err)
	}
	for _, t := range c.levels[0] {
		rec.delTable(c.sourceLevel, t.fd.Num)
	}
	// Move grandparent to level-3
	for _, t := range v.levels[2] {
		rec.delTable(2, t.fd.Num)
		rec.addTableFile(3, t)
	}
	if err := s.commit(rec, false); err != nil {
		t.Fatal(err)
	}
	c.release()

	v = s.version()
	for level, want := range []bool{false, true, false, true} {
		got := len(v.levels[level]) > 0
		if want != got {
			t.Fatalf("invalid level-%d tables len: want %v, got %v", level, want, got)
		}
	}
	for i, f := range v.levels[1][:len(v.levels[1])-1] {
		nf := v.levels[1][i+1]
		if bytes.Equal(f.imax.ukey(), nf.imin.ukey()) {
			t.Fatalf("KEY %q hop across table %d .. %d", f.imax.ukey(), f.fd.Num, nf.fd.Num)
		}
	}
	v.release()

	// Compaction with transient error.
	v = s.version()
	c = newCompaction(s, v, 1, append(tFiles{}, v.levels[1]...), undefinedCompaction)
	rec = &sessionRecord{}
	b = &tableCompactionBuilder{
		s:         s,
		c:         c,
		rec:       rec,
		stat1:     new(cStatStaging),
		minSeq:    0,
		strict:    true,
		tableSize: o.CompactionTableSize,
	}
	stor.EmulateErrorOnce(testutil.ModeSync, storage.TypeTable, errors.New("table sync error (once)"))
	stor.EmulateRandomError(testutil.ModeRead|testutil.ModeWrite, storage.TypeTable, 0.01, errors.New("table random IO error"))
	for {
		if err := b.run(new(compactionTransactCounter)); err != nil {
			t.Logf("(expected) b.run: %v", err)
		} else {
			break
		}
	}
	if err := s.commit(rec, false); err != nil {
		t.Fatal(err)
	}
	c.release()

	stor.EmulateErrorOnce(testutil.ModeSync, storage.TypeTable, nil)
	stor.EmulateRandomError(testutil.ModeRead|testutil.ModeWrite, storage.TypeTable, 0, nil)

	v = s.version()
	if len(v.levels[1]) != len(v.levels[2]) {
		t.Fatalf("invalid tables length, want %d, got %d", len(v.levels[1]), len(v.levels[2]))
	}
	for i, f0 := range v.levels[1] {
		f1 := v.levels[2][i]
		iter0 := s.tops.newIterator(f0, nil, nil)
		iter1 := s.tops.newIterator(f1, nil, nil)
		for j := 0; true; j++ {
			next0 := iter0.Next()
			next1 := iter1.Next()
			if next0 != next1 {
				t.Fatalf("#%d.%d invalid eoi: want %v, got %v", i, j, next0, next1)
			}
			key0 := iter0.Key()
			key1 := iter1.Key()
			if !bytes.Equal(key0, key1) {
				t.Fatalf("#%d.%d invalid key: want %q, got %q", i, j, key0, key1)
			}
			if next0 == false {
				break
			}
		}
		iter0.Release()
		iter1.Release()
	}
	v.release()
}

func testDB_IterTriggeredCompaction(t *testing.T, limitDiv int) {
	const (
		vSize = 200 * opt.KiB
		tSize = 100 * opt.MiB
		mIter = 100
		n     = tSize / vSize
	)

	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		Compression:                  opt.NoCompression,
		DisableBlockCache:            true,
	})
	defer h.close()

	h.db.memdbMaxLevel = 2

	key := func(x int) string {
		return fmt.Sprintf("v%06d", x)
	}

	// Fill.
	value := strings.Repeat("x", vSize)
	for i := 0; i < n; i++ {
		h.put(key(i), value)
	}
	h.compactMem()

	// Delete all.
	for i := 0; i < n; i++ {
		h.delete(key(i))
	}
	h.compactMem()

	var (
		limit = n / limitDiv

		startKey = key(0)
		limitKey = key(limit)
		maxKey   = key(n)
		slice    = &util.Range{Limit: []byte(limitKey)}

		initialSize0 = h.sizeOf(startKey, limitKey)
		initialSize1 = h.sizeOf(limitKey, maxKey)
	)

	t.Logf("initial size %s [rest %s]", shortenb(initialSize0), shortenb(initialSize1))

	for r := 0; true; r++ {
		if r >= mIter {
			t.Fatal("taking too long to compact")
		}

		// Iterates.
		iter := h.db.NewIterator(slice, h.ro)
		for iter.Next() {
		}
		if err := iter.Error(); err != nil {
			t.Fatalf("Iter err: %v", err)
		}
		iter.Release()

		// Wait compaction.
		h.waitCompaction()

		// Check size.
		size0 := h.sizeOf(startKey, limitKey)
		size1 := h.sizeOf(limitKey, maxKey)
		t.Logf("#%03d size %s [rest %s]", r, shortenb(size0), shortenb(size1))
		if size0 < initialSize0/10 {
			break
		}
	}

	if initialSize1 > 0 {
		h.sizeAssert(limitKey, maxKey, initialSize1/4-opt.MiB, initialSize1+opt.MiB)
	}
}

func TestDB_IterTriggeredCompaction(t *testing.T) {
	testDB_IterTriggeredCompaction(t, 1)
}

func TestDB_IterTriggeredCompactionHalf(t *testing.T) {
	testDB_IterTriggeredCompaction(t, 2)
}

func TestDB_ReadOnly(t *testing.T) {
	h := newDbHarness(t)
	defer h.close()

	h.put("foo", "v1")
	h.put("bar", "v2")
	h.compactMem()

	h.put("xfoo", "v1")
	h.put("xbar", "v2")

	t.Log("Trigger read-only")
	if err := h.db.SetReadOnly(); err != nil {
		h.close()
		t.Fatalf("SetReadOnly error: %v", err)
	}

	mode := testutil.ModeCreate | testutil.ModeRemove | testutil.ModeRename | testutil.ModeWrite | testutil.ModeSync
	h.stor.EmulateError(mode, storage.TypeAll, errors.New("read-only DB shouldn't writes"))

	ro := func(key, value, wantValue string) {
		if err := h.db.Put([]byte(key), []byte(value), h.wo); err != ErrReadOnly {
			t.Fatalf("unexpected error: %v", err)
		}
		h.getVal(key, wantValue)
	}

	ro("foo", "vx", "v1")

	h.o.ReadOnly = true
	h.reopenDB()

	ro("foo", "vx", "v1")
	ro("bar", "vx", "v2")
	h.assertNumKeys(4)
}

func TestDB_BulkInsertDelete(t *testing.T) {
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		Compression:                  opt.NoCompression,
		CompactionTableSize:          128 * opt.KiB,
		CompactionTotalSize:          1 * opt.MiB,
		WriteBuffer:                  256 * opt.KiB,
	})
	defer h.close()

	const R = 100
	const N = 2500
	key := make([]byte, 4)
	value := make([]byte, 256)
	for i := 0; i < R; i++ {
		offset := N * i
		for j := 0; j < N; j++ {
			binary.BigEndian.PutUint32(key, uint32(offset+j))
			if err := h.db.Put(key, value, nil); err != nil {
				t.Fatal("Put error: ", err)
			}
		}
		for j := 0; j < N; j++ {
			binary.BigEndian.PutUint32(key, uint32(offset+j))
			if err := h.db.Delete(key, nil); err != nil {
				t.Fatal("Delete error: ", err)
			}
		}
	}

	h.waitCompaction()
	if tot := h.totalTables(); tot > 10 {
		t.Fatalf("too many uncompacted tables: %d (%s)", tot, h.getTablesPerLevel())
	}
}

func TestDB_GracefulClose(t *testing.T) {
	runtime.GOMAXPROCS(4)
	h := newDbHarnessWopt(t, &opt.Options{
		DisableLargeBatchTransaction: true,
		Compression:                  opt.NoCompression,
		CompactionTableSize:          1 * opt.MiB,
		WriteBuffer:                  1 * opt.MiB,
	})
	defer h.close()

	var closeWait sync.WaitGroup

	// During write.
	n := 0
	closing := false
	for i := 0; i < 1000000; i++ {
		if !closing && h.totalTables() > 3 {
			t.Logf("close db during write, index=%d", i)
			closeWait.Add(1)
			go func() {
				h.closeDB()
				closeWait.Done()
			}()
			closing = true
		}
		if err := h.db.Put([]byte(fmt.Sprintf("%09d", i)), []byte(fmt.Sprintf("VAL-%09d", i)), h.wo); err != nil {
			t.Logf("Put error: %s (expected)", err)
			n = i
			break
		}
	}
	closeWait.Wait()

	// During read.
	h.openDB()
	closing = false
	for i := 0; i < n; i++ {
		if !closing && i > n/2 {
			t.Logf("close db during read, index=%d", i)
			closeWait.Add(1)
			go func() {
				h.closeDB()
				closeWait.Done()
			}()
			closing = true
		}
		if _, err := h.db.Get([]byte(fmt.Sprintf("%09d", i)), h.ro); err != nil {
			t.Logf("Get error: %s (expected)", err)
			break
		}
	}
	closeWait.Wait()

	// During iterate.
	h.openDB()
	closing = false
	iter := h.db.NewIterator(nil, h.ro)
	for i := 0; iter.Next(); i++ {
		if len(iter.Key()) == 0 || len(iter.Value()) == 0 {
			t.Error("Key or value has zero length")
		}
		if !closing {
			t.Logf("close db during iter, index=%d", i)
			closeWait.Add(1)
			go func() {
				h.closeDB()
				closeWait.Done()
			}()
			closing = true
		}
		time.Sleep(time.Millisecond)
	}
	if err := iter.Error(); err != nil {
		t.Logf("Iter error: %s (expected)", err)
	}
	iter.Release()
	closeWait.Wait()
}
```

## File: `leveldb/db_transaction.go`
```go
// Copyright (c) 2016, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"errors"
	"sync"
	"time"

	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/util"
)

var errTransactionDone = errors.New("leveldb: transaction already closed")

// Transaction is the transaction handle.
type Transaction struct {
	db        *DB
	lk        sync.RWMutex
	seq       uint64
	mem       *memDB
	tables    tFiles
	ikScratch []byte
	rec       sessionRecord
	stats     cStatStaging
	closed    bool
}

// Get gets the value for the given key. It returns ErrNotFound if the
// DB does not contains the key.
//
// The returned slice is its own copy, it is safe to modify the contents
// of the returned slice.
// It is safe to modify the contents of the argument after Get returns.
func (tr *Transaction) Get(key []byte, ro *opt.ReadOptions) ([]byte, error) {
	tr.lk.RLock()
	defer tr.lk.RUnlock()
	if tr.closed {
		return nil, errTransactionDone
	}
	return tr.db.get(tr.mem.DB, tr.tables, key, tr.seq, ro)
}

// Has returns true if the DB does contains the given key.
//
// It is safe to modify the contents of the argument after Has returns.
func (tr *Transaction) Has(key []byte, ro *opt.ReadOptions) (bool, error) {
	tr.lk.RLock()
	defer tr.lk.RUnlock()
	if tr.closed {
		return false, errTransactionDone
	}
	return tr.db.has(tr.mem.DB, tr.tables, key, tr.seq, ro)
}

// NewIterator returns an iterator for the latest snapshot of the transaction.
// The returned iterator is not safe for concurrent use, but it is safe to use
// multiple iterators concurrently, with each in a dedicated goroutine.
// It is also safe to use an iterator concurrently while writes to the
// transaction. The resultant key/value pairs are guaranteed to be consistent.
//
// Slice allows slicing the iterator to only contains keys in the given
// range. A nil Range.Start is treated as a key before all keys in the
// DB. And a nil Range.Limit is treated as a key after all keys in
// the DB.
//
// The returned iterator has locks on its own resources, so it can live beyond
// the lifetime of the transaction who creates them.
//
// WARNING: Any slice returned by interator (e.g. slice returned by calling
// Iterator.Key() or Iterator.Key() methods), its content should not be modified
// unless noted otherwise.
//
// The iterator must be released after use, by calling Release method.
//
// Also read Iterator documentation of the leveldb/iterator package.
func (tr *Transaction) NewIterator(slice *util.Range, ro *opt.ReadOptions) iterator.Iterator {
	tr.lk.RLock()
	defer tr.lk.RUnlock()
	if tr.closed {
		return iterator.NewEmptyIterator(errTransactionDone)
	}
	tr.mem.incref()
	return tr.db.newIterator(tr.mem, tr.tables, tr.seq, slice, ro)
}

func (tr *Transaction) flush() error {
	// Flush memdb.
	if tr.mem.Len() != 0 {
		tr.stats.startTimer()
		iter := tr.mem.NewIterator(nil)
		t, n, err := tr.db.s.tops.createFrom(iter)
		iter.Release()
		tr.stats.stopTimer()
		if err != nil {
			return err
		}
		if tr.mem.getref() == 1 {
			tr.mem.Reset()
		} else {
			tr.mem.decref()
			tr.mem = tr.db.mpoolGet(0)
			tr.mem.incref()
		}
		tr.tables = append(tr.tables, t)
		tr.rec.addTableFile(0, t)
		tr.stats.write += t.size
		tr.db.logf("transaction@flush created L0@%d N·%d S·%s %q:%q", t.fd.Num, n, shortenb(t.size), t.imin, t.imax)
	}
	return nil
}

func (tr *Transaction) put(kt keyType, key, value []byte) error {
	tr.ikScratch = makeInternalKey(tr.ikScratch, key, tr.seq+1, kt)
	if tr.mem.Free() < len(tr.ikScratch)+len(value) {
		if err := tr.flush(); err != nil {
			return err
		}
	}
	if err := tr.mem.Put(tr.ikScratch, value); err != nil {
		return err
	}
	tr.seq++
	return nil
}

// Put sets the value for the given key. It overwrites any previous value
// for that key; a DB is not a multi-map.
// Please note that the transaction is not compacted until committed, so if you
// writes 10 same keys, then those 10 same keys are in the transaction.
//
// It is safe to modify the contents of the arguments after Put returns.
func (tr *Transaction) Put(key, value []byte, wo *opt.WriteOptions) error {
	tr.lk.Lock()
	defer tr.lk.Unlock()
	if tr.closed {
		return errTransactionDone
	}
	return tr.put(keyTypeVal, key, value)
}

// Delete deletes the value for the given key.
// Please note that the transaction is not compacted until committed, so if you
// writes 10 same keys, then those 10 same keys are in the transaction.
//
// It is safe to modify the contents of the arguments after Delete returns.
func (tr *Transaction) Delete(key []byte, wo *opt.WriteOptions) error {
	tr.lk.Lock()
	defer tr.lk.Unlock()
	if tr.closed {
		return errTransactionDone
	}
	return tr.put(keyTypeDel, key, nil)
}

// Write apply the given batch to the transaction. The batch will be applied
// sequentially.
// Please note that the transaction is not compacted until committed, so if you
// writes 10 same keys, then those 10 same keys are in the transaction.
//
// It is safe to modify the contents of the arguments after Write returns.
func (tr *Transaction) Write(b *Batch, wo *opt.WriteOptions) error {
	if b == nil || b.Len() == 0 {
		return nil
	}

	tr.lk.Lock()
	defer tr.lk.Unlock()
	if tr.closed {
		return errTransactionDone
	}
	return b.replayInternal(func(i int, kt keyType, k, v []byte) error {
		return tr.put(kt, k, v)
	})
}

func (tr *Transaction) setDone() {
	tr.closed = true
	tr.db.tr = nil
	tr.mem.decref()
	<-tr.db.writeLockC
}

// Commit commits the transaction. If error is not nil, then the transaction is
// not committed, it can then either be retried or discarded.
//
// Other methods should not be called after transaction has been committed.
func (tr *Transaction) Commit() error {
	if err := tr.db.ok(); err != nil {
		return err
	}

	tr.lk.Lock()
	defer tr.lk.Unlock()
	if tr.closed {
		return errTransactionDone
	}
	if err := tr.flush(); err != nil {
		// Return error, lets user decide either to retry or discard
		// transaction.
		return err
	}
	if len(tr.tables) != 0 {
		// Committing transaction.
		tr.rec.setSeqNum(tr.seq)
		tr.db.compCommitLk.Lock()
		tr.stats.startTimer()
		var cerr error
		for retry := 0; retry < 3; retry++ {
			cerr = tr.db.s.commit(&tr.rec, false)
			if cerr != nil {
				tr.db.logf("transaction@commit error R·%d %q", retry, cerr)
				select {
				case <-time.After(time.Second):
				case <-tr.db.closeC:
					tr.db.logf("transaction@commit exiting")
					tr.db.compCommitLk.Unlock()
					return cerr
				}
			} else {
				// Success. Set db.seq.
				tr.db.setSeq(tr.seq)
				break
			}
		}
		tr.stats.stopTimer()
		if cerr != nil {
			// Return error, lets user decide either to retry or discard
			// transaction.
			return cerr
		}

		// Update compaction stats. This is safe as long as we hold compCommitLk.
		tr.db.compStats.addStat(0, &tr.stats)

		// Trigger table auto-compaction.
		tr.db.compTrigger(tr.db.tcompCmdC)
		tr.db.compCommitLk.Unlock()

		// Additionally, wait compaction when certain threshold reached.
		// Ignore error, returns error only if transaction can't be committed.
		_ = tr.db.waitCompaction()
	}
	// Only mark as done if transaction committed successfully.
	tr.setDone()
	return nil
}

func (tr *Transaction) discard() {
	// Discard transaction.
	for _, t := range tr.tables {
		tr.db.logf("transaction@discard @%d", t.fd.Num)
		// Iterator may still use the table, so we use tOps.remove here.
		tr.db.s.tops.remove(t.fd)
	}
}

// Discard discards the transaction.
// This method is noop if transaction is already closed (either committed or
// discarded)
//
// Other methods should not be called after transaction has been discarded.
func (tr *Transaction) Discard() {
	tr.lk.Lock()
	if !tr.closed {
		tr.discard()
		tr.setDone()
	}
	tr.lk.Unlock()
}

func (db *DB) waitCompaction() error {
	if db.s.tLen(0) >= db.s.o.GetWriteL0PauseTrigger() {
		return db.compTriggerWait(db.tcompCmdC)
	}
	return nil
}

// OpenTransaction opens an atomic DB transaction. Only one transaction can be
// opened at a time. Subsequent call to Write and OpenTransaction will be blocked
// until in-flight transaction is committed or discarded.
// The returned transaction handle is safe for concurrent use.
//
// Transaction is very expensive and can overwhelm compaction, especially if
// transaction size is small. Use with caution.
// The rule of thumb is if you need to merge at least same amount of
// `Options.WriteBuffer` worth of data then use transaction, otherwise don't.
//
// The transaction must be closed once done, either by committing or discarding
// the transaction.
// Closing the DB will discard open transaction.
func (db *DB) OpenTransaction() (*Transaction, error) {
	if err := db.ok(); err != nil {
		return nil, err
	}

	// The write happen synchronously.
	select {
	case db.writeLockC <- struct{}{}:
	case err := <-db.compPerErrC:
		return nil, err
	case <-db.closeC:
		return nil, ErrClosed
	}

	if db.tr != nil {
		panic("leveldb: has open transaction")
	}

	// Flush current memdb.
	if db.mem != nil && db.mem.Len() != 0 {
		if _, err := db.rotateMem(0, true); err != nil {
			return nil, err
		}
	}

	// Wait compaction when certain threshold reached.
	if err := db.waitCompaction(); err != nil {
		return nil, err
	}

	tr := &Transaction{
		db:  db,
		seq: db.seq,
		mem: db.mpoolGet(0),
	}
	tr.mem.incref()
	db.tr = tr
	return tr, nil
}
```

## File: `leveldb/db_util.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/util"
)

// Reader is the interface that wraps basic Get and NewIterator methods.
// This interface implemented by both DB and Snapshot.
type Reader interface {
	Get(key []byte, ro *opt.ReadOptions) (value []byte, err error)
	NewIterator(slice *util.Range, ro *opt.ReadOptions) iterator.Iterator
}

// Sizes is list of size.
type Sizes []int64

// Sum returns sum of the sizes.
func (sizes Sizes) Sum() int64 {
	var sum int64
	for _, size := range sizes {
		sum += size
	}
	return sum
}

// Logging.
func (db *DB) log(v ...interface{})                 { db.s.log(v...) }
func (db *DB) logf(format string, v ...interface{}) { db.s.logf(format, v...) }

// Check and clean files.
func (db *DB) checkAndCleanFiles() error {
	v := db.s.version()
	defer v.release()

	tmap := make(map[int64]bool)
	for _, tables := range v.levels {
		for _, t := range tables {
			tmap[t.fd.Num] = false
		}
	}

	fds, err := db.s.stor.List(storage.TypeAll)
	if err != nil {
		return err
	}

	var nt int
	var rem []storage.FileDesc
	for _, fd := range fds {
		keep := true
		switch fd.Type {
		case storage.TypeManifest:
			keep = fd.Num >= db.s.manifestFd.Num
		case storage.TypeJournal:
			if !db.frozenJournalFd.Zero() {
				keep = fd.Num >= db.frozenJournalFd.Num
			} else {
				keep = fd.Num >= db.journalFd.Num
			}
		case storage.TypeTable:
			_, keep = tmap[fd.Num]
			if keep {
				tmap[fd.Num] = true
				nt++
			}
		}

		if !keep {
			rem = append(rem, fd)
		}
	}

	if nt != len(tmap) {
		var mfds []storage.FileDesc
		for num, present := range tmap {
			if !present {
				mfds = append(mfds, storage.FileDesc{Type: storage.TypeTable, Num: num})
				db.logf("db@janitor table missing @%d", num)
			}
		}
		return errors.NewErrCorrupted(storage.FileDesc{}, &errors.ErrMissingFiles{Fds: mfds})
	}

	db.logf("db@janitor F·%d G·%d", len(fds), len(rem))
	for _, fd := range rem {
		db.logf("db@janitor removing %s-%d", fd.Type, fd.Num)
		if err := db.s.stor.Remove(fd); err != nil {
			return err
		}
	}
	return nil
}
```

## File: `leveldb/db_write.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"sync/atomic"
	"time"

	"github.com/syndtr/goleveldb/leveldb/memdb"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/util"
)

func (db *DB) writeJournal(batches []*Batch, seq uint64, sync bool) error {
	wr, err := db.journal.Next()
	if err != nil {
		return err
	}
	if err := writeBatchesWithHeader(wr, batches, seq); err != nil {
		return err
	}
	if err := db.journal.Flush(); err != nil {
		return err
	}
	if sync {
		return db.journalWriter.Sync()
	}
	return nil
}

func (db *DB) rotateMem(n int, wait bool) (mem *memDB, err error) {
	retryLimit := 3
retry:
	// Wait for pending memdb compaction.
	err = db.compTriggerWait(db.mcompCmdC)
	if err != nil {
		return
	}
	retryLimit--

	// Create new memdb and journal.
	mem, err = db.newMem(n)
	if err != nil {
		if err == errHasFrozenMem {
			if retryLimit <= 0 {
				panic("BUG: still has frozen memdb")
			}
			goto retry
		}
		return
	}

	// Schedule memdb compaction.
	if wait {
		err = db.compTriggerWait(db.mcompCmdC)
	} else {
		db.compTrigger(db.mcompCmdC)
	}
	return
}

func (db *DB) flush(n int) (mdb *memDB, mdbFree int, err error) {
	delayed := false
	slowdownTrigger := db.s.o.GetWriteL0SlowdownTrigger()
	pauseTrigger := db.s.o.GetWriteL0PauseTrigger()
	flush := func() (retry bool) {
		mdb = db.getEffectiveMem()
		if mdb == nil {
			err = ErrClosed
			return false
		}
		defer func() {
			if retry {
				mdb.decref()
				mdb = nil
			}
		}()
		tLen := db.s.tLen(0)
		mdbFree = mdb.Free()
		switch {
		case tLen >= slowdownTrigger && !delayed:
			delayed = true
			time.Sleep(time.Millisecond)
		case mdbFree >= n:
			return false
		case tLen >= pauseTrigger:
			delayed = true
			// Set the write paused flag explicitly.
			atomic.StoreInt32(&db.inWritePaused, 1)
			err = db.compTriggerWait(db.tcompCmdC)
			// Unset the write paused flag.
			atomic.StoreInt32(&db.inWritePaused, 0)
			if err != nil {
				return false
			}
		default:
			// Allow memdb to grow if it has no entry.
			if mdb.Len() == 0 {
				mdbFree = n
			} else {
				mdb.decref()
				mdb, err = db.rotateMem(n, false)
				if err == nil {
					mdbFree = mdb.Free()
				} else {
					mdbFree = 0
				}
			}
			return false
		}
		return true
	}
	start := time.Now()
	for flush() {
	}
	if delayed {
		db.writeDelay += time.Since(start)
		db.writeDelayN++
	} else if db.writeDelayN > 0 {
		db.logf("db@write was delayed N·%d T·%v", db.writeDelayN, db.writeDelay)
		atomic.AddInt32(&db.cWriteDelayN, int32(db.writeDelayN))
		atomic.AddInt64(&db.cWriteDelay, int64(db.writeDelay))
		db.writeDelay = 0
		db.writeDelayN = 0
	}
	return
}

type writeMerge struct {
	sync       bool
	batch      *Batch
	keyType    keyType
	key, value []byte
}

func (db *DB) unlockWrite(overflow bool, merged int, err error) {
	for i := 0; i < merged; i++ {
		db.writeAckC <- err
	}
	if overflow {
		// Pass lock to the next write (that failed to merge).
		db.writeMergedC <- false
	} else {
		// Release lock.
		<-db.writeLockC
	}
}

// ourBatch is batch that we can modify.
func (db *DB) writeLocked(batch, ourBatch *Batch, merge, sync bool) error {
	// Try to flush memdb. This method would also trying to throttle writes
	// if it is too fast and compaction cannot catch-up.
	mdb, mdbFree, err := db.flush(batch.internalLen)
	if err != nil {
		db.unlockWrite(false, 0, err)
		return err
	}
	defer mdb.decref()

	var (
		overflow bool
		merged   int
		batches  = []*Batch{batch}
	)

	if merge {
		// Merge limit.
		var mergeLimit int
		if batch.internalLen > 128<<10 {
			mergeLimit = (1 << 20) - batch.internalLen
		} else {
			mergeLimit = 128 << 10
		}
		mergeCap := mdbFree - batch.internalLen
		if mergeLimit > mergeCap {
			mergeLimit = mergeCap
		}

	merge:
		for mergeLimit > 0 {
			select {
			case incoming := <-db.writeMergeC:
				if incoming.batch != nil {
					// Merge batch.
					if incoming.batch.internalLen > mergeLimit {
						overflow = true
						break merge
					}
					batches = append(batches, incoming.batch)
					mergeLimit -= incoming.batch.internalLen
				} else {
					// Merge put.
					internalLen := len(incoming.key) + len(incoming.value) + 8
					if internalLen > mergeLimit {
						overflow = true
						break merge
					}
					if ourBatch == nil {
						ourBatch = db.batchPool.Get().(*Batch)
						ourBatch.Reset()
						batches = append(batches, ourBatch)
					}
					// We can use same batch since concurrent write doesn't
					// guarantee write order.
					ourBatch.appendRec(incoming.keyType, incoming.key, incoming.value)
					mergeLimit -= internalLen
				}
				sync = sync || incoming.sync
				merged++
				db.writeMergedC <- true

			default:
				break merge
			}
		}
	}

	// Release ourBatch if any.
	if ourBatch != nil {
		defer db.batchPool.Put(ourBatch)
	}

	// Seq number.
	seq := db.seq + 1

	// Write journal.
	if err := db.writeJournal(batches, seq, sync); err != nil {
		db.unlockWrite(overflow, merged, err)
		return err
	}

	// Put batches.
	for _, batch := range batches {
		if err := batch.putMem(seq, mdb.DB); err != nil {
			panic(err)
		}
		seq += uint64(batch.Len())
	}

	// Incr seq number.
	db.addSeq(uint64(batchesLen(batches)))

	// Rotate memdb if it's reach the threshold.
	if batch.internalLen >= mdbFree {
		if _, err := db.rotateMem(0, false); err != nil {
			db.unlockWrite(overflow, merged, err)
			return err
		}
	}

	db.unlockWrite(overflow, merged, nil)
	return nil
}

// Write apply the given batch to the DB. The batch records will be applied
// sequentially. Write might be used concurrently, when used concurrently and
// batch is small enough, write will try to merge the batches. Set NoWriteMerge
// option to true to disable write merge.
//
// It is safe to modify the contents of the arguments after Write returns but
// not before. Write will not modify content of the batch.
func (db *DB) Write(batch *Batch, wo *opt.WriteOptions) error {
	if err := db.ok(); err != nil || batch == nil || batch.Len() == 0 {
		return err
	}

	// If the batch size is larger than write buffer, it may justified to write
	// using transaction instead. Using transaction the batch will be written
	// into tables directly, skipping the journaling.
	if batch.internalLen > db.s.o.GetWriteBuffer() && !db.s.o.GetDisableLargeBatchTransaction() {
		tr, err := db.OpenTransaction()
		if err != nil {
			return err
		}
		if err := tr.Write(batch, wo); err != nil {
			tr.Discard()
			return err
		}
		return tr.Commit()
	}

	merge := !wo.GetNoWriteMerge() && !db.s.o.GetNoWriteMerge()
	sync := wo.GetSync() && !db.s.o.GetNoSync()

	// Acquire write lock.
	if merge {
		select {
		case db.writeMergeC <- writeMerge{sync: sync, batch: batch}:
			if <-db.writeMergedC {
				// Write is merged.
				return <-db.writeAckC
			}
			// Write is not merged, the write lock is handed to us. Continue.
		case db.writeLockC <- struct{}{}:
			// Write lock acquired.
		case err := <-db.compPerErrC:
			// Compaction error.
			return err
		case <-db.closeC:
			// Closed
			return ErrClosed
		}
	} else {
		select {
		case db.writeLockC <- struct{}{}:
			// Write lock acquired.
		case err := <-db.compPerErrC:
			// Compaction error.
			return err
		case <-db.closeC:
			// Closed
			return ErrClosed
		}
	}

	return db.writeLocked(batch, nil, merge, sync)
}

func (db *DB) putRec(kt keyType, key, value []byte, wo *opt.WriteOptions) error {
	if err := db.ok(); err != nil {
		return err
	}

	merge := !wo.GetNoWriteMerge() && !db.s.o.GetNoWriteMerge()
	sync := wo.GetSync() && !db.s.o.GetNoSync()

	// Acquire write lock.
	if merge {
		select {
		case db.writeMergeC <- writeMerge{sync: sync, keyType: kt, key: key, value: value}:
			if <-db.writeMergedC {
				// Write is merged.
				return <-db.writeAckC
			}
			// Write is not merged, the write lock is handed to us. Continue.
		case db.writeLockC <- struct{}{}:
			// Write lock acquired.
		case err := <-db.compPerErrC:
			// Compaction error.
			return err
		case <-db.closeC:
			// Closed
			return ErrClosed
		}
	} else {
		select {
		case db.writeLockC <- struct{}{}:
			// Write lock acquired.
		case err := <-db.compPerErrC:
			// Compaction error.
			return err
		case <-db.closeC:
			// Closed
			return ErrClosed
		}
	}

	batch := db.batchPool.Get().(*Batch)
	batch.Reset()
	batch.appendRec(kt, key, value)
	return db.writeLocked(batch, batch, merge, sync)
}

// Put sets the value for the given key. It overwrites any previous value
// for that key; a DB is not a multi-map. Write merge also applies for Put, see
// Write.
//
// It is safe to modify the contents of the arguments after Put returns but not
// before.
func (db *DB) Put(key, value []byte, wo *opt.WriteOptions) error {
	return db.putRec(keyTypeVal, key, value, wo)
}

// Delete deletes the value for the given key. Delete will not returns error if
// key doesn't exist. Write merge also applies for Delete, see Write.
//
// It is safe to modify the contents of the arguments after Delete returns but
// not before.
func (db *DB) Delete(key []byte, wo *opt.WriteOptions) error {
	return db.putRec(keyTypeDel, key, nil, wo)
}

func isMemOverlaps(icmp *iComparer, mem *memdb.DB, min, max []byte) bool {
	iter := mem.NewIterator(nil)
	defer iter.Release()
	return (max == nil || (iter.First() && icmp.uCompare(max, internalKey(iter.Key()).ukey()) >= 0)) &&
		(min == nil || (iter.Last() && icmp.uCompare(min, internalKey(iter.Key()).ukey()) <= 0))
}

// CompactRange compacts the underlying DB for the given key range.
// In particular, deleted and overwritten versions are discarded,
// and the data is rearranged to reduce the cost of operations
// needed to access the data. This operation should typically only
// be invoked by users who understand the underlying implementation.
//
// A nil Range.Start is treated as a key before all keys in the DB.
// And a nil Range.Limit is treated as a key after all keys in the DB.
// Therefore if both is nil then it will compact entire DB.
func (db *DB) CompactRange(r util.Range) error {
	if err := db.ok(); err != nil {
		return err
	}

	// Lock writer.
	select {
	case db.writeLockC <- struct{}{}:
	case err := <-db.compPerErrC:
		return err
	case <-db.closeC:
		return ErrClosed
	}

	// Check for overlaps in memdb.
	mdb := db.getEffectiveMem()
	if mdb == nil {
		return ErrClosed
	}
	defer mdb.decref()
	if isMemOverlaps(db.s.icmp, mdb.DB, r.Start, r.Limit) {
		// Memdb compaction.
		if _, err := db.rotateMem(0, false); err != nil {
			<-db.writeLockC
			return err
		}
		<-db.writeLockC
		if err := db.compTriggerWait(db.mcompCmdC); err != nil {
			return err
		}
	} else {
		<-db.writeLockC
	}

	// Table compaction.
	return db.compTriggerRange(db.tcompCmdC, -1, r.Start, r.Limit)
}

// SetReadOnly makes DB read-only. It will stay read-only until reopened.
func (db *DB) SetReadOnly() error {
	if err := db.ok(); err != nil {
		return err
	}

	// Lock writer.
	select {
	case db.writeLockC <- struct{}{}:
		db.compWriteLocking = true
	case err := <-db.compPerErrC:
		return err
	case <-db.closeC:
		return ErrClosed
	}

	// Set compaction read-only.
	select {
	case db.compErrSetC <- ErrReadOnly:
	case perr := <-db.compPerErrC:
		return perr
	case <-db.closeC:
		return ErrClosed
	}

	return nil
}
```

## File: `leveldb/doc.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package leveldb provides implementation of LevelDB key/value database.
//
// Create or open a database:
//
//	// The returned DB instance is safe for concurrent use. Which mean that all
//	// DB's methods may be called concurrently from multiple goroutine.
//	db, err := leveldb.OpenFile("path/to/db", nil)
//	...
//	defer db.Close()
//	...
//
// Read or modify the database content:
//
//	// Remember that the contents of the returned slice should not be modified.
//	data, err := db.Get([]byte("key"), nil)
//	...
//	err = db.Put([]byte("key"), []byte("value"), nil)
//	...
//	err = db.Delete([]byte("key"), nil)
//	...
//
// Iterate over database content:
//
//	iter := db.NewIterator(nil, nil)
//	for iter.Next() {
//		// Remember that the contents of the returned slice should not be modified, and
//		// only valid until the next call to Next.
//		key := iter.Key()
//		value := iter.Value()
//		...
//	}
//	iter.Release()
//	err = iter.Error()
//	...
//
// Iterate over subset of database content with a particular prefix:
//	iter := db.NewIterator(util.BytesPrefix([]byte("foo-")), nil)
//	for iter.Next() {
//		// Use key/value.
//		...
//	}
//	iter.Release()
//	err = iter.Error()
//	...
//
// Seek-then-Iterate:
//
// 	iter := db.NewIterator(nil, nil)
// 	for ok := iter.Seek(key); ok; ok = iter.Next() {
// 		// Use key/value.
// 		...
// 	}
// 	iter.Release()
// 	err = iter.Error()
// 	...
//
// Iterate over subset of database content:
//
// 	iter := db.NewIterator(&util.Range{Start: []byte("foo"), Limit: []byte("xoo")}, nil)
// 	for iter.Next() {
// 		// Use key/value.
// 		...
// 	}
// 	iter.Release()
// 	err = iter.Error()
// 	...
//
// Batch writes:
//
//	batch := new(leveldb.Batch)
//	batch.Put([]byte("foo"), []byte("value"))
//	batch.Put([]byte("bar"), []byte("another value"))
//	batch.Delete([]byte("baz"))
//	err = db.Write(batch, nil)
//	...
//
// Use bloom filter:
//
//	o := &opt.Options{
//		Filter: filter.NewBloomFilter(10),
//	}
//	db, err := leveldb.OpenFile("path/to/db", o)
//	...
//	defer db.Close()
//	...
package leveldb
```

## File: `leveldb/errors.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"github.com/syndtr/goleveldb/leveldb/errors"
)

// Common errors.
var (
	ErrNotFound         = errors.ErrNotFound
	ErrReadOnly         = errors.New("leveldb: read-only mode")
	ErrSnapshotReleased = errors.New("leveldb: snapshot released")
	ErrIterReleased     = errors.New("leveldb: iterator released")
	ErrClosed           = errors.New("leveldb: closed")
)
```

## File: `leveldb/external_test.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/testutil"
)

var _ = testutil.Defer(func() {
	Describe("Leveldb external", func() {
		o := &opt.Options{
			DisableBlockCache:      true,
			BlockRestartInterval:   5,
			BlockSize:              80,
			Compression:            opt.NoCompression,
			OpenFilesCacheCapacity: -1,
			Strict:                 opt.StrictAll,
			WriteBuffer:            1000,
			CompactionTableSize:    2000,
		}

		Describe("write test", func() {
			It("should do write correctly", func(done Done) {
				db := newTestingDB(o, nil, nil)
				t := testutil.DBTesting{
					DB:      db,
					Deleted: testutil.KeyValue_Generate(nil, 500, 1, 1, 50, 5, 5).Clone(),
				}
				testutil.DoDBTesting(&t)
				db.TestClose()
				done <- true
			}, 80.0)
		})

		Describe("read test", func() {
			testutil.AllKeyValueTesting(nil, nil, func(kv testutil.KeyValue) testutil.DB {
				// Building the DB.
				db := newTestingDB(o, nil, nil)
				kv.IterateShuffled(nil, func(i int, key, value []byte) {
					err := db.TestPut(key, value)
					Expect(err).NotTo(HaveOccurred())
				})

				return db
			}, func(db testutil.DB) {
				db.(*testingDB).TestClose()
			})
		})

		Describe("transaction test", func() {
			It("should do transaction correctly", func(done Done) {
				db := newTestingDB(o, nil, nil)

				By("creating first transaction")
				var err error
				tr := &testingTransaction{}
				tr.Transaction, err = db.OpenTransaction()
				Expect(err).NotTo(HaveOccurred())
				t0 := &testutil.DBTesting{
					DB:      tr,
					Deleted: testutil.KeyValue_Generate(nil, 200, 1, 1, 50, 5, 5).Clone(),
				}
				testutil.DoDBTesting(t0)
				testutil.TestGet(tr, t0.Present)
				testutil.TestHas(tr, t0.Present)

				By("committing first transaction")
				err = tr.Commit()
				Expect(err).NotTo(HaveOccurred())
				testutil.TestIter(db, nil, t0.Present)
				testutil.TestGet(db, t0.Present)
				testutil.TestHas(db, t0.Present)

				By("manipulating DB without transaction")
				t0.DB = db
				testutil.DoDBTesting(t0)

				By("creating second transaction")
				tr.Transaction, err = db.OpenTransaction()
				Expect(err).NotTo(HaveOccurred())
				t1 := &testutil.DBTesting{
					DB:      tr,
					Deleted: t0.Deleted.Clone(),
					Present: t0.Present.Clone(),
				}
				testutil.DoDBTesting(t1)
				testutil.TestIter(db, nil, t0.Present)

				By("discarding second transaction")
				tr.Discard()
				testutil.TestIter(db, nil, t0.Present)

				By("creating third transaction")
				tr.Transaction, err = db.OpenTransaction()
				Expect(err).NotTo(HaveOccurred())
				t0.DB = tr
				testutil.DoDBTesting(t0)

				By("committing third transaction")
				err = tr.Commit()
				Expect(err).NotTo(HaveOccurred())
				testutil.TestIter(db, nil, t0.Present)

				db.TestClose()
				done <- true
			}, 240.0)
		})
	})
})
```

## File: `leveldb/filter.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"github.com/syndtr/goleveldb/leveldb/filter"
)

type iFilter struct {
	filter.Filter
}

func (f iFilter) Contains(filter, key []byte) bool {
	return f.Filter.Contains(filter, internalKey(key).ukey())
}

func (f iFilter) NewGenerator() filter.FilterGenerator {
	return iFilterGenerator{f.Filter.NewGenerator()}
}

type iFilterGenerator struct {
	filter.FilterGenerator
}

func (g iFilterGenerator) Add(key []byte) {
	g.FilterGenerator.Add(internalKey(key).ukey())
}
```

## File: `leveldb/key.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"encoding/binary"
	"fmt"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

// ErrInternalKeyCorrupted records internal key corruption.
type ErrInternalKeyCorrupted struct {
	Ikey   []byte
	Reason string
}

func (e *ErrInternalKeyCorrupted) Error() string {
	return fmt.Sprintf("leveldb: internal key %q corrupted: %s", e.Ikey, e.Reason)
}

func newErrInternalKeyCorrupted(ikey []byte, reason string) error {
	return errors.NewErrCorrupted(storage.FileDesc{}, &ErrInternalKeyCorrupted{append([]byte(nil), ikey...), reason})
}

type keyType uint

func (kt keyType) String() string {
	switch kt {
	case keyTypeDel:
		return "d"
	case keyTypeVal:
		return "v"
	}
	return fmt.Sprintf("<invalid:%#x>", uint(kt))
}

// Value types encoded as the last component of internal keys.
// Don't modify; this value are saved to disk.
const (
	keyTypeDel = keyType(0)
	keyTypeVal = keyType(1)
)

// keyTypeSeek defines the keyType that should be passed when constructing an
// internal key for seeking to a particular sequence number (since we
// sort sequence numbers in decreasing order and the value type is
// embedded as the low 8 bits in the sequence number in internal keys,
// we need to use the highest-numbered ValueType, not the lowest).
const keyTypeSeek = keyTypeVal

const (
	// Maximum value possible for sequence number; the 8-bits are
	// used by value type, so its can packed together in single
	// 64-bit integer.
	keyMaxSeq = (uint64(1) << 56) - 1
	// Maximum value possible for packed sequence number and type.
	keyMaxNum = (keyMaxSeq << 8) | uint64(keyTypeSeek)
)

// Maximum number encoded in bytes.
var keyMaxNumBytes = make([]byte, 8)

func init() {
	binary.LittleEndian.PutUint64(keyMaxNumBytes, keyMaxNum)
}

type internalKey []byte

func makeInternalKey(dst, ukey []byte, seq uint64, kt keyType) internalKey {
	if seq > keyMaxSeq {
		panic("leveldb: invalid sequence number")
	} else if kt > keyTypeVal {
		panic("leveldb: invalid type")
	}

	dst = ensureBuffer(dst, len(ukey)+8)
	copy(dst, ukey)
	binary.LittleEndian.PutUint64(dst[len(ukey):], (seq<<8)|uint64(kt))
	return internalKey(dst)
}

func parseInternalKey(ik []byte) (ukey []byte, seq uint64, kt keyType, err error) {
	if len(ik) < 8 {
		return nil, 0, 0, newErrInternalKeyCorrupted(ik, "invalid length")
	}
	num := binary.LittleEndian.Uint64(ik[len(ik)-8:])
	seq, kt = num>>8, keyType(num&0xff)
	if kt > keyTypeVal {
		return nil, 0, 0, newErrInternalKeyCorrupted(ik, "invalid type")
	}
	ukey = ik[:len(ik)-8]
	return
}

func validInternalKey(ik []byte) bool {
	_, _, _, err := parseInternalKey(ik)
	return err == nil
}

func (ik internalKey) assert() {
	if ik == nil {
		panic("leveldb: nil internalKey")
	}
	if len(ik) < 8 {
		panic(fmt.Sprintf("leveldb: internal key %q, len=%d: invalid length", []byte(ik), len(ik)))
	}
}

func (ik internalKey) ukey() []byte {
	ik.assert()
	return ik[:len(ik)-8]
}

func (ik internalKey) num() uint64 {
	ik.assert()
	return binary.LittleEndian.Uint64(ik[len(ik)-8:])
}

func (ik internalKey) parseNum() (seq uint64, kt keyType) {
	num := ik.num()
	seq, kt = num>>8, keyType(num&0xff)
	if kt > keyTypeVal {
		panic(fmt.Sprintf("leveldb: internal key %q, len=%d: invalid type %#x", []byte(ik), len(ik), kt))
	}
	return
}

func (ik internalKey) String() string {
	if ik == nil {
		return "<nil>"
	}

	if ukey, seq, kt, err := parseInternalKey(ik); err == nil {
		return fmt.Sprintf("%s,%s%d", shorten(string(ukey)), kt, seq)
	}
	return fmt.Sprintf("<invalid:%#x>", []byte(ik))
}
```

## File: `leveldb/key_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"bytes"
	"testing"

	"github.com/syndtr/goleveldb/leveldb/comparer"
)

var defaultIComparer = &iComparer{comparer.DefaultComparer}

func ikey(key string, seq uint64, kt keyType) internalKey {
	return makeInternalKey(nil, []byte(key), seq, kt)
}

func shortSep(a, b []byte) []byte {
	dst := make([]byte, len(a))
	dst = defaultIComparer.Separator(dst[:0], a, b)
	if dst == nil {
		return a
	}
	return dst
}

func shortSuccessor(b []byte) []byte {
	dst := make([]byte, len(b))
	dst = defaultIComparer.Successor(dst[:0], b)
	if dst == nil {
		return b
	}
	return dst
}

func testSingleKey(t *testing.T, key string, seq uint64, kt keyType) {
	ik := ikey(key, seq, kt)

	if !bytes.Equal(ik.ukey(), []byte(key)) {
		t.Errorf("user key does not equal, got %v, want %v", string(ik.ukey()), key)
	}

	rseq, rt := ik.parseNum()
	if rseq != seq {
		t.Errorf("seq number does not equal, got %v, want %v", rseq, seq)
	}
	if rt != kt {
		t.Errorf("type does not equal, got %v, want %v", rt, kt)
	}

	if rukey, rseq, rt, kerr := parseInternalKey(ik); kerr == nil {
		if !bytes.Equal(rukey, []byte(key)) {
			t.Errorf("user key does not equal, got %v, want %v", string(ik.ukey()), key)
		}
		if rseq != seq {
			t.Errorf("seq number does not equal, got %v, want %v", rseq, seq)
		}
		if rt != kt {
			t.Errorf("type does not equal, got %v, want %v", rt, kt)
		}
	} else {
		t.Errorf("key error: %v", kerr)
	}
}

func TestInternalKey_EncodeDecode(t *testing.T) {
	keys := []string{"", "k", "hello", "longggggggggggggggggggggg"}
	seqs := []uint64{
		1, 2, 3,
		(1 << 8) - 1, 1 << 8, (1 << 8) + 1,
		(1 << 16) - 1, 1 << 16, (1 << 16) + 1,
		(1 << 32) - 1, 1 << 32, (1 << 32) + 1,
	}
	for _, key := range keys {
		for _, seq := range seqs {
			testSingleKey(t, key, seq, keyTypeVal)
			testSingleKey(t, "hello", 1, keyTypeDel)
		}
	}
}

func assertBytes(t *testing.T, want, got []byte) {
	if !bytes.Equal(got, want) {
		t.Errorf("assert failed, got %v, want %v", got, want)
	}
}

func TestInternalKeyShortSeparator(t *testing.T) {
	// When user keys are same
	assertBytes(t, ikey("foo", 100, keyTypeVal),
		shortSep(ikey("foo", 100, keyTypeVal),
			ikey("foo", 99, keyTypeVal)))
	assertBytes(t, ikey("foo", 100, keyTypeVal),
		shortSep(ikey("foo", 100, keyTypeVal),
			ikey("foo", 101, keyTypeVal)))
	assertBytes(t, ikey("foo", 100, keyTypeVal),
		shortSep(ikey("foo", 100, keyTypeVal),
			ikey("foo", 100, keyTypeVal)))
	assertBytes(t, ikey("foo", 100, keyTypeVal),
		shortSep(ikey("foo", 100, keyTypeVal),
			ikey("foo", 100, keyTypeDel)))

	// When user keys are misordered
	assertBytes(t, ikey("foo", 100, keyTypeVal),
		shortSep(ikey("foo", 100, keyTypeVal),
			ikey("bar", 99, keyTypeVal)))

	// When user keys are different, but correctly ordered
	assertBytes(t, ikey("g", keyMaxSeq, keyTypeSeek),
		shortSep(ikey("foo", 100, keyTypeVal),
			ikey("hello", 200, keyTypeVal)))

	// When start user key is prefix of limit user key
	assertBytes(t, ikey("foo", 100, keyTypeVal),
		shortSep(ikey("foo", 100, keyTypeVal),
			ikey("foobar", 200, keyTypeVal)))

	// When limit user key is prefix of start user key
	assertBytes(t, ikey("foobar", 100, keyTypeVal),
		shortSep(ikey("foobar", 100, keyTypeVal),
			ikey("foo", 200, keyTypeVal)))
}

func TestInternalKeyShortestSuccessor(t *testing.T) {
	assertBytes(t, ikey("g", keyMaxSeq, keyTypeSeek),
		shortSuccessor(ikey("foo", 100, keyTypeVal)))
	assertBytes(t, ikey("\xff\xff", 100, keyTypeVal),
		shortSuccessor(ikey("\xff\xff", 100, keyTypeVal)))
}
```

## File: `leveldb/leveldb_suite_test.go`
```go
package leveldb

import (
	"testing"

	"github.com/syndtr/goleveldb/leveldb/testutil"
)

func TestLevelDB(t *testing.T) {
	testutil.RunSuite(t, "LevelDB Suite")
}
```

## File: `leveldb/options.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"github.com/syndtr/goleveldb/leveldb/filter"
	"github.com/syndtr/goleveldb/leveldb/opt"
)

func dupOptions(o *opt.Options) *opt.Options {
	newo := &opt.Options{}
	if o != nil {
		*newo = *o
	}
	if newo.Strict == 0 {
		newo.Strict = opt.DefaultStrict
	}
	return newo
}

func (s *session) setOptions(o *opt.Options) {
	no := dupOptions(o)
	// Alternative filters.
	if filters := o.GetAltFilters(); len(filters) > 0 {
		no.AltFilters = make([]filter.Filter, len(filters))
		for i, filter := range filters {
			no.AltFilters[i] = &iFilter{filter}
		}
	}
	// Comparer.
	s.icmp = &iComparer{o.GetComparer()}
	no.Comparer = s.icmp
	// Filter.
	if filter := o.GetFilter(); filter != nil {
		no.Filter = &iFilter{filter}
	}

	s.o = &cachedOptions{Options: no}
	s.o.cache()
}

const optCachedLevel = 7

type cachedOptions struct {
	*opt.Options

	compactionExpandLimit []int
	compactionGPOverlaps  []int
	compactionSourceLimit []int
	compactionTableSize   []int
	compactionTotalSize   []int64
}

func (co *cachedOptions) cache() {
	co.compactionExpandLimit = make([]int, optCachedLevel)
	co.compactionGPOverlaps = make([]int, optCachedLevel)
	co.compactionSourceLimit = make([]int, optCachedLevel)
	co.compactionTableSize = make([]int, optCachedLevel)
	co.compactionTotalSize = make([]int64, optCachedLevel)

	for level := 0; level < optCachedLevel; level++ {
		co.compactionExpandLimit[level] = co.Options.GetCompactionExpandLimit(level)
		co.compactionGPOverlaps[level] = co.Options.GetCompactionGPOverlaps(level)
		co.compactionSourceLimit[level] = co.Options.GetCompactionSourceLimit(level)
		co.compactionTableSize[level] = co.Options.GetCompactionTableSize(level)
		co.compactionTotalSize[level] = co.Options.GetCompactionTotalSize(level)
	}
}

func (co *cachedOptions) GetCompactionExpandLimit(level int) int {
	if level < optCachedLevel {
		return co.compactionExpandLimit[level]
	}
	return co.Options.GetCompactionExpandLimit(level)
}

func (co *cachedOptions) GetCompactionGPOverlaps(level int) int {
	if level < optCachedLevel {
		return co.compactionGPOverlaps[level]
	}
	return co.Options.GetCompactionGPOverlaps(level)
}

func (co *cachedOptions) GetCompactionSourceLimit(level int) int {
	if level < optCachedLevel {
		return co.compactionSourceLimit[level]
	}
	return co.Options.GetCompactionSourceLimit(level)
}

func (co *cachedOptions) GetCompactionTableSize(level int) int {
	if level < optCachedLevel {
		return co.compactionTableSize[level]
	}
	return co.Options.GetCompactionTableSize(level)
}

func (co *cachedOptions) GetCompactionTotalSize(level int) int64 {
	if level < optCachedLevel {
		return co.compactionTotalSize[level]
	}
	return co.Options.GetCompactionTotalSize(level)
}
```

## File: `leveldb/session.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"fmt"
	"io"
	"os"
	"sync"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/journal"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

// ErrManifestCorrupted records manifest corruption. This error will be
// wrapped with errors.ErrCorrupted.
type ErrManifestCorrupted struct {
	Field  string
	Reason string
}

func (e *ErrManifestCorrupted) Error() string {
	return fmt.Sprintf("leveldb: manifest corrupted (field '%s'): %s", e.Field, e.Reason)
}

func newErrManifestCorrupted(fd storage.FileDesc, field, reason string) error {
	return errors.NewErrCorrupted(fd, &ErrManifestCorrupted{field, reason})
}

// session represent a persistent database session.
type session struct {
	// Need 64-bit alignment.
	stNextFileNum    int64 // current unused file number
	stJournalNum     int64 // current journal file number; need external synchronization
	stPrevJournalNum int64 // prev journal file number; no longer used; for compatibility with older version of leveldb
	stTempFileNum    int64
	stSeqNum         uint64 // last mem compacted seq; need external synchronization

	stor     *iStorage
	storLock storage.Locker
	o        *cachedOptions
	icmp     *iComparer
	tops     *tOps

	manifest       *journal.Writer
	manifestWriter storage.Writer
	manifestFd     storage.FileDesc

	stCompPtrs  []internalKey // compaction pointers; need external synchronization
	stVersion   *version      // current version
	ntVersionID int64         // next version id to assign
	refCh       chan *vTask
	relCh       chan *vTask
	deltaCh     chan *vDelta
	abandon     chan int64
	closeC      chan struct{}
	closeW      sync.WaitGroup
	vmu         sync.Mutex

	// Testing fields
	fileRefCh chan chan map[int64]int // channel used to pass current reference stat
}

// Creates new initialized session instance.
func newSession(stor storage.Storage, o *opt.Options) (s *session, err error) {
	if stor == nil {
		return nil, os.ErrInvalid
	}
	storLock, err := stor.Lock()
	if err != nil {
		return
	}
	s = &session{
		stor:      newIStorage(stor),
		storLock:  storLock,
		refCh:     make(chan *vTask),
		relCh:     make(chan *vTask),
		deltaCh:   make(chan *vDelta),
		abandon:   make(chan int64),
		fileRefCh: make(chan chan map[int64]int),
		closeC:    make(chan struct{}),
	}
	s.setOptions(o)
	s.tops = newTableOps(s)

	s.closeW.Add(1)
	go s.refLoop()
	s.setVersion(nil, newVersion(s))
	s.log("log@legend F·NumFile S·FileSize N·Entry C·BadEntry B·BadBlock Ke·KeyError D·DroppedEntry L·Level Q·SeqNum T·TimeElapsed")
	return
}

// Close session.
func (s *session) close() {
	s.tops.close()
	if s.manifest != nil {
		s.manifest.Close()
	}
	if s.manifestWriter != nil {
		s.manifestWriter.Close()
	}
	s.manifest = nil
	s.manifestWriter = nil
	s.setVersion(nil, &version{s: s, closing: true, id: s.ntVersionID})

	// Close all background goroutines
	close(s.closeC)
	s.closeW.Wait()
}

// Release session lock.
func (s *session) release() {
	s.storLock.Unlock()
}

// Create a new database session; need external synchronization.
func (s *session) create() error {
	// create manifest
	return s.newManifest(nil, nil)
}

// Recover a database session; need external synchronization.
func (s *session) recover() (err error) {
	defer func() {
		if os.IsNotExist(err) {
			// Don't return os.ErrNotExist if the underlying storage contains
			// other files that belong to LevelDB. So the DB won't get trashed.
			if fds, _ := s.stor.List(storage.TypeAll); len(fds) > 0 {
				err = &errors.ErrCorrupted{Err: errors.New("database entry point either missing or corrupted")}
			}
		}
	}()

	fd, err := s.stor.GetMeta()
	if err != nil {
		return
	}

	reader, err := s.stor.Open(fd)
	if err != nil {
		return
	}
	defer reader.Close()

	var (
		// Options.
		strict = s.o.GetStrict(opt.StrictManifest)

		jr      = journal.NewReader(reader, dropper{s, fd}, strict, true)
		rec     = &sessionRecord{}
		staging = s.stVersion.newStaging()
	)
	for {
		var r io.Reader
		r, err = jr.Next()
		if err != nil {
			if err == io.EOF {
				err = nil
				break
			}
			return errors.SetFd(err, fd)
		}

		err = rec.decode(r)
		if err == nil {
			// save compact pointers
			for _, r := range rec.compPtrs {
				s.setCompPtr(r.level, r.ikey)
			}
			// commit record to version staging
			staging.commit(rec)
		} else {
			err = errors.SetFd(err, fd)
			if strict || !errors.IsCorrupted(err) {
				return
			}
			s.logf("manifest error: %v (skipped)", errors.SetFd(err, fd))
		}
		rec.resetCompPtrs()
		rec.resetAddedTables()
		rec.resetDeletedTables()
	}

	switch {
	case !rec.has(recComparer):
		return newErrManifestCorrupted(fd, "comparer", "missing")
	case rec.comparer != s.icmp.uName():
		return newErrManifestCorrupted(fd, "comparer", fmt.Sprintf("mismatch: want '%s', got '%s'", s.icmp.uName(), rec.comparer))
	case !rec.has(recNextFileNum):
		return newErrManifestCorrupted(fd, "next-file-num", "missing")
	case !rec.has(recJournalNum):
		return newErrManifestCorrupted(fd, "journal-file-num", "missing")
	case !rec.has(recSeqNum):
		return newErrManifestCorrupted(fd, "seq-num", "missing")
	}

	s.manifestFd = fd
	s.setVersion(rec, staging.finish(false))
	s.setNextFileNum(rec.nextFileNum)
	s.recordCommited(rec)
	return nil
}

// Commit session; need external synchronization.
func (s *session) commit(r *sessionRecord, trivial bool) (err error) {
	v := s.version()
	defer v.release()

	// spawn new version based on current version
	nv := v.spawn(r, trivial)

	// abandon useless version id to prevent blocking version processing loop.
	defer func() {
		if err != nil {
			s.abandon <- nv.id
			s.logf("commit@abandon useless vid D%d", nv.id)
		}
	}()

	if s.manifest == nil {
		// manifest journal writer not yet created, create one
		err = s.newManifest(r, nv)
	} else if s.manifest.Size() >= s.o.GetMaxManifestFileSize() {
		// pass nil sessionRecord to avoid over-reference table file
		err = s.newManifest(nil, nv)
	} else {
		err = s.flushManifest(r)
	}

	// finally, apply new version if no error rise
	if err == nil {
		s.setVersion(r, nv)
	}

	return
}
```

## File: `leveldb/session_compaction.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"sort"
	"sync/atomic"

	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/memdb"
	"github.com/syndtr/goleveldb/leveldb/opt"
)

const (
	undefinedCompaction = iota
	level0Compaction
	nonLevel0Compaction
	seekCompaction
)

func (s *session) pickMemdbLevel(umin, umax []byte, maxLevel int) int {
	v := s.version()
	defer v.release()
	return v.pickMemdbLevel(umin, umax, maxLevel)
}

func (s *session) flushMemdb(rec *sessionRecord, mdb *memdb.DB, maxLevel int) (int, error) {
	// Create sorted table.
	iter := mdb.NewIterator(nil)
	defer iter.Release()
	t, n, err := s.tops.createFrom(iter)
	if err != nil {
		return 0, err
	}

	// Pick level other than zero can cause compaction issue with large
	// bulk insert and delete on strictly incrementing key-space. The
	// problem is that the small deletion markers trapped at lower level,
	// while key/value entries keep growing at higher level. Since the
	// key-space is strictly incrementing it will not overlaps with
	// higher level, thus maximum possible level is always picked, while
	// overlapping deletion marker pushed into lower level.
	// See: https://github.com/syndtr/goleveldb/issues/127.
	flushLevel := s.pickMemdbLevel(t.imin.ukey(), t.imax.ukey(), maxLevel)
	rec.addTableFile(flushLevel, t)

	s.logf("memdb@flush created L%d@%d N·%d S·%s %q:%q", flushLevel, t.fd.Num, n, shortenb(t.size), t.imin, t.imax)
	return flushLevel, nil
}

// Pick a compaction based on current state; need external synchronization.
func (s *session) pickCompaction() *compaction {
	v := s.version()

	var sourceLevel int
	var t0 tFiles
	var typ int
	if v.cScore >= 1 {
		sourceLevel = v.cLevel
		cptr := s.getCompPtr(sourceLevel)
		tables := v.levels[sourceLevel]
		if cptr != nil && sourceLevel > 0 {
			n := len(tables)
			if i := sort.Search(n, func(i int) bool {
				return s.icmp.Compare(tables[i].imax, cptr) > 0
			}); i < n {
				t0 = append(t0, tables[i])
			}
		}
		if len(t0) == 0 {
			t0 = append(t0, tables[0])
		}
		if sourceLevel == 0 {
			typ = level0Compaction
		} else {
			typ = nonLevel0Compaction
		}
	} else {
		if p := atomic.LoadPointer(&v.cSeek); p != nil {
			ts := (*tSet)(p)
			sourceLevel = ts.level
			t0 = append(t0, ts.table)
			typ = seekCompaction
		} else {
			v.release()
			return nil
		}
	}

	return newCompaction(s, v, sourceLevel, t0, typ)
}

// Create compaction from given level and range; need external synchronization.
func (s *session) getCompactionRange(sourceLevel int, umin, umax []byte, noLimit bool) *compaction {
	v := s.version()

	if sourceLevel >= len(v.levels) {
		v.release()
		return nil
	}

	t0 := v.levels[sourceLevel].getOverlaps(nil, s.icmp, umin, umax, sourceLevel == 0)
	if len(t0) == 0 {
		v.release()
		return nil
	}

	// Avoid compacting too much in one shot in case the range is large.
	// But we cannot do this for level-0 since level-0 files can overlap
	// and we must not pick one file and drop another older file if the
	// two files overlap.
	if !noLimit && sourceLevel > 0 {
		limit := int64(v.s.o.GetCompactionSourceLimit(sourceLevel))
		total := int64(0)
		for i, t := range t0 {
			total += t.size
			if total >= limit {
				s.logf("table@compaction limiting F·%d -> F·%d", len(t0), i+1)
				t0 = t0[:i+1]
				break
			}
		}
	}

	typ := level0Compaction
	if sourceLevel != 0 {
		typ = nonLevel0Compaction
	}
	return newCompaction(s, v, sourceLevel, t0, typ)
}

func newCompaction(s *session, v *version, sourceLevel int, t0 tFiles, typ int) *compaction {
	c := &compaction{
		s:             s,
		v:             v,
		typ:           typ,
		sourceLevel:   sourceLevel,
		levels:        [2]tFiles{t0, nil},
		maxGPOverlaps: int64(s.o.GetCompactionGPOverlaps(sourceLevel)),
		tPtrs:         make([]int, len(v.levels)),
	}
	c.expand()
	c.save()
	return c
}

// compaction represent a compaction state.
type compaction struct {
	s *session
	v *version

	typ           int
	sourceLevel   int
	levels        [2]tFiles
	maxGPOverlaps int64

	gp                tFiles
	gpi               int
	seenKey           bool
	gpOverlappedBytes int64
	imin, imax        internalKey
	tPtrs             []int
	released          bool

	snapGPI               int
	snapSeenKey           bool
	snapGPOverlappedBytes int64
	snapTPtrs             []int
}

func (c *compaction) save() {
	c.snapGPI = c.gpi
	c.snapSeenKey = c.seenKey
	c.snapGPOverlappedBytes = c.gpOverlappedBytes
	c.snapTPtrs = append(c.snapTPtrs[:0], c.tPtrs...)
}

func (c *compaction) restore() {
	c.gpi = c.snapGPI
	c.seenKey = c.snapSeenKey
	c.gpOverlappedBytes = c.snapGPOverlappedBytes
	c.tPtrs = append(c.tPtrs[:0], c.snapTPtrs...)
}

func (c *compaction) release() {
	if !c.released {
		c.released = true
		c.v.release()
	}
}

// Expand compacted tables; need external synchronization.
func (c *compaction) expand() {
	limit := int64(c.s.o.GetCompactionExpandLimit(c.sourceLevel))
	vt0 := c.v.levels[c.sourceLevel]
	vt1 := tFiles{}
	if level := c.sourceLevel + 1; level < len(c.v.levels) {
		vt1 = c.v.levels[level]
	}

	t0, t1 := c.levels[0], c.levels[1]
	imin, imax := t0.getRange(c.s.icmp)

	// For non-zero levels, the ukey can't hop across tables at all.
	if c.sourceLevel == 0 {
		// We expand t0 here just incase ukey hop across tables.
		t0 = vt0.getOverlaps(t0, c.s.icmp, imin.ukey(), imax.ukey(), c.sourceLevel == 0)
		if len(t0) != len(c.levels[0]) {
			imin, imax = t0.getRange(c.s.icmp)
		}
	}
	t1 = vt1.getOverlaps(t1, c.s.icmp, imin.ukey(), imax.ukey(), false)
	// Get entire range covered by compaction.
	amin, amax := append(t0, t1...).getRange(c.s.icmp)

	// See if we can grow the number of inputs in "sourceLevel" without
	// changing the number of "sourceLevel+1" files we pick up.
	if len(t1) > 0 {
		exp0 := vt0.getOverlaps(nil, c.s.icmp, amin.ukey(), amax.ukey(), c.sourceLevel == 0)
		if len(exp0) > len(t0) && t1.size()+exp0.size() < limit {
			xmin, xmax := exp0.getRange(c.s.icmp)
			exp1 := vt1.getOverlaps(nil, c.s.icmp, xmin.ukey(), xmax.ukey(), false)
			if len(exp1) == len(t1) {
				c.s.logf("table@compaction expanding L%d+L%d (F·%d S·%s)+(F·%d S·%s) -> (F·%d S·%s)+(F·%d S·%s)",
					c.sourceLevel, c.sourceLevel+1, len(t0), shortenb(t0.size()), len(t1), shortenb(t1.size()),
					len(exp0), shortenb(exp0.size()), len(exp1), shortenb(exp1.size()))
				imin, imax = xmin, xmax
				t0, t1 = exp0, exp1
				amin, amax = append(t0, t1...).getRange(c.s.icmp)
			}
		}
	}

	// Compute the set of grandparent files that overlap this compaction
	// (parent == sourceLevel+1; grandparent == sourceLevel+2)
	if level := c.sourceLevel + 2; level < len(c.v.levels) {
		c.gp = c.v.levels[level].getOverlaps(c.gp, c.s.icmp, amin.ukey(), amax.ukey(), false)
	}

	c.levels[0], c.levels[1] = t0, t1
	c.imin, c.imax = imin, imax
}

// Check whether compaction is trivial.
func (c *compaction) trivial() bool {
	return len(c.levels[0]) == 1 && len(c.levels[1]) == 0 && c.gp.size() <= c.maxGPOverlaps
}

func (c *compaction) baseLevelForKey(ukey []byte) bool {
	for level := c.sourceLevel + 2; level < len(c.v.levels); level++ {
		tables := c.v.levels[level]
		for c.tPtrs[level] < len(tables) {
			t := tables[c.tPtrs[level]]
			if c.s.icmp.uCompare(ukey, t.imax.ukey()) <= 0 {
				// We've advanced far enough.
				if c.s.icmp.uCompare(ukey, t.imin.ukey()) >= 0 {
					// Key falls in this file's range, so definitely not base level.
					return false
				}
				break
			}
			c.tPtrs[level]++
		}
	}
	return true
}

func (c *compaction) shouldStopBefore(ikey internalKey) bool {
	for ; c.gpi < len(c.gp); c.gpi++ {
		gp := c.gp[c.gpi]
		if c.s.icmp.Compare(ikey, gp.imax) <= 0 {
			break
		}
		if c.seenKey {
			c.gpOverlappedBytes += gp.size
		}
	}
	c.seenKey = true

	if c.gpOverlappedBytes > c.maxGPOverlaps {
		// Too much overlap for current output; start new output.
		c.gpOverlappedBytes = 0
		return true
	}
	return false
}

// Creates an iterator.
func (c *compaction) newIterator() iterator.Iterator {
	// Creates iterator slice.
	icap := len(c.levels)
	if c.sourceLevel == 0 {
		// Special case for level-0.
		icap = len(c.levels[0]) + 1
	}
	its := make([]iterator.Iterator, 0, icap)

	// Options.
	ro := &opt.ReadOptions{
		DontFillCache: true,
		Strict:        opt.StrictOverride,
	}
	strict := c.s.o.GetStrict(opt.StrictCompaction)
	if strict {
		ro.Strict |= opt.StrictReader
	}

	for i, tables := range c.levels {
		if len(tables) == 0 {
			continue
		}

		// Level-0 is not sorted and may overlaps each other.
		if c.sourceLevel+i == 0 {
			for _, t := range tables {
				its = append(its, c.s.tops.newIterator(t, nil, ro))
			}
		} else {
			it := iterator.NewIndexedIterator(tables.newIndexIterator(c.s.tops, c.s.icmp, nil, ro), strict)
			its = append(its, it)
		}
	}

	return iterator.NewMergedIterator(its, c.s.icmp, strict)
}
```

## File: `leveldb/session_record.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"bufio"
	"encoding/binary"
	"io"
	"strings"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

type byteReader interface {
	io.Reader
	io.ByteReader
}

// These numbers are written to disk and should not be changed.
const (
	recComparer    = 1
	recJournalNum  = 2
	recNextFileNum = 3
	recSeqNum      = 4
	recCompPtr     = 5
	recDelTable    = 6
	recAddTable    = 7
	// 8 was used for large value refs
	recPrevJournalNum = 9
)

type cpRecord struct {
	level int
	ikey  internalKey
}

type atRecord struct {
	level int
	num   int64
	size  int64
	imin  internalKey
	imax  internalKey
}

type dtRecord struct {
	level int
	num   int64
}

type sessionRecord struct {
	hasRec         int
	comparer       string
	journalNum     int64
	prevJournalNum int64
	nextFileNum    int64
	seqNum         uint64
	compPtrs       []cpRecord
	addedTables    []atRecord
	deletedTables  []dtRecord

	scratch [binary.MaxVarintLen64]byte
	err     error
}

func (p *sessionRecord) has(rec int) bool {
	return p.hasRec&(1<<uint(rec)) != 0
}

func (p *sessionRecord) setComparer(name string) {
	p.hasRec |= 1 << recComparer
	p.comparer = name
}

func (p *sessionRecord) setJournalNum(num int64) {
	p.hasRec |= 1 << recJournalNum
	p.journalNum = num
}

func (p *sessionRecord) setPrevJournalNum(num int64) {
	p.hasRec |= 1 << recPrevJournalNum
	p.prevJournalNum = num
}

func (p *sessionRecord) setNextFileNum(num int64) {
	p.hasRec |= 1 << recNextFileNum
	p.nextFileNum = num
}

func (p *sessionRecord) setSeqNum(num uint64) {
	p.hasRec |= 1 << recSeqNum
	p.seqNum = num
}

func (p *sessionRecord) addCompPtr(level int, ikey internalKey) {
	p.hasRec |= 1 << recCompPtr
	p.compPtrs = append(p.compPtrs, cpRecord{level, ikey})
}

func (p *sessionRecord) resetCompPtrs() {
	p.hasRec &= ^(1 << recCompPtr)
	p.compPtrs = p.compPtrs[:0]
}

func (p *sessionRecord) addTable(level int, num, size int64, imin, imax internalKey) {
	p.hasRec |= 1 << recAddTable
	p.addedTables = append(p.addedTables, atRecord{level, num, size, imin, imax})
}

func (p *sessionRecord) addTableFile(level int, t *tFile) {
	p.addTable(level, t.fd.Num, t.size, t.imin, t.imax)
}

func (p *sessionRecord) resetAddedTables() {
	p.hasRec &= ^(1 << recAddTable)
	p.addedTables = p.addedTables[:0]
}

func (p *sessionRecord) delTable(level int, num int64) {
	p.hasRec |= 1 << recDelTable
	p.deletedTables = append(p.deletedTables, dtRecord{level, num})
}

func (p *sessionRecord) resetDeletedTables() {
	p.hasRec &= ^(1 << recDelTable)
	p.deletedTables = p.deletedTables[:0]
}

func (p *sessionRecord) putUvarint(w io.Writer, x uint64) {
	if p.err != nil {
		return
	}
	n := binary.PutUvarint(p.scratch[:], x)
	_, p.err = w.Write(p.scratch[:n])
}

func (p *sessionRecord) putVarint(w io.Writer, x int64) {
	if x < 0 {
		panic("invalid negative value")
	}
	p.putUvarint(w, uint64(x))
}

func (p *sessionRecord) putBytes(w io.Writer, x []byte) {
	if p.err != nil {
		return
	}
	p.putUvarint(w, uint64(len(x)))
	if p.err != nil {
		return
	}
	_, p.err = w.Write(x)
}

func (p *sessionRecord) encode(w io.Writer) error {
	p.err = nil
	if p.has(recComparer) {
		p.putUvarint(w, recComparer)
		p.putBytes(w, []byte(p.comparer))
	}
	if p.has(recJournalNum) {
		p.putUvarint(w, recJournalNum)
		p.putVarint(w, p.journalNum)
	}
	if p.has(recNextFileNum) {
		p.putUvarint(w, recNextFileNum)
		p.putVarint(w, p.nextFileNum)
	}
	if p.has(recSeqNum) {
		p.putUvarint(w, recSeqNum)
		p.putUvarint(w, p.seqNum)
	}
	for _, r := range p.compPtrs {
		p.putUvarint(w, recCompPtr)
		p.putUvarint(w, uint64(r.level))
		p.putBytes(w, r.ikey)
	}
	for _, r := range p.deletedTables {
		p.putUvarint(w, recDelTable)
		p.putUvarint(w, uint64(r.level))
		p.putVarint(w, r.num)
	}
	for _, r := range p.addedTables {
		p.putUvarint(w, recAddTable)
		p.putUvarint(w, uint64(r.level))
		p.putVarint(w, r.num)
		p.putVarint(w, r.size)
		p.putBytes(w, r.imin)
		p.putBytes(w, r.imax)
	}
	return p.err
}

func (p *sessionRecord) readUvarintMayEOF(field string, r io.ByteReader, mayEOF bool) uint64 {
	if p.err != nil {
		return 0
	}
	x, err := binary.ReadUvarint(r)
	if err != nil {
		if err == io.ErrUnexpectedEOF || (!mayEOF && err == io.EOF) {
			p.err = errors.NewErrCorrupted(storage.FileDesc{}, &ErrManifestCorrupted{field, "short read"})
		} else if strings.HasPrefix(err.Error(), "binary:") {
			p.err = errors.NewErrCorrupted(storage.FileDesc{}, &ErrManifestCorrupted{field, err.Error()})
		} else {
			p.err = err
		}
		return 0
	}
	return x
}

func (p *sessionRecord) readUvarint(field string, r io.ByteReader) uint64 {
	return p.readUvarintMayEOF(field, r, false)
}

func (p *sessionRecord) readVarint(field string, r io.ByteReader) int64 {
	x := int64(p.readUvarintMayEOF(field, r, false))
	if x < 0 {
		p.err = errors.NewErrCorrupted(storage.FileDesc{}, &ErrManifestCorrupted{field, "invalid negative value"})
	}
	return x
}

func (p *sessionRecord) readBytes(field string, r byteReader) []byte {
	if p.err != nil {
		return nil
	}
	n := p.readUvarint(field, r)
	if p.err != nil {
		return nil
	}
	x := make([]byte, n)
	_, p.err = io.ReadFull(r, x)
	if p.err != nil {
		if p.err == io.ErrUnexpectedEOF {
			p.err = errors.NewErrCorrupted(storage.FileDesc{}, &ErrManifestCorrupted{field, "short read"})
		}
		return nil
	}
	return x
}

func (p *sessionRecord) readLevel(field string, r io.ByteReader) int {
	if p.err != nil {
		return 0
	}
	x := p.readUvarint(field, r)
	if p.err != nil {
		return 0
	}
	return int(x)
}

func (p *sessionRecord) decode(r io.Reader) error {
	br, ok := r.(byteReader)
	if !ok {
		br = bufio.NewReader(r)
	}
	p.err = nil
	for p.err == nil {
		rec := p.readUvarintMayEOF("field-header", br, true)
		if p.err != nil {
			if p.err == io.EOF {
				return nil
			}
			return p.err
		}
		switch rec {
		case recComparer:
			x := p.readBytes("comparer", br)
			if p.err == nil {
				p.setComparer(string(x))
			}
		case recJournalNum:
			x := p.readVarint("journal-num", br)
			if p.err == nil {
				p.setJournalNum(x)
			}
		case recPrevJournalNum:
			x := p.readVarint("prev-journal-num", br)
			if p.err == nil {
				p.setPrevJournalNum(x)
			}
		case recNextFileNum:
			x := p.readVarint("next-file-num", br)
			if p.err == nil {
				p.setNextFileNum(x)
			}
		case recSeqNum:
			x := p.readUvarint("seq-num", br)
			if p.err == nil {
				p.setSeqNum(x)
			}
		case recCompPtr:
			level := p.readLevel("comp-ptr.level", br)
			ikey := p.readBytes("comp-ptr.ikey", br)
			if p.err == nil {
				p.addCompPtr(level, internalKey(ikey))
			}
		case recAddTable:
			level := p.readLevel("add-table.level", br)
			num := p.readVarint("add-table.num", br)
			size := p.readVarint("add-table.size", br)
			imin := p.readBytes("add-table.imin", br)
			imax := p.readBytes("add-table.imax", br)
			if p.err == nil {
				p.addTable(level, num, size, imin, imax)
			}
		case recDelTable:
			level := p.readLevel("del-table.level", br)
			num := p.readVarint("del-table.num", br)
			if p.err == nil {
				p.delTable(level, num)
			}
		}
	}

	return p.err
}
```

## File: `leveldb/session_record_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"bytes"
	"testing"
)

func decodeEncode(v *sessionRecord) (res bool, err error) {
	b := new(bytes.Buffer)
	err = v.encode(b)
	if err != nil {
		return
	}
	v2 := &sessionRecord{}
	err = v.decode(b)
	if err != nil {
		return
	}
	b2 := new(bytes.Buffer)
	err = v2.encode(b2)
	if err != nil {
		return
	}
	return bytes.Equal(b.Bytes(), b2.Bytes()), nil
}

func TestSessionRecord_EncodeDecode(t *testing.T) {
	big := int64(1) << 50
	v := &sessionRecord{}
	i := int64(0)
	test := func() {
		res, err := decodeEncode(v)
		if err != nil {
			t.Fatalf("error when testing encode/decode sessionRecord: %v", err)
		}
		if !res {
			t.Error("encode/decode test failed at iteration:", i)
		}
	}

	for ; i < 4; i++ {
		test()
		v.addTable(3, big+300+i, big+400+i,
			makeInternalKey(nil, []byte("foo"), uint64(big+500+1), keyTypeVal),
			makeInternalKey(nil, []byte("zoo"), uint64(big+600+1), keyTypeDel))
		v.delTable(4, big+700+i)
		v.addCompPtr(int(i), makeInternalKey(nil, []byte("x"), uint64(big+900+1), keyTypeVal))
	}

	v.setComparer("foo")
	v.setJournalNum(big + 100)
	v.setPrevJournalNum(big + 99)
	v.setNextFileNum(big + 200)
	v.setSeqNum(uint64(big + 1000))
	test()
}
```

## File: `leveldb/session_util.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"fmt"
	"sync/atomic"
	"time"

	"github.com/syndtr/goleveldb/leveldb/journal"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

// Logging.

type dropper struct {
	s  *session
	fd storage.FileDesc
}

func (d dropper) Drop(err error) {
	if e, ok := err.(*journal.ErrCorrupted); ok {
		d.s.logf("journal@drop %s-%d S·%s %q", d.fd.Type, d.fd.Num, shortenb(int64(e.Size)), e.Reason)
	} else {
		d.s.logf("journal@drop %s-%d %q", d.fd.Type, d.fd.Num, err)
	}
}

func (s *session) log(v ...interface{})                 { s.stor.Log(fmt.Sprint(v...)) }
func (s *session) logf(format string, v ...interface{}) { s.stor.Log(fmt.Sprintf(format, v...)) }

// File utils.

func (s *session) newTemp() storage.FileDesc {
	num := atomic.AddInt64(&s.stTempFileNum, 1) - 1
	return storage.FileDesc{Type: storage.TypeTemp, Num: num}
}

// Session state.

const (
	// maxCachedNumber represents the maximum number of version tasks
	// that can be cached in the ref loop.
	maxCachedNumber = 256

	// maxCachedTime represents the maximum time for ref loop to cache
	// a version task.
	maxCachedTime = 5 * time.Minute
)

// vDelta indicates the change information between the next version
// and the currently specified version
type vDelta struct {
	vid     int64
	added   []int64
	deleted []int64
}

// vTask defines a version task for either reference or release.
type vTask struct {
	vid     int64
	files   []tFiles
	created time.Time
}

func (s *session) refLoop() {
	var (
		fileRef    = make(map[int64]int)    // Table file reference counter
		ref        = make(map[int64]*vTask) // Current referencing version store
		deltas     = make(map[int64]*vDelta)
		referenced = make(map[int64]struct{})
		released   = make(map[int64]*vDelta)  // Released version that waiting for processing
		abandoned  = make(map[int64]struct{}) // Abandoned version id
		next, last int64
	)
	// addFileRef adds file reference counter with specified file number and
	// reference value
	addFileRef := func(fnum int64, ref int) int {
		ref += fileRef[fnum]
		if ref > 0 {
			fileRef[fnum] = ref
		} else if ref == 0 {
			delete(fileRef, fnum)
		} else {
			panic(fmt.Sprintf("negative ref: %v", fnum))
		}
		return ref
	}
	// skipAbandoned skips useless abandoned version id.
	skipAbandoned := func() bool {
		if _, exist := abandoned[next]; exist {
			delete(abandoned, next)
			return true
		}
		return false
	}
	// applyDelta applies version change to current file reference.
	applyDelta := func(d *vDelta) {
		for _, t := range d.added {
			addFileRef(t, 1)
		}
		for _, t := range d.deleted {
			if addFileRef(t, -1) == 0 {
				s.tops.remove(storage.FileDesc{Type: storage.TypeTable, Num: t})
			}
		}
	}

	timer := time.NewTimer(0)
	<-timer.C // discard the initial tick
	defer timer.Stop()

	// processTasks processes version tasks in strict order.
	//
	// If we want to use delta to reduce the cost of file references and dereferences,
	// we must strictly follow the id of the version, otherwise some files that are
	// being referenced will be deleted.
	//
	// In addition, some db operations (such as iterators) may cause a version to be
	// referenced for a long time. In order to prevent such operations from blocking
	// the entire processing queue, we will properly convert some of the version tasks
	// into full file references and releases.
	processTasks := func() {
		timer.Reset(maxCachedTime)
		// Make sure we don't cache too many version tasks.
		for {
			// Skip any abandoned version number to prevent blocking processing.
			if skipAbandoned() {
				next++
				continue
			}
			// Don't bother the version that has been released.
			if _, exist := released[next]; exist {
				break
			}
			// Ensure the specified version has been referenced.
			if _, exist := ref[next]; !exist {
				break
			}
			if last-next < maxCachedNumber && time.Since(ref[next].created) < maxCachedTime {
				break
			}
			// Convert version task into full file references and releases mode.
			// Reference version(i+1) first and wait version(i) to release.
			// FileRef(i+1) = FileRef(i) + Delta(i)
			for _, tt := range ref[next].files {
				for _, t := range tt {
					addFileRef(t.fd.Num, 1)
				}
			}
			// Note, if some compactions take a long time, even more than 5 minutes,
			// we may miss the corresponding delta information here.
			// Fortunately it will not affect the correctness of the file reference,
			// and we can apply the delta once we receive it.
			if d := deltas[next]; d != nil {
				applyDelta(d)
			}
			referenced[next] = struct{}{}
			delete(ref, next)
			delete(deltas, next)
			next++
		}

		// Use delta information to process all released versions.
		for {
			if skipAbandoned() {
				next++
				continue
			}
			if d, exist := released[next]; exist {
				if d != nil {
					applyDelta(d)
				}
				delete(released, next)
				next++
				continue
			}
			return
		}
	}

	for {
		processTasks()

		select {
		case t := <-s.refCh:
			if _, exist := ref[t.vid]; exist {
				panic("duplicate reference request")
			}
			ref[t.vid] = t
			if t.vid > last {
				last = t.vid
			}

		case d := <-s.deltaCh:
			if _, exist := ref[d.vid]; !exist {
				if _, exist2 := referenced[d.vid]; !exist2 {
					panic("invalid release request")
				}
				// The reference opt is already expired, apply
				// delta here.
				applyDelta(d)
				continue
			}
			deltas[d.vid] = d

		case t := <-s.relCh:
			if _, exist := referenced[t.vid]; exist {
				for _, tt := range t.files {
					for _, t := range tt {
						if addFileRef(t.fd.Num, -1) == 0 {
							s.tops.remove(t.fd)
						}
					}
				}
				delete(referenced, t.vid)
				continue
			}
			if _, exist := ref[t.vid]; !exist {
				panic("invalid release request")
			}
			released[t.vid] = deltas[t.vid]
			delete(deltas, t.vid)
			delete(ref, t.vid)

		case id := <-s.abandon:
			if id >= next {
				abandoned[id] = struct{}{}
			}

		case <-timer.C:

		case r := <-s.fileRefCh:
			ref := make(map[int64]int)
			for f, c := range fileRef {
				ref[f] = c
			}
			r <- ref

		case <-s.closeC:
			s.closeW.Done()
			return
		}
	}
}

// Get current version. This will incr version ref, must call
// version.release (exactly once) after use.
func (s *session) version() *version {
	s.vmu.Lock()
	defer s.vmu.Unlock()
	s.stVersion.incref()
	return s.stVersion
}

func (s *session) tLen(level int) int {
	s.vmu.Lock()
	defer s.vmu.Unlock()
	return s.stVersion.tLen(level)
}

// Set current version to v.
func (s *session) setVersion(r *sessionRecord, v *version) {
	s.vmu.Lock()
	defer s.vmu.Unlock()
	// Hold by session. It is important to call this first before releasing
	// current version, otherwise the still used files might get released.
	v.incref()
	if s.stVersion != nil {
		if r != nil {
			var (
				added   = make([]int64, 0, len(r.addedTables))
				deleted = make([]int64, 0, len(r.deletedTables))
			)
			for _, t := range r.addedTables {
				added = append(added, t.num)
			}
			for _, t := range r.deletedTables {
				deleted = append(deleted, t.num)
			}
			select {
			case s.deltaCh <- &vDelta{vid: s.stVersion.id, added: added, deleted: deleted}:
			case <-v.s.closeC:
				s.log("reference loop already exist")
			}
		}
		// Release current version.
		s.stVersion.releaseNB()
	}
	s.stVersion = v
}

// Get current unused file number.
func (s *session) nextFileNum() int64 {
	return atomic.LoadInt64(&s.stNextFileNum)
}

// Set current unused file number to num.
func (s *session) setNextFileNum(num int64) {
	atomic.StoreInt64(&s.stNextFileNum, num)
}

// Mark file number as used.
func (s *session) markFileNum(num int64) {
	nextFileNum := num + 1
	for {
		old, x := atomic.LoadInt64(&s.stNextFileNum), nextFileNum
		if old > x {
			x = old
		}
		if atomic.CompareAndSwapInt64(&s.stNextFileNum, old, x) {
			break
		}
	}
}

// Allocate a file number.
func (s *session) allocFileNum() int64 {
	return atomic.AddInt64(&s.stNextFileNum, 1) - 1
}

// Reuse given file number.
func (s *session) reuseFileNum(num int64) {
	for {
		old, x := atomic.LoadInt64(&s.stNextFileNum), num
		if old != x+1 {
			x = old
		}
		if atomic.CompareAndSwapInt64(&s.stNextFileNum, old, x) {
			break
		}
	}
}

// Set compaction ptr at given level; need external synchronization.
func (s *session) setCompPtr(level int, ik internalKey) {
	if level >= len(s.stCompPtrs) {
		newCompPtrs := make([]internalKey, level+1)
		copy(newCompPtrs, s.stCompPtrs)
		s.stCompPtrs = newCompPtrs
	}
	s.stCompPtrs[level] = append(internalKey{}, ik...)
}

// Get compaction ptr at given level; need external synchronization.
func (s *session) getCompPtr(level int) internalKey {
	if level >= len(s.stCompPtrs) {
		return nil
	}
	return s.stCompPtrs[level]
}

// Manifest related utils.

// Fill given session record obj with current states; need external
// synchronization.
func (s *session) fillRecord(r *sessionRecord, snapshot bool) {
	r.setNextFileNum(s.nextFileNum())

	if snapshot {
		if !r.has(recJournalNum) {
			r.setJournalNum(s.stJournalNum)
		}

		if !r.has(recSeqNum) {
			r.setSeqNum(s.stSeqNum)
		}

		for level, ik := range s.stCompPtrs {
			if ik != nil {
				r.addCompPtr(level, ik)
			}
		}

		r.setComparer(s.icmp.uName())
	}
}

// Mark if record has been committed, this will update session state;
// need external synchronization.
func (s *session) recordCommited(rec *sessionRecord) {
	if rec.has(recJournalNum) {
		s.stJournalNum = rec.journalNum
	}

	if rec.has(recPrevJournalNum) {
		s.stPrevJournalNum = rec.prevJournalNum
	}

	if rec.has(recSeqNum) {
		s.stSeqNum = rec.seqNum
	}

	for _, r := range rec.compPtrs {
		s.setCompPtr(r.level, r.ikey)
	}
}

// Create a new manifest file; need external synchronization.
func (s *session) newManifest(rec *sessionRecord, v *version) (err error) {
	fd := storage.FileDesc{Type: storage.TypeManifest, Num: s.allocFileNum()}
	writer, err := s.stor.Create(fd)
	if err != nil {
		return
	}
	jw := journal.NewWriter(writer)

	if v == nil {
		v = s.version()
		defer v.release()
	}
	if rec == nil {
		rec = &sessionRecord{}
	}
	s.fillRecord(rec, true)
	v.fillRecord(rec)

	defer func() {
		if err == nil {
			s.recordCommited(rec)
			if s.manifest != nil {
				s.manifest.Close()
			}
			if s.manifestWriter != nil {
				s.manifestWriter.Close()
			}
			if !s.manifestFd.Zero() {
				err = s.stor.Remove(s.manifestFd)
			}
			s.manifestFd = fd
			s.manifestWriter = writer
			s.manifest = jw
		} else {
			writer.Close()
			if rerr := s.stor.Remove(fd); err != nil {
				err = fmt.Errorf("newManifest error: %v, cleanup error (%v)", err, rerr)
			}
			s.reuseFileNum(fd.Num)
		}
	}()

	w, err := jw.Next()
	if err != nil {
		return
	}
	err = rec.encode(w)
	if err != nil {
		return
	}
	err = jw.Flush()
	if err != nil {
		return
	}
	if !s.o.GetNoSync() {
		err = writer.Sync()
		if err != nil {
			return
		}
	}
	err = s.stor.SetMeta(fd)
	return
}

// Flush record to disk.
func (s *session) flushManifest(rec *sessionRecord) (err error) {
	s.fillRecord(rec, false)
	w, err := s.manifest.Next()
	if err != nil {
		return
	}
	err = rec.encode(w)
	if err != nil {
		return
	}
	err = s.manifest.Flush()
	if err != nil {
		return
	}
	if !s.o.GetNoSync() {
		err = s.manifestWriter.Sync()
		if err != nil {
			return
		}
	}
	s.recordCommited(rec)
	return
}
```

## File: `leveldb/storage.go`
```go
package leveldb

import (
	"github.com/syndtr/goleveldb/leveldb/storage"
	"sync/atomic"
)

type iStorage struct {
	storage.Storage
	read  uint64
	write uint64
}

func (c *iStorage) Open(fd storage.FileDesc) (storage.Reader, error) {
	r, err := c.Storage.Open(fd)
	return &iStorageReader{r, c}, err
}

func (c *iStorage) Create(fd storage.FileDesc) (storage.Writer, error) {
	w, err := c.Storage.Create(fd)
	return &iStorageWriter{w, c}, err
}

func (c *iStorage) reads() uint64 {
	return atomic.LoadUint64(&c.read)
}

func (c *iStorage) writes() uint64 {
	return atomic.LoadUint64(&c.write)
}

// newIStorage returns the given storage wrapped by iStorage.
func newIStorage(s storage.Storage) *iStorage {
	return &iStorage{s, 0, 0}
}

type iStorageReader struct {
	storage.Reader
	c *iStorage
}

func (r *iStorageReader) Read(p []byte) (n int, err error) {
	n, err = r.Reader.Read(p)
	atomic.AddUint64(&r.c.read, uint64(n))
	return n, err
}

func (r *iStorageReader) ReadAt(p []byte, off int64) (n int, err error) {
	n, err = r.Reader.ReadAt(p, off)
	atomic.AddUint64(&r.c.read, uint64(n))
	return n, err
}

type iStorageWriter struct {
	storage.Writer
	c *iStorage
}

func (w *iStorageWriter) Write(p []byte) (n int, err error) {
	n, err = w.Writer.Write(p)
	atomic.AddUint64(&w.c.write, uint64(n))
	return n, err
}
```

## File: `leveldb/table.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"bytes"
	"fmt"
	"sort"
	"sync/atomic"

	"github.com/syndtr/goleveldb/leveldb/cache"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/table"
	"github.com/syndtr/goleveldb/leveldb/util"
)

// tFile holds basic information about a table.
type tFile struct {
	fd         storage.FileDesc
	seekLeft   int32
	size       int64
	imin, imax internalKey
}

// Returns true if given key is after largest key of this table.
func (t *tFile) after(icmp *iComparer, ukey []byte) bool {
	return ukey != nil && icmp.uCompare(ukey, t.imax.ukey()) > 0
}

// Returns true if given key is before smallest key of this table.
func (t *tFile) before(icmp *iComparer, ukey []byte) bool {
	return ukey != nil && icmp.uCompare(ukey, t.imin.ukey()) < 0
}

// Returns true if given key range overlaps with this table key range.
func (t *tFile) overlaps(icmp *iComparer, umin, umax []byte) bool {
	return !t.after(icmp, umin) && !t.before(icmp, umax)
}

// Cosumes one seek and return current seeks left.
func (t *tFile) consumeSeek() int32 {
	return atomic.AddInt32(&t.seekLeft, -1)
}

// Creates new tFile.
func newTableFile(fd storage.FileDesc, size int64, imin, imax internalKey) *tFile {
	f := &tFile{
		fd:   fd,
		size: size,
		imin: imin,
		imax: imax,
	}

	// We arrange to automatically compact this file after
	// a certain number of seeks.  Let's assume:
	//   (1) One seek costs 10ms
	//   (2) Writing or reading 1MB costs 10ms (100MB/s)
	//   (3) A compaction of 1MB does 25MB of IO:
	//         1MB read from this level
	//         10-12MB read from next level (boundaries may be misaligned)
	//         10-12MB written to next level
	// This implies that 25 seeks cost the same as the compaction
	// of 1MB of data.  I.e., one seek costs approximately the
	// same as the compaction of 40KB of data.  We are a little
	// conservative and allow approximately one seek for every 16KB
	// of data before triggering a compaction.
	f.seekLeft = int32(size / 16384)
	if f.seekLeft < 100 {
		f.seekLeft = 100
	}

	return f
}

func tableFileFromRecord(r atRecord) *tFile {
	return newTableFile(storage.FileDesc{Type: storage.TypeTable, Num: r.num}, r.size, r.imin, r.imax)
}

// tFiles hold multiple tFile.
type tFiles []*tFile

func (tf tFiles) Len() int      { return len(tf) }
func (tf tFiles) Swap(i, j int) { tf[i], tf[j] = tf[j], tf[i] }

// Returns true if i smallest key is less than j.
// This used for sort by key in ascending order.
func (tf tFiles) lessByKey(icmp *iComparer, i, j int) bool {
	a, b := tf[i], tf[j]
	n := icmp.Compare(a.imin, b.imin)
	if n == 0 {
		return a.fd.Num < b.fd.Num
	}
	return n < 0
}

// Returns true if i file number is greater than j.
// This used for sort by file number in descending order.
func (tf tFiles) lessByNum(i, j int) bool {
	return tf[i].fd.Num > tf[j].fd.Num
}

// Sorts tables by key in ascending order.
func (tf tFiles) sortByKey(icmp *iComparer) {
	sort.Sort(&tFilesSortByKey{tFiles: tf, icmp: icmp})
}

// Sorts tables by file number in descending order.
func (tf tFiles) sortByNum() {
	sort.Sort(&tFilesSortByNum{tFiles: tf})
}

// Returns sum of all tables size.
func (tf tFiles) size() (sum int64) {
	for _, t := range tf {
		sum += t.size
	}
	return sum
}

// Searches smallest index of tables whose its smallest
// key is after or equal with given key.
func (tf tFiles) searchMin(icmp *iComparer, ikey internalKey) int {
	return sort.Search(len(tf), func(i int) bool {
		return icmp.Compare(tf[i].imin, ikey) >= 0
	})
}

// Searches smallest index of tables whose its largest
// key is after or equal with given key.
func (tf tFiles) searchMax(icmp *iComparer, ikey internalKey) int {
	return sort.Search(len(tf), func(i int) bool {
		return icmp.Compare(tf[i].imax, ikey) >= 0
	})
}

// Searches smallest index of tables whose its file number
// is smaller than the given number.
func (tf tFiles) searchNumLess(num int64) int {
	return sort.Search(len(tf), func(i int) bool {
		return tf[i].fd.Num < num
	})
}

// Searches smallest index of tables whose its smallest
// key is after the given key.
func (tf tFiles) searchMinUkey(icmp *iComparer, umin []byte) int {
	return sort.Search(len(tf), func(i int) bool {
		return icmp.ucmp.Compare(tf[i].imin.ukey(), umin) > 0
	})
}

// Searches smallest index of tables whose its largest
// key is after the given key.
func (tf tFiles) searchMaxUkey(icmp *iComparer, umax []byte) int {
	return sort.Search(len(tf), func(i int) bool {
		return icmp.ucmp.Compare(tf[i].imax.ukey(), umax) > 0
	})
}

// Returns true if given key range overlaps with one or more
// tables key range. If unsorted is true then binary search will not be used.
func (tf tFiles) overlaps(icmp *iComparer, umin, umax []byte, unsorted bool) bool {
	if unsorted {
		// Check against all files.
		for _, t := range tf {
			if t.overlaps(icmp, umin, umax) {
				return true
			}
		}
		return false
	}

	i := 0
	if len(umin) > 0 {
		// Find the earliest possible internal key for min.
		i = tf.searchMax(icmp, makeInternalKey(nil, umin, keyMaxSeq, keyTypeSeek))
	}
	if i >= len(tf) {
		// Beginning of range is after all files, so no overlap.
		return false
	}
	return !tf[i].before(icmp, umax)
}

// Returns tables whose its key range overlaps with given key range.
// Range will be expanded if ukey found hop across tables.
// If overlapped is true then the search will be restarted if umax
// expanded.
// The dst content will be overwritten.
func (tf tFiles) getOverlaps(dst tFiles, icmp *iComparer, umin, umax []byte, overlapped bool) tFiles {
	// Short circuit if tf is empty
	if len(tf) == 0 {
		return nil
	}
	// For non-zero levels, there is no ukey hop across at all.
	// And what's more, the files in these levels are strictly sorted,
	// so use binary search instead of heavy traverse.
	if !overlapped {
		var begin, end int
		// Determine the begin index of the overlapped file
		if umin != nil {
			index := tf.searchMinUkey(icmp, umin)
			if index == 0 {
				begin = 0
			} else if bytes.Compare(tf[index-1].imax.ukey(), umin) >= 0 {
				// The min ukey overlaps with the index-1 file, expand it.
				begin = index - 1
			} else {
				begin = index
			}
		}
		// Determine the end index of the overlapped file
		if umax != nil {
			index := tf.searchMaxUkey(icmp, umax)
			if index == len(tf) {
				end = len(tf)
			} else if bytes.Compare(tf[index].imin.ukey(), umax) <= 0 {
				// The max ukey overlaps with the index file, expand it.
				end = index + 1
			} else {
				end = index
			}
		} else {
			end = len(tf)
		}
		// Ensure the overlapped file indexes are valid.
		if begin >= end {
			return nil
		}
		dst = make([]*tFile, end-begin)
		copy(dst, tf[begin:end])
		return dst
	}

	dst = dst[:0]
	for i := 0; i < len(tf); {
		t := tf[i]
		if t.overlaps(icmp, umin, umax) {
			if umin != nil && icmp.uCompare(t.imin.ukey(), umin) < 0 {
				umin = t.imin.ukey()
				dst = dst[:0]
				i = 0
				continue
			} else if umax != nil && icmp.uCompare(t.imax.ukey(), umax) > 0 {
				umax = t.imax.ukey()
				// Restart search if it is overlapped.
				dst = dst[:0]
				i = 0
				continue
			}

			dst = append(dst, t)
		}
		i++
	}

	return dst
}

// Returns tables key range.
func (tf tFiles) getRange(icmp *iComparer) (imin, imax internalKey) {
	for i, t := range tf {
		if i == 0 {
			imin, imax = t.imin, t.imax
			continue
		}
		if icmp.Compare(t.imin, imin) < 0 {
			imin = t.imin
		}
		if icmp.Compare(t.imax, imax) > 0 {
			imax = t.imax
		}
	}

	return
}

// Creates iterator index from tables.
func (tf tFiles) newIndexIterator(tops *tOps, icmp *iComparer, slice *util.Range, ro *opt.ReadOptions) iterator.IteratorIndexer {
	if slice != nil {
		var start, limit int
		if slice.Start != nil {
			start = tf.searchMax(icmp, internalKey(slice.Start))
		}
		if slice.Limit != nil {
			limit = tf.searchMin(icmp, internalKey(slice.Limit))
		} else {
			limit = tf.Len()
		}
		tf = tf[start:limit]
	}
	return iterator.NewArrayIndexer(&tFilesArrayIndexer{
		tFiles: tf,
		tops:   tops,
		icmp:   icmp,
		slice:  slice,
		ro:     ro,
	})
}

// Tables iterator index.
type tFilesArrayIndexer struct {
	tFiles
	tops  *tOps
	icmp  *iComparer
	slice *util.Range
	ro    *opt.ReadOptions
}

func (a *tFilesArrayIndexer) Search(key []byte) int {
	return a.searchMax(a.icmp, internalKey(key))
}

func (a *tFilesArrayIndexer) Get(i int) iterator.Iterator {
	if i == 0 || i == a.Len()-1 {
		return a.tops.newIterator(a.tFiles[i], a.slice, a.ro)
	}
	return a.tops.newIterator(a.tFiles[i], nil, a.ro)
}

// Helper type for sortByKey.
type tFilesSortByKey struct {
	tFiles
	icmp *iComparer
}

func (x *tFilesSortByKey) Less(i, j int) bool {
	return x.lessByKey(x.icmp, i, j)
}

// Helper type for sortByNum.
type tFilesSortByNum struct {
	tFiles
}

func (x *tFilesSortByNum) Less(i, j int) bool {
	return x.lessByNum(i, j)
}

// Table operations.
type tOps struct {
	s            *session
	noSync       bool
	evictRemoved bool
	fileCache    *cache.Cache
	blockCache   *cache.Cache
	blockBuffer  *util.BufferPool
}

// Creates an empty table and returns table writer.
func (t *tOps) create(tSize int) (*tWriter, error) {
	fd := storage.FileDesc{Type: storage.TypeTable, Num: t.s.allocFileNum()}
	fw, err := t.s.stor.Create(fd)
	if err != nil {
		return nil, err
	}
	return &tWriter{
		t:  t,
		fd: fd,
		w:  fw,
		tw: table.NewWriter(fw, t.s.o.Options, t.blockBuffer, tSize),
	}, nil
}

// Builds table from src iterator.
func (t *tOps) createFrom(src iterator.Iterator) (f *tFile, n int, err error) {
	w, err := t.create(0)
	if err != nil {
		return
	}

	defer func() {
		if err != nil {
			if derr := w.drop(); derr != nil {
				err = fmt.Errorf("error createFrom (%v); error dropping (%v)", err, derr)
			}
		}
	}()

	for src.Next() {
		err = w.append(src.Key(), src.Value())
		if err != nil {
			return
		}
	}
	err = src.Error()
	if err != nil {
		return
	}

	n = w.tw.EntriesLen()
	f, err = w.finish()
	return
}

// Opens table. It returns a cache handle, which should
// be released after use.
func (t *tOps) open(f *tFile) (ch *cache.Handle, err error) {
	ch = t.fileCache.Get(0, uint64(f.fd.Num), func() (size int, value cache.Value) {
		var r storage.Reader
		r, err = t.s.stor.Open(f.fd)
		if err != nil {
			return 0, nil
		}

		var blockCache *cache.NamespaceGetter
		if t.blockCache != nil {
			blockCache = &cache.NamespaceGetter{Cache: t.blockCache, NS: uint64(f.fd.Num)}
		}

		var tr *table.Reader
		tr, err = table.NewReader(r, f.size, f.fd, blockCache, t.blockBuffer, t.s.o.Options)
		if err != nil {
			_ = r.Close()
			return 0, nil
		}
		return 1, tr

	})
	if ch == nil && err == nil {
		err = ErrClosed
	}
	return
}

// Finds key/value pair whose key is greater than or equal to the
// given key.
func (t *tOps) find(f *tFile, key []byte, ro *opt.ReadOptions) (rkey, rvalue []byte, err error) {
	ch, err := t.open(f)
	if err != nil {
		return nil, nil, err
	}
	defer ch.Release()
	return ch.Value().(*table.Reader).Find(key, true, ro)
}

// Finds key that is greater than or equal to the given key.
func (t *tOps) findKey(f *tFile, key []byte, ro *opt.ReadOptions) (rkey []byte, err error) {
	ch, err := t.open(f)
	if err != nil {
		return nil, err
	}
	defer ch.Release()
	return ch.Value().(*table.Reader).FindKey(key, true, ro)
}

// Returns approximate offset of the given key.
func (t *tOps) offsetOf(f *tFile, key []byte) (offset int64, err error) {
	ch, err := t.open(f)
	if err != nil {
		return
	}
	defer ch.Release()
	return ch.Value().(*table.Reader).OffsetOf(key)
}

// Creates an iterator from the given table.
func (t *tOps) newIterator(f *tFile, slice *util.Range, ro *opt.ReadOptions) iterator.Iterator {
	ch, err := t.open(f)
	if err != nil {
		return iterator.NewEmptyIterator(err)
	}
	iter := ch.Value().(*table.Reader).NewIterator(slice, ro)
	iter.SetReleaser(ch)
	return iter
}

// Removes table from persistent storage. It waits until
// no one use the the table.
func (t *tOps) remove(fd storage.FileDesc) {
	t.fileCache.Delete(0, uint64(fd.Num), func() {
		if err := t.s.stor.Remove(fd); err != nil {
			t.s.logf("table@remove removing @%d %q", fd.Num, err)
		} else {
			t.s.logf("table@remove removed @%d", fd.Num)
		}
		if t.evictRemoved && t.blockCache != nil {
			t.blockCache.EvictNS(uint64(fd.Num))
		}
		// Try to reuse file num, useful for discarded transaction.
		t.s.reuseFileNum(fd.Num)
	})
}

// Closes the table ops instance. It will close all tables,
// regadless still used or not.
func (t *tOps) close() {
	t.fileCache.Close(true)
	if t.blockCache != nil {
		t.blockCache.Close(false)
	}
}

// Creates new initialized table ops instance.
func newTableOps(s *session) *tOps {
	var (
		fileCacher  cache.Cacher
		blockCache  *cache.Cache
		blockBuffer *util.BufferPool
	)
	if s.o.GetOpenFilesCacheCapacity() > 0 {
		fileCacher = s.o.GetOpenFilesCacher().New(s.o.GetOpenFilesCacheCapacity())
	}
	if !s.o.GetDisableBlockCache() {
		var blockCacher cache.Cacher
		if s.o.GetBlockCacheCapacity() > 0 {
			blockCacher = s.o.GetBlockCacher().New(s.o.GetBlockCacheCapacity())
		}
		blockCache = cache.NewCache(blockCacher)
	}
	if !s.o.GetDisableBufferPool() {
		blockBuffer = util.NewBufferPool(s.o.GetBlockSize() + 5)
	}
	return &tOps{
		s:            s,
		noSync:       s.o.GetNoSync(),
		evictRemoved: s.o.GetBlockCacheEvictRemoved(),
		fileCache:    cache.NewCache(fileCacher),
		blockCache:   blockCache,
		blockBuffer:  blockBuffer,
	}
}

// tWriter wraps the table writer. It keep track of file descriptor
// and added key range.
type tWriter struct {
	t *tOps

	fd storage.FileDesc
	w  storage.Writer
	tw *table.Writer

	first, last []byte
}

// Append key/value pair to the table.
func (w *tWriter) append(key, value []byte) error {
	if w.first == nil {
		w.first = append([]byte(nil), key...)
	}
	w.last = append(w.last[:0], key...)
	return w.tw.Append(key, value)
}

// Returns true if the table is empty.
func (w *tWriter) empty() bool {
	return w.first == nil
}

// Closes the storage.Writer.
func (w *tWriter) close() error {
	if w.w != nil {
		if err := w.w.Close(); err != nil {
			return err
		}
		w.w = nil
	}
	return nil
}

// Finalizes the table and returns table file.
func (w *tWriter) finish() (f *tFile, err error) {
	defer func() {
		if cerr := w.close(); cerr != nil {
			if err == nil {
				err = cerr
			} else {
				err = fmt.Errorf("error opening file (%v); error unlocking file (%v)", err, cerr)
			}
		}
	}()
	err = w.tw.Close()
	if err != nil {
		return
	}
	if !w.t.noSync {
		err = w.w.Sync()
		if err != nil {
			return
		}
	}
	f = newTableFile(w.fd, int64(w.tw.BytesLen()), internalKey(w.first), internalKey(w.last))
	return
}

// Drops the table.
func (w *tWriter) drop() error {
	if err := w.close(); err != nil {
		return err
	}
	w.tw = nil
	w.first = nil
	w.last = nil
	if err := w.t.s.stor.Remove(w.fd); err != nil {
		return err
	}
	w.t.s.reuseFileNum(w.fd.Num)
	return nil
}
```

## File: `leveldb/table_test.go`
```go
// Copyright (c) 2019, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"encoding/binary"
	"math/rand"
	"reflect"
	"testing"

	"github.com/onsi/gomega"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/testutil"
)

func TestGetOverlaps(t *testing.T) {
	gomega.RegisterTestingT(t)
	stor := testutil.NewStorage()
	defer stor.Close()
	s, err := newSession(stor, nil)
	if err != nil {
		t.Fatal(err)
	}

	v := newVersion(s)
	v.newStaging()

	tmp := make([]byte, 4)
	mik := func(i uint64, typ keyType, ukey bool) []byte {
		if i == 0 {
			return nil
		}
		binary.BigEndian.PutUint32(tmp, uint32(i))
		if ukey {
			key := make([]byte, 4)
			copy(key, tmp)
			return key
		}
		return []byte(makeInternalKey(nil, tmp, 0, typ))
	}

	rec := &sessionRecord{}
	for i, f := range []struct {
		min   uint64
		max   uint64
		level int
	}{
		// Overlapped level 0 files
		{1, 8, 0},
		{4, 5, 0},
		{6, 10, 0},
		// Non-overlapped level 1 files
		{2, 3, 1},
		{8, 10, 1},
		{13, 13, 1},
		{20, 100, 1},
	} {
		rec.addTable(f.level, int64(i), 1, mik(f.min, keyTypeVal, false), mik(f.max, keyTypeVal, false))
	}
	vs := v.newStaging()
	vs.commit(rec)
	v = vs.finish(false)

	for i, x := range []struct {
		min      uint64
		max      uint64
		level    int
		expected []int64
	}{
		// Level0 cases
		{0, 0, 0, []int64{2, 1, 0}},
		{1, 0, 0, []int64{2, 1, 0}},
		{0, 10, 0, []int64{2, 1, 0}},
		{2, 7, 0, []int64{2, 1, 0}},

		// Level1 cases
		{1, 1, 1, nil},
		{0, 100, 1, []int64{3, 4, 5, 6}},
		{5, 0, 1, []int64{4, 5, 6}},
		{5, 4, 1, nil}, // invalid search space
		{1, 13, 1, []int64{3, 4, 5}},
		{2, 13, 1, []int64{3, 4, 5}},
		{3, 13, 1, []int64{3, 4, 5}},
		{4, 13, 1, []int64{4, 5}},
		{4, 19, 1, []int64{4, 5}},
		{4, 20, 1, []int64{4, 5, 6}},
		{4, 100, 1, []int64{4, 5, 6}},
		{4, 105, 1, []int64{4, 5, 6}},
	} {
		tf := v.levels[x.level]
		res := tf.getOverlaps(nil, s.icmp, mik(x.min, keyTypeSeek, true), mik(x.max, keyTypeSeek, true), x.level == 0)

		var fnums []int64
		for _, f := range res {
			fnums = append(fnums, f.fd.Num)
		}
		if !reflect.DeepEqual(x.expected, fnums) {
			t.Errorf("case %d failed, expected %v, got %v", i, x.expected, fnums)
		}
	}
}

func BenchmarkGetOverlapLevel0(b *testing.B) {
	benchmarkGetOverlap(b, 0, 500000)
}

func BenchmarkGetOverlapNonLevel0(b *testing.B) {
	benchmarkGetOverlap(b, 1, 500000)
}

func benchmarkGetOverlap(b *testing.B, level int, size int) {
	stor := storage.NewMemStorage()
	defer stor.Close()
	s, err := newSession(stor, nil)
	if err != nil {
		b.Fatal(err)
	}

	v := newVersion(s)
	v.newStaging()

	tmp := make([]byte, 4)
	mik := func(i uint64, typ keyType, ukey bool) []byte {
		if i == 0 {
			return nil
		}
		binary.BigEndian.PutUint32(tmp, uint32(i))
		if ukey {
			key := make([]byte, 4)
			copy(key, tmp)
			return key
		}
		return []byte(makeInternalKey(nil, tmp, 0, typ))
	}

	rec := &sessionRecord{}
	for i := 1; i <= size; i++ {
		min := mik(uint64(2*i), keyTypeVal, false)
		max := mik(uint64(2*i+1), keyTypeVal, false)
		rec.addTable(level, int64(i), 1, min, max)
	}
	vs := v.newStaging()
	vs.commit(rec)
	v = vs.finish(false)

	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		files := v.levels[level]
		start := rand.Intn(size)
		end := rand.Intn(size-start) + start
		files.getOverlaps(nil, s.icmp, mik(uint64(2*start), keyTypeVal, true), mik(uint64(2*end), keyTypeVal, true), level == 0)
	}
}
```

## File: `leveldb/testutil_test.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/testutil"
	"github.com/syndtr/goleveldb/leveldb/util"
)

type testingDB struct {
	*DB
	ro   *opt.ReadOptions
	wo   *opt.WriteOptions
	stor *testutil.Storage
}

func (t *testingDB) TestPut(key []byte, value []byte) error {
	return t.Put(key, value, t.wo)
}

func (t *testingDB) TestDelete(key []byte) error {
	return t.Delete(key, t.wo)
}

func (t *testingDB) TestGet(key []byte) (value []byte, err error) {
	return t.Get(key, t.ro)
}

func (t *testingDB) TestHas(key []byte) (ret bool, err error) {
	return t.Has(key, t.ro)
}

func (t *testingDB) TestNewIterator(slice *util.Range) iterator.Iterator {
	return t.NewIterator(slice, t.ro)
}

func (t *testingDB) TestClose() {
	err := t.Close()
	ExpectWithOffset(1, err).NotTo(HaveOccurred())
	err = t.stor.Close()
	ExpectWithOffset(1, err).NotTo(HaveOccurred())
}

func newTestingDB(o *opt.Options, ro *opt.ReadOptions, wo *opt.WriteOptions) *testingDB {
	stor := testutil.NewStorage()
	db, err := Open(stor, o)
	// FIXME: This may be called from outside It, which may cause panic.
	Expect(err).NotTo(HaveOccurred())
	return &testingDB{
		DB:   db,
		ro:   ro,
		wo:   wo,
		stor: stor,
	}
}

type testingTransaction struct {
	*Transaction
	ro *opt.ReadOptions
	wo *opt.WriteOptions
}

func (t *testingTransaction) TestPut(key []byte, value []byte) error {
	return t.Put(key, value, t.wo)
}

func (t *testingTransaction) TestDelete(key []byte) error {
	return t.Delete(key, t.wo)
}

func (t *testingTransaction) TestGet(key []byte) (value []byte, err error) {
	return t.Get(key, t.ro)
}

func (t *testingTransaction) TestHas(key []byte) (ret bool, err error) {
	return t.Has(key, t.ro)
}

func (t *testingTransaction) TestNewIterator(slice *util.Range) iterator.Iterator {
	return t.NewIterator(slice, t.ro)
}

func (t *testingTransaction) TestClose() {}
```

## File: `leveldb/util.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"fmt"
	"sort"

	"github.com/syndtr/goleveldb/leveldb/storage"
)

func shorten(str string) string {
	if len(str) <= 8 {
		return str
	}
	return str[:3] + ".." + str[len(str)-3:]
}

var bunits = [...]string{"", "Ki", "Mi", "Gi", "Ti"}

func shortenb(bytes int64) string {
	i := 0
	for ; bytes > 1024 && i < 4; i++ {
		bytes /= 1024
	}
	return fmt.Sprintf("%d%sB", bytes, bunits[i])
}

func sshortenb(bytes int64) string {
	if bytes == 0 {
		return "~"
	}
	sign := "+"
	if bytes < 0 {
		sign = "-"
		bytes *= -1
	}
	i := 0
	for ; bytes > 1024 && i < 4; i++ {
		bytes /= 1024
	}
	return fmt.Sprintf("%s%d%sB", sign, bytes, bunits[i])
}

func sint(x int) string {
	if x == 0 {
		return "~"
	}
	sign := "+"
	if x < 0 {
		sign = "-"
		x *= -1
	}
	return fmt.Sprintf("%s%d", sign, x)
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

type fdSorter []storage.FileDesc

func (p fdSorter) Len() int {
	return len(p)
}

func (p fdSorter) Less(i, j int) bool {
	return p[i].Num < p[j].Num
}

func (p fdSorter) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func sortFds(fds []storage.FileDesc) {
	sort.Sort(fdSorter(fds))
}

func ensureBuffer(b []byte, n int) []byte {
	if cap(b) < n {
		return make([]byte, n)
	}
	return b[:n]
}
```

## File: `leveldb/version.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package leveldb

import (
	"fmt"
	"sync/atomic"
	"time"
	"unsafe"

	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/util"
)

type tSet struct {
	level int
	table *tFile
}

type version struct {
	id int64 // unique monotonous increasing version id
	s  *session

	levels []tFiles

	// Level that should be compacted next and its compaction score.
	// Score < 1 means compaction is not strictly needed. These fields
	// are initialized by computeCompaction()
	cLevel int
	cScore float64

	cSeek unsafe.Pointer

	closing  bool
	ref      int
	released bool
}

// newVersion creates a new version with an unique monotonous increasing id.
func newVersion(s *session) *version {
	id := atomic.AddInt64(&s.ntVersionID, 1)
	nv := &version{s: s, id: id - 1}
	return nv
}

func (v *version) incref() {
	if v.released {
		panic("already released")
	}

	v.ref++
	if v.ref == 1 {
		select {
		case v.s.refCh <- &vTask{vid: v.id, files: v.levels, created: time.Now()}:
			// We can use v.levels directly here since it is immutable.
		case <-v.s.closeC:
			v.s.log("reference loop already exist")
		}
	}
}

func (v *version) releaseNB() {
	v.ref--
	if v.ref > 0 {
		return
	} else if v.ref < 0 {
		panic("negative version ref")
	}
	select {
	case v.s.relCh <- &vTask{vid: v.id, files: v.levels, created: time.Now()}:
		// We can use v.levels directly here since it is immutable.
	case <-v.s.closeC:
		v.s.log("reference loop already exist")
	}

	v.released = true
}

func (v *version) release() {
	v.s.vmu.Lock()
	v.releaseNB()
	v.s.vmu.Unlock()
}

func (v *version) walkOverlapping(aux tFiles, ikey internalKey, f func(level int, t *tFile) bool, lf func(level int) bool) {
	ukey := ikey.ukey()

	// Aux level.
	if aux != nil {
		for _, t := range aux {
			if t.overlaps(v.s.icmp, ukey, ukey) {
				if !f(-1, t) {
					return
				}
			}
		}

		if lf != nil && !lf(-1) {
			return
		}
	}

	// Walk tables level-by-level.
	for level, tables := range v.levels {
		if len(tables) == 0 {
			continue
		}

		if level == 0 {
			// Level-0 files may overlap each other. Find all files that
			// overlap ukey.
			for _, t := range tables {
				if t.overlaps(v.s.icmp, ukey, ukey) {
					if !f(level, t) {
						return
					}
				}
			}
		} else {
			if i := tables.searchMax(v.s.icmp, ikey); i < len(tables) {
				t := tables[i]
				if v.s.icmp.uCompare(ukey, t.imin.ukey()) >= 0 {
					if !f(level, t) {
						return
					}
				}
			}
		}

		if lf != nil && !lf(level) {
			return
		}
	}
}

func (v *version) get(aux tFiles, ikey internalKey, ro *opt.ReadOptions, noValue bool) (value []byte, tcomp bool, err error) {
	if v.closing {
		return nil, false, ErrClosed
	}

	ukey := ikey.ukey()
	sampleSeeks := !v.s.o.GetDisableSeeksCompaction()

	var (
		tset  *tSet
		tseek bool

		// Level-0.
		zfound bool
		zseq   uint64
		zkt    keyType
		zval   []byte
	)

	err = ErrNotFound

	// Since entries never hop across level, finding key/value
	// in smaller level make later levels irrelevant.
	v.walkOverlapping(aux, ikey, func(level int, t *tFile) bool {
		if sampleSeeks && level >= 0 && !tseek {
			if tset == nil {
				tset = &tSet{level, t}
			} else {
				tseek = true
			}
		}

		var (
			fikey, fval []byte
			ferr        error
		)
		if noValue {
			fikey, ferr = v.s.tops.findKey(t, ikey, ro)
		} else {
			fikey, fval, ferr = v.s.tops.find(t, ikey, ro)
		}

		switch ferr {
		case nil:
		case ErrNotFound:
			return true
		default:
			err = ferr
			return false
		}

		if fukey, fseq, fkt, fkerr := parseInternalKey(fikey); fkerr == nil {
			if v.s.icmp.uCompare(ukey, fukey) == 0 {
				// Level <= 0 may overlaps each-other.
				if level <= 0 {
					if fseq >= zseq {
						zfound = true
						zseq = fseq
						zkt = fkt
						zval = fval
					}
				} else {
					switch fkt {
					case keyTypeVal:
						value = fval
						err = nil
					case keyTypeDel:
					default:
						panic("leveldb: invalid internalKey type")
					}
					return false
				}
			}
		} else {
			err = fkerr
			return false
		}

		return true
	}, func(level int) bool {
		if zfound {
			switch zkt {
			case keyTypeVal:
				value = zval
				err = nil
			case keyTypeDel:
			default:
				panic("leveldb: invalid internalKey type")
			}
			return false
		}

		return true
	})

	if tseek && tset.table.consumeSeek() <= 0 {
		tcomp = atomic.CompareAndSwapPointer(&v.cSeek, nil, unsafe.Pointer(tset))
	}

	return
}

func (v *version) sampleSeek(ikey internalKey) (tcomp bool) {
	var tset *tSet

	v.walkOverlapping(nil, ikey, func(level int, t *tFile) bool {
		if tset == nil {
			tset = &tSet{level, t}
			return true
		}
		if tset.table.consumeSeek() <= 0 {
			tcomp = atomic.CompareAndSwapPointer(&v.cSeek, nil, unsafe.Pointer(tset))
		}
		return false
	}, nil)

	return
}

func (v *version) getIterators(slice *util.Range, ro *opt.ReadOptions) (its []iterator.Iterator) {
	strict := opt.GetStrict(v.s.o.Options, ro, opt.StrictReader)
	for level, tables := range v.levels {
		if level == 0 {
			// Merge all level zero files together since they may overlap.
			for _, t := range tables {
				its = append(its, v.s.tops.newIterator(t, slice, ro))
			}
		} else if len(tables) != 0 {
			its = append(its, iterator.NewIndexedIterator(tables.newIndexIterator(v.s.tops, v.s.icmp, slice, ro), strict))
		}
	}
	return
}

func (v *version) newStaging() *versionStaging {
	return &versionStaging{base: v}
}

// Spawn a new version based on this version.
func (v *version) spawn(r *sessionRecord, trivial bool) *version {
	staging := v.newStaging()
	staging.commit(r)
	return staging.finish(trivial)
}

func (v *version) fillRecord(r *sessionRecord) {
	for level, tables := range v.levels {
		for _, t := range tables {
			r.addTableFile(level, t)
		}
	}
}

func (v *version) tLen(level int) int {
	if level < len(v.levels) {
		return len(v.levels[level])
	}
	return 0
}

func (v *version) offsetOf(ikey internalKey) (n int64, err error) {
	for level, tables := range v.levels {
		for _, t := range tables {
			if v.s.icmp.Compare(t.imax, ikey) <= 0 {
				// Entire file is before "ikey", so just add the file size
				n += t.size
			} else if v.s.icmp.Compare(t.imin, ikey) > 0 {
				// Entire file is after "ikey", so ignore
				if level > 0 {
					// Files other than level 0 are sorted by meta->min, so
					// no further files in this level will contain data for
					// "ikey".
					break
				}
			} else {
				// "ikey" falls in the range for this table. Add the
				// approximate offset of "ikey" within the table.
				if m, err := v.s.tops.offsetOf(t, ikey); err == nil {
					n += m
				} else {
					return 0, err
				}
			}
		}
	}

	return
}

func (v *version) pickMemdbLevel(umin, umax []byte, maxLevel int) (level int) {
	if maxLevel > 0 {
		if len(v.levels) == 0 {
			return maxLevel
		}
		if !v.levels[0].overlaps(v.s.icmp, umin, umax, true) {
			var overlaps tFiles
			for ; level < maxLevel; level++ {
				if pLevel := level + 1; pLevel >= len(v.levels) {
					return maxLevel
				} else if v.levels[pLevel].overlaps(v.s.icmp, umin, umax, false) {
					break
				}
				if gpLevel := level + 2; gpLevel < len(v.levels) {
					overlaps = v.levels[gpLevel].getOverlaps(overlaps, v.s.icmp, umin, umax, false)
					if overlaps.size() > int64(v.s.o.GetCompactionGPOverlaps(level)) {
						break
					}
				}
			}
		}
	}
	return
}

func (v *version) computeCompaction() {
	// Precomputed best level for next compaction
	bestLevel := int(-1)
	bestScore := float64(-1)

	statFiles := make([]int, len(v.levels))
	statSizes := make([]string, len(v.levels))
	statScore := make([]string, len(v.levels))
	statTotSize := int64(0)

	for level, tables := range v.levels {
		var score float64
		size := tables.size()
		if level == 0 {
			// We treat level-0 specially by bounding the number of files
			// instead of number of bytes for two reasons:
			//
			// (1) With larger write-buffer sizes, it is nice not to do too
			// many level-0 compaction.
			//
			// (2) The files in level-0 are merged on every read and
			// therefore we wish to avoid too many files when the individual
			// file size is small (perhaps because of a small write-buffer
			// setting, or very high compression ratios, or lots of
			// overwrites/deletions).
			score = float64(len(tables)) / float64(v.s.o.GetCompactionL0Trigger())
		} else {
			score = float64(size) / float64(v.s.o.GetCompactionTotalSize(level))
		}

		if score > bestScore {
			bestLevel = level
			bestScore = score
		}

		statFiles[level] = len(tables)
		statSizes[level] = shortenb(size)
		statScore[level] = fmt.Sprintf("%.2f", score)
		statTotSize += size
	}

	v.cLevel = bestLevel
	v.cScore = bestScore

	v.s.logf("version@stat F·%v S·%s%v Sc·%v", statFiles, shortenb(statTotSize), statSizes, statScore)
}

func (v *version) needCompaction() bool {
	return v.cScore >= 1 || atomic.LoadPointer(&v.cSeek) != nil
}

type tablesScratch struct {
	added   map[int64]atRecord
	deleted map[int64]struct{}
}

type versionStaging struct {
	base   *version
	levels []tablesScratch
}

func (p *versionStaging) getScratch(level int) *tablesScratch {
	if level >= len(p.levels) {
		newLevels := make([]tablesScratch, level+1)
		copy(newLevels, p.levels)
		p.levels = newLevels
	}
	return &(p.levels[level])
}

func (p *versionStaging) commit(r *sessionRecord) {
	// Deleted tables.
	for _, r := range r.deletedTables {
		scratch := p.getScratch(r.level)
		if r.level < len(p.base.levels) && len(p.base.levels[r.level]) > 0 {
			if scratch.deleted == nil {
				scratch.deleted = make(map[int64]struct{})
			}
			scratch.deleted[r.num] = struct{}{}
		}
		if scratch.added != nil {
			delete(scratch.added, r.num)
		}
	}

	// New tables.
	for _, r := range r.addedTables {
		scratch := p.getScratch(r.level)
		if scratch.added == nil {
			scratch.added = make(map[int64]atRecord)
		}
		scratch.added[r.num] = r
		if scratch.deleted != nil {
			delete(scratch.deleted, r.num)
		}
	}
}

func (p *versionStaging) finish(trivial bool) *version {
	// Build new version.
	nv := newVersion(p.base.s)
	numLevel := len(p.levels)
	if len(p.base.levels) > numLevel {
		numLevel = len(p.base.levels)
	}
	nv.levels = make([]tFiles, numLevel)
	for level := 0; level < numLevel; level++ {
		var baseTabels tFiles
		if level < len(p.base.levels) {
			baseTabels = p.base.levels[level]
		}

		if level < len(p.levels) {
			scratch := p.levels[level]

			// Short circuit if there is no change at all.
			if len(scratch.added) == 0 && len(scratch.deleted) == 0 {
				nv.levels[level] = baseTabels
				continue
			}

			var nt tFiles
			// Prealloc list if possible.
			if n := len(baseTabels) + len(scratch.added) - len(scratch.deleted); n > 0 {
				nt = make(tFiles, 0, n)
			}

			// Base tables.
			for _, t := range baseTabels {
				if _, ok := scratch.deleted[t.fd.Num]; ok {
					continue
				}
				if _, ok := scratch.added[t.fd.Num]; ok {
					continue
				}
				nt = append(nt, t)
			}

			// Avoid resort if only files in this level are deleted
			if len(scratch.added) == 0 {
				nv.levels[level] = nt
				continue
			}

			// For normal table compaction, one compaction will only involve two levels
			// of files. And the new files generated after merging the source level and
			// source+1 level related files can be inserted as a whole into source+1 level
			// without any overlap with the other source+1 files.
			//
			// When the amount of data maintained by leveldb is large, the number of files
			// per level will be very large. While qsort is very inefficient for sorting
			// already ordered arrays. Therefore, for the normal table compaction, we use
			// binary search here to find the insert index to insert a batch of new added
			// files directly instead of using qsort.
			if trivial && len(scratch.added) > 0 {
				added := make(tFiles, 0, len(scratch.added))
				for _, r := range scratch.added {
					added = append(added, tableFileFromRecord(r))
				}
				if level == 0 {
					added.sortByNum()
					index := nt.searchNumLess(added[len(added)-1].fd.Num)
					nt = append(nt[:index], append(added, nt[index:]...)...)
				} else {
					added.sortByKey(p.base.s.icmp)
					_, amax := added.getRange(p.base.s.icmp)
					index := nt.searchMin(p.base.s.icmp, amax)
					nt = append(nt[:index], append(added, nt[index:]...)...)
				}
				nv.levels[level] = nt
				continue
			}

			// New tables.
			for _, r := range scratch.added {
				nt = append(nt, tableFileFromRecord(r))
			}

			if len(nt) != 0 {
				// Sort tables.
				if level == 0 {
					nt.sortByNum()
				} else {
					nt.sortByKey(p.base.s.icmp)
				}

				nv.levels[level] = nt
			}
		} else {
			nv.levels[level] = baseTabels
		}
	}

	// Trim levels.
	n := len(nv.levels)
	for ; n > 0 && nv.levels[n-1] == nil; n-- {
	}
	nv.levels = nv.levels[:n]

	// Compute compaction score for new version.
	nv.computeCompaction()

	return nv
}

type versionReleaser struct {
	v    *version
	once bool
}

func (vr *versionReleaser) Release() {
	v := vr.v
	v.s.vmu.Lock()
	if !vr.once {
		v.releaseNB()
		vr.once = true
	}
	v.s.vmu.Unlock()
}
```

## File: `leveldb/version_test.go`
```go
package leveldb

import (
	"encoding/binary"
	"math/rand"
	"reflect"
	"sync"
	"testing"
	"time"

	"github.com/onsi/gomega"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/testutil"
)

type testFileRec struct {
	level int
	num   int64
}

func TestVersionStaging(t *testing.T) {
	gomega.RegisterTestingT(t)
	stor := testutil.NewStorage()
	defer stor.Close()
	s, err := newSession(stor, nil)
	if err != nil {
		t.Fatal(err)
	}
	defer func() {
		s.close()
		s.release()
	}()

	v := newVersion(s)
	v.newStaging()

	tmp := make([]byte, 4)
	mik := func(i uint64) []byte {
		binary.BigEndian.PutUint32(tmp, uint32(i))
		return []byte(makeInternalKey(nil, tmp, 0, keyTypeVal))
	}

	for i, x := range []struct {
		add, del []testFileRec
		trivial  bool
		levels   [][]int64
	}{
		{
			add: []testFileRec{
				{1, 1},
			},
			levels: [][]int64{
				{},
				{1},
			},
		},
		{
			add: []testFileRec{
				{1, 1},
			},
			levels: [][]int64{
				{},
				{1},
			},
		},
		{
			del: []testFileRec{
				{1, 1},
			},
			levels: [][]int64{},
		},
		{
			add: []testFileRec{
				{0, 1},
				{0, 3},
				{0, 2},
				{2, 5},
				{1, 4},
			},
			levels: [][]int64{
				{3, 2, 1},
				{4},
				{5},
			},
		},
		{
			add: []testFileRec{
				{1, 6},
				{2, 5},
			},
			del: []testFileRec{
				{0, 1},
				{0, 4},
			},
			levels: [][]int64{
				{3, 2},
				{4, 6},
				{5},
			},
		},
		{
			del: []testFileRec{
				{0, 3},
				{0, 2},
				{1, 4},
				{1, 6},
				{2, 5},
			},
			levels: [][]int64{},
		},
		{
			add: []testFileRec{
				{0, 1},
			},
			levels: [][]int64{
				{1},
			},
		},
		{
			add: []testFileRec{
				{1, 2},
			},
			levels: [][]int64{
				{1},
				{2},
			},
		},
		{
			add: []testFileRec{
				{0, 3},
			},
			levels: [][]int64{
				{3, 1},
				{2},
			},
		},
		{
			add: []testFileRec{
				{6, 9},
			},
			levels: [][]int64{
				{3, 1},
				{2},
				{},
				{},
				{},
				{},
				{9},
			},
		},
		{
			del: []testFileRec{
				{6, 9},
			},
			levels: [][]int64{
				{3, 1},
				{2},
			},
		},
		// memory compaction
		{
			add: []testFileRec{
				{0, 5},
			},
			trivial: true,
			levels: [][]int64{
				{5, 3, 1},
				{2},
			},
		},
		// memory compaction
		{
			add: []testFileRec{
				{0, 4},
			},
			trivial: true,
			levels: [][]int64{
				{5, 4, 3, 1},
				{2},
			},
		},
		// table compaction
		{
			add: []testFileRec{
				{1, 6},
				{1, 7},
				{1, 8},
			},
			del: []testFileRec{
				{0, 3},
				{0, 4},
				{0, 5},
			},
			trivial: true,
			levels: [][]int64{
				{1},
				{2, 6, 7, 8},
			},
		},
	} {
		rec := &sessionRecord{}
		for _, f := range x.add {
			ik := mik(uint64(f.num))
			rec.addTable(f.level, f.num, 1, ik, ik)
		}
		for _, f := range x.del {
			rec.delTable(f.level, f.num)
		}
		vs := v.newStaging()
		vs.commit(rec)
		v = vs.finish(x.trivial)
		if len(v.levels) != len(x.levels) {
			t.Fatalf("#%d: invalid level count: want=%d got=%d", i, len(x.levels), len(v.levels))
		}
		for j, want := range x.levels {
			tables := v.levels[j]
			if len(want) != len(tables) {
				t.Fatalf("#%d.%d: invalid tables count: want=%d got=%d", i, j, len(want), len(tables))
			}
			got := make([]int64, len(tables))
			for k, t := range tables {
				got[k] = t.fd.Num
			}
			if !reflect.DeepEqual(want, got) {
				t.Fatalf("#%d.%d: invalid tables: want=%v got=%v", i, j, want, got)
			}
		}
	}
}

func TestVersionReference(t *testing.T) {
	gomega.RegisterTestingT(t)
	stor := testutil.NewStorage()
	defer stor.Close()
	s, err := newSession(stor, nil)
	if err != nil {
		t.Fatal(err)
	}
	defer func() {
		s.close()
		s.release()
	}()

	tmp := make([]byte, 4)
	mik := func(i uint64) []byte {
		binary.BigEndian.PutUint32(tmp, uint32(i))
		return []byte(makeInternalKey(nil, tmp, 0, keyTypeVal))
	}

	// Test normal version task correctness
	refc := make(chan map[int64]int)

	for i, x := range []struct {
		add, del []testFileRec
		expect   map[int64]int
		failed   bool
	}{
		{
			[]testFileRec{{0, 1}, {0, 2}},
			nil,
			map[int64]int{1: 1, 2: 1},
			false,
		},
		{
			[]testFileRec{{0, 3}, {0, 4}},
			[]testFileRec{{0, 1}},
			map[int64]int{2: 1, 3: 1, 4: 1},
			false,
		},
		{
			[]testFileRec{{0, 1}, {0, 5}, {0, 6}, {0, 7}},
			[]testFileRec{{0, 2}, {0, 3}, {0, 4}},
			map[int64]int{1: 1, 5: 1, 6: 1, 7: 1},
			false,
		},
		{
			nil,
			nil,
			map[int64]int{1: 1, 5: 1, 6: 1, 7: 1},
			true,
		},
		{
			[]testFileRec{{0, 1}, {0, 5}, {0, 6}, {0, 7}},
			nil,
			map[int64]int{1: 2, 5: 2, 6: 2, 7: 2},
			false,
		},
		{
			nil,
			[]testFileRec{{0, 1}, {0, 5}, {0, 6}, {0, 7}},
			map[int64]int{1: 1, 5: 1, 6: 1, 7: 1},
			false,
		},
		{
			[]testFileRec{{0, 0}},
			[]testFileRec{{0, 1}, {0, 5}, {0, 6}, {0, 7}},
			map[int64]int{0: 1},
			false,
		},
	} {
		rec := &sessionRecord{}
		for n, f := range x.add {
			rec.addTable(f.level, f.num, 1, mik(uint64(i+n)), mik(uint64(i+n)))
		}
		for _, f := range x.del {
			rec.delTable(f.level, f.num)
		}

		// Simulate some read operations
		var wg sync.WaitGroup
		readN := rand.Intn(300)
		for i := 0; i < readN; i++ {
			wg.Add(1)
			go func() {
				v := s.version()
				time.Sleep(time.Millisecond * time.Duration(rand.Intn(300)))
				v.release()
				wg.Done()
			}()
		}

		v := s.version()
		vs := v.newStaging()
		vs.commit(rec)
		nv := vs.finish(false)

		if x.failed {
			s.abandon <- nv.id
		} else {
			s.setVersion(rec, nv)
		}
		v.release()

		// Wait all read operations
		wg.Wait()

		time.Sleep(100 * time.Millisecond) // Wait lazy reference finish tasks

		s.fileRefCh <- refc
		ref := <-refc
		if !reflect.DeepEqual(ref, x.expect) {
			t.Errorf("case %d failed, file reference mismatch, GOT %v, WANT %v", i, ref, x.expect)
		}
	}

	// Test version task overflow
	var longV = s.version() // This version is held by some long-time operation
	var exp = map[int64]int{0: 1, maxCachedNumber: 1}
	for i := 1; i <= maxCachedNumber; i++ {
		rec := &sessionRecord{}
		rec.addTable(0, int64(i), 1, mik(uint64(i)), mik(uint64(i)))
		rec.delTable(0, int64(i-1))
		v := s.version()
		vs := v.newStaging()
		vs.commit(rec)
		nv := vs.finish(false)
		s.setVersion(rec, nv)
		v.release()
	}
	time.Sleep(100 * time.Millisecond) // Wait lazy reference finish tasks

	s.fileRefCh <- refc
	ref := <-refc
	if !reflect.DeepEqual(exp, ref) {
		t.Errorf("file reference mismatch, GOT %v, WANT %v", ref, exp)
	}

	longV.release()
	s.fileRefCh <- refc
	ref = <-refc
	delete(exp, 0)
	if !reflect.DeepEqual(exp, ref) {
		t.Errorf("file reference mismatch, GOT %v, WANT %v", ref, exp)
	}
}

func BenchmarkVersionStagingNonTrivial(b *testing.B) {
	benchmarkVersionStaging(b, false, 100000)
}

func BenchmarkVersionStagingTrivial(b *testing.B) {
	benchmarkVersionStaging(b, true, 100000)
}

func benchmarkVersionStaging(b *testing.B, trivial bool, size int) {
	stor := storage.NewMemStorage()
	defer stor.Close()
	s, err := newSession(stor, nil)
	if err != nil {
		b.Fatal(err)
	}
	defer func() {
		s.close()
		s.release()
	}()

	tmp := make([]byte, 4)
	mik := func(i uint64) []byte {
		binary.BigEndian.PutUint32(tmp, uint32(i))
		return []byte(makeInternalKey(nil, tmp, 0, keyTypeVal))
	}

	rec := &sessionRecord{}
	for i := 0; i < size; i++ {
		ik := mik(uint64(i))
		rec.addTable(1, int64(i), 1, ik, ik)
	}

	v := newVersion(s)
	vs := v.newStaging()
	vs.commit(rec)
	v = vs.finish(false)

	b.ResetTimer()
	b.ReportAllocs()

	for i := 0; i < b.N; i++ {
		rec := &sessionRecord{}
		index := rand.Intn(size)
		ik := mik(uint64(index))

		cnt := 0
		for j := index; j < size && cnt <= 3; j++ {
			rec.addTable(1, int64(i), 1, ik, ik)
			cnt++
		}
		vs := v.newStaging()
		vs.commit(rec)
		vs.finish(trivial)
	}
}
```

## File: `leveldb/cache/bench_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package cache

import (
	"sync/atomic"
	"testing"
)

func BenchmarkCache_InsertRemove(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		}).Release()
	}
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCache_Insert(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCache_Lookup(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)
	for i := 0; i < b.N; i++ {
		c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		c.Get(0, uint64(i), nil).Release()
	}
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCache_AppendRemove(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)
	for i := 0; i < b.N; i++ {
		c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		c.Get(1, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		}).Release()
	}
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCache_Append(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)
	for i := 0; i < b.N; i++ {
		c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		c.Get(1, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCache_Delete(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)
	handles := make([]*Handle, b.N)
	for i := 0; i < b.N; i++ {
		handles[i] = c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		handles[i].Release()
	}
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCacheParallel_Insert(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)

	var ns uint64
	b.StartTimer()
	b.RunParallel(func(pb *testing.PB) {
		ns := atomic.AddUint64(&ns, 1)
		i := uint64(0)
		for pb.Next() {
			c.Get(ns, i, func() (int, Value) {
				return 1, i
			})
			i++
		}
	})
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCacheParallel_Lookup(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)
	for i := 0; i < b.N; i++ {
		c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}

	var counter uint64
	b.StartTimer()
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			i := atomic.AddUint64(&counter, 1) - 1
			c.Get(0, i, nil).Release()
		}
	})
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCacheParallel_Append(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)
	for i := 0; i < b.N; i++ {
		c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}

	var ns uint64
	b.StartTimer()
	b.RunParallel(func(pb *testing.PB) {
		ns := atomic.AddUint64(&ns, 1)
		i := uint64(0)
		for pb.Next() {
			c.Get(ns, i, func() (int, Value) {
				return 1, i
			})
			i++
		}
	})
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}

func BenchmarkCacheParallel_Delete(b *testing.B) {
	b.StopTimer()
	c := NewCache(nil)
	handles := make([]*Handle, b.N)
	for i := 0; i < b.N; i++ {
		handles[i] = c.Get(0, uint64(i), func() (int, Value) {
			return 1, uint64(i)
		})
	}

	var counter int64
	b.StartTimer()
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			i := atomic.AddInt64(&counter, 1) - 1
			handles[i].Release()
		}
	})
	b.ReportMetric(float64(c.Nodes()), "nodes")
	b.Logf("STATS: %#v", c.GetStats())
}
```

## File: `leveldb/cache/cache.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package cache provides interface and implementation of a cache algorithms.
package cache

import (
	"sort"
	"sync"
	"sync/atomic"
	"unsafe"

	"github.com/syndtr/goleveldb/leveldb/util"
)

// Cacher provides interface to implements a caching functionality.
// An implementation must be safe for concurrent use.
type Cacher interface {
	// Capacity returns cache capacity.
	Capacity() int

	// SetCapacity sets cache capacity.
	SetCapacity(capacity int)

	// Promote promotes the 'cache node'.
	Promote(n *Node)

	// Ban evicts the 'cache node' and prevent subsequent 'promote'.
	Ban(n *Node)

	// Evict evicts the 'cache node'.
	Evict(n *Node)
}

// Value is a 'cache-able object'. It may implements util.Releaser, if
// so the the Release method will be called once object is released.
type Value interface{}

// NamespaceGetter provides convenient wrapper for namespace.
type NamespaceGetter struct {
	Cache *Cache
	NS    uint64
}

// Get simply calls Cache.Get() method.
func (g *NamespaceGetter) Get(key uint64, setFunc func() (size int, value Value)) *Handle {
	return g.Cache.Get(g.NS, key, setFunc)
}

// The hash tables implementation is based on:
// "Dynamic-Sized Nonblocking Hash Tables", by Yujie Liu,
// Kunlong Zhang, and Michael Spear.
// ACM Symposium on Principles of Distributed Computing, Jul 2014.

const (
	mInitialSize           = 1 << 4
	mOverflowThreshold     = 1 << 5
	mOverflowGrowThreshold = 1 << 7
)

const (
	bucketUninitialized = iota
	bucketInitialized
	bucketFrozen
)

type mNodes []*Node

func (x mNodes) Len() int { return len(x) }
func (x mNodes) Less(i, j int) bool {
	a, b := x[i].ns, x[j].ns
	if a == b {
		return x[i].key < x[j].key
	}
	return a < b
}
func (x mNodes) Swap(i, j int) { x[i], x[j] = x[j], x[i] }

func (x mNodes) sort() { sort.Sort(x) }

func (x mNodes) search(ns, key uint64) int {
	return sort.Search(len(x), func(i int) bool {
		a := x[i].ns
		if a == ns {
			return x[i].key >= key
		}
		return a > ns
	})
}

type mBucket struct {
	mu    sync.Mutex
	nodes mNodes
	state int8
}

func (b *mBucket) freeze() mNodes {
	b.mu.Lock()
	defer b.mu.Unlock()
	if b.state == bucketInitialized {
		b.state = bucketFrozen
	} else if b.state == bucketUninitialized {
		panic("BUG: freeze uninitialized bucket")
	}
	return b.nodes
}

func (b *mBucket) frozen() bool {
	if b.state == bucketFrozen {
		return true
	}
	if b.state == bucketUninitialized {
		panic("BUG: accessing uninitialized bucket")
	}
	return false
}

func (b *mBucket) get(r *Cache, h *mHead, hash uint32, ns, key uint64, getOnly bool) (done, created bool, n *Node) {
	b.mu.Lock()

	if b.frozen() {
		b.mu.Unlock()
		return
	}

	// Find the node.
	i := b.nodes.search(ns, key)
	if i < len(b.nodes) {
		n = b.nodes[i]
		if n.ns == ns && n.key == key {
			atomic.AddInt32(&n.ref, 1)
			b.mu.Unlock()
			return true, false, n
		}
	}

	// Get only.
	if getOnly {
		b.mu.Unlock()
		return true, false, nil
	}

	// Create node.
	n = &Node{
		r:    r,
		hash: hash,
		ns:   ns,
		key:  key,
		ref:  1,
	}
	// Add node to bucket.
	if i == len(b.nodes) {
		b.nodes = append(b.nodes, n)
	} else {
		b.nodes = append(b.nodes[:i+1], b.nodes[i:]...)
		b.nodes[i] = n
	}
	bLen := len(b.nodes)
	b.mu.Unlock()

	// Update counter.
	grow := atomic.AddInt64(&r.statNodes, 1) >= h.growThreshold
	if bLen > mOverflowThreshold {
		grow = grow || atomic.AddInt32(&h.overflow, 1) >= mOverflowGrowThreshold
	}

	// Grow.
	if grow && atomic.CompareAndSwapInt32(&h.resizeInProgress, 0, 1) {
		nhLen := len(h.buckets) << 1
		nh := &mHead{
			buckets:         make([]mBucket, nhLen),
			mask:            uint32(nhLen) - 1,
			predecessor:     unsafe.Pointer(h),
			growThreshold:   int64(nhLen * mOverflowThreshold),
			shrinkThreshold: int64(nhLen >> 1),
		}
		ok := atomic.CompareAndSwapPointer(&r.mHead, unsafe.Pointer(h), unsafe.Pointer(nh))
		if !ok {
			panic("BUG: failed swapping head")
		}
		atomic.AddInt32(&r.statGrow, 1)
		go nh.initBuckets()
	}

	return true, true, n
}

func (b *mBucket) delete(r *Cache, h *mHead, hash uint32, ns, key uint64) (done, deleted bool) {
	b.mu.Lock()

	if b.frozen() {
		b.mu.Unlock()
		return
	}

	// Find the node.
	i := b.nodes.search(ns, key)
	if i == len(b.nodes) {
		b.mu.Unlock()
		return true, false
	}
	n := b.nodes[i]
	var bLen int
	if n.ns == ns && n.key == key {
		if atomic.LoadInt32(&n.ref) == 0 {
			deleted = true

			// Save and clear value.
			if n.value != nil {
				// Call releaser.
				if r, ok := n.value.(util.Releaser); ok {
					r.Release()
				}
				n.value = nil
			}

			// Remove node from bucket.
			b.nodes = append(b.nodes[:i], b.nodes[i+1:]...)
			bLen = len(b.nodes)
		}
	}
	b.mu.Unlock()

	if deleted {
		// Call delete funcs.
		for _, f := range n.delFuncs {
			f()
		}

		// Update counter.
		atomic.AddInt64(&r.statSize, int64(n.size)*-1)
		shrink := atomic.AddInt64(&r.statNodes, -1) < h.shrinkThreshold
		if bLen >= mOverflowThreshold {
			atomic.AddInt32(&h.overflow, -1)
		}

		// Shrink.
		if shrink && len(h.buckets) > mInitialSize && atomic.CompareAndSwapInt32(&h.resizeInProgress, 0, 1) {
			nhLen := len(h.buckets) >> 1
			nh := &mHead{
				buckets:         make([]mBucket, nhLen),
				mask:            uint32(nhLen) - 1,
				predecessor:     unsafe.Pointer(h),
				growThreshold:   int64(nhLen * mOverflowThreshold),
				shrinkThreshold: int64(nhLen >> 1),
			}
			ok := atomic.CompareAndSwapPointer(&r.mHead, unsafe.Pointer(h), unsafe.Pointer(nh))
			if !ok {
				panic("BUG: failed swapping head")
			}
			atomic.AddInt32(&r.statShrink, 1)
			go nh.initBuckets()
		}
	}

	return true, deleted
}

type mHead struct {
	buckets          []mBucket
	mask             uint32
	predecessor      unsafe.Pointer // *mNode
	resizeInProgress int32

	overflow        int32
	growThreshold   int64
	shrinkThreshold int64
}

func (h *mHead) initBucket(i uint32) *mBucket {
	b := &h.buckets[i]
	b.mu.Lock()
	if b.state >= bucketInitialized {
		b.mu.Unlock()
		return b
	}

	p := (*mHead)(atomic.LoadPointer(&h.predecessor))
	if p == nil {
		panic("BUG: uninitialized bucket doesn't have predecessor")
	}

	var nodes mNodes
	if h.mask > p.mask {
		// Grow.
		m := p.initBucket(i & p.mask).freeze()
		// Split nodes.
		for _, x := range m {
			if x.hash&h.mask == i {
				nodes = append(nodes, x)
			}
		}
	} else {
		// Shrink.
		m0 := p.initBucket(i).freeze()
		m1 := p.initBucket(i + uint32(len(h.buckets))).freeze()
		// Merge nodes.
		nodes = make(mNodes, 0, len(m0)+len(m1))
		nodes = append(nodes, m0...)
		nodes = append(nodes, m1...)
		nodes.sort()
	}
	b.nodes = nodes
	b.state = bucketInitialized
	b.mu.Unlock()
	return b
}

func (h *mHead) initBuckets() {
	for i := range h.buckets {
		h.initBucket(uint32(i))
	}
	atomic.StorePointer(&h.predecessor, nil)
}

func (h *mHead) enumerateNodesWithCB(f func([]*Node)) {
	var nodes []*Node
	for x := range h.buckets {
		b := h.initBucket(uint32(x))

		b.mu.Lock()
		nodes = append(nodes, b.nodes...)
		b.mu.Unlock()
		f(nodes)
	}
}

func (h *mHead) enumerateNodesByNS(ns uint64) []*Node {
	var nodes []*Node
	for x := range h.buckets {
		b := h.initBucket(uint32(x))

		b.mu.Lock()
		i := b.nodes.search(ns, 0)
		for ; i < len(b.nodes); i++ {
			n := b.nodes[i]
			if n.ns != ns {
				break
			}
			nodes = append(nodes, n)
		}
		b.mu.Unlock()
	}
	return nodes
}

type Stats struct {
	Buckets     int
	Nodes       int64
	Size        int64
	GrowCount   int32
	ShrinkCount int32
	HitCount    int64
	MissCount   int64
	SetCount    int64
	DelCount    int64
}

// Cache is a 'cache map'.
type Cache struct {
	mu     sync.RWMutex
	mHead  unsafe.Pointer // *mNode
	cacher Cacher
	closed bool

	statNodes  int64
	statSize   int64
	statGrow   int32
	statShrink int32
	statHit    int64
	statMiss   int64
	statSet    int64
	statDel    int64
}

// NewCache creates a new 'cache map'. The cacher is optional and
// may be nil.
func NewCache(cacher Cacher) *Cache {
	h := &mHead{
		buckets:         make([]mBucket, mInitialSize),
		mask:            mInitialSize - 1,
		growThreshold:   int64(mInitialSize * mOverflowThreshold),
		shrinkThreshold: 0,
	}
	for i := range h.buckets {
		h.buckets[i].state = bucketInitialized
	}
	r := &Cache{
		mHead:  unsafe.Pointer(h),
		cacher: cacher,
	}
	return r
}

func (r *Cache) getBucket(hash uint32) (*mHead, *mBucket) {
	h := (*mHead)(atomic.LoadPointer(&r.mHead))
	i := hash & h.mask
	return h, h.initBucket(i)
}

func (r *Cache) enumerateNodesWithCB(f func([]*Node)) {
	h := (*mHead)(atomic.LoadPointer(&r.mHead))
	h.enumerateNodesWithCB(f)
}

func (r *Cache) enumerateNodesByNS(ns uint64) []*Node {
	h := (*mHead)(atomic.LoadPointer(&r.mHead))
	return h.enumerateNodesByNS(ns)
}

func (r *Cache) delete(n *Node) bool {
	for {
		h, b := r.getBucket(n.hash)
		done, deleted := b.delete(r, h, n.hash, n.ns, n.key)
		if done {
			return deleted
		}
	}
}

// GetStats returns cache statistics.
func (r *Cache) GetStats() Stats {
	return Stats{
		Buckets:     len((*mHead)(atomic.LoadPointer(&r.mHead)).buckets),
		Nodes:       atomic.LoadInt64(&r.statNodes),
		Size:        atomic.LoadInt64(&r.statSize),
		GrowCount:   atomic.LoadInt32(&r.statGrow),
		ShrinkCount: atomic.LoadInt32(&r.statShrink),
		HitCount:    atomic.LoadInt64(&r.statHit),
		MissCount:   atomic.LoadInt64(&r.statMiss),
		SetCount:    atomic.LoadInt64(&r.statSet),
		DelCount:    atomic.LoadInt64(&r.statDel),
	}
}

// Nodes returns number of 'cache node' in the map.
func (r *Cache) Nodes() int {
	return int(atomic.LoadInt64(&r.statNodes))
}

// Size returns sums of 'cache node' size in the map.
func (r *Cache) Size() int {
	return int(atomic.LoadInt64(&r.statSize))
}

// Capacity returns cache capacity.
func (r *Cache) Capacity() int {
	if r.cacher == nil {
		return 0
	}
	return r.cacher.Capacity()
}

// SetCapacity sets cache capacity.
func (r *Cache) SetCapacity(capacity int) {
	if r.cacher != nil {
		r.cacher.SetCapacity(capacity)
	}
}

// Get gets 'cache node' with the given namespace and key.
// If cache node is not found and setFunc is not nil, Get will atomically creates
// the 'cache node' by calling setFunc. Otherwise Get will returns nil.
//
// The returned 'cache handle' should be released after use by calling Release
// method.
func (r *Cache) Get(ns, key uint64, setFunc func() (size int, value Value)) *Handle {
	r.mu.RLock()
	defer r.mu.RUnlock()
	if r.closed {
		return nil
	}

	hash := murmur32(ns, key, 0xf00)
	for {
		h, b := r.getBucket(hash)
		done, created, n := b.get(r, h, hash, ns, key, setFunc == nil)
		if done {
			if created || n == nil {
				atomic.AddInt64(&r.statMiss, 1)
			} else {
				atomic.AddInt64(&r.statHit, 1)
			}

			if n != nil {
				n.mu.Lock()
				if n.value == nil {
					if setFunc == nil {
						n.mu.Unlock()
						n.unRefInternal(false)
						return nil
					}

					n.size, n.value = setFunc()
					if n.value == nil {
						n.size = 0
						n.mu.Unlock()
						n.unRefInternal(false)
						return nil
					}
					atomic.AddInt64(&r.statSet, 1)
					atomic.AddInt64(&r.statSize, int64(n.size))
				}
				n.mu.Unlock()
				if r.cacher != nil {
					r.cacher.Promote(n)
				}
				return &Handle{unsafe.Pointer(n)}
			}

			break
		}
	}
	return nil
}

// Delete removes and ban 'cache node' with the given namespace and key.
// A banned 'cache node' will never inserted into the 'cache tree'. Ban
// only attributed to the particular 'cache node', so when a 'cache node'
// is recreated it will not be banned.
//
// If delFunc is not nil, then it will be executed if such 'cache node'
// doesn't exist or once the 'cache node' is released.
//
// Delete return true is such 'cache node' exist.
func (r *Cache) Delete(ns, key uint64, delFunc func()) bool {
	r.mu.RLock()
	defer r.mu.RUnlock()
	if r.closed {
		return false
	}

	hash := murmur32(ns, key, 0xf00)
	for {
		h, b := r.getBucket(hash)
		done, _, n := b.get(r, h, hash, ns, key, true)
		if done {
			if n != nil {
				if delFunc != nil {
					n.mu.Lock()
					n.delFuncs = append(n.delFuncs, delFunc)
					n.mu.Unlock()
				}
				if r.cacher != nil {
					r.cacher.Ban(n)
				}
				n.unRefInternal(true)
				return true
			}

			break
		}
	}

	if delFunc != nil {
		delFunc()
	}

	return false
}

// Evict evicts 'cache node' with the given namespace and key. This will
// simply call Cacher.Evict.
//
// Evict return true is such 'cache node' exist.
func (r *Cache) Evict(ns, key uint64) bool {
	r.mu.RLock()
	defer r.mu.RUnlock()
	if r.closed {
		return false
	}

	hash := murmur32(ns, key, 0xf00)
	for {
		h, b := r.getBucket(hash)
		done, _, n := b.get(r, h, hash, ns, key, true)
		if done {
			if n != nil {
				if r.cacher != nil {
					r.cacher.Evict(n)
				}
				n.unRefInternal(true)
				return true
			}

			break
		}
	}

	return false
}

// EvictNS evicts 'cache node' with the given namespace. This will
// simply call Cacher.Evict on all nodes with the given namespace.
func (r *Cache) EvictNS(ns uint64) {
	r.mu.RLock()
	defer r.mu.RUnlock()
	if r.closed {
		return
	}

	if r.cacher != nil {
		nodes := r.enumerateNodesByNS(ns)
		for _, n := range nodes {
			r.cacher.Evict(n)
		}
	}
}

func (r *Cache) evictAll() {
	r.enumerateNodesWithCB(func(nodes []*Node) {
		for _, n := range nodes {
			r.cacher.Evict(n)
		}
	})
}

// EvictAll evicts all 'cache node'. This will simply call Cacher.EvictAll.
func (r *Cache) EvictAll() {
	r.mu.RLock()
	defer r.mu.RUnlock()
	if r.closed {
		return
	}

	if r.cacher != nil {
		r.evictAll()
	}
}

// Close closes the 'cache map'.
// All 'Cache' method is no-op after 'cache map' is closed.
// All 'cache node' will be evicted from 'cacher'.
//
// If 'force' is true then all 'cache node' will be forcefully released
// even if the 'node ref' is not zero.
func (r *Cache) Close(force bool) {
	var head *mHead
	// Hold RW-lock to make sure no more in-flight operations.
	r.mu.Lock()
	if !r.closed {
		r.closed = true
		head = (*mHead)(atomic.LoadPointer(&r.mHead))
		atomic.StorePointer(&r.mHead, nil)
	}
	r.mu.Unlock()

	if head != nil {
		head.enumerateNodesWithCB(func(nodes []*Node) {
			for _, n := range nodes {
				// Zeroing ref. Prevent unRefExternal to call finalizer.
				if force {
					atomic.StoreInt32(&n.ref, 0)
				}

				// Evict from cacher.
				if r.cacher != nil {
					r.cacher.Evict(n)
				}

				if force {
					n.callFinalizer()
				}
			}
		})
	}
}

// Node is a 'cache node'.
type Node struct {
	r *Cache

	hash    uint32
	ns, key uint64

	mu    sync.Mutex
	size  int
	value Value

	ref      int32
	delFuncs []func()

	CacheData unsafe.Pointer
}

// NS returns this 'cache node' namespace.
func (n *Node) NS() uint64 {
	return n.ns
}

// Key returns this 'cache node' key.
func (n *Node) Key() uint64 {
	return n.key
}

// Size returns this 'cache node' size.
func (n *Node) Size() int {
	return n.size
}

// Value returns this 'cache node' value.
func (n *Node) Value() Value {
	return n.value
}

// Ref returns this 'cache node' ref counter.
func (n *Node) Ref() int32 {
	return atomic.LoadInt32(&n.ref)
}

// GetHandle returns an handle for this 'cache node'.
func (n *Node) GetHandle() *Handle {
	if atomic.AddInt32(&n.ref, 1) <= 1 {
		panic("BUG: Node.GetHandle on zero ref")
	}
	return &Handle{unsafe.Pointer(n)}
}

func (n *Node) callFinalizer() {
	// Call releaser.
	if n.value != nil {
		if r, ok := n.value.(util.Releaser); ok {
			r.Release()
		}
		n.value = nil
	}

	// Call delete funcs.
	for _, f := range n.delFuncs {
		f()
	}
	n.delFuncs = nil
}

func (n *Node) unRefInternal(updateStat bool) {
	if atomic.AddInt32(&n.ref, -1) == 0 {
		n.r.delete(n)
		if updateStat {
			atomic.AddInt64(&n.r.statDel, 1)
		}
	}
}

func (n *Node) unRefExternal() {
	if atomic.AddInt32(&n.ref, -1) == 0 {
		n.r.mu.RLock()
		if n.r.closed {
			n.callFinalizer()
		} else {
			n.r.delete(n)
			atomic.AddInt64(&n.r.statDel, 1)
		}
		n.r.mu.RUnlock()
	}
}

// Handle is a 'cache handle' of a 'cache node'.
type Handle struct {
	n unsafe.Pointer // *Node
}

// Value returns the value of the 'cache node'.
func (h *Handle) Value() Value {
	n := (*Node)(atomic.LoadPointer(&h.n))
	if n != nil {
		return n.value
	}
	return nil
}

// Release releases this 'cache handle'.
// It is safe to call release multiple times.
func (h *Handle) Release() {
	nPtr := atomic.LoadPointer(&h.n)
	if nPtr != nil && atomic.CompareAndSwapPointer(&h.n, nPtr, nil) {
		n := (*Node)(nPtr)
		n.unRefExternal()
	}
}

func murmur32(ns, key uint64, seed uint32) uint32 {
	const (
		m = uint32(0x5bd1e995)
		r = 24
	)

	k1 := uint32(ns >> 32)
	k2 := uint32(ns)
	k3 := uint32(key >> 32)
	k4 := uint32(key)

	k1 *= m
	k1 ^= k1 >> r
	k1 *= m

	k2 *= m
	k2 ^= k2 >> r
	k2 *= m

	k3 *= m
	k3 ^= k3 >> r
	k3 *= m

	k4 *= m
	k4 ^= k4 >> r
	k4 *= m

	h := seed

	h *= m
	h ^= k1
	h *= m
	h ^= k2
	h *= m
	h ^= k3
	h *= m
	h ^= k4

	h ^= h >> 13
	h *= m
	h ^= h >> 15

	return h
}
```

## File: `leveldb/cache/cache_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package cache

import (
	"math/rand"
	"runtime"
	"sync"
	"sync/atomic"
	"testing"
	"time"
	"unsafe"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

type int32o int32

func (o *int32o) acquire() {
	if atomic.AddInt32((*int32)(o), 1) != 1 {
		panic("BUG: invalid ref")
	}
}

func (o *int32o) Release() {
	if atomic.AddInt32((*int32)(o), -1) != 0 {
		panic("BUG: invalid ref")
	}
}

type releaserFunc struct {
	fn    func()
	value Value
}

func (r releaserFunc) Release() {
	if r.fn != nil {
		r.fn()
	}
}

func set(c *Cache, ns, key uint64, value Value, charge int, relf func()) *Handle {
	return c.Get(ns, key, func() (int, Value) {
		if relf != nil {
			return charge, releaserFunc{relf, value}
		}
		return charge, value
	})
}

func shuffleNodes(nodes mNodes) mNodes {
	shuffled := append(mNodes(nil), nodes...)
	rand.Shuffle(len(shuffled), func(i, j int) {
		shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
	})
	return shuffled
}

func generateSortedNodes(nNS, minNKey, maxNKey int) mNodes {
	var generated mNodes
	for i := 0; i < nNS; i++ {
		nKey := minNKey
		if maxNKey-minNKey > 0 {
			nKey += rand.Intn(maxNKey - minNKey)
		}
		for j := 0; j < nKey; j++ {
			generated = append(generated, &Node{ns: uint64(i), key: uint64(j)})
		}
	}
	return generated
}

func TestNodesSort(t *testing.T) {
	testFunc := func(nNS, minNKey, maxNKey int) func(t *testing.T) {
		return func(t *testing.T) {
			sorted := generateSortedNodes(nNS, minNKey, maxNKey)
			for i := 0; i < 3; i++ {
				shuffled := shuffleNodes(sorted)
				require.NotEqual(t, sorted, shuffled)
				shuffled.sort()
				require.Equal(t, sorted, shuffled)
			}
			for i, x := range sorted {
				r := sorted.search(x.ns, x.key)
				require.Equal(t, i, r)
			}
		}
	}

	t.Run("SingleNS", testFunc(1, 100, 100))
	t.Run("MultipleNS", testFunc(10, 1, 10))

	t.Run("SearchInexact", func(t *testing.T) {
		data := mNodes{
			&Node{ns: 0, key: 2},
			&Node{ns: 0, key: 3},
			&Node{ns: 0, key: 4},
			&Node{ns: 2, key: 1},
			&Node{ns: 2, key: 2},
			&Node{ns: 2, key: 3},
		}
		require.Equal(t, 0, data.search(0, 1))
		require.Equal(t, 0, data.search(0, 2))
		require.Equal(t, 3, data.search(0, 5))
		require.Equal(t, 3, data.search(1, 1001000))
		require.Equal(t, 5, data.search(2, 3))
		require.Equal(t, 6, data.search(2, 4))
		require.Equal(t, 6, data.search(10, 10))
	})
}

func TestCacheMap(t *testing.T) {
	runtime.GOMAXPROCS(runtime.NumCPU())

	type cacheMapTestParams struct {
		nObjects, nHandles, concurrent, repeat int
	}

	var params []cacheMapTestParams
	if testing.Short() {
		params = []cacheMapTestParams{
			{1000, 100, 20, 3},
			{10000, 300, 50, 10},
		}
	} else {
		params = []cacheMapTestParams{
			{10000, 400, 50, 3},
			{100000, 1000, 100, 10},
		}
	}

	var (
		objects [][]int32o
		handles [][]unsafe.Pointer
	)

	for _, x := range params {
		objects = append(objects, make([]int32o, x.nObjects))
		handles = append(handles, make([]unsafe.Pointer, x.nHandles))
	}

	c := NewCache(nil)

	wg := new(sync.WaitGroup)
	var done int32

	for id, param := range params {
		id := id
		param := param
		objects := objects[id]
		handles := handles[id]
		for job := 0; job < param.concurrent; job++ {
			wg.Add(1)
			go func() {
				defer wg.Done()

				r := rand.New(rand.NewSource(time.Now().UnixNano()))
				for j := len(objects) * param.repeat; j >= 0; j-- {
					if t.Failed() {
						return
					}

					i := r.Intn(len(objects))
					h := c.Get(uint64(id), uint64(i), func() (int, Value) {
						o := &objects[i]
						o.acquire()
						return 1, o
					})
					if !assert.True(t, h.Value().(*int32o) == &objects[i]) {
						return
					}
					if !assert.True(t, objects[i] == 1) {
						return
					}
					if !atomic.CompareAndSwapPointer(&handles[r.Intn(len(handles))], nil, unsafe.Pointer(h)) {
						h.Release()
					}
				}
			}()
		}

		// Randomly release handles at interval.
		go func() {
			r := rand.New(rand.NewSource(time.Now().UnixNano()))

			for atomic.LoadInt32(&done) == 0 {
				i := r.Intn(len(handles))
				h := (*Handle)(atomic.LoadPointer(&handles[i]))
				if h != nil && atomic.CompareAndSwapPointer(&handles[i], unsafe.Pointer(h), nil) {
					h.Release()
				}
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// Emulate constant grow-shrink.
	growShrinkStop := make(chan bool, 1)
	go func() {
		handles := make([]*Handle, 100000)
		for atomic.LoadInt32(&done) == 0 {
			for i := range handles {
				handles[i] = c.Get(999999999, uint64(i), func() (int, Value) {
					return 1, 1
				})
			}
			for _, h := range handles {
				h.Release()
			}
		}
		growShrinkStop <- true
	}()

	wg.Wait()
	atomic.StoreInt32(&done, 1)

	// Releasing handles.
	activeCount := 0
	for _, handle := range handles {
		for i := range handle {
			h := (*Handle)(atomic.LoadPointer(&handle[i]))
			if h != nil && atomic.CompareAndSwapPointer(&handle[i], unsafe.Pointer(h), nil) {
				activeCount++
				h.Release()
			}
		}
	}
	t.Logf("active_handles=%d", activeCount)

	// Checking object refs
	for id, object := range objects {
		for i, o := range object {
			require.EqualValues(t, 0, o, "invalid object ref: %d-%03d", id, i)
		}
	}

	<-growShrinkStop

	require.Zero(t, c.Nodes())
	require.Zero(t, c.Size())
	t.Logf("STATS: %#v", c.GetStats())
}

func TestCacheMap_NodesAndSize(t *testing.T) {
	c := NewCache(nil)
	require.Zero(t, c.Capacity())
	require.Zero(t, c.Nodes())
	require.Zero(t, c.Size())
	set(c, 0, 1, 1, 1, nil)
	set(c, 0, 2, 2, 2, nil)
	set(c, 1, 1, 3, 3, nil)
	set(c, 2, 1, 4, 1, nil)
	require.Equal(t, 4, c.Nodes())
	require.Equal(t, 7, c.Size())
}

func TestLRUCache_Capacity(t *testing.T) {
	c := NewCache(NewLRU(10))
	require.Equal(t, 10, c.Capacity())
	set(c, 0, 1, 1, 1, nil).Release()
	set(c, 0, 2, 2, 2, nil).Release()
	set(c, 1, 1, 3, 3, nil).Release()
	set(c, 2, 1, 4, 1, nil).Release()
	set(c, 2, 2, 5, 1, nil).Release()
	set(c, 2, 3, 6, 1, nil).Release()
	set(c, 2, 4, 7, 1, nil).Release()
	set(c, 2, 5, 8, 1, nil).Release()
	require.Equal(t, 7, c.Nodes())
	require.Equal(t, 10, c.Size())
	c.SetCapacity(9)
	require.Equal(t, 9, c.Capacity())
	require.Equal(t, 6, c.Nodes())
	require.Equal(t, 8, c.Size())
}

func TestCacheMap_NilValue(t *testing.T) {
	c := NewCache(NewLRU(10))
	h := c.Get(0, 0, func() (size int, value Value) {
		return 1, nil
	})
	require.Nil(t, h)
	require.Zero(t, c.Nodes())
	require.Zero(t, c.Size())
}

func TestLRUCache_GetLatency(t *testing.T) {
	runtime.GOMAXPROCS(runtime.NumCPU())

	const (
		concurrentSet = 30
		concurrentGet = 3
		duration      = 3 * time.Second
		delay         = 3 * time.Millisecond
		maxKey        = 100000
	)

	var (
		set, getHit, getAll        int32
		getMaxLatency, getDuration int64
	)

	c := NewCache(NewLRU(5000))
	wg := &sync.WaitGroup{}
	until := time.Now().Add(duration)
	for i := 0; i < concurrentSet; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			r := rand.New(rand.NewSource(time.Now().UnixNano()))
			for time.Now().Before(until) {
				c.Get(0, uint64(r.Intn(maxKey)), func() (int, Value) {
					time.Sleep(delay)
					atomic.AddInt32(&set, 1)
					return 1, 1
				}).Release()
			}
		}(i)
	}
	for i := 0; i < concurrentGet; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			r := rand.New(rand.NewSource(time.Now().UnixNano()))
			for {
				mark := time.Now()
				if mark.Before(until) {
					h := c.Get(0, uint64(r.Intn(maxKey)), nil)
					latency := int64(time.Since(mark))
					m := atomic.LoadInt64(&getMaxLatency)
					if latency > m {
						atomic.CompareAndSwapInt64(&getMaxLatency, m, latency)
					}
					atomic.AddInt64(&getDuration, latency)
					if h != nil {
						atomic.AddInt32(&getHit, 1)
						h.Release()
					}
					atomic.AddInt32(&getAll, 1)
				} else {
					break
				}
			}
		}(i)
	}

	wg.Wait()
	getAvgLatency := time.Duration(getDuration) / time.Duration(getAll)
	t.Logf("set=%d getHit=%d getAll=%d getMaxLatency=%v getAvgLatency=%v",
		set, getHit, getAll, time.Duration(getMaxLatency), getAvgLatency)

	require.LessOrEqual(t, getAvgLatency, delay/3)
	t.Logf("STATS: %#v", c.GetStats())
}

func TestLRUCache_HitMiss(t *testing.T) {
	cases := []struct {
		key   uint64
		value string
	}{
		{1, "vvvvvvvvv"},
		{100, "v1"},
		{0, "v2"},
		{12346, "v3"},
		{777, "v4"},
		{999, "v5"},
		{7654, "v6"},
		{2, "v7"},
		{3, "v8"},
		{9, "v9"},
	}

	setFin := 0
	c := NewCache(NewLRU(1000))
	for i, x := range cases {
		set(c, 0, x.key, x.value, len(x.value), func() {
			setFin++
		}).Release()
		for j, y := range cases {
			h := c.Get(0, y.key, nil)
			if j <= i {
				// should hit
				require.NotNilf(t, h, "case '%d' iteration '%d' should hit", i, j)
				require.Equalf(t, y.value, h.Value().(releaserFunc).value, "case '%d' iteration '%d' should have valid value", i, j)
			} else {
				// should miss
				require.Nilf(t, h, "case '%d' iteration '%d' should miss", i, j)
			}
			if h != nil {
				h.Release()
			}
		}
	}

	for i, x := range cases {
		finalizerOk := false
		c.Delete(0, x.key, func() {
			finalizerOk = true
		})

		require.True(t, finalizerOk)

		for j, y := range cases {
			h := c.Get(0, y.key, nil)
			if j > i {
				// should hit
				require.NotNilf(t, h, "case '%d' iteration '%d' should hit", i, j)
				require.Equalf(t, y.value, h.Value().(releaserFunc).value, "case '%d' iteration '%d' should have valid value", i, j)
			} else {
				// should miss
				require.Nilf(t, h, "case '%d' iteration '%d' should miss", i, j)
			}
			if h != nil {
				h.Release()
			}
		}
	}

	require.Equal(t, len(cases), setFin, "some set finalizer may not be executed")
}

func TestLRUCache_Eviction(t *testing.T) {
	c := NewCache(NewLRU(12))
	o1 := set(c, 0, 1, 1, 1, nil)
	set(c, 0, 2, 2, 1, nil).Release()
	set(c, 0, 3, 3, 1, nil).Release()
	set(c, 0, 4, 4, 1, nil).Release()
	set(c, 0, 5, 5, 1, nil).Release()
	if h := c.Get(0, 2, nil); h != nil { // 1,3,4,5,2
		h.Release()
	}
	set(c, 0, 9, 9, 10, nil).Release() // 5,2,9

	for _, key := range []uint64{9, 2, 5, 1} {
		h := c.Get(0, key, nil)
		require.NotNilf(t, h, "miss for key '%d'", key)
		require.Equalf(t, int(key), h.Value(), "invalid value for key '%d'", key)
		h.Release()
	}
	o1.Release()
	for _, key := range []uint64{1, 2, 5} {
		h := c.Get(0, key, nil)
		require.NotNilf(t, h, "miss for key '%d'", key)
		require.Equalf(t, int(key), h.Value(), "invalid value for key '%d'", key)
		h.Release()
	}
	for _, key := range []uint64{3, 4, 9} {
		h := c.Get(0, key, nil)
		if !assert.Nilf(t, h, "hit for key '%d'", key) {
			require.Equalf(t, int(key), h.Value(), "invalid value for key '%d'", key)
			h.Release()
		}
	}
}

func TestLRUCache_Evict(t *testing.T) {
	lru := NewLRU(6).(*lru)
	c := NewCache(lru)
	set(c, 0, 1, 1, 1, nil).Release()
	set(c, 0, 2, 2, 1, nil).Release()
	set(c, 1, 1, 3, 1, nil).Release()
	set(c, 1, 2, 4, 1, nil).Release()
	set(c, 2, 1, 5, 1, nil).Release()
	set(c, 2, 2, 6, 1, nil).Release()

	v := 1
	for ns := 0; ns < 3; ns++ {
		for key := 1; key < 3; key++ {
			h := c.Get(uint64(ns), uint64(key), nil)
			require.NotNilf(t, h, "NS=%d key=%d", ns, key)
			require.Equal(t, v, h.Value())
			h.Release()
			v++
		}
	}

	require.True(t, c.Evict(0, 1))
	require.Equal(t, 5, lru.used)
	require.False(t, c.Evict(0, 1))

	c.EvictNS(1)
	require.Equal(t, 3, lru.used)
	require.Nil(t, c.Get(1, 1, nil))
	require.Nil(t, c.Get(1, 2, nil))

	c.EvictAll()
	require.Zero(t, lru.used)
	require.Nil(t, c.Get(0, 1, nil))
	require.Nil(t, c.Get(0, 2, nil))
	require.Nil(t, c.Get(1, 1, nil))
	require.Nil(t, c.Get(1, 2, nil))
	require.Nil(t, c.Get(2, 1, nil))
	require.Nil(t, c.Get(2, 2, nil))
}

func TestLRUCache_Delete(t *testing.T) {
	delFuncCalled := 0
	delFunc := func() {
		delFuncCalled++
	}

	c := NewCache(NewLRU(2))
	set(c, 0, 1, 1, 1, nil).Release()
	set(c, 0, 2, 2, 1, nil).Release()

	require.True(t, c.Delete(0, 1, delFunc))
	require.Nil(t, c.Get(0, 1, nil))
	require.False(t, c.Delete(0, 1, delFunc))

	h2 := c.Get(0, 2, nil)
	require.NotNil(t, h2)
	require.True(t, c.Delete(0, 2, delFunc))
	require.True(t, c.Delete(0, 2, delFunc))

	set(c, 0, 3, 3, 1, nil).Release()
	set(c, 0, 4, 4, 1, nil).Release()
	c.Get(0, 2, nil).Release()

	for key := 2; key <= 4; key++ {
		h := c.Get(0, uint64(key), nil)
		require.NotNil(t, h)
		h.Release()
	}

	h2.Release()
	require.Nil(t, c.Get(0, 2, nil))
	require.Equal(t, 4, delFuncCalled)
}

func TestLRUCache_Close(t *testing.T) {
	relFuncCalled := 0
	relFunc := func() {
		relFuncCalled++
	}
	delFuncCalled := 0
	delFunc := func() {
		delFuncCalled++
	}

	c := NewCache(NewLRU(2))
	set(c, 0, 1, 1, 1, relFunc).Release()
	set(c, 0, 2, 2, 1, relFunc).Release()

	h3 := set(c, 0, 3, 3, 1, relFunc)
	require.NotNil(t, h3)
	require.True(t, c.Delete(0, 3, delFunc))

	c.Close(true)

	require.Equal(t, 3, relFuncCalled)
	require.Equal(t, 1, delFuncCalled)
}
```

## File: `leveldb/cache/lru.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package cache

import (
	"sync"
	"unsafe"
)

type lruNode struct {
	n   *Node
	h   *Handle
	ban bool

	next, prev *lruNode
}

func (n *lruNode) insert(at *lruNode) {
	x := at.next
	at.next = n
	n.prev = at
	n.next = x
	x.prev = n
}

func (n *lruNode) remove() {
	if n.prev != nil {
		n.prev.next = n.next
		n.next.prev = n.prev
		n.prev = nil
		n.next = nil
	} else {
		panic("BUG: removing removed node")
	}
}

type lru struct {
	mu       sync.Mutex
	capacity int
	used     int
	recent   lruNode
}

func (r *lru) reset() {
	r.recent.next = &r.recent
	r.recent.prev = &r.recent
	r.used = 0
}

func (r *lru) Capacity() int {
	r.mu.Lock()
	defer r.mu.Unlock()
	return r.capacity
}

func (r *lru) SetCapacity(capacity int) {
	var evicted []*lruNode

	r.mu.Lock()
	r.capacity = capacity
	for r.used > r.capacity {
		rn := r.recent.prev
		if rn == nil {
			panic("BUG: invalid LRU used or capacity counter")
		}
		rn.remove()
		rn.n.CacheData = nil
		r.used -= rn.n.Size()
		evicted = append(evicted, rn)
	}
	r.mu.Unlock()

	for _, rn := range evicted {
		rn.h.Release()
	}
}

func (r *lru) Promote(n *Node) {
	var evicted []*lruNode

	r.mu.Lock()
	if n.CacheData == nil {
		if n.Size() <= r.capacity {
			rn := &lruNode{n: n, h: n.GetHandle()}
			rn.insert(&r.recent)
			n.CacheData = unsafe.Pointer(rn)
			r.used += n.Size()

			for r.used > r.capacity {
				rn := r.recent.prev
				if rn == nil {
					panic("BUG: invalid LRU used or capacity counter")
				}
				rn.remove()
				rn.n.CacheData = nil
				r.used -= rn.n.Size()
				evicted = append(evicted, rn)
			}
		}
	} else {
		rn := (*lruNode)(n.CacheData)
		if !rn.ban {
			rn.remove()
			rn.insert(&r.recent)
		}
	}
	r.mu.Unlock()

	for _, rn := range evicted {
		rn.h.Release()
	}
}

func (r *lru) Ban(n *Node) {
	r.mu.Lock()
	if n.CacheData == nil {
		n.CacheData = unsafe.Pointer(&lruNode{n: n, ban: true})
	} else {
		rn := (*lruNode)(n.CacheData)
		if !rn.ban {
			rn.remove()
			rn.ban = true
			r.used -= rn.n.Size()
			r.mu.Unlock()

			rn.h.Release()
			rn.h = nil
			return
		}
	}
	r.mu.Unlock()
}

func (r *lru) Evict(n *Node) {
	r.mu.Lock()
	rn := (*lruNode)(n.CacheData)
	if rn == nil || rn.ban {
		r.mu.Unlock()
		return
	}
	rn.remove()
	r.used -= n.Size()
	n.CacheData = nil
	r.mu.Unlock()

	rn.h.Release()
}

// NewLRU create a new LRU-cache.
func NewLRU(capacity int) Cacher {
	r := &lru{capacity: capacity}
	r.reset()
	return r
}
```

## File: `leveldb/comparer/bytes_comparer.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package comparer

import "bytes"

type bytesComparer struct{}

func (bytesComparer) Compare(a, b []byte) int {
	return bytes.Compare(a, b)
}

func (bytesComparer) Name() string {
	return "leveldb.BytewiseComparator"
}

func (bytesComparer) Separator(dst, a, b []byte) []byte {
	i, n := 0, len(a)
	if n > len(b) {
		n = len(b)
	}
	for ; i < n && a[i] == b[i]; i++ {
	}
	if i >= n {
		// Do not shorten if one string is a prefix of the other
	} else if c := a[i]; c < 0xff && c+1 < b[i] {
		dst = append(dst, a[:i+1]...)
		dst[len(dst)-1]++
		return dst
	}
	return nil
}

func (bytesComparer) Successor(dst, b []byte) []byte {
	for i, c := range b {
		if c != 0xff {
			dst = append(dst, b[:i+1]...)
			dst[len(dst)-1]++
			return dst
		}
	}
	return nil
}

// DefaultComparer are default implementation of the Comparer interface.
// It uses the natural ordering, consistent with bytes.Compare.
var DefaultComparer = bytesComparer{}
```

## File: `leveldb/comparer/comparer.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package comparer provides interface and implementation for ordering
// sets of data.
package comparer

// BasicComparer is the interface that wraps the basic Compare method.
type BasicComparer interface {
	// Compare returns -1, 0, or +1 depending on whether a is 'less than',
	// 'equal to' or 'greater than' b. The two arguments can only be 'equal'
	// if their contents are exactly equal. Furthermore, the empty slice
	// must be 'less than' any non-empty slice.
	Compare(a, b []byte) int
}

// Comparer defines a total ordering over the space of []byte keys: a 'less
// than' relationship.
type Comparer interface {
	BasicComparer

	// Name returns name of the comparer.
	//
	// The Level-DB on-disk format stores the comparer name, and opening a
	// database with a different comparer from the one it was created with
	// will result in an error.
	//
	// An implementation to a new name whenever the comparer implementation
	// changes in a way that will cause the relative ordering of any two keys
	// to change.
	//
	// Names starting with "leveldb." are reserved and should not be used
	// by any users of this package.
	Name() string

	// Bellow are advanced functions used to reduce the space requirements
	// for internal data structures such as index blocks.

	// Separator appends a sequence of bytes x to dst such that a <= x && x < b,
	// where 'less than' is consistent with Compare. An implementation should
	// return nil if x equal to a.
	//
	// Either contents of a or b should not by any means modified. Doing so
	// may cause corruption on the internal state.
	Separator(dst, a, b []byte) []byte

	// Successor appends a sequence of bytes x to dst such that x >= b, where
	// 'less than' is consistent with Compare. An implementation should return
	// nil if x equal to b.
	//
	// Contents of b should not by any means modified. Doing so may cause
	// corruption on the internal state.
	Successor(dst, b []byte) []byte
}
```

## File: `leveldb/errors/errors.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package errors provides common error types used throughout leveldb.
package errors

import (
	"errors"
	"fmt"

	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/util"
)

// Common errors.
var (
	ErrNotFound    = New("leveldb: not found")
	ErrReleased    = util.ErrReleased
	ErrHasReleaser = util.ErrHasReleaser
)

// New returns an error that formats as the given text.
func New(text string) error {
	return errors.New(text)
}

// ErrCorrupted is the type that wraps errors that indicate corruption in
// the database.
type ErrCorrupted struct {
	Fd  storage.FileDesc
	Err error
}

func (e *ErrCorrupted) Error() string {
	if !e.Fd.Zero() {
		return fmt.Sprintf("%v [file=%v]", e.Err, e.Fd)
	}
	return e.Err.Error()
}

// NewErrCorrupted creates new ErrCorrupted error.
func NewErrCorrupted(fd storage.FileDesc, err error) error {
	return &ErrCorrupted{fd, err}
}

// IsCorrupted returns a boolean indicating whether the error is indicating
// a corruption.
func IsCorrupted(err error) bool {
	switch err.(type) {
	case *ErrCorrupted:
		return true
	case *storage.ErrCorrupted:
		return true
	}
	return false
}

// ErrMissingFiles is the type that indicating a corruption due to missing
// files. ErrMissingFiles always wrapped with ErrCorrupted.
type ErrMissingFiles struct {
	Fds []storage.FileDesc
}

func (e *ErrMissingFiles) Error() string { return "file missing" }

// SetFd sets 'file info' of the given error with the given file.
// Currently only ErrCorrupted is supported, otherwise will do nothing.
func SetFd(err error, fd storage.FileDesc) error {
	switch x := err.(type) {
	case *ErrCorrupted:
		x.Fd = fd
		return x
	default:
		return err
	}
}
```

## File: `leveldb/filter/bloom.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package filter

import (
	"github.com/syndtr/goleveldb/leveldb/util"
)

func bloomHash(key []byte) uint32 {
	return util.Hash(key, 0xbc9f1d34)
}

type bloomFilter int

// Name: The bloom filter serializes its parameters and is backward compatible
// with respect to them. Therefor, its parameters are not added to its
// name.
func (bloomFilter) Name() string {
	return "leveldb.BuiltinBloomFilter"
}

func (f bloomFilter) Contains(filter, key []byte) bool {
	nBytes := len(filter) - 1
	if nBytes < 1 {
		return false
	}
	nBits := uint32(nBytes * 8)

	// Use the encoded k so that we can read filters generated by
	// bloom filters created using different parameters.
	k := filter[nBytes]
	if k > 30 {
		// Reserved for potentially new encodings for short bloom filters.
		// Consider it a match.
		return true
	}

	kh := bloomHash(key)
	delta := (kh >> 17) | (kh << 15) // Rotate right 17 bits
	for j := uint8(0); j < k; j++ {
		bitpos := kh % nBits
		if (uint32(filter[bitpos/8]) & (1 << (bitpos % 8))) == 0 {
			return false
		}
		kh += delta
	}
	return true
}

func (f bloomFilter) NewGenerator() FilterGenerator {
	// Round down to reduce probing cost a little bit.
	k := uint8(f * 69 / 100) // 0.69 =~ ln(2)
	if k < 1 {
		k = 1
	} else if k > 30 {
		k = 30
	}
	return &bloomFilterGenerator{
		n: int(f),
		k: k,
	}
}

type bloomFilterGenerator struct {
	n int
	k uint8

	keyHashes []uint32
}

func (g *bloomFilterGenerator) Add(key []byte) {
	// Use double-hashing to generate a sequence of hash values.
	// See analysis in [Kirsch,Mitzenmacher 2006].
	g.keyHashes = append(g.keyHashes, bloomHash(key))
}

func (g *bloomFilterGenerator) Generate(b Buffer) {
	// Compute bloom filter size (in both bits and bytes)
	nBits := uint32(len(g.keyHashes) * g.n)
	// For small n, we can see a very high false positive rate.  Fix it
	// by enforcing a minimum bloom filter length.
	if nBits < 64 {
		nBits = 64
	}
	nBytes := (nBits + 7) / 8
	nBits = nBytes * 8

	dest := b.Alloc(int(nBytes) + 1)
	dest[nBytes] = g.k
	for _, kh := range g.keyHashes {
		delta := (kh >> 17) | (kh << 15) // Rotate right 17 bits
		for j := uint8(0); j < g.k; j++ {
			bitpos := kh % nBits
			dest[bitpos/8] |= (1 << (bitpos % 8))
			kh += delta
		}
	}

	g.keyHashes = g.keyHashes[:0]
}

// NewBloomFilter creates a new initialized bloom filter for given
// bitsPerKey.
//
// Since bitsPerKey is persisted individually for each bloom filter
// serialization, bloom filters are backwards compatible with respect to
// changing bitsPerKey. This means that no big performance penalty will
// be experienced when changing the parameter. See documentation for
// opt.Options.Filter for more information.
func NewBloomFilter(bitsPerKey int) Filter {
	return bloomFilter(bitsPerKey)
}
```

## File: `leveldb/filter/bloom_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package filter

import (
	"encoding/binary"
	"github.com/syndtr/goleveldb/leveldb/util"
	"testing"
)

type harness struct {
	t *testing.T

	bloom     Filter
	generator FilterGenerator
	filter    []byte
}

func newHarness(t *testing.T) *harness {
	bloom := NewBloomFilter(10)
	return &harness{
		t:         t,
		bloom:     bloom,
		generator: bloom.NewGenerator(),
	}
}

func (h *harness) add(key []byte) {
	h.generator.Add(key)
}

func (h *harness) addNum(key uint32) {
	var b [4]byte
	binary.LittleEndian.PutUint32(b[:], key)
	h.add(b[:])
}

func (h *harness) build() {
	b := &util.Buffer{}
	h.generator.Generate(b)
	h.filter = b.Bytes()
}

func (h *harness) reset() {
	h.filter = nil
}

func (h *harness) filterLen() int {
	return len(h.filter)
}

func (h *harness) assert(key []byte, want, silent bool) bool {
	got := h.bloom.Contains(h.filter, key)
	if !silent && got != want {
		h.t.Errorf("assert on '%v' failed got '%v', want '%v'", key, got, want)
	}
	return got
}

func (h *harness) assertNum(key uint32, want, silent bool) bool {
	var b [4]byte
	binary.LittleEndian.PutUint32(b[:], key)
	return h.assert(b[:], want, silent)
}

func TestBloomFilter_Empty(t *testing.T) {
	h := newHarness(t)
	h.build()
	h.assert([]byte("hello"), false, false)
	h.assert([]byte("world"), false, false)
}

func TestBloomFilter_Small(t *testing.T) {
	h := newHarness(t)
	h.add([]byte("hello"))
	h.add([]byte("world"))
	h.build()
	h.assert([]byte("hello"), true, false)
	h.assert([]byte("world"), true, false)
	h.assert([]byte("x"), false, false)
	h.assert([]byte("foo"), false, false)
}

func nextN(n int) int {
	switch {
	case n < 10:
		n += 1
	case n < 100:
		n += 10
	case n < 1000:
		n += 100
	default:
		n += 1000
	}
	return n
}

func TestBloomFilter_VaryingLengths(t *testing.T) {
	h := newHarness(t)
	var mediocre, good int
	for n := 1; n < 10000; n = nextN(n) {
		h.reset()
		for i := 0; i < n; i++ {
			h.addNum(uint32(i))
		}
		h.build()

		got := h.filterLen()
		want := (n * 10 / 8) + 40
		if got > want {
			t.Errorf("filter len test failed, '%d' > '%d'", got, want)
		}

		for i := 0; i < n; i++ {
			h.assertNum(uint32(i), true, false)
		}

		var rate float32
		for i := 0; i < 10000; i++ {
			if h.assertNum(uint32(i+1000000000), true, true) {
				rate++
			}
		}
		rate /= 10000
		if rate > 0.02 {
			t.Errorf("false positive rate is more than 2%%, got %v, at len %d", rate, n)
		}
		if rate > 0.0125 {
			mediocre++
		} else {
			good++
		}
	}
	t.Logf("false positive rate: %d good, %d mediocre", good, mediocre)
	if mediocre > good/5 {
		t.Error("mediocre false positive rate is more than expected")
	}
}
```

## File: `leveldb/filter/filter.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package filter provides interface and implementation of probabilistic
// data structure.
//
// The filter is resposible for creating small filter from a set of keys.
// These filter will then used to test whether a key is a member of the set.
// In many cases, a filter can cut down the number of disk seeks from a
// handful to a single disk seek per DB.Get call.
package filter

// Buffer is the interface that wraps basic Alloc, Write and WriteByte methods.
type Buffer interface {
	// Alloc allocs n bytes of slice from the buffer. This also advancing
	// write offset.
	Alloc(n int) []byte

	// Write appends the contents of p to the buffer.
	Write(p []byte) (n int, err error)

	// WriteByte appends the byte c to the buffer.
	WriteByte(c byte) error
}

// Filter is the filter.
type Filter interface {
	// Name returns the name of this policy.
	//
	// Note that if the filter encoding changes in an incompatible way,
	// the name returned by this method must be changed. Otherwise, old
	// incompatible filters may be passed to methods of this type.
	Name() string

	// NewGenerator creates a new filter generator.
	NewGenerator() FilterGenerator

	// Contains returns true if the filter contains the given key.
	//
	// The filter are filters generated by the filter generator.
	Contains(filter, key []byte) bool
}

// FilterGenerator is the filter generator.
type FilterGenerator interface {
	// Add adds a key to the filter generator.
	//
	// The key may become invalid after call to this method end, therefor
	// key must be copied if implementation require keeping key for later
	// use. The key should not modified directly, doing so may cause
	// undefined results.
	Add(key []byte)

	// Generate generates filters based on keys passed so far. After call
	// to Generate the filter generator maybe resetted, depends on implementation.
	Generate(b Buffer)
}
```

## File: `leveldb/iterator/array_iter.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package iterator

import (
	"github.com/syndtr/goleveldb/leveldb/util"
)

// BasicArray is the interface that wraps basic Len and Search method.
type BasicArray interface {
	// Len returns length of the array.
	Len() int

	// Search finds smallest index that point to a key that is greater
	// than or equal to the given key.
	Search(key []byte) int
}

// Array is the interface that wraps BasicArray and basic Index method.
type Array interface {
	BasicArray

	// Index returns key/value pair with index of i.
	Index(i int) (key, value []byte)
}

// Array is the interface that wraps BasicArray and basic Get method.
type ArrayIndexer interface {
	BasicArray

	// Get returns a new data iterator with index of i.
	Get(i int) Iterator
}

type basicArrayIterator struct {
	util.BasicReleaser
	array BasicArray
	pos   int
	err   error
}

func (i *basicArrayIterator) Valid() bool {
	return i.pos >= 0 && i.pos < i.array.Len() && !i.Released()
}

func (i *basicArrayIterator) First() bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	if i.array.Len() == 0 {
		i.pos = -1
		return false
	}
	i.pos = 0
	return true
}

func (i *basicArrayIterator) Last() bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	n := i.array.Len()
	if n == 0 {
		i.pos = 0
		return false
	}
	i.pos = n - 1
	return true
}

func (i *basicArrayIterator) Seek(key []byte) bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	n := i.array.Len()
	if n == 0 {
		i.pos = 0
		return false
	}
	i.pos = i.array.Search(key)
	return i.pos < n
}

func (i *basicArrayIterator) Next() bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	i.pos++
	if n := i.array.Len(); i.pos >= n {
		i.pos = n
		return false
	}
	return true
}

func (i *basicArrayIterator) Prev() bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	i.pos--
	if i.pos < 0 {
		i.pos = -1
		return false
	}
	return true
}

func (i *basicArrayIterator) Error() error { return i.err }

type arrayIterator struct {
	basicArrayIterator
	array      Array
	pos        int
	key, value []byte
}

func (i *arrayIterator) updateKV() {
	if i.pos == i.basicArrayIterator.pos {
		return
	}
	i.pos = i.basicArrayIterator.pos
	if i.Valid() {
		i.key, i.value = i.array.Index(i.pos)
	} else {
		i.key = nil
		i.value = nil
	}
}

func (i *arrayIterator) Key() []byte {
	i.updateKV()
	return i.key
}

func (i *arrayIterator) Value() []byte {
	i.updateKV()
	return i.value
}

type arrayIteratorIndexer struct {
	basicArrayIterator
	array ArrayIndexer
}

func (i *arrayIteratorIndexer) Get() Iterator {
	if i.Valid() {
		return i.array.Get(i.basicArrayIterator.pos)
	}
	return nil
}

// NewArrayIterator returns an iterator from the given array.
func NewArrayIterator(array Array) Iterator {
	return &arrayIterator{
		basicArrayIterator: basicArrayIterator{array: array, pos: -1},
		array:              array,
		pos:                -1,
	}
}

// NewArrayIndexer returns an index iterator from the given array.
func NewArrayIndexer(array ArrayIndexer) IteratorIndexer {
	return &arrayIteratorIndexer{
		basicArrayIterator: basicArrayIterator{array: array, pos: -1},
		array:              array,
	}
}
```

## File: `leveldb/iterator/array_iter_test.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package iterator_test

import (
	. "github.com/onsi/ginkgo"

	. "github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/testutil"
)

var _ = testutil.Defer(func() {
	Describe("Array iterator", func() {
		It("Should iterates and seeks correctly", func() {
			// Build key/value.
			kv := testutil.KeyValue_Generate(nil, 70, 1, 1, 5, 3, 3)

			// Test the iterator.
			t := testutil.IteratorTesting{
				KeyValue: kv.Clone(),
				Iter:     NewArrayIterator(kv),
			}
			testutil.DoIteratorTesting(&t)
		})
	})
})
```

## File: `leveldb/iterator/indexed_iter.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package iterator

import (
	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/util"
)

// IteratorIndexer is the interface that wraps CommonIterator and basic Get
// method. IteratorIndexer provides index for indexed iterator.
type IteratorIndexer interface {
	CommonIterator

	// Get returns a new data iterator for the current position, or nil if
	// done.
	Get() Iterator
}

type indexedIterator struct {
	util.BasicReleaser
	index  IteratorIndexer
	strict bool

	data Iterator
	err  error
	errf func(err error)
}

func (i *indexedIterator) setData() {
	if i.data != nil {
		i.data.Release()
	}
	i.data = i.index.Get()
}

func (i *indexedIterator) clearData() {
	if i.data != nil {
		i.data.Release()
	}
	i.data = nil
}

func (i *indexedIterator) indexErr() {
	if err := i.index.Error(); err != nil {
		if i.errf != nil {
			i.errf(err)
		}
		i.err = err
	}
}

func (i *indexedIterator) dataErr() bool {
	if err := i.data.Error(); err != nil {
		if i.errf != nil {
			i.errf(err)
		}
		if i.strict || !errors.IsCorrupted(err) {
			i.err = err
			return true
		}
	}
	return false
}

func (i *indexedIterator) Valid() bool {
	return i.data != nil && i.data.Valid()
}

func (i *indexedIterator) First() bool {
	if i.err != nil {
		return false
	} else if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	if !i.index.First() {
		i.indexErr()
		i.clearData()
		return false
	}
	i.setData()
	return i.Next()
}

func (i *indexedIterator) Last() bool {
	if i.err != nil {
		return false
	} else if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	if !i.index.Last() {
		i.indexErr()
		i.clearData()
		return false
	}
	i.setData()
	if !i.data.Last() {
		if i.dataErr() {
			return false
		}
		i.clearData()
		return i.Prev()
	}
	return true
}

func (i *indexedIterator) Seek(key []byte) bool {
	if i.err != nil {
		return false
	} else if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	if !i.index.Seek(key) {
		i.indexErr()
		i.clearData()
		return false
	}
	i.setData()
	if !i.data.Seek(key) {
		if i.dataErr() {
			return false
		}
		i.clearData()
		return i.Next()
	}
	return true
}

func (i *indexedIterator) Next() bool {
	if i.err != nil {
		return false
	} else if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	switch {
	case i.data != nil && !i.data.Next():
		if i.dataErr() {
			return false
		}
		i.clearData()
		fallthrough
	case i.data == nil:
		if !i.index.Next() {
			i.indexErr()
			return false
		}
		i.setData()
		return i.Next()
	}
	return true
}

func (i *indexedIterator) Prev() bool {
	if i.err != nil {
		return false
	} else if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	switch {
	case i.data != nil && !i.data.Prev():
		if i.dataErr() {
			return false
		}
		i.clearData()
		fallthrough
	case i.data == nil:
		if !i.index.Prev() {
			i.indexErr()
			return false
		}
		i.setData()
		if !i.data.Last() {
			if i.dataErr() {
				return false
			}
			i.clearData()
			return i.Prev()
		}
	}
	return true
}

func (i *indexedIterator) Key() []byte {
	if i.data == nil {
		return nil
	}
	return i.data.Key()
}

func (i *indexedIterator) Value() []byte {
	if i.data == nil {
		return nil
	}
	return i.data.Value()
}

func (i *indexedIterator) Release() {
	i.clearData()
	i.index.Release()
	i.BasicReleaser.Release()
}

func (i *indexedIterator) Error() error {
	if i.err != nil {
		return i.err
	}
	if err := i.index.Error(); err != nil {
		return err
	}
	return nil
}

func (i *indexedIterator) SetErrorCallback(f func(err error)) {
	i.errf = f
}

// NewIndexedIterator returns an 'indexed iterator'. An index is iterator
// that returns another iterator, a 'data iterator'. A 'data iterator' is the
// iterator that contains actual key/value pairs.
//
// If strict is true the any 'corruption errors' (i.e errors.IsCorrupted(err) == true)
// won't be ignored and will halt 'indexed iterator', otherwise the iterator will
// continue to the next 'data iterator'. Corruption on 'index iterator' will not be
// ignored and will halt the iterator.
func NewIndexedIterator(index IteratorIndexer, strict bool) Iterator {
	return &indexedIterator{index: index, strict: strict}
}
```

## File: `leveldb/iterator/indexed_iter_test.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package iterator_test

import (
	"sort"

	. "github.com/onsi/ginkgo"

	"github.com/syndtr/goleveldb/leveldb/comparer"
	. "github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/testutil"
)

type keyValue struct {
	key []byte
	testutil.KeyValue
}

type keyValueIndex []keyValue

func (x keyValueIndex) Search(key []byte) int {
	return sort.Search(x.Len(), func(i int) bool {
		return comparer.DefaultComparer.Compare(x[i].key, key) >= 0
	})
}

func (x keyValueIndex) Len() int                        { return len(x) }
func (x keyValueIndex) Index(i int) (key, value []byte) { return x[i].key, nil }
func (x keyValueIndex) Get(i int) Iterator              { return NewArrayIterator(x[i]) }

var _ = testutil.Defer(func() {
	Describe("Indexed iterator", func() {
		Test := func(n ...int) func() {
			if len(n) == 0 {
				rnd := testutil.NewRand()
				n = make([]int, rnd.Intn(17)+3)
				for i := range n {
					n[i] = rnd.Intn(19) + 1
				}
			}

			return func() {
				It("Should iterates and seeks correctly", func(done Done) {
					// Build key/value.
					index := make(keyValueIndex, len(n))
					sum := 0
					for _, x := range n {
						sum += x
					}
					kv := testutil.KeyValue_Generate(nil, sum, 1, 1, 10, 4, 4)
					for i, j := 0, 0; i < len(n); i++ {
						for x := n[i]; x > 0; x-- {
							key, value := kv.Index(j)
							index[i].key = key
							index[i].Put(key, value)
							j++
						}
					}

					// Test the iterator.
					t := testutil.IteratorTesting{
						KeyValue: kv.Clone(),
						Iter:     NewIndexedIterator(NewArrayIndexer(index), true),
					}
					testutil.DoIteratorTesting(&t)
					done <- true
				}, 15.0)
			}
		}

		Describe("with 100 keys", Test(100))
		Describe("with 50-50 keys", Test(50, 50))
		Describe("with 50-1 keys", Test(50, 1))
		Describe("with 50-1-50 keys", Test(50, 1, 50))
		Describe("with 1-50 keys", Test(1, 50))
		Describe("with random N-keys", Test())
	})
})
```

## File: `leveldb/iterator/iter.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package iterator provides interface and implementation to traverse over
// contents of a database.
package iterator

import (
	"errors"

	"github.com/syndtr/goleveldb/leveldb/util"
)

var (
	ErrIterReleased = errors.New("leveldb/iterator: iterator released")
)

// IteratorSeeker is the interface that wraps the 'seeks method'.
type IteratorSeeker interface {
	// First moves the iterator to the first key/value pair. If the iterator
	// only contains one key/value pair then First and Last would moves
	// to the same key/value pair.
	// It returns whether such pair exist.
	First() bool

	// Last moves the iterator to the last key/value pair. If the iterator
	// only contains one key/value pair then First and Last would moves
	// to the same key/value pair.
	// It returns whether such pair exist.
	Last() bool

	// Seek moves the iterator to the first key/value pair whose key is greater
	// than or equal to the given key.
	// It returns whether such pair exist.
	//
	// It is safe to modify the contents of the argument after Seek returns.
	Seek(key []byte) bool

	// Next moves the iterator to the next key/value pair.
	// It returns false if the iterator is exhausted.
	Next() bool

	// Prev moves the iterator to the previous key/value pair.
	// It returns false if the iterator is exhausted.
	Prev() bool
}

// CommonIterator is the interface that wraps common iterator methods.
type CommonIterator interface {
	IteratorSeeker

	// util.Releaser is the interface that wraps basic Release method.
	// When called Release will releases any resources associated with the
	// iterator.
	util.Releaser

	// util.ReleaseSetter is the interface that wraps the basic SetReleaser
	// method.
	util.ReleaseSetter

	// TODO: Remove this when ready.
	Valid() bool

	// Error returns any accumulated error. Exhausting all the key/value pairs
	// is not considered to be an error.
	Error() error
}

// Iterator iterates over a DB's key/value pairs in key order.
//
// When encounter an error any 'seeks method' will return false and will
// yield no key/value pairs. The error can be queried by calling the Error
// method. Calling Release is still necessary.
//
// An iterator must be released after use, but it is not necessary to read
// an iterator until exhaustion.
// Also, an iterator is not necessarily safe for concurrent use, but it is
// safe to use multiple iterators concurrently, with each in a dedicated
// goroutine.
type Iterator interface {
	CommonIterator

	// Key returns the key of the current key/value pair, or nil if done.
	// The caller should not modify the contents of the returned slice, and
	// its contents may change on the next call to any 'seeks method'.
	Key() []byte

	// Value returns the value of the current key/value pair, or nil if done.
	// The caller should not modify the contents of the returned slice, and
	// its contents may change on the next call to any 'seeks method'.
	Value() []byte
}

// ErrorCallbackSetter is the interface that wraps basic SetErrorCallback
// method.
//
// ErrorCallbackSetter implemented by indexed and merged iterator.
type ErrorCallbackSetter interface {
	// SetErrorCallback allows set an error callback of the corresponding
	// iterator. Use nil to clear the callback.
	SetErrorCallback(f func(err error))
}

type emptyIterator struct {
	util.BasicReleaser
	err error
}

func (i *emptyIterator) rErr() {
	if i.err == nil && i.Released() {
		i.err = ErrIterReleased
	}
}

func (*emptyIterator) Valid() bool            { return false }
func (i *emptyIterator) First() bool          { i.rErr(); return false }
func (i *emptyIterator) Last() bool           { i.rErr(); return false }
func (i *emptyIterator) Seek(key []byte) bool { i.rErr(); return false }
func (i *emptyIterator) Next() bool           { i.rErr(); return false }
func (i *emptyIterator) Prev() bool           { i.rErr(); return false }
func (*emptyIterator) Key() []byte            { return nil }
func (*emptyIterator) Value() []byte          { return nil }
func (i *emptyIterator) Error() error         { return i.err }

// NewEmptyIterator creates an empty iterator. The err parameter can be
// nil, but if not nil the given err will be returned by Error method.
func NewEmptyIterator(err error) Iterator {
	return &emptyIterator{err: err}
}
```

## File: `leveldb/iterator/iter_suite_test.go`
```go
package iterator_test

import (
	"testing"

	"github.com/syndtr/goleveldb/leveldb/testutil"
)

func TestIterator(t *testing.T) {
	testutil.RunSuite(t, "Iterator Suite")
}
```

## File: `leveldb/iterator/merged_iter.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package iterator

import (
	"container/heap"

	"github.com/syndtr/goleveldb/leveldb/comparer"
	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/util"
)

type dir int

const (
	dirReleased dir = iota - 1
	dirSOI
	dirEOI
	dirBackward
	dirForward
)

type mergedIterator struct {
	cmp    comparer.Comparer
	iters  []Iterator
	strict bool

	keys     [][]byte
	index    int
	dir      dir
	err      error
	errf     func(err error)
	releaser util.Releaser

	indexes []int // the heap of iterator indexes
	reverse bool  //nolint: structcheck // if true, indexes is a max-heap
}

func assertKey(key []byte) []byte {
	if key == nil {
		panic("leveldb/iterator: nil key")
	}
	return key
}

func (i *mergedIterator) iterErr(iter Iterator) bool {
	if err := iter.Error(); err != nil {
		if i.errf != nil {
			i.errf(err)
		}
		if i.strict || !errors.IsCorrupted(err) {
			i.err = err
			return true
		}
	}
	return false
}

func (i *mergedIterator) Valid() bool {
	return i.err == nil && i.dir > dirEOI
}

func (i *mergedIterator) First() bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	h := i.indexHeap()
	h.Reset(false)
	for x, iter := range i.iters {
		switch {
		case iter.First():
			i.keys[x] = assertKey(iter.Key())
			h.Push(x)
		case i.iterErr(iter):
			return false
		default:
			i.keys[x] = nil
		}
	}
	heap.Init(h)
	i.dir = dirSOI
	return i.next()
}

func (i *mergedIterator) Last() bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	h := i.indexHeap()
	h.Reset(true)
	for x, iter := range i.iters {
		switch {
		case iter.Last():
			i.keys[x] = assertKey(iter.Key())
			h.Push(x)
		case i.iterErr(iter):
			return false
		default:
			i.keys[x] = nil
		}
	}
	heap.Init(h)
	i.dir = dirEOI
	return i.prev()
}

func (i *mergedIterator) Seek(key []byte) bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	h := i.indexHeap()
	h.Reset(false)
	for x, iter := range i.iters {
		switch {
		case iter.Seek(key):
			i.keys[x] = assertKey(iter.Key())
			h.Push(x)
		case i.iterErr(iter):
			return false
		default:
			i.keys[x] = nil
		}
	}
	heap.Init(h)
	i.dir = dirSOI
	return i.next()
}

func (i *mergedIterator) next() bool {
	h := i.indexHeap()
	if h.Len() == 0 {
		i.dir = dirEOI
		return false
	}
	i.index = heap.Pop(h).(int)
	i.dir = dirForward
	return true
}

func (i *mergedIterator) Next() bool {
	if i.dir == dirEOI || i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	switch i.dir {
	case dirSOI:
		return i.First()
	case dirBackward:
		key := append([]byte(nil), i.keys[i.index]...)
		if !i.Seek(key) {
			return false
		}
		return i.Next()
	}

	x := i.index
	iter := i.iters[x]
	switch {
	case iter.Next():
		i.keys[x] = assertKey(iter.Key())
		heap.Push(i.indexHeap(), x)
	case i.iterErr(iter):
		return false
	default:
		i.keys[x] = nil
	}
	return i.next()
}

func (i *mergedIterator) prev() bool {
	h := i.indexHeap()
	if h.Len() == 0 {
		i.dir = dirSOI
		return false
	}
	i.index = heap.Pop(h).(int)
	i.dir = dirBackward
	return true
}

func (i *mergedIterator) Prev() bool {
	if i.dir == dirSOI || i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	switch i.dir {
	case dirEOI:
		return i.Last()
	case dirForward:
		key := append([]byte(nil), i.keys[i.index]...)
		h := i.indexHeap()
		h.Reset(true)
		for x, iter := range i.iters {
			if x == i.index {
				continue
			}
			seek := iter.Seek(key)
			switch {
			case seek && iter.Prev(), !seek && iter.Last():
				i.keys[x] = assertKey(iter.Key())
				h.Push(x)
			case i.iterErr(iter):
				return false
			default:
				i.keys[x] = nil
			}
		}
		heap.Init(h)
	}

	x := i.index
	iter := i.iters[x]
	switch {
	case iter.Prev():
		i.keys[x] = assertKey(iter.Key())
		heap.Push(i.indexHeap(), x)
	case i.iterErr(iter):
		return false
	default:
		i.keys[x] = nil
	}
	return i.prev()
}

func (i *mergedIterator) Key() []byte {
	if i.err != nil || i.dir <= dirEOI {
		return nil
	}
	return i.keys[i.index]
}

func (i *mergedIterator) Value() []byte {
	if i.err != nil || i.dir <= dirEOI {
		return nil
	}
	return i.iters[i.index].Value()
}

func (i *mergedIterator) Release() {
	if i.dir != dirReleased {
		i.dir = dirReleased
		for _, iter := range i.iters {
			iter.Release()
		}
		i.iters = nil
		i.keys = nil
		i.indexes = nil
		if i.releaser != nil {
			i.releaser.Release()
			i.releaser = nil
		}
	}
}

func (i *mergedIterator) SetReleaser(releaser util.Releaser) {
	if i.dir == dirReleased {
		panic(util.ErrReleased)
	}
	if i.releaser != nil && releaser != nil {
		panic(util.ErrHasReleaser)
	}
	i.releaser = releaser
}

func (i *mergedIterator) Error() error {
	return i.err
}

func (i *mergedIterator) SetErrorCallback(f func(err error)) {
	i.errf = f
}

func (i *mergedIterator) indexHeap() *indexHeap {
	return (*indexHeap)(i)
}

// NewMergedIterator returns an iterator that merges its input. Walking the
// resultant iterator will return all key/value pairs of all input iterators
// in strictly increasing key order, as defined by cmp.
// The input's key ranges may overlap, but there are assumed to be no duplicate
// keys: if iters[i] contains a key k then iters[j] will not contain that key k.
// None of the iters may be nil.
//
// If strict is true the any 'corruption errors' (i.e errors.IsCorrupted(err) == true)
// won't be ignored and will halt 'merged iterator', otherwise the iterator will
// continue to the next 'input iterator'.
func NewMergedIterator(iters []Iterator, cmp comparer.Comparer, strict bool) Iterator {
	return &mergedIterator{
		iters:   iters,
		cmp:     cmp,
		strict:  strict,
		keys:    make([][]byte, len(iters)),
		indexes: make([]int, 0, len(iters)),
	}
}

// indexHeap implements heap.Interface.
type indexHeap mergedIterator

func (h *indexHeap) Len() int { return len(h.indexes) }
func (h *indexHeap) Less(i, j int) bool {
	i, j = h.indexes[i], h.indexes[j]
	r := h.cmp.Compare(h.keys[i], h.keys[j])
	if h.reverse {
		return r > 0
	}
	return r < 0
}

func (h *indexHeap) Swap(i, j int) {
	h.indexes[i], h.indexes[j] = h.indexes[j], h.indexes[i]
}

func (h *indexHeap) Push(value interface{}) {
	h.indexes = append(h.indexes, value.(int))
}

func (h *indexHeap) Pop() interface{} {
	e := len(h.indexes) - 1
	popped := h.indexes[e]
	h.indexes = h.indexes[:e]
	return popped
}

func (h *indexHeap) Reset(reverse bool) {
	h.reverse = reverse
	h.indexes = h.indexes[:0]
}
```

## File: `leveldb/iterator/merged_iter_test.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package iterator_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/comparer"
	. "github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/testutil"
)

var _ = testutil.Defer(func() {
	Describe("Merged iterator", func() {
		Test := func(filled int, empty int) func() {
			return func() {
				It("Should iterates and seeks correctly", func(done Done) {
					rnd := testutil.NewRand()

					// Build key/value.
					filledKV := make([]testutil.KeyValue, filled)
					kv := testutil.KeyValue_Generate(nil, 100, 1, 1, 10, 4, 4)
					kv.Iterate(func(i int, key, value []byte) {
						filledKV[rnd.Intn(filled)].Put(key, value)
					})

					// Create itearators.
					iters := make([]Iterator, filled+empty)
					for i := range iters {
						if empty == 0 || (rnd.Int()%2 == 0 && filled > 0) {
							filled--
							Expect(filledKV[filled].Len()).ShouldNot(BeZero())
							iters[i] = NewArrayIterator(filledKV[filled])
						} else {
							empty--
							iters[i] = NewEmptyIterator(nil)
						}
					}

					// Test the iterator.
					t := testutil.IteratorTesting{
						KeyValue: kv.Clone(),
						Iter:     NewMergedIterator(iters, comparer.DefaultComparer, true),
					}
					testutil.DoIteratorTesting(&t)
					done <- true
				}, 15.0)
			}
		}

		Describe("with three, all filled iterators", Test(3, 0))
		Describe("with one filled, one empty iterators", Test(1, 1))
		Describe("with one filled, two empty iterators", Test(1, 2))
	})
})

func BenchmarkMergedIterator(b *testing.B) {
	n := 11
	iters := make([]Iterator, n)
	for i := range iters {
		kv := testutil.KeyValue_Generate(nil, 100, 1, 1, 10, 4, 4)
		iters[i] = NewArrayIterator(kv)
	}

	mi := NewMergedIterator(iters, comparer.DefaultComparer, true)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		mi.First()
		for mi.Next() {
			mi.Key()
		}
	}
}
```

## File: `leveldb/journal/journal.go`
```go
// Copyright 2011 The LevelDB-Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Taken from: https://code.google.com/p/leveldb-go/source/browse/leveldb/record/record.go?r=1d5ccbe03246da926391ee12d1c6caae054ff4b0
// License, authors and contributors informations can be found at bellow URLs respectively:
// 	https://code.google.com/p/leveldb-go/source/browse/LICENSE
//	https://code.google.com/p/leveldb-go/source/browse/AUTHORS
//  https://code.google.com/p/leveldb-go/source/browse/CONTRIBUTORS

// Package journal reads and writes sequences of journals. Each journal is a stream
// of bytes that completes before the next journal starts.
//
// When reading, call Next to obtain an io.Reader for the next journal. Next will
// return io.EOF when there are no more journals. It is valid to call Next
// without reading the current journal to exhaustion.
//
// When writing, call Next to obtain an io.Writer for the next journal. Calling
// Next finishes the current journal. Call Close to finish the final journal.
//
// Optionally, call Flush to finish the current journal and flush the underlying
// writer without starting a new journal. To start a new journal after flushing,
// call Next.
//
// Neither Readers or Writers are safe to use concurrently.
//
// Example code:
//	func read(r io.Reader) ([]string, error) {
//		var ss []string
//		journals := journal.NewReader(r, nil, true, true)
//		for {
//			j, err := journals.Next()
//			if err == io.EOF {
//				break
//			}
//			if err != nil {
//				return nil, err
//			}
//			s, err := ioutil.ReadAll(j)
//			if err != nil {
//				return nil, err
//			}
//			ss = append(ss, string(s))
//		}
//		return ss, nil
//	}
//
//	func write(w io.Writer, ss []string) error {
//		journals := journal.NewWriter(w)
//		for _, s := range ss {
//			j, err := journals.Next()
//			if err != nil {
//				return err
//			}
//			if _, err := j.Write([]byte(s)), err != nil {
//				return err
//			}
//		}
//		return journals.Close()
//	}
//
// The wire format is that the stream is divided into 32KiB blocks, and each
// block contains a number of tightly packed chunks. Chunks cannot cross block
// boundaries. The last block may be shorter than 32 KiB. Any unused bytes in a
// block must be zero.
//
// A journal maps to one or more chunks. Each chunk has a 7 byte header (a 4
// byte checksum, a 2 byte little-endian uint16 length, and a 1 byte chunk type)
// followed by a payload. The checksum is over the chunk type and the payload.
//
// There are four chunk types: whether the chunk is the full journal, or the
// first, middle or last chunk of a multi-chunk journal. A multi-chunk journal
// has one first chunk, zero or more middle chunks, and one last chunk.
//
// The wire format allows for limited recovery in the face of data corruption:
// on a format error (such as a checksum mismatch), the reader moves to the
// next block and looks for the next full or first chunk.
package journal

import (
	"encoding/binary"
	"fmt"
	"io"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/util"
)

// These constants are part of the wire format and should not be changed.
const (
	fullChunkType   = 1
	firstChunkType  = 2
	middleChunkType = 3
	lastChunkType   = 4
)

const (
	blockSize  = 32 * 1024
	headerSize = 7
)

type flusher interface {
	Flush() error
}

// ErrCorrupted is the error type that generated by corrupted block or chunk.
type ErrCorrupted struct {
	Size   int
	Reason string
}

func (e *ErrCorrupted) Error() string {
	return fmt.Sprintf("leveldb/journal: block/chunk corrupted: %s (%d bytes)", e.Reason, e.Size)
}

// Dropper is the interface that wrap simple Drop method. The Drop
// method will be called when the journal reader dropping a block or chunk.
type Dropper interface {
	Drop(err error)
}

// Reader reads journals from an underlying io.Reader.
type Reader struct {
	// r is the underlying reader.
	r io.Reader
	// the dropper.
	dropper Dropper
	// strict flag.
	strict bool
	// checksum flag.
	checksum bool
	// seq is the sequence number of the current journal.
	seq int
	// buf[i:j] is the unread portion of the current chunk's payload.
	// The low bound, i, excludes the chunk header.
	i, j int
	// n is the number of bytes of buf that are valid. Once reading has started,
	// only the final block can have n < blockSize.
	n int
	// last is whether the current chunk is the last chunk of the journal.
	last bool
	// err is any accumulated error.
	err error
	// buf is the buffer.
	buf [blockSize]byte
}

// NewReader returns a new reader. The dropper may be nil, and if
// strict is true then corrupted or invalid chunk will halt the journal
// reader entirely.
func NewReader(r io.Reader, dropper Dropper, strict, checksum bool) *Reader {
	return &Reader{
		r:        r,
		dropper:  dropper,
		strict:   strict,
		checksum: checksum,
		last:     true,
	}
}

var errSkip = errors.New("leveldb/journal: skipped")

func (r *Reader) corrupt(n int, reason string, skip bool) error {
	if r.dropper != nil {
		r.dropper.Drop(&ErrCorrupted{n, reason})
	}
	if r.strict && !skip {
		r.err = errors.NewErrCorrupted(storage.FileDesc{}, &ErrCorrupted{n, reason})
		return r.err
	}
	return errSkip
}

// nextChunk sets r.buf[r.i:r.j] to hold the next chunk's payload, reading the
// next block into the buffer if necessary.
func (r *Reader) nextChunk(first bool) error {
	for {
		if r.j+headerSize <= r.n {
			checksum := binary.LittleEndian.Uint32(r.buf[r.j+0 : r.j+4])
			length := binary.LittleEndian.Uint16(r.buf[r.j+4 : r.j+6])
			chunkType := r.buf[r.j+6]
			unprocBlock := r.n - r.j
			if checksum == 0 && length == 0 && chunkType == 0 {
				// Drop entire block.
				r.i = r.n
				r.j = r.n
				return r.corrupt(unprocBlock, "zero header", false)
			}
			if chunkType < fullChunkType || chunkType > lastChunkType {
				// Drop entire block.
				r.i = r.n
				r.j = r.n
				return r.corrupt(unprocBlock, fmt.Sprintf("invalid chunk type %#x", chunkType), false)
			}
			r.i = r.j + headerSize
			r.j = r.j + headerSize + int(length)
			if r.j > r.n {
				// Drop entire block.
				r.i = r.n
				r.j = r.n
				return r.corrupt(unprocBlock, "chunk length overflows block", false)
			} else if r.checksum && checksum != util.NewCRC(r.buf[r.i-1:r.j]).Value() {
				// Drop entire block.
				r.i = r.n
				r.j = r.n
				return r.corrupt(unprocBlock, "checksum mismatch", false)
			}
			if first && chunkType != fullChunkType && chunkType != firstChunkType {
				chunkLength := (r.j - r.i) + headerSize
				r.i = r.j
				// Report the error, but skip it.
				return r.corrupt(chunkLength, "orphan chunk", true)
			}
			r.last = chunkType == fullChunkType || chunkType == lastChunkType
			return nil
		}

		// The last block.
		if r.n < blockSize && r.n > 0 {
			if !first {
				return r.corrupt(0, "missing chunk part", false)
			}
			r.err = io.EOF
			return r.err
		}

		// Read block.
		n, err := io.ReadFull(r.r, r.buf[:])
		if err != nil && err != io.EOF && err != io.ErrUnexpectedEOF {
			return err
		}
		if n == 0 {
			if !first {
				return r.corrupt(0, "missing chunk part", false)
			}
			r.err = io.EOF
			return r.err
		}
		r.i, r.j, r.n = 0, 0, n
	}
}

// Next returns a reader for the next journal. It returns io.EOF if there are no
// more journals. The reader returned becomes stale after the next Next call,
// and should no longer be used. If strict is false, the reader will returns
// io.ErrUnexpectedEOF error when found corrupted journal.
func (r *Reader) Next() (io.Reader, error) {
	r.seq++
	if r.err != nil {
		return nil, r.err
	}
	r.i = r.j
	for {
		if err := r.nextChunk(true); err == nil {
			break
		} else if err != errSkip {
			return nil, err
		}
	}
	return &singleReader{r, r.seq, nil}, nil
}

// Reset resets the journal reader, allows reuse of the journal reader. Reset returns
// last accumulated error.
func (r *Reader) Reset(reader io.Reader, dropper Dropper, strict, checksum bool) error {
	r.seq++
	err := r.err
	r.r = reader
	r.dropper = dropper
	r.strict = strict
	r.checksum = checksum
	r.i = 0
	r.j = 0
	r.n = 0
	r.last = true
	r.err = nil
	return err
}

type singleReader struct {
	r   *Reader
	seq int
	err error
}

func (x *singleReader) Read(p []byte) (int, error) {
	r := x.r
	if r.seq != x.seq {
		return 0, errors.New("leveldb/journal: stale reader")
	}
	if x.err != nil {
		return 0, x.err
	}
	if r.err != nil {
		return 0, r.err
	}
	for r.i == r.j {
		if r.last {
			return 0, io.EOF
		}
		x.err = r.nextChunk(false)
		if x.err != nil {
			if x.err == errSkip {
				x.err = io.ErrUnexpectedEOF
			}
			return 0, x.err
		}
	}
	n := copy(p, r.buf[r.i:r.j])
	r.i += n
	return n, nil
}

func (x *singleReader) ReadByte() (byte, error) {
	r := x.r
	if r.seq != x.seq {
		return 0, errors.New("leveldb/journal: stale reader")
	}
	if x.err != nil {
		return 0, x.err
	}
	if r.err != nil {
		return 0, r.err
	}
	for r.i == r.j {
		if r.last {
			return 0, io.EOF
		}
		x.err = r.nextChunk(false)
		if x.err != nil {
			if x.err == errSkip {
				x.err = io.ErrUnexpectedEOF
			}
			return 0, x.err
		}
	}
	c := r.buf[r.i]
	r.i++
	return c, nil
}

// Writer writes journals to an underlying io.Writer.
type Writer struct {
	// w is the underlying writer.
	w io.Writer
	// seq is the sequence number of the current journal.
	seq int
	// f is w as a flusher.
	f flusher
	// buf[i:j] is the bytes that will become the current chunk.
	// The low bound, i, includes the chunk header.
	i, j int
	// buf[:written] has already been written to w.
	// written is zero unless Flush has been called.
	written int
	// blockNumber is the zero based block number currently held in buf.
	blockNumber int64
	// first is whether the current chunk is the first chunk of the journal.
	first bool
	// pending is whether a chunk is buffered but not yet written.
	pending bool
	// err is any accumulated error.
	err error
	// buf is the buffer.
	buf [blockSize]byte
}

// NewWriter returns a new Writer.
func NewWriter(w io.Writer) *Writer {
	f, _ := w.(flusher)
	return &Writer{
		w: w,
		f: f,
	}
}

// fillHeader fills in the header for the pending chunk.
func (w *Writer) fillHeader(last bool) {
	if w.i+headerSize > w.j || w.j > blockSize {
		panic("leveldb/journal: bad writer state")
	}
	if last {
		if w.first {
			w.buf[w.i+6] = fullChunkType
		} else {
			w.buf[w.i+6] = lastChunkType
		}
	} else {
		if w.first {
			w.buf[w.i+6] = firstChunkType
		} else {
			w.buf[w.i+6] = middleChunkType
		}
	}
	binary.LittleEndian.PutUint32(w.buf[w.i+0:w.i+4], util.NewCRC(w.buf[w.i+6:w.j]).Value())
	binary.LittleEndian.PutUint16(w.buf[w.i+4:w.i+6], uint16(w.j-w.i-headerSize))
}

// writeBlock writes the buffered block to the underlying writer, and reserves
// space for the next chunk's header.
func (w *Writer) writeBlock() {
	_, w.err = w.w.Write(w.buf[w.written:])
	w.i = 0
	w.j = headerSize
	w.written = 0
	w.blockNumber++
}

// writePending finishes the current journal and writes the buffer to the
// underlying writer.
func (w *Writer) writePending() {
	if w.err != nil {
		return
	}
	if w.pending {
		w.fillHeader(true)
		w.pending = false
	}
	_, w.err = w.w.Write(w.buf[w.written:w.j])
	w.written = w.j
}

// Close finishes the current journal and closes the writer.
func (w *Writer) Close() error {
	w.seq++
	w.writePending()
	if w.err != nil {
		return w.err
	}
	w.err = errors.New("leveldb/journal: closed Writer")
	return nil
}

// Flush finishes the current journal, writes to the underlying writer, and
// flushes it if that writer implements interface{ Flush() error }.
func (w *Writer) Flush() error {
	w.seq++
	w.writePending()
	if w.err != nil {
		return w.err
	}
	if w.f != nil {
		w.err = w.f.Flush()
		return w.err
	}
	return nil
}

// Reset resets the journal writer, allows reuse of the journal writer. Reset
// will also closes the journal writer if not already.
func (w *Writer) Reset(writer io.Writer) (err error) {
	w.seq++
	if w.err == nil {
		w.writePending()
		err = w.err
	}
	w.w = writer
	w.f, _ = writer.(flusher)
	w.i = 0
	w.j = 0
	w.written = 0
	w.blockNumber = 0
	w.first = false
	w.pending = false
	w.err = nil
	return
}

// Next returns a writer for the next journal. The writer returned becomes stale
// after the next Close, Flush or Next call, and should no longer be used.
func (w *Writer) Next() (io.Writer, error) {
	w.seq++
	if w.err != nil {
		return nil, w.err
	}
	if w.pending {
		w.fillHeader(true)
	}
	w.i = w.j
	w.j += headerSize
	// Check if there is room in the block for the header.
	if w.j > blockSize {
		// Fill in the rest of the block with zeroes.
		for k := w.i; k < blockSize; k++ {
			w.buf[k] = 0
		}
		w.writeBlock()
		if w.err != nil {
			return nil, w.err
		}
	}
	w.first = true
	w.pending = true
	return singleWriter{w, w.seq}, nil
}

// Size returns the current size of the file.
func (w *Writer) Size() int64 {
	if w == nil {
		return 0
	}
	return w.blockNumber*blockSize + int64(w.j)
}

type singleWriter struct {
	w   *Writer
	seq int
}

func (x singleWriter) Write(p []byte) (int, error) {
	w := x.w
	if w.seq != x.seq {
		return 0, errors.New("leveldb/journal: stale writer")
	}
	if w.err != nil {
		return 0, w.err
	}
	n0 := len(p)
	for len(p) > 0 {
		// Write a block, if it is full.
		if w.j == blockSize {
			w.fillHeader(false)
			w.writeBlock()
			if w.err != nil {
				return 0, w.err
			}
			w.first = false
		}
		// Copy bytes into the buffer.
		n := copy(w.buf[w.j:], p)
		w.j += n
		p = p[n:]
	}
	return n0, nil
}
```

## File: `leveldb/journal/journal_test.go`
```go
// Copyright 2011 The LevelDB-Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Taken from: https://code.google.com/p/leveldb-go/source/browse/leveldb/record/record_test.go?r=df1fa28f7f3be6c3935548169002309c12967135
// License, authors and contributors informations can be found at bellow URLs respectively:
// 	https://code.google.com/p/leveldb-go/source/browse/LICENSE
//	https://code.google.com/p/leveldb-go/source/browse/AUTHORS
//  https://code.google.com/p/leveldb-go/source/browse/CONTRIBUTORS

package journal

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"io"
	"io/ioutil"
	"math/rand"
	"strings"
	"testing"

	"github.com/stretchr/testify/require"
)

type dropper struct {
	t *testing.T
}

func (d dropper) Drop(err error) {
	d.t.Log(err)
}

func short(s string) string {
	if len(s) < 64 {
		return s
	}
	return fmt.Sprintf("%s...(skipping %d bytes)...%s", s[:20], len(s)-40, s[len(s)-20:])
}

// big returns a string of length n, composed of repetitions of partial.
func big(partial string, n int) string {
	return strings.Repeat(partial, n/len(partial)+1)[:n]
}

func TestEmpty(t *testing.T) {
	buf := new(bytes.Buffer)
	r := NewReader(buf, dropper{t}, true, true)
	if _, err := r.Next(); err != io.EOF {
		t.Fatalf("got %v, want %v", err, io.EOF)
	}
}

func testGenerator(t *testing.T, reset func(), gen func() (string, bool)) {
	buf := new(bytes.Buffer)

	reset()
	w := NewWriter(buf)
	for {
		s, ok := gen()
		if !ok {
			break
		}
		ww, err := w.Next()
		if err != nil {
			t.Fatal(err)
		}
		if _, err := ww.Write([]byte(s)); err != nil {
			t.Fatal(err)
		}
	}
	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	reset()
	r := NewReader(buf, dropper{t}, true, true)
	for {
		s, ok := gen()
		if !ok {
			break
		}
		rr, err := r.Next()
		if err != nil {
			t.Fatal(err)
		}
		x, err := ioutil.ReadAll(rr)
		if err != nil {
			t.Fatal(err)
		}
		if string(x) != s {
			t.Fatalf("got %q, want %q", short(string(x)), short(s))
		}
	}
	if _, err := r.Next(); err != io.EOF {
		t.Fatalf("got %v, want %v", err, io.EOF)
	}
}

func testLiterals(t *testing.T, s []string) {
	var i int
	reset := func() {
		i = 0
	}
	gen := func() (string, bool) {
		if i == len(s) {
			return "", false
		}
		i++
		return s[i-1], true
	}
	testGenerator(t, reset, gen)
}

func TestMany(t *testing.T) {
	const n = 1e5
	var i int
	reset := func() {
		i = 0
	}
	gen := func() (string, bool) {
		if i == n {
			return "", false
		}
		i++
		return fmt.Sprintf("%d.", i-1), true
	}
	testGenerator(t, reset, gen)
}

func TestRandom(t *testing.T) {
	const n = 1e2
	var (
		i int
		r *rand.Rand
	)
	reset := func() {
		i, r = 0, rand.New(rand.NewSource(0))
	}
	gen := func() (string, bool) {
		if i == n {
			return "", false
		}
		i++
		return strings.Repeat(string(uint8(i)), r.Intn(2*blockSize+16)), true
	}
	testGenerator(t, reset, gen)
}

func TestBasic(t *testing.T) {
	testLiterals(t, []string{
		strings.Repeat("a", 1000),
		strings.Repeat("b", 97270),
		strings.Repeat("c", 8000),
	})
}

func TestBoundary(t *testing.T) {
	for i := blockSize - 16; i < blockSize+16; i++ {
		s0 := big("abcd", i)
		for j := blockSize - 16; j < blockSize+16; j++ {
			s1 := big("ABCDE", j)
			testLiterals(t, []string{s0, s1})
			testLiterals(t, []string{s0, "", s1})
			testLiterals(t, []string{s0, "x", s1})
		}
	}
}

func TestFlush(t *testing.T) {
	buf := new(bytes.Buffer)
	w := NewWriter(buf)
	// Write a couple of records. Everything should still be held
	// in the record.Writer buffer, so that buf.Len should be 0.
	w0, _ := w.Next()
	if _, err := w0.Write([]byte("0")); err != nil {
		t.Fatal(err)
	}
	w1, _ := w.Next()
	if _, err := w1.Write([]byte("11")); err != nil {
		t.Fatal(err)
	}
	if got, want := buf.Len(), 0; got != want {
		t.Fatalf("buffer length #0: got %d want %d", got, want)
	}
	// Flush the record.Writer buffer, which should yield 17 bytes.
	// 17 = 2*7 + 1 + 2, which is two headers and 1 + 2 payload bytes.
	if err := w.Flush(); err != nil {
		t.Fatal(err)
	}
	if got, want := buf.Len(), 17; got != want {
		t.Fatalf("buffer length #1: got %d want %d", got, want)
	}
	// Do another write, one that isn't large enough to complete the block.
	// The write should not have flowed through to buf.
	w2, _ := w.Next()
	if _, err := w2.Write(bytes.Repeat([]byte("2"), 10000)); err != nil {
		t.Fatal(err)
	}
	if got, want := buf.Len(), 17; got != want {
		t.Fatalf("buffer length #2: got %d want %d", got, want)
	}
	// Flushing should get us up to 10024 bytes written.
	// 10024 = 17 + 7 + 10000.
	if err := w.Flush(); err != nil {
		t.Fatal(err)
	}
	if got, want := buf.Len(), 10024; got != want {
		t.Fatalf("buffer length #3: got %d want %d", got, want)
	}
	// Do a bigger write, one that completes the current block.
	// We should now have 32768 bytes (a complete block), without
	// an explicit flush.
	w3, _ := w.Next()
	if _, err := w3.Write(bytes.Repeat([]byte("3"), 40000)); err != nil {
		t.Fatal(err)
	}
	if got, want := buf.Len(), 32768; got != want {
		t.Fatalf("buffer length #4: got %d want %d", got, want)
	}
	// Flushing should get us up to 50038 bytes written.
	// 50038 = 10024 + 2*7 + 40000. There are two headers because
	// the one record was split into two chunks.
	if err := w.Flush(); err != nil {
		t.Fatal(err)
	}
	if got, want := buf.Len(), 50038; got != want {
		t.Fatalf("buffer length #5: got %d want %d", got, want)
	}
	// Check that reading those records give the right lengths.
	r := NewReader(buf, dropper{t}, true, true)
	wants := []int64{1, 2, 10000, 40000}
	for i, want := range wants {
		rr, _ := r.Next()
		n, err := io.Copy(ioutil.Discard, rr)
		if err != nil {
			t.Fatalf("read #%d: %v", i, err)
		}
		if n != want {
			t.Fatalf("read #%d: got %d bytes want %d", i, n, want)
		}
	}
}

func TestNonExhaustiveRead(t *testing.T) {
	const n = 100
	buf := new(bytes.Buffer)
	p := make([]byte, 10)
	rnd := rand.New(rand.NewSource(1))

	w := NewWriter(buf)
	for i := 0; i < n; i++ {
		length := len(p) + rnd.Intn(3*blockSize)
		s := string(uint8(i)) + "123456789abcdefgh"
		ww, _ := w.Next()
		if _, err := ww.Write([]byte(big(s, length))); err != nil {
			t.Fatal(err)
		}
	}
	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	r := NewReader(buf, dropper{t}, true, true)
	for i := 0; i < n; i++ {
		rr, _ := r.Next()
		_, err := io.ReadFull(rr, p)
		if err != nil {
			t.Fatal(err)
		}
		want := string(uint8(i)) + "123456789"
		if got := string(p); got != want {
			t.Fatalf("read #%d: got %q want %q", i, got, want)
		}
	}
}

func TestStaleReader(t *testing.T) {
	buf := new(bytes.Buffer)

	w := NewWriter(buf)
	w0, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := w0.Write([]byte("0")); err != nil {
		t.Fatal(err)
	}
	w1, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := w1.Write([]byte("11")); err != nil {
		t.Fatal(err)
	}
	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	r := NewReader(buf, dropper{t}, true, true)
	r0, err := r.Next()
	if err != nil {
		t.Fatal(err)
	}
	r1, err := r.Next()
	if err != nil {
		t.Fatal(err)
	}
	p := make([]byte, 1)
	if _, err := r0.Read(p); err == nil || !strings.Contains(err.Error(), "stale") {
		t.Fatalf("stale read #0: unexpected error: %v", err)
	}
	if _, err := r1.Read(p); err != nil {
		t.Fatalf("fresh read #1: got %v want nil error", err)
	}
	if p[0] != '1' {
		t.Fatalf("fresh read #1: byte contents: got '%c' want '1'", p[0])
	}
}

func TestStaleWriter(t *testing.T) {
	buf := new(bytes.Buffer)

	w := NewWriter(buf)
	w0, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	w1, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := w0.Write([]byte("0")); err == nil || !strings.Contains(err.Error(), "stale") {
		t.Fatalf("stale write #0: unexpected error: %v", err)
	}
	if _, err := w1.Write([]byte("11")); err != nil {
		t.Fatalf("fresh write #1: got %v want nil error", err)
	}
	if err := w.Flush(); err != nil {
		t.Fatalf("flush: %v", err)
	}
	if _, err := w1.Write([]byte("0")); err == nil || !strings.Contains(err.Error(), "stale") {
		t.Fatalf("stale write #1: unexpected error: %v", err)
	}
}

func TestSize(t *testing.T) {
	var buf bytes.Buffer
	zeroes := make([]byte, 8<<10)
	w := NewWriter(&buf)
	for i := 0; i < 100; i++ {
		writer, err := w.Next()
		require.NoError(t, err)

		for j := 0; j < rand.Intn(10); j++ {
			n := rand.Intn(len(zeroes))
			_, err = writer.Write(zeroes[:n])
			require.NoError(t, err)
		}

		require.NoError(t, w.Flush())
		if buf.Len() != int(w.Size()) {
			t.Fatalf("expected %d, but found %d", buf.Len(), w.Size())
		}
	}
	require.NoError(t, w.Close())
}

func TestCorrupt_MissingLastBlock(t *testing.T) {
	buf := new(bytes.Buffer)

	w := NewWriter(buf)

	// First record.
	ww, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize-1024)); err != nil {
		t.Fatalf("write #0: unexpected error: %v", err)
	}

	// Second record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize-headerSize)); err != nil {
		t.Fatalf("write #1: unexpected error: %v", err)
	}

	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	// Cut the last block.
	b := buf.Bytes()[:blockSize]
	r := NewReader(bytes.NewReader(b), dropper{t}, false, true)

	// First read.
	rr, err := r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err := io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #0: %v", err)
	}
	if n != blockSize-1024 {
		t.Fatalf("read #0: got %d bytes want %d", n, blockSize-1024)
	}

	// Second read.
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	_, err = io.Copy(ioutil.Discard, rr)
	if err != io.ErrUnexpectedEOF {
		t.Fatalf("read #1: unexpected error: %v", err)
	}

	if _, err := r.Next(); err != io.EOF {
		t.Fatalf("last next: unexpected error: %v", err)
	}
}

func TestCorrupt_CorruptedFirstBlock(t *testing.T) {
	buf := new(bytes.Buffer)

	w := NewWriter(buf)

	// First record.
	ww, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize/2)); err != nil {
		t.Fatalf("write #0: unexpected error: %v", err)
	}

	// Second record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize-headerSize)); err != nil {
		t.Fatalf("write #1: unexpected error: %v", err)
	}

	// Third record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), (blockSize-headerSize)+1)); err != nil {
		t.Fatalf("write #2: unexpected error: %v", err)
	}

	// Fourth record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), (blockSize-headerSize)+2)); err != nil {
		t.Fatalf("write #3: unexpected error: %v", err)
	}

	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	b := buf.Bytes()
	// Corrupting block #0.
	for i := 0; i < 1024; i++ {
		b[i] = '1'
	}

	r := NewReader(bytes.NewReader(b), dropper{t}, false, true)

	// First read (third record).
	rr, err := r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err := io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #0: %v", err)
	}
	if want := int64(blockSize-headerSize) + 1; n != want {
		t.Fatalf("read #0: got %d bytes want %d", n, want)
	}

	// Second read (fourth record).
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err = io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #1: %v", err)
	}
	if want := int64(blockSize-headerSize) + 2; n != want {
		t.Fatalf("read #1: got %d bytes want %d", n, want)
	}

	if _, err := r.Next(); err != io.EOF {
		t.Fatalf("last next: unexpected error: %v", err)
	}
}

func TestCorrupt_CorruptedMiddleBlock(t *testing.T) {
	buf := new(bytes.Buffer)

	w := NewWriter(buf)

	// First record.
	ww, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize/2)); err != nil {
		t.Fatalf("write #0: unexpected error: %v", err)
	}

	// Second record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize-headerSize)); err != nil {
		t.Fatalf("write #1: unexpected error: %v", err)
	}

	// Third record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), (blockSize-headerSize)+1)); err != nil {
		t.Fatalf("write #2: unexpected error: %v", err)
	}

	// Fourth record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), (blockSize-headerSize)+2)); err != nil {
		t.Fatalf("write #3: unexpected error: %v", err)
	}

	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	b := buf.Bytes()
	// Corrupting block #1.
	for i := 0; i < 1024; i++ {
		b[blockSize+i] = '1'
	}

	r := NewReader(bytes.NewReader(b), dropper{t}, false, true)

	// First read (first record).
	rr, err := r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err := io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #0: %v", err)
	}
	if want := int64(blockSize / 2); n != want {
		t.Fatalf("read #0: got %d bytes want %d", n, want)
	}

	// Second read (second record).
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	_, err = io.Copy(ioutil.Discard, rr)
	if err != io.ErrUnexpectedEOF {
		t.Fatalf("read #1: unexpected error: %v", err)
	}

	// Third read (fourth record).
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err = io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #2: %v", err)
	}
	if want := int64(blockSize-headerSize) + 2; n != want {
		t.Fatalf("read #2: got %d bytes want %d", n, want)
	}

	if _, err := r.Next(); err != io.EOF {
		t.Fatalf("last next: unexpected error: %v", err)
	}
}

func TestCorrupt_CorruptedLastBlock(t *testing.T) {
	buf := new(bytes.Buffer)

	w := NewWriter(buf)

	// First record.
	ww, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize/2)); err != nil {
		t.Fatalf("write #0: unexpected error: %v", err)
	}

	// Second record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize-headerSize)); err != nil {
		t.Fatalf("write #1: unexpected error: %v", err)
	}

	// Third record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), (blockSize-headerSize)+1)); err != nil {
		t.Fatalf("write #2: unexpected error: %v", err)
	}

	// Fourth record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), (blockSize-headerSize)+2)); err != nil {
		t.Fatalf("write #3: unexpected error: %v", err)
	}

	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	b := buf.Bytes()
	// Corrupting block #3.
	for i := len(b) - 1; i > len(b)-1024; i-- {
		b[i] = '1'
	}

	r := NewReader(bytes.NewReader(b), dropper{t}, false, true)

	// First read (first record).
	rr, err := r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err := io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #0: %v", err)
	}
	if want := int64(blockSize / 2); n != want {
		t.Fatalf("read #0: got %d bytes want %d", n, want)
	}

	// Second read (second record).
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err = io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #1: %v", err)
	}
	if want := int64(blockSize - headerSize); n != want {
		t.Fatalf("read #1: got %d bytes want %d", n, want)
	}

	// Third read (third record).
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err = io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #2: %v", err)
	}
	if want := int64(blockSize-headerSize) + 1; n != want {
		t.Fatalf("read #2: got %d bytes want %d", n, want)
	}

	// Fourth read (fourth record).
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	_, err = io.Copy(ioutil.Discard, rr)
	if err != io.ErrUnexpectedEOF {
		t.Fatalf("read #3: unexpected error: %v", err)
	}

	if _, err := r.Next(); err != io.EOF {
		t.Fatalf("last next: unexpected error: %v", err)
	}
}

func TestCorrupt_FirstChuckLengthOverflow(t *testing.T) {
	buf := new(bytes.Buffer)

	w := NewWriter(buf)

	// First record.
	ww, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize/2)); err != nil {
		t.Fatalf("write #0: unexpected error: %v", err)
	}

	// Second record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize-headerSize)); err != nil {
		t.Fatalf("write #1: unexpected error: %v", err)
	}

	// Third record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), (blockSize-headerSize)+1)); err != nil {
		t.Fatalf("write #2: unexpected error: %v", err)
	}

	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	b := buf.Bytes()
	// Corrupting record #1.
	x := blockSize
	binary.LittleEndian.PutUint16(b[x+4:], 0xffff)

	r := NewReader(bytes.NewReader(b), dropper{t}, false, true)

	// First read (first record).
	rr, err := r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err := io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #0: %v", err)
	}
	if want := int64(blockSize / 2); n != want {
		t.Fatalf("read #0: got %d bytes want %d", n, want)
	}

	// Second read (second record).
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	_, err = io.Copy(ioutil.Discard, rr)
	if err != io.ErrUnexpectedEOF {
		t.Fatalf("read #1: unexpected error: %v", err)
	}

	if _, err := r.Next(); err != io.EOF {
		t.Fatalf("last next: unexpected error: %v", err)
	}
}

func TestCorrupt_MiddleChuckLengthOverflow(t *testing.T) {
	buf := new(bytes.Buffer)

	w := NewWriter(buf)

	// First record.
	ww, err := w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize/2)); err != nil {
		t.Fatalf("write #0: unexpected error: %v", err)
	}

	// Second record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), blockSize-headerSize)); err != nil {
		t.Fatalf("write #1: unexpected error: %v", err)
	}

	// Third record.
	ww, err = w.Next()
	if err != nil {
		t.Fatal(err)
	}
	if _, err := ww.Write(bytes.Repeat([]byte("0"), (blockSize-headerSize)+1)); err != nil {
		t.Fatalf("write #2: unexpected error: %v", err)
	}

	if err := w.Close(); err != nil {
		t.Fatal(err)
	}

	b := buf.Bytes()
	// Corrupting record #1.
	x := blockSize/2 + headerSize
	binary.LittleEndian.PutUint16(b[x+4:], 0xffff)

	r := NewReader(bytes.NewReader(b), dropper{t}, false, true)

	// First read (first record).
	rr, err := r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err := io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #0: %v", err)
	}
	if want := int64(blockSize / 2); n != want {
		t.Fatalf("read #0: got %d bytes want %d", n, want)
	}

	// Second read (third record).
	rr, err = r.Next()
	if err != nil {
		t.Fatal(err)
	}
	n, err = io.Copy(ioutil.Discard, rr)
	if err != nil {
		t.Fatalf("read #1: %v", err)
	}
	if want := int64(blockSize-headerSize) + 1; n != want {
		t.Fatalf("read #1: got %d bytes want %d", n, want)
	}

	if _, err := r.Next(); err != io.EOF {
		t.Fatalf("last next: unexpected error: %v", err)
	}
}
```

## File: `leveldb/memdb/bench_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package memdb

import (
	"encoding/binary"
	"math/rand"
	"testing"

	"github.com/syndtr/goleveldb/leveldb/comparer"
)

func BenchmarkPut(b *testing.B) {
	buf := make([][4]byte, b.N)
	for i := range buf {
		binary.LittleEndian.PutUint32(buf[i][:], uint32(i))
	}

	b.ResetTimer()
	p := New(comparer.DefaultComparer, 0)
	for i := range buf {
		if err := p.Put(buf[i][:], nil); err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkPutRandom(b *testing.B) {
	buf := make([][4]byte, b.N)
	for i := range buf {
		binary.LittleEndian.PutUint32(buf[i][:], uint32(rand.Int()))
	}

	b.ResetTimer()
	p := New(comparer.DefaultComparer, 0)
	for i := range buf {
		if err := p.Put(buf[i][:], nil); err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkGet(b *testing.B) {
	buf := make([][4]byte, b.N)
	for i := range buf {
		binary.LittleEndian.PutUint32(buf[i][:], uint32(i))
	}

	p := New(comparer.DefaultComparer, 0)
	for i := range buf {
		if err := p.Put(buf[i][:], nil); err != nil {
			b.Fatal(err)
		}
	}

	b.ResetTimer()
	for i := range buf {
		if _, err := p.Get(buf[i][:]); err != nil {
			b.Fatal(err)
		}
	}
}

func BenchmarkGetRandom(b *testing.B) {
	buf := make([][4]byte, b.N)
	for i := range buf {
		binary.LittleEndian.PutUint32(buf[i][:], uint32(i))
	}

	p := New(comparer.DefaultComparer, 0)
	for i := range buf {
		if err := p.Put(buf[i][:], nil); err != nil {
			b.Fatal(err)
		}
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		if _, err := p.Get(buf[rand.Int()%b.N][:]); err != nil {
			b.Fatal(err)
		}
	}
}
```

## File: `leveldb/memdb/memdb.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package memdb provides in-memory key/value database implementation.
package memdb

import (
	"math/rand"
	"sync"

	"github.com/syndtr/goleveldb/leveldb/comparer"
	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/util"
)

// Common errors.
var (
	ErrNotFound     = errors.ErrNotFound
	ErrIterReleased = errors.New("leveldb/memdb: iterator released")
)

const tMaxHeight = 12

type dbIter struct {
	util.BasicReleaser
	p          *DB
	slice      *util.Range
	node       int
	forward    bool
	key, value []byte
	err        error
}

func (i *dbIter) fill(checkStart, checkLimit bool) bool {
	if i.node != 0 {
		n := i.p.nodeData[i.node]
		m := n + i.p.nodeData[i.node+nKey]
		i.key = i.p.kvData[n:m]
		if i.slice != nil {
			switch {
			case checkLimit && i.slice.Limit != nil && i.p.cmp.Compare(i.key, i.slice.Limit) >= 0:
				fallthrough
			case checkStart && i.slice.Start != nil && i.p.cmp.Compare(i.key, i.slice.Start) < 0:
				i.node = 0
				goto bail
			}
		}
		i.value = i.p.kvData[m : m+i.p.nodeData[i.node+nVal]]
		return true
	}
bail:
	i.key = nil
	i.value = nil
	return false
}

func (i *dbIter) Valid() bool {
	return i.node != 0
}

func (i *dbIter) First() bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	i.forward = true
	i.p.mu.RLock()
	defer i.p.mu.RUnlock()
	if i.slice != nil && i.slice.Start != nil {
		i.node, _ = i.p.findGE(i.slice.Start, false)
	} else {
		i.node = i.p.nodeData[nNext]
	}
	return i.fill(false, true)
}

func (i *dbIter) Last() bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	i.forward = false
	i.p.mu.RLock()
	defer i.p.mu.RUnlock()
	if i.slice != nil && i.slice.Limit != nil {
		i.node = i.p.findLT(i.slice.Limit)
	} else {
		i.node = i.p.findLast()
	}
	return i.fill(true, false)
}

func (i *dbIter) Seek(key []byte) bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	i.forward = true
	i.p.mu.RLock()
	defer i.p.mu.RUnlock()
	if i.slice != nil && i.slice.Start != nil && i.p.cmp.Compare(key, i.slice.Start) < 0 {
		key = i.slice.Start
	}
	i.node, _ = i.p.findGE(key, false)
	return i.fill(false, true)
}

func (i *dbIter) Next() bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	if i.node == 0 {
		if !i.forward {
			return i.First()
		}
		return false
	}
	i.forward = true
	i.p.mu.RLock()
	defer i.p.mu.RUnlock()
	i.node = i.p.nodeData[i.node+nNext]
	return i.fill(false, true)
}

func (i *dbIter) Prev() bool {
	if i.Released() {
		i.err = ErrIterReleased
		return false
	}

	if i.node == 0 {
		if i.forward {
			return i.Last()
		}
		return false
	}
	i.forward = false
	i.p.mu.RLock()
	defer i.p.mu.RUnlock()
	i.node = i.p.findLT(i.key)
	return i.fill(true, false)
}

func (i *dbIter) Key() []byte {
	return i.key
}

func (i *dbIter) Value() []byte {
	return i.value
}

func (i *dbIter) Error() error { return i.err }

func (i *dbIter) Release() {
	if !i.Released() {
		i.p = nil
		i.node = 0
		i.key = nil
		i.value = nil
		i.BasicReleaser.Release()
	}
}

const (
	nKV = iota
	nKey
	nVal
	nHeight
	nNext
)

// DB is an in-memory key/value database.
type DB struct {
	cmp comparer.BasicComparer
	rnd *rand.Rand

	mu     sync.RWMutex
	kvData []byte
	// Node data:
	// [0]         : KV offset
	// [1]         : Key length
	// [2]         : Value length
	// [3]         : Height
	// [3..height] : Next nodes
	nodeData  []int
	prevNode  [tMaxHeight]int
	maxHeight int
	n         int
	kvSize    int
}

func (p *DB) randHeight() (h int) {
	const branching = 4
	h = 1
	for h < tMaxHeight && p.rnd.Int()%branching == 0 {
		h++
	}
	return
}

// Must hold RW-lock if prev == true, as it use shared prevNode slice.
func (p *DB) findGE(key []byte, prev bool) (int, bool) {
	node := 0
	h := p.maxHeight - 1
	for {
		next := p.nodeData[node+nNext+h]
		cmp := 1
		if next != 0 {
			o := p.nodeData[next]
			cmp = p.cmp.Compare(p.kvData[o:o+p.nodeData[next+nKey]], key)
		}
		if cmp < 0 {
			// Keep searching in this list
			node = next
		} else {
			if prev {
				p.prevNode[h] = node
			} else if cmp == 0 {
				return next, true
			}
			if h == 0 {
				return next, cmp == 0
			}
			h--
		}
	}
}

func (p *DB) findLT(key []byte) int {
	node := 0
	h := p.maxHeight - 1
	for {
		next := p.nodeData[node+nNext+h]
		o := p.nodeData[next]
		if next == 0 || p.cmp.Compare(p.kvData[o:o+p.nodeData[next+nKey]], key) >= 0 {
			if h == 0 {
				break
			}
			h--
		} else {
			node = next
		}
	}
	return node
}

func (p *DB) findLast() int {
	node := 0
	h := p.maxHeight - 1
	for {
		next := p.nodeData[node+nNext+h]
		if next == 0 {
			if h == 0 {
				break
			}
			h--
		} else {
			node = next
		}
	}
	return node
}

// Put sets the value for the given key. It overwrites any previous value
// for that key; a DB is not a multi-map.
//
// It is safe to modify the contents of the arguments after Put returns.
func (p *DB) Put(key []byte, value []byte) error {
	p.mu.Lock()
	defer p.mu.Unlock()

	if node, exact := p.findGE(key, true); exact {
		kvOffset := len(p.kvData)
		p.kvData = append(p.kvData, key...)
		p.kvData = append(p.kvData, value...)
		p.nodeData[node] = kvOffset
		m := p.nodeData[node+nVal]
		p.nodeData[node+nVal] = len(value)
		p.kvSize += len(value) - m
		return nil
	}

	h := p.randHeight()
	if h > p.maxHeight {
		for i := p.maxHeight; i < h; i++ {
			p.prevNode[i] = 0
		}
		p.maxHeight = h
	}

	kvOffset := len(p.kvData)
	p.kvData = append(p.kvData, key...)
	p.kvData = append(p.kvData, value...)
	// Node
	node := len(p.nodeData)
	p.nodeData = append(p.nodeData, kvOffset, len(key), len(value), h)
	for i, n := range p.prevNode[:h] {
		m := n + nNext + i
		p.nodeData = append(p.nodeData, p.nodeData[m])
		p.nodeData[m] = node
	}

	p.kvSize += len(key) + len(value)
	p.n++
	return nil
}

// Delete deletes the value for the given key. It returns ErrNotFound if
// the DB does not contain the key.
//
// It is safe to modify the contents of the arguments after Delete returns.
func (p *DB) Delete(key []byte) error {
	p.mu.Lock()
	defer p.mu.Unlock()

	node, exact := p.findGE(key, true)
	if !exact {
		return ErrNotFound
	}

	h := p.nodeData[node+nHeight]
	for i, n := range p.prevNode[:h] {
		m := n + nNext + i
		p.nodeData[m] = p.nodeData[p.nodeData[m]+nNext+i]
	}

	p.kvSize -= p.nodeData[node+nKey] + p.nodeData[node+nVal]
	p.n--
	return nil
}

// Contains returns true if the given key are in the DB.
//
// It is safe to modify the contents of the arguments after Contains returns.
func (p *DB) Contains(key []byte) bool {
	p.mu.RLock()
	_, exact := p.findGE(key, false)
	p.mu.RUnlock()
	return exact
}

// Get gets the value for the given key. It returns error.ErrNotFound if the
// DB does not contain the key.
//
// The caller should not modify the contents of the returned slice, but
// it is safe to modify the contents of the argument after Get returns.
func (p *DB) Get(key []byte) (value []byte, err error) {
	p.mu.RLock()
	if node, exact := p.findGE(key, false); exact {
		o := p.nodeData[node] + p.nodeData[node+nKey]
		value = p.kvData[o : o+p.nodeData[node+nVal]]
	} else {
		err = ErrNotFound
	}
	p.mu.RUnlock()
	return
}

// Find finds key/value pair whose key is greater than or equal to the
// given key. It returns ErrNotFound if the table doesn't contain
// such pair.
//
// The caller should not modify the contents of the returned slice, but
// it is safe to modify the contents of the argument after Find returns.
func (p *DB) Find(key []byte) (rkey, value []byte, err error) {
	p.mu.RLock()
	if node, _ := p.findGE(key, false); node != 0 {
		n := p.nodeData[node]
		m := n + p.nodeData[node+nKey]
		rkey = p.kvData[n:m]
		value = p.kvData[m : m+p.nodeData[node+nVal]]
	} else {
		err = ErrNotFound
	}
	p.mu.RUnlock()
	return
}

// NewIterator returns an iterator of the DB.
// The returned iterator is not safe for concurrent use, but it is safe to use
// multiple iterators concurrently, with each in a dedicated goroutine.
// It is also safe to use an iterator concurrently with modifying its
// underlying DB. However, the resultant key/value pairs are not guaranteed
// to be a consistent snapshot of the DB at a particular point in time.
//
// Slice allows slicing the iterator to only contains keys in the given
// range. A nil Range.Start is treated as a key before all keys in the
// DB. And a nil Range.Limit is treated as a key after all keys in
// the DB.
//
// WARNING: Any slice returned by interator (e.g. slice returned by calling
// Iterator.Key() or Iterator.Key() methods), its content should not be modified
// unless noted otherwise.
//
// The iterator must be released after use, by calling Release method.
//
// Also read Iterator documentation of the leveldb/iterator package.
func (p *DB) NewIterator(slice *util.Range) iterator.Iterator {
	return &dbIter{p: p, slice: slice}
}

// Capacity returns keys/values buffer capacity.
func (p *DB) Capacity() int {
	p.mu.RLock()
	defer p.mu.RUnlock()
	return cap(p.kvData)
}

// Size returns sum of keys and values length. Note that deleted
// key/value will not be accounted for, but it will still consume
// the buffer, since the buffer is append only.
func (p *DB) Size() int {
	p.mu.RLock()
	defer p.mu.RUnlock()
	return p.kvSize
}

// Free returns keys/values free buffer before need to grow.
func (p *DB) Free() int {
	p.mu.RLock()
	defer p.mu.RUnlock()
	return cap(p.kvData) - len(p.kvData)
}

// Len returns the number of entries in the DB.
func (p *DB) Len() int {
	p.mu.RLock()
	defer p.mu.RUnlock()
	return p.n
}

// Reset resets the DB to initial empty state. Allows reuse the buffer.
func (p *DB) Reset() {
	p.mu.Lock()
	p.rnd = rand.New(rand.NewSource(0xdeadbeef))
	p.maxHeight = 1
	p.n = 0
	p.kvSize = 0
	p.kvData = p.kvData[:0]
	p.nodeData = p.nodeData[:nNext+tMaxHeight]
	p.nodeData[nKV] = 0
	p.nodeData[nKey] = 0
	p.nodeData[nVal] = 0
	p.nodeData[nHeight] = tMaxHeight
	for n := 0; n < tMaxHeight; n++ {
		p.nodeData[nNext+n] = 0
		p.prevNode[n] = 0
	}
	p.mu.Unlock()
}

// New creates a new initialized in-memory key/value DB. The capacity
// is the initial key/value buffer capacity. The capacity is advisory,
// not enforced.
//
// This DB is append-only, deleting an entry would remove entry node but not
// reclaim KV buffer.
//
// The returned DB instance is safe for concurrent use.
func New(cmp comparer.BasicComparer, capacity int) *DB {
	p := &DB{
		cmp:       cmp,
		rnd:       rand.New(rand.NewSource(0xdeadbeef)),
		maxHeight: 1,
		kvData:    make([]byte, 0, capacity),
		nodeData:  make([]int, 4+tMaxHeight),
	}
	p.nodeData[nHeight] = tMaxHeight
	return p
}
```

## File: `leveldb/memdb/memdb_suite_test.go`
```go
package memdb

import (
	"testing"

	"github.com/syndtr/goleveldb/leveldb/testutil"
)

func TestMemDB(t *testing.T) {
	testutil.RunSuite(t, "MemDB Suite")
}
```

## File: `leveldb/memdb/memdb_test.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package memdb

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/comparer"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/testutil"
	"github.com/syndtr/goleveldb/leveldb/util"
)

func (p *DB) TestFindLT(key []byte) (rkey, value []byte, err error) {
	p.mu.RLock()
	if node := p.findLT(key); node != 0 {
		n := p.nodeData[node]
		m := n + p.nodeData[node+nKey]
		rkey = p.kvData[n:m]
		value = p.kvData[m : m+p.nodeData[node+nVal]]
	} else {
		err = ErrNotFound
	}
	p.mu.RUnlock()
	return
}

func (p *DB) TestFindLast() (rkey, value []byte, err error) {
	p.mu.RLock()
	if node := p.findLast(); node != 0 {
		n := p.nodeData[node]
		m := n + p.nodeData[node+nKey]
		rkey = p.kvData[n:m]
		value = p.kvData[m : m+p.nodeData[node+nVal]]
	} else {
		err = ErrNotFound
	}
	p.mu.RUnlock()
	return
}

func (p *DB) TestPut(key []byte, value []byte) error {
	return p.Put(key, value)
}

func (p *DB) TestDelete(key []byte) error {
	return p.Delete(key)
}

func (p *DB) TestFind(key []byte) (rkey, rvalue []byte, err error) {
	return p.Find(key)
}

func (p *DB) TestGet(key []byte) (value []byte, err error) {
	return p.Get(key)
}

func (p *DB) TestNewIterator(slice *util.Range) iterator.Iterator {
	return p.NewIterator(slice)
}

var _ = testutil.Defer(func() {
	Describe("Memdb", func() {
		Describe("write test", func() {
			It("should do write correctly", func() {
				db := New(comparer.DefaultComparer, 0)
				t := testutil.DBTesting{
					DB:      db,
					Deleted: testutil.KeyValue_Generate(nil, 1000, 1, 1, 30, 5, 5).Clone(),
					PostFn: func(t *testutil.DBTesting) {
						Expect(db.Len()).Should(Equal(t.Present.Len()))
						Expect(db.Size()).Should(Equal(t.Present.Size()))
						switch t.Act {
						case testutil.DBPut, testutil.DBOverwrite:
							Expect(db.Contains(t.ActKey)).Should(BeTrue())
						default:
							Expect(db.Contains(t.ActKey)).Should(BeFalse())
						}
					},
				}
				testutil.DoDBTesting(&t)
			})
		})

		Describe("read test", func() {
			testutil.AllKeyValueTesting(nil, func(kv testutil.KeyValue) testutil.DB {
				// Building the DB.
				db := New(comparer.DefaultComparer, 0)
				kv.IterateShuffled(nil, func(i int, key, value []byte) {
					Expect(db.Put(key, value)).ShouldNot(HaveOccurred())
				})

				if kv.Len() > 1 {
					It("Should find correct keys with findLT", func() {
						testutil.ShuffledIndex(nil, kv.Len()-1, 1, func(i int) {
							key_, key, _ := kv.IndexInexact(i + 1)
							expectedKey, expectedValue := kv.Index(i)

							// Using key that exist.
							rkey, rvalue, err := db.TestFindLT(key)
							Expect(err).ShouldNot(HaveOccurred(), "Error for key %q -> %q", key, expectedKey)
							Expect(rkey).Should(Equal(expectedKey), "Key")
							Expect(rvalue).Should(Equal(expectedValue), "Value for key %q -> %q", key, expectedKey)

							// Using key that doesn't exist.
							rkey, rvalue, err = db.TestFindLT(key_)
							Expect(err).ShouldNot(HaveOccurred(), "Error for key %q (%q) -> %q", key_, key, expectedKey)
							Expect(rkey).Should(Equal(expectedKey))
							Expect(rvalue).Should(Equal(expectedValue), "Value for key %q (%q) -> %q", key_, key, expectedKey)
						})
					})
				}

				if kv.Len() > 0 {
					It("Should find last key with findLast", func() {
						key, value := kv.Index(kv.Len() - 1)
						rkey, rvalue, err := db.TestFindLast()
						Expect(err).ShouldNot(HaveOccurred())
						Expect(rkey).Should(Equal(key))
						Expect(rvalue).Should(Equal(value))
					})
				}

				return db
			}, nil, nil)
		})
	})
})
```

## File: `leveldb/opt/options.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package opt provides sets of options used by LevelDB.
package opt

import (
	"math"

	"github.com/syndtr/goleveldb/leveldb/cache"
	"github.com/syndtr/goleveldb/leveldb/comparer"
	"github.com/syndtr/goleveldb/leveldb/filter"
)

const (
	KiB = 1024
	MiB = KiB * 1024
	GiB = MiB * 1024
)

var (
	DefaultBlockCacher                   = LRUCacher
	DefaultBlockCacheCapacity            = 8 * MiB
	DefaultBlockRestartInterval          = 16
	DefaultBlockSize                     = 4 * KiB
	DefaultCompactionExpandLimitFactor   = 25
	DefaultCompactionGPOverlapsFactor    = 10
	DefaultCompactionL0Trigger           = 4
	DefaultCompactionSourceLimitFactor   = 1
	DefaultCompactionTableSize           = 2 * MiB
	DefaultCompactionTableSizeMultiplier = 1.0
	DefaultCompactionTotalSize           = 10 * MiB
	DefaultCompactionTotalSizeMultiplier = 10.0
	DefaultCompressionType               = SnappyCompression
	DefaultIteratorSamplingRate          = 1 * MiB
	DefaultOpenFilesCacher               = LRUCacher
	DefaultWriteBuffer                   = 4 * MiB
	DefaultWriteL0PauseTrigger           = 12
	DefaultWriteL0SlowdownTrigger        = 8
	DefaultFilterBaseLg                  = 11
	DefaultMaxManifestFileSize           = int64(64 * MiB)
)

// Cacher is a caching algorithm.
type Cacher interface {
	New(capacity int) cache.Cacher
}

type cacherFunc struct {
	NewFunc func(capacity int) cache.Cacher
}

func (f *cacherFunc) New(capacity int) cache.Cacher {
	if f != nil && f.NewFunc != nil {
		return f.NewFunc(capacity)
	}
	return nil
}

func CacherFunc(f func(capacity int) cache.Cacher) Cacher {
	return &cacherFunc{f}
}

type passthroughCacher struct {
	Cacher cache.Cacher
}

func (p *passthroughCacher) New(capacity int) cache.Cacher {
	return p.Cacher
}

// PassthroughCacher can be used to passthrough pre-initialized
// 'cacher instance'. This is useful for sharing cache over multiple
// DB instances.
//
// Shared cache example:
//
//     fileCache := opt.NewLRU(500)
//     blockCache := opt.NewLRU(8 * opt.MiB)
// 	   options := &opt.Options{
//         OpenFilesCacher: fileCache,
//         BlockCacher: blockCache,
//     }
//     db1, err1 := leveldb.OpenFile("path/to/db1", options)
//     ...
//     db2, err2 := leveldb.OpenFile("path/to/db2", options)
//     ...
func PassthroughCacher(x cache.Cacher) Cacher {
	return &passthroughCacher{x}
}

// NewLRU creates LRU 'passthrough cacher'.
func NewLRU(capacity int) Cacher {
	return PassthroughCacher(cache.NewLRU(capacity))
}

var (
	// LRUCacher is the LRU-cache algorithm.
	LRUCacher = CacherFunc(cache.NewLRU)

	// NoCacher is the value to disable caching algorithm.
	NoCacher = CacherFunc(nil)
)

// Compression is the 'sorted table' block compression algorithm to use.
type Compression uint

func (c Compression) String() string {
	switch c {
	case DefaultCompression:
		return "default"
	case NoCompression:
		return "none"
	case SnappyCompression:
		return "snappy"
	}
	return "invalid"
}

const (
	DefaultCompression Compression = iota
	NoCompression
	SnappyCompression
	nCompression
)

// Strict is the DB 'strict level'.
type Strict uint

const (
	// If present then a corrupted or invalid chunk or block in manifest
	// journal will cause an error instead of being dropped.
	// This will prevent database with corrupted manifest to be opened.
	StrictManifest Strict = 1 << iota

	// If present then journal chunk checksum will be verified.
	StrictJournalChecksum

	// If present then a corrupted or invalid chunk or block in journal
	// will cause an error instead of being dropped.
	// This will prevent database with corrupted journal to be opened.
	StrictJournal

	// If present then 'sorted table' block checksum will be verified.
	// This has effect on both 'read operation' and compaction.
	StrictBlockChecksum

	// If present then a corrupted 'sorted table' will fails compaction.
	// The database will enter read-only mode.
	StrictCompaction

	// If present then a corrupted 'sorted table' will halts 'read operation'.
	StrictReader

	// If present then leveldb.Recover will drop corrupted 'sorted table'.
	StrictRecovery

	// This only applicable for ReadOptions, if present then this ReadOptions
	// 'strict level' will override global ones.
	StrictOverride

	// StrictAll enables all strict flags.
	StrictAll = StrictManifest | StrictJournalChecksum | StrictJournal | StrictBlockChecksum | StrictCompaction | StrictReader | StrictRecovery

	// DefaultStrict is the default strict flags. Specify any strict flags
	// will override default strict flags as whole (i.e. not OR'ed).
	DefaultStrict = StrictJournalChecksum | StrictBlockChecksum | StrictCompaction | StrictReader

	// NoStrict disables all strict flags. Override default strict flags.
	NoStrict = ^StrictAll
)

// Options holds the optional parameters for the DB at large.
type Options struct {
	// AltFilters defines one or more 'alternative filters'.
	// 'alternative filters' will be used during reads if a filter block
	// does not match with the 'effective filter'.
	//
	// The default value is nil
	AltFilters []filter.Filter

	// BlockCacher provides cache algorithm for LevelDB 'sorted table' block caching.
	// Specify NoCacher to disable caching algorithm.
	//
	// The default value is LRUCacher.
	BlockCacher Cacher

	// BlockCacheCapacity defines the capacity of the 'sorted table' block caching.
	// Use -1 for zero, this has same effect as specifying NoCacher to BlockCacher.
	//
	// The default value is 8MiB.
	BlockCacheCapacity int

	// BlockCacheEvictRemoved allows enable forced-eviction on cached block belonging
	// to removed 'sorted table'.
	//
	// The default if false.
	BlockCacheEvictRemoved bool

	// BlockRestartInterval is the number of keys between restart points for
	// delta encoding of keys.
	//
	// The default value is 16.
	BlockRestartInterval int

	// BlockSize is the minimum uncompressed size in bytes of each 'sorted table'
	// block.
	//
	// The default value is 4KiB.
	BlockSize int

	// CompactionExpandLimitFactor limits compaction size after expanded.
	// This will be multiplied by table size limit at compaction target level.
	//
	// The default value is 25.
	CompactionExpandLimitFactor int

	// CompactionGPOverlapsFactor limits overlaps in grandparent (Level + 2) that a
	// single 'sorted table' generates.
	// This will be multiplied by table size limit at grandparent level.
	//
	// The default value is 10.
	CompactionGPOverlapsFactor int

	// CompactionL0Trigger defines number of 'sorted table' at level-0 that will
	// trigger compaction.
	//
	// The default value is 4.
	CompactionL0Trigger int

	// CompactionSourceLimitFactor limits compaction source size. This doesn't apply to
	// level-0.
	// This will be multiplied by table size limit at compaction target level.
	//
	// The default value is 1.
	CompactionSourceLimitFactor int

	// CompactionTableSize limits size of 'sorted table' that compaction generates.
	// The limits for each level will be calculated as:
	//   CompactionTableSize * (CompactionTableSizeMultiplier ^ Level)
	// The multiplier for each level can also fine-tuned using CompactionTableSizeMultiplierPerLevel.
	//
	// The default value is 2MiB.
	CompactionTableSize int

	// CompactionTableSizeMultiplier defines multiplier for CompactionTableSize.
	//
	// The default value is 1.
	CompactionTableSizeMultiplier float64

	// CompactionTableSizeMultiplierPerLevel defines per-level multiplier for
	// CompactionTableSize.
	// Use zero to skip a level.
	//
	// The default value is nil.
	CompactionTableSizeMultiplierPerLevel []float64

	// CompactionTotalSize limits total size of 'sorted table' for each level.
	// The limits for each level will be calculated as:
	//   CompactionTotalSize * (CompactionTotalSizeMultiplier ^ Level)
	// The multiplier for each level can also fine-tuned using
	// CompactionTotalSizeMultiplierPerLevel.
	//
	// The default value is 10MiB.
	CompactionTotalSize int

	// CompactionTotalSizeMultiplier defines multiplier for CompactionTotalSize.
	//
	// The default value is 10.
	CompactionTotalSizeMultiplier float64

	// CompactionTotalSizeMultiplierPerLevel defines per-level multiplier for
	// CompactionTotalSize.
	// Use zero to skip a level.
	//
	// The default value is nil.
	CompactionTotalSizeMultiplierPerLevel []float64

	// Comparer defines a total ordering over the space of []byte keys: a 'less
	// than' relationship. The same comparison algorithm must be used for reads
	// and writes over the lifetime of the DB.
	//
	// The default value uses the same ordering as bytes.Compare.
	Comparer comparer.Comparer

	// Compression defines the 'sorted table' block compression to use.
	//
	// The default value (DefaultCompression) uses snappy compression.
	Compression Compression

	// DisableBufferPool allows disable use of util.BufferPool functionality.
	//
	// The default value is false.
	DisableBufferPool bool

	// DisableBlockCache allows disable use of cache.Cache functionality on
	// 'sorted table' block.
	//
	// The default value is false.
	DisableBlockCache bool

	// DisableCompactionBackoff allows disable compaction retry backoff.
	//
	// The default value is false.
	DisableCompactionBackoff bool

	// DisableLargeBatchTransaction allows disabling switch-to-transaction mode
	// on large batch write. If enable batch writes large than WriteBuffer will
	// use transaction.
	//
	// The default is false.
	DisableLargeBatchTransaction bool

	// DisableSeeksCompaction allows disabling 'seeks triggered compaction'.
	// The purpose of 'seeks triggered compaction' is to optimize database so
	// that 'level seeks' can be minimized, however this might generate many
	// small compaction which may not preferable.
	//
	// The default is false.
	DisableSeeksCompaction bool

	// ErrorIfExist defines whether an error should returned if the DB already
	// exist.
	//
	// The default value is false.
	ErrorIfExist bool

	// ErrorIfMissing defines whether an error should returned if the DB is
	// missing. If false then the database will be created if missing, otherwise
	// an error will be returned.
	//
	// The default value is false.
	ErrorIfMissing bool

	// Filter defines an 'effective filter' to use. An 'effective filter'
	// if defined will be used to generate per-table filter block.
	// The filter name will be stored on disk.
	// During reads LevelDB will try to find matching filter from
	// 'effective filter' and 'alternative filters'.
	//
	// Filter can be changed after a DB has been created. It is recommended
	// to put old filter to the 'alternative filters' to mitigate lack of
	// filter during transition period.
	//
	// A filter is used to reduce disk reads when looking for a specific key.
	//
	// The default value is nil.
	Filter filter.Filter

	// IteratorSamplingRate defines approximate gap (in bytes) between read
	// sampling of an iterator. The samples will be used to determine when
	// compaction should be triggered.
	// Use negative value to disable iterator sampling.
	// The iterator sampling is disabled if DisableSeeksCompaction is true.
	//
	// The default is 1MiB.
	IteratorSamplingRate int

	// NoSync allows completely disable fsync.
	//
	// The default is false.
	NoSync bool

	// NoWriteMerge allows disabling write merge.
	//
	// The default is false.
	NoWriteMerge bool

	// OpenFilesCacher provides cache algorithm for open files caching.
	// Specify NoCacher to disable caching algorithm.
	//
	// The default value is LRUCacher.
	OpenFilesCacher Cacher

	// OpenFilesCacheCapacity defines the capacity of the open files caching.
	// Use -1 for zero, this has same effect as specifying NoCacher to OpenFilesCacher.
	//
	// The default value is 200 on MacOS and 500 on other.
	OpenFilesCacheCapacity int

	// If true then opens DB in read-only mode.
	//
	// The default value is false.
	ReadOnly bool

	// Strict defines the DB strict level.
	Strict Strict

	// WriteBuffer defines maximum size of a 'memdb' before flushed to
	// 'sorted table'. 'memdb' is an in-memory DB backed by an on-disk
	// unsorted journal.
	//
	// LevelDB may held up to two 'memdb' at the same time.
	//
	// The default value is 4MiB.
	WriteBuffer int

	// WriteL0StopTrigger defines number of 'sorted table' at level-0 that will
	// pause write.
	//
	// The default value is 12.
	WriteL0PauseTrigger int

	// WriteL0SlowdownTrigger defines number of 'sorted table' at level-0 that
	// will trigger write slowdown.
	//
	// The default value is 8.
	WriteL0SlowdownTrigger int

	// FilterBaseLg is the log size for filter block to create a bloom filter.
	//
	// The default value is 11(as well as 2KB)
	FilterBaseLg int

	// MaxManifestFileSize is the maximum size limit of the MANIFEST-****** file.
	// When the MANIFEST-****** file grows beyond this size, LevelDB will create
	// a new MANIFEST file.
	//
	// The default value is 64 MiB.
	MaxManifestFileSize int64
}

func (o *Options) GetAltFilters() []filter.Filter {
	if o == nil {
		return nil
	}
	return o.AltFilters
}

func (o *Options) GetBlockCacher() Cacher {
	if o == nil || o.BlockCacher == nil {
		return DefaultBlockCacher
	}
	return o.BlockCacher
}

func (o *Options) GetBlockCacheCapacity() int {
	if o == nil || o.BlockCacheCapacity == 0 {
		return DefaultBlockCacheCapacity
	} else if o.BlockCacheCapacity < 0 {
		return 0
	}
	return o.BlockCacheCapacity
}

func (o *Options) GetBlockCacheEvictRemoved() bool {
	if o == nil {
		return false
	}
	return o.BlockCacheEvictRemoved
}

func (o *Options) GetBlockRestartInterval() int {
	if o == nil || o.BlockRestartInterval <= 0 {
		return DefaultBlockRestartInterval
	}
	return o.BlockRestartInterval
}

func (o *Options) GetBlockSize() int {
	if o == nil || o.BlockSize <= 0 {
		return DefaultBlockSize
	}
	return o.BlockSize
}

func (o *Options) GetCompactionExpandLimit(level int) int {
	factor := DefaultCompactionExpandLimitFactor
	if o != nil && o.CompactionExpandLimitFactor > 0 {
		factor = o.CompactionExpandLimitFactor
	}
	return o.GetCompactionTableSize(level+1) * factor
}

func (o *Options) GetCompactionGPOverlaps(level int) int {
	factor := DefaultCompactionGPOverlapsFactor
	if o != nil && o.CompactionGPOverlapsFactor > 0 {
		factor = o.CompactionGPOverlapsFactor
	}
	return o.GetCompactionTableSize(level+2) * factor
}

func (o *Options) GetCompactionL0Trigger() int {
	if o == nil || o.CompactionL0Trigger == 0 {
		return DefaultCompactionL0Trigger
	}
	return o.CompactionL0Trigger
}

func (o *Options) GetCompactionSourceLimit(level int) int {
	factor := DefaultCompactionSourceLimitFactor
	if o != nil && o.CompactionSourceLimitFactor > 0 {
		factor = o.CompactionSourceLimitFactor
	}
	return o.GetCompactionTableSize(level+1) * factor
}

func (o *Options) GetCompactionTableSize(level int) int {
	var (
		base = DefaultCompactionTableSize
		mult float64
	)
	if o != nil {
		if o.CompactionTableSize > 0 {
			base = o.CompactionTableSize
		}
		if level < len(o.CompactionTableSizeMultiplierPerLevel) && o.CompactionTableSizeMultiplierPerLevel[level] > 0 {
			mult = o.CompactionTableSizeMultiplierPerLevel[level]
		} else if o.CompactionTableSizeMultiplier > 0 {
			mult = math.Pow(o.CompactionTableSizeMultiplier, float64(level))
		}
	}
	if mult == 0 {
		mult = math.Pow(DefaultCompactionTableSizeMultiplier, float64(level))
	}
	return int(float64(base) * mult)
}

func (o *Options) GetCompactionTotalSize(level int) int64 {
	var (
		base = DefaultCompactionTotalSize
		mult float64
	)
	if o != nil {
		if o.CompactionTotalSize > 0 {
			base = o.CompactionTotalSize
		}
		if level < len(o.CompactionTotalSizeMultiplierPerLevel) && o.CompactionTotalSizeMultiplierPerLevel[level] > 0 {
			mult = o.CompactionTotalSizeMultiplierPerLevel[level]
		} else if o.CompactionTotalSizeMultiplier > 0 {
			mult = math.Pow(o.CompactionTotalSizeMultiplier, float64(level))
		}
	}
	if mult == 0 {
		mult = math.Pow(DefaultCompactionTotalSizeMultiplier, float64(level))
	}
	return int64(float64(base) * mult)
}

func (o *Options) GetComparer() comparer.Comparer {
	if o == nil || o.Comparer == nil {
		return comparer.DefaultComparer
	}
	return o.Comparer
}

func (o *Options) GetCompression() Compression {
	if o == nil || o.Compression <= DefaultCompression || o.Compression >= nCompression {
		return DefaultCompressionType
	}
	return o.Compression
}

func (o *Options) GetDisableBufferPool() bool {
	if o == nil {
		return false
	}
	return o.DisableBufferPool
}

func (o *Options) GetDisableBlockCache() bool {
	if o == nil {
		return false
	}
	return o.DisableBlockCache
}

func (o *Options) GetDisableCompactionBackoff() bool {
	if o == nil {
		return false
	}
	return o.DisableCompactionBackoff
}

func (o *Options) GetDisableLargeBatchTransaction() bool {
	if o == nil {
		return false
	}
	return o.DisableLargeBatchTransaction
}

func (o *Options) GetDisableSeeksCompaction() bool {
	if o == nil {
		return false
	}
	return o.DisableSeeksCompaction
}

func (o *Options) GetErrorIfExist() bool {
	if o == nil {
		return false
	}
	return o.ErrorIfExist
}

func (o *Options) GetErrorIfMissing() bool {
	if o == nil {
		return false
	}
	return o.ErrorIfMissing
}

func (o *Options) GetFilter() filter.Filter {
	if o == nil {
		return nil
	}
	return o.Filter
}

func (o *Options) GetIteratorSamplingRate() int {
	if o == nil || o.IteratorSamplingRate == 0 {
		return DefaultIteratorSamplingRate
	} else if o.IteratorSamplingRate < 0 {
		return 0
	}
	return o.IteratorSamplingRate
}

func (o *Options) GetNoSync() bool {
	if o == nil {
		return false
	}
	return o.NoSync
}

func (o *Options) GetNoWriteMerge() bool {
	if o == nil {
		return false
	}
	return o.NoWriteMerge
}

func (o *Options) GetOpenFilesCacher() Cacher {
	if o == nil || o.OpenFilesCacher == nil {
		return DefaultOpenFilesCacher
	}
	return o.OpenFilesCacher
}

func (o *Options) GetOpenFilesCacheCapacity() int {
	if o == nil || o.OpenFilesCacheCapacity == 0 {
		return DefaultOpenFilesCacheCapacity
	} else if o.OpenFilesCacheCapacity < 0 {
		return 0
	}
	return o.OpenFilesCacheCapacity
}

func (o *Options) GetReadOnly() bool {
	if o == nil {
		return false
	}
	return o.ReadOnly
}

func (o *Options) GetStrict(strict Strict) bool {
	if o == nil || o.Strict == 0 {
		return DefaultStrict&strict != 0
	}
	return o.Strict&strict != 0
}

func (o *Options) GetWriteBuffer() int {
	if o == nil || o.WriteBuffer <= 0 {
		return DefaultWriteBuffer
	}
	return o.WriteBuffer
}

func (o *Options) GetWriteL0PauseTrigger() int {
	if o == nil || o.WriteL0PauseTrigger == 0 {
		return DefaultWriteL0PauseTrigger
	}
	return o.WriteL0PauseTrigger
}

func (o *Options) GetWriteL0SlowdownTrigger() int {
	if o == nil || o.WriteL0SlowdownTrigger == 0 {
		return DefaultWriteL0SlowdownTrigger
	}
	return o.WriteL0SlowdownTrigger
}

func (o *Options) GetFilterBaseLg() int {
	if o == nil || o.FilterBaseLg <= 0 {
		return DefaultFilterBaseLg
	}
	return o.FilterBaseLg
}

// ReadOptions holds the optional parameters for 'read operation'. The
// 'read operation' includes Get, Find and NewIterator.
type ReadOptions struct {
	// DontFillCache defines whether block reads for this 'read operation'
	// should be cached. If false then the block will be cached. This does
	// not affects already cached block.
	//
	// The default value is false.
	DontFillCache bool

	// Strict will be OR'ed with global DB 'strict level' unless StrictOverride
	// is present. Currently only StrictReader that has effect here.
	Strict Strict
}

func (ro *ReadOptions) GetDontFillCache() bool {
	if ro == nil {
		return false
	}
	return ro.DontFillCache
}

func (ro *ReadOptions) GetStrict(strict Strict) bool {
	if ro == nil {
		return false
	}
	return ro.Strict&strict != 0
}

// WriteOptions holds the optional parameters for 'write operation'. The
// 'write operation' includes Write, Put and Delete.
type WriteOptions struct {
	// NoWriteMerge allows disabling write merge.
	//
	// The default is false.
	NoWriteMerge bool

	// Sync is whether to sync underlying writes from the OS buffer cache
	// through to actual disk, if applicable. Setting Sync can result in
	// slower writes.
	//
	// If false, and the machine crashes, then some recent writes may be lost.
	// Note that if it is just the process that crashes (and the machine does
	// not) then no writes will be lost.
	//
	// In other words, Sync being false has the same semantics as a write
	// system call. Sync being true means write followed by fsync.
	//
	// The default value is false.
	Sync bool
}

func (wo *WriteOptions) GetNoWriteMerge() bool {
	if wo == nil {
		return false
	}
	return wo.NoWriteMerge
}

func (wo *WriteOptions) GetSync() bool {
	if wo == nil {
		return false
	}
	return wo.Sync
}

func GetStrict(o *Options, ro *ReadOptions, strict Strict) bool {
	if ro.GetStrict(StrictOverride) {
		return ro.GetStrict(strict)
	}
	return o.GetStrict(strict) || ro.GetStrict(strict)
}

func (o *Options) GetMaxManifestFileSize() int64 {
	if o == nil || o.MaxManifestFileSize <= 0 {
		return DefaultMaxManifestFileSize
	}
	return o.MaxManifestFileSize
}
```

## File: `leveldb/opt/options_darwin.go`
```go
//go:build darwin
// +build darwin

package opt

var (
	DefaultOpenFilesCacheCapacity = 200
)
```

## File: `leveldb/opt/options_default.go`
```go
//go:build !darwin
// +build !darwin

package opt

var (
	DefaultOpenFilesCacheCapacity = 500
)
```

## File: `leveldb/storage/file_storage.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reservefs.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package storage

import (
	"errors"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strconv"
	"strings"
	"sync"
	"time"
)

var (
	errFileOpen = errors.New("leveldb/storage: file still open")
	errReadOnly = errors.New("leveldb/storage: storage is read-only")
)

type fileLock interface {
	release() error
}

type fileStorageLock struct {
	fs *fileStorage
}

func (lock *fileStorageLock) Unlock() {
	if lock.fs != nil {
		lock.fs.mu.Lock()
		defer lock.fs.mu.Unlock()
		if lock.fs.slock == lock {
			lock.fs.slock = nil
		}
	}
}

type int64Slice []int64

func (p int64Slice) Len() int           { return len(p) }
func (p int64Slice) Less(i, j int) bool { return p[i] < p[j] }
func (p int64Slice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }

func writeFileSynced(filename string, data []byte, perm os.FileMode) error {
	f, err := os.OpenFile(filename, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, perm)
	if err != nil {
		return err
	}
	n, err := f.Write(data)
	if err == nil && n < len(data) {
		err = io.ErrShortWrite
	}
	if err1 := f.Sync(); err == nil {
		err = err1
	}
	if err1 := f.Close(); err == nil {
		err = err1
	}
	return err
}

const logSizeThreshold = 1024 * 1024 // 1 MiB

// fileStorage is a file-system backed storage.
type fileStorage struct {
	path     string
	readOnly bool

	mu      sync.Mutex
	flock   fileLock
	slock   *fileStorageLock
	logw    *os.File
	logSize int64
	buf     []byte
	// Opened file counter; if open < 0 means closed.
	open int
	day  int
}

// OpenFile returns a new filesystem-backed storage implementation with the given
// path. This also acquire a file lock, so any subsequent attempt to open the
// same path will fail.
//
// The storage must be closed after use, by calling Close method.
func OpenFile(path string, readOnly bool) (Storage, error) {
	if fi, err := os.Stat(path); err == nil {
		if !fi.IsDir() {
			return nil, fmt.Errorf("leveldb/storage: open %s: not a directory", path)
		}
	} else if os.IsNotExist(err) && !readOnly {
		if err := os.MkdirAll(path, 0755); err != nil {
			return nil, err
		}
	} else {
		return nil, err
	}

	flock, err := newFileLock(filepath.Join(path, "LOCK"), readOnly)
	if err != nil {
		return nil, err
	}

	defer func() {
		if err != nil {
			if ferr := flock.release(); ferr != nil {
				err = fmt.Errorf("error opening file (%v); error unlocking file (%v)", err, ferr)
			}
		}
	}()

	var (
		logw    *os.File
		logSize int64
	)
	if !readOnly {
		logw, err = os.OpenFile(filepath.Join(path, "LOG"), os.O_WRONLY|os.O_CREATE, 0644)
		if err != nil {
			return nil, err
		}
		logSize, err = logw.Seek(0, os.SEEK_END)
		if err != nil {
			logw.Close()
			return nil, err
		}
	}

	fs := &fileStorage{
		path:     path,
		readOnly: readOnly,
		flock:    flock,
		logw:     logw,
		logSize:  logSize,
	}
	runtime.SetFinalizer(fs, (*fileStorage).Close)
	return fs, nil
}

func (fs *fileStorage) Lock() (Locker, error) {
	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return nil, ErrClosed
	}
	if fs.readOnly {
		return &fileStorageLock{}, nil
	}
	if fs.slock != nil {
		return nil, ErrLocked
	}
	fs.slock = &fileStorageLock{fs: fs}
	return fs.slock, nil
}

func itoa(buf []byte, i int, wid int) []byte {
	u := uint(i)
	if u == 0 && wid <= 1 {
		return append(buf, '0')
	}

	// Assemble decimal in reverse order.
	var b [32]byte
	bp := len(b)
	for ; u > 0 || wid > 0; u /= 10 {
		bp--
		wid--
		b[bp] = byte(u%10) + '0'
	}
	return append(buf, b[bp:]...)
}

func (fs *fileStorage) printDay(t time.Time) error {
	if fs.day == t.Day() {
		return nil
	}
	fs.day = t.Day()
	_, err := fs.logw.Write([]byte("=============== " + t.Format("Jan 2, 2006 (MST)") + " ===============\n"))
	return err
}

func (fs *fileStorage) doLog(t time.Time, str string) {
	if fs.logSize > logSizeThreshold {
		// Rotate log file.
		fs.logw.Close()
		fs.logw = nil
		fs.logSize = 0
		if err := rename(filepath.Join(fs.path, "LOG"), filepath.Join(fs.path, "LOG.old")); err != nil {
			return
		}
	}
	if fs.logw == nil {
		var err error
		fs.logw, err = os.OpenFile(filepath.Join(fs.path, "LOG"), os.O_WRONLY|os.O_CREATE, 0644)
		if err != nil {
			return
		}
		// Force printDay on new log file.
		fs.day = 0
	}
	if err := fs.printDay(t); err != nil {
		return
	}
	hour, min, sec := t.Clock()
	msec := t.Nanosecond() / 1e3
	// time
	fs.buf = itoa(fs.buf[:0], hour, 2)
	fs.buf = append(fs.buf, ':')
	fs.buf = itoa(fs.buf, min, 2)
	fs.buf = append(fs.buf, ':')
	fs.buf = itoa(fs.buf, sec, 2)
	fs.buf = append(fs.buf, '.')
	fs.buf = itoa(fs.buf, msec, 6)
	fs.buf = append(fs.buf, ' ')
	// write
	fs.buf = append(fs.buf, []byte(str)...)
	fs.buf = append(fs.buf, '\n')
	n, _ := fs.logw.Write(fs.buf)
	fs.logSize += int64(n)
}

func (fs *fileStorage) Log(str string) {
	if !fs.readOnly {
		t := time.Now()
		fs.mu.Lock()
		defer fs.mu.Unlock()
		if fs.open < 0 {
			return
		}
		fs.doLog(t, str)
	}
}

func (fs *fileStorage) log(str string) {
	if !fs.readOnly {
		fs.doLog(time.Now(), str)
	}
}

func (fs *fileStorage) setMeta(fd FileDesc) error {
	content := fsGenName(fd) + "\n"
	// Check and backup old CURRENT file.
	currentPath := filepath.Join(fs.path, "CURRENT")
	if _, err := os.Stat(currentPath); err == nil {
		b, err := ioutil.ReadFile(currentPath)
		if err != nil {
			fs.log(fmt.Sprintf("backup CURRENT: %v", err))
			return err
		}
		if string(b) == content {
			// Content not changed, do nothing.
			return nil
		}
		if err := writeFileSynced(currentPath+".bak", b, 0644); err != nil {
			fs.log(fmt.Sprintf("backup CURRENT: %v", err))
			return err
		}
	} else if !os.IsNotExist(err) {
		return err
	}
	path := fmt.Sprintf("%s.%d", filepath.Join(fs.path, "CURRENT"), fd.Num)
	if err := writeFileSynced(path, []byte(content), 0644); err != nil {
		fs.log(fmt.Sprintf("create CURRENT.%d: %v", fd.Num, err))
		return err
	}
	// Replace CURRENT file.
	if err := rename(path, currentPath); err != nil {
		fs.log(fmt.Sprintf("rename CURRENT.%d: %v", fd.Num, err))
		return err
	}
	// Sync root directory.
	if err := syncDir(fs.path); err != nil {
		fs.log(fmt.Sprintf("syncDir: %v", err))
		return err
	}
	return nil
}

func (fs *fileStorage) SetMeta(fd FileDesc) error {
	if !FileDescOk(fd) {
		return ErrInvalidFile
	}
	if fs.readOnly {
		return errReadOnly
	}

	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return ErrClosed
	}
	return fs.setMeta(fd)
}

func (fs *fileStorage) GetMeta() (FileDesc, error) {
	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return FileDesc{}, ErrClosed
	}
	dir, err := os.Open(fs.path)
	if err != nil {
		return FileDesc{}, err
	}
	names, err := dir.Readdirnames(0)
	// Close the dir first before checking for Readdirnames error.
	if ce := dir.Close(); ce != nil {
		fs.log(fmt.Sprintf("close dir: %v", ce))
	}
	if err != nil {
		return FileDesc{}, err
	}
	// Try this in order:
	// - CURRENT.[0-9]+ ('pending rename' file, descending order)
	// - CURRENT
	// - CURRENT.bak
	//
	// Skip corrupted file or file that point to a missing target file.
	type currentFile struct {
		name string
		fd   FileDesc
	}
	tryCurrent := func(name string) (*currentFile, error) {
		b, err := ioutil.ReadFile(filepath.Join(fs.path, name))
		if err != nil {
			if os.IsNotExist(err) {
				err = os.ErrNotExist
			}
			return nil, err
		}
		var fd FileDesc
		if len(b) < 1 || b[len(b)-1] != '\n' || !fsParseNamePtr(string(b[:len(b)-1]), &fd) {
			fs.log(fmt.Sprintf("%s: corrupted content: %q", name, b))
			err := &ErrCorrupted{
				Err: errors.New("leveldb/storage: corrupted or incomplete CURRENT file"),
			}
			return nil, err
		}
		if _, err := os.Stat(filepath.Join(fs.path, fsGenName(fd))); err != nil {
			if os.IsNotExist(err) {
				fs.log(fmt.Sprintf("%s: missing target file: %s", name, fd))
				err = os.ErrNotExist
			}
			return nil, err
		}
		return &currentFile{name: name, fd: fd}, nil
	}
	tryCurrents := func(names []string) (*currentFile, error) {
		var (
			cur *currentFile
			// Last corruption error.
			lastCerr error
		)
		for _, name := range names {
			var err error
			cur, err = tryCurrent(name)
			if err == nil {
				break
			} else if err == os.ErrNotExist {
				// Fallback to the next file.
			} else if isCorrupted(err) {
				lastCerr = err
				// Fallback to the next file.
			} else {
				// In case the error is due to permission, etc.
				return nil, err
			}
		}
		if cur == nil {
			err := os.ErrNotExist
			if lastCerr != nil {
				err = lastCerr
			}
			return nil, err
		}
		return cur, nil
	}

	// Try 'pending rename' files.
	var nums []int64
	for _, name := range names {
		if strings.HasPrefix(name, "CURRENT.") && name != "CURRENT.bak" {
			i, err := strconv.ParseInt(name[8:], 10, 64)
			if err == nil {
				nums = append(nums, i)
			}
		}
	}
	var (
		pendCur   *currentFile
		pendErr   = os.ErrNotExist
		pendNames []string
	)
	if len(nums) > 0 {
		sort.Sort(sort.Reverse(int64Slice(nums)))
		pendNames = make([]string, len(nums))
		for i, num := range nums {
			pendNames[i] = fmt.Sprintf("CURRENT.%d", num)
		}
		pendCur, pendErr = tryCurrents(pendNames)
		if pendErr != nil && pendErr != os.ErrNotExist && !isCorrupted(pendErr) {
			return FileDesc{}, pendErr
		}
	}

	// Try CURRENT and CURRENT.bak.
	curCur, curErr := tryCurrents([]string{"CURRENT", "CURRENT.bak"})
	if curErr != nil && curErr != os.ErrNotExist && !isCorrupted(curErr) {
		return FileDesc{}, curErr
	}

	// pendCur takes precedence, but guards against obsolete pendCur.
	if pendCur != nil && (curCur == nil || pendCur.fd.Num > curCur.fd.Num) {
		curCur = pendCur
	}

	if curCur != nil {
		// Restore CURRENT file to proper state.
		if !fs.readOnly && (curCur.name != "CURRENT" || len(pendNames) != 0) {
			// Ignore setMeta errors, however don't delete obsolete files if we
			// catch error.
			if err := fs.setMeta(curCur.fd); err == nil {
				// Remove 'pending rename' files.
				for _, name := range pendNames {
					if err := os.Remove(filepath.Join(fs.path, name)); err != nil {
						fs.log(fmt.Sprintf("remove %s: %v", name, err))
					}
				}
			}
		}
		return curCur.fd, nil
	}

	// Nothing found.
	if isCorrupted(pendErr) {
		return FileDesc{}, pendErr
	}
	return FileDesc{}, curErr
}

func (fs *fileStorage) List(ft FileType) (fds []FileDesc, err error) {
	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return nil, ErrClosed
	}
	dir, err := os.Open(fs.path)
	if err != nil {
		return
	}
	names, err := dir.Readdirnames(0)
	// Close the dir first before checking for Readdirnames error.
	if cerr := dir.Close(); cerr != nil {
		fs.log(fmt.Sprintf("close dir: %v", cerr))
	}
	if err == nil {
		for _, name := range names {
			if fd, ok := fsParseName(name); ok && fd.Type&ft != 0 {
				fds = append(fds, fd)
			}
		}
	}
	return
}

func (fs *fileStorage) Open(fd FileDesc) (Reader, error) {
	if !FileDescOk(fd) {
		return nil, ErrInvalidFile
	}

	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return nil, ErrClosed
	}
	of, err := os.OpenFile(filepath.Join(fs.path, fsGenName(fd)), os.O_RDONLY, 0)
	if err != nil {
		if fsHasOldName(fd) && os.IsNotExist(err) {
			of, err = os.OpenFile(filepath.Join(fs.path, fsGenOldName(fd)), os.O_RDONLY, 0)
			if err == nil {
				goto ok
			}
		}
		return nil, err
	}
ok:
	fs.open++
	return &fileWrap{File: of, fs: fs, fd: fd}, nil
}

func (fs *fileStorage) Create(fd FileDesc) (Writer, error) {
	if !FileDescOk(fd) {
		return nil, ErrInvalidFile
	}
	if fs.readOnly {
		return nil, errReadOnly
	}

	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return nil, ErrClosed
	}
	of, err := os.OpenFile(filepath.Join(fs.path, fsGenName(fd)), os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0644)
	if err != nil {
		return nil, err
	}
	fs.open++
	return &fileWrap{File: of, fs: fs, fd: fd}, nil
}

func (fs *fileStorage) Remove(fd FileDesc) error {
	if !FileDescOk(fd) {
		return ErrInvalidFile
	}
	if fs.readOnly {
		return errReadOnly
	}

	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return ErrClosed
	}
	err := os.Remove(filepath.Join(fs.path, fsGenName(fd)))
	if err != nil {
		if fsHasOldName(fd) && os.IsNotExist(err) {
			if e1 := os.Remove(filepath.Join(fs.path, fsGenOldName(fd))); !os.IsNotExist(e1) {
				fs.log(fmt.Sprintf("remove %s: %v (old name)", fd, err))
				err = e1
			}
		} else {
			fs.log(fmt.Sprintf("remove %s: %v", fd, err))
		}
	}
	return err
}

func (fs *fileStorage) Rename(oldfd, newfd FileDesc) error {
	if !FileDescOk(oldfd) || !FileDescOk(newfd) {
		return ErrInvalidFile
	}
	if oldfd == newfd {
		return nil
	}
	if fs.readOnly {
		return errReadOnly
	}

	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return ErrClosed
	}
	return rename(filepath.Join(fs.path, fsGenName(oldfd)), filepath.Join(fs.path, fsGenName(newfd)))
}

func (fs *fileStorage) Close() error {
	fs.mu.Lock()
	defer fs.mu.Unlock()
	if fs.open < 0 {
		return ErrClosed
	}
	// Clear the finalizer.
	runtime.SetFinalizer(fs, nil)

	if fs.open > 0 {
		fs.log(fmt.Sprintf("close: warning, %d files still open", fs.open))
	}
	fs.open = -1
	if fs.logw != nil {
		fs.logw.Close()
	}
	return fs.flock.release()
}

type fileWrap struct {
	*os.File
	fs     *fileStorage
	fd     FileDesc
	closed bool
}

func (fw *fileWrap) Sync() error {
	if err := fw.File.Sync(); err != nil {
		return err
	}
	if fw.fd.Type == TypeManifest {
		// Also sync parent directory if file type is manifest.
		// See: https://code.google.com/p/leveldb/issues/detail?id=190.
		if err := syncDir(fw.fs.path); err != nil {
			fw.fs.log(fmt.Sprintf("syncDir: %v", err))
			return err
		}
	}
	return nil
}

func (fw *fileWrap) Close() error {
	fw.fs.mu.Lock()
	defer fw.fs.mu.Unlock()
	if fw.closed {
		return ErrClosed
	}
	fw.closed = true
	fw.fs.open--
	err := fw.File.Close()
	if err != nil {
		fw.fs.log(fmt.Sprintf("close %s: %v", fw.fd, err))
	}
	return err
}

func fsGenName(fd FileDesc) string {
	switch fd.Type {
	case TypeManifest:
		return fmt.Sprintf("MANIFEST-%06d", fd.Num)
	case TypeJournal:
		return fmt.Sprintf("%06d.log", fd.Num)
	case TypeTable:
		return fmt.Sprintf("%06d.ldb", fd.Num)
	case TypeTemp:
		return fmt.Sprintf("%06d.tmp", fd.Num)
	default:
		panic("invalid file type")
	}
}

func fsHasOldName(fd FileDesc) bool {
	return fd.Type == TypeTable
}

func fsGenOldName(fd FileDesc) string {
	switch fd.Type {
	case TypeTable:
		return fmt.Sprintf("%06d.sst", fd.Num)
	default:
		return fsGenName(fd)
	}
}

func fsParseName(name string) (fd FileDesc, ok bool) {
	var tail string
	_, err := fmt.Sscanf(name, "%d.%s", &fd.Num, &tail)
	if err == nil {
		switch tail {
		case "log":
			fd.Type = TypeJournal
		case "ldb", "sst":
			fd.Type = TypeTable
		case "tmp":
			fd.Type = TypeTemp
		default:
			return
		}
		return fd, true
	}
	n, _ := fmt.Sscanf(name, "MANIFEST-%d%s", &fd.Num, &tail)
	if n == 1 {
		fd.Type = TypeManifest
		return fd, true
	}
	return
}

func fsParseNamePtr(name string, fd *FileDesc) bool {
	_fd, ok := fsParseName(name)
	if fd != nil {
		*fd = _fd
	}
	return ok
}
```

## File: `leveldb/storage/file_storage_nacl.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

//go:build nacl
// +build nacl

package storage

import (
	"os"
	"syscall"
)

func newFileLock(path string, readOnly bool) (fl fileLock, err error) {
	return nil, syscall.ENOTSUP
}

func setFileLock(f *os.File, readOnly, lock bool) error {
	return syscall.ENOTSUP
}

func rename(oldpath, newpath string) error {
	return syscall.ENOTSUP
}

func isErrInvalid(err error) bool {
	return false
}

func syncDir(name string) error {
	return syscall.ENOTSUP
}
```

## File: `leveldb/storage/file_storage_plan9.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package storage

import (
	"os"
)

type plan9FileLock struct {
	f *os.File
}

func (fl *plan9FileLock) release() error {
	return fl.f.Close()
}

func newFileLock(path string, readOnly bool) (fl fileLock, err error) {
	var (
		flag int
		perm os.FileMode
	)
	if readOnly {
		flag = os.O_RDONLY
	} else {
		flag = os.O_RDWR
		perm = os.ModeExclusive
	}
	f, err := os.OpenFile(path, flag, perm)
	if os.IsNotExist(err) {
		f, err = os.OpenFile(path, flag|os.O_CREATE, perm|0644)
	}
	if err != nil {
		return
	}
	fl = &plan9FileLock{f: f}
	return
}

func rename(oldpath, newpath string) error {
	if _, err := os.Stat(newpath); err == nil {
		if err := os.Remove(newpath); err != nil {
			return err
		}
	}

	return os.Rename(oldpath, newpath)
}

func syncDir(name string) error {
	f, err := os.Open(name)
	if err != nil {
		return err
	}
	defer f.Close()
	if err := f.Sync(); err != nil {
		return err
	}
	return nil
}
```

## File: `leveldb/storage/file_storage_solaris.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

//go:build solaris
// +build solaris

package storage

import (
	"os"
	"syscall"
)

type unixFileLock struct {
	f *os.File
}

func (fl *unixFileLock) release() error {
	if err := setFileLock(fl.f, false, false); err != nil {
		return err
	}
	return fl.f.Close()
}

func newFileLock(path string, readOnly bool) (fl fileLock, err error) {
	var flag int
	if readOnly {
		flag = os.O_RDONLY
	} else {
		flag = os.O_RDWR
	}
	f, err := os.OpenFile(path, flag, 0)
	if os.IsNotExist(err) {
		f, err = os.OpenFile(path, flag|os.O_CREATE, 0644)
	}
	if err != nil {
		return
	}
	err = setFileLock(f, readOnly, true)
	if err != nil {
		f.Close()
		return
	}
	fl = &unixFileLock{f: f}
	return
}

func setFileLock(f *os.File, readOnly, lock bool) error {
	flock := syscall.Flock_t{
		Type:   syscall.F_UNLCK,
		Start:  0,
		Len:    0,
		Whence: 1,
	}
	if lock {
		if readOnly {
			flock.Type = syscall.F_RDLCK
		} else {
			flock.Type = syscall.F_WRLCK
		}
	}
	return syscall.FcntlFlock(f.Fd(), syscall.F_SETLK, &flock)
}

func rename(oldpath, newpath string) error {
	return os.Rename(oldpath, newpath)
}

func syncDir(name string) error {
	f, err := os.Open(name)
	if err != nil {
		return err
	}
	defer f.Close()
	if err := f.Sync(); err != nil {
		return err
	}
	return nil
}
```

## File: `leveldb/storage/file_storage_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package storage

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"path/filepath"
	"strings"
	"testing"
)

var cases = []struct {
	oldName []string
	name    string
	ftype   FileType
	num     int64
}{
	{nil, "000100.log", TypeJournal, 100},
	{nil, "000000.log", TypeJournal, 0},
	{[]string{"000000.sst"}, "000000.ldb", TypeTable, 0},
	{nil, "MANIFEST-000002", TypeManifest, 2},
	{nil, "MANIFEST-000007", TypeManifest, 7},
	{nil, "9223372036854775807.log", TypeJournal, 9223372036854775807},
	{nil, "000100.tmp", TypeTemp, 100},
}

var invalidCases = []string{
	"",
	"foo",
	"foo-dx-100.log",
	".log",
	"",
	"manifest",
	"CURREN",
	"CURRENTX",
	"MANIFES",
	"MANIFEST",
	"MANIFEST-",
	"XMANIFEST-3",
	"MANIFEST-3x",
	"LOC",
	"LOCKx",
	"LO",
	"LOGx",
	"18446744073709551616.log",
	"184467440737095516150.log",
	"100",
	"100.",
	"100.lop",
}

func tempDir(t *testing.T) string {
	dir, err := ioutil.TempDir("", "goleveldb-")
	if err != nil {
		t.Fatal(t)
	}
	t.Log("Using temp-dir:", dir)
	return dir
}

func TestFileStorage_CreateFileName(t *testing.T) {
	for _, c := range cases {
		if name := fsGenName(FileDesc{c.ftype, c.num}); name != c.name {
			t.Errorf("invalid filename got '%s', want '%s'", name, c.name)
		}
	}
}

func TestFileStorage_MetaSetGet(t *testing.T) {
	temp := tempDir(t)
	fs, err := OpenFile(temp, false)
	if err != nil {
		t.Fatal("OpenFile: got error: ", err)
	}

	for i := 0; i < 10; i++ {
		num := rand.Int63()
		fd := FileDesc{Type: TypeManifest, Num: num}
		w, err := fs.Create(fd)
		if err != nil {
			t.Fatalf("Create(%d): got error: %v", i, err)
		}
		if _, err := w.Write([]byte("TEST")); err != nil {
			t.Fatalf("Write(%d): got error: %v", i, err)
		}
		w.Close()
		if err := fs.SetMeta(fd); err != nil {
			t.Fatalf("SetMeta(%d): got error: %v", i, err)
		}
		rfd, err := fs.GetMeta()
		if err != nil {
			t.Fatalf("GetMeta(%d): got error: %v", i, err)
		}
		if fd != rfd {
			t.Fatalf("Invalid meta (%d): got '%s', want '%s'", i, rfd, fd)
		}
	}
	os.RemoveAll(temp)
}

func TestFileStorage_Meta(t *testing.T) {
	type current struct {
		num      int64
		backup   bool
		current  bool
		manifest bool
		corrupt  bool
	}
	type testCase struct {
		currents []current
		notExist bool
		corrupt  bool
		expect   int64
	}
	cases := []testCase{
		{
			currents: []current{
				{num: 2, backup: true, manifest: true},
				{num: 1, current: true},
			},
			expect: 2,
		},
		{
			currents: []current{
				{num: 2, backup: true, manifest: true},
				{num: 1, current: true, manifest: true},
			},
			expect: 1,
		},
		{
			currents: []current{
				{num: 2, manifest: true},
				{num: 3, manifest: true},
				{num: 4, current: true, manifest: true},
			},
			expect: 4,
		},
		{
			currents: []current{
				{num: 2, manifest: true},
				{num: 3, manifest: true},
				{num: 4, current: true, manifest: true, corrupt: true},
			},
			expect: 3,
		},
		{
			currents: []current{
				{num: 2, manifest: true},
				{num: 3, manifest: true},
				{num: 5, current: true, manifest: true, corrupt: true},
				{num: 4, backup: true, manifest: true},
			},
			expect: 4,
		},
		{
			currents: []current{
				{num: 4, manifest: true},
				{num: 3, manifest: true},
				{num: 2, current: true, manifest: true},
			},
			expect: 4,
		},
		{
			currents: []current{
				{num: 4, manifest: true, corrupt: true},
				{num: 3, manifest: true},
				{num: 2, current: true, manifest: true},
			},
			expect: 3,
		},
		{
			currents: []current{
				{num: 4, manifest: true, corrupt: true},
				{num: 3, manifest: true, corrupt: true},
				{num: 2, current: true, manifest: true},
			},
			expect: 2,
		},
		{
			currents: []current{
				{num: 4},
				{num: 3, manifest: true},
				{num: 2, current: true, manifest: true},
			},
			expect: 3,
		},
		{
			currents: []current{
				{num: 4},
				{num: 3, manifest: true},
				{num: 6, current: true},
				{num: 5, backup: true, manifest: true},
			},
			expect: 5,
		},
		{
			currents: []current{
				{num: 4},
				{num: 3},
				{num: 6, current: true},
				{num: 5, backup: true},
			},
			notExist: true,
		},
		{
			currents: []current{
				{num: 4, corrupt: true},
				{num: 3},
				{num: 6, current: true},
				{num: 5, backup: true},
			},
			corrupt: true,
		},
	}
	for i, tc := range cases {
		t.Logf("Test-%d", i)
		temp := tempDir(t)
		fs, err := OpenFile(temp, false)
		if err != nil {
			t.Fatal("OpenFile: got error: ", err)
		}
		for _, cur := range tc.currents {
			var curName string
			switch {
			case cur.current:
				curName = "CURRENT"
			case cur.backup:
				curName = "CURRENT.bak"
			default:
				curName = fmt.Sprintf("CURRENT.%d", cur.num)
			}
			fd := FileDesc{Type: TypeManifest, Num: cur.num}
			content := fmt.Sprintf("%s\n", fsGenName(fd))
			if cur.corrupt {
				content = content[:len(content)-1-rand.Intn(3)]
			}
			if err := ioutil.WriteFile(filepath.Join(temp, curName), []byte(content), 0644); err != nil {
				t.Fatal(err)
			}
			if cur.manifest {
				w, err := fs.Create(fd)
				if err != nil {
					t.Fatal(err)
				}
				if _, err := w.Write([]byte("TEST")); err != nil {
					t.Fatal(err)
				}
				w.Close()
			}
		}
		ret, err := fs.GetMeta()
		if tc.notExist {
			if err != os.ErrNotExist {
				t.Fatalf("expect ErrNotExist, got: %v", err)
			}
		} else if tc.corrupt {
			if !isCorrupted(err) {
				t.Fatalf("expect ErrCorrupted, got: %v", err)
			}
		} else {
			if err != nil {
				t.Fatal(err)
			}
			if ret.Type != TypeManifest {
				t.Fatalf("expecting manifest, got: %s", ret.Type)
			}
			if ret.Num != tc.expect {
				t.Fatalf("invalid num, expect=%d got=%d", tc.expect, ret.Num)
			}
			fis, err := ioutil.ReadDir(temp)
			if err != nil {
				t.Fatal(err)
			}
			for _, fi := range fis {
				if strings.HasPrefix(fi.Name(), "CURRENT") {
					switch fi.Name() {
					case "CURRENT", "CURRENT.bak":
					default:
						t.Fatalf("found rouge CURRENT file: %s", fi.Name())
					}
				}
				t.Logf("-> %s", fi.Name())
			}
		}
		os.RemoveAll(temp)
	}
}

func TestFileStorage_ParseFileName(t *testing.T) {
	for _, c := range cases {
		for _, name := range append([]string{c.name}, c.oldName...) {
			fd, ok := fsParseName(name)
			if !ok {
				t.Errorf("cannot parse filename '%s'", name)
				continue
			}
			if fd.Type != c.ftype {
				t.Errorf("filename '%s' invalid type got '%d', want '%d'", name, fd.Type, c.ftype)
			}
			if fd.Num != c.num {
				t.Errorf("filename '%s' invalid number got '%d', want '%d'", name, fd.Num, c.num)
			}
		}
	}
}

func TestFileStorage_InvalidFileName(t *testing.T) {
	for _, name := range invalidCases {
		if fsParseNamePtr(name, nil) {
			t.Errorf("filename '%s' should be invalid", name)
		}
	}
}

func TestFileStorage_Locking(t *testing.T) {
	temp := tempDir(t)
	defer os.RemoveAll(temp)

	p1, err := OpenFile(temp, false)
	if err != nil {
		t.Fatal("OpenFile(1): got error: ", err)
	}

	p2, err := OpenFile(temp, false)
	if err != nil {
		t.Logf("OpenFile(2): got error: %s (expected)", err)
	} else {
		p2.Close()
		p1.Close()
		t.Fatal("OpenFile(2): expect error")
	}

	p1.Close()

	p3, err := OpenFile(temp, false)
	if err != nil {
		t.Fatal("OpenFile(3): got error: ", err)
	}
	defer p3.Close()

	l, err := p3.Lock()
	if err != nil {
		t.Fatal("storage lock failed(1): ", err)
	}
	_, err = p3.Lock()
	if err == nil {
		t.Fatal("expect error for second storage lock attempt")
	} else {
		t.Logf("storage lock got error: %s (expected)", err)
	}
	l.Unlock()
	_, err = p3.Lock()
	if err != nil {
		t.Fatal("storage lock failed(2): ", err)
	}
}

func TestFileStorage_ReadOnlyLocking(t *testing.T) {
	temp := tempDir(t)
	defer os.RemoveAll(temp)

	p1, err := OpenFile(temp, false)
	if err != nil {
		t.Fatal("OpenFile(1): got error: ", err)
	}

	_, err = OpenFile(temp, true)
	if err != nil {
		t.Logf("OpenFile(2): got error: %s (expected)", err)
	} else {
		t.Fatal("OpenFile(2): expect error")
	}

	p1.Close()

	p3, err := OpenFile(temp, true)
	if err != nil {
		t.Fatal("OpenFile(3): got error: ", err)
	}

	p4, err := OpenFile(temp, true)
	if err != nil {
		t.Fatal("OpenFile(4): got error: ", err)
	}

	_, err = OpenFile(temp, false)
	if err != nil {
		t.Logf("OpenFile(5): got error: %s (expected)", err)
	} else {
		t.Fatal("OpenFile(2): expect error")
	}

	p3.Close()
	p4.Close()
}
```

## File: `leveldb/storage/file_storage_unix.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

//go:build darwin || dragonfly || freebsd || linux || netbsd || openbsd
// +build darwin dragonfly freebsd linux netbsd openbsd

package storage

import (
	"os"
	"syscall"
)

type unixFileLock struct {
	f *os.File
}

func (fl *unixFileLock) release() error {
	if err := setFileLock(fl.f, false, false); err != nil {
		return err
	}
	return fl.f.Close()
}

func newFileLock(path string, readOnly bool) (fl fileLock, err error) {
	var flag int
	if readOnly {
		flag = os.O_RDONLY
	} else {
		flag = os.O_RDWR
	}
	f, err := os.OpenFile(path, flag, 0)
	if os.IsNotExist(err) {
		f, err = os.OpenFile(path, flag|os.O_CREATE, 0644)
	}
	if err != nil {
		return
	}
	err = setFileLock(f, readOnly, true)
	if err != nil {
		f.Close()
		return
	}
	fl = &unixFileLock{f: f}
	return
}

func setFileLock(f *os.File, readOnly, lock bool) error {
	how := syscall.LOCK_UN
	if lock {
		if readOnly {
			how = syscall.LOCK_SH
		} else {
			how = syscall.LOCK_EX
		}
	}
	return syscall.Flock(int(f.Fd()), how|syscall.LOCK_NB)
}

func rename(oldpath, newpath string) error {
	return os.Rename(oldpath, newpath)
}

func isErrInvalid(err error) bool {
	if err == os.ErrInvalid {
		return true
	}
	// Go < 1.8
	if syserr, ok := err.(*os.SyscallError); ok && syserr.Err == syscall.EINVAL {
		return true
	}
	// Go >= 1.8 returns *os.PathError instead
	if patherr, ok := err.(*os.PathError); ok && patherr.Err == syscall.EINVAL {
		return true
	}
	return false
}

func syncDir(name string) error {
	// As per fsync manpage, Linux seems to expect fsync on directory, however
	// some system don't support this, so we will ignore syscall.EINVAL.
	//
	// From fsync(2):
	//   Calling fsync() does not necessarily ensure that the entry in the
	//   directory containing the file has also reached disk. For that an
	//   explicit fsync() on a file descriptor for the directory is also needed.
	f, err := os.Open(name)
	if err != nil {
		return err
	}
	defer f.Close()
	if err := f.Sync(); err != nil && !isErrInvalid(err) {
		return err
	}
	return nil
}
```

## File: `leveldb/storage/file_storage_windows.go`
```go
// Copyright (c) 2013, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package storage

import (
	"syscall"
	"unsafe"
)

var (
	modkernel32 = syscall.NewLazyDLL("kernel32.dll")

	procMoveFileExW = modkernel32.NewProc("MoveFileExW")
)

const (
	_MOVEFILE_REPLACE_EXISTING = 1
)

type windowsFileLock struct {
	fd syscall.Handle
}

func (fl *windowsFileLock) release() error {
	return syscall.Close(fl.fd)
}

func newFileLock(path string, readOnly bool) (fl fileLock, err error) {
	pathp, err := syscall.UTF16PtrFromString(path)
	if err != nil {
		return
	}
	var access, shareMode uint32
	if readOnly {
		access = syscall.GENERIC_READ
		shareMode = syscall.FILE_SHARE_READ | syscall.FILE_SHARE_WRITE
	} else {
		access = syscall.GENERIC_READ | syscall.GENERIC_WRITE
	}
	fd, err := syscall.CreateFile(pathp, access, shareMode, nil, syscall.OPEN_EXISTING, syscall.FILE_ATTRIBUTE_NORMAL, 0)
	if err == syscall.ERROR_FILE_NOT_FOUND {
		fd, err = syscall.CreateFile(pathp, access, shareMode, nil, syscall.OPEN_ALWAYS, syscall.FILE_ATTRIBUTE_NORMAL, 0)
	}
	if err != nil {
		return
	}
	fl = &windowsFileLock{fd: fd}
	return
}

func moveFileEx(from *uint16, to *uint16, flags uint32) error {
	r1, _, e1 := syscall.Syscall(procMoveFileExW.Addr(), 3, uintptr(unsafe.Pointer(from)), uintptr(unsafe.Pointer(to)), uintptr(flags))
	if r1 == 0 {
		if e1 != 0 {
			return error(e1)
		}
		return syscall.EINVAL
	}
	return nil
}

func rename(oldpath, newpath string) error {
	from, err := syscall.UTF16PtrFromString(oldpath)
	if err != nil {
		return err
	}
	to, err := syscall.UTF16PtrFromString(newpath)
	if err != nil {
		return err
	}
	return moveFileEx(from, to, _MOVEFILE_REPLACE_EXISTING)
}

func syncDir(name string) error { return nil }
```

## File: `leveldb/storage/mem_storage.go`
```go
// Copyright (c) 2013, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package storage

import (
	"bytes"
	"os"
	"sync"
)

const typeShift = 4

// Verify at compile-time that typeShift is large enough to cover all FileType
// values by confirming that 0 == 0.
var _ [0]struct{} = [TypeAll >> typeShift]struct{}{}

type memStorageLock struct {
	ms *memStorage
}

func (lock *memStorageLock) Unlock() {
	ms := lock.ms
	ms.mu.Lock()
	defer ms.mu.Unlock()
	if ms.slock == lock {
		ms.slock = nil
	}
}

// memStorage is a memory-backed storage.
type memStorage struct {
	mu    sync.Mutex
	slock *memStorageLock
	files map[uint64]*memFile
	meta  FileDesc
}

// NewMemStorage returns a new memory-backed storage implementation.
func NewMemStorage() Storage {
	return &memStorage{
		files: make(map[uint64]*memFile),
	}
}

func (ms *memStorage) Lock() (Locker, error) {
	ms.mu.Lock()
	defer ms.mu.Unlock()
	if ms.slock != nil {
		return nil, ErrLocked
	}
	ms.slock = &memStorageLock{ms: ms}
	return ms.slock, nil
}

func (*memStorage) Log(str string) {}

func (ms *memStorage) SetMeta(fd FileDesc) error {
	if !FileDescOk(fd) {
		return ErrInvalidFile
	}

	ms.mu.Lock()
	ms.meta = fd
	ms.mu.Unlock()
	return nil
}

func (ms *memStorage) GetMeta() (FileDesc, error) {
	ms.mu.Lock()
	defer ms.mu.Unlock()
	if ms.meta.Zero() {
		return FileDesc{}, os.ErrNotExist
	}
	return ms.meta, nil
}

func (ms *memStorage) List(ft FileType) ([]FileDesc, error) {
	ms.mu.Lock()
	var fds []FileDesc
	for x := range ms.files {
		fd := unpackFile(x)
		if fd.Type&ft != 0 {
			fds = append(fds, fd)
		}
	}
	ms.mu.Unlock()
	return fds, nil
}

func (ms *memStorage) Open(fd FileDesc) (Reader, error) {
	if !FileDescOk(fd) {
		return nil, ErrInvalidFile
	}

	ms.mu.Lock()
	defer ms.mu.Unlock()
	if m, exist := ms.files[packFile(fd)]; exist {
		if m.open {
			return nil, errFileOpen
		}
		m.open = true
		return &memReader{Reader: bytes.NewReader(m.Bytes()), ms: ms, m: m}, nil
	}
	return nil, os.ErrNotExist
}

func (ms *memStorage) Create(fd FileDesc) (Writer, error) {
	if !FileDescOk(fd) {
		return nil, ErrInvalidFile
	}

	x := packFile(fd)
	ms.mu.Lock()
	defer ms.mu.Unlock()
	m, exist := ms.files[x]
	if exist {
		if m.open {
			return nil, errFileOpen
		}
		m.Reset()
	} else {
		m = &memFile{}
		ms.files[x] = m
	}
	m.open = true
	return &memWriter{memFile: m, ms: ms}, nil
}

func (ms *memStorage) Remove(fd FileDesc) error {
	if !FileDescOk(fd) {
		return ErrInvalidFile
	}

	x := packFile(fd)
	ms.mu.Lock()
	defer ms.mu.Unlock()
	if _, exist := ms.files[x]; exist {
		delete(ms.files, x)
		return nil
	}
	return os.ErrNotExist
}

func (ms *memStorage) Rename(oldfd, newfd FileDesc) error {
	if !FileDescOk(oldfd) || !FileDescOk(newfd) {
		return ErrInvalidFile
	}
	if oldfd == newfd {
		return nil
	}

	oldx := packFile(oldfd)
	newx := packFile(newfd)
	ms.mu.Lock()
	defer ms.mu.Unlock()
	oldm, exist := ms.files[oldx]
	if !exist {
		return os.ErrNotExist
	}
	newm, exist := ms.files[newx]
	if (exist && newm.open) || oldm.open {
		return errFileOpen
	}
	delete(ms.files, oldx)
	ms.files[newx] = oldm
	return nil
}

func (*memStorage) Close() error { return nil }

type memFile struct {
	bytes.Buffer
	open bool
}

type memReader struct {
	*bytes.Reader
	ms     *memStorage
	m      *memFile
	closed bool
}

func (mr *memReader) Close() error {
	mr.ms.mu.Lock()
	defer mr.ms.mu.Unlock()
	if mr.closed {
		return ErrClosed
	}
	mr.m.open = false
	return nil
}

type memWriter struct {
	*memFile
	ms     *memStorage
	closed bool
}

func (*memWriter) Sync() error { return nil }

func (mw *memWriter) Close() error {
	mw.ms.mu.Lock()
	defer mw.ms.mu.Unlock()
	if mw.closed {
		return ErrClosed
	}
	mw.memFile.open = false
	return nil
}

func packFile(fd FileDesc) uint64 {
	return uint64(fd.Num)<<typeShift | uint64(fd.Type)
}

func unpackFile(x uint64) FileDesc {
	return FileDesc{FileType(x) & TypeAll, int64(x >> typeShift)}
}
```

## File: `leveldb/storage/mem_storage_test.go`
```go
// Copyright (c) 2013, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package storage

import (
	"bytes"
	"fmt"
	"testing"
)

func TestMemStorage(t *testing.T) {
	m := NewMemStorage()

	l, err := m.Lock()
	if err != nil {
		t.Fatal("storage lock failed(1): ", err)
	}
	_, err = m.Lock()
	if err == nil {
		t.Fatal("expect error for second storage lock attempt")
	} else {
		t.Logf("storage lock got error: %s (expected)", err)
	}
	l.Unlock()
	_, err = m.Lock()
	if err != nil {
		t.Fatal("storage lock failed(2): ", err)
	}

	w, err := m.Create(FileDesc{TypeTable, 1})
	if err != nil {
		t.Fatal("Storage.Create: ", err)
	}
	if _, err := w.Write([]byte("abc")); err != nil {
		t.Fatal("Storage.Write: ", err)
	}
	w.Close()
	if fds, _ := m.List(TypeAll); len(fds) != 1 {
		t.Fatal("invalid GetFiles len")
	}
	buf := new(bytes.Buffer)
	r, err := m.Open(FileDesc{TypeTable, 1})
	if err != nil {
		t.Fatal("Open: got error: ", err)
	}
	if _, err := buf.ReadFrom(r); err != nil {
		t.Fatal("ReadFrom: got error: ", err)
	}
	r.Close()
	if got := buf.String(); got != "abc" {
		t.Fatalf("Read: invalid value, want=abc got=%s", got)
	}
	if _, err := m.Open(FileDesc{TypeTable, 1}); err != nil {
		t.Fatal("Open: got error: ", err)
	}
	if _, err := m.Open(FileDesc{TypeTable, 1}); err == nil {
		t.Fatal("expecting error")
	}
	if err := m.Remove(FileDesc{TypeTable, 1}); err != nil {
		t.Fatal("Remove: got error: ", err)
	}
	if fds, _ := m.List(TypeAll); len(fds) != 0 {
		t.Fatal("invalid GetFiles len", len(fds))
	}
	if _, err := m.Open(FileDesc{TypeTable, 1}); err == nil {
		t.Fatal("expecting error")
	}
}

func TestMemStorageRename(t *testing.T) {
	fd1 := FileDesc{Type: TypeTable, Num: 1}
	fd2 := FileDesc{Type: TypeTable, Num: 2}

	m := NewMemStorage()
	w, err := m.Create(fd1)
	if err != nil {
		t.Fatalf("Storage.Create: %v", err)
	}

	fmt.Fprintf(w, "abc")
	w.Close()

	rd, err := m.Open(fd1)
	if err != nil {
		t.Fatalf("Storage.Open(%v): %v", fd1, err)
	}
	rd.Close()

	fds, err := m.List(TypeAll)
	if err != nil {
		t.Fatalf("Storage.List: %v", err)
	}
	for _, fd := range fds {
		if !FileDescOk(fd) {
			t.Errorf("Storage.List -> FileDescOk(%q)", fd)
		}
	}

	err = m.Rename(fd1, fd2)
	if err != nil {
		t.Fatalf("Storage.Rename: %v", err)
	}

	rd, err = m.Open(fd2)
	if err != nil {
		t.Fatalf("Storage.Open(%v): %v", fd2, err)
	}
	rd.Close()

	fds, err = m.List(TypeAll)
	if err != nil {
		t.Fatalf("Storage.List: %v", err)
	}
	for _, fd := range fds {
		if !FileDescOk(fd) {
			t.Errorf("Storage.List -> FileDescOk(%q)", fd)
		}
	}
}
```

## File: `leveldb/storage/storage.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package storage provides storage abstraction for LevelDB.
package storage

import (
	"errors"
	"fmt"
	"io"
)

// FileType represent a file type.
type FileType int

// File types.
const (
	TypeManifest FileType = 1 << iota
	TypeJournal
	TypeTable
	TypeTemp

	TypeAll = TypeManifest | TypeJournal | TypeTable | TypeTemp
)

func (t FileType) String() string {
	switch t {
	case TypeManifest:
		return "manifest"
	case TypeJournal:
		return "journal"
	case TypeTable:
		return "table"
	case TypeTemp:
		return "temp"
	}
	return fmt.Sprintf("<unknown:%d>", t)
}

// Common error.
var (
	ErrInvalidFile = errors.New("leveldb/storage: invalid file for argument")
	ErrLocked      = errors.New("leveldb/storage: already locked")
	ErrClosed      = errors.New("leveldb/storage: closed")
)

// ErrCorrupted is the type that wraps errors that indicate corruption of
// a file. Package storage has its own type instead of using
// errors.ErrCorrupted to prevent circular import.
type ErrCorrupted struct {
	Fd  FileDesc
	Err error
}

func isCorrupted(err error) bool {
	switch err.(type) {
	case *ErrCorrupted:
		return true
	default:
		return false
	}
}

func (e *ErrCorrupted) Error() string {
	if !e.Fd.Zero() {
		return fmt.Sprintf("%v [file=%v]", e.Err, e.Fd)
	}
	return e.Err.Error()
}

// Syncer is the interface that wraps basic Sync method.
type Syncer interface {
	// Sync commits the current contents of the file to stable storage.
	Sync() error
}

// Reader is the interface that groups the basic Read, Seek, ReadAt and Close
// methods.
type Reader interface {
	io.ReadSeeker
	io.ReaderAt
	io.Closer
}

// Writer is the interface that groups the basic Write, Sync and Close
// methods.
type Writer interface {
	io.WriteCloser
	Syncer
}

// Locker is the interface that wraps Unlock method.
type Locker interface {
	Unlock()
}

// FileDesc is a 'file descriptor'.
type FileDesc struct {
	Type FileType
	Num  int64
}

func (fd FileDesc) String() string {
	switch fd.Type {
	case TypeManifest:
		return fmt.Sprintf("MANIFEST-%06d", fd.Num)
	case TypeJournal:
		return fmt.Sprintf("%06d.log", fd.Num)
	case TypeTable:
		return fmt.Sprintf("%06d.ldb", fd.Num)
	case TypeTemp:
		return fmt.Sprintf("%06d.tmp", fd.Num)
	default:
		return fmt.Sprintf("%#x-%d", fd.Type, fd.Num)
	}
}

// Zero returns true if fd == (FileDesc{}).
func (fd FileDesc) Zero() bool {
	return fd == (FileDesc{})
}

// FileDescOk returns true if fd is a valid 'file descriptor'.
func FileDescOk(fd FileDesc) bool {
	switch fd.Type {
	case TypeManifest:
	case TypeJournal:
	case TypeTable:
	case TypeTemp:
	default:
		return false
	}
	return fd.Num >= 0
}

// Storage is the storage. A storage instance must be safe for concurrent use.
type Storage interface {
	// Lock locks the storage. Any subsequent attempt to call Lock will fail
	// until the last lock released.
	// Caller should call Unlock method after use.
	Lock() (Locker, error)

	// Log logs a string. This is used for logging.
	// An implementation may write to a file, stdout or simply do nothing.
	Log(str string)

	// SetMeta store 'file descriptor' that can later be acquired using GetMeta
	// method. The 'file descriptor' should point to a valid file.
	// SetMeta should be implemented in such way that changes should happen
	// atomically.
	SetMeta(fd FileDesc) error

	// GetMeta returns 'file descriptor' stored in meta. The 'file descriptor'
	// can be updated using SetMeta method.
	// Returns os.ErrNotExist if meta doesn't store any 'file descriptor', or
	// 'file descriptor' point to nonexistent file.
	GetMeta() (FileDesc, error)

	// List returns file descriptors that match the given file types.
	// The file types may be OR'ed together.
	List(ft FileType) ([]FileDesc, error)

	// Open opens file with the given 'file descriptor' read-only.
	// Returns os.ErrNotExist error if the file does not exist.
	// Returns ErrClosed if the underlying storage is closed.
	Open(fd FileDesc) (Reader, error)

	// Create creates file with the given 'file descriptor', truncate if already
	// exist and opens write-only.
	// Returns ErrClosed if the underlying storage is closed.
	Create(fd FileDesc) (Writer, error)

	// Remove removes file with the given 'file descriptor'.
	// Returns ErrClosed if the underlying storage is closed.
	Remove(fd FileDesc) error

	// Rename renames file from oldfd to newfd.
	// Returns ErrClosed if the underlying storage is closed.
	Rename(oldfd, newfd FileDesc) error

	// Close closes the storage.
	// It is valid to call Close multiple times. Other methods should not be
	// called after the storage has been closed.
	Close() error
}
```

## File: `leveldb/table/block_test.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package table

import (
	"encoding/binary"
	"fmt"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/comparer"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/testutil"
	"github.com/syndtr/goleveldb/leveldb/util"
)

type blockTesting struct {
	tr *Reader
	b  *block
}

func (t *blockTesting) TestNewIterator(slice *util.Range) iterator.Iterator {
	return t.tr.newBlockIter(t.b, nil, slice, false)
}

var _ = testutil.Defer(func() {
	Describe("Block", func() {
		Build := func(kv *testutil.KeyValue, restartInterval int) *blockTesting {
			// Building the block.
			bw := &blockWriter{
				restartInterval: restartInterval,
				scratch:         make([]byte, 30),
			}
			kv.Iterate(func(i int, key, value []byte) {
				Expect(bw.append(key, value)).ShouldNot(HaveOccurred())
			})
			Expect(bw.finish()).ShouldNot(HaveOccurred())

			// Opening the block.
			data := bw.buf.Bytes()
			restartsLen := int(binary.LittleEndian.Uint32(data[len(data)-4:]))
			return &blockTesting{
				tr: &Reader{cmp: comparer.DefaultComparer},
				b: &block{
					data:           data,
					restartsLen:    restartsLen,
					restartsOffset: len(data) - (restartsLen+1)*4,
				},
			}
		}

		Describe("read test", func() {
			for restartInterval := 1; restartInterval <= 5; restartInterval++ {
				Describe(fmt.Sprintf("with restart interval of %d", restartInterval), func() {
					kv := &testutil.KeyValue{}
					Text := func() string {
						return fmt.Sprintf("and %d keys", kv.Len())
					}

					Test := func() {
						// Make block.
						br := Build(kv, restartInterval)
						// Do testing.
						testutil.KeyValueTesting(nil, kv.Clone(), br, nil, nil)
					}

					Describe(Text(), Test)

					kv.PutString("", "empty")
					Describe(Text(), Test)

					kv.PutString("a1", "foo")
					Describe(Text(), Test)

					kv.PutString("a2", "v")
					Describe(Text(), Test)

					kv.PutString("a3qqwrkks", "hello")
					Describe(Text(), Test)

					kv.PutString("a4", "bar")
					Describe(Text(), Test)

					kv.PutString("a5111111", "v5")
					kv.PutString("a6", "")
					kv.PutString("a7", "v7")
					kv.PutString("a8", "vvvvvvvvvvvvvvvvvvvvvv8")
					kv.PutString("b", "v9")
					kv.PutString("c9", "v9")
					kv.PutString("c91", "v9")
					kv.PutString("d0", "v9")
					Describe(Text(), Test)
				})
			}
		})

		Describe("out-of-bound slice test", func() {
			kv := &testutil.KeyValue{}
			kv.PutString("k1", "v1")
			kv.PutString("k2", "v2")
			kv.PutString("k3abcdefgg", "v3")
			kv.PutString("k4", "v4")
			kv.PutString("k5", "v5")
			for restartInterval := 1; restartInterval <= 5; restartInterval++ {
				Describe(fmt.Sprintf("with restart interval of %d", restartInterval), func() {
					// Make block.
					bt := Build(kv, restartInterval)

					Test := func(r *util.Range) func(done Done) {
						return func(done Done) {
							iter := bt.TestNewIterator(r)
							Expect(iter.Error()).ShouldNot(HaveOccurred())

							t := testutil.IteratorTesting{
								KeyValue: kv.Clone(),
								Iter:     iter,
							}

							testutil.DoIteratorTesting(&t)
							iter.Release()
							done <- true
						}
					}

					It("Should do iterations and seeks correctly #0",
						Test(&util.Range{Start: []byte("k0"), Limit: []byte("k6")}), 2.0)

					It("Should do iterations and seeks correctly #1",
						Test(&util.Range{Start: []byte(""), Limit: []byte("zzzzzzz")}), 2.0)
				})
			}
		})
	})
})
```

## File: `leveldb/table/reader.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package table

import (
	"encoding/binary"
	"fmt"
	"io"
	"sort"
	"strings"
	"sync"

	"github.com/golang/snappy"

	"github.com/syndtr/goleveldb/leveldb/cache"
	"github.com/syndtr/goleveldb/leveldb/comparer"
	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/filter"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/util"
)

// Reader errors.
var (
	ErrNotFound       = errors.ErrNotFound
	ErrReaderReleased = errors.New("leveldb/table: reader released")
	ErrIterReleased   = errors.New("leveldb/table: iterator released")
)

// ErrCorrupted describes error due to corruption. This error will be wrapped
// with errors.ErrCorrupted.
type ErrCorrupted struct {
	Pos    int64
	Size   int64
	Kind   string
	Reason string
}

func (e *ErrCorrupted) Error() string {
	return fmt.Sprintf("leveldb/table: corruption on %s (pos=%d): %s", e.Kind, e.Pos, e.Reason)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

type block struct {
	bpool          *util.BufferPool
	bh             blockHandle
	data           []byte
	restartsLen    int
	restartsOffset int
}

func (b *block) seek(cmp comparer.Comparer, rstart, rlimit int, key []byte) (index, offset int, err error) {
	index = sort.Search(b.restartsLen-rstart-(b.restartsLen-rlimit), func(i int) bool {
		offset := int(binary.LittleEndian.Uint32(b.data[b.restartsOffset+4*(rstart+i):]))
		offset++                                    // shared always zero, since this is a restart point
		v1, n1 := binary.Uvarint(b.data[offset:])   // key length
		_, n2 := binary.Uvarint(b.data[offset+n1:]) // value length
		m := offset + n1 + n2
		return cmp.Compare(b.data[m:m+int(v1)], key) > 0
	}) + rstart - 1
	if index < rstart {
		// The smallest key is greater-than key sought.
		index = rstart
	}
	offset = int(binary.LittleEndian.Uint32(b.data[b.restartsOffset+4*index:]))
	return
}

func (b *block) restartIndex(rstart, rlimit, offset int) int {
	return sort.Search(b.restartsLen-rstart-(b.restartsLen-rlimit), func(i int) bool {
		return int(binary.LittleEndian.Uint32(b.data[b.restartsOffset+4*(rstart+i):])) > offset
	}) + rstart - 1
}

func (b *block) restartOffset(index int) int {
	return int(binary.LittleEndian.Uint32(b.data[b.restartsOffset+4*index:]))
}

func (b *block) entry(offset int) (key, value []byte, nShared, n int, err error) {
	if offset >= b.restartsOffset {
		if offset != b.restartsOffset {
			err = &ErrCorrupted{Reason: "entries offset not aligned"}
		}
		return
	}
	v0, n0 := binary.Uvarint(b.data[offset:])       // Shared prefix length
	v1, n1 := binary.Uvarint(b.data[offset+n0:])    // Key length
	v2, n2 := binary.Uvarint(b.data[offset+n0+n1:]) // Value length
	m := n0 + n1 + n2
	n = m + int(v1) + int(v2)
	if n0 <= 0 || n1 <= 0 || n2 <= 0 || offset+n > b.restartsOffset {
		err = &ErrCorrupted{Reason: "entries corrupted"}
		return
	}
	key = b.data[offset+m : offset+m+int(v1)]
	value = b.data[offset+m+int(v1) : offset+n]
	nShared = int(v0)
	return
}

func (b *block) Release() {
	b.bpool.Put(b.data)
	b.bpool = nil
	b.data = nil
}

type dir int

const (
	dirReleased dir = iota - 1
	dirSOI
	dirEOI
	dirBackward
	dirForward
)

type blockIter struct {
	tr            *Reader
	block         *block
	blockReleaser util.Releaser
	releaser      util.Releaser
	key, value    []byte
	offset        int
	// Previous offset, only filled by Next.
	prevOffset   int
	prevNode     []int
	prevKeys     []byte
	restartIndex int
	// Iterator direction.
	dir dir
	// Restart index slice range.
	riStart int
	riLimit int
	// Offset slice range.
	offsetStart     int
	offsetRealStart int
	offsetLimit     int
	// Error.
	err error
}

func (i *blockIter) sErr(err error) {
	i.err = err
	i.key = nil
	i.value = nil
	i.prevNode = nil
	i.prevKeys = nil
}

func (i *blockIter) reset() {
	if i.dir == dirBackward {
		i.prevNode = i.prevNode[:0]
		i.prevKeys = i.prevKeys[:0]
	}
	i.restartIndex = i.riStart
	i.offset = i.offsetStart
	i.dir = dirSOI
	i.key = i.key[:0]
	i.value = nil
}

func (i *blockIter) isFirst() bool {
	switch i.dir {
	case dirForward:
		return i.prevOffset == i.offsetRealStart
	case dirBackward:
		return len(i.prevNode) == 1 && i.restartIndex == i.riStart
	}
	return false
}

func (i *blockIter) isLast() bool {
	switch i.dir {
	case dirForward, dirBackward:
		return i.offset == i.offsetLimit
	}
	return false
}

func (i *blockIter) First() bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	if i.dir == dirBackward {
		i.prevNode = i.prevNode[:0]
		i.prevKeys = i.prevKeys[:0]
	}
	i.dir = dirSOI
	return i.Next()
}

func (i *blockIter) Last() bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	if i.dir == dirBackward {
		i.prevNode = i.prevNode[:0]
		i.prevKeys = i.prevKeys[:0]
	}
	i.dir = dirEOI
	return i.Prev()
}

func (i *blockIter) Seek(key []byte) bool {
	if i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	ri, offset, err := i.block.seek(i.tr.cmp, i.riStart, i.riLimit, key)
	if err != nil {
		i.sErr(err)
		return false
	}
	i.restartIndex = ri
	i.offset = max(i.offsetStart, offset)
	if i.dir == dirSOI || i.dir == dirEOI {
		i.dir = dirForward
	}
	for i.Next() {
		if i.tr.cmp.Compare(i.key, key) >= 0 {
			return true
		}
	}
	return false
}

func (i *blockIter) Next() bool {
	if i.dir == dirEOI || i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	if i.dir == dirSOI {
		i.restartIndex = i.riStart
		i.offset = i.offsetStart
	} else if i.dir == dirBackward {
		i.prevNode = i.prevNode[:0]
		i.prevKeys = i.prevKeys[:0]
	}
	for i.offset < i.offsetRealStart {
		key, value, nShared, n, err := i.block.entry(i.offset)
		if err != nil {
			i.sErr(i.tr.fixErrCorruptedBH(i.block.bh, err))
			return false
		}
		if n == 0 {
			i.dir = dirEOI
			return false
		}
		i.key = append(i.key[:nShared], key...)
		i.value = value
		i.offset += n
	}
	if i.offset >= i.offsetLimit {
		i.dir = dirEOI
		if i.offset != i.offsetLimit {
			i.sErr(i.tr.newErrCorruptedBH(i.block.bh, "entries offset not aligned"))
		}
		return false
	}
	key, value, nShared, n, err := i.block.entry(i.offset)
	if err != nil {
		i.sErr(i.tr.fixErrCorruptedBH(i.block.bh, err))
		return false
	}
	if n == 0 {
		i.dir = dirEOI
		return false
	}
	i.key = append(i.key[:nShared], key...)
	i.value = value
	i.prevOffset = i.offset
	i.offset += n
	i.dir = dirForward
	return true
}

func (i *blockIter) Prev() bool {
	if i.dir == dirSOI || i.err != nil {
		return false
	} else if i.dir == dirReleased {
		i.err = ErrIterReleased
		return false
	}

	var ri int
	if i.dir == dirForward {
		// Change direction.
		i.offset = i.prevOffset
		if i.offset == i.offsetRealStart {
			i.dir = dirSOI
			return false
		}
		ri = i.block.restartIndex(i.restartIndex, i.riLimit, i.offset)
		i.dir = dirBackward
	} else if i.dir == dirEOI {
		// At the end of iterator.
		i.restartIndex = i.riLimit
		i.offset = i.offsetLimit
		if i.offset == i.offsetRealStart {
			i.dir = dirSOI
			return false
		}
		ri = i.riLimit - 1
		i.dir = dirBackward
	} else if len(i.prevNode) == 1 {
		// This is the end of a restart range.
		i.offset = i.prevNode[0]
		i.prevNode = i.prevNode[:0]
		if i.restartIndex == i.riStart {
			i.dir = dirSOI
			return false
		}
		i.restartIndex--
		ri = i.restartIndex
	} else {
		// In the middle of restart range, get from cache.
		n := len(i.prevNode) - 3
		node := i.prevNode[n:]
		i.prevNode = i.prevNode[:n]
		// Get the key.
		ko := node[0]
		i.key = append(i.key[:0], i.prevKeys[ko:]...)
		i.prevKeys = i.prevKeys[:ko]
		// Get the value.
		vo := node[1]
		vl := vo + node[2]
		i.value = i.block.data[vo:vl]
		i.offset = vl
		return true
	}
	// Build entries cache.
	i.key = i.key[:0]
	i.value = nil
	offset := i.block.restartOffset(ri)
	if offset == i.offset {
		ri--
		if ri < 0 {
			i.dir = dirSOI
			return false
		}
		offset = i.block.restartOffset(ri)
	}
	i.prevNode = append(i.prevNode, offset)
	for {
		key, value, nShared, n, err := i.block.entry(offset)
		if err != nil {
			i.sErr(i.tr.fixErrCorruptedBH(i.block.bh, err))
			return false
		}
		if offset >= i.offsetRealStart {
			if i.value != nil {
				// Appends 3 variables:
				// 1. Previous keys offset
				// 2. Value offset in the data block
				// 3. Value length
				i.prevNode = append(i.prevNode, len(i.prevKeys), offset-len(i.value), len(i.value))
				i.prevKeys = append(i.prevKeys, i.key...)
			}
			i.value = value
		}
		i.key = append(i.key[:nShared], key...)
		offset += n
		// Stop if target offset reached.
		if offset >= i.offset {
			if offset != i.offset {
				i.sErr(i.tr.newErrCorruptedBH(i.block.bh, "entries offset not aligned"))
				return false
			}

			break
		}
	}
	i.restartIndex = ri
	i.offset = offset
	return true
}

func (i *blockIter) Key() []byte {
	if i.err != nil || i.dir <= dirEOI {
		return nil
	}
	return i.key
}

func (i *blockIter) Value() []byte {
	if i.err != nil || i.dir <= dirEOI {
		return nil
	}
	return i.value
}

func (i *blockIter) Release() {
	if i.dir != dirReleased {
		i.tr = nil
		i.block = nil
		i.prevNode = nil
		i.prevKeys = nil
		i.key = nil
		i.value = nil
		i.dir = dirReleased
		if i.blockReleaser != nil {
			i.blockReleaser.Release()
			i.blockReleaser = nil
		}
		if i.releaser != nil {
			i.releaser.Release()
			i.releaser = nil
		}
	}
}

func (i *blockIter) SetReleaser(releaser util.Releaser) {
	if i.dir == dirReleased {
		panic(util.ErrReleased)
	}
	if i.releaser != nil && releaser != nil {
		panic(util.ErrHasReleaser)
	}
	i.releaser = releaser
}

func (i *blockIter) Valid() bool {
	return i.err == nil && (i.dir == dirBackward || i.dir == dirForward)
}

func (i *blockIter) Error() error {
	return i.err
}

type filterBlock struct {
	bpool      *util.BufferPool
	data       []byte
	oOffset    int
	baseLg     uint
	filtersNum int
}

func (b *filterBlock) contains(filter filter.Filter, offset uint64, key []byte) bool {
	i := int(offset >> b.baseLg)
	if i < b.filtersNum {
		o := b.data[b.oOffset+i*4:]
		n := int(binary.LittleEndian.Uint32(o))
		m := int(binary.LittleEndian.Uint32(o[4:]))
		if n < m && m <= b.oOffset {
			return filter.Contains(b.data[n:m], key)
		} else if n == m {
			return false
		}
	}
	return true
}

func (b *filterBlock) Release() {
	b.bpool.Put(b.data)
	b.bpool = nil
	b.data = nil
}

type indexIter struct {
	*blockIter
	tr    *Reader
	slice *util.Range
	// Options
	fillCache bool
}

func (i *indexIter) Get() iterator.Iterator {
	value := i.Value()
	if value == nil {
		return nil
	}
	dataBH, n := decodeBlockHandle(value)
	if n == 0 {
		return iterator.NewEmptyIterator(i.tr.newErrCorruptedBH(i.tr.indexBH, "bad data block handle"))
	}

	var slice *util.Range
	if i.slice != nil && (i.blockIter.isFirst() || i.blockIter.isLast()) {
		slice = i.slice
	}
	return i.tr.getDataIterErr(dataBH, slice, i.tr.verifyChecksum, i.fillCache)
}

// Reader is a table reader.
type Reader struct {
	mu     sync.RWMutex
	fd     storage.FileDesc
	reader io.ReaderAt
	cache  *cache.NamespaceGetter
	err    error
	bpool  *util.BufferPool
	// Options
	o              *opt.Options
	cmp            comparer.Comparer
	filter         filter.Filter
	verifyChecksum bool

	dataEnd                   int64
	metaBH, indexBH, filterBH blockHandle
	indexBlock                *block
	filterBlock               *filterBlock
}

func (r *Reader) blockKind(bh blockHandle) string {
	switch bh.offset {
	case r.metaBH.offset:
		return "meta-block"
	case r.indexBH.offset:
		return "index-block"
	case r.filterBH.offset:
		if r.filterBH.length > 0 {
			return "filter-block"
		}
	}
	return "data-block"
}

func (r *Reader) newErrCorrupted(pos, size int64, kind, reason string) error {
	return &errors.ErrCorrupted{Fd: r.fd, Err: &ErrCorrupted{Pos: pos, Size: size, Kind: kind, Reason: reason}}
}

func (r *Reader) newErrCorruptedBH(bh blockHandle, reason string) error {
	return r.newErrCorrupted(int64(bh.offset), int64(bh.length), r.blockKind(bh), reason)
}

func (r *Reader) fixErrCorruptedBH(bh blockHandle, err error) error {
	if cerr, ok := err.(*ErrCorrupted); ok {
		cerr.Pos = int64(bh.offset)
		cerr.Size = int64(bh.length)
		cerr.Kind = r.blockKind(bh)
		return &errors.ErrCorrupted{Fd: r.fd, Err: cerr}
	}
	return err
}

func (r *Reader) readRawBlock(bh blockHandle, verifyChecksum bool) ([]byte, error) {
	data := r.bpool.Get(int(bh.length + blockTrailerLen))
	if _, err := r.reader.ReadAt(data, int64(bh.offset)); err != nil && err != io.EOF {
		return nil, err
	}

	if verifyChecksum {
		n := bh.length + 1
		checksum0 := binary.LittleEndian.Uint32(data[n:])
		checksum1 := util.NewCRC(data[:n]).Value()
		if checksum0 != checksum1 {
			r.bpool.Put(data)
			return nil, r.newErrCorruptedBH(bh, fmt.Sprintf("checksum mismatch, want=%#x got=%#x", checksum0, checksum1))
		}
	}

	switch data[bh.length] {
	case blockTypeNoCompression:
		data = data[:bh.length]
	case blockTypeSnappyCompression:
		decLen, err := snappy.DecodedLen(data[:bh.length])
		if err != nil {
			r.bpool.Put(data)
			return nil, r.newErrCorruptedBH(bh, err.Error())
		}
		decData := r.bpool.Get(decLen)
		decData, err = snappy.Decode(decData, data[:bh.length])
		r.bpool.Put(data)
		if err != nil {
			r.bpool.Put(decData)
			return nil, r.newErrCorruptedBH(bh, err.Error())
		}
		data = decData
	default:
		r.bpool.Put(data)
		return nil, r.newErrCorruptedBH(bh, fmt.Sprintf("unknown compression type %#x", data[bh.length]))
	}
	return data, nil
}

func (r *Reader) readBlock(bh blockHandle, verifyChecksum bool) (*block, error) {
	data, err := r.readRawBlock(bh, verifyChecksum)
	if err != nil {
		return nil, err
	}
	restartsLen := int(binary.LittleEndian.Uint32(data[len(data)-4:]))
	b := &block{
		bpool:          r.bpool,
		bh:             bh,
		data:           data,
		restartsLen:    restartsLen,
		restartsOffset: len(data) - (restartsLen+1)*4,
	}
	return b, nil
}

func (r *Reader) readBlockCached(bh blockHandle, verifyChecksum, fillCache bool) (*block, util.Releaser, error) {
	if r.cache != nil {
		var (
			err error
			ch  *cache.Handle
		)
		if fillCache {
			ch = r.cache.Get(bh.offset, func() (size int, value cache.Value) {
				var b *block
				b, err = r.readBlock(bh, verifyChecksum)
				if err != nil {
					return 0, nil
				}
				return cap(b.data), b
			})
		} else {
			ch = r.cache.Get(bh.offset, nil)
		}
		if ch != nil {
			b, ok := ch.Value().(*block)
			if !ok {
				ch.Release()
				return nil, nil, errors.New("leveldb/table: inconsistent block type")
			}
			return b, ch, err
		} else if err != nil {
			return nil, nil, err
		}
	}

	b, err := r.readBlock(bh, verifyChecksum)
	return b, b, err
}

func (r *Reader) readFilterBlock(bh blockHandle) (*filterBlock, error) {
	data, err := r.readRawBlock(bh, true)
	if err != nil {
		return nil, err
	}
	n := len(data)
	if n < 5 {
		return nil, r.newErrCorruptedBH(bh, "too short")
	}
	m := n - 5
	oOffset := int(binary.LittleEndian.Uint32(data[m:]))
	if oOffset > m {
		return nil, r.newErrCorruptedBH(bh, "invalid data-offsets offset")
	}
	b := &filterBlock{
		bpool:      r.bpool,
		data:       data,
		oOffset:    oOffset,
		baseLg:     uint(data[n-1]),
		filtersNum: (m - oOffset) / 4,
	}
	return b, nil
}

func (r *Reader) readFilterBlockCached(bh blockHandle, fillCache bool) (*filterBlock, util.Releaser, error) {
	if r.cache != nil {
		var (
			err error
			ch  *cache.Handle
		)
		if fillCache {
			ch = r.cache.Get(bh.offset, func() (size int, value cache.Value) {
				var b *filterBlock
				b, err = r.readFilterBlock(bh)
				if err != nil {
					return 0, nil
				}
				return cap(b.data), b
			})
		} else {
			ch = r.cache.Get(bh.offset, nil)
		}
		if ch != nil {
			b, ok := ch.Value().(*filterBlock)
			if !ok {
				ch.Release()
				return nil, nil, errors.New("leveldb/table: inconsistent block type")
			}
			return b, ch, err
		} else if err != nil {
			return nil, nil, err
		}
	}

	b, err := r.readFilterBlock(bh)
	return b, b, err
}

func (r *Reader) getIndexBlock(fillCache bool) (b *block, rel util.Releaser, err error) {
	if r.indexBlock == nil {
		return r.readBlockCached(r.indexBH, true, fillCache)
	}
	return r.indexBlock, util.NoopReleaser{}, nil
}

func (r *Reader) getFilterBlock(fillCache bool) (*filterBlock, util.Releaser, error) {
	if r.filterBlock == nil {
		return r.readFilterBlockCached(r.filterBH, fillCache)
	}
	return r.filterBlock, util.NoopReleaser{}, nil
}

func (r *Reader) newBlockIter(b *block, bReleaser util.Releaser, slice *util.Range, inclLimit bool) *blockIter {
	bi := &blockIter{
		tr:            r,
		block:         b,
		blockReleaser: bReleaser,
		// Valid key should never be nil.
		key:             make([]byte, 0),
		dir:             dirSOI,
		riStart:         0,
		riLimit:         b.restartsLen,
		offsetStart:     0,
		offsetRealStart: 0,
		offsetLimit:     b.restartsOffset,
	}
	if slice != nil {
		if slice.Start != nil {
			if bi.Seek(slice.Start) {
				bi.riStart = b.restartIndex(bi.restartIndex, b.restartsLen, bi.prevOffset)
				bi.offsetStart = b.restartOffset(bi.riStart)
				bi.offsetRealStart = bi.prevOffset
			} else {
				bi.riStart = b.restartsLen
				bi.offsetStart = b.restartsOffset
				bi.offsetRealStart = b.restartsOffset
			}
		}
		if slice.Limit != nil {
			if bi.Seek(slice.Limit) && (!inclLimit || bi.Next()) {
				bi.offsetLimit = bi.prevOffset
				bi.riLimit = bi.restartIndex + 1
			}
		}
		bi.reset()
		if bi.offsetStart > bi.offsetLimit {
			bi.sErr(errors.New("leveldb/table: invalid slice range"))
		}
	}
	return bi
}

func (r *Reader) getDataIter(dataBH blockHandle, slice *util.Range, verifyChecksum, fillCache bool) iterator.Iterator {
	b, rel, err := r.readBlockCached(dataBH, verifyChecksum, fillCache)
	if err != nil {
		return iterator.NewEmptyIterator(err)
	}
	return r.newBlockIter(b, rel, slice, false)
}

func (r *Reader) getDataIterErr(dataBH blockHandle, slice *util.Range, verifyChecksum, fillCache bool) iterator.Iterator {
	r.mu.RLock()
	defer r.mu.RUnlock()

	if r.err != nil {
		return iterator.NewEmptyIterator(r.err)
	}

	return r.getDataIter(dataBH, slice, verifyChecksum, fillCache)
}

// NewIterator creates an iterator from the table.
//
// Slice allows slicing the iterator to only contains keys in the given
// range. A nil Range.Start is treated as a key before all keys in the
// table. And a nil Range.Limit is treated as a key after all keys in
// the table.
//
// WARNING: Any slice returned by interator (e.g. slice returned by calling
// Iterator.Key() or Iterator.Key() methods), its content should not be modified
// unless noted otherwise.
//
// The returned iterator is not safe for concurrent use and should be released
// after use.
//
// Also read Iterator documentation of the leveldb/iterator package.
func (r *Reader) NewIterator(slice *util.Range, ro *opt.ReadOptions) iterator.Iterator {
	r.mu.RLock()
	defer r.mu.RUnlock()

	if r.err != nil {
		return iterator.NewEmptyIterator(r.err)
	}

	fillCache := !ro.GetDontFillCache()
	indexBlock, rel, err := r.getIndexBlock(fillCache)
	if err != nil {
		return iterator.NewEmptyIterator(err)
	}
	index := &indexIter{
		blockIter: r.newBlockIter(indexBlock, rel, slice, true),
		tr:        r,
		slice:     slice,
		fillCache: !ro.GetDontFillCache(),
	}
	return iterator.NewIndexedIterator(index, opt.GetStrict(r.o, ro, opt.StrictReader))
}

func (r *Reader) find(key []byte, filtered bool, ro *opt.ReadOptions, noValue bool) (rkey, value []byte, err error) {
	r.mu.RLock()
	defer r.mu.RUnlock()

	if r.err != nil {
		err = r.err
		return
	}

	indexBlock, rel, err := r.getIndexBlock(true)
	if err != nil {
		return
	}
	defer rel.Release()

	index := r.newBlockIter(indexBlock, nil, nil, true)
	defer index.Release()

	if !index.Seek(key) {
		if err = index.Error(); err == nil {
			err = ErrNotFound
		}
		return
	}

	dataBH, n := decodeBlockHandle(index.Value())
	if n == 0 {
		r.err = r.newErrCorruptedBH(r.indexBH, "bad data block handle")
		return nil, nil, r.err
	}

	// The filter should only used for exact match.
	if filtered && r.filter != nil {
		filterBlock, frel, ferr := r.getFilterBlock(true)
		if ferr == nil {
			if !filterBlock.contains(r.filter, dataBH.offset, key) {
				frel.Release()
				return nil, nil, ErrNotFound
			}
			frel.Release()
		} else if !errors.IsCorrupted(ferr) {
			return nil, nil, ferr
		}
	}

	data := r.getDataIter(dataBH, nil, r.verifyChecksum, !ro.GetDontFillCache())
	if !data.Seek(key) {
		data.Release()
		if err = data.Error(); err != nil {
			return
		}

		// The nearest greater-than key is the first key of the next block.
		if !index.Next() {
			if err = index.Error(); err == nil {
				err = ErrNotFound
			}
			return
		}

		dataBH, n = decodeBlockHandle(index.Value())
		if n == 0 {
			r.err = r.newErrCorruptedBH(r.indexBH, "bad data block handle")
			return nil, nil, r.err
		}

		data = r.getDataIter(dataBH, nil, r.verifyChecksum, !ro.GetDontFillCache())
		if !data.Next() {
			data.Release()
			if err = data.Error(); err == nil {
				err = ErrNotFound
			}
			return
		}
	}

	// Key doesn't use block buffer, no need to copy the buffer.
	rkey = data.Key()
	if !noValue {
		if r.bpool == nil {
			value = data.Value()
		} else {
			// Value does use block buffer, and since the buffer will be
			// recycled, it need to be copied.
			value = append([]byte(nil), data.Value()...)
		}
	}
	data.Release()
	return
}

// Find finds key/value pair whose key is greater than or equal to the
// given key. It returns ErrNotFound if the table doesn't contain
// such pair.
// If filtered is true then the nearest 'block' will be checked against
// 'filter data' (if present) and will immediately return ErrNotFound if
// 'filter data' indicates that such pair doesn't exist.
//
// The caller may modify the contents of the returned slice as it is its
// own copy.
// It is safe to modify the contents of the argument after Find returns.
func (r *Reader) Find(key []byte, filtered bool, ro *opt.ReadOptions) (rkey, value []byte, err error) {
	return r.find(key, filtered, ro, false)
}

// FindKey finds key that is greater than or equal to the given key.
// It returns ErrNotFound if the table doesn't contain such key.
// If filtered is true then the nearest 'block' will be checked against
// 'filter data' (if present) and will immediately return ErrNotFound if
// 'filter data' indicates that such key doesn't exist.
//
// The caller may modify the contents of the returned slice as it is its
// own copy.
// It is safe to modify the contents of the argument after Find returns.
func (r *Reader) FindKey(key []byte, filtered bool, ro *opt.ReadOptions) (rkey []byte, err error) {
	rkey, _, err = r.find(key, filtered, ro, true)
	return
}

// Get gets the value for the given key. It returns errors.ErrNotFound
// if the table does not contain the key.
//
// The caller may modify the contents of the returned slice as it is its
// own copy.
// It is safe to modify the contents of the argument after Find returns.
func (r *Reader) Get(key []byte, ro *opt.ReadOptions) (value []byte, err error) {
	r.mu.RLock()
	defer r.mu.RUnlock()

	if r.err != nil {
		err = r.err
		return
	}

	rkey, value, err := r.find(key, false, ro, false)
	if err == nil && r.cmp.Compare(rkey, key) != 0 {
		value = nil
		err = ErrNotFound
	}
	return
}

// OffsetOf returns approximate offset for the given key.
//
// It is safe to modify the contents of the argument after Get returns.
func (r *Reader) OffsetOf(key []byte) (offset int64, err error) {
	r.mu.RLock()
	defer r.mu.RUnlock()

	if r.err != nil {
		err = r.err
		return
	}

	indexBlock, rel, err := r.readBlockCached(r.indexBH, true, true)
	if err != nil {
		return
	}
	defer rel.Release()

	index := r.newBlockIter(indexBlock, nil, nil, true)
	defer index.Release()
	if index.Seek(key) {
		dataBH, n := decodeBlockHandle(index.Value())
		if n == 0 {
			r.err = r.newErrCorruptedBH(r.indexBH, "bad data block handle")
			return
		}
		offset = int64(dataBH.offset)
		return
	}
	err = index.Error()
	if err == nil {
		offset = r.dataEnd
	}
	return
}

// Release implements util.Releaser.
// It also close the file if it is an io.Closer.
func (r *Reader) Release() {
	r.mu.Lock()
	defer r.mu.Unlock()

	if closer, ok := r.reader.(io.Closer); ok {
		closer.Close()
	}
	if r.indexBlock != nil {
		r.indexBlock.Release()
		r.indexBlock = nil
	}
	if r.filterBlock != nil {
		r.filterBlock.Release()
		r.filterBlock = nil
	}
	r.reader = nil
	r.cache = nil
	r.bpool = nil
	r.err = ErrReaderReleased
}

// NewReader creates a new initialized table reader for the file.
// The fi, cache and bpool is optional and can be nil.
//
// The returned table reader instance is safe for concurrent use.
func NewReader(f io.ReaderAt, size int64, fd storage.FileDesc, cache *cache.NamespaceGetter, bpool *util.BufferPool, o *opt.Options) (*Reader, error) {
	if f == nil {
		return nil, errors.New("leveldb/table: nil file")
	}

	r := &Reader{
		fd:             fd,
		reader:         f,
		cache:          cache,
		bpool:          bpool,
		o:              o,
		cmp:            o.GetComparer(),
		verifyChecksum: o.GetStrict(opt.StrictBlockChecksum),
	}

	if size < footerLen {
		r.err = r.newErrCorrupted(0, size, "table", "too small")
		return r, nil
	}

	footerPos := size - footerLen
	var footer [footerLen]byte
	if _, err := r.reader.ReadAt(footer[:], footerPos); err != nil && err != io.EOF {
		return nil, err
	}
	if string(footer[footerLen-len(magic):footerLen]) != magic {
		r.err = r.newErrCorrupted(footerPos, footerLen, "table-footer", "bad magic number")
		return r, nil
	}

	var n int
	// Decode the metaindex block handle.
	r.metaBH, n = decodeBlockHandle(footer[:])
	if n == 0 {
		r.err = r.newErrCorrupted(footerPos, footerLen, "table-footer", "bad metaindex block handle")
		return r, nil
	}

	// Decode the index block handle.
	r.indexBH, n = decodeBlockHandle(footer[n:])
	if n == 0 {
		r.err = r.newErrCorrupted(footerPos, footerLen, "table-footer", "bad index block handle")
		return r, nil
	}

	// Read metaindex block.
	metaBlock, err := r.readBlock(r.metaBH, true)
	if err != nil {
		if errors.IsCorrupted(err) {
			r.err = err
			return r, nil
		}
		return nil, err
	}

	// Set data end.
	r.dataEnd = int64(r.metaBH.offset)

	// Read metaindex.
	metaIter := r.newBlockIter(metaBlock, nil, nil, true)
	for metaIter.Next() {
		key := string(metaIter.Key())
		if !strings.HasPrefix(key, "filter.") {
			continue
		}
		fn := key[7:]
		if f0 := o.GetFilter(); f0 != nil && f0.Name() == fn {
			r.filter = f0
		} else {
			for _, f0 := range o.GetAltFilters() {
				if f0.Name() == fn {
					r.filter = f0
					break
				}
			}
		}
		if r.filter != nil {
			filterBH, n := decodeBlockHandle(metaIter.Value())
			if n == 0 {
				continue
			}
			r.filterBH = filterBH
			// Update data end.
			r.dataEnd = int64(filterBH.offset)
			break
		}
	}
	metaIter.Release()
	metaBlock.Release()

	// Cache index and filter block locally, since we don't have global cache.
	if cache == nil {
		r.indexBlock, err = r.readBlock(r.indexBH, true)
		if err != nil {
			if errors.IsCorrupted(err) {
				r.err = err
				return r, nil
			}
			return nil, err
		}
		if r.filter != nil {
			r.filterBlock, err = r.readFilterBlock(r.filterBH)
			if err != nil {
				if !errors.IsCorrupted(err) {
					return nil, err
				}

				// Don't use filter then.
				r.filter = nil
			}
		}
	}

	return r, nil
}
```

## File: `leveldb/table/table.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package table allows read and write sorted key/value.
package table

import (
	"encoding/binary"
)

/*
Table:

Table is consist of one or more data blocks, an optional filter block
a metaindex block, an index block and a table footer. Metaindex block
is a special block used to keep parameters of the table, such as filter
block name and its block handle. Index block is a special block used to
keep record of data blocks offset and length, index block use one as
restart interval. The key used by index block are the last key of preceding
block, shorter separator of adjacent blocks or shorter successor of the
last key of the last block. Filter block is an optional block contains
sequence of filter data generated by a filter generator.

Table data structure:
                                                         + optional
                                                        /
    +--------------+--------------+--------------+------+-------+-----------------+-------------+--------+
    | data block 1 |      ...     | data block n | filter block | metaindex block | index block | footer |
    +--------------+--------------+--------------+--------------+-----------------+-------------+--------+

    Each block followed by a 5-bytes trailer contains compression type and checksum.

Table block trailer:

    +---------------------------+-------------------+
    | compression type (1-byte) | checksum (4-byte) |
    +---------------------------+-------------------+

    The checksum is a CRC-32 computed using Castagnoli's polynomial. Compression
    type also included in the checksum.

Table footer:

      +------------------- 40-bytes -------------------+
     /                                                  \
    +------------------------+--------------------+------+-----------------+
    | metaindex block handle / index block handle / ---- | magic (8-bytes) |
    +------------------------+--------------------+------+-----------------+

    The magic are first 64-bit of SHA-1 sum of "http://code.google.com/p/leveldb/".

NOTE: All fixed-length integer are little-endian.
*/

/*
Block:

Block is consist of one or more key/value entries and a block trailer.
Block entry shares key prefix with its preceding key until a restart
point reached. A block should contains at least one restart point.
First restart point are always zero.

Block data structure:

      + restart point                 + restart point (depends on restart interval)
     /                               /
    +---------------+---------------+---------------+---------------+---------+
    | block entry 1 | block entry 2 |      ...      | block entry n | trailer |
    +---------------+---------------+---------------+---------------+---------+

Key/value entry:

              +---- key len ----+
             /                   \
    +-------+---------+-----------+---------+--------------------+--------------+----------------+
    | shared (varint) | not shared (varint) | value len (varint) | key (varlen) | value (varlen) |
    +-----------------+---------------------+--------------------+--------------+----------------+

    Block entry shares key prefix with its preceding key:
    Conditions:
        restart_interval=2
        entry one  : key=deck,value=v1
        entry two  : key=dock,value=v2
        entry three: key=duck,value=v3
    The entries will be encoded as follow:

      + restart point (offset=0)                                                 + restart point (offset=16)
     /                                                                          /
    +-----+-----+-----+----------+--------+-----+-----+-----+---------+--------+-----+-----+-----+----------+--------+
    |  0  |  4  |  2  |  "deck"  |  "v1"  |  1  |  3  |  2  |  "ock"  |  "v2"  |  0  |  4  |  2  |  "duck"  |  "v3"  |
    +-----+-----+-----+----------+--------+-----+-----+-----+---------+--------+-----+-----+-----+----------+--------+
     \                                   / \                                  / \                                   /
      +----------- entry one -----------+   +----------- entry two ----------+   +---------- entry three ----------+

    The block trailer will contains two restart points:

    +------------+-----------+--------+
    |     0      |    16     |   2    |
    +------------+-----------+---+----+
     \                      /     \
      +-- restart points --+       + restart points length

Block trailer:

      +-- 4-bytes --+
     /               \
    +-----------------+-----------------+-----------------+------------------------------+
    | restart point 1 |       ....      | restart point n | restart points len (4-bytes) |
    +-----------------+-----------------+-----------------+------------------------------+


NOTE: All fixed-length integer are little-endian.
*/

/*
Filter block:

Filter block consist of one or more filter data and a filter block trailer.
The trailer contains filter data offsets, a trailer offset and a 1-byte base Lg.

Filter block data structure:

      + offset 1      + offset 2      + offset n      + trailer offset
     /               /               /               /
    +---------------+---------------+---------------+---------+
    | filter data 1 |      ...      | filter data n | trailer |
    +---------------+---------------+---------------+---------+

Filter block trailer:

      +- 4-bytes -+
     /             \
    +---------------+---------------+---------------+-------------------------------+------------------+
    | data 1 offset |      ....     | data n offset | data-offsets offset (4-bytes) | base Lg (1-byte) |
    +-------------- +---------------+---------------+-------------------------------+------------------+


NOTE: All fixed-length integer are little-endian.
*/

const (
	blockTrailerLen = 5
	footerLen       = 48

	magic = "\x57\xfb\x80\x8b\x24\x75\x47\xdb"

	// The block type gives the per-block compression format.
	// These constants are part of the file format and should not be changed.
	blockTypeNoCompression     = 0
	blockTypeSnappyCompression = 1
)

type blockHandle struct {
	offset, length uint64
}

func decodeBlockHandle(src []byte) (blockHandle, int) {
	offset, n := binary.Uvarint(src)
	length, m := binary.Uvarint(src[n:])
	if n == 0 || m == 0 {
		return blockHandle{}, 0
	}
	return blockHandle{offset, length}, n + m
}

func encodeBlockHandle(dst []byte, b blockHandle) int {
	n := binary.PutUvarint(dst, b.offset)
	m := binary.PutUvarint(dst[n:], b.length)
	return n + m
}
```

## File: `leveldb/table/table_suite_test.go`
```go
package table

import (
	"testing"

	"github.com/syndtr/goleveldb/leveldb/testutil"
)

func TestTable(t *testing.T) {
	testutil.RunSuite(t, "Table Suite")
}
```

## File: `leveldb/table/table_test.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package table

import (
	"bytes"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/testutil"
	"github.com/syndtr/goleveldb/leveldb/util"
)

type tableWrapper struct {
	*Reader
}

func (t tableWrapper) TestFind(key []byte) (rkey, rvalue []byte, err error) {
	return t.Reader.Find(key, false, nil)
}

func (t tableWrapper) TestGet(key []byte) (value []byte, err error) {
	return t.Reader.Get(key, nil)
}

func (t tableWrapper) TestNewIterator(slice *util.Range) iterator.Iterator {
	return t.Reader.NewIterator(slice, nil)
}

var _ = testutil.Defer(func() {
	Describe("Table", func() {
		Describe("approximate offset test", func() {
			var (
				buf = &bytes.Buffer{}
				o   = &opt.Options{
					BlockSize:   1024,
					Compression: opt.NoCompression,
				}
			)

			// Building the table.
			tw := NewWriter(buf, o, nil, 0)
			err := tw.Append([]byte("k01"), []byte("hello"))
			Expect(err).ShouldNot(HaveOccurred())
			err = tw.Append([]byte("k02"), []byte("hello2"))
			Expect(err).ShouldNot(HaveOccurred())
			err = tw.Append([]byte("k03"), bytes.Repeat([]byte{'x'}, 10000))
			Expect(err).ShouldNot(HaveOccurred())
			err = tw.Append([]byte("k04"), bytes.Repeat([]byte{'x'}, 200000))
			Expect(err).ShouldNot(HaveOccurred())
			err = tw.Append([]byte("k05"), bytes.Repeat([]byte{'x'}, 300000))
			Expect(err).ShouldNot(HaveOccurred())
			err = tw.Append([]byte("k06"), []byte("hello3"))
			Expect(err).ShouldNot(HaveOccurred())
			err = tw.Append([]byte("k07"), bytes.Repeat([]byte{'x'}, 100000))
			Expect(err).ShouldNot(HaveOccurred())

			err = tw.Close()

			It("Should be able to approximate offset of a key correctly", func() {
				Expect(err).ShouldNot(HaveOccurred())

				tr, err := NewReader(bytes.NewReader(buf.Bytes()), int64(buf.Len()), storage.FileDesc{}, nil, nil, o)
				Expect(err).ShouldNot(HaveOccurred())
				CheckOffset := func(key string, expect, threshold int) {
					offset, err := tr.OffsetOf([]byte(key))
					Expect(err).ShouldNot(HaveOccurred())
					Expect(offset).Should(BeNumerically("~", expect, threshold), "Offset of key %q", key)
				}

				CheckOffset("k0", 0, 0)
				CheckOffset("k01a", 0, 0)
				CheckOffset("k02", 0, 0)
				CheckOffset("k03", 0, 0)
				CheckOffset("k04", 10000, 1000)
				CheckOffset("k04a", 210000, 1000)
				CheckOffset("k05", 210000, 1000)
				CheckOffset("k06", 510000, 1000)
				CheckOffset("k07", 510000, 1000)
				CheckOffset("xyz", 610000, 2000)
			})
		})

		Describe("read test", func() {
			Build := func(kv testutil.KeyValue) testutil.DB {
				o := &opt.Options{
					BlockSize:            512,
					BlockRestartInterval: 3,
				}
				buf := &bytes.Buffer{}

				// Building the table.
				tw := NewWriter(buf, o, nil, 0)
				kv.Iterate(func(i int, key, value []byte) {
					Expect(tw.Append(key, value)).ShouldNot(HaveOccurred())
				})
				tw.Close()

				// Opening the table.
				tr, _ := NewReader(bytes.NewReader(buf.Bytes()), int64(buf.Len()), storage.FileDesc{}, nil, nil, o)
				return tableWrapper{tr}
			}
			Test := func(kv *testutil.KeyValue, body func(r *Reader)) func() {
				return func() {
					db := Build(*kv)
					if body != nil {
						body(db.(tableWrapper).Reader)
					}
					testutil.KeyValueTesting(nil, *kv, db, nil, nil)
				}
			}

			testutil.AllKeyValueTesting(nil, Build, nil, nil)
			Describe("with one key per block", Test(testutil.KeyValue_Generate(nil, 9, 1, 1, 10, 512, 512), func(r *Reader) {
				It("should have correct blocks number", func() {
					indexBlock, err := r.readBlock(r.indexBH, true)
					Expect(err).To(BeNil())
					Expect(indexBlock.restartsLen).Should(Equal(9))
				})
			}))
		})
	})
})
```

## File: `leveldb/table/writer.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package table

import (
	"encoding/binary"
	"errors"
	"fmt"
	"io"

	"github.com/golang/snappy"

	"github.com/syndtr/goleveldb/leveldb/comparer"
	"github.com/syndtr/goleveldb/leveldb/filter"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/util"
)

func sharedPrefixLen(a, b []byte) int {
	i, n := 0, len(a)
	if n > len(b) {
		n = len(b)
	}
	for i < n && a[i] == b[i] {
		i++
	}
	return i
}

type blockWriter struct {
	restartInterval int
	buf             util.Buffer
	nEntries        int
	prevKey         []byte
	restarts        []uint32
	scratch         []byte
}

func (w *blockWriter) append(key, value []byte) (err error) {
	nShared := 0
	if w.nEntries%w.restartInterval == 0 {
		w.restarts = append(w.restarts, uint32(w.buf.Len()))
	} else {
		nShared = sharedPrefixLen(w.prevKey, key)
	}
	n := binary.PutUvarint(w.scratch[0:], uint64(nShared))
	n += binary.PutUvarint(w.scratch[n:], uint64(len(key)-nShared))
	n += binary.PutUvarint(w.scratch[n:], uint64(len(value)))
	if _, err = w.buf.Write(w.scratch[:n]); err != nil {
		return err
	}
	if _, err = w.buf.Write(key[nShared:]); err != nil {
		return err
	}
	if _, err = w.buf.Write(value); err != nil {
		return err
	}
	w.prevKey = append(w.prevKey[:0], key...)
	w.nEntries++
	return nil
}

func (w *blockWriter) finish() error {
	// Write restarts entry.
	if w.nEntries == 0 {
		// Must have at least one restart entry.
		w.restarts = append(w.restarts, 0)
	}
	w.restarts = append(w.restarts, uint32(len(w.restarts)))
	for _, x := range w.restarts {
		buf4 := w.buf.Alloc(4)
		binary.LittleEndian.PutUint32(buf4, x)
	}
	return nil
}

func (w *blockWriter) reset() {
	w.buf.Reset()
	w.nEntries = 0
	w.restarts = w.restarts[:0]
}

func (w *blockWriter) bytesLen() int {
	restartsLen := len(w.restarts)
	if restartsLen == 0 {
		restartsLen = 1
	}
	return w.buf.Len() + 4*restartsLen + 4
}

type filterWriter struct {
	generator filter.FilterGenerator
	buf       util.Buffer
	nKeys     int
	offsets   []uint32
	baseLg    uint
}

func (w *filterWriter) add(key []byte) {
	if w.generator == nil {
		return
	}
	w.generator.Add(key)
	w.nKeys++
}

func (w *filterWriter) flush(offset uint64) {
	if w.generator == nil {
		return
	}
	for x := int(offset / uint64(1<<w.baseLg)); x > len(w.offsets); {
		w.generate()
	}
}

func (w *filterWriter) finish() error {
	if w.generator == nil {
		return nil
	}
	// Generate last keys.

	if w.nKeys > 0 {
		w.generate()
	}
	w.offsets = append(w.offsets, uint32(w.buf.Len()))
	for _, x := range w.offsets {
		buf4 := w.buf.Alloc(4)
		binary.LittleEndian.PutUint32(buf4, x)
	}
	return w.buf.WriteByte(byte(w.baseLg))
}

func (w *filterWriter) generate() {
	// Record offset.
	w.offsets = append(w.offsets, uint32(w.buf.Len()))
	// Generate filters.
	if w.nKeys > 0 {
		w.generator.Generate(&w.buf)
		w.nKeys = 0
	}
}

// Writer is a table writer.
type Writer struct {
	writer io.Writer
	err    error
	// Options
	cmp         comparer.Comparer
	filter      filter.Filter
	compression opt.Compression
	blockSize   int

	bpool       *util.BufferPool
	dataBlock   blockWriter
	indexBlock  blockWriter
	filterBlock filterWriter
	pendingBH   blockHandle
	offset      uint64
	nEntries    int
	// Scratch allocated enough for 5 uvarint. Block writer should not use
	// first 20-bytes since it will be used to encode block handle, which
	// then passed to the block writer itself.
	scratch            [50]byte
	comparerScratch    []byte
	compressionScratch []byte
}

func (w *Writer) writeBlock(buf *util.Buffer, compression opt.Compression) (bh blockHandle, err error) {
	// Compress the buffer if necessary.
	var b []byte
	if compression == opt.SnappyCompression {
		// Allocate scratch enough for compression and block trailer.
		if n := snappy.MaxEncodedLen(buf.Len()) + blockTrailerLen; len(w.compressionScratch) < n {
			w.compressionScratch = make([]byte, n)
		}
		compressed := snappy.Encode(w.compressionScratch, buf.Bytes())
		n := len(compressed)
		b = compressed[:n+blockTrailerLen]
		b[n] = blockTypeSnappyCompression
	} else {
		tmp := buf.Alloc(blockTrailerLen)
		tmp[0] = blockTypeNoCompression
		b = buf.Bytes()
	}

	// Calculate the checksum.
	n := len(b) - 4
	checksum := util.NewCRC(b[:n]).Value()
	binary.LittleEndian.PutUint32(b[n:], checksum)

	// Write the buffer to the file.
	_, err = w.writer.Write(b)
	if err != nil {
		return
	}
	bh = blockHandle{w.offset, uint64(len(b) - blockTrailerLen)}
	w.offset += uint64(len(b))
	return
}

func (w *Writer) flushPendingBH(key []byte) error {
	if w.pendingBH.length == 0 {
		return nil
	}
	var separator []byte
	if len(key) == 0 {
		separator = w.cmp.Successor(w.comparerScratch[:0], w.dataBlock.prevKey)
	} else {
		separator = w.cmp.Separator(w.comparerScratch[:0], w.dataBlock.prevKey, key)
	}
	if separator == nil {
		separator = w.dataBlock.prevKey
	} else {
		w.comparerScratch = separator
	}
	n := encodeBlockHandle(w.scratch[:20], w.pendingBH)
	// Append the block handle to the index block.
	if err := w.indexBlock.append(separator, w.scratch[:n]); err != nil {
		return err
	}
	// Reset prev key of the data block.
	w.dataBlock.prevKey = w.dataBlock.prevKey[:0]
	// Clear pending block handle.
	w.pendingBH = blockHandle{}
	return nil
}

func (w *Writer) finishBlock() error {
	if err := w.dataBlock.finish(); err != nil {
		return err
	}
	bh, err := w.writeBlock(&w.dataBlock.buf, w.compression)
	if err != nil {
		return err
	}
	w.pendingBH = bh
	// Reset the data block.
	w.dataBlock.reset()
	// Flush the filter block.
	w.filterBlock.flush(w.offset)
	return nil
}

// Append appends key/value pair to the table. The keys passed must
// be in increasing order.
//
// It is safe to modify the contents of the arguments after Append returns.
func (w *Writer) Append(key, value []byte) error {
	if w.err != nil {
		return w.err
	}
	if w.nEntries > 0 && w.cmp.Compare(w.dataBlock.prevKey, key) >= 0 {
		w.err = fmt.Errorf("leveldb/table: Writer: keys are not in increasing order: %q, %q", w.dataBlock.prevKey, key)
		return w.err
	}

	if err := w.flushPendingBH(key); err != nil {
		return err
	}
	// Append key/value pair to the data block.
	if err := w.dataBlock.append(key, value); err != nil {
		return err
	}
	// Add key to the filter block.
	w.filterBlock.add(key)

	// Finish the data block if block size target reached.
	if w.dataBlock.bytesLen() >= w.blockSize {
		if err := w.finishBlock(); err != nil {
			w.err = err
			return w.err
		}
	}
	w.nEntries++
	return nil
}

// BlocksLen returns number of blocks written so far.
func (w *Writer) BlocksLen() int {
	n := w.indexBlock.nEntries
	if w.pendingBH.length > 0 {
		// Includes the pending block.
		n++
	}
	return n
}

// EntriesLen returns number of entries added so far.
func (w *Writer) EntriesLen() int {
	return w.nEntries
}

// BytesLen returns number of bytes written so far.
func (w *Writer) BytesLen() int {
	return int(w.offset)
}

// Close will finalize the table. Calling Append is not possible
// after Close, but calling BlocksLen, EntriesLen and BytesLen
// is still possible.
func (w *Writer) Close() error {
	defer func() {
		if w.bpool != nil {
			// Buffer.Bytes() returns [offset:] of the buffer.
			// We need to Reset() so that the offset = 0, resulting
			// in buf.Bytes() returning the whole allocated bytes.
			w.dataBlock.buf.Reset()
			w.bpool.Put(w.dataBlock.buf.Bytes())
		}
	}()

	if w.err != nil {
		return w.err
	}

	// Write the last data block. Or empty data block if there
	// aren't any data blocks at all.
	if w.dataBlock.nEntries > 0 || w.nEntries == 0 {
		if err := w.finishBlock(); err != nil {
			w.err = err
			return w.err
		}
	}
	if err := w.flushPendingBH(nil); err != nil {
		return err
	}

	// Write the filter block.
	var filterBH blockHandle
	if err := w.filterBlock.finish(); err != nil {
		return err
	}
	if buf := &w.filterBlock.buf; buf.Len() > 0 {
		filterBH, w.err = w.writeBlock(buf, opt.NoCompression)
		if w.err != nil {
			return w.err
		}
	}

	// Write the metaindex block.
	if filterBH.length > 0 {
		key := []byte("filter." + w.filter.Name())
		n := encodeBlockHandle(w.scratch[:20], filterBH)
		if err := w.dataBlock.append(key, w.scratch[:n]); err != nil {
			return err
		}
	}
	if err := w.dataBlock.finish(); err != nil {
		return err
	}
	metaindexBH, err := w.writeBlock(&w.dataBlock.buf, w.compression)
	if err != nil {
		w.err = err
		return w.err
	}

	// Write the index block.
	if err := w.indexBlock.finish(); err != nil {
		return err
	}
	indexBH, err := w.writeBlock(&w.indexBlock.buf, w.compression)
	if err != nil {
		w.err = err
		return w.err
	}

	// Write the table footer.
	footer := w.scratch[:footerLen]
	for i := range footer {
		footer[i] = 0
	}
	n := encodeBlockHandle(footer, metaindexBH)
	encodeBlockHandle(footer[n:], indexBH)
	copy(footer[footerLen-len(magic):], magic)
	if _, err := w.writer.Write(footer); err != nil {
		w.err = err
		return w.err
	}
	w.offset += footerLen

	w.err = errors.New("leveldb/table: writer is closed")
	return nil
}

// NewWriter creates a new initialized table writer for the file.
//
// Table writer is not safe for concurrent use.
func NewWriter(f io.Writer, o *opt.Options, pool *util.BufferPool, size int) *Writer {
	var bufBytes []byte
	if pool == nil {
		bufBytes = make([]byte, size)
	} else {
		bufBytes = pool.Get(size)
	}
	bufBytes = bufBytes[:0]

	w := &Writer{
		writer:          f,
		cmp:             o.GetComparer(),
		filter:          o.GetFilter(),
		compression:     o.GetCompression(),
		blockSize:       o.GetBlockSize(),
		comparerScratch: make([]byte, 0),
		bpool:           pool,
		dataBlock:       blockWriter{buf: *util.NewBuffer(bufBytes)},
	}
	// data block
	w.dataBlock.restartInterval = o.GetBlockRestartInterval()
	// The first 20-bytes are used for encoding block handle.
	w.dataBlock.scratch = w.scratch[20:]
	// index block
	w.indexBlock.restartInterval = 1
	w.indexBlock.scratch = w.scratch[20:]
	// filter block
	if w.filter != nil {
		w.filterBlock.generator = w.filter.NewGenerator()
		w.filterBlock.baseLg = uint(o.GetFilterBaseLg())
		w.filterBlock.flush(0)
	}
	return w
}
```

## File: `leveldb/testutil/db.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package testutil

import (
	"fmt"
	"math/rand"

	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/iterator"
	"github.com/syndtr/goleveldb/leveldb/util"
)

type DB interface{}

type Put interface {
	TestPut(key []byte, value []byte) error
}

type Delete interface {
	TestDelete(key []byte) error
}

type Find interface {
	TestFind(key []byte) (rkey, rvalue []byte, err error)
}

type Get interface {
	TestGet(key []byte) (value []byte, err error)
}

type Has interface {
	TestHas(key []byte) (ret bool, err error)
}

type NewIterator interface {
	TestNewIterator(slice *util.Range) iterator.Iterator
}

type DBAct int

func (a DBAct) String() string {
	switch a {
	case DBNone:
		return "none"
	case DBPut:
		return "put"
	case DBOverwrite:
		return "overwrite"
	case DBDelete:
		return "delete"
	case DBDeleteNA:
		return "delete_na"
	}
	return "unknown"
}

const (
	DBNone DBAct = iota
	DBPut
	DBOverwrite
	DBDelete
	DBDeleteNA
)

type DBTesting struct {
	Rand *rand.Rand
	DB   interface {
		Get
		Put
		Delete
	}
	PostFn             func(t *DBTesting)
	Deleted, Present   KeyValue
	Act, LastAct       DBAct
	ActKey, LastActKey []byte
}

func (t *DBTesting) post() {
	if t.PostFn != nil {
		t.PostFn(t)
	}
}

func (t *DBTesting) setAct(act DBAct, key []byte) {
	t.LastAct, t.Act = t.Act, act
	t.LastActKey, t.ActKey = t.ActKey, key
}

func (t *DBTesting) text() string {
	return fmt.Sprintf("last action was <%v> %q, <%v> %q", t.LastAct, t.LastActKey, t.Act, t.ActKey)
}

func (t *DBTesting) Text() string {
	return "DBTesting " + t.text()
}

func (t *DBTesting) TestPresentKV(key, value []byte) {
	rvalue, err := t.DB.TestGet(key)
	Expect(err).ShouldNot(HaveOccurred(), "Get on key %q, %s", key, t.text())
	Expect(rvalue).Should(Equal(value), "Value for key %q, %s", key, t.text())
}

func (t *DBTesting) TestAllPresent() {
	t.Present.IterateShuffled(t.Rand, func(i int, key, value []byte) {
		t.TestPresentKV(key, value)
	})
}

func (t *DBTesting) TestDeletedKey(key []byte) {
	_, err := t.DB.TestGet(key)
	Expect(err).Should(Equal(errors.ErrNotFound), "Get on deleted key %q, %s", key, t.text())
}

func (t *DBTesting) TestAllDeleted() {
	t.Deleted.IterateShuffled(t.Rand, func(i int, key, value []byte) {
		t.TestDeletedKey(key)
	})
}

func (t *DBTesting) TestAll() {
	dn := t.Deleted.Len()
	pn := t.Present.Len()
	ShuffledIndex(t.Rand, dn+pn, 1, func(i int) {
		if i >= dn {
			key, value := t.Present.Index(i - dn)
			t.TestPresentKV(key, value)
		} else {
			t.TestDeletedKey(t.Deleted.KeyAt(i))
		}
	})
}

func (t *DBTesting) Put(key, value []byte) {
	if new := t.Present.PutU(key, value); new {
		t.setAct(DBPut, key)
	} else {
		t.setAct(DBOverwrite, key)
	}
	t.Deleted.Delete(key)
	err := t.DB.TestPut(key, value)
	Expect(err).ShouldNot(HaveOccurred(), t.Text())
	t.TestPresentKV(key, value)
	t.post()
}

func (t *DBTesting) PutRandom() bool {
	if t.Deleted.Len() > 0 {
		i := t.Rand.Intn(t.Deleted.Len())
		key, value := t.Deleted.Index(i)
		t.Put(key, value)
		return true
	}
	return false
}

func (t *DBTesting) Delete(key []byte) {
	if exist, value := t.Present.Delete(key); exist {
		t.setAct(DBDelete, key)
		t.Deleted.PutU(key, value)
	} else {
		t.setAct(DBDeleteNA, key)
	}
	err := t.DB.TestDelete(key)
	Expect(err).ShouldNot(HaveOccurred(), t.Text())
	t.TestDeletedKey(key)
	t.post()
}

func (t *DBTesting) DeleteRandom() bool {
	if t.Present.Len() > 0 {
		i := t.Rand.Intn(t.Present.Len())
		t.Delete(t.Present.KeyAt(i))
		return true
	}
	return false
}

func (t *DBTesting) RandomAct(round int) {
	for i := 0; i < round; i++ {
		if t.Rand.Int()%2 == 0 {
			t.PutRandom()
		} else {
			t.DeleteRandom()
		}
	}
}

func DoDBTesting(t *DBTesting) {
	if t.Rand == nil {
		t.Rand = NewRand()
	}

	t.DeleteRandom()
	t.PutRandom()
	t.DeleteRandom()
	t.DeleteRandom()
	for i := t.Deleted.Len() / 2; i >= 0; i-- {
		t.PutRandom()
	}
	t.RandomAct((t.Deleted.Len() + t.Present.Len()) * 10)

	// Additional iterator testing
	if db, ok := t.DB.(NewIterator); ok {
		iter := db.TestNewIterator(nil)
		Expect(iter.Error()).NotTo(HaveOccurred())

		it := IteratorTesting{
			KeyValue: t.Present,
			Iter:     iter,
		}

		DoIteratorTesting(&it)
		iter.Release()
	}
}
```

## File: `leveldb/testutil/ginkgo.go`
```go
package testutil

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func RunSuite(t GinkgoTestingT, name string) {
	RunDefer()

	SynchronizedBeforeSuite(func() []byte {
		RunDefer("setup")
		return nil
	}, func(data []byte) {})
	SynchronizedAfterSuite(func() {
		RunDefer("teardown")
	}, func() {})

	RegisterFailHandler(Fail)
	RunSpecs(t, name)
}
```

## File: `leveldb/testutil/iter.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package testutil

import (
	"fmt"
	"math/rand"

	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/iterator"
)

type IterAct int

func (a IterAct) String() string {
	switch a {
	case IterNone:
		return "none"
	case IterFirst:
		return "first"
	case IterLast:
		return "last"
	case IterPrev:
		return "prev"
	case IterNext:
		return "next"
	case IterSeek:
		return "seek"
	case IterSOI:
		return "soi"
	case IterEOI:
		return "eoi"
	}
	return "unknown"
}

const (
	IterNone IterAct = iota
	IterFirst
	IterLast
	IterPrev
	IterNext
	IterSeek
	IterSOI
	IterEOI
)

type IteratorTesting struct {
	KeyValue
	Iter         iterator.Iterator
	Rand         *rand.Rand
	PostFn       func(t *IteratorTesting)
	Pos          int
	Act, LastAct IterAct

	once bool
}

func (t *IteratorTesting) init() {
	if !t.once {
		t.Pos = -1
		t.once = true
	}
}

func (t *IteratorTesting) post() {
	if t.PostFn != nil {
		t.PostFn(t)
	}
}

func (t *IteratorTesting) setAct(act IterAct) {
	t.LastAct, t.Act = t.Act, act
}

func (t *IteratorTesting) text() string {
	return fmt.Sprintf("at pos %d and last action was <%v> -> <%v>", t.Pos, t.LastAct, t.Act)
}

func (t *IteratorTesting) Text() string {
	return "IteratorTesting is " + t.text()
}

func (t *IteratorTesting) IsFirst() bool {
	t.init()
	return t.Len() > 0 && t.Pos == 0
}

func (t *IteratorTesting) IsLast() bool {
	t.init()
	return t.Len() > 0 && t.Pos == t.Len()-1
}

func (t *IteratorTesting) TestKV() {
	t.init()
	key, value := t.Index(t.Pos)
	Expect(t.Iter.Key()).NotTo(BeNil())
	Expect(t.Iter.Key()).Should(Equal(key), "Key is invalid, %s", t.text())
	Expect(t.Iter.Value()).Should(Equal(value), "Value for key %q, %s", key, t.text())
}

func (t *IteratorTesting) First() {
	t.init()
	t.setAct(IterFirst)

	ok := t.Iter.First()
	Expect(t.Iter.Error()).ShouldNot(HaveOccurred())
	if t.Len() > 0 {
		t.Pos = 0
		Expect(ok).Should(BeTrue(), t.Text())
		t.TestKV()
	} else {
		t.Pos = -1
		Expect(ok).ShouldNot(BeTrue(), t.Text())
	}
	t.post()
}

func (t *IteratorTesting) Last() {
	t.init()
	t.setAct(IterLast)

	ok := t.Iter.Last()
	Expect(t.Iter.Error()).ShouldNot(HaveOccurred())
	if t.Len() > 0 {
		t.Pos = t.Len() - 1
		Expect(ok).Should(BeTrue(), t.Text())
		t.TestKV()
	} else {
		t.Pos = 0
		Expect(ok).ShouldNot(BeTrue(), t.Text())
	}
	t.post()
}

func (t *IteratorTesting) Next() {
	t.init()
	t.setAct(IterNext)

	ok := t.Iter.Next()
	Expect(t.Iter.Error()).ShouldNot(HaveOccurred())
	if t.Pos < t.Len()-1 {
		t.Pos++
		Expect(ok).Should(BeTrue(), t.Text())
		t.TestKV()
	} else {
		t.Pos = t.Len()
		Expect(ok).ShouldNot(BeTrue(), t.Text())
	}
	t.post()
}

func (t *IteratorTesting) Prev() {
	t.init()
	t.setAct(IterPrev)

	ok := t.Iter.Prev()
	Expect(t.Iter.Error()).ShouldNot(HaveOccurred())
	if t.Pos > 0 {
		t.Pos--
		Expect(ok).Should(BeTrue(), t.Text())
		t.TestKV()
	} else {
		t.Pos = -1
		Expect(ok).ShouldNot(BeTrue(), t.Text())
	}
	t.post()
}

func (t *IteratorTesting) Seek(i int) {
	t.init()
	t.setAct(IterSeek)

	key, _ := t.Index(i)
	oldKey, _ := t.IndexOrNil(t.Pos)

	ok := t.Iter.Seek(key)
	Expect(t.Iter.Error()).ShouldNot(HaveOccurred())
	Expect(ok).Should(BeTrue(), fmt.Sprintf("Seek from key %q to %q, to pos %d, %s", oldKey, key, i, t.text()))

	t.Pos = i
	t.TestKV()
	t.post()
}

func (t *IteratorTesting) SeekInexact(i int) {
	t.init()
	t.setAct(IterSeek)
	var key0 []byte
	key1, _ := t.Index(i)
	if i > 0 {
		key0, _ = t.Index(i - 1)
	}
	key := BytesSeparator(key0, key1)
	oldKey, _ := t.IndexOrNil(t.Pos)

	ok := t.Iter.Seek(key)
	Expect(t.Iter.Error()).ShouldNot(HaveOccurred())
	Expect(ok).Should(BeTrue(), fmt.Sprintf("Seek from key %q to %q (%q), to pos %d, %s", oldKey, key, key1, i, t.text()))

	t.Pos = i
	t.TestKV()
	t.post()
}

func (t *IteratorTesting) SeekKey(key []byte) {
	t.init()
	t.setAct(IterSeek)
	oldKey, _ := t.IndexOrNil(t.Pos)
	i := t.Search(key)

	ok := t.Iter.Seek(key)
	Expect(t.Iter.Error()).ShouldNot(HaveOccurred())
	if i < t.Len() {
		key_, _ := t.Index(i)
		Expect(ok).Should(BeTrue(), fmt.Sprintf("Seek from key %q to %q (%q), to pos %d, %s", oldKey, key, key_, i, t.text()))
		t.Pos = i
		t.TestKV()
	} else {
		Expect(ok).ShouldNot(BeTrue(), fmt.Sprintf("Seek from key %q to %q, %s", oldKey, key, t.text()))
	}

	t.Pos = i
	t.post()
}

func (t *IteratorTesting) SOI() {
	t.init()
	t.setAct(IterSOI)
	Expect(t.Pos).Should(BeNumerically("<=", 0), t.Text())
	for i := 0; i < 3; i++ {
		t.Prev()
	}
	t.post()
}

func (t *IteratorTesting) EOI() {
	t.init()
	t.setAct(IterEOI)
	Expect(t.Pos).Should(BeNumerically(">=", t.Len()-1), t.Text())
	for i := 0; i < 3; i++ {
		t.Next()
	}
	t.post()
}

func (t *IteratorTesting) WalkPrev(fn func(t *IteratorTesting)) {
	t.init()
	for old := t.Pos; t.Pos > 0; old = t.Pos {
		fn(t)
		Expect(t.Pos).Should(BeNumerically("<", old), t.Text())
	}
}

func (t *IteratorTesting) WalkNext(fn func(t *IteratorTesting)) {
	t.init()
	for old := t.Pos; t.Pos < t.Len()-1; old = t.Pos {
		fn(t)
		Expect(t.Pos).Should(BeNumerically(">", old), t.Text())
	}
}

func (t *IteratorTesting) PrevAll() {
	t.WalkPrev(func(t *IteratorTesting) {
		t.Prev()
	})
}

func (t *IteratorTesting) NextAll() {
	t.WalkNext(func(t *IteratorTesting) {
		t.Next()
	})
}

func DoIteratorTesting(t *IteratorTesting) {
	if t.Rand == nil {
		t.Rand = NewRand()
	}
	t.SOI()
	t.NextAll()
	t.First()
	t.SOI()
	t.NextAll()
	t.EOI()
	t.PrevAll()
	t.Last()
	t.EOI()
	t.PrevAll()
	t.SOI()

	t.NextAll()
	t.PrevAll()
	t.NextAll()
	t.Last()
	t.PrevAll()
	t.First()
	t.NextAll()
	t.EOI()

	ShuffledIndex(t.Rand, t.Len(), 1, func(i int) {
		t.Seek(i)
	})

	ShuffledIndex(t.Rand, t.Len(), 1, func(i int) {
		t.SeekInexact(i)
	})

	ShuffledIndex(t.Rand, t.Len(), 1, func(i int) {
		t.Seek(i)
		if i%2 != 0 {
			t.PrevAll()
			t.SOI()
		} else {
			t.NextAll()
			t.EOI()
		}
	})

	for _, key := range []string{"", "foo", "bar", "\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"} {
		t.SeekKey([]byte(key))
	}
}
```

## File: `leveldb/testutil/kv.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package testutil

import (
	"fmt"
	"math/rand"
	"sort"
	"strings"

	"github.com/syndtr/goleveldb/leveldb/util"
)

type KeyValueEntry struct {
	key, value []byte
}

type KeyValue struct {
	entries []KeyValueEntry
	nbytes  int
}

func (kv *KeyValue) Put(key, value []byte) {
	if n := len(kv.entries); n > 0 && cmp.Compare(kv.entries[n-1].key, key) >= 0 {
		panic(fmt.Sprintf("Put: keys are not in increasing order: %q, %q", kv.entries[n-1].key, key))
	}
	kv.entries = append(kv.entries, KeyValueEntry{key, value})
	kv.nbytes += len(key) + len(value)
}

func (kv *KeyValue) PutString(key, value string) {
	kv.Put([]byte(key), []byte(value))
}

func (kv *KeyValue) PutU(key, value []byte) bool {
	if i, exist := kv.Get(key); !exist {
		if i < kv.Len() {
			kv.entries = append(kv.entries[:i+1], kv.entries[i:]...)
			kv.entries[i] = KeyValueEntry{key, value}
		} else {
			kv.entries = append(kv.entries, KeyValueEntry{key, value})
		}
		kv.nbytes += len(key) + len(value)
		return true
	} else {
		kv.nbytes += len(value) - len(kv.ValueAt(i))
		kv.entries[i].value = value
	}
	return false
}

func (kv *KeyValue) PutUString(key, value string) bool {
	return kv.PutU([]byte(key), []byte(value))
}

func (kv *KeyValue) Delete(key []byte) (exist bool, value []byte) {
	i, exist := kv.Get(key)
	if exist {
		value = kv.entries[i].value
		kv.DeleteIndex(i)
	}
	return
}

func (kv *KeyValue) DeleteIndex(i int) bool {
	if i < kv.Len() {
		kv.nbytes -= len(kv.KeyAt(i)) + len(kv.ValueAt(i))
		kv.entries = append(kv.entries[:i], kv.entries[i+1:]...)
		return true
	}
	return false
}

func (kv KeyValue) Len() int {
	return len(kv.entries)
}

func (kv *KeyValue) Size() int {
	return kv.nbytes
}

func (kv KeyValue) KeyAt(i int) []byte {
	return kv.entries[i].key
}

func (kv KeyValue) ValueAt(i int) []byte {
	return kv.entries[i].value
}

func (kv KeyValue) Index(i int) (key, value []byte) {
	if i < 0 || i >= len(kv.entries) {
		panic(fmt.Sprintf("Index #%d: out of range", i))
	}
	return kv.entries[i].key, kv.entries[i].value
}

func (kv KeyValue) IndexInexact(i int) (key_, key, value []byte) {
	key, value = kv.Index(i)
	var key0 []byte
	var key1 = kv.KeyAt(i)
	if i > 0 {
		key0 = kv.KeyAt(i - 1)
	}
	key_ = BytesSeparator(key0, key1)
	return
}

func (kv KeyValue) IndexOrNil(i int) (key, value []byte) {
	if i >= 0 && i < len(kv.entries) {
		return kv.entries[i].key, kv.entries[i].value
	}
	return nil, nil
}

func (kv KeyValue) IndexString(i int) (key, value string) {
	key_, _value := kv.Index(i)
	return string(key_), string(_value)
}

func (kv KeyValue) Search(key []byte) int {
	return sort.Search(kv.Len(), func(i int) bool {
		return cmp.Compare(kv.KeyAt(i), key) >= 0
	})
}

func (kv KeyValue) SearchString(key string) int {
	return kv.Search([]byte(key))
}

func (kv KeyValue) Get(key []byte) (i int, exist bool) {
	i = kv.Search(key)
	if i < kv.Len() && cmp.Compare(kv.KeyAt(i), key) == 0 {
		exist = true
	}
	return
}

func (kv KeyValue) GetString(key string) (i int, exist bool) {
	return kv.Get([]byte(key))
}

func (kv KeyValue) Iterate(fn func(i int, key, value []byte)) {
	for i, x := range kv.entries {
		fn(i, x.key, x.value)
	}
}

func (kv KeyValue) IterateString(fn func(i int, key, value string)) {
	kv.Iterate(func(i int, key, value []byte) {
		fn(i, string(key), string(value))
	})
}

func (kv KeyValue) IterateShuffled(rnd *rand.Rand, fn func(i int, key, value []byte)) {
	ShuffledIndex(rnd, kv.Len(), 1, func(i int) {
		fn(i, kv.entries[i].key, kv.entries[i].value)
	})
}

func (kv KeyValue) IterateShuffledString(rnd *rand.Rand, fn func(i int, key, value string)) {
	kv.IterateShuffled(rnd, func(i int, key, value []byte) {
		fn(i, string(key), string(value))
	})
}

func (kv KeyValue) IterateInexact(fn func(i int, key_, key, value []byte)) {
	for i := range kv.entries {
		key_, key, value := kv.IndexInexact(i)
		fn(i, key_, key, value)
	}
}

func (kv KeyValue) IterateInexactString(fn func(i int, key_, key, value string)) {
	kv.IterateInexact(func(i int, key_, key, value []byte) {
		fn(i, string(key_), string(key), string(value))
	})
}

func (kv KeyValue) Clone() KeyValue {
	return KeyValue{append([]KeyValueEntry{}, kv.entries...), kv.nbytes}
}

func (kv KeyValue) Slice(start, limit int) KeyValue {
	if start < 0 || limit > kv.Len() {
		panic(fmt.Sprintf("Slice %d .. %d: out of range", start, limit))
	} else if limit < start {
		panic(fmt.Sprintf("Slice %d .. %d: invalid range", start, limit))
	}
	return KeyValue{append([]KeyValueEntry{}, kv.entries[start:limit]...), kv.nbytes}
}

func (kv KeyValue) SliceKey(start, limit []byte) KeyValue {
	start_ := 0
	limit_ := kv.Len()
	if start != nil {
		start_ = kv.Search(start)
	}
	if limit != nil {
		limit_ = kv.Search(limit)
	}
	return kv.Slice(start_, limit_)
}

func (kv KeyValue) SliceKeyString(start, limit string) KeyValue {
	return kv.SliceKey([]byte(start), []byte(limit))
}

func (kv KeyValue) SliceRange(r *util.Range) KeyValue {
	if r != nil {
		return kv.SliceKey(r.Start, r.Limit)
	}
	return kv.Clone()
}

func (kv KeyValue) Range(start, limit int) (r util.Range) {
	if kv.Len() > 0 {
		if start == kv.Len() {
			r.Start = BytesAfter(kv.KeyAt(start - 1))
		} else {
			r.Start = kv.KeyAt(start)
		}
	}
	if limit < kv.Len() {
		r.Limit = kv.KeyAt(limit)
	}
	return
}

func KeyValue_EmptyKey() *KeyValue {
	kv := &KeyValue{}
	kv.PutString("", "v")
	return kv
}

func KeyValue_EmptyValue() *KeyValue {
	kv := &KeyValue{}
	kv.PutString("abc", "")
	kv.PutString("abcd", "")
	return kv
}

func KeyValue_OneKeyValue() *KeyValue {
	kv := &KeyValue{}
	kv.PutString("abc", "v")
	return kv
}

func KeyValue_BigValue() *KeyValue {
	kv := &KeyValue{}
	kv.PutString("big1", strings.Repeat("1", 200000))
	return kv
}

func KeyValue_SpecialKey() *KeyValue {
	kv := &KeyValue{}
	kv.PutString("\xff\xff", "v3")
	return kv
}

func KeyValue_MultipleKeyValue() *KeyValue {
	kv := &KeyValue{}
	kv.PutString("a", "v")
	kv.PutString("aa", "v1")
	kv.PutString("aaa", "v2")
	kv.PutString("aaacccccccccc", "v2")
	kv.PutString("aaaccccccccccd", "v3")
	kv.PutString("aaaccccccccccf", "v4")
	kv.PutString("aaaccccccccccfg", "v5")
	kv.PutString("ab", "v6")
	kv.PutString("abc", "v7")
	kv.PutString("abcd", "v8")
	kv.PutString("accccccccccccccc", "v9")
	kv.PutString("b", "v10")
	kv.PutString("bb", "v11")
	kv.PutString("bc", "v12")
	kv.PutString("c", "v13")
	kv.PutString("c1", "v13")
	kv.PutString("czzzzzzzzzzzzzz", "v14")
	kv.PutString("fffffffffffffff", "v15")
	kv.PutString("g11", "v15")
	kv.PutString("g111", "v15")
	kv.PutString("g111\xff", "v15")
	kv.PutString("zz", "v16")
	kv.PutString("zzzzzzz", "v16")
	kv.PutString("zzzzzzzzzzzzzzzz", "v16")
	return kv
}

var keymap = []byte("012345678ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxy")

func KeyValue_Generate(rnd *rand.Rand, n, incr, minlen, maxlen, vminlen, vmaxlen int) *KeyValue {
	if rnd == nil {
		rnd = NewRand()
	}
	if maxlen < minlen {
		panic("max len should >= min len")
	}

	rrand := func(min, max int) int {
		if min == max {
			return max
		}
		return rnd.Intn(max-min) + min
	}

	kv := &KeyValue{}
	endC := byte(len(keymap) - incr)
	gen := make([]byte, 0, maxlen)
	for i := 0; i < n; i++ {
		m := rrand(minlen, maxlen)
		last := gen
	retry:
		gen = last[:m]
		if k := len(last); m > k {
			for j := k; j < m; j++ {
				gen[j] = 0
			}
		} else {
			for j := m - 1; j >= 0; j-- {
				c := last[j]
				if c == endC {
					continue
				}
				gen[j] = c + byte(incr)
				for j++; j < m; j++ {
					gen[j] = 0
				}
				goto ok
			}
			if m < maxlen {
				m++
				goto retry
			}
			panic(fmt.Sprintf("only able to generate %d keys out of %d keys, try increasing max len", kv.Len(), n))
		ok:
		}
		key := make([]byte, m)
		for j := 0; j < m; j++ {
			key[j] = keymap[gen[j]]
		}
		value := make([]byte, rrand(vminlen, vmaxlen))
		for n := copy(value, fmt.Sprintf("v%d", i)); n < len(value); n++ {
			value[n] = 'x'
		}
		kv.Put(key, value)
	}
	return kv
}
```

## File: `leveldb/testutil/kvtest.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package testutil

import (
	"fmt"
	"math/rand"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/util"
)

func TestFind(db Find, kv KeyValue) {
	ShuffledIndex(nil, kv.Len(), 1, func(i int) {
		key_, key, value := kv.IndexInexact(i)

		// Using exact key.
		rkey, rvalue, err := db.TestFind(key)
		Expect(err).ShouldNot(HaveOccurred(), "Error for exact key %q", key)
		Expect(rkey).Should(Equal(key), "Key")
		Expect(rvalue).Should(Equal(value), "Value for exact key %q", key)

		// Using inexact key.
		rkey, rvalue, err = db.TestFind(key_)
		Expect(err).ShouldNot(HaveOccurred(), "Error for inexact key %q (%q)", key_, key)
		Expect(rkey).Should(Equal(key), "Key for inexact key %q (%q)", key_, key)
		Expect(rvalue).Should(Equal(value), "Value for inexact key %q (%q)", key_, key)
	})
}

func TestFindAfterLast(db Find, kv KeyValue) {
	var key []byte
	if kv.Len() > 0 {
		key_, _ := kv.Index(kv.Len() - 1)
		key = BytesAfter(key_)
	}
	rkey, _, err := db.TestFind(key)
	Expect(err).Should(HaveOccurred(), "Find for key %q yield key %q", key, rkey)
	Expect(err).Should(Equal(errors.ErrNotFound))
}

func TestGet(db Get, kv KeyValue) {
	ShuffledIndex(nil, kv.Len(), 1, func(i int) {
		key_, key, value := kv.IndexInexact(i)

		// Using exact key.
		rvalue, err := db.TestGet(key)
		Expect(err).ShouldNot(HaveOccurred(), "Error for key %q", key)
		Expect(rvalue).Should(Equal(value), "Value for key %q", key)

		// Using inexact key.
		if len(key_) > 0 {
			_, err = db.TestGet(key_)
			Expect(err).Should(HaveOccurred(), "Error for key %q", key_)
			Expect(err).Should(Equal(errors.ErrNotFound))
		}
	})
}

func TestHas(db Has, kv KeyValue) {
	ShuffledIndex(nil, kv.Len(), 1, func(i int) {
		key_, key, _ := kv.IndexInexact(i)

		// Using exact key.
		ret, err := db.TestHas(key)
		Expect(err).ShouldNot(HaveOccurred(), "Error for key %q", key)
		Expect(ret).Should(BeTrue(), "False for key %q", key)

		// Using inexact key.
		if len(key_) > 0 {
			ret, err = db.TestHas(key_)
			Expect(err).ShouldNot(HaveOccurred(), "Error for key %q", key_)
			Expect(ret).ShouldNot(BeTrue(), "True for key %q", key)
		}
	})
}

func TestIter(db NewIterator, r *util.Range, kv KeyValue) {
	iter := db.TestNewIterator(r)
	Expect(iter.Error()).ShouldNot(HaveOccurred())

	t := IteratorTesting{
		KeyValue: kv,
		Iter:     iter,
	}

	DoIteratorTesting(&t)
	iter.Release()
}

func KeyValueTesting(rnd *rand.Rand, kv KeyValue, p DB, setup func(KeyValue) DB, teardown func(DB)) {
	if rnd == nil {
		rnd = NewRand()
	}

	if p == nil {
		BeforeEach(func() {
			p = setup(kv)
		})
		if teardown != nil {
			AfterEach(func() {
				teardown(p)
			})
		}
	}

	It("Should find all keys with Find", func() {
		if db, ok := p.(Find); ok {
			TestFind(db, kv)
		}
	})

	It("Should return error if Find on key after the last", func() {
		if db, ok := p.(Find); ok {
			TestFindAfterLast(db, kv)
		}
	})

	It("Should only find exact key with Get", func() {
		if db, ok := p.(Get); ok {
			TestGet(db, kv)
		}
	})

	It("Should only find present key with Has", func() {
		if db, ok := p.(Has); ok {
			TestHas(db, kv)
		}
	})

	It("Should iterates and seeks correctly", func(done Done) {
		if db, ok := p.(NewIterator); ok {
			TestIter(db, nil, kv.Clone())
		}
		done <- true
	}, 30.0)

	It("Should iterates and seeks slice correctly", func(done Done) {
		if db, ok := p.(NewIterator); ok {
			RandomIndex(rnd, kv.Len(), Min(kv.Len(), 50), func(i int) {
				type slice struct {
					r            *util.Range
					start, limit int
				}

				key_, _, _ := kv.IndexInexact(i)
				for _, x := range []slice{
					{&util.Range{Start: key_, Limit: nil}, i, kv.Len()},
					{&util.Range{Start: nil, Limit: key_}, 0, i},
				} {
					By(fmt.Sprintf("Random index of %d .. %d", x.start, x.limit), func() {
						TestIter(db, x.r, kv.Slice(x.start, x.limit))
					})
				}
			})
		}
		done <- true
	}, 200.0)

	It("Should iterates and seeks slice correctly", func(done Done) {
		if db, ok := p.(NewIterator); ok {
			RandomRange(rnd, kv.Len(), Min(kv.Len(), 50), func(start, limit int) {
				By(fmt.Sprintf("Random range of %d .. %d", start, limit), func() {
					r := kv.Range(start, limit)
					TestIter(db, &r, kv.Slice(start, limit))
				})
			})
		}
		done <- true
	}, 200.0)
}

func AllKeyValueTesting(rnd *rand.Rand, body, setup func(KeyValue) DB, teardown func(DB)) {
	Test := func(kv *KeyValue) func() {
		return func() {
			var p DB
			if setup != nil {
				Defer("setup", func() {
					p = setup(*kv)
				})
			}
			if teardown != nil {
				Defer("teardown", func() {
					teardown(p)
				})
			}
			if body != nil {
				p = body(*kv)
			}
			KeyValueTesting(rnd, *kv, p, func(KeyValue) DB {
				return p
			}, nil)
		}
	}

	Describe("with no key/value (empty)", Test(&KeyValue{}))
	Describe("with empty key", Test(KeyValue_EmptyKey()))
	Describe("with empty value", Test(KeyValue_EmptyValue()))
	Describe("with one key/value", Test(KeyValue_OneKeyValue()))
	Describe("with big value", Test(KeyValue_BigValue()))
	Describe("with special key", Test(KeyValue_SpecialKey()))
	Describe("with multiple key/value", Test(KeyValue_MultipleKeyValue()))
	Describe("with generated key/value 2-incr", Test(KeyValue_Generate(nil, 120, 2, 1, 50, 10, 120)))
	Describe("with generated key/value 3-incr", Test(KeyValue_Generate(nil, 120, 3, 1, 50, 10, 120)))
}
```

## File: `leveldb/testutil/storage.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package testutil

import (
	"bytes"
	"fmt"
	"io"
	"math/rand"
	"os"
	"path/filepath"
	"runtime"
	"strings"
	"sync"

	. "github.com/onsi/gomega"

	"github.com/syndtr/goleveldb/leveldb/storage"
)

var (
	storageMu     sync.Mutex
	storageUseFS  = true
	storageKeepFS = false
	storageNum    int
)

type StorageMode int

const (
	ModeOpen StorageMode = 1 << iota
	ModeCreate
	ModeRemove
	ModeRename
	ModeRead
	ModeWrite
	ModeSync
	ModeClose
)

const (
	modeOpen = iota
	modeCreate
	modeRemove
	modeRename
	modeRead
	modeWrite
	modeSync
	modeClose

	modeCount
)

const (
	typeManifest = iota
	typeJournal
	typeTable
	typeTemp

	typeCount
)

const flattenCount = modeCount * typeCount

func flattenType(m StorageMode, t storage.FileType) int {
	var x int
	switch m {
	case ModeOpen:
		x = modeOpen
	case ModeCreate:
		x = modeCreate
	case ModeRemove:
		x = modeRemove
	case ModeRename:
		x = modeRename
	case ModeRead:
		x = modeRead
	case ModeWrite:
		x = modeWrite
	case ModeSync:
		x = modeSync
	case ModeClose:
		x = modeClose
	default:
		panic("invalid storage mode")
	}
	x *= typeCount
	switch t {
	case storage.TypeManifest:
		return x + typeManifest
	case storage.TypeJournal:
		return x + typeJournal
	case storage.TypeTable:
		return x + typeTable
	case storage.TypeTemp:
		return x + typeTemp
	default:
		panic("invalid file type")
	}
}

func listFlattenType(m StorageMode, t storage.FileType) []int {
	ret := make([]int, 0, flattenCount)
	add := func(x int) {
		x *= typeCount
		switch {
		case t&storage.TypeManifest != 0:
			ret = append(ret, x+typeManifest)
		case t&storage.TypeJournal != 0:
			ret = append(ret, x+typeJournal)
		case t&storage.TypeTable != 0:
			ret = append(ret, x+typeTable)
		case t&storage.TypeTemp != 0:
			ret = append(ret, x+typeTemp)
		}
	}
	switch {
	case m&ModeOpen != 0:
		add(modeOpen)
	case m&ModeCreate != 0:
		add(modeCreate)
	case m&ModeRemove != 0:
		add(modeRemove)
	case m&ModeRename != 0:
		add(modeRename)
	case m&ModeRead != 0:
		add(modeRead)
	case m&ModeWrite != 0:
		add(modeWrite)
	case m&ModeSync != 0:
		add(modeSync)
	case m&ModeClose != 0:
		add(modeClose)
	}
	return ret
}

func packFile(fd storage.FileDesc) uint64 {
	if fd.Num>>(63-typeCount) != 0 {
		panic("overflow")
	}
	return uint64(fd.Num<<typeCount) | uint64(fd.Type)
}

func unpackFile(x uint64) storage.FileDesc {
	return storage.FileDesc{
		Type: storage.FileType(x) & storage.TypeAll,
		Num:  int64(x >> typeCount),
	}
}

type emulatedError struct {
	err error
}

func (err emulatedError) Error() string {
	return fmt.Sprintf("emulated storage error: %v", err.err)
}

type storageLock struct {
	s *Storage
	l storage.Locker
}

func (l storageLock) Unlock() {
	l.l.Unlock()
	l.s.logI("storage lock released")
}

type reader struct {
	s  *Storage
	fd storage.FileDesc
	storage.Reader
}

func (r *reader) Read(p []byte) (n int, err error) {
	err = r.s.emulateError(ModeRead, r.fd.Type)
	if err == nil {
		r.s.stall(ModeRead, r.fd.Type)
		n, err = r.Reader.Read(p)
	}
	r.s.count(ModeRead, r.fd.Type, n)
	if err != nil && err != io.EOF {
		r.s.logI("read error, fd=%s n=%d err=%v", r.fd, n, err)
	}
	return
}

func (r *reader) ReadAt(p []byte, off int64) (n int, err error) {
	err = r.s.emulateError(ModeRead, r.fd.Type)
	if err == nil {
		r.s.stall(ModeRead, r.fd.Type)
		n, err = r.Reader.ReadAt(p, off)
	}
	r.s.count(ModeRead, r.fd.Type, n)
	if err != nil && err != io.EOF {
		r.s.logI("readAt error, fd=%s offset=%d n=%d err=%v", r.fd, off, n, err)
	}
	return
}

func (r *reader) Close() (err error) {
	return r.s.fileClose(r.fd, r.Reader)
}

type writer struct {
	s  *Storage
	fd storage.FileDesc
	storage.Writer
}

func (w *writer) Write(p []byte) (n int, err error) {
	err = w.s.emulateError(ModeWrite, w.fd.Type)
	if err == nil {
		w.s.stall(ModeWrite, w.fd.Type)
		n, err = w.Writer.Write(p)
	}
	w.s.count(ModeWrite, w.fd.Type, n)
	if err != nil && err != io.EOF {
		w.s.logI("write error, fd=%s n=%d err=%v", w.fd, n, err)
	}
	return
}

func (w *writer) Sync() (err error) {
	err = w.s.emulateError(ModeSync, w.fd.Type)
	if err == nil {
		w.s.stall(ModeSync, w.fd.Type)
		err = w.Writer.Sync()
	}
	w.s.count(ModeSync, w.fd.Type, 0)
	if err != nil {
		w.s.logI("sync error, fd=%s err=%v", w.fd, err)
	}
	return
}

func (w *writer) Close() (err error) {
	return w.s.fileClose(w.fd, w.Writer)
}

type Storage struct {
	storage.Storage
	path    string
	onClose func() (preserve bool, err error)
	onLog   func(str string)

	lmu sync.Mutex
	lb  bytes.Buffer

	mu   sync.Mutex
	rand *rand.Rand
	// Open files, true=writer, false=reader
	opens                   map[uint64]bool
	counters                [flattenCount]int
	bytesCounter            [flattenCount]int64
	emulatedError           [flattenCount]error
	emulatedErrorOnce       [flattenCount]bool
	emulatedRandomError     [flattenCount]error
	emulatedRandomErrorProb [flattenCount]float64
	stallCond               sync.Cond
	stalled                 [flattenCount]bool
}

func (s *Storage) log(skip int, str string) {
	s.lmu.Lock()
	defer s.lmu.Unlock()
	_, file, line, ok := runtime.Caller(skip + 2)
	if ok {
		// Truncate file name at last file name separator.
		if index := strings.LastIndex(file, "/"); index >= 0 {
			file = file[index+1:]
		} else if index = strings.LastIndex(file, "\\"); index >= 0 {
			file = file[index+1:]
		}
	} else {
		file = "???"
		line = 1
	}
	fmt.Fprintf(&s.lb, "%s:%d: ", file, line)
	lines := strings.Split(str, "\n")
	if l := len(lines); l > 1 && lines[l-1] == "" {
		lines = lines[:l-1]
	}
	for i, line := range lines {
		if i > 0 {
			s.lb.WriteString("\n\t")
		}
		s.lb.WriteString(line)
	}
	if s.onLog != nil {
		s.onLog(s.lb.String())
		s.lb.Reset()
	} else {
		s.lb.WriteByte('\n')
	}
}

func (s *Storage) logISkip(skip int, format string, args ...interface{}) {
	pc, _, _, ok := runtime.Caller(skip + 1)
	if ok {
		if f := runtime.FuncForPC(pc); f != nil {
			fname := f.Name()
			if index := strings.LastIndex(fname, "."); index >= 0 {
				fname = fname[index+1:]
			}
			format = fname + ": " + format
		}
	}
	s.log(skip+1, fmt.Sprintf(format, args...))
}

func (s *Storage) logI(format string, args ...interface{}) {
	s.logISkip(1, format, args...)
}

func (s *Storage) OnLog(onLog func(log string)) {
	s.lmu.Lock()
	s.onLog = onLog
	if s.lb.Len() != 0 {
		log := s.lb.String()
		s.onLog(log[:len(log)-1])
		s.lb.Reset()
	}
	s.lmu.Unlock()
}

func (s *Storage) Log(str string) {
	s.log(1, "Log: "+str)
	s.Storage.Log(str)
}

func (s *Storage) Lock() (l storage.Locker, err error) {
	l, err = s.Storage.Lock()
	if err != nil {
		s.logI("storage locking failed, err=%v", err)
	} else {
		s.logI("storage locked")
		l = storageLock{s, l}
	}
	return
}

func (s *Storage) List(t storage.FileType) (fds []storage.FileDesc, err error) {
	fds, err = s.Storage.List(t)
	if err != nil {
		s.logI("list failed, err=%v", err)
		return
	}
	s.logI("list, type=0x%x count=%d", int(t), len(fds))
	return
}

func (s *Storage) GetMeta() (fd storage.FileDesc, err error) {
	fd, err = s.Storage.GetMeta()
	if err != nil {
		if !os.IsNotExist(err) {
			s.logI("get meta failed, err=%v", err)
		}
		return
	}
	s.logI("get meta, fd=%s", fd)
	return
}

func (s *Storage) SetMeta(fd storage.FileDesc) error {
	ExpectWithOffset(1, fd.Type).To(Equal(storage.TypeManifest))
	err := s.Storage.SetMeta(fd)
	if err != nil {
		s.logI("set meta failed, fd=%s err=%v", fd, err)
	} else {
		s.logI("set meta, fd=%s", fd)
	}
	return err
}

func (s *Storage) fileClose(fd storage.FileDesc, closer io.Closer) (err error) {
	err = s.emulateError(ModeClose, fd.Type)
	if err == nil {
		s.stall(ModeClose, fd.Type)
	}
	x := packFile(fd)
	s.mu.Lock()
	defer s.mu.Unlock()
	if err == nil {
		ExpectWithOffset(2, s.opens).To(HaveKey(x), "File closed, fd=%s", fd)
		err = closer.Close()
	}
	s.countNB(ModeClose, fd.Type, 0)
	writer := s.opens[x]
	if err != nil {
		s.logISkip(1, "file close failed, fd=%s writer=%v err=%v", fd, writer, err)
	} else {
		s.logISkip(1, "file closed, fd=%s writer=%v", fd, writer)
		delete(s.opens, x)
	}
	return
}

func (s *Storage) assertOpen(fd storage.FileDesc) {
	x := packFile(fd)
	ExpectWithOffset(2, s.opens).NotTo(HaveKey(x), "File open, fd=%s writer=%v", fd, s.opens[x])
}

func (s *Storage) Open(fd storage.FileDesc) (r storage.Reader, err error) {
	err = s.emulateError(ModeOpen, fd.Type)
	if err == nil {
		s.stall(ModeOpen, fd.Type)
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	if err == nil {
		s.assertOpen(fd)
		s.countNB(ModeOpen, fd.Type, 0)
		r, err = s.Storage.Open(fd)
	}
	if err != nil {
		s.logI("file open failed, fd=%s err=%v", fd, err)
	} else {
		s.logI("file opened, fd=%s", fd)
		s.opens[packFile(fd)] = false
		r = &reader{s, fd, r}
	}
	return
}

func (s *Storage) Create(fd storage.FileDesc) (w storage.Writer, err error) {
	err = s.emulateError(ModeCreate, fd.Type)
	if err == nil {
		s.stall(ModeCreate, fd.Type)
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	if err == nil {
		s.assertOpen(fd)
		s.countNB(ModeCreate, fd.Type, 0)
		w, err = s.Storage.Create(fd)
	}
	if err != nil {
		s.logI("file create failed, fd=%s err=%v", fd, err)
	} else {
		s.logI("file created, fd=%s", fd)
		s.opens[packFile(fd)] = true
		w = &writer{s, fd, w}
	}
	return
}

func (s *Storage) Remove(fd storage.FileDesc) (err error) {
	err = s.emulateError(ModeRemove, fd.Type)
	if err == nil {
		s.stall(ModeRemove, fd.Type)
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	if err == nil {
		s.assertOpen(fd)
		s.countNB(ModeRemove, fd.Type, 0)
		err = s.Storage.Remove(fd)
	}
	if err != nil {
		s.logI("file remove failed, fd=%s err=%v", fd, err)
	} else {
		s.logI("file removed, fd=%s", fd)
	}
	return
}

func (s *Storage) ForceRemove(fd storage.FileDesc) (err error) {
	s.countNB(ModeRemove, fd.Type, 0)
	if err = s.Storage.Remove(fd); err != nil {
		s.logI("file remove failed (forced), fd=%s err=%v", fd, err)
	} else {
		s.logI("file removed (forced), fd=%s", fd)
	}
	return
}

func (s *Storage) Rename(oldfd, newfd storage.FileDesc) (err error) {
	err = s.emulateError(ModeRename, oldfd.Type)
	if err == nil {
		s.stall(ModeRename, oldfd.Type)
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	if err == nil {
		s.assertOpen(oldfd)
		s.assertOpen(newfd)
		s.countNB(ModeRename, oldfd.Type, 0)
		err = s.Storage.Rename(oldfd, newfd)
	}
	if err != nil {
		s.logI("file rename failed, oldfd=%s newfd=%s err=%v", oldfd, newfd, err)
	} else {
		s.logI("file renamed, oldfd=%s newfd=%s", oldfd, newfd)
	}
	return
}

func (s *Storage) ForceRename(oldfd, newfd storage.FileDesc) (err error) {
	s.countNB(ModeRename, oldfd.Type, 0)
	if err = s.Storage.Rename(oldfd, newfd); err != nil {
		s.logI("file rename failed (forced), oldfd=%s newfd=%s err=%v", oldfd, newfd, err)
	} else {
		s.logI("file renamed (forced), oldfd=%s newfd=%s", oldfd, newfd)
	}
	return
}

func (s *Storage) openFiles() string {
	out := "Open files:"
	for x, writer := range s.opens {
		fd := unpackFile(x)
		out += fmt.Sprintf("\n · fd=%s writer=%v", fd, writer)
	}
	return out
}

func (s *Storage) CloseCheck() {
	s.mu.Lock()
	defer s.mu.Unlock()
	ExpectWithOffset(1, s.opens).To(BeEmpty(), s.openFiles())
}

func (s *Storage) OnClose(onClose func() (preserve bool, err error)) {
	s.mu.Lock()
	s.onClose = onClose
	s.mu.Unlock()
}

func (s *Storage) Close() error {
	s.mu.Lock()
	defer s.mu.Unlock()
	ExpectWithOffset(1, s.opens).To(BeEmpty(), s.openFiles())
	err := s.Storage.Close()
	if err != nil {
		s.logI("storage closing failed, err=%v", err)
	} else {
		s.logI("storage closed")
	}
	var preserve bool
	if s.onClose != nil {
		var err0 error
		if preserve, err0 = s.onClose(); err0 != nil {
			s.logI("onClose error, err=%v", err0)
		}
	}
	if s.path != "" {
		if storageKeepFS || preserve {
			s.logI("storage is preserved, path=%v", s.path)
		} else {
			if err1 := os.RemoveAll(s.path); err1 != nil {
				s.logI("cannot remove storage, err=%v", err1)
			} else {
				s.logI("storage has been removed")
			}
		}
	}
	return err
}

func (s *Storage) countNB(m StorageMode, t storage.FileType, n int) {
	s.counters[flattenType(m, t)]++
	s.bytesCounter[flattenType(m, t)] += int64(n)
}

func (s *Storage) count(m StorageMode, t storage.FileType, n int) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.countNB(m, t, n)
}

func (s *Storage) ResetCounter(m StorageMode, t storage.FileType) {
	for _, x := range listFlattenType(m, t) {
		s.counters[x] = 0
		s.bytesCounter[x] = 0
	}
}

func (s *Storage) Counter(m StorageMode, t storage.FileType) (count int, bytes int64) {
	for _, x := range listFlattenType(m, t) {
		count += s.counters[x]
		bytes += s.bytesCounter[x]
	}
	return
}

func (s *Storage) emulateError(m StorageMode, t storage.FileType) error {
	s.mu.Lock()
	defer s.mu.Unlock()
	x := flattenType(m, t)
	if err := s.emulatedError[x]; err != nil {
		if s.emulatedErrorOnce[x] {
			s.emulatedError[x] = nil
		}
		return emulatedError{err}
	}
	if err := s.emulatedRandomError[x]; err != nil && s.rand.Float64() < s.emulatedRandomErrorProb[x] {
		return emulatedError{err}
	}
	return nil
}

func (s *Storage) EmulateError(m StorageMode, t storage.FileType, err error) {
	s.mu.Lock()
	defer s.mu.Unlock()
	for _, x := range listFlattenType(m, t) {
		s.emulatedError[x] = err
		s.emulatedErrorOnce[x] = false
	}
}

func (s *Storage) EmulateErrorOnce(m StorageMode, t storage.FileType, err error) {
	s.mu.Lock()
	defer s.mu.Unlock()
	for _, x := range listFlattenType(m, t) {
		s.emulatedError[x] = err
		s.emulatedErrorOnce[x] = true
	}
}

func (s *Storage) EmulateRandomError(m StorageMode, t storage.FileType, prob float64, err error) {
	s.mu.Lock()
	defer s.mu.Unlock()
	for _, x := range listFlattenType(m, t) {
		s.emulatedRandomError[x] = err
		s.emulatedRandomErrorProb[x] = prob
	}
}

func (s *Storage) stall(m StorageMode, t storage.FileType) {
	x := flattenType(m, t)
	s.mu.Lock()
	defer s.mu.Unlock()
	for s.stalled[x] {
		s.stallCond.Wait()
	}
}

func (s *Storage) Stall(m StorageMode, t storage.FileType) {
	s.mu.Lock()
	defer s.mu.Unlock()
	for _, x := range listFlattenType(m, t) {
		s.stalled[x] = true
	}
}

func (s *Storage) Release(m StorageMode, t storage.FileType) {
	s.mu.Lock()
	defer s.mu.Unlock()
	for _, x := range listFlattenType(m, t) {
		s.stalled[x] = false
	}
	s.stallCond.Broadcast()
}

func NewStorage() *Storage {
	var (
		stor storage.Storage
		path string
	)
	if storageUseFS {
		for {
			storageMu.Lock()
			num := storageNum
			storageNum++
			storageMu.Unlock()
			path = filepath.Join(os.TempDir(), fmt.Sprintf("goleveldb-test%d0%d0%d", os.Getuid(), os.Getpid(), num))
			if _, err := os.Stat(path); os.IsNotExist(err) {
				stor, err = storage.OpenFile(path, false)
				ExpectWithOffset(1, err).NotTo(HaveOccurred(), "creating storage at %s", path)
				break
			}
		}
	} else {
		stor = storage.NewMemStorage()
	}
	s := &Storage{
		Storage: stor,
		path:    path,
		rand:    NewRand(),
		opens:   make(map[uint64]bool),
	}
	s.stallCond.L = &s.mu
	if s.path != "" {
		s.logI("using FS storage")
		s.logI("storage path: %s", s.path)
	} else {
		s.logI("using MEM storage")
	}
	return s
}
```

## File: `leveldb/testutil/util.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package testutil

import (
	"bytes"
	"flag"
	"math/rand"
	"reflect"
	"sync"

	"github.com/onsi/ginkgo/config"

	"github.com/syndtr/goleveldb/leveldb/comparer"
)

var (
	runfn = make(map[string][]func())
	runmu sync.Mutex
)

func Defer(args ...interface{}) bool {
	var (
		group string
		fn    func()
	)
	for _, arg := range args {
		v := reflect.ValueOf(arg)
		switch v.Kind() {
		case reflect.String:
			group = v.String()
		case reflect.Func:
			r := reflect.ValueOf(&fn).Elem()
			r.Set(v)
		}
	}
	if fn != nil {
		runmu.Lock()
		runfn[group] = append(runfn[group], fn)
		runmu.Unlock()
	}
	return true
}

func RunDefer(groups ...string) bool {
	if len(groups) == 0 {
		groups = append(groups, "")
	}
	runmu.Lock()
	var runfn_ []func()
	for _, group := range groups {
		runfn_ = append(runfn_, runfn[group]...)
		delete(runfn, group)
	}
	runmu.Unlock()
	for _, fn := range runfn_ {
		fn()
	}
	return runfn_ != nil
}

func RandomSeed() int64 {
	if !flag.Parsed() {
		panic("random seed not initialized")
	}
	return config.GinkgoConfig.RandomSeed
}

func NewRand() *rand.Rand {
	return rand.New(rand.NewSource(RandomSeed()))
}

var cmp = comparer.DefaultComparer

func BytesSeparator(a, b []byte) []byte {
	if bytes.Equal(a, b) {
		return b
	}
	i, n := 0, len(a)
	if n > len(b) {
		n = len(b)
	}
	for ; i < n && (a[i] == b[i]); i++ {
	}
	x := append([]byte(nil), a[:i]...)
	if i < n {
		if c := a[i] + 1; c < b[i] {
			return append(x, c)
		}
		x = append(x, a[i])
		i++
	}
	for ; i < len(a); i++ {
		if c := a[i]; c < 0xff {
			return append(x, c+1)
		} else {
			x = append(x, c)
		}
	}
	if len(b) > i && b[i] > 0 {
		return append(x, b[i]-1)
	}
	return append(x, 'x')
}

func BytesAfter(b []byte) []byte {
	var x []byte
	for _, c := range b {
		if c < 0xff {
			return append(x, c+1)
		}
		x = append(x, c)
	}
	return append(x, 'x')
}

func RandomIndex(rnd *rand.Rand, n, round int, fn func(i int)) {
	if rnd == nil {
		rnd = NewRand()
	}
	for x := 0; x < round; x++ {
		fn(rnd.Intn(n))
	}
}

func ShuffledIndex(rnd *rand.Rand, n, round int, fn func(i int)) {
	if rnd == nil {
		rnd = NewRand()
	}
	for x := 0; x < round; x++ {
		for _, i := range rnd.Perm(n) {
			fn(i)
		}
	}
}

func RandomRange(rnd *rand.Rand, n, round int, fn func(start, limit int)) {
	if rnd == nil {
		rnd = NewRand()
	}
	for x := 0; x < round; x++ {
		start := rnd.Intn(n)
		length := 0
		if j := n - start; j > 0 {
			length = rnd.Intn(j)
		}
		fn(start, start+length)
	}
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
```

## File: `leveldb/util/buffer.go`
```go
// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package util

// This a copy of Go std bytes.Buffer with some modification
// and some features stripped.

import (
	"bytes"
	"io"
)

// smallBufferSize is an initial allocation minimal capacity.
const smallBufferSize = 64
const maxInt = int(^uint(0) >> 1)

// A Buffer is a variable-sized buffer of bytes with Read and Write methods.
// The zero value for Buffer is an empty buffer ready to use.
type Buffer struct {
	buf []byte // contents are the bytes buf[off : len(buf)]
	off int    // read at &buf[off], write at &buf[len(buf)]
}

// Bytes returns a slice of the contents of the unread portion of the buffer;
// len(b.Bytes()) == b.Len().  If the caller changes the contents of the
// returned slice, the contents of the buffer will change provided there
// are no intervening method calls on the Buffer.
func (b *Buffer) Bytes() []byte { return b.buf[b.off:] }

// String returns the contents of the unread portion of the buffer
// as a string.  If the Buffer is a nil pointer, it returns "<nil>".
func (b *Buffer) String() string {
	if b == nil {
		// Special case, useful in debugging.
		return "<nil>"
	}
	return string(b.buf[b.off:])
}

// Len returns the number of bytes of the unread portion of the buffer;
// b.Len() == len(b.Bytes()).
func (b *Buffer) Len() int { return len(b.buf) - b.off }

// Truncate discards all but the first n unread bytes from the buffer.
// It panics if n is negative or greater than the length of the buffer.
func (b *Buffer) Truncate(n int) {
	if n == 0 {
		b.Reset()
		return
	}
	if n < 0 || n > b.Len() {
		panic("leveldb/util.Buffer: truncation out of range")
	}
	b.buf = b.buf[:b.off+n]
}

// Reset resets the buffer so it has no content.
// b.Reset() is the same as b.Truncate(0).
func (b *Buffer) Reset() {
	b.buf = b.buf[:0]
	b.off = 0
}

// tryGrowByReslice is a inlineable version of grow for the fast-case where the
// internal buffer only needs to be resliced.
// It returns the index where bytes should be written and whether it succeeded.
func (b *Buffer) tryGrowByReslice(n int) (int, bool) {
	if l := len(b.buf); n <= cap(b.buf)-l {
		b.buf = b.buf[:l+n]
		return l, true
	}
	return 0, false
}

// grow grows the buffer to guarantee space for n more bytes.
// It returns the index where bytes should be written.
// If the buffer can't grow it will panic with bytes.ErrTooLarge.
func (b *Buffer) grow(n int) int {
	m := b.Len()
	// If buffer is empty, reset to recover space.
	if m == 0 && b.off != 0 {
		b.Reset()
	}
	// Try to grow by means of a reslice.
	if i, ok := b.tryGrowByReslice(n); ok {
		return i
	}
	if b.buf == nil && n <= smallBufferSize {
		b.buf = make([]byte, n, smallBufferSize)
		return 0
	}
	c := cap(b.buf)
	if n <= c/2-m {
		// We can slide things down instead of allocating a new
		// slice. We only need m+n <= c to slide, but
		// we instead let capacity get twice as large so we
		// don't spend all our time copying.
		copy(b.buf, b.buf[b.off:])
	} else if c > maxInt-c-n {
		panic(bytes.ErrTooLarge)
	} else {
		// Not enough space anywhere, we need to allocate.
		buf := makeSlice(2*c + n)
		copy(buf, b.buf[b.off:])
		b.buf = buf
	}
	// Restore b.off and len(b.buf).
	b.off = 0
	b.buf = b.buf[:m+n]
	return m
}

// Alloc allocs n bytes of slice from the buffer, growing the buffer as
// needed. If n is negative, Alloc will panic.
// If the buffer can't grow it will panic with bytes.ErrTooLarge.
func (b *Buffer) Alloc(n int) []byte {
	if n < 0 {
		panic("leveldb/util.Buffer.Alloc: negative count")
	}
	m, ok := b.tryGrowByReslice(n)
	if !ok {
		m = b.grow(n)
	}
	return b.buf[m:]
}

// Grow grows the buffer's capacity, if necessary, to guarantee space for
// another n bytes. After Grow(n), at least n bytes can be written to the
// buffer without another allocation.
// If n is negative, Grow will panic.
// If the buffer can't grow it will panic with bytes.ErrTooLarge.
func (b *Buffer) Grow(n int) {
	if n < 0 {
		panic("leveldb/util.Buffer.Grow: negative count")
	}
	m := b.grow(n)
	b.buf = b.buf[:m]
}

// Write appends the contents of p to the buffer, growing the buffer as
// needed. The return value n is the length of p; err is always nil. If the
// buffer becomes too large, Write will panic with bytes.ErrTooLarge.
func (b *Buffer) Write(p []byte) (n int, err error) {
	m, ok := b.tryGrowByReslice(len(p))
	if !ok {
		m = b.grow(len(p))
	}
	return copy(b.buf[m:], p), nil
}

// MinRead is the minimum slice size passed to a Read call by
// Buffer.ReadFrom.  As long as the Buffer has at least MinRead bytes beyond
// what is required to hold the contents of r, ReadFrom will not grow the
// underlying buffer.
const MinRead = 512

// ReadFrom reads data from r until EOF and appends it to the buffer, growing
// the buffer as needed. The return value n is the number of bytes read. Any
// error except io.EOF encountered during the read is also returned. If the
// buffer becomes too large, ReadFrom will panic with bytes.ErrTooLarge.
func (b *Buffer) ReadFrom(r io.Reader) (n int64, err error) {
	for {
		i := b.grow(MinRead)
		b.buf = b.buf[:i]
		m, e := r.Read(b.buf[i:cap(b.buf)])
		if m < 0 {
			panic("leveldb/util.Buffer.ReadFrom: reader returned negative count from Read")
		}

		b.buf = b.buf[:i+m]
		n += int64(m)
		if e == io.EOF {
			return n, nil // e is EOF, so return nil explicitly
		}
		if e != nil {
			return n, e
		}
	}
}

// makeSlice allocates a slice of size n. If the allocation fails, it panics
// with bytes.ErrTooLarge.
func makeSlice(n int) []byte {
	// If the make fails, give a known error.
	defer func() {
		if recover() != nil {
			panic(bytes.ErrTooLarge)
		}
	}()
	return make([]byte, n)
}

// WriteTo writes data to w until the buffer is drained or an error occurs.
// The return value n is the number of bytes written; it always fits into an
// int, but it is int64 to match the io.WriterTo interface. Any error
// encountered during the write is also returned.
func (b *Buffer) WriteTo(w io.Writer) (n int64, err error) {
	if b.off < len(b.buf) {
		nBytes := b.Len()
		m, e := w.Write(b.buf[b.off:])
		if m > nBytes {
			panic("leveldb/util.Buffer.WriteTo: invalid Write count")
		}
		b.off += m
		n = int64(m)
		if e != nil {
			return n, e
		}
		// all bytes should have been written, by definition of
		// Write method in io.Writer
		if m != nBytes {
			return n, io.ErrShortWrite
		}
	}
	// Buffer is now empty; reset.
	b.Reset()
	return
}

// WriteByte appends the byte c to the buffer, growing the buffer as needed.
// The returned error is always nil, but is included to match bufio.Writer's
// WriteByte. If the buffer becomes too large, WriteByte will panic with
// bytes.ErrTooLarge.
func (b *Buffer) WriteByte(c byte) error {
	m, ok := b.tryGrowByReslice(1)
	if !ok {
		m = b.grow(1)
	}
	b.buf[m] = c
	return nil
}

// Read reads the next len(p) bytes from the buffer or until the buffer
// is drained.  The return value n is the number of bytes read.  If the
// buffer has no data to return, err is io.EOF (unless len(p) is zero);
// otherwise it is nil.
func (b *Buffer) Read(p []byte) (n int, err error) {
	if b.off >= len(b.buf) {
		// Buffer is empty, reset to recover space.
		b.Reset()
		if len(p) == 0 {
			return
		}
		return 0, io.EOF
	}
	n = copy(p, b.buf[b.off:])
	b.off += n
	return
}

// Next returns a slice containing the next n bytes from the buffer,
// advancing the buffer as if the bytes had been returned by Read.
// If there are fewer than n bytes in the buffer, Next returns the entire buffer.
// The slice is only valid until the next call to a read or write method.
func (b *Buffer) Next(n int) []byte {
	m := b.Len()
	if n > m {
		n = m
	}
	data := b.buf[b.off : b.off+n]
	b.off += n
	return data
}

// ReadByte reads and returns the next byte from the buffer.
// If no byte is available, it returns error io.EOF.
func (b *Buffer) ReadByte() (c byte, err error) {
	if b.off >= len(b.buf) {
		// Buffer is empty, reset to recover space.
		b.Reset()
		return 0, io.EOF
	}
	c = b.buf[b.off]
	b.off++
	return c, nil
}

// ReadBytes reads until the first occurrence of delim in the input,
// returning a slice containing the data up to and including the delimiter.
// If ReadBytes encounters an error before finding a delimiter,
// it returns the data read before the error and the error itself (often io.EOF).
// ReadBytes returns err != nil if and only if the returned data does not end in
// delim.
func (b *Buffer) ReadBytes(delim byte) (line []byte, err error) {
	slice, err := b.readSlice(delim)
	// return a copy of slice. The buffer's backing array may
	// be overwritten by later calls.
	line = append(line, slice...)
	return
}

// readSlice is like ReadBytes but returns a reference to internal buffer data.
func (b *Buffer) readSlice(delim byte) (line []byte, err error) {
	i := bytes.IndexByte(b.buf[b.off:], delim)
	end := b.off + i + 1
	if i < 0 {
		end = len(b.buf)
		err = io.EOF
	}
	line = b.buf[b.off:end]
	b.off = end
	return line, err
}

// NewBuffer creates and initializes a new Buffer using buf as its initial
// contents.  It is intended to prepare a Buffer to read existing data.  It
// can also be used to size the internal buffer for writing. To do that,
// buf should have the desired capacity but a length of zero.
//
// In most cases, new(Buffer) (or just declaring a Buffer variable) is
// sufficient to initialize a Buffer.
func NewBuffer(buf []byte) *Buffer { return &Buffer{buf: buf} }
```

## File: `leveldb/util/buffer_pool.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package util

import (
	"fmt"
	"sync"
	"sync/atomic"
)

// BufferPool is a 'buffer pool'.
type BufferPool struct {
	pool     [6]sync.Pool
	baseline [5]int

	get     uint32
	put     uint32
	less    uint32
	equal   uint32
	greater uint32
	miss    uint32
}

func (p *BufferPool) poolNum(n int) int {
	for i, x := range p.baseline {
		if n <= x {
			return i
		}
	}
	return len(p.baseline)
}

// Get returns buffer with length of n.
func (p *BufferPool) Get(n int) []byte {
	if p == nil {
		return make([]byte, n)
	}
	atomic.AddUint32(&p.get, 1)

	poolNum := p.poolNum(n)

	b := p.pool[poolNum].Get().(*[]byte)

	if cap(*b) == 0 {
		// If we grabbed nothing, increment the miss stats.
		atomic.AddUint32(&p.miss, 1)

		if poolNum == len(p.baseline) {
			*b = make([]byte, n)
			return *b
		}

		*b = make([]byte, p.baseline[poolNum])
		*b = (*b)[:n]
		return *b
	} else {
		// If there is enough capacity in the bytes grabbed, resize the length
		// to n and return.
		if n < cap(*b) {
			atomic.AddUint32(&p.less, 1)
			*b = (*b)[:n]
			return *b
		} else if n == cap(*b) {
			atomic.AddUint32(&p.equal, 1)
			*b = (*b)[:n]
			return *b
		} else if n > cap(*b) {
			atomic.AddUint32(&p.greater, 1)
		}
	}

	if poolNum == len(p.baseline) {
		*b = make([]byte, n)
		return *b
	}
	*b = make([]byte, p.baseline[poolNum])
	*b = (*b)[:n]
	return *b
}

// Put adds given buffer to the pool.
func (p *BufferPool) Put(b []byte) {
	if p == nil {
		return
	}

	poolNum := p.poolNum(cap(b))

	atomic.AddUint32(&p.put, 1)
	p.pool[poolNum].Put(&b)
}

func (p *BufferPool) String() string {
	if p == nil {
		return "<nil>"
	}
	return fmt.Sprintf("BufferPool{B·%d G·%d P·%d <·%d =·%d >·%d M·%d}",
		p.baseline, p.get, p.put, p.less, p.equal, p.greater, p.miss)
}

// NewBufferPool creates a new initialized 'buffer pool'.
func NewBufferPool(baseline int) *BufferPool {
	if baseline <= 0 {
		panic("baseline can't be <= 0")
	}
	bufPool := &BufferPool{
		baseline: [...]int{baseline / 4, baseline / 2, baseline, baseline * 2, baseline * 4},
		pool: [6]sync.Pool{
			{
				New: func() interface{} { return new([]byte) },
			},
			{
				New: func() interface{} { return new([]byte) },
			},
			{
				New: func() interface{} { return new([]byte) },
			},
			{
				New: func() interface{} { return new([]byte) },
			},
			{
				New: func() interface{} { return new([]byte) },
			},
			{
				New: func() interface{} { return new([]byte) },
			},
		},
	}

	return bufPool
}
```

## File: `leveldb/util/buffer_test.go`
```go
// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package util

import (
	"bytes"
	"io"
	"math/rand"
	"runtime"
	"testing"
)

const N = 10000      // make this bigger for a larger (and slower) test
var data string      // test data for write tests
var testBytes []byte // test data; same as data but as a slice.

func init() {
	testBytes = make([]byte, N)
	for i := 0; i < N; i++ {
		testBytes[i] = 'a' + byte(i%26)
	}
	data = string(testBytes)
}

// Verify that contents of buf match the string s.
func check(t *testing.T, testname string, buf *Buffer, s string) {
	bytes := buf.Bytes()
	str := buf.String()
	if buf.Len() != len(bytes) {
		t.Errorf("%s: buf.Len() == %d, len(buf.Bytes()) == %d", testname, buf.Len(), len(bytes))
	}

	if buf.Len() != len(str) {
		t.Errorf("%s: buf.Len() == %d, len(buf.String()) == %d", testname, buf.Len(), len(str))
	}

	if buf.Len() != len(s) {
		t.Errorf("%s: buf.Len() == %d, len(s) == %d", testname, buf.Len(), len(s))
	}

	if string(bytes) != s {
		t.Errorf("%s: string(buf.Bytes()) == %q, s == %q", testname, string(bytes), s)
	}
}

// Fill buf through n writes of byte slice fub.
// The initial contents of buf corresponds to the string s;
// the result is the final contents of buf returned as a string.
func fillBytes(t *testing.T, testname string, buf *Buffer, s string, n int, fub []byte) string {
	check(t, testname+" (fill 1)", buf, s)
	for ; n > 0; n-- {
		m, err := buf.Write(fub)
		if m != len(fub) {
			t.Errorf(testname+" (fill 2): m == %d, expected %d", m, len(fub))
		}
		if err != nil {
			t.Errorf(testname+" (fill 3): err should always be nil, found err == %s", err)
		}
		s += string(fub)
		check(t, testname+" (fill 4)", buf, s)
	}
	return s
}

func TestNewBuffer(t *testing.T) {
	buf := NewBuffer(testBytes)
	check(t, "NewBuffer", buf, data)
}

// Empty buf through repeated reads into fub.
// The initial contents of buf corresponds to the string s.
func empty(t *testing.T, testname string, buf *Buffer, s string, fub []byte) {
	check(t, testname+" (empty 1)", buf, s)

	for {
		n, err := buf.Read(fub)
		if n == 0 {
			break
		}
		if err != nil {
			t.Errorf(testname+" (empty 2): err should always be nil, found err == %s", err)
		}
		s = s[n:]
		check(t, testname+" (empty 3)", buf, s)
	}

	check(t, testname+" (empty 4)", buf, "")
}

func TestBasicOperations(t *testing.T) {
	var buf Buffer

	for i := 0; i < 5; i++ {
		check(t, "TestBasicOperations (1)", &buf, "")

		buf.Reset()
		check(t, "TestBasicOperations (2)", &buf, "")

		buf.Truncate(0)
		check(t, "TestBasicOperations (3)", &buf, "")

		n, err := buf.Write([]byte(data[0:1]))
		if n != 1 {
			t.Errorf("wrote 1 byte, but n == %d", n)
		}
		if err != nil {
			t.Errorf("err should always be nil, but err == %s", err)
		}
		check(t, "TestBasicOperations (4)", &buf, "a")

		if err := buf.WriteByte(data[1]); err != nil {
			t.Fatal(err)
		}
		check(t, "TestBasicOperations (5)", &buf, "ab")

		n, err = buf.Write([]byte(data[2:26]))
		if err != nil {
			t.Fatal(err)
		}
		if n != 24 {
			t.Errorf("wrote 25 bytes, but n == %d", n)
		}
		check(t, "TestBasicOperations (6)", &buf, data[0:26])

		buf.Truncate(26)
		check(t, "TestBasicOperations (7)", &buf, data[0:26])

		buf.Truncate(20)
		check(t, "TestBasicOperations (8)", &buf, data[0:20])

		empty(t, "TestBasicOperations (9)", &buf, data[0:20], make([]byte, 5))
		empty(t, "TestBasicOperations (10)", &buf, "", make([]byte, 100))

		if err := buf.WriteByte(data[1]); err != nil {
			t.Fatal(err)
		}
		c, err := buf.ReadByte()
		if err != nil {
			t.Error("ReadByte unexpected eof")
		}
		if c != data[1] {
			t.Errorf("ReadByte wrong value c=%v", c)
		}
		_, err = buf.ReadByte()
		if err == nil {
			t.Error("ReadByte unexpected not eof")
		}
	}
}

func TestLargeByteWrites(t *testing.T) {
	var buf Buffer
	limit := 30
	if testing.Short() {
		limit = 9
	}
	for i := 3; i < limit; i += 3 {
		s := fillBytes(t, "TestLargeWrites (1)", &buf, "", 5, testBytes)
		empty(t, "TestLargeByteWrites (2)", &buf, s, make([]byte, len(data)/i))
	}
	check(t, "TestLargeByteWrites (3)", &buf, "")
}

func TestLargeByteReads(t *testing.T) {
	var buf Buffer
	for i := 3; i < 30; i += 3 {
		s := fillBytes(t, "TestLargeReads (1)", &buf, "", 5, testBytes[0:len(testBytes)/i])
		empty(t, "TestLargeReads (2)", &buf, s, make([]byte, len(data)))
	}
	check(t, "TestLargeByteReads (3)", &buf, "")
}

func TestMixedReadsAndWrites(t *testing.T) {
	var buf Buffer
	s := ""
	for i := 0; i < 50; i++ {
		wlen := rand.Intn(len(data))
		s = fillBytes(t, "TestMixedReadsAndWrites (1)", &buf, s, 1, testBytes[0:wlen])
		rlen := rand.Intn(len(data))
		fub := make([]byte, rlen)
		n, _ := buf.Read(fub)
		s = s[n:]
	}
	empty(t, "TestMixedReadsAndWrites (2)", &buf, s, make([]byte, buf.Len()))
}

func TestNil(t *testing.T) {
	var b *Buffer
	if b.String() != "<nil>" {
		t.Errorf("expected <nil>; got %q", b.String())
	}
}

func TestReadFrom(t *testing.T) {
	var buf Buffer
	for i := 3; i < 30; i += 3 {
		s := fillBytes(t, "TestReadFrom (1)", &buf, "", 5, testBytes[0:len(testBytes)/i])
		var b Buffer
		if _, err := b.ReadFrom(&buf); err != nil {
			t.Fatal(err)
		}
		empty(t, "TestReadFrom (2)", &b, s, make([]byte, len(data)))
	}
}

func TestWriteTo(t *testing.T) {
	var buf Buffer
	for i := 3; i < 30; i += 3 {
		s := fillBytes(t, "TestWriteTo (1)", &buf, "", 5, testBytes[0:len(testBytes)/i])
		var b Buffer
		if _, err := buf.WriteTo(&b); err != nil {
			t.Fatal(err)
		}
		empty(t, "TestWriteTo (2)", &b, s, make([]byte, len(data)))
	}
}

func TestNext(t *testing.T) {
	b := []byte{0, 1, 2, 3, 4}
	tmp := make([]byte, 5)
	for i := 0; i <= 5; i++ {
		for j := i; j <= 5; j++ {
			for k := 0; k <= 6; k++ {
				// 0 <= i <= j <= 5; 0 <= k <= 6
				// Check that if we start with a buffer
				// of length j at offset i and ask for
				// Next(k), we get the right bytes.
				buf := NewBuffer(b[0:j])
				n, _ := buf.Read(tmp[0:i])
				if n != i {
					t.Fatalf("Read %d returned %d", i, n)
				}
				bb := buf.Next(k)
				want := k
				if want > j-i {
					want = j - i
				}
				if len(bb) != want {
					t.Fatalf("in %d,%d: len(Next(%d)) == %d", i, j, k, len(bb))
				}
				for l, v := range bb {
					if v != byte(l+i) {
						t.Fatalf("in %d,%d: Next(%d)[%d] = %d, want %d", i, j, k, l, v, l+i)
					}
				}
			}
		}
	}
}

var readBytesTests = []struct {
	buffer   string
	delim    byte
	expected []string
	err      error
}{
	{"", 0, []string{""}, io.EOF},
	{"a\x00", 0, []string{"a\x00"}, nil},
	{"abbbaaaba", 'b', []string{"ab", "b", "b", "aaab"}, nil},
	{"hello\x01world", 1, []string{"hello\x01"}, nil},
	{"foo\nbar", 0, []string{"foo\nbar"}, io.EOF},
	{"alpha\nbeta\ngamma\n", '\n', []string{"alpha\n", "beta\n", "gamma\n"}, nil},
	{"alpha\nbeta\ngamma", '\n', []string{"alpha\n", "beta\n", "gamma"}, io.EOF},
}

func TestReadBytes(t *testing.T) {
	for _, test := range readBytesTests {
		buf := NewBuffer([]byte(test.buffer))
		var err error
		for _, expected := range test.expected {
			var bytes []byte
			bytes, err = buf.ReadBytes(test.delim)
			if string(bytes) != expected {
				t.Errorf("expected %q, got %q", expected, bytes)
			}
			if err != nil {
				break
			}
		}
		if err != test.err {
			t.Errorf("expected error %v, got %v", test.err, err)
		}
	}
}

func TestGrow(t *testing.T) {
	x := []byte{'x'}
	y := []byte{'y'}
	tmp := make([]byte, 72)
	for _, startLen := range []int{0, 100, 1000, 10000, 100000} {
		xBytes := bytes.Repeat(x, startLen)
		for _, growLen := range []int{0, 100, 1000, 10000, 100000} {
			buf := NewBuffer(xBytes)
			// If we read, this affects buf.off, which is good to test.
			readBytes, _ := buf.Read(tmp)
			buf.Grow(growLen)
			yBytes := bytes.Repeat(y, growLen)
			// Check no allocation occurs in write, as long as we're single-threaded.
			var m1, m2 runtime.MemStats
			runtime.ReadMemStats(&m1)
			if _, err := buf.Write(yBytes); err != nil {
				t.Fatal(err)
			}
			runtime.ReadMemStats(&m2)
			if runtime.GOMAXPROCS(-1) == 1 && m1.Mallocs != m2.Mallocs {
				t.Errorf("allocation occurred during write")
			}
			// Check that buffer has correct data.
			if !bytes.Equal(buf.Bytes()[0:startLen-readBytes], xBytes[readBytes:]) {
				t.Errorf("bad initial data at %d %d", startLen, growLen)
			}
			if !bytes.Equal(buf.Bytes()[startLen-readBytes:startLen-readBytes+growLen], yBytes) {
				t.Errorf("bad written data at %d %d", startLen, growLen)
			}
		}
	}
}

// TestReadEmptyAtEOF: Was a bug: used to give EOF reading empty slice at EOF.
func TestReadEmptyAtEOF(t *testing.T) {
	b := new(Buffer)
	slice := make([]byte, 0)
	n, err := b.Read(slice)
	if err != nil {
		t.Errorf("read error: %v", err)
	}
	if n != 0 {
		t.Errorf("wrong count; got %d want 0", n)
	}
}

// TestBufferGrowth tests that we occasionally compact. Issue 5154.
func TestBufferGrowth(t *testing.T) {
	var b Buffer
	buf := make([]byte, 1024)
	if _, err := b.Write(buf[0:1]); err != nil {
		t.Fatal(err)
	}
	var cap0 int
	for i := 0; i < 5<<10; i++ {
		if _, err := b.Write(buf); err != nil {
			t.Fatal(err)
		}
		if _, err := b.Read(buf); err != nil {
			t.Fatal(err)
		}
		if i == 0 {
			cap0 = cap(b.buf)
		}
	}
	cap1 := cap(b.buf)
	// (*Buffer).grow allows for 2x capacity slop before sliding,
	// so set our error threshold at 3x.
	if cap1 > cap0*3 {
		t.Errorf("buffer cap = %d; too big (grew from %d)", cap1, cap0)
	}
}

func BenchmarkWriteByte(b *testing.B) {
	const n = 4 << 10
	b.SetBytes(n)
	buf := NewBuffer(make([]byte, n))
	for i := 0; i < b.N; i++ {
		buf.Reset()
		for i := 0; i < n; i++ {
			if err := buf.WriteByte('x'); err != nil {
				b.Fatal(err)
			}
		}
	}
}

func BenchmarkAlloc(b *testing.B) {
	const n = 4 << 10
	b.SetBytes(n)
	buf := NewBuffer(make([]byte, n))
	for i := 0; i < b.N; i++ {
		buf.Reset()
		for i := 0; i < n; i++ {
			buf.Alloc(1)
		}
	}
}

// BenchmarkBufferNotEmptyWriteRead: From Issue 5154.
func BenchmarkBufferNotEmptyWriteRead(b *testing.B) {
	buf := make([]byte, 1024)
	for i := 0; i < b.N; i++ {
		var buf2 Buffer
		if _, err := buf2.Write(buf[0:1]); err != nil {
			b.Fatal(err)
		}
		for i := 0; i < 5<<10; i++ {
			if _, err := buf2.Write(buf); err != nil {
				b.Fatal(err)
			}
			if _, err := buf2.Read(buf); err != nil {
				b.Fatal(err)
			}
		}
	}
}

// BenchmarkBufferFullSmallReads checks that we don't compact too often. From Issue 5154.
func BenchmarkBufferFullSmallReads(b *testing.B) {
	buf := make([]byte, 1024)
	for i := 0; i < b.N; i++ {
		var buf2 Buffer
		if _, err := buf2.Write(buf); err != nil {
			b.Fatal(err)
		}
		for buf2.Len()+20 < cap(buf2.buf) {
			if _, err := buf2.Write(buf[:10]); err != nil {
				b.Fatal(err)
			}
		}
		for i := 0; i < 5<<10; i++ {
			if _, err := buf2.Read(buf[:1]); err != nil {
				b.Fatal(err)
			}
			if _, err := buf2.Write(buf[:1]); err != nil {
				b.Fatal(err)
			}
		}
	}
}
```

## File: `leveldb/util/crc32.go`
```go
// Copyright 2011 The LevelDB-Go Authors. All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package util

import (
	"hash/crc32"
)

var table = crc32.MakeTable(crc32.Castagnoli)

// CRC is a CRC-32 checksum computed using Castagnoli's polynomial.
type CRC uint32

// NewCRC creates a new crc based on the given bytes.
func NewCRC(b []byte) CRC {
	return CRC(0).Update(b)
}

// Update updates the crc with the given bytes.
func (c CRC) Update(b []byte) CRC {
	return CRC(crc32.Update(uint32(c), table, b))
}

// Value returns a masked crc.
func (c CRC) Value() uint32 {
	return uint32(c>>15|c<<17) + 0xa282ead8
}
```

## File: `leveldb/util/hash.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package util

import (
	"encoding/binary"
)

// Hash return hash of the given data.
func Hash(data []byte, seed uint32) uint32 {
	// Similar to murmur hash
	const (
		m = uint32(0xc6a4a793)
		r = uint32(24)
	)
	var (
		h = seed ^ (uint32(len(data)) * m)
		i int
	)

	for n := len(data) - len(data)%4; i < n; i += 4 {
		h += binary.LittleEndian.Uint32(data[i:])
		h *= m
		h ^= (h >> 16)
	}

	switch len(data) - i {
	default:
		panic("not reached")
	case 3:
		h += uint32(data[i+2]) << 16
		fallthrough
	case 2:
		h += uint32(data[i+1]) << 8
		fallthrough
	case 1:
		h += uint32(data[i])
		h *= m
		h ^= (h >> r)
	case 0:
	}

	return h
}
```

## File: `leveldb/util/hash_test.go`
```go
// Copyright (c) 2012, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package util

import (
	"testing"
)

var hashTests = []struct {
	data []byte
	seed uint32
	hash uint32
}{
	{nil, 0xbc9f1d34, 0xbc9f1d34},
	{[]byte{0x62}, 0xbc9f1d34, 0xef1345c4},
	{[]byte{0xc3, 0x97}, 0xbc9f1d34, 0x5b663814},
	{[]byte{0xe2, 0x99, 0xa5}, 0xbc9f1d34, 0x323c078f},
	{[]byte{0xe1, 0x80, 0xb9, 0x32}, 0xbc9f1d34, 0xed21633a},
	{[]byte{
		0x01, 0xc0, 0x00, 0x00,
		0x00, 0x00, 0x00, 0x00,
		0x00, 0x00, 0x00, 0x00,
		0x00, 0x00, 0x00, 0x00,
		0x14, 0x00, 0x00, 0x00,
		0x00, 0x00, 0x04, 0x00,
		0x00, 0x00, 0x00, 0x14,
		0x00, 0x00, 0x00, 0x18,
		0x28, 0x00, 0x00, 0x00,
		0x00, 0x00, 0x00, 0x00,
		0x02, 0x00, 0x00, 0x00,
		0x00, 0x00, 0x00, 0x00,
	}, 0x12345678, 0xf333dabb},
}

func TestHash(t *testing.T) {
	for i, x := range hashTests {
		h := Hash(x.data, x.seed)
		if h != x.hash {
			t.Fatalf("test-%d: invalid hash, %#x vs %#x", i, h, x.hash)
		}
	}
}
```

## File: `leveldb/util/range.go`
```go
// Copyright (c) 2014, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package util

// Range is a key range.
type Range struct {
	// Start of the key range, include in the range.
	Start []byte

	// Limit of the key range, not include in the range.
	Limit []byte
}

// BytesPrefix returns key range that satisfy the given prefix.
// This only applicable for the standard 'bytes comparer'.
func BytesPrefix(prefix []byte) *Range {
	var limit []byte
	for i := len(prefix) - 1; i >= 0; i-- {
		c := prefix[i]
		if c < 0xff {
			limit = make([]byte, i+1)
			copy(limit, prefix)
			limit[i] = c + 1
			break
		}
	}
	return &Range{prefix, limit}
}
```

## File: `leveldb/util/util.go`
```go
// Copyright (c) 2013, Suryandaru Triandana <syndtr@gmail.com>
// All rights reserved.
//
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package util provides utilities used throughout leveldb.
package util

import (
	"errors"
)

var (
	ErrReleased    = errors.New("leveldb: resource already relesed")
	ErrHasReleaser = errors.New("leveldb: releaser already defined")
)

// Releaser is the interface that wraps the basic Release method.
type Releaser interface {
	// Release releases associated resources. Release should always success
	// and can be called multiple times without causing error.
	Release()
}

// ReleaseSetter is the interface that wraps the basic SetReleaser method.
type ReleaseSetter interface {
	// SetReleaser associates the given releaser to the resources. The
	// releaser will be called once coresponding resources released.
	// Calling SetReleaser with nil will clear the releaser.
	//
	// This will panic if a releaser already present or coresponding
	// resource is already released. Releaser should be cleared first
	// before assigned a new one.
	SetReleaser(releaser Releaser)
}

// BasicReleaser provides basic implementation of Releaser and ReleaseSetter.
type BasicReleaser struct {
	releaser Releaser
	released bool
}

// Released returns whether Release method already called.
func (r *BasicReleaser) Released() bool {
	return r.released
}

// Release implements Releaser.Release.
func (r *BasicReleaser) Release() {
	if !r.released {
		if r.releaser != nil {
			r.releaser.Release()
			r.releaser = nil
		}
		r.released = true
	}
}

// SetReleaser implements ReleaseSetter.SetReleaser.
func (r *BasicReleaser) SetReleaser(releaser Releaser) {
	if r.released {
		panic(ErrReleased)
	}
	if r.releaser != nil && releaser != nil {
		panic(ErrHasReleaser)
	}
	r.releaser = releaser
}

type NoopReleaser struct{}

func (NoopReleaser) Release() {}
```

## File: `manualtest/dbstress/key.go`
```go
package main

import (
	"encoding/binary"
	"fmt"

	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/storage"
)

type ErrIkeyCorrupted struct {
	Ikey   []byte
	Reason string
}

func (e *ErrIkeyCorrupted) Error() string {
	return fmt.Sprintf("leveldb: iKey %q corrupted: %s", e.Ikey, e.Reason)
}

func newErrIkeyCorrupted(ikey []byte, reason string) error {
	return errors.NewErrCorrupted(storage.FileDesc{}, &ErrIkeyCorrupted{append([]byte(nil), ikey...), reason})
}

type kType int

func (kt kType) String() string {
	switch kt {
	case ktDel:
		return "d"
	case ktVal:
		return "v"
	}
	return "x"
}

// Value types encoded as the last component of internal keys.
// Don't modify; this value are saved to disk.
const (
	ktDel kType = iota
	ktVal
)

// ktSeek defines the kType that should be passed when constructing an
// internal key for seeking to a particular sequence number (since we
// sort sequence numbers in decreasing order and the value type is
// embedded as the low 8 bits in the sequence number in internal keys,
// we need to use the highest-numbered ValueType, not the lowest).
const ktSeek = ktVal

const (
	// Maximum value possible for sequence number; the 8-bits are
	// used by value type, so its can packed together in single
	// 64-bit integer.
	kMaxSeq uint64 = (uint64(1) << 56) - 1
	// Maximum value possible for packed sequence number and type.
	kMaxNum uint64 = (kMaxSeq << 8) | uint64(ktSeek)
)

// Maximum number encoded in bytes.
var kMaxNumBytes = make([]byte, 8)

func init() {
	binary.LittleEndian.PutUint64(kMaxNumBytes, kMaxNum)
}

func parseIkey(ik []byte) (ukey []byte, seq uint64, kt kType, err error) {
	if len(ik) < 8 {
		return nil, 0, 0, newErrIkeyCorrupted(ik, "invalid length")
	}
	num := binary.LittleEndian.Uint64(ik[len(ik)-8:])
	seq, kt = num>>8, kType(num&0xff)
	if kt > ktVal {
		return nil, 0, 0, newErrIkeyCorrupted(ik, "invalid type")
	}
	ukey = ik[:len(ik)-8]
	return
}
```

## File: `manualtest/dbstress/main.go`
```go
package main

import (
	"crypto/rand"
	"encoding/binary"
	"flag"
	"fmt"
	"log"
	mrand "math/rand"
	"net/http"
	_ "net/http/pprof"
	"os"
	"os/signal"
	"path"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
	"syscall"
	"time"

	"github.com/syndtr/goleveldb/leveldb"
	"github.com/syndtr/goleveldb/leveldb/errors"
	"github.com/syndtr/goleveldb/leveldb/filter"
	"github.com/syndtr/goleveldb/leveldb/opt"
	"github.com/syndtr/goleveldb/leveldb/storage"
	"github.com/syndtr/goleveldb/leveldb/table"
	"github.com/syndtr/goleveldb/leveldb/util"
)

var (
	dbPath                 = path.Join(os.TempDir(), "goleveldb-testdb")
	openFilesCacheCapacity = 500
	keyLen                 = 63
	valueLen               = 256
	numKeys                = arrayInt{100000, 1332, 531, 1234, 9553, 1024, 35743}
	httpProf               = "127.0.0.1:5454"
	transactionProb        = 0.5
	enableBlockCache       = false
	enableCompression      = false
	enableBufferPool       = false
	maxManifestFileSize    = opt.DefaultMaxManifestFileSize

	wg         = new(sync.WaitGroup)
	done, fail uint32

	bpool *util.BufferPool
)

type arrayInt []int

func (a arrayInt) String() string {
	var str string
	for i, n := range a {
		if i > 0 {
			str += ","
		}
		str += strconv.Itoa(n)
	}
	return str
}

func (a *arrayInt) Set(str string) error {
	var na arrayInt
	for _, s := range strings.Split(str, ",") {
		s = strings.TrimSpace(s)
		if s != "" {
			n, err := strconv.Atoi(s)
			if err != nil {
				return err
			}
			na = append(na, n)
		}
	}
	*a = na
	return nil
}

func init() {
	flag.StringVar(&dbPath, "db", dbPath, "testdb path")
	flag.IntVar(&openFilesCacheCapacity, "openfilescachecap", openFilesCacheCapacity, "open files cache capacity")
	flag.IntVar(&keyLen, "keylen", keyLen, "key length")
	flag.IntVar(&valueLen, "valuelen", valueLen, "value length")
	flag.Var(&numKeys, "numkeys", "num keys")
	flag.StringVar(&httpProf, "httpprof", httpProf, "http pprof listen addr")
	flag.Float64Var(&transactionProb, "transactionprob", transactionProb, "probablity of writes using transaction")
	flag.BoolVar(&enableBufferPool, "enablebufferpool", enableBufferPool, "enable buffer pool")
	flag.BoolVar(&enableBlockCache, "enableblockcache", enableBlockCache, "enable block cache")
	flag.BoolVar(&enableCompression, "enablecompression", enableCompression, "enable block compression")
	flag.Int64Var(&maxManifestFileSize, "maxManifestFileSize", maxManifestFileSize, "max manifest file size")
}

func randomData(dst []byte, ns, prefix byte, i uint32, dataLen int) []byte {
	if dataLen < (2+4+4)*2+4 {
		panic("dataLen is too small")
	}
	if cap(dst) < dataLen {
		dst = make([]byte, dataLen)
	} else {
		dst = dst[:dataLen]
	}
	half := (dataLen - 4) / 2
	if _, err := rand.Reader.Read(dst[2 : half-8]); err != nil {
		panic(err)
	}
	dst[0] = ns
	dst[1] = prefix
	binary.LittleEndian.PutUint32(dst[half-8:], i)
	binary.LittleEndian.PutUint32(dst[half-8:], i)
	binary.LittleEndian.PutUint32(dst[half-4:], util.NewCRC(dst[:half-4]).Value())
	full := half * 2
	copy(dst[half:full], dst[:half])
	if full < dataLen-4 {
		if _, err := rand.Reader.Read(dst[full : dataLen-4]); err != nil {
			panic(err)
		}
	}
	binary.LittleEndian.PutUint32(dst[dataLen-4:], util.NewCRC(dst[:dataLen-4]).Value())
	return dst
}

func dataSplit(data []byte) (data0, data1 []byte) {
	n := (len(data) - 4) / 2
	return data[:n], data[n : n+n]
}

func dataNS(data []byte) byte {
	return data[0]
}

func dataPrefix(data []byte) byte {
	return data[1]
}

func dataI(data []byte) uint32 {
	return binary.LittleEndian.Uint32(data[(len(data)-4)/2-8:])
}

func dataChecksum(data []byte) (uint32, uint32) {
	checksum0 := binary.LittleEndian.Uint32(data[len(data)-4:])
	checksum1 := util.NewCRC(data[:len(data)-4]).Value()
	return checksum0, checksum1
}

func dataPrefixSlice(ns, prefix byte) *util.Range {
	return util.BytesPrefix([]byte{ns, prefix})
}

func dataNsSlice(ns byte) *util.Range {
	return util.BytesPrefix([]byte{ns})
}

type testingStorage struct {
	storage.Storage
}

func (ts *testingStorage) scanTable(fd storage.FileDesc, checksum bool) (corrupted bool, err error) {
	r, err := ts.Open(fd)
	if err != nil {
		return false, err
	}
	defer r.Close()

	size, err := r.Seek(0, os.SEEK_END)
	if err != nil {
		return false, err
	}

	o := &opt.Options{
		DisableLargeBatchTransaction: true,
		Strict:                       opt.NoStrict,
	}
	if checksum {
		o.Strict = opt.StrictBlockChecksum | opt.StrictReader
	}
	tr, err := table.NewReader(r, size, fd, nil, bpool, o)
	if err != nil {
		return false, err
	}
	defer tr.Release()

	checkData := func(i int, t string, data []byte) bool {
		if len(data) == 0 {
			panic(fmt.Sprintf("[%v] nil data: i=%d t=%s", fd, i, t))
		}

		checksum0, checksum1 := dataChecksum(data)
		if checksum0 != checksum1 {
			atomic.StoreUint32(&fail, 1)
			atomic.StoreUint32(&done, 1)
			corrupted = true

			data0, data1 := dataSplit(data)
			data0c0, data0c1 := dataChecksum(data0)
			data1c0, data1c1 := dataChecksum(data1)
			log.Printf("FATAL: [%v] Corrupted data i=%d t=%s (%#x != %#x): %x(%v) vs %x(%v)",
				fd, i, t, checksum0, checksum1, data0, data0c0 == data0c1, data1, data1c0 == data1c1)
			return true
		}
		return false
	}

	iter := tr.NewIterator(nil, nil)
	defer iter.Release()
	for i := 0; iter.Next(); i++ {
		ukey, _, kt, kerr := parseIkey(iter.Key())
		if kerr != nil {
			atomic.StoreUint32(&fail, 1)
			atomic.StoreUint32(&done, 1)
			corrupted = true

			log.Printf("FATAL: [%v] Corrupted ikey i=%d: %v", fd, i, kerr)
			return corrupted, nil
		}
		if checkData(i, "key", ukey) {
			return corrupted, nil
		}
		if kt == ktVal && checkData(i, "value", iter.Value()) {
			return corrupted, nil
		}
	}
	if err := iter.Error(); err != nil {
		if errors.IsCorrupted(err) {
			atomic.StoreUint32(&fail, 1)
			atomic.StoreUint32(&done, 1)
			corrupted = true

			log.Printf("FATAL: [%v] Corruption detected: %v", fd, err)
		} else {
			return false, err
		}
	}

	return corrupted, nil
}

func (ts *testingStorage) Remove(fd storage.FileDesc) error {
	if atomic.LoadUint32(&fail) == 1 {
		return nil
	}

	if fd.Type == storage.TypeTable {
		corrupted, err := ts.scanTable(fd, true)
		if err != nil {
			return err
		}
		if corrupted {
			return nil
		}
	}
	return ts.Storage.Remove(fd)
}

type latencyStats struct {
	mark          time.Time
	dur, min, max time.Duration
	num           int
}

func (s *latencyStats) start() {
	s.mark = time.Now()
}

func (s *latencyStats) record(n int) {
	if s.mark.IsZero() {
		panic("not started")
	}
	dur := time.Since(s.mark)
	dur1 := dur / time.Duration(n)
	if dur1 < s.min || s.min == 0 {
		s.min = dur1
	}
	if dur1 > s.max {
		s.max = dur1
	}
	s.dur += dur
	s.num += n
	s.mark = time.Time{}
}

func (s *latencyStats) ratePerSec() int {
	durSec := s.dur / time.Second
	if durSec > 0 {
		return s.num / int(durSec)
	}
	return s.num
}

func (s *latencyStats) avg() time.Duration {
	if s.num > 0 {
		return s.dur / time.Duration(s.num)
	}
	return 0
}

func (s *latencyStats) add(x *latencyStats) {
	if x.min < s.min || s.min == 0 {
		s.min = x.min
	}
	if x.max > s.max {
		s.max = x.max
	}
	s.dur += x.dur
	s.num += x.num
}

func main() {
	flag.Parse()

	if enableBufferPool {
		bpool = util.NewBufferPool(opt.DefaultBlockSize + 128)
	}

	log.Printf("Test DB stored at %q", dbPath)
	if httpProf != "" {
		log.Printf("HTTP pprof listening at %q", httpProf)
		runtime.SetBlockProfileRate(1)
		go func() {
			if err := http.ListenAndServe(httpProf, nil); err != nil {
				log.Fatalf("HTTPPROF: %v", err)
			}
		}()
	}

	runtime.GOMAXPROCS(runtime.NumCPU())

	os.RemoveAll(dbPath)
	stor, err := storage.OpenFile(dbPath, false)
	if err != nil {
		log.Fatal(err)
	}
	tstor := &testingStorage{stor}
	defer tstor.Close()

	fatalf := func(err error, format string, v ...interface{}) {
		atomic.StoreUint32(&fail, 1)
		atomic.StoreUint32(&done, 1)
		log.Printf("FATAL: "+format, v...)
		if err != nil && errors.IsCorrupted(err) {
			cerr := err.(*errors.ErrCorrupted)
			if !cerr.Fd.Zero() && cerr.Fd.Type == storage.TypeTable {
				log.Print("FATAL: corruption detected, scanning...")
				corrupted, serr := tstor.scanTable(storage.FileDesc{Type: storage.TypeTable, Num: cerr.Fd.Num}, false)
				if serr != nil {
					log.Printf("FATAL: unable to scan table %v", serr)
				} else if !corrupted {
					log.Printf("FATAL: unable to find corrupted key/value pair in table %v", cerr.Fd)
				}
			}
		}
		runtime.Goexit()
	}

	if openFilesCacheCapacity == 0 {
		openFilesCacheCapacity = -1
	}
	o := &opt.Options{
		OpenFilesCacheCapacity: openFilesCacheCapacity,
		DisableBufferPool:      !enableBufferPool,
		DisableBlockCache:      !enableBlockCache,
		ErrorIfExist:           true,
		Compression:            opt.NoCompression,
		Filter:                 filter.NewBloomFilter(10),
		MaxManifestFileSize:    maxManifestFileSize,
	}
	if enableCompression {
		o.Compression = opt.DefaultCompression
	}

	db, err := leveldb.Open(tstor, o)
	if err != nil {
		log.Fatal(err) // nolint: gocritic
	}
	defer db.Close()

	var (
		mu              = &sync.Mutex{}
		gGetStat        = &latencyStats{}
		gIterStat       = &latencyStats{}
		gWriteStat      = &latencyStats{}
		gTrasactionStat = &latencyStats{}
		startTime       = time.Now()

		writeReq    = make(chan *leveldb.Batch)
		writeAck    = make(chan error)
		writeAckAck = make(chan struct{})
	)

	go func() {
		for b := range writeReq {

			var err error
			if mrand.Float64() < transactionProb {
				log.Print("> Write using transaction")
				gTrasactionStat.start()
				var tr *leveldb.Transaction
				if tr, err = db.OpenTransaction(); err == nil {
					if err = tr.Write(b, nil); err == nil {
						if err = tr.Commit(); err == nil {
							gTrasactionStat.record(b.Len())
						}
					} else {
						tr.Discard()
					}
				}
			} else {
				gWriteStat.start()
				if err = db.Write(b, nil); err == nil {
					gWriteStat.record(b.Len())
				}
			}
			writeAck <- err
			<-writeAckAck
		}
	}()

	go func() {
		for {
			time.Sleep(3 * time.Second)

			log.Print("------------------------")

			log.Printf("> Elapsed=%v", time.Since(startTime))
			mu.Lock()
			log.Printf("> GetLatencyMin=%v GetLatencyMax=%v GetLatencyAvg=%v GetRatePerSec=%d",
				gGetStat.min, gGetStat.max, gGetStat.avg(), gGetStat.ratePerSec())
			log.Printf("> IterLatencyMin=%v IterLatencyMax=%v IterLatencyAvg=%v IterRatePerSec=%d",
				gIterStat.min, gIterStat.max, gIterStat.avg(), gIterStat.ratePerSec())
			log.Printf("> WriteLatencyMin=%v WriteLatencyMax=%v WriteLatencyAvg=%v WriteRatePerSec=%d",
				gWriteStat.min, gWriteStat.max, gWriteStat.avg(), gWriteStat.ratePerSec())
			log.Printf("> TransactionLatencyMin=%v TransactionLatencyMax=%v TransactionLatencyAvg=%v TransactionRatePerSec=%d",
				gTrasactionStat.min, gTrasactionStat.max, gTrasactionStat.avg(), gTrasactionStat.ratePerSec())
			mu.Unlock()

			cachedblock, _ := db.GetProperty("leveldb.cachedblock")
			openedtables, _ := db.GetProperty("leveldb.openedtables")
			alivesnaps, _ := db.GetProperty("leveldb.alivesnaps")
			aliveiters, _ := db.GetProperty("leveldb.aliveiters")
			blockpool, _ := db.GetProperty("leveldb.blockpool")
			writeDelay, _ := db.GetProperty("leveldb.writedelay")
			ioStats, _ := db.GetProperty("leveldb.iostats")
			compCount, _ := db.GetProperty("leveldb.compcount")
			log.Printf("> BlockCache=%s OpenedTables=%s AliveSnaps=%s AliveIter=%s BlockPool=%q WriteDelay=%q IOStats=%q CompCount=%q",
				cachedblock, openedtables, alivesnaps, aliveiters, blockpool, writeDelay, ioStats, compCount)
			log.Print("------------------------")
		}
	}()

	for ns, numKey := range numKeys {
		func(ns, numKey int) {
			log.Printf("[%02d] STARTING: numKey=%d", ns, numKey)

			keys := make([][]byte, numKey)
			for i := range keys {
				keys[i] = randomData(nil, byte(ns), 1, uint32(i), keyLen)
			}

			wg.Add(1)
			go func() {
				var wi uint32
				defer func() {
					log.Printf("[%02d] WRITER DONE #%d", ns, wi)
					wg.Done()
				}()

				var (
					b       = new(leveldb.Batch)
					k2, v2  []byte
					nReader int32
				)
				for atomic.LoadUint32(&done) == 0 {
					log.Printf("[%02d] WRITER #%d", ns, wi)

					b.Reset()
					for _, k1 := range keys {
						k2 = randomData(k2, byte(ns), 2, wi, keyLen)
						v2 = randomData(v2, byte(ns), 3, wi, valueLen)
						b.Put(k2, v2)
						b.Put(k1, k2)
					}
					writeReq <- b
					if err := <-writeAck; err != nil {
						writeAckAck <- struct{}{}
						fatalf(err, "[%02d] WRITER #%d db.Write: %v", ns, wi, err)
					}

					snap, err := db.GetSnapshot()
					if err != nil {
						writeAckAck <- struct{}{}
						fatalf(err, "[%02d] WRITER #%d db.GetSnapshot: %v", ns, wi, err)
					}

					writeAckAck <- struct{}{}

					wg.Add(1)
					atomic.AddInt32(&nReader, 1)
					go func(snapwi uint32, snap *leveldb.Snapshot) {
						var (
							ri       int
							iterStat = &latencyStats{}
							getStat  = &latencyStats{}
						)
						defer func() {
							mu.Lock()
							gGetStat.add(getStat)
							gIterStat.add(iterStat)
							mu.Unlock()

							atomic.AddInt32(&nReader, -1)
							log.Printf("[%02d] READER #%d.%d DONE Snap=%v Alive=%d IterLatency=%v GetLatency=%v", ns, snapwi, ri, snap, atomic.LoadInt32(&nReader), iterStat.avg(), getStat.avg())
							snap.Release()
							wg.Done()
						}()

						stopi := snapwi + 3
						for (ri < 3 || atomic.LoadUint32(&wi) < stopi) && atomic.LoadUint32(&done) == 0 {
							var n int
							iter := snap.NewIterator(dataPrefixSlice(byte(ns), 1), nil)
							iterStat.start()
							for iter.Next() {
								k1 := iter.Key()
								k2 := iter.Value()
								iterStat.record(1)

								if dataNS(k2) != byte(ns) {
									fatalf(nil, "[%02d] READER #%d.%d K%d invalid in-key NS: want=%d got=%d", ns, snapwi, ri, n, ns, dataNS(k2))
								}

								kwritei := dataI(k2)
								if kwritei != snapwi {
									fatalf(nil, "[%02d] READER #%d.%d K%d invalid in-key iter num: %d", ns, snapwi, ri, n, kwritei)
								}

								getStat.start()
								v2, err := snap.Get(k2, nil)
								if err != nil {
									fatalf(err, "[%02d] READER #%d.%d K%d snap.Get: %v\nk1: %x\n -> k2: %x", ns, snapwi, ri, n, err, k1, k2)
								}
								getStat.record(1)

								if checksum0, checksum1 := dataChecksum(v2); checksum0 != checksum1 {
									err := &errors.ErrCorrupted{Fd: storage.FileDesc{Type: 0xff, Num: 0}, Err: fmt.Errorf("v2: %x: checksum mismatch: %v vs %v", v2, checksum0, checksum1)}
									fatalf(err, "[%02d] READER #%d.%d K%d snap.Get: %v\nk1: %x\n -> k2: %x", ns, snapwi, ri, n, err, k1, k2)
								}

								n++
								iterStat.start()
							}
							iter.Release()
							if err := iter.Error(); err != nil {
								fatalf(err, "[%02d] READER #%d.%d K%d iter.Error: %v", ns, snapwi, ri, numKey, err)
							}
							if n != numKey {
								fatalf(nil, "[%02d] READER #%d.%d missing keys: want=%d got=%d", ns, snapwi, ri, numKey, n)
							}

							ri++
						}
					}(wi, snap)

					atomic.AddUint32(&wi, 1)
				}
			}()

			delB := new(leveldb.Batch)
			wg.Add(1)
			go func() {
				var (
					i        int
					iterStat = &latencyStats{}
				)
				defer func() {
					log.Printf("[%02d] SCANNER DONE #%d", ns, i)
					wg.Done()
				}()

				time.Sleep(2 * time.Second)

				for atomic.LoadUint32(&done) == 0 {
					var n int
					delB.Reset()
					iter := db.NewIterator(dataNsSlice(byte(ns)), nil)
					iterStat.start()
					for iter.Next() && atomic.LoadUint32(&done) == 0 {
						k := iter.Key()
						v := iter.Value()
						iterStat.record(1)

						for ci, x := range [...][]byte{k, v} {
							checksum0, checksum1 := dataChecksum(x)
							if checksum0 != checksum1 {
								if ci == 0 {
									fatalf(nil, "[%02d] SCANNER %d.%d invalid key checksum: want %d, got %d\n%x -> %x", ns, i, n, checksum0, checksum1, k, v)
								} else {
									fatalf(nil, "[%02d] SCANNER %d.%d invalid value checksum: want %d, got %d\n%x -> %x", ns, i, n, checksum0, checksum1, k, v)
								}
							}
						}

						if dataPrefix(k) == 2 || mrand.Int()%999 == 0 {
							delB.Delete(k)
						}

						n++
						iterStat.start()
					}
					iter.Release()
					if err := iter.Error(); err != nil {
						fatalf(err, "[%02d] SCANNER #%d.%d iter.Error: %v", ns, i, n, err)
					}

					if n > 0 {
						log.Printf("[%02d] SCANNER #%d IterLatency=%v", ns, i, iterStat.avg())
					}

					if delB.Len() > 0 && atomic.LoadUint32(&done) == 0 {
						t := time.Now()
						writeReq <- delB
						if err := <-writeAck; err != nil {
							writeAckAck <- struct{}{}
							fatalf(err, "[%02d] SCANNER #%d db.Write: %v", ns, i, err)
						} else {
							writeAckAck <- struct{}{}
						}
						log.Printf("[%02d] SCANNER #%d Deleted=%d Time=%v", ns, i, delB.Len(), time.Since(t))
					}

					i++
				}
			}()
		}(ns, numKey)
	}

	go func() {
		sig := make(chan os.Signal, 1)
		signal.Notify(sig, os.Interrupt, syscall.SIGTERM)
		log.Printf("Got signal: %v, exiting...", <-sig)
		atomic.StoreUint32(&done, 1)
	}()

	wg.Wait()
}
```

## File: `manualtest/filelock/main.go`
```go
package main

import (
	"bufio"
	"bytes"
	"flag"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"

	"github.com/syndtr/goleveldb/leveldb/storage"
)

var (
	filename string
	child    bool
)

func init() {
	flag.StringVar(&filename, "filename", filepath.Join(os.TempDir(), "goleveldb_filelock_test"), "Filename used for testing")
	flag.BoolVar(&child, "child", false, "This is the child")
}

func runChild() error {
	var args []string
	args = append(args, os.Args[1:]...)
	args = append(args, "-child")
	cmd := exec.Command(os.Args[0], args...)
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	r := bufio.NewReader(&out)
	for {
		line, _, e1 := r.ReadLine()
		if e1 != nil {
			break
		}
		fmt.Println("[Child]", string(line))
	}
	return err
}

func main() {
	flag.Parse()

	fmt.Printf("Using path: %s\n", filename)
	if child {
		fmt.Println("Child flag set.")
	}

	stor, err := storage.OpenFile(filename, false)
	if err != nil {
		fmt.Printf("Could not open storage: %s", err)
		os.Exit(10)
	}

	if !child {
		fmt.Println("Executing child -- first test (expecting error)")
		err := runChild()
		if err == nil {
			fmt.Println("Expecting error from child")
		} else if err.Error() != "exit status 10" {
			fmt.Println("Got unexpected error from child:", err)
		} else {
			fmt.Printf("Got error from child: %s (expected)\n", err)
		}
	}

	err = stor.Close()
	if err != nil {
		fmt.Printf("Error when closing storage: %s", err)
		os.Exit(11)
	}

	if !child {
		fmt.Println("Executing child -- second test")
		err := runChild()
		if err != nil {
			fmt.Println("Got unexpected error from child:", err)
		}
	}

	os.RemoveAll(filename)
}
```

