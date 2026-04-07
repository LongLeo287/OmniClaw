---
id: scritchy
type: knowledge
owner: OA_Triage
---
# scritchy
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: Readme.txt
```txt
Scritchy - Removing the plumbing from CQRS

Scritchy is a convention-based CQRS framework for .Net

More info over at:
- The demo site: 	http://scritchyexample.apphb.com
- The google group: 	http://groups.google.com/group/scritchy

There is also a NuGet package available:
http://nuget.org/List/Packages/Scritchy

And a screencast: Scritchy CQRS - Building a working CQRS app in 15 minutes
http://www.youtube.com/watch?v=5DKTFZD3hu8

```

### File: LICENSE.txt
```txt
The MIT License (MIT)

Copyright (c) 2013 Tom Janssens

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

### File: Example\Domain\StockItem.cs
```cs
﻿namespace Example.Domain
{
    public class StockItem : Scritchy.Domain.AR
    {
        int Amount = 0;
        bool IsAllowed = false;

        public void AllowItem(string Name)
        {
            if (IsAllowed == true) return;
            Changes += new Events.ItemAllowed { StockItemId = Id, Name = Name };
        }

        public void CanBanItem()
        {
            Guard.Against(Amount > 0, "An item that is in stock can not be banned");
        }

        public void BanItem()
        {
            if (IsAllowed == false) return;
            Changes += new Events.ItemBanned { StockItemId = Id };
        }

        public void CanAddItems()
        {
            Guard.Against(IsAllowed == false, "An item of this type is not allowed in the stock");
        }

        public void AddItems(int Amount)
        {
            Changes += new Events.ItemsAdded { StockItemId = Id, Amount = Amount };
        }

        public void CanRemoveItems(int Amount)
        {
            Guard.Against(IsAllowed == false, "An item of this type is not allowed in the stock");
            Guard.Against(this.Amount < Amount, "You do not have enough stock left to remove this amount of items");
        }

        public void RemoveItems(int Amount)
        {
            Changes += new Events.ItemsRemoved { StockItemId = Id, Amount = Amount };
        }

        public void OnItemsAdded(int Amount)
        {
            this.Amount += Amount;
        }

        public void OnItemsRemoved(int Amount)
        {
            this.Amount -= Amount;
        }

        public void OnItemAllowed()
        {
            IsAllowed = true;
        }

        public void OnItemBanned()
        {
            IsAllowed = false;
        }
    }
}

```

### File: Example\Properties\AssemblyInfo.cs
```cs
﻿using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

// General Information about an assembly is controlled through the following 
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
[assembly: AssemblyTitle("Example")]
[assembly: AssemblyDescription("")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("Microsoft")]
[assembly: AssemblyProduct("Example")]
[assembly: AssemblyCopyright("Copyright © Microsoft 2011")]
[assembly: AssemblyTrademark("")]
[assembly: AssemblyCulture("")]

// Setting ComVisible to false makes the types in this assembly not visible 
// to COM components.  If you need to access a type in this assembly from 
// COM, set the ComVisible attribute to true on that type.
[assembly: ComVisible(false)]

// The following GUID is for the ID of the typelib if this project is exposed to COM
[assembly: Guid("3a9eff4f-8fc8-4501-9a3a-e8f70cc00c4a")]

// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version 
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Build and Revision Numbers 
// by using the '*' as shown below:
// [assembly: AssemblyVersion("1.0.*")]
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]

```

### File: Example\Domain\Commands\StockItem.cs
```cs
﻿namespace Example.Domain.Commands
{
    public class AddItems
    {
        public string StockItemId { get; set; }
        public int Amount { get; set; }
    }

    public class RemoveItems
    {
        public string StockItemId { get; set; }
        public int Amount { get; set; }
    }
    
    public class AllowItem
    {
        public string StockItemId { get; set; }
        public string Name { get; set; }
    }

    public class BanItem
    {
        public string StockItemId { get; set; }
    }
}

```

### File: Example\Domain\Events\StockItem.cs
```cs
﻿
namespace Example.Domain.Events
{
    public class ItemAllowed
    {
        public string StockItemId { get; set; }
        public string Name { get; set; }
    }

    public class ItemBanned
    {
        public string StockItemId { get; set; }
    }

    public class ItemsRemoved
    {
        public string StockItemId { get; set; }
        public int Amount { get; set; }
    }

    public class ItemsAdded
    {
        public string StockItemId { get; set; }
        public int Amount { get; set; }
    }
}

```

