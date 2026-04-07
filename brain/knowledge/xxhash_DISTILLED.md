---
id: xxhash
type: knowledge
owner: OA_Triage
---
# xxhash
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# xxhash-rust

[![Rust](https://github.com/DoumanAsh/xxhash-rust/actions/workflows/rust.yml/badge.svg)](https://github.com/DoumanAsh/xxhash-rust/actions/workflows/rust.yml)
[![Crates.io](https://img.shields.io/crates/v/xxhash-rust.svg)](https://crates.io/crates/xxhash-rust)
[![Documentation](https://docs.rs/xxhash-rust/badge.svg)](https://docs.rs/crate/xxhash-rust/)

Implementation of [xxHash](https://github.com/Cyan4973/xxHash) in Rust

Each algorithm is implemented via feature, allowing precise control over code size.

## Example

- Cargo.toml

```toml
[dependencies.xxhash-rust]
version = "0.8.12"
features = ["xxh3", "const_xxh3"]
```

- main.rs

```rust
use xxhash_rust::const_xxh3::xxh3_64 as const_xxh3;
use xxhash_rust::xxh3::xxh3_64;

const TEST: u64 = const_xxh3(b"TEST");

fn test_input(text: &str) -> bool {
    xxh3_64(text.as_bytes()) == TEST
}

assert!(!test_input("tEST"));
assert!(test_input("TEST"));
```

## Features:

By default all features are off.

- `std` - Enables `std::io::Write` trait implementation
- `xxh32` - Enables 32bit algorithm. Suitable for x86 targets
- `const_xxh32` - `const fn` version of `xxh32` algorithm
- `xxh64` - Enables 64 algorithm. Suitable for x86_64 targets
- `const_xxh64` - `const fn` version of `xxh64` algorithm
- `xxh3` - Enables `xxh3` family of algorithms, superior to `xxh32` and `xxh64` in terms of performance.
- `const_xxh3` - `const fn` version of `xxh3` algorithm

## HW acceleration

Similar to reference implementation, crate implements various SIMDs in `xxh3` depending on provided flags.
All checks are performed only at compile time, hence user is encouraged to enable these accelerations (for example via `-C target_cpu=native`)

Used SIMD acceleration:

- SSE2 - widely available, can be safely enabled in 99% of cases. Enabled by default in `x86_64` targets.
- AVX2;
- AVX512;
- Neon - Enabled by default on aarch64 targets (most likely)
- Wasm SIMD128 - Has to be enabled via rust flag: `-Ctarget-feature=+simd128`

## Streaming vs One-shot

For performance reasons one-shot version of algorithm does not re-use streaming version.
Unless needed, user is advised to use one-shot version which tends to be more optimal.

## `const fn` version

While `const fn` provides compile time implementation, it does so at performance cost.
Hence you should only use it at _compile_ time.

To guarantee that something is computed at compile time make sure to initialize hash output
as `const` or `static` variable, otherwise it is possible function is executed at runtime, which
would be worse than regular algorithm.

`const fn` is implemented in best possible way while conforming to limitations of Rust `const
fn`, but these limitations are quite strict making any high performance code impossible.

## Version note

- `0.8.*` corresponds to C's `0.8.*`

In order to  keep up with original implementation version I'm not planning to bump major/minor until C implementation does so.

```

### File: .rust-analyzer.json
```json
{
    "cargo": {
        "features": [
            "xxh32",
            "const_xxh32",
            "xxh64",
            "const_xxh64",
            "xxh3",
            "const_xxh3"
        ]
    }
}

```

### File: src\const_xxh3.rs
```rs
//!Xxh3 `const fn` implementation
//!
//!This module is efficient only when hashes are guaranteed to be executed at compile time.
//!At runtime algorithm is written in fairly inefficient code, although still fast enough.

use core::mem;

use crate::xxh32_common as xxh32;
use crate::xxh64_common as xxh64;
use crate::xxh3_common::*;

const INITIAL_ACC: [u64; ACC_NB] = [
    xxh32::PRIME_3 as u64, xxh64::PRIME_1, xxh64::PRIME_2, xxh64::PRIME_3,
    xxh64::PRIME_4, xxh32::PRIME_2 as u64, xxh64::PRIME_5, xxh32::PRIME_1 as u64
];

#[inline(always)]
const fn read_u32(input: &[u8], cursor: usize) -> u32 {
    input[cursor] as u32 | (input[cursor + 1] as u32) << 8 | (input[cursor + 2] as u32) << 16 | (input[cursor + 3] as u32) << 24
}


#[inline(always)]
const fn read_u64(input: &[u8], cursor: usize) -> u64 {
    input[cursor] as u64
        | (input[cursor + 1] as u64) << 8
        | (input[cursor + 2] as u64) << 16
        | (input[cursor + 3] as u64) << 24
        | (input[cursor + 4] as u64) << 32
        | (input[cursor + 5] as u64) << 40
        | (input[cursor + 6] as u64) << 48
        | (input[cursor + 7] as u64) << 56
}

#[inline(always)]
const fn mult32_to64(left: u32, right: u32) -> u64 {
    (left as u64).wrapping_mul(right as u64)
}

#[inline]
const fn mix16_b(input: &[u8], input_offset: usize, secret: &[u8], secret_offset: usize, seed: u64) -> u64 {
    let mut input_lo = read_u64(input, input_offset);
    let mut input_hi = read_u64(input, input_offset + 8);

    input_lo ^= read_u64(secret, secret_offset).wrapping_add(seed);
    input_hi ^= read_u64(secret, secret_offset + 8).wrapping_sub(seed);

    mul128_fold64(input_lo, input_hi)
}

#[allow(clippy::too_many_arguments)]
#[inline]
const fn mix32_b(mut acc: (u64, u64), input_1: &[u8], input_1_off: usize, input_2: &[u8], input_2_off: usize, secret: &[u8], secret_offset: usize, seed: u64) -> (u64, u64) {
    acc.0 = acc.0.wrapping_add(mix16_b(input_1, input_1_off, secret, secret_offset, seed));
    acc.0 ^= read_u64(input_2, input_2_off).wrapping_add(read_u64(input_2, input_2_off + 8));

    acc.1 = acc.1.wrapping_add(mix16_b(input_2, input_2_off, secret, secret_offset + 16, seed));
    acc.1 ^= read_u64(input_1, input_1_off).wrapping_add(read_u64(input_1, input_1_off + 8));

    acc
}

#[inline(always)]
const fn xxh3_64_9to16(input: &[u8], seed: u64, secret: &[u8]) -> u64 {
    let flip1 = (read_u64(secret, 24) ^ read_u64(secret, 32)).wrapping_add(seed);
    let flip2 = (read_u64(secret, 40) ^ read_u64(secret, 48)).wrapping_sub(seed);

    let input_lo = read_u64(input, 0) ^ flip1;
    let input_hi = read_u64(input, input.len() - 8) ^ flip2;

    let acc = (input.len() as u64).wrapping_add(input_lo.swap_bytes())
                                  .wrapping_add(input_hi)
                                  .wrapping_add(mul128_fold64(input_lo, input_hi));

    avalanche(acc)
}

#[inline(always)]
const fn xxh3_64_4to8(input: &[u8], mut seed: u64, secret: &[u8]) -> u64 {
    seed ^= ((seed as u32).swap_bytes() as u64) << 32;

    let input1 = read_u32(input, 0);
    let input2 = read_u32(input, input.len() - 4);

    let flip = (read_u64(secret, 8) ^ read_u64(secret, 16)).wrapping_sub(seed);
    let input64 = (input2 as u64).wrapping_add((input1 as u64) << 32);
    let keyed = input64 ^ flip;

    strong_avalanche(keyed, input.len() as u64)
}

#[inline(always)]
const fn xxh3_64_1to3(input: &[u8], seed: u64, secret: &[u8]) -> u64 {
    let combo = ((input[0] as u32) << 16)
                | ((input[input.len() >> 1] as u32) << 24)
                | (input[input.len() - 1] as u32)
                | ((input.len() as u32) << 8);


    let flip = ((read_u32(secret, 0) ^ read_u32(secret, 4)) as u64).wrapping_add(seed);
    xxh64::avalanche((combo as u64) ^ flip)
}

#[inline(always)]
const fn xxh3_64_0to16(input: &[u8], seed: u64, secret: &[u8]) -> u64 {
    if input.len() > 8 {
        xxh3_64_9to16(input, seed, secret)
    } else if input.len() >= 4 {
        xxh3_64_4to8(input, seed, secret)
    } else if input.len() > 0 {
        xxh3_64_1to3(input, seed, secret)
    } else {
        xxh64::avalanche(seed ^ read_u64(secret, 56) ^ read_u64(secret, 64))
    }
}

#[inline(always)]
const fn xxh3_64_7to128(input: &[u8], seed: u64, secret: &[u8]) -> u64 {
    let mut acc = (input.len() as u64).wrapping_mul(xxh64::PRIME_1);

    if input.len() > 32 {
        if input.len() > 64 {
            if input.len() > 96 {
                acc = acc.wrapping_add(mix16_b(input, 48, secret, 96, seed));
                acc = acc.wrapping_add(mix16_b(input, input.len()-64, secret, 112, seed));
            }

            acc = acc.wrapping_add(mix16_b(input, 32, secret, 64, seed));
            acc = acc.wrapping_add(mix16_b(input, input.len()-48, secret, 80, seed));
        }

        acc = acc.wrapping_add(mix16_b(input, 16, secret, 32, seed));
        acc = acc.wrapping_add(mix16_b(input, input.len()-32, secret, 48, seed));
    }

    acc = acc.wrapping_add(mix16_b(input, 0, secret, 0, seed));
    acc = acc.wrapping_add(mix16_b(input, input.len()-16, secret, 16, seed));

    avalanche(acc)
}

const fn xxh3_64_129to240(input: &[u8], seed: u64, secret: &[u8]) -> u64 {
    const START_OFFSET: usize = 3;
    const LAST_OFFSET: usize = 17;

    let mut acc = (input.len() as u64).wrapping_mul(xxh64::PRIME_1);
    let nb_rounds = input.len() / 16;

    let mut idx = 0;
    while idx < 8 {
        acc = acc.wrapping_add(mix16_b(input, 16*idx, secret, 16*idx, seed));
        idx += 1;
    }
    acc = avalanche(acc);

    while idx < nb_rounds {
        acc = acc.wrapping_add(mix16_b(input, 16*idx, secret, 16*(idx-8)+START_OFFSET, seed));
        idx += 1;
    }

    acc = acc.wrapping_add(mix16_b(input, input.len()-16, secret, SECRET_SIZE_MIN-LAST_OFFSET, seed));

    avalanche(acc)
}

#[inline(always)]
const fn mix_two_accs(acc: &[u64], acc_offset: usize, secret: &[u8], secret_offset: usize) -> u64 {
    mul128_fold64(acc[acc_offset] ^ read_u64(secret, secret_offset),
                  acc[acc_offset + 1] ^ read_u64(secret, secret_offset + 8))
}

#[inline]
const fn merge_accs(acc: &[u64], secret: &[u8], secret_offset: usize, mut result: u64) -> u64 {
    let mut idx = 0;
    while idx < 4 {
        result = result.wrapping_add(mix_two_accs(acc, idx * 2, secret, secret_offset + idx * 16));
        idx += 1;
    }

    avalanche(result)
}

const fn scramble_acc(mut acc: [u64; ACC_NB], secret: &[u8], secret_offset: usize) -> [u64; ACC_NB] {
    let mut idx = 0;

    while idx < ACC_NB {
        let key = read_u64(secret, secret_offset + 8 * idx);
        let mut acc_val = xorshift64(acc[idx], 47);
        acc_val ^= key;
        acc[idx] = acc_val.wrapping_mul(xxh32::PRIME_1 as u64);

        idx += 1;
    }

    acc
}

const fn accumulate_512(mut acc: [u64; ACC_NB], input: &[u8], input_offset: usize, secret: &[u8], secret_offset: usize) -> [u64; ACC_NB] {
    let mut idx = 0;
    while idx < ACC_NB {
        let data_val = read_u64(input, input_offset + 8 * idx);
        let data_key = data_val ^ read_u64(secret, secret_offset + 8 * idx);

        acc[idx ^ 1] = acc[idx ^ 1].wrapping_add(data_val);
        acc[idx] = acc[idx].wrapping_add(mult32_to64((data_key & 0xFFFFFFFF) as u32, (data_key >> 32) as u32));

        idx += 1;
    }

    acc
}

#[inline(always)]
const fn accumulate_loop(mut acc: [u64; ACC_NB], input: &[u8], input_offset: usize, secret: &[u8], secret_offset: usize, nb_stripes: usize) -> [u64; ACC_NB] {
    let mut idx = 0;
    while idx < nb_stripes {
        acc = accumulate_512(acc, input, input_offset + idx * STRIPE_LEN, secret, secret_offset + idx * SECRET_CONSUME_RATE);

        idx += 1;
    }

    acc
}

#[inline]
const fn hash_long_internal_loop(input: &[u8], secret: &[u8]) -> [u64; ACC_NB] {
    let mut acc = INITIAL_ACC;

    let nb_stripes = (secret.len() - STRIPE_LEN) / SECRET_CONSUME_RATE;
    let block_len = STRIPE_LEN * nb_stripes;
    let nb_blocks = (input.len() - 1) / block_len;

    let mut idx = 0;
    while idx < nb_blocks {
        acc = accumulate_loop(acc, input, idx * block_len, secret, 0, nb_stripes);
        acc = scramble_acc(acc, secret, secret.len() - STRIPE_LEN);

        idx += 1;
    }

    let nb_stripes = ((input.len() - 1) - (block_len * nb_blocks)) / STRIPE_LEN;

    acc = accumulate_loop(acc, input, nb_blocks * block_len, secret, 0, nb_stripes);
    accumulate_512(acc, input, input.len() - STRIPE_LEN, secret, secret.len() - STRIPE_LEN - SECRET_LASTACC_START)
}

const fn xxh3_64_long_impl(input: &[u8], secret: &[u8]) -> u64 {
    let acc = hash_long_internal_loop(input, secret);

    merge_accs(&acc, secret, SECRET_MERGEACCS_START, (input.len() as u64).wrapping_mul(xxh64::PRIME_1))
}

#[inline(always)]
///Returns 64bit hash for provided input.
pub const fn xxh3_64(input: &[u8]) -> u64 {
    xxh3_64_with_seed(input, 0)
}

///Returns 64bit hash for provided input using seed.
pub const fn xxh3_64_with_seed(input: &[u8], seed: u64) -> u64 {
    if input.len() <= 16 {
        xxh3_64_0to16(input, seed, &DEFAULT_SECRET)
    } else if input.len() <= 128 {
        xxh3_64_7to128(input, seed, &DEFAULT_SECRET)
    } else if input.len() <= MID_SIZE_MAX {
        xxh3_64_129to240(input, seed, &DEFAULT_SECRET)
    } else {
        xxh3_64_long_impl(input, &const_custom_default_secret(seed))
    }
}

///Returns 64bit hash for provided input using custom secret.
pub const fn xxh3_64_with_secret(input: &[u8], secret: &[u8; DEFAULT_SECRET_SIZE]) -> u64 {
    if input.len() <= 16 {
        xxh3_64_0to16(input, 0, secret)
    } else if input.len() <= 128 {
        xxh3_64_7to128(input, 0, secret)
    } else if input.len() <= MID_SIZE_MAX {
        xxh3_64_129to240(input, 0, secret)
    } else {
        xxh3_64_long_impl(input, secret)
    }
}

//
//128bit
//

#[inline(always)]
const fn xxh3_128_1to3(input: &[u8], seed: u64, secret: &[u8]) -> u128 {
    let c1 = input[0];
    let c2 = input[input.len() >> 1];
    let c3 = input[input.len() - 1];
    let input_lo = (c1 as u32) << 16 | (c2 as u32) << 24 | c3 as u32 | (input.len() as u32) << 8;
    let input_hi = input_lo.swap_bytes().rotate_left(13);

    let flip_lo = (read_u32(secret, 0) as u64 ^ read_u32(secret, 4) as u64).wrapping_add(seed);
    let flip_hi = (read_u32(secret, 8) as u64 ^ read_u32(secret, 12) as u64).wrapping_sub(seed);
    let keyed_lo = input_lo as u64 ^ flip_lo;
    let keyed_hi = input_hi as u64 ^ flip_hi;

    xxh64::avalanche(keyed_lo) as u128 | (xxh64::avalanche(keyed_hi) as u128) << 64
}

#[inline(always)]
const fn xxh3_128_4to8(input: &[u8], mut seed: u64, secret: &[u8]) -> u128 {
    seed ^= ((seed as u32).swap_bytes() as u64) << 32;

    let lo = read_u32(input, 0);
    let hi = read_u32(input, input.len() - 4);
    let input_64 = (lo as u64).wrapping_add((hi as u64) << 32);

    let flip = (read_u64(secret, 16) ^ read_u64(secret, 24)).wrapping_add(seed);
    let keyed = input_64 ^ flip;

    let (mut lo, mut hi) = mul64_to128(keyed, xxh64::PRIME_1.wrapping_add((input.len() as u64) << 2));

    hi = hi.wrapping_add(lo << 1);
    lo ^= hi >> 3;

    lo = xorshift64(lo, 35).wrapping_mul(0x9FB21C651E98DF25);
    lo = xorshift64(lo, 28);
    hi = avalanche(hi);

    lo as u128 | (hi as u128) << 64
}

#[inline(always)]
const fn xxh3_128_9to16(input: &[u8], seed: u64, secret: &[u8]) -> u128 {
    let flip_lo = (read_u64(secret, 32) ^ read_u64(secret, 40)).wrapping_sub(seed);
    let flip_hi = (read_u64(secret, 48) ^ read_u64(secret, 56)).wrapping_add(seed);
    let input_lo = read_u64(input, 0);
    let mut input_hi = read_u64(input, input.len() - 8);

    let (mut mul_low, mut mul_high) = mul64_to128(input_lo ^ input_hi ^ flip_lo, xxh64::PRIME_1);

    mul_low = mul_low.wrapping_add((input.len() as u64 - 1) << 54);
    input_hi ^= flip_hi;
    mul_high = mul_high.wrapping_add(
        input_hi.wrapping_add(mult32_to64(input_hi as u32, xxh32::PRIME_2 - 1))
    );

    mul_low ^= mul_high.swap_bytes();

    let (result_low, mut result_hi) = mul64_to128(mul_low, xxh64::PRIME_2);
    result_hi = result_hi.wrapping_add(
        mul_high.wrapping_mul(xxh64::PRIME_2)
    );

    avalanche(result_low) as u128 | (avalanche(result_hi) as u128) << 64
}

#[inline(always)]
const fn xxh3_128_0to16(input: &[u8], seed: u64, secret: &[u8]) -> u128 {
    if input.len() > 8 {
        xxh3_128_9to16(input, seed, secret)
    } else if input.len() >= 4 {
        xxh3_128_4to8(input, seed, secret)
    } else if input.len() > 0 {
        xxh3_128_1to3(input, seed, secret)
    } else {
        let flip_lo = read_u64(secret, 64) ^ read_u64(secret, 72);
        let flip_hi = read_u64(secret, 80) ^ read_u64(secret, 88);
        xxh64::avalanche(seed ^ flip_lo) as u128 | (xxh64::avalanche(seed ^ flip_hi) as u128) << 64
    }
}

#[inline(always)]
const fn xxh3_128_7to128(input: &[u8], seed: u64, secret: &[u8]) -> u128 {
    let mut acc = ((input.len() as u64).wrapping_mul(xxh64::PRIME_1), 0u64);

    if input.len() > 32 {
        if input.len() > 64 {
            if input.len() > 96 {
                acc = mix32_b(acc, input, 48, input, input.len() - 64, secret, 96, seed);
            }

            acc = mix32_b(acc, input, 32, input, input.len() - 48, secret, 64, seed);
        }

        acc = mix32_b(acc, input, 16, input, input.len() - 32, secret, 32, seed);
    }

    acc = mix32_b(acc, input, 0, input, input.len() - 16, secret, 0, seed);

    let result_lo = acc.0.wrapping_add(acc.1);
    let result_hi = acc.0.wrapping_mul(xxh64::PRIME_1)
                         .wrapping_add(acc.1.wrapping_mul(xxh64::PRIME_4))
                         .wrapping_add((input.len() as u64).wrapping_sub(seed).wrapping_mul(xxh64::PRIME_2));

    avalanche(result_lo) as u128 | (0u64.wrapping_sub(avalanche(result_hi)) as u128) << 64
}

#[inline(never)]
const fn xxh3_128_129to240(input: &[u8], seed: u64, secret: &[u8]) -> u128 {
    const START_OFFSET: usize = 3;
    const LAST_OFFSET: usize = 17;
    let nb_rounds = input.len() / 32;

    let mut acc = ((input.len() as u64).wrapping_mul(xxh64::PRIME_1), 0u64);

    let mut idx = 0;
    while idx < 4 {
        acc = mix32_b(acc, input, 32 * idx, input, (32 * idx) + 16, secret, 32 * idx, seed);
        idx += 1;
    }

    acc.0 = avalanche(acc.0);
    acc.1 = avalanche(acc.1);

    while idx < nb_rounds {
        acc = mix32_b(acc, input, 32 * idx, input, (32 * idx) + 16, secret, START_OFFSET.wrapping_add(32 * (idx - 4)), seed);
        idx += 1;
    }

    acc = mix32_b(acc, input, input.len() - 16, input, input.len() - 32, secret, SECRET_SIZE_MIN - LAST_OFFSET - 16, 0u64.wrapping_sub(seed));
    let result_lo = acc.0.wrapping_add(acc.1);
    let result_hi = acc.0.wrapping_mul(xxh64::PRIME_1)
                         .wrapping_add(acc.1.wrapping_mul(xxh64::PRIME_4))
                         .wrapping_add((input.len() as u64).wrapping_sub(seed).wrapping_mul(xxh64::PRIME_2));

    avalanche(result_lo) as u128 | 0u128.wrapping_sub(avalanche(result_hi) as u128) << 64
}

const fn xxh3_
... [TRUNCATED]
```

### File: src\const_xxh32.rs
```rs
//!Const eval friendly xxh32 implementation.

use core::mem;

use crate::xxh32_common::*;

#[inline(always)]
const fn read_u32(input: &[u8], cursor: usize) -> u32 {
    input[cursor] as u32 | (input[cursor + 1] as u32) << 8 | (input[cursor + 2] as u32) << 16 | (input[cursor + 3] as u32) << 24
}

const fn finalize(mut input: u32, data: &[u8], mut cursor: usize) -> u32 {
    let mut len = data.len() - cursor;

    while len >= 4 {
        input = input.wrapping_add(
            read_u32(data, cursor).wrapping_mul(PRIME_3)
        );
        cursor += mem::size_of::<u32>();
        len -= mem::size_of::<u32>();
        input = input.rotate_left(17).wrapping_mul(PRIME_4);
    }

    while len > 0 {
        input = input.wrapping_add((data[cursor] as u32).wrapping_mul(PRIME_5));
        cursor += mem::size_of::<u8>();
        len -= mem::size_of::<u8>();
        input = input.rotate_left(11).wrapping_mul(PRIME_1);
    }

    avalanche(input)
}

///Const variant of xxh32 hashing
pub const fn xxh32(input: &[u8], seed: u32) -> u32 {
    let mut result = input.len() as u32;
    let mut cursor = 0;

    if input.len() >= CHUNK_SIZE {
        let mut v1 = seed.wrapping_add(PRIME_1).wrapping_add(PRIME_2);
        let mut v2 = seed.wrapping_add(PRIME_2);
        let mut v3 = seed;
        let mut v4 = seed.wrapping_sub(PRIME_1);

        loop {
            v1 = round(v1, read_u32(input, cursor));
            cursor += mem::size_of::<u32>();
            v2 = round(v2, read_u32(input, cursor));
            cursor += mem::size_of::<u32>();
            v3 = round(v3, read_u32(input, cursor));
            cursor += mem::size_of::<u32>();
            v4 = round(v4, read_u32(input, cursor));
            cursor += mem::size_of::<u32>();

            if (input.len() - cursor) < CHUNK_SIZE {
                break;
            }
        }

        result = result.wrapping_add(
            v1.rotate_left(1).wrapping_add(
                v2.rotate_left(7).wrapping_add(
                    v3.rotate_left(12).wrapping_add(
                        v4.rotate_left(18)
                    )
                )
            )
        );
    } else {
        result = result.wrapping_add(seed.wrapping_add(PRIME_5));
    }

    finalize(result, input, cursor)
}

```

### File: src\const_xxh64.rs
```rs
//!Const 64 bit version of xxhash algorithm

use core::mem;

use crate::xxh64_common::*;

#[inline(always)]
const fn read_u32(input: &[u8], cursor: usize) -> u32 {
    input[cursor] as u32 | (input[cursor + 1] as u32) << 8 | (input[cursor + 2] as u32) << 16 | (input[cursor + 3] as u32) << 24
}

#[inline(always)]
const fn read_u64(input: &[u8], cursor: usize) -> u64 {
    input[cursor] as u64
        | (input[cursor + 1] as u64) << 8
        | (input[cursor + 2] as u64) << 16
        | (input[cursor + 3] as u64) << 24
        | (input[cursor + 4] as u64) << 32
        | (input[cursor + 5] as u64) << 40
        | (input[cursor + 6] as u64) << 48
        | (input[cursor + 7] as u64) << 56
}

const fn finalize(mut input: u64, data: &[u8], mut cursor: usize) -> u64 {
    let mut len = data.len() - cursor;

    while len >= 8 {
        input ^= round(0, read_u64(data, cursor));
        cursor += mem::size_of::<u64>();
        len -= mem::size_of::<u64>();
        input = input.rotate_left(27).wrapping_mul(PRIME_1).wrapping_add(PRIME_4)
    }

    if len >= 4 {
        input ^= (read_u32(data, cursor) as u64).wrapping_mul(PRIME_1);
        cursor += mem::size_of::<u32>();
        len -= mem::size_of::<u32>();
        input = input.rotate_left(23).wrapping_mul(PRIME_2).wrapping_add(PRIME_3);
    }

    while len > 0 {
        input ^= (data[cursor] as u64).wrapping_mul(PRIME_5);
        cursor += mem::size_of::<u8>();
        len -= mem::size_of::<u8>();
        input = input.rotate_left(11).wrapping_mul(PRIME_1);
    }

    avalanche(input)
}

///Returns hash for the provided input.
pub const fn xxh64(input: &[u8], seed: u64) -> u64 {
    let input_len = input.len() as u64;
    let mut cursor = 0;
    let mut result;

    if input.len() >= CHUNK_SIZE {
        let mut v1 = seed.wrapping_add(PRIME_1).wrapping_add(PRIME_2);
        let mut v2 = seed.wrapping_add(PRIME_2);
        let mut v3 = seed;
        let mut v4 = seed.wrapping_sub(PRIME_1);

        loop {
            v1 = round(v1, read_u64(input, cursor));
            cursor += mem::size_of::<u64>();
            v2 = round(v2, read_u64(input, cursor));
            cursor += mem::size_of::<u64>();
            v3 = round(v3, read_u64(input, cursor));
            cursor += mem::size_of::<u64>();
            v4 = round(v4, read_u64(input, cursor));
            cursor += mem::size_of::<u64>();

            if (input.len() - cursor) < CHUNK_SIZE {
                break;
            }
        }

        result = v1.rotate_left(1).wrapping_add(v2.rotate_left(7))
                                  .wrapping_add(v3.rotate_left(12))
                                  .wrapping_add(v4.rotate_left(18));

        result = merge_round(result, v1);
        result = merge_round(result, v2);
        result = merge_round(result, v3);
        result = merge_round(result, v4);
    } else {
        result = seed.wrapping_add(PRIME_5)
    }

    result = result.wrapping_add(input_len);

    finalize(result, input, cursor)
}

```

### File: src\lib.rs
```rs
//!Implementation of [xxHash](https://github.com/Cyan4973/xxHash) in Rust
//!
//!Version corresponds to xxHash [releases](https://github.com/Cyan4973/xxHash/releases)
//!
//!Each algorithm is implemented via feature, allowing precise control over code size.
//!
//!## Example
//!
//!- Cargo.toml
//!
//!```toml
//![dependencies.xxhash-rust]
//!version = "0.8.5"
//!features = ["xxh3", "const_xxh3"]
//!```
//!
//!- main.rs
//!
//!```rust
//!use xxhash_rust::const_xxh3::xxh3_64 as const_xxh3;
//!use xxhash_rust::xxh3::xxh3_64;
//!
//!const TEST: u64 = const_xxh3(b"TEST");
//!
//!fn test_input(text: &str) -> bool {
//!    match xxh3_64(text.as_bytes()) {
//!        TEST => true,
//!        _ => false
//!    }
//!}
//!
//!assert!(!test_input("tEST"));
//!assert!(test_input("TEST"));
//!```
//!
//!## Features:
//!
//!By default all features are off.
//!
//!- `std` - Enables `std::io::Write` trait implementation
//!- `xxh32` - Enables 32bit algorithm. Suitable for x86 targets
//!- `const_xxh32` - `const fn` version of `xxh32` algorithm
//!- `xxh64` - Enables 64 algorithm. Suitable for x86_64 targets
//!- `const_xxh64` - `const fn` version of `xxh64` algorithm
//!- `xxh3` - Enables `xxh3` family of algorithms, superior to `xxh32` and `xxh64` in terms of performance.
//!- `const_xxh3` - `const fn` version of `xxh3` algorithm
//!
//!## HW acceleration
//!
//!Similar to reference implementation, crate implements various SIMDs in `xxh3` depending on provided flags.
//!All checks are performed only at compile time, hence user is encouraged to enable these accelerations (for example via `-C target_cpu=native`)
//!
//!Used SIMD acceleration:
//!
//!- SSE2 - widely available, can be safely enabled in 99% of cases. Enabled by default in `x86_64` targets.
//!- AVX2;
//!- AVX512;
//!- Neon - Enabled by default on aarch64 targets (most likely);
//!- Wasm SIMD128 - Has to be enabled via rust flag: `-Ctarget-feature=+simd128`
//!
//!## Streaming vs One-shot
//!
//!For performance reasons one-shot version of algorithm does not re-use streaming version.
//!Unless needed, user is advised to use one-shot version which tends to be more optimal.
//!
//!## `cosnt fn` version
//!
//!While `const fn` provides compile time implementation, it does so at performance cost.
//!Hence you should only use it at _compile_ time.
//!
//!To guarantee that something is computed at compile time make sure to initialize hash output
//!as `const` or `static` variable, otherwise it is possible function is executed at runtime, which
//!would be worse than regular algorithm.
//!
//!`const fn` is implemented in best possible way while conforming to limitations of Rust `const
//!fn`, but these limitations are quite strict making any high performance code impossible.

#![no_std]
#![warn(missing_docs)]
#![allow(clippy::style)]

#[cfg(feature = "std")]
extern crate std;

#[cfg(any(feature = "xxh32", feature = "xxh3", feature = "xxh64"))]
mod utils;

#[cfg(any(feature = "xxh32", feature = "const_xxh32", feature = "xxh3", feature = "const_xxh3"))]
mod xxh32_common;
#[cfg(feature = "xxh32")]
pub mod xxh32;
#[cfg(feature = "const_xxh32")]
pub mod const_xxh32;

#[cfg(any(feature = "xxh64", feature = "const_xxh64", feature = "xxh3", feature = "const_xxh3"))]
mod xxh64_common;
#[cfg(feature = "xxh64")]
pub mod xxh64;
#[cfg(feature = "const_xxh64")]
pub mod const_xxh64;

#[cfg(any(feature = "xxh3", feature = "const_xxh3"))]
mod xxh3_common;
#[cfg(feature = "xxh3")]
pub mod xxh3;
#[cfg(feature = "const_xxh3")]
pub mod const_xxh3;

```

### File: src\utils.rs
```rs
//! Utilities of the crate
use core::{ptr, mem};

#[inline(always)]
pub const fn get_aligned_chunk_ref<T: Copy>(input: &[u8], offset: usize) -> &T {
    debug_assert!(mem::size_of::<T>() > 0); //Size MUST be positive
    debug_assert!(mem::size_of::<T>() <= input.len().saturating_sub(offset)); //Must fit

    unsafe {
        &*(input.as_ptr().add(offset) as *const T)
    }
}

#[allow(unused)]
#[inline(always)]
pub const fn get_aligned_chunk<T: Copy>(input: &[u8], offset: usize) -> T {
    *get_aligned_chunk_ref(input, offset)
}

#[inline(always)]
pub fn get_unaligned_chunk<T: Copy>(input: &[u8], offset: usize) -> T {
    debug_assert!(mem::size_of::<T>() > 0); //Size MUST be positive
    debug_assert!(mem::size_of::<T>() <= input.len().saturating_sub(offset)); //Must fit

    unsafe {
        ptr::read_unaligned(input.as_ptr().add(offset) as *const T)
    }
}

#[derive(Debug)]
pub struct Buffer<T> {
    pub ptr: T,
    pub len: usize,
    pub offset: usize,
}

impl Buffer<*mut u8> {
    #[inline(always)]
    pub fn copy_from_slice(&self, src: &[u8]) {
        self.copy_from_slice_by_size(src, src.len())
    }

    #[inline(always)]
    pub fn copy_from_slice_by_size(&self, src: &[u8], len: usize) {
        debug_assert!(self.len.saturating_sub(self.offset) >= len);

        unsafe {
            ptr::copy_nonoverlapping(src.as_ptr(), self.ptr.add(self.offset), len);
        }
    }
}

```

### File: src\xxh3.rs
```rs
//!XXH3 implementation
//!
//!Provides `Hasher` only for 64bit as 128bit variant would not be much different due to trait
//!being limited to `u64` outputs.

use core::{ptr, mem, slice, hash};

use crate::xxh32_common as xxh32;
use crate::xxh64_common as xxh64;
use crate::xxh3_common::*;
use crate::utils::{Buffer, get_unaligned_chunk, get_aligned_chunk_ref};

// Code is as close to original C implementation as possible
// It does make it look ugly, but it is fast and easy to update once xxhash gets new version.

#[cfg(all(any(target_feature = "sse2", target_feature = "neon", all(target_family = "wasm", target_feature = "simd128")), not(any(target_feature = "avx2", target_feature = "avx512f"))))]
#[repr(align(16))]
#[derive(Clone)]
struct Acc([u64; ACC_NB]);
#[cfg(all(target_feature = "avx2", not(target_feature = "avx512f")))]
#[repr(align(32))]
#[derive(Clone)]
struct Acc([u64; ACC_NB]);
#[cfg(target_feature = "avx512f")]
#[repr(align(64))]
#[derive(Clone)]
struct Acc([u64; ACC_NB]);
#[cfg(not(any(target_feature = "avx512f", target_feature = "avx2", target_feature = "neon", all(target_family = "wasm", target_feature = "simd128"), target_feature = "sse2")))]
#[repr(align(8))]
#[derive(Clone)]
struct Acc([u64; ACC_NB]);

const INITIAL_ACC: Acc = Acc([
    xxh32::PRIME_3 as u64, xxh64::PRIME_1, xxh64::PRIME_2, xxh64::PRIME_3,
    xxh64::PRIME_4, xxh32::PRIME_2 as u64, xxh64::PRIME_5, xxh32::PRIME_1 as u64
]);

type LongHashFn = fn(&[u8], u64, &[u8]) -> u64;
type LongHashFn128 = fn(&[u8], u64, &[u8]) -> u128;

#[cfg(all(target_family = "wasm", target_feature = "simd128"))]
type StripeLanes = [[u8; mem::size_of::<core::arch::wasm32::v128>()]; STRIPE_LEN / mem::size_of::<core::arch::wasm32::v128>()];
#[cfg(all(target_arch = "x86", target_feature = "avx512f"))]
type StripeLanes = [[u8; mem::size_of::<core::arch::x86::__m512i>()]; STRIPE_LEN / mem::size_of::<core::arch::x86::__m512i>()];
#[cfg(all(target_arch = "x86_64", target_feature = "avx512f"))]
type StripeLanes = [[u8; mem::size_of::<core::arch::x86_64::__m512i>()]; STRIPE_LEN / mem::size_of::<core::arch::x86_64::__m512i>()];
#[cfg(all(target_arch = "x86", target_feature = "avx2", not(target_feature = "avx512f")))]
type StripeLanes = [[u8; mem::size_of::<core::arch::x86::__m256i>()]; STRIPE_LEN / mem::size_of::<core::arch::x86::__m256i>()];
#[cfg(all(target_arch = "x86_64", target_feature = "avx2", not(target_feature = "avx512f")))]
type StripeLanes = [[u8; mem::size_of::<core::arch::x86_64::__m256i>()]; STRIPE_LEN / mem::size_of::<core::arch::x86_64::__m256i>()];
#[cfg(all(target_arch = "x86", target_feature = "sse2", not(any(target_feature = "avx2", target_feature = "avx512f"))))]
type StripeLanes = [[u8; mem::size_of::<core::arch::x86::__m128i>()]; STRIPE_LEN / mem::size_of::<core::arch::x86::__m128i>()];
#[cfg(all(target_arch = "x86_64", target_feature = "sse2", not(any(target_feature = "avx2", target_feature = "avx512f"))))]
type StripeLanes = [[u8; mem::size_of::<core::arch::x86_64::__m128i>()]; STRIPE_LEN / mem::size_of::<core::arch::x86_64::__m128i>()];
#[cfg(target_feature = "neon")]
type StripeLanes = [[u8; mem::size_of::<core::arch::aarch64::uint8x16_t>()]; STRIPE_LEN / mem::size_of::<core::arch::aarch64::uint8x16_t>()];

// TODO: replace with [`core::arch::x86::_MM_SHUFFLE`](https://doc.rust-lang.org/core/arch/x86/fn._MM_SHUFFLE.html)
// when it stabilizes
#[cfg(any(target_feature = "sse2", target_feature = "avx2", target_feature = "avx512f"))]
#[inline]
const fn _mm_shuffle(z: u32, y: u32, x: u32, w: u32) -> i32 {
    ((z << 6) | (y << 4) | (x << 2) | w) as i32
}

#[inline(always)]
const fn mult32_to64(left: u32, right: u32) -> u64 {
    (left as u64).wrapping_mul(right as u64)
}

//#[inline(always)]
//fn _mm_prefetch(_ptr: *const i8, _offset: isize) {
//    #[cfg(target_arch = "x86")]
//    unsafe {
//        core::arch::x86::_mm_prefetch(_ptr.offset(_offset), core::arch::x86::_MM_HINT_T0);
//    }
//
//    #[cfg(target_arch = "x86_64")]
//    unsafe {
//        core::arch::x86_64::_mm_prefetch(_ptr.offset(_offset), core::arch::x86_64::_MM_HINT_T0);
//    }
//}

macro_rules! to_u128 {
    ($lo:expr, $hi:expr) => {
        ($lo) as u128 | ((($hi) as u128) << 64)
    };
}

macro_rules! slice_offset_ptr {
    ($slice:expr, $offset:expr) => {{
        let slice = $slice;
        let offset = $offset;
        debug_assert!(slice.len() >= offset);

        #[allow(unused_unsafe)]
        unsafe {
            (slice.as_ptr() as *const u8).add(offset)
        }
    }}
}

#[inline(always)]
fn read_32le_unaligned(data: &[u8], offset: usize) -> u32 {
    u32::from_ne_bytes(*get_aligned_chunk_ref(data, offset)).to_le()
}

#[inline(always)]
fn read_64le_unaligned(data: &[u8], offset: usize) -> u64 {
    u64::from_ne_bytes(*get_aligned_chunk_ref(data, offset)).to_le()
}

#[inline(always)]
fn mix_two_accs(acc: &mut Acc, offset: usize, secret: &[[u8; 8]; 2]) -> u64 {
    mul128_fold64(acc.0[offset] ^ u64::from_ne_bytes(secret[0]).to_le(),
                  acc.0[offset + 1] ^ u64::from_ne_bytes(secret[1]).to_le())
}

#[inline]
fn merge_accs(acc: &mut Acc, secret: &[[[u8; 8]; 2]; 4], mut result: u64) -> u64 {
    macro_rules! mix_two_accs {
        ($idx:literal) => {
            result = result.wrapping_add(mix_two_accs(acc, $idx * 2, &secret[$idx]))
        }
    }

    mix_two_accs!(0);
    mix_two_accs!(1);
    mix_two_accs!(2);
    mix_two_accs!(3);

    avalanche(result)
}

#[inline(always)]
fn mix16_b(input: &[[u8; 8]; 2], secret: &[[u8; 8]; 2], seed: u64) -> u64 {
    let mut input_lo = u64::from_ne_bytes(input[0]).to_le();
    let mut input_hi = u64::from_ne_bytes(input[1]).to_le();

    input_lo ^= u64::from_ne_bytes(secret[0]).to_le().wrapping_add(seed);
    input_hi ^= u64::from_ne_bytes(secret[1]).to_le().wrapping_sub(seed);

    mul128_fold64(input_lo, input_hi)
}

#[inline(always)]
//Inputs are two chunks of unaligned u64
//Secret are two chunks of unaligned (u64, u64)
fn mix32_b(lo: &mut u64, hi: &mut u64, input_1: &[[u8; 8]; 2], input_2: &[[u8; 8]; 2], secret: &[[[u8; 8]; 2]; 2], seed: u64) {
    *lo = lo.wrapping_add(mix16_b(input_1, &secret[0], seed));
    *lo ^= u64::from_ne_bytes(input_2[0]).to_le().wrapping_add(u64::from_ne_bytes(input_2[1]).to_le());

    *hi = hi.wrapping_add(mix16_b(input_2, &secret[1], seed));
    *hi ^= u64::from_ne_bytes(input_1[0]).to_le().wrapping_add(u64::from_ne_bytes(input_1[1]).to_le());
}

#[inline(always)]
fn custom_default_secret(seed: u64) -> [u8; DEFAULT_SECRET_SIZE] {
    let mut result = mem::MaybeUninit::<[u8; DEFAULT_SECRET_SIZE]>::uninit();

    let nb_rounds = DEFAULT_SECRET_SIZE / 16;

    for idx in 0..nb_rounds {
        let low = get_unaligned_chunk::<u64>(&DEFAULT_SECRET, idx * 16).to_le().wrapping_add(seed);
        let hi = get_unaligned_chunk::<u64>(&DEFAULT_SECRET, idx * 16 + 8).to_le().wrapping_sub(seed);

        Buffer {
            ptr: result.as_mut_ptr() as *mut u8,
            len: DEFAULT_SECRET_SIZE,
            offset: idx * 16,
        }.copy_from_slice(&low.to_le_bytes());
        Buffer {
            ptr: result.as_mut_ptr() as *mut u8,
            len: DEFAULT_SECRET_SIZE,
            offset: idx * 16 + 8,
        }.copy_from_slice(&hi.to_le_bytes());
    }

    unsafe {
        result.assume_init()
    }
}

#[cfg(all(target_family = "wasm", target_feature = "simd128"))]
fn accumulate_512_wasm(acc: &mut Acc, input: &StripeLanes, secret: &StripeLanes) {
    const LANES: usize = ACC_NB;

    use core::arch::wasm32::*;

    let mut idx = 0usize;
    let xacc = acc.0.as_mut_ptr() as *mut v128;

    unsafe {
        while idx.wrapping_add(1) < LANES / 2 {
            let data_vec_1 = v128_load(input[idx].as_ptr() as _);
            let data_vec_2 = v128_load(input[idx.wrapping_add(1)].as_ptr() as _);

            let key_vec_1 = v128_load(secret[idx].as_ptr() as _);
            let key_vec_2 = v128_load(secret[idx.wrapping_add(1)].as_ptr() as _);

            let data_key_1 = v128_xor(data_vec_1, key_vec_1);
            let data_key_2 = v128_xor(data_vec_2, key_vec_2);

            let data_swap_1 = i64x2_shuffle::<1, 0>(data_vec_1, data_vec_1);
            let data_swap_2 = i64x2_shuffle::<1, 0>(data_vec_2, data_vec_2);

            let mixed_lo = i32x4_shuffle::<0, 2, 4, 6>(data_key_1, data_key_2);
            let mixed_hi = i32x4_shuffle::<1, 3, 5, 7>(data_key_1, data_key_2);

            let prod_1 = u64x2_extmul_low_u32x4(mixed_lo, mixed_hi);
            let prod_2 = u64x2_extmul_high_u32x4(mixed_lo, mixed_hi);

            let sum_1 = i64x2_add(prod_1, data_swap_1);
            let sum_2 = i64x2_add(prod_2, data_swap_2);

            xacc.add(idx).write(i64x2_add(sum_1, *xacc.add(idx)));
            xacc.add(idx.wrapping_add(1)).write(i64x2_add(sum_2, *xacc.add(idx.wrapping_add(1))));

            idx = idx.wrapping_add(2);
        }
    }
}

#[cfg(all(target_arch = "aarch64", target_feature = "neon"))]
macro_rules! vld1q_u8 {
    ($ptr:expr) => {
        core::arch::aarch64::vld1q_u8($ptr)

    }
}

//For some dumb reasons vld1q_u8 is unstable for arm
#[cfg(all(target_arch = "arm", target_feature = "neon"))]
macro_rules! vld1q_u8 {
    ($ptr:expr) => {
        core::ptr::read_unaligned($ptr as *const core::arch::arm::uint8x16_t)
    }
}

#[cfg(target_feature = "neon")]
fn accumulate_512_neon(acc: &mut Acc, input: &StripeLanes, secret: &StripeLanes) {
    //Full Neon version from xxhash source
    const NEON_LANES: usize = ACC_NB;

    unsafe {
        #[cfg(target_arch = "arm")]
        use core::arch::arm::*;
        #[cfg(target_arch = "aarch64")]
        use core::arch::aarch64::*;

        let mut idx = 0usize;
        let xacc = acc.0.as_mut_ptr() as *mut uint64x2_t;

        while idx.wrapping_add(1) < NEON_LANES / 2 {
            /* data_vec = xinput[i]; */
            let data_vec_1 = vreinterpretq_u64_u8(vld1q_u8!(input[idx].as_ptr()));
            let data_vec_2 = vreinterpretq_u64_u8(vld1q_u8!(input[idx.wrapping_add(1)].as_ptr()));
            /* key_vec  = xsecret[i];  */
            let key_vec_1  = vreinterpretq_u64_u8(vld1q_u8!(secret[idx].as_ptr()));
            let key_vec_2  = vreinterpretq_u64_u8(vld1q_u8!(secret[idx.wrapping_add(1)].as_ptr()));
            /* data_swap = swap(data_vec) */
            let data_swap_1 = vextq_u64(data_vec_1, data_vec_1, 1);
            let data_swap_2 = vextq_u64(data_vec_2, data_vec_2, 1);
            /* data_key = data_vec ^ key_vec; */
            let data_key_1 = veorq_u64(data_vec_1, key_vec_1);
            let data_key_2 = veorq_u64(data_vec_2, key_vec_2);

            let unzipped = vuzpq_u32(
                vreinterpretq_u32_u64(data_key_1),
                vreinterpretq_u32_u64(data_key_2)
            );
            /* data_key_lo = data_key & 0xFFFFFFFF */
            let data_key_lo = unzipped.0;
            /* data_key_hi = data_key >> 32 */
            let data_key_hi = unzipped.1;

            //xxhash does it with inline assembly, but idk if I want to embed it here
            let sum_1 = vmlal_u32(data_swap_1, vget_low_u32(data_key_lo), vget_low_u32(data_key_hi));
            #[cfg(target_arch = "aarch64")]
            let sum_2 = vmlal_high_u32(data_swap_2, data_key_lo, data_key_hi);
            #[cfg(target_arch = "arm")]
            let sum_2 = vmlal_u32(data_swap_2, vget_high_u32(data_key_lo), vget_high_u32(data_key_hi));

            xacc.add(idx).write(vaddq_u64(*xacc.add(idx), sum_1));
            xacc.add(idx.wrapping_add(1)).write(vaddq_u64(*xacc.add(idx.wrapping_add(1)), sum_2));

            idx = idx.wrapping_add(2);
        }
    }
}

#[cfg(all(target_feature = "sse2", not(any(target_feature = "avx2", target_feature = "avx512f"))))]
fn accumulate_512_sse2(acc: &mut Acc, input: &StripeLanes, secret: &StripeLanes) {
    unsafe {
        #[cfg(target_arch = "x86")]
        use core::arch::x86::*;
        #[cfg(target_arch = "x86_64")]
        use core::arch::x86_64::*;

        let xacc = acc.0.as_mut_ptr() as *mut __m128i;

        for idx in 0..secret.len() {
            let data_vec = _mm_loadu_si128(input[idx].as_ptr() as _);
            let key_vec = _mm_loadu_si128(secret[idx].as_ptr() as _);
            let data_key = _mm_xor_si128(data_vec, key_vec);

            let data_key_lo = _mm_shuffle_epi32(data_key, _mm_shuffle(0, 3, 0, 1));
            let product = _mm_mul_epu32(data_key, data_key_lo);

            let data_swap = _mm_shuffle_epi32(data_vec, _mm_shuffle(1,0,3,2));
            let sum = _mm_add_epi64(*xacc.add(idx), data_swap);
            xacc.add(idx).write(_mm_add_epi64(product, sum));
        }
    }
}

#[cfg(all(target_feature = "avx2", not(target_feature = "avx512f")))]
fn accumulate_512_avx2(acc: &mut Acc, input: &StripeLanes, secret: &StripeLanes) {
    unsafe {
        #[cfg(target_arch = "x86")]
        use core::arch::x86::*;
        #[cfg(target_arch = "x86_64")]
        use core::arch::x86_64::*;

        let xacc = acc.0.as_mut_ptr() as *mut __m256i;

        for idx in 0..secret.len() {
            let data_vec = _mm256_loadu_si256(input[idx].as_ptr() as _);
            let key_vec = _mm256_loadu_si256(secret[idx].as_ptr() as _);
            let data_key = _mm256_xor_si256(data_vec, key_vec);

            let data_key_lo = _mm256_srli_epi64(data_key, 32);
            let product = _mm256_mul_epu32(data_key, data_key_lo);

            let data_swap = _mm256_shuffle_epi32(data_vec, _mm_shuffle(1,0,3,2));
            let sum = _mm256_add_epi64(*xacc.add(idx), data_swap);
            xacc.add(idx).write(_mm256_add_epi64(product, sum));
        }
    }
}

#[cfg(target_feature = "avx512f")]
fn accumulate_512_avx512(acc: &mut Acc, input: &StripeLanes, secret: &StripeLanes) {
    unsafe {
        #[cfg(target_arch = "x86")]
        use core::arch::x86::*;
        #[cfg(target_arch = "x86_64")]
        use core::arch::x86_64::*;

        let xacc = acc.0.as_mut_ptr() as *mut __m512i;

        let idx = 0;

        let data_vec = _mm512_loadu_si512(input[idx].as_ptr() as _);
        let key_vec = _mm512_loadu_si512(secret[idx].as_ptr() as _);
        let data_key = _mm512_xor_si512(data_vec, key_vec);

        let data_key_lo = _mm512_srli_epi64(data_key, 32);
        let product = _mm512_mul_epu32(data_key, data_key_lo);

        let data_swap = _mm512_shuffle_epi32(data_vec, _mm_shuffle(1, 0, 3, 2));
        let sum = _mm512_add_epi64(*xacc.add(idx), data_swap);
        xacc.add(idx).write(_mm512_add_epi64(product, sum));
    }
}

#[cfg(not(any(target_feature = "avx512f", target_feature = "avx2", target_feature = "sse2", target_feature = "neon", all(target_family = "wasm", target_feature = "simd128"))))]
fn accumulate_512_scalar(acc: &mut Acc, input: &[[u8; 8]; ACC_NB], secret: &[[u8; 8]; ACC_NB]) {
    for idx in 0..ACC_NB {
        let data_val = u64::from_ne_bytes(input[idx]).to_le();
        let data_key = data_val ^ u64::from_ne_bytes(secret[idx]).to_le();

        acc.0[idx ^ 1] = acc.0[idx ^ 1].wrapping_add(data_val);
        acc.0[idx] = acc.0[idx].wrapping_add(mult32_to
... [TRUNCATED]
```

### File: src\xxh32.rs
```rs
//!32 bit version of xxhash algorithm
//!
//!Written using C implementation as reference.

use core::{mem, slice};

use crate::utils::{Buffer, get_unaligned_chunk, get_aligned_chunk};
use crate::xxh32_common::*;

fn finalize(mut input: u32, mut data: &[u8], is_aligned: bool) -> u32 {
    while data.len() >= 4 {
        input = input.wrapping_add(match is_aligned {
            true => get_aligned_chunk::<u32>(data, 0).to_le().wrapping_mul(PRIME_3),
            false => get_unaligned_chunk::<u32>(data, 0).to_le().wrapping_mul(PRIME_3),
        });
        input = input.rotate_left(17).wrapping_mul(PRIME_4);
        data = &data[4..];
    }

    for byte in data.iter() {
        input = input.wrapping_add((*byte as u32).wrapping_mul(PRIME_5));
        input = input.rotate_left(11).wrapping_mul(PRIME_1);
    }

    avalanche(input)
}

#[inline(always)]
const fn init_v(seed: u32) -> (u32, u32, u32, u32) {
    (
        seed.wrapping_add(PRIME_1).wrapping_add(PRIME_2),
        seed.wrapping_add(PRIME_2),
        seed,
        seed.wrapping_sub(PRIME_1),
    )
}

macro_rules! round_loop {
    ($input:ident => $($v:tt)+) => {
        $($v)+.0 = round($($v)+.0, get_unaligned_chunk::<u32>($input, 0).to_le());
        $($v)+.1 = round($($v)+.1, get_unaligned_chunk::<u32>($input, 4).to_le());
        $($v)+.2 = round($($v)+.2, get_unaligned_chunk::<u32>($input, 8).to_le());
        $($v)+.3 = round($($v)+.3, get_unaligned_chunk::<u32>($input, 12).to_le());
        $input = &$input[16..];
    }
}

///Returns hash for the provided input
pub fn xxh32(mut input: &[u8], seed: u32) -> u32 {
    let mut result = input.len() as u32;

    if input.len() >= CHUNK_SIZE {
        let mut v = init_v(seed);

        loop {
            round_loop!(input => v);
            if input.len() < CHUNK_SIZE {
                break;
            }
        }

        result = result.wrapping_add(
            v.0.rotate_left(1).wrapping_add(
                v.1.rotate_left(7).wrapping_add(
                    v.2.rotate_left(12).wrapping_add(
                        v.3.rotate_left(18)
                    )
                )
            )
        );
    } else {
        result = result.wrapping_add(seed.wrapping_add(PRIME_5));
    }

    return finalize(result, input, false);
}

///XXH32 Streaming algorithm
#[derive(Clone)]
pub struct Xxh32 {
    total_len: u32,
    is_large_len: bool,
    v: (u32, u32, u32, u32),
    mem: [u32; 4],
    mem_size: u32,
}

impl Xxh32 {
    #[inline]
    ///Creates new hasher with specified seed.
    pub const fn new(seed: u32) -> Self {
        Self {
            total_len: 0,
            is_large_len: false,
            v: init_v(seed),
            mem: [0, 0, 0, 0],
            mem_size: 0,
        }
    }

    ///Hashes provided input.
    pub fn update(&mut self, mut input: &[u8]) {
        self.total_len = self.total_len.wrapping_add(input.len() as u32);
        self.is_large_len |= (input.len() as u32 >= CHUNK_SIZE as u32) | (self.total_len >= CHUNK_SIZE as u32);

        if (self.mem_size + input.len() as u32) < CHUNK_SIZE as u32 {
            Buffer {
                ptr: self.mem.as_mut_ptr() as *mut u8,
                len: mem::size_of_val(&self.mem),
                offset: self.mem_size as _,
            }.copy_from_slice(input);
            self.mem_size += input.len() as u32;
            return
        }

        if self.mem_size > 0 {
            //previous if can fail only when we do not have enough space in buffer for input.
            //hence fill_len >= input.len()
            let fill_len = CHUNK_SIZE - self.mem_size as usize;

            Buffer {
                ptr: self.mem.as_mut_ptr() as *mut u8,
                len: mem::size_of_val(&self.mem),
                offset: self.mem_size as _,
            }.copy_from_slice_by_size(input, fill_len);

            self.v.0 = round(self.v.0, self.mem[0].to_le());
            self.v.1 = round(self.v.1, self.mem[1].to_le());
            self.v.2 = round(self.v.2, self.mem[2].to_le());
            self.v.3 = round(self.v.3, self.mem[3].to_le());

            input = &input[fill_len..];
            self.mem_size = 0;
        }

        if input.len() >= CHUNK_SIZE {
            loop {
                round_loop!(input => self.v);
                if input.len() < CHUNK_SIZE {
                    break;
                }
            }
        }

        if input.len() > 0 {
            Buffer {
                ptr: self.mem.as_mut_ptr() as *mut u8,
                len: mem::size_of_val(&self.mem),
                offset: 0
            }.copy_from_slice(input);
            self.mem_size = input.len() as u32;
        }
    }

    ///Finalize hashing.
    pub fn digest(&self) -> u32 {
        let mut result = self.total_len;

        if self.is_large_len {
            result = result.wrapping_add(
                self.v.0.rotate_left(1).wrapping_add(
                    self.v.1.rotate_left(7).wrapping_add(
                        self.v.2.rotate_left(12).wrapping_add(
                            self.v.3.rotate_left(18)
                        )
                    )
                )
            );
        } else {
            result = result.wrapping_add(self.v.2.wrapping_add(PRIME_5));
        }

        let input = unsafe {
            slice::from_raw_parts(self.mem.as_ptr() as *const u8, self.mem_size as usize)
        };

        return finalize(result, input, true);
    }

    #[inline]
    ///Resets the state with specified seed.
    pub fn reset(&mut self, seed: u32) {
        self.total_len = 0;
        self.is_large_len = false;
        self.v = init_v(seed);
        self.mem_size = 0;
    }
}

impl Default for Xxh32 {
    #[inline(always)]
    fn default() -> Self {
        Self::new(0)
    }
}

#[cfg(feature = "std")]
impl std::io::Write for Xxh32 {
    #[inline]
    fn write(&mut self, buf: &[u8]) -> std::io::Result<usize> {
        self.update(buf);
        Ok(buf.len())
    }

    #[inline]
    fn flush(&mut self) -> std::io::Result<()> {
        Ok(())
    }
}

```

### File: src\xxh32_common.rs
```rs
#![allow(unused)]

use core::mem;

pub const CHUNK_SIZE: usize = mem::size_of::<u32>() * 4;
pub const PRIME_1: u32 = 0x9E3779B1;
pub const PRIME_2: u32 = 0x85EBCA77;
pub const PRIME_3: u32 = 0xC2B2AE3D;
pub const PRIME_4: u32 = 0x27D4EB2F;
pub const PRIME_5: u32 = 0x165667B1;

#[inline]
pub const fn round(acc: u32, input: u32) -> u32 {
    acc.wrapping_add(input.wrapping_mul(PRIME_2))
       .rotate_left(13)
       .wrapping_mul(PRIME_1)
}

#[inline]
pub const fn avalanche(mut input: u32) -> u32 {
    input ^= input >> 15;
    input = input.wrapping_mul(PRIME_2);
    input ^= input >> 13;
    input = input.wrapping_mul(PRIME_3);
    input ^= input >> 16;
    input
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
