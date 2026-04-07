---
id: qsv-lookup-tables
type: knowledge
owner: OA_Triage
---
# qsv-lookup-tables
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# qsv-lookup-tables

A repository of common lookup tables that can be used with [qsv](https://github.com/jqnatividad/qsv#qsv-ultra-fast-csv-data-wrangling-toolkit)'s [`luau`](https://github.com/jqnatividad/qsv#luau_deeplink) command's `qsv_register_lookup` helper function.

Please feel free to submit a pull request to add more lookup tables.

## Usage

To use a lookup table, simply use the name of the csv you want to use with the [`qsv_register_lookup`](https://github.com/jqnatividad/qsv/blob/b8fded6b41c4b31f0f257a0fa1513a921e035e7a/src/cmd/luau.rs#L1349-L1368) helper using the "dathere://" scheme.

```lua
us_states_lookup_headers = qsv_register_lookup("us_states", "dathere://us-states-example.csv")
```

The first argument is the name of the lookup table to download the data to. The second argument is the dathere URL of the CSV file in the [`lookup-tables`](https://github.com/dathere/qsv-lookup-tables/tree/main/lookup-tables) directory.

When the lookup table is downloaded sucessfully, a Luau table is created with the same name as the first argument ("us_states" in this case). The table is a two-dimensional Luau table, where the first dimension is the value of the first column of the CSV file (the lookup key), and the second dimension are the rest of the columns with their data.

Further, qsv_register_lookup returns the header names of the CSV file as another Luau table ("us_states_lookup_headers" in this example), which can be used to access the data in the lookup table.

### Example

We have a small table with some transactions for which we want to get the total amount with the corresponding state sales tax.   
(source code: [testlookup.luau](examples/readme-example/testlookup.luau), data: [data.csv](examples/readme-example/data.csv))

#### data.csv

```csv
Order ID,Amount,State
20230301001,13.50,NJ
20230301002,15.00,NY
20230301003,72.00,TX
20230301004,12.00,CA
20230301005,33.70,DE
```

#### [us-states-example.csv](https://github.com/dathere/qsv-lookup-tables/blob/main/lookup-tables/us-states-example.csv) lookup table

```csv
 Abbreviation,Name,Capital,Population (2019),area (square miles),Sales Tax (2023)
 AL,Alabama,Montgomery ,"4,903,185","52,420",4
 AK,Alaska,Juneau,"731,545","665,384",0
 AZ,Arizona,Phoenix,"7,278,717","113,990",5.6
 AR,Arkansas,Little Rock,"3,017,804","53,179",6.5
 CA,California,Sacramento,"39,512,223","163,695",7.5
 ...
 WV,West Virginia,Charleston,"1,792,147,24,230",6
 WI,Wisconsin,Madison,"5,822,434,65,496",5
 WY,Wyoming,Cheyenne,"578,759,97,813",4
```

#### testlookup.luau

```lua
BEGIN {
    -- this is the BEGIN block, which is executed ONCE at the beginning
    -- we typically use it to initialize variables, load lookup tables and setup functions
    running_total = 0;
    running_total_after_tax = 0;
    amount_table = {};
    amount_table_with_salestax = {};

    -- we use the "dathere://" scheme to load "us-states-example.csv" from the
    -- https://github.com/dathere/qsv-lookup-tables repository
    -- 6000 is the cache TTL in seconds (10 minutes)
    us_states_lookup_headers_table = qsv_register_lookup("us_states",
       "dathere://us-states-example.csv", 6000)

    -- note how we use the qsv_log function to log to the qsv log file
    -- which you can enable by setting the QSV_LOG_LEVEL environment variable to "debug"
    -- e.g. `export QSV_LOG_LEVEL=debug`
    qsv_log("debug", "us_states_lookup_headers:", us_states_lookup_headers_table)
    qsv_log("info", "us_states lookup table:", us_states)
    qsv_log("info", 
      `NY Capital: {us_states["NY"]["Capital"]} can be also {us_states.NY.Capital} or {us_states["NY"].Capital}`)

    -- a simple function to sum a table of numbers
    function sum(numbers_table: table): number
        local sum: number = 0;
        for _, v in ipairs(numbers_table) do
            sum = sum + v;
        end
        return sum;
    end
    
}!


----------------------------------------------------------------------------
-- this is the MAIN script loop, which is executed ONCE for each row in order

-- note the different ways we can access the columns of the current row
-- "Amount", the 2nd column and "State", the 3rd column in the lookup table
local amount_with_salestax: number = Amount + col[2] * (us_states[col["State"]]["Sales Tax (2023)"] / 100);
amount_with_salestax = col["Amount"] + col.Amount * (us_states[col.State]["Sales Tax (2023)"] / 100);
amount_with_salestax = col.Amount + Amount * (us_states[State]["Sales Tax (2023)"] / 100);

local Rate: number = us_states[State]["Sales Tax (2023)"];

-- _IDX is the current row index. We use it to store the amount_with_salestax in the amount_array
amount_table[_IDX] = Amount;
amount_table_with_salestax[_IDX] = amount_with_salestax;
running_total = running_total + Amount;
running_total_after_tax = running_total_after_tax + amount_with_salestax;

-- we round using Lua's powerful String library - https://luau-lang.org/library#string-library
running_total = string.format("%.2f", running_total);
local rounded_running_total_after_tax = string.format("%.2f", running_total_after_tax);

-- we return multiple values, which are "mapped" to the columns specified in the qsv command
return {Rate, amount_with_salestax, running_total, rounded_running_total_after_tax};


----------------------------------------------------------------------------
END {
    -- and this is the END block, which is executed ONCE at the end

    -- first we use Lua's table library to unpack the contents of the amount_table into a list
    -- https://luau-lang.org/library#table-library
    -- and then we use the builtin math library - https://luau-lang.org/library#math-library
    -- to get the min and max values
    local min_amount: number = math.min(table.unpack(amount_table_with_salestax));
    local max_amount: number = math.max(table.unpack(amount_table_with_salestax));
    qsv_log("debug", `min_amount: {min_amount} max_amount: {max_amount}`)

    -- and here, we use our own sum function
    local grand_total_with_salestax = string.format("%.2f",sum(amount_table_with_salestax));
    local grand_total = string.format("%.2f",sum(amount_table));

    -- this message is returned to stderr
    -- _ROWCOUNT is a special variable that is set to the number of rows processed
    -- without an index, it is zero until we reach the END block
    return `Min/Max: {min_amount}/{max_amount} Grand total of {_ROWCOUNT} rows: {grand_total}/{grand_total_with_salestax}`;
}!
```

To run the example, issue the following commands:

```bash
export QSV_LOG_LEVEL=debug
qsv luau map "Rate (%)","Amount with Tax","Running Total - Before Tax","Running Total - After Tax" \
    file:testlookup.luau --colindex data.csv | qsv table
```

And here's the output after running. The first line is the output of the `return` statement in the END block sent to stderr.
The rest is the output sent to stdout and piped to `qsv table` to format it as a table.

```bash
Min/Max: 12.9/76.5 Grand total of 5 rows: 146.20/153.15
Order_ID     Amount  State  Rate (%)  Amount with Tax  Running Total - Before Tax  Running Total - After Tax
20230301001  13.50   NJ     7         14.445           13.50                       14.45
20230301002  15.00   NY     4         15.6             28.50                       30.05
20230301003  72.00   TX     6.25      76.5             100.50                      106.55
20230301004  12.00   CA     7.5       12.9             112.50                      119.45
20230301005  33.70   DE     0         33.7             146.20                      153.15
```

And the logfile should look like this:

#### [qsv_rCURRENT.log](examples/readme-example/qsv_rCURRENT.log)

```SystemVerilog
[2023-03-16 10:09:07.521653 +00:00] INFO [qsv::util] src/util.rs:617: START: luau map Rate (%),Amount with Tax,Running Total - Before Tax,Running Total - After Tax -x file:testlookup.luau testme.csv
[2023-03-16 10:09:07.539190 +00:00] INFO [qsv::cmd::luau] src/cmd/luau.rs:240: TIMEOUT: 15 secs
[2023-03-16 10:09:07.540808 +00:00] DEBUG [qsv::cmd::luau] src/cmd/luau.rs:276: begin_block_replace: "BEGIN {\n\n    running_total = 0;\n    running_total_after_tax = 0;\n    amount_table = {};\n    amount_table_with_salestax = {};\n\n    us_states_lookup_headers_table = qsv_register_lookup(\"us_states\", \"dathere://us-states-example.csv\")\n\n    qsv_log(\"debug\", \"us_states_lookup_headers:\", us_states_lookup_headers_table)\n    qsv_log(\"info\", \"us_states lookup table:\", us_states)\n    qsv_log(\"info\", `NY Capital: {us_states[\"NY\"][\"Capital\"]} can be also {us_states.NY.Capital} or {us_states[\"NY\"].Capital}`)\n\n    function sum(numbers_table: table): number\n        local sum: number = 0;\n        for _, v in ipairs(numbers_table) do\n            sum = sum + v;\n        end\n        return sum;\n    end\n    \n}!"
[2023-03-16 10:09:07.541500 +00:00] DEBUG [qsv::cmd::luau] src/cmd/luau.rs:293: MAIN script: "local amount_with_salestax: number = Amount + col[2] * (us_states[col[\"State\"]][\"Sales Tax (2023)\"] / 100);\namount_with_salestax = col[\"Amount\"] + col.Amount * (us_states[col.State][\"Sales Tax (2023)\"] / 100);\namount_with_salestax = col.Amount + Amount * (us_states[State][\"Sales Tax (2023)\"] / 100);\n\nlocal Rate: number = us_states[State][\"Sales Tax (2023)\"];\n\namount_table[_IDX] = Amount;\namount_table_with_salestax[_IDX] = amount_with_salestax;\nrunning_total = running_total + Amount;\nrunning_total_after_tax = running_total_after_tax + amount_with_salestax;\n\nrunning_total = string.format(\"%.2f\", running_total);\nlocal rounded_running_total_after_tax = string.format(\"%.2f\", running_total_after_tax);\n\nreturn {Rate, amount_with_salestax, running_total, rounded_running_total_after_tax};"
[2023-03-16 10:09:07.541531 +00:00] DEBUG [qsv::cmd::luau] src/cmd/luau.rs:315: BEGIN script: "running_total = 0;\n    running_total_after_tax = 0;\n    amount_table = {};\n    amount_table_with_salestax = {};\n\n    us_states_lookup_headers_table = qsv_register_lookup(\"us_states\", \"dathere://us-states-example.csv\")\n\n    qsv_log(\"debug\", \"us_states_lookup_headers:\", us_states_lookup_headers_table)\n    qsv_log(\"info\", \"us_states lookup table:\", us_states)\n    qsv_log(\"info\", `NY Capital: {us_states[\"NY\"][\"Capital\"]} can be also {us_states.NY.Capital} or {us_states[\"NY\"].Capital}`)\n\n    function sum(numbers_table: table): number\n        local sum: number = 0;\n        for _, v in ipairs(numbers_table) do\n            sum = sum + v;\n        end\n        return sum;\n    end"
[2023-03-16 10:09:07.541559 +00:00] DEBUG [qsv::cmd::luau] src/cmd/luau.rs:336: END script: "local min_amount: number = math.min(table.unpack(amount_table_with_salestax));\n    local max_amount: number = math.max(table.unpack(amount_table_with_salestax));\n    qsv_log(\"debug\", `min_amount: {min_amount} max_amount: {max_amount}`)\n\n    local grand_total_with_salestax = string.format(\"%.2f\",sum(amount_table_with_salestax));\n    local grand_total = string.format(\"%.2f\",sum(amount_table));\n\n    return `Min/Max: {min_amount}/{max_amount} Grand total of {_ROWCOUNT} rows: {grand_total}/{grand_total_with_salestax}`;"
[2023-03-16 10:09:07.541936 +00:00] INFO [qsv::cmd::luau] src/cmd/luau.rs:488: Compiling and executing BEGIN script.
[2023-03-16 10:09:07.542892 +00:00] DEBUG [reqwest::connect] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/reqwest-0.11.14/src/connect.rs:429: starting new connection: https://raw.githubusercontent.com/
[2023-03-16 10:09:07.543139 +00:00] DEBUG [hyper::client::connect::dns] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/hyper-0.14.25/src/client/connect/dns.rs:122: resolving host="raw.githubusercontent.com"
[2023-03-16 10:09:07.545048 +00:00] DEBUG [hyper::client::connect::http] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/hyper-0.14.25/src/client/connect/http.rs:537: connecting to [2606:50c0:8001::154]:443
[2023-03-16 10:09:07.556831 +00:00] DEBUG [hyper::client::connect::http] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/hyper-0.14.25/src/client/connect/http.rs:540: connected to [2606:50c0:8001::154]:443
[2023-03-16 10:09:07.556898 +00:00] DEBUG [rustls::client::hs] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/rustls-0.20.8/src/client/hs.rs:55: No cached session for DnsName(DnsName(DnsName("raw.githubusercontent.com")))
[2023-03-16 10:09:07.557035 +00:00] DEBUG [rustls::client::hs] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/rustls-0.20.8/src/client/hs.rs:127: Not resuming any session
[2023-03-16 10:09:07.570430 +00:00] DEBUG [rustls::client::hs] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/rustls-0.20.8/src/client/hs.rs:583: Using ciphersuite TLS13_AES_128_GCM_SHA256
[2023-03-16 10:09:07.570457 +00:00] DEBUG [rustls::client::tls13] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/rustls-0.20.8/src/client/tls13.rs:130: Not resuming
[2023-03-16 10:09:07.570728 +00:00] DEBUG [rustls::client::tls13] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/rustls-0.20.8/src/client/tls13.rs:395: TLS1.3 encrypted extensions: [ServerNameAck, Protocols([6832])]
[2023-03-16 10:09:07.570749 +00:00] DEBUG [rustls::client::hs] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/rustls-0.20.8/src/client/hs.rs:452: ALPN protocol is Some(b"h2")
[2023-03-16 10:09:07.571040 +00:00] DEBUG [rustls::client::tls13] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/rustls-0.20.8/src/client/tls13.rs:1050: Ticket saved
[2023-03-16 10:09:07.571101 +00:00] DEBUG [h2::client] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/h2-0.3.16/src/client.rs:1167: binding client connection
[2023-03-16 10:09:07.571141 +00:00] DEBUG [h2::client] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/h2-0.3.16/src/client.rs:1172: client connection bound
[2023-03-16 10:09:07.571175 +00:00] DEBUG [h2::codec::framed_write] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/h2-0.3.16/src/codec/framed_write.rs:232: send frame=Settings { flags: (0x0), enable_push: 0, initial_window_size: 65535, max_frame_size: 16384 }
[2023-03-16 10:09:07.571210 +00:00] DEBUG [h2::proto::connection] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/h2-0.3.16/src/proto/connection.rs:138: Connection; peer=Client
[2023-03-16 10:09:07.571321 +00:00] DEBUG [hyper::client::pool] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/hyper-0.14.25/src/client/pool.rs:376: pooling idle connection for ("https", raw.githubusercontent.com)
[2023-03-16 10:09:07.571418 +00:00] DEBUG [h2::codec::framed_write] /Users/johnsmith/.cargo/registry/src/github.com-djkasdjag90849231/h2-0.3.16/src/codec/framed_write.rs:232: send frame=Headers { stream_id: StreamId(1), flags: (0x5: END_HEADERS | END_STREAM) }
[2023-03-16 10:09:07.594966 +00:00] DEBUG [h2::codec::framed_
... [TRUNCATED]
```

