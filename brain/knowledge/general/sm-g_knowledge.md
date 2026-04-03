---
id: sm-g-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:15.276094
---

# KNOWLEDGE EXTRACT: sm-g
> **Extracted on:** 2026-03-30 17:53:52
> **Source:** sm-g

---

## File: `ByValue.md`
```markdown
# 📦 sm-g/ByValue [🔖 PENDING/APPROVE]
🔗 https://github.com/sm-g/ByValue


## Meta
- **Stars:** ⭐ 7 | **Forks:** 🍴 0
- **Language:** C# | **License:** MIT
- **Last updated:** 2025-11-08
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
DDD ValueObject implementation helper

## README (trích đầu)
```
# ByValue

[![Build status](https://ci.appveyor.com/api/projects/status/k6nmr1mdixf7xho6/branch/master?svg=true)](https://ci.appveyor.com/project/sm-g/byvalue/branch/master) [![Build Status](https://travis-ci.org/sm-g/ByValue.svg?branch=master)](https://travis-ci.org/sm-g/ByValue) [![NuGet](http://img.shields.io/nuget/v/ByValue.svg)](https://www.nuget.org/packages/ByValue/)

This library helps to create ValueObjects with properly implemented equality behavior:

1. Provides base `ValueObject` class.
2. Gives extension `ByValue()` for comparing collections with semantic of ValueObject (`IReadOnlyCollection`, `IReadOnlyDictionary`, `IDictionary` and `ISet` are supported).

## Example

```cs
public class MultilineAddress : ValueObject
{
    public MultilineAddress(IReadOnlyCollection<string> addressLines, string city, string postalCode)
    {
        AddressLines = addressLines ?? throw new ArgumentNullException(nameof(addressLines));
        City = city ?? throw new ArgumentNullException(nameof(city));
        PostalCode = postalCode ?? throw new ArgumentNullException(nameof(postalCode));

        if (addressLines.Count < 1 || addressLines.Count > 3)
            throw new ArgumentOutOfRangeException(nameof(addressLines), addressLines, "Multiline address should have from 1 to 3 address lines");
    }

    public IReadOnlyCollection<string> AddressLines { get; }
    public string City { get; }
    public string PostalCode { get; }

    // here you should return values, which will be used in Equals() and GetHashCode()
    protected override IEnumerable<object> Reflect()
    {
        // by default collections compared with not strcit ordering
        yield return AddressLines.ByValue(Ordering.Strict);

        // you can transform object's properties when return them
        yield return City.ToUpperInvariant();

        yield return PostalCode;
    }
}
```

### SingleValueObject

Inherit from `SingleValueObject` to boost performance when ValueObject has only one property:

```cs
public class UserId : SingleValueObject<int>
{
    public UserId(int value)
        : base(value)
    {
        if (value == 0)
            throw new ArgumentOutOfRangeException(nameof(value));
    }

    public static explicit operator UserId(int value)
    {
        return new UserId(value);
    }

    public static implicit operator int(UserId userId)
    {
        return userId == null ? 0 : userId.Value;
    }

    public static implicit operator int? (UserId userId)
    {
        return userId == null ? (int?)null : userId.Value;
    }
}
```

### Custom EqualityComparer

When using `ByValue()` to compare collections, elements will be compared using default `EqualityComparer`. Sometimes this is not acceptable.

Here is `AddressBook` which implements value object semantic:

```cs
public class AddressBook : ReadOnlyCollection<MultilineAddress>
{
    public AddressBook(IList<MultilineAddress> list)
        : base(list)
    {
    }

    public override bool Equals(object obj)
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

