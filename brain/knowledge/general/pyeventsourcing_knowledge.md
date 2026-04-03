---
id: pyeventsourcing-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:04.109381
---

# KNOWLEDGE EXTRACT: pyeventsourcing
> **Extracted on:** 2026-03-30 17:51:30
> **Source:** pyeventsourcing

---

## File: `eventsourcing.md`
```markdown
# 📦 pyeventsourcing/eventsourcing [🔖 PENDING/APPROVE]
🔗 https://github.com/pyeventsourcing/eventsourcing
🌐 https://eventsourcing.readthedocs.io/

## Meta
- **Stars:** ⭐ 1643 | **Forks:** 🍴 141
- **Language:** Python | **License:** BSD-3-Clause
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A library for event sourcing in Python.

## README (trích đầu)
```
[![Build Status](https://github.com/pyeventsourcing/eventsourcing/actions/workflows/runtests.yaml/badge.svg?branch=9.5)](https://github.com/pyeventsourcing/eventsourcing)
[![Coverage Status](https://coveralls.io/repos/github/pyeventsourcing/eventsourcing/badge.svg?branch=main)](https://coveralls.io/github/pyeventsourcing/eventsourcing?branch=main)
[![Documentation Status](https://readthedocs.org/projects/eventsourcing/badge/?version=stable)](https://eventsourcing.readthedocs.io/en/stable/)
[![Latest Release](https://badge.fury.io/py/eventsourcing.svg)](https://pypi.org/project/eventsourcing/)
[![Downloads](https://static.pepy.tech/personalized-badge/eventsourcing?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads)](https://pypistats.org/packages/eventsourcing)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# Event Sourcing in Python

This project is a comprehensive Python library for implementing event sourcing, a design pattern where all
changes to application state are stored as a sequence of events. This library provides a solid foundation
for building event-sourced applications in Python, with a focus on reliability, performance, and developer
experience. Please [read the docs](https://eventsourcing.readthedocs.io/). See also [extension projects](https://github.com/pyeventsourcing).

*"totally amazing and a pleasure to use"*

*"very clean and intuitive"*

*"a huge help and time saver"*

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/pyeventsourcing/eventsourcing)


## Installation

Use pip to install the [stable distribution](https://pypi.org/project/eventsourcing/)
from the Python Package Index.

    $ pip install eventsourcing

Please note, it is recommended to install Python
packages into a Python virtual environment.


## Synopsis

Define aggregates with the `Aggregate` class and the `@event` decorator.

```python
from eventsourcing.domain import Aggregate, event

class Dog(Aggregate):
    @event('Registered')
    def __init__(self, name: str) -> None:
        self.name = name
        self.tricks: list[str] = []

    @event('TrickAdded')
    def add_trick(self, trick: str) -> None:
        self.tricks.append(trick)
```

Define application objects with the `Application` class.

```python
from typing import Any
from uuid import UUID

from eventsourcing.application import Application


class DogSchool(Application[UUID]):
    def register_dog(self, name: str) -> UUID:
        dog = Dog(name)
        self.save(dog)
        return dog.id

    def add_trick(self, dog_id: UUID, trick: str) -> None:
        dog: Dog = self.repository.get(dog_id)
        dog.add_trick(trick)
        self.save(dog)

    def get_dog(self, dog_id: UUID) -> dict[str, Any]:
        dog: Dog = self.repository.get(dog_id)
        return {'name': dog.name, 'tricks': tuple(dog.tricks)}
```

Write a test.

```python
def test_dog_school(
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

