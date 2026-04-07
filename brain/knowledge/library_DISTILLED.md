---
id: library
type: knowledge
owner: OA_Triage
---
# library
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![CircleCI](https://circleci.com/gh/ddd-by-examples/library.svg?style=svg)](https://circleci.com/gh/ddd-by-examples/library)
[![Code Coverage](https://codecov.io/gh/ddd-by-examples/library/branch/master/graph/badge.svg)](https://codecov.io/gh/ddd-by-examples/library)

# Table of contents

1. [About](#about)
2. [Domain description](#domain-description)
3. [General assumptions](#general-assumptions)  
    3.1 [Process discovery](#process-discovery)  
    3.2 [Project structure and architecture](#project-structure-and-architecture)    
    3.3 [Aggregates](#aggregates)  
    3.4 [Events](#events)  
    3.4.1 [Events in Repositories](#events-in-repositories)   
    3.5 [ArchUnit](#archunit)  
    3.6 [Functional thinking](#functional-thinking)  
    3.7 [No ORM](#no-orm)  
    3.8 [Architecture-code gap](#architecture-code-gap)  
    3.9 [Model-code gap](#model-code-gap)   
    3.10 [Spring](#spring)  
    3.11 [Tests](#tests)  
4. [How to contribute](#how-to-contribute)
5. [References](#references)

## About

This is a project of a library, driven by real [business requirements](#domain-description).
We use techniques strongly connected with Domain Driven Design, Behavior-Driven Development,
Event Storming, User Story Mapping. 

## Domain description

A public library allows patrons to place books on hold at its various library branches.
Available books can be placed on hold only by one patron at any given point in time.
Books are either circulating or restricted, and can have retrieval or usage fees.
A restricted book can only be held by a researcher patron. A regular patron is limited
to five holds at any given moment, while a researcher patron is allowed an unlimited number
of holds. An open-ended book hold is active until the patron checks out the book, at which time it
is completed. A closed-ended book hold that is not completed within a fixed number of 
days after it was requested will expire. This check is done at the beginning of a day by 
taking a look at daily sheet with expiring holds. Only a researcher patron can request
an open-ended hold duration. Any patron with more than two overdue checkouts at a library
branch will get a rejection if trying a hold at that same library branch. A book can be
checked out for up to 60 days. Check for overdue checkouts is done by taking a look at
daily sheet with overdue checkouts. Patron interacts with his/her current holds, checkouts, etc.
by taking a look at patron profile. Patron profile looks like a daily sheet, but the
information there is limited to one patron and is not necessarily daily. Currently a
patron can see current holds (not canceled nor expired) and current checkouts (including overdue).
Also, he/she is able to hold a book and cancel a hold.

How actually a patron knows which books are there to lend? Library has its catalogue of
books where books are added together with their specific instances. A specific book
instance of a book can be added only if there is book with matching ISBN already in
the catalogue.  Book must have non-empty title and price. At the time of adding an instance
we decide whether it will be Circulating or Restricted. This enables
us to have book with same ISBN as circulated and restricted at the same time (for instance,
there is a book signed by the author that we want to keep as Restricted)

## General assumptions

### Process discovery

The first thing we started with was domain exploration with the help of Big Picture EventStorming.
The description you found in the previous chapter, landed on our virtual wall:    
![Event Storming Domain description](docs/images/eventstorming-domain-desc.png)   
The EventStorming session led us to numerous discoveries, modeled with the sticky notes:  
![Event Storming Big Picture](docs/images/eventstorming-big-picture.jpg)   
During the session we discovered following definitions:  
![Event Storming Definitions](docs/images/eventstorming-definitions.png)    

This made us think of real life scenarios that might happen. We discovered them described with the help of
the **Example mapping**:  
![Example mapping](docs/images/example-mapping.png)  

This in turn became the base for our *Design Level* sessions, where we analyzed each example:  
![Example mapping](docs/images/eventstorming-design-level.jpg)  

Please follow the links below to get more details on each of the mentioned steps:
- [Big Picture EventStorming](./docs/big-picture.md)
- [Example Mapping](docs/example-mapping.md)
- [Design Level EventStorming](docs/design-level.md)

### Project structure and architecture
At the very beginning, not to overcomplicate the project, we decided to assign each bounded context
to a separate package, which means that the system is a modular monolith. There are no obstacles, though,
to put contexts into maven modules or finally into microservices.

Bounded contexts should (amongst others) introduce autonomy in the sense of architecture. Thus, each module
encapsulating the context has its own local architecture aligned to problem complexity.
In the case of a context, where we identified true business logic (**lending**) we introduced a domain model
that is a simplified (for the purpose of the project) abstraction of the reality and utilized
hexagonal architecture. In the case of a context, that during Event Storming turned out to lack any complex
domain logic, we applied CRUD-like local architecture.  

![Architecture](docs/images/architecture-big-picture.png) 

If we are talking about hexagonal architecture, it lets us separate domain and application logic from
frameworks (and infrastructure). What do we gain with this approach? Firstly, we can unit test most important
part of the application - **business logic** - usually without the need to stub any dependency.
Secondly, we create ourselves an opportunity to adjust infrastructure layer without the worry of
breaking the core functionality. In the infrastructure layer we intensively use Spring Framework
as probably the most mature and powerful application framework with an incredible test support.
More information about how we use Spring you will find [here](#spring).

As we already mentioned, the architecture was driven by Event Storming sessions. Apart from identifying
contexts and their complexity, we could also make a decision that we separate read and write models (CQRS).
As an example you can have a look at **Patron Profiles** and *Daily Sheets*.

### Aggregates
Aggregates discovered during Event Storming sessions communicate with each other with events. There is
a contention, though, should they be consistent immediately or eventually? As aggregates in general
determine business boundaries, eventual consistency sounds like a better choice, but choices in software
are never costless. Providing eventual consistency requires some infrastructural tools, like message broker
or event store. That's why we could (and did) start with immediate consistency.

> Good architecture is the one which postpones all important decisions

... that's why we made it easy to change the consistency model, providing tests for each option, including
basic implementations based on **DomainEvents** interface, which can be adjusted to our needs and
toolset in future. Let's have a look at following examples:

* Immediate consistency
    ```groovy
    def 'should synchronize Patron, Book and DailySheet with events'() {
        given:
            bookRepository.save(book)
        and:
            patronRepo.publish(patronCreated())
        when:
            patronRepo.publish(placedOnHold(book))
        then:
            patronShouldBeFoundInDatabaseWithOneBookOnHold(patronId)
        and:
            bookReactedToPlacedOnHoldEvent()
        and:
            dailySheetIsUpdated()
    }
    
    boolean bookReactedToPlacedOnHoldEvent() {
        return bookRepository.findBy(book.bookId).get() instanceof BookOnHold
    }
    
    boolean dailySheetIsUpdated() {
        return new JdbcTemplate(datasource).query("select count(*) from holds_sheet s where s.hold_by_patron_id = ?",
                [patronId.patronId] as Object[],
                new ColumnMapRowMapper()).get(0)
                .get("COUNT(*)") == 1
    }
    ```
   _Please note that here we are just reading from database right after events are being published_
   
   Simple implementation of the event bus is based on Spring application events:
    ```java
    @AllArgsConstructor
    public class JustForwardDomainEventPublisher implements DomainEvents {
    
        private final ApplicationEventPublisher applicationEventPublisher;
    
        @Override
        public void publish(DomainEvent event) {
            applicationEventPublisher.publishEvent(event);
        }
    }
    ```

* Eventual consistency
    ```groovy
    def 'should synchronize Patron, Book and DailySheet with events'() {
        given:
            bookRepository.save(book)
        and:
            patronRepo.publish(patronCreated())
        when:
            patronRepo.publish(placedOnHold(book))
        then:
            patronShouldBeFoundInDatabaseWithOneBookOnHold(patronId)
        and:
            bookReactedToPlacedOnHoldEvent()
        and:
            dailySheetIsUpdated()
    }
    
    void bookReactedToPlacedOnHoldEvent() {
        pollingConditions.eventually {
            assert bookRepository.findBy(book.bookId).get() instanceof BookOnHold
        }
    }
    
    void dailySheetIsUpdated() {
        pollingConditions.eventually {
            assert countOfHoldsInDailySheet() == 1
        }
    }
    ```
    _Please note that the test looks exactly the same as previous one, but now we utilized Groovy's
    **PollingConditions** to perform asynchronous functionality tests_

    Sample implementation of event bus is following:
    
    ```java
    @AllArgsConstructor
    public class StoreAndForwardDomainEventPublisher implements DomainEvents {
    
        private final JustForwardDomainEventPublisher justForwardDomainEventPublisher;
        private final EventsStorage eventsStorage;
    
        @Override
        public void publish(DomainEvent event) {
            eventsStorage.save(event);
        }
    
        @Scheduled(fixedRate = 3000L)
        @Transactional
        public void publishAllPeriodically() {
            List<DomainEvent> domainEvents = eventsStorage.toPublish();
            domainEvents.forEach(justForwardDomainEventPublisher::publish);
            eventsStorage.published(domainEvents);
        }
    }
    ```

To clarify, we should always aim for aggregates that can handle a business operation atomically
(transactionally if you like), so each aggregate should be as independent and decoupled from other
aggregates as possible. Thus, eventual consistency is promoted. As we already mentioned, it comes
with some tradeoffs, so from the pragmatic point of view immediate consistency is also a choice.
You might ask yourself a question now: _What if I don't have any events yet?_. Well, a pragmatic
approach would be to encapsulate the communication between aggregates in a _Service-like_ class,
where you could call proper aggregates line by line explicitly.

### Events
Talking about inter-aggregate communication, we must remember that events reduce coupling, but don't remove
it completely. Thus, it is very vital to share(publish) only those events, that are necessary for other
aggregates to exist and function. Otherwise there is a threat that the level of coupling will increase
introducing **feature envy**, because other aggregates might start using those events to perform actions
they are not supposed to perform. A solution to this problem could be the distinction of domain events
and integration events, which will be described here soon.  

### Events in Repositories 
Repositories are one of the most popular design pattern. They abstract our domain model from data layer. 
In other words, they deal with state. That said, a common use-case is when we pass a new state to our repository,
so that it gets persisted. It may look like so:

```java
public class BusinessService {
   
    private final PatronRepository patronRepository;
    
    void businessMethod(PatronId patronId) {
        Patron patron = patronRepository.findById(patronId);
        //do sth
        patronRepository.save(patron);
    }
}
```

Conceptually, between 1st and 3rd line of that business method we change state of our Patron from A to B. 
This change might be calculated by dirty checking or we might just override entire Patron state in the database. 
Third option is _Let's make implicit explicit_ and actually call this state change A->B an **event**. 
After all, event-driven architecture is all about promoting state changes as domain events.

Thanks to this our domain model may become immutable and just return events as results of invoking a command like so:

```java
public BookPlacedOnHold placeOnHold(AvailableBook book) {
      ...
}
```

And our repository might operate directly on events like so:

```java
public interface PatronRepository {
     void save(PatronEvent event) {
}
```

### ArchUnit

One of the main components of a successful project is technical leadership that lets the team go in the right
direction. Nevertheless, there are tools that can support teams in keeping the code clean and protect the
architecture, so that the project won't become a Big Ball of Mud, and thus will be pleasant to develop and
to maintain. The first option, the one we proposed, is [ArchUnit](https://www.archunit.org/) - a Java architecture
test tool. ArchUnit lets you write unit tests of your architecture, so that it is always consistent with initial
vision. Maven modules could be an alternative as well, but let's focus on the former.

In terms of hexagonal architecture, it is essential to ensure, that we do not mix different levels of
abstraction (hexagon levels):
```java 
@ArchTest
public static final ArchRule model_should_not_depend_on_infrastructure =
    noClasses()
        .that()
        .resideInAPackage("..model..")
        .should()
        .dependOnClassesThat()
        .resideInAPackage("..infrastructure..");
```      
and that frameworks do not affect the domain model  
```java
@ArchTest
public static final ArchRule model_should_not_depend_on_spring =
    noClasses()
        .that()
        .resideInAPackage("..io.pillopl.library.lending..model..")
        .should()
        .dependOnClassesThat()
        .resideInAPackage("org.springframework..");
```    

### Functional thinking
When you look at the code you might find a scent of functional programming. Although we do not follow
a _clean_ FP, we try to think of business processes as pipelines or workflows, utilizing functional style through
following concepts.

_Please note that this is not a reference project for FP._

#### Immutable objects
Each class that represents a business concept is immutable, thanks to which we:
* provide full encapsulation and objects' states protection,
* secure objects
... [TRUNCATED]
```

### File: Diabetes-Prediction-using-Machine-Learning_knowledge.md
```md
---
id: diabetes-prediction-using-machine-learning-knowled
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:21.208935
---

# KNOWLEDGE EXTRACT: Diabetes-Prediction-using-Machine-Learning
> **Extracted on:** 2026-03-29 20:30:41
> **Source:** Diabetes-Prediction-using-Machine-Learning

---

## File: `.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

## File: `Diabetes Prediction using Support Vector Machines.ipynb`
```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "a3a811ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.simplefilter('ignore')\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "287a0b31",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"diabetesdata.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "580fd291",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183</td>\n",
       "      <td>64</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89</td>\n",
       "      <td>66</td>\n",
       "      <td>23</td>\n",
       "      <td>94</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>168</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>763</th>\n",
       "      <td>10</td>\n",
       "      <td>101</td>\n",
       "      <td>76</td>\n",
       "      <td>48</td>\n",
       "      <td>180</td>\n",
       "      <td>32.9</td>\n",
       "      <td>0.171</td>\n",
       "      <td>63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>764</th>\n",
       "      <td>2</td>\n",
       "      <td>122</td>\n",
       "      <td>70</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>36.8</td>\n",
       "      <td>0.340</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>765</th>\n",
       "      <td>5</td>\n",
       "      <td>121</td>\n",
       "      <td>72</td>\n",
       "      <td>23</td>\n",
       "      <td>112</td>\n",
       "      <td>26.2</td>\n",
       "      <td>0.245</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>766</th>\n",
       "      <td>1</td>\n",
       "      <td>126</td>\n",
       "      <td>60</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30.1</td>\n",
       "      <td>0.349</td>\n",
       "      <td>47</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>767</th>\n",
       "      <td>1</td>\n",
       "      <td>93</td>\n",
       "      <td>70</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "      <td>30.4</td>\n",
       "      <td>0.315</td>\n",
       "      <td>23</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>768 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0              6      148             72             35        0  33.6   \n",
       "1              1       85             66             29        0  26.6   \n",
       "2              8      183             64              0        0  23.3   \n",
       "3              1       89             66             23       94  28.1   \n",
       "4              0      137             40             35      168  43.1   \n",
       "..           ...      ...            ...            ...      ...   ...   \n",
       "763           10      101             76             48      180  32.9   \n",
       "764            2      122             70             27        0  36.8   \n",
       "765            5      121             72             23      112  26.2   \n",
       "766            1      126             60              0        0  30.1   \n",
       "767            1       93             70             31        0  30.4   \n",
       "\n",
       "     DiabetesPedigreeFunction  Age  Outcome  \n",
       "0                       0.627   50        1  \n",
       "1                       0.351   31        0  \n",
       "2                       0.672   32        1  \n",
       "3                       0.167   21        0  \n",
       "4                       2.288   33        1  \n",
       "..                        ...  ...      ...  \n",
       "763                     0.171   63        0  \n",
       "764                     0.340   27        0  \n",
       "765                     0.245   30        0  \n",
       "766                     0.349   47        1  \n",
       "767                     0.315   23        0  \n",
       "\n",
       "[768 rows x 9 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "95c1147f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(768, 9)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "89081bf3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.845052</td>\n",
       "      <td>120.894531</td>\n",
       "      <td>69.105469</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>31.992578</td>\n",
       "      <td>0.471876</td>\n",
       "      <td>33.240885</td>\n",
       "      <td>0.348958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.369578</td>\n",
       "      <td>31.972618</td>\n",
       "      <td>19.355807</td>\n",
       "      <td>15.952218</td>\n",
       "      <td>115.244002</td>\n",
       "      <td>7.884160</td>\n",
       "      <td>0.331329</td>\n",
       "      <td>11.760232</td>\n",
       "      <td>0.476951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.078000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>0.243750</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>30.500000</td>\n",
       "      <td>32.000000</td>\n",
       "
... [TRUNCATED]
```

### File: End-to-End-Chest-Disease-Classification_knowledge.md
```md
---
id: end-to-end-chest-disease-classification-knowledge
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:21.908240
---

# KNOWLEDGE EXTRACT: End-to-End-Chest-Disease-Classification
> **Extracted on:** 2026-03-29 21:40:31
> **Source:** End-to-End-Chest-Disease-Classification

---

## File: `.dockerignore`
```
.github/
.jenkins/
docs/
Artifacts/
Logs/
Notebook_Experiments/
chestenv/
```

## File: `.dvcignore`
```
# Add patterns of files dvc should ignore, which could improve
# the performance. Learn more at
# https://dvc.org/doc/user-guide/dvcignore
```

## File: `.gitignore`
```
# Environments
chestenv
Notebook_Experiments/Data
mlruns
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

## File: `app.py`
```python
import os
from Respire.Utils import decodeImage
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, render_template
from Respire.Pipeline.Prediction_Pipeline import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #for AWS
```

## File: `docker-compose.yml`
```yaml
version: '3'
services:
  application:
    image: "${IMAGE_NAME}"
    ports:
      - "8080:8080"
```

## File: `Dockerfile`
```
FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
```

## File: `dvc.lock`
```
schema: '2.0'
stages:
  Data_Ingestion:
    cmd: python Respire\Pipeline\Data_Ingestion.py
    deps:
    - path: Config\config.yaml
      hash: md5
      md5: 0b75ac98a8aea3e04f42f671359b236c
      size: 560
    - path: Respire\Components\Data_Ingestion.py
      hash: md5
      md5: 64c516517af256dc44af001346813546
      size: 1439
    - path: Respire\Pipeline\Data_Ingestion.py
      hash: md5
      md5: 0380ed98a36cd2e9941f214f5c248017
      size: 591
    outs:
    - path: Artifacts\Data_Ingestion\Chest-CT-Scan-data
      hash: md5
      md5: 904fa45d934ce879b3b1933dca6cb2f1.dir
      size: 49247431
      nfiles: 343
  Base_Model:
    cmd: python Respire/Pipeline/Base_Model.py
    deps:
    - path: Config/config.yaml
      hash: md5
      md5: 0b75ac98a8aea3e04f42f671359b236c
      size: 560
    - path: Respire/Pipeline/Base_Model.py
      hash: md5
      md5: eb811c7cbed55a61c4db8f93b831c3c3
      size: 622
    params:
      params.yaml:
        CLASSES: 2
        IMAGE_SIZE:
        - 224
        - 224
        - 3
        INCLUDE_TOP: false
        LEARNING_RATE: 0.01
        WEIGHTS: imagenet
    outs:
    - path: Artifacts/Base_Model
      hash: md5
      md5: bc30f61379a1a1ef62f4989b315c189c.dir
      size: 118054560
      nfiles: 2
  Model_Training:
    cmd: python Respire/Pipeline/Model_Trainer.py
    deps:
    - path: Artifacts/Base_Model
      hash: md5
      md5: bc30f61379a1a1ef62f4989b315c189c.dir
      size: 118054560
      nfiles: 2
    - path: Artifacts/Data_Ingestion/Chest-CT-Scan-data
      hash: md5
      md5: 904fa45d934ce879b3b1933dca6cb2f1.dir
      size: 49247431
      nfiles: 343
    - path: Respire/Pipeline/Model_Trainer.py
      hash: md5
      md5: 003a73720aeeebec6d2034ff8374c07b
      size: 563
    - path: config/config.yaml
      hash: md5
      md5: 0b75ac98a8aea3e04f42f671359b236c
      size: 560
    params:
      params.yaml:
        AUGMENTATION: true
        BATCH_SIZE: 16
        EPOCHS: 2
        IMAGE_SIZE:
        - 224
        - 224
        - 3
    outs:
    - path: Artifacts/Model_Training/Trained_Model.h5
      hash: md5
      md5: 6b2b79135ff1d9a4bb30735e0c807888
      size: 59337520
  Model_Evaluation:
    cmd: python Respire/Pipeline/Model_Evaluation.py
    deps:
    - path: Artifacts/Data_Ingestion/Chest-CT-Scan-data
      hash: md5
      md5: 904fa45d934ce879b3b1933dca6cb2f1.dir
      size: 49247431
      nfiles: 343
    - path: Artifacts/Model_Training/Trained_model.h5
      hash: md5
      md5: 6b2b79135ff1d9a4bb30735e0c807888
      size: 59337520
    - path: Respire/Pipeline/Model_Evaluation.py
      hash: md5
      md5: addf806b28a72b94a8c8e2d7e471ca9b
      size: 557
    - path: config/config.yaml
      hash: md5
      md5: 0b75ac98a8aea3e04f42f671359b236c
      size: 560
    params:
      params.yaml:
        BATCH_SIZE: 16
        IMAGE_SIZE:
        - 224
        - 224
        - 3
    outs:
    - path: scores.json
      hash: md5
      md5: 62f2cefffb99b4b5cfc4c33d6d12e776
      size: 58
```

## File: `dvc.yaml`
```yaml
stages:

  Data_Ingestion:
    cmd: python Respire\Pipeline\Training_Pipeline\Data_Ingestion.py
    deps:
      - Respire\Pipeline\Training_Pipeline\Data_Ingestion.py
      - Respire\Components\Data_Ingestion.py
      - Config\config.yaml
    outs:
      - Artifacts\Data_Ingestion\Chest-CT-Scan-data
    
  Base_Model:
    cmd: python Respire\Pipeline\Training_Pipeline\Base_Model.py
    deps:
      - Respire\Pipeline\Training_Pipeline\Base_Model.py
      - Respire\Components\Base_Model.py
      - Config\config.yaml
    params:
      - IMAGE_SIZE
      - INCLUDE_TOP
      - CLASSES
      - WEIGHTS
      - LEARNING_RATE
    outs:
      - Artifacts\Base_Model

  
  Model_Training:
    cmd: python Respire\Pipeline\Training_Pipeline\Model_Trainer.py
    deps:
      - Respire\Pipeline\Training_Pipeline\Model_Trainer.py
      - config\config.yaml
      - Artifacts\Data_Ingestion\Chest-CT-Scan-data
      - Artifacts\Base_Model
    params:
      - IMAGE_SIZE
      - EPOCHS
      - BATCH_SIZE
      - AUGMENTATION
    outs:
      - Artifacts\Model_Training\Trained_Model.h5


  Model_Evaluation:
    cmd: python Respire\Pipeline\Training_Pipeline\Model_Evaluation.py
    deps:
      - Respire\Pipeline\Training_Pipeline\Model_Evaluation.py
      - config\config.yaml
      - Artifacts\Data_Ingestion\Chest-CT-Scan-data
      - Artifacts\Model_Training\Trained_model.h5
    params:
      - IMAGE_SIZE
      - BATCH_SIZE
    metrics:
    - scores.json:
        cache: false
```

## File: `main.py`
```python
from Respire.Logger import logging
from Respire.Pipeline.Training_Pipeline.Data_Ingestion import DataIngestionTrainingPipeline
from Respire.Pipeline.Training_Pipeline.Base_Model import PrepareBaseModelTrainingPipeline
from Respire.Pipeline.Training_Pipeline.Model_Trainer import ModelTrainingPipeline
from Respire.Pipeline.Training_Pipeline.Model_Evaluation import EvaluationPipeline


try:
    logging.info("<----------------- Data Ingestion Initiated ----------------->")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info("<----------------- Data Ingestion completed ----------------->")

    
    logging.info("<----------------- Base Model Preparation Initiated ----------------->")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info("<----------------- Base Model Preparation completed ----------------->")

    
    logging.info("<----------------- Model Training Initiated ----------------->")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logging.info("<----------------- Model Training completed ----------------->")

 
    logging.info("<----------------- Model Evaluation Initiated ----------------->")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logging.info("<----------------- Model Evaluation completed ----------------->")

except Exception as e:
    logging.exception(e)
    raise e
```

## File: `params.yaml`
```yaml
AUGMENTATION: True
IMAGE_SIZE: [224, 224, 3] # as per VGG 16 model
BATCH_SIZE: 16
INCLUDE_TOP: False
EPOCHS: 2
CLASSES: 2
WEIGHTS: imagenet
LEARNING_RATE: 0.01
```

## File: `README.md`
```markdown
# End-to-End-Chest-Disease-Classification
By [<b>Hema Kalyan Murapaka</b>](https://kalyanm45.github.io)

Connect with me on social media and explore my work:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/hemakalyan)&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/KalyanM45)&nbsp;
[![Medium](https://img.shields.io/badge/Medium-Follow-03a57a?style=flat-square&logo=medium)](https://medium.com/@kalyan45)&nbsp;
![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/mhemakalyan)
[![Sponsor Hema Kalyan Murapaka](https://img.shields.io/badge/Sponsor-Hema_Kalyan-28a745?style=flat-square&logo=github-sponsors)](https://github.com/sponsors/KalyanMurapaka45)

**Special Thanks to GitHub Sponsors**

## About The Project

Medical imaging has transformed healthcare by providing detailed insights into various diseases, particularly in the chest area. However, the current reliance on manual interpretation of imaging data by radiologists leads to delays, errors, and inefficiencies in diagnosing chest diseases. With a growing demand for healthcare services and a shortage of radiologists in some areas, there's an urgent need for automated systems to accurately detect and classify chest diseases from imaging data. These systems would not only improve diagnostic accuracy and efficiency but also alleviate strain on healthcare resources, enhancing patient care and outcomes.

## Library Requirements

 - Tensorflow==2.12.0
 - Pandas
 - GDown
 - DVC
 - MLFlow==2.2.2
 - Flask

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/KalyanM45/End-to-End-Chest-Disease-Classification.git
     ```

2. **Create a Virtual Environment** (Optional but recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
   - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
   - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.


### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. **Pull the Docker Image**
   - Open your terminal or command prompt.
   - Run the following command to pull the Docker image from DockerHub:
     ```
     docker pull kalyan45/Chest-detection-app
     ```
     This command downloads the Docker image from the DockerHub.

2. **Run the Docker Container**
   - Start the Docker container by running the following command. Adjust the port mapping as needed:
     ``
... [TRUNCATED]
```

### File: model-hierarchy-skill_knowledge.md
```md
---
id: model-hierarchy-skill-knowledge
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.046005
---

# KNOWLEDGE EXTRACT: model-hierarchy-skill
> **Extracted on:** 2026-03-29 22:08:37
> **Source:** model-hierarchy-skill

---

## File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/
.venv/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Zak Cole

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

## File: `pyproject.toml`
```
[project]
name = "model-hierarchy-skill"
version = "0.1.0"
description = "OpenClaw skill for cost-optimized model routing based on task complexity"
readme = "README.md"
license = {text = "MIT"}
authors = [{name = "Zak Cole", email = "zak@numbergroup.xyz"}]
requires-python = ">=3.9"

[project.optional-dependencies]
test = ["pytest>=7.0.0"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
addopts = "-v"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

## File: `README.md`
```markdown
# model-hierarchy-skill

Cost-optimize AI agent operations by routing tasks to appropriate models based on complexity.

## The Problem

Most AI agents run everything on expensive models. But 80% of agent tasks are routine: file reads, status checks, formatting, simple Q&A. You're paying $15-75/M tokens for work that $0.14/M tokens handles fine.

## The Solution

A skill that teaches agents to classify tasks and route them to the cheapest model that can handle them:

| Task Type | Model Tier | Cost | Examples |
|-----------|------------|------|----------|
| Routine (80%) | Cheap | $0.14-0.50/M | File ops, status checks, formatting |
| Moderate (15%) | Mid | $1-5/M | Code gen, summaries, drafts |
| Complex (5%) | Premium | $10-75/M | Debugging, architecture, novel problems |

**Result: ~10x cost reduction** with equivalent quality on the tasks that matter.

## Quick Start

### OpenClaw

```bash
# Copy SKILL.md to your skills directory
cp SKILL.md ~/.openclaw/skills/model-hierarchy/SKILL.md

# Restart gateway to pick up the skill
openclaw gateway restart
```

### Claude Code / Codex

Add to your `CLAUDE.md` or project instructions:

```markdown
## Model Routing

Before executing tasks, classify complexity:
- ROUTINE (file ops, lookups, formatting) → Use cheapest model
- MODERATE (code, summaries, analysis) → Use mid-tier model  
- COMPLEX (debugging, architecture, failures) → Use premium model

When spawning sub-agents, default to cheap models unless task requires more.
```

### Other Agent Systems

See [SKILL.md](SKILL.md) for the full classification rules and integration examples.

## Cost Math

Assuming 100K tokens/day:

| Strategy | Monthly Cost |
|----------|--------------|
| Pure Opus | ~$225 |
| Pure Sonnet | ~$45 |
| Hierarchy (80/15/5) | ~$19 |

## Testing

```bash
# Run classification tests
python -m pytest tests/ -v

# Test specific scenarios
python tests/test_classification.py
```

## Files

```
model-hierarchy-skill/
├── SKILL.md          # The skill (install this)
├── README.md         # You're here
├── tests/
│   ├── test_classification.py
│   └── scenarios.json
└── examples/
    ├── openclaw.md
    └── claude-code.md
```

## License

MIT
```

## File: `SKILL.md`
```markdown
---
name: model-hierarchy
description: >
  Cost-optimize AI agent operations by routing tasks to appropriate models based on complexity.
  Use this skill when: (1) deciding which model to use for a task, (2) spawning sub-agents,
  (3) considering cost efficiency, (4) the current model feels like overkill for the task.
  Triggers: "model routing", "cost optimization", "which model", "too expensive", "spawn agent".

---

# Model Hierarchy

Route tasks to the cheapest model that can handle them. Most agent work is routine.

## Core Principle

**80% of agent tasks are janitorial.** File reads, status checks, formatting, simple Q&A. These don't need expensive models. Reserve premium models for problems that actually require deep reasoning.

## Model Tiers

### Tier 1: Cheap ($0.10-0.50/M tokens)

| Model | Input | Output | Best For |
|-------|-------|--------|----------|
| DeepSeek V3 | $0.14 | $0.28 | General routine work |
| GPT-4o-mini | $0.15 | $0.60 | Quick responses |
| Claude Haiku | $0.25 | $1.25 | Fast tool use |
| Gemini Flash | $0.075 | $0.30 | High volume |
| GLM 5 (Zhipu) | (OpenRouter Z.AI) | (OpenRouter Z.AI) | Routine + moderate text; 200K context; **text-only** — do not use for image/vision |
| Kimi K2.5 (Moonshot) | $0.45 | $2.25 | Routine + moderate; 262K context; **multimodal (text + image + video)** |

**Text-only models (e.g. GLM 5):** Do not use for any task that requires image input or vision — no photo analysis, screenshots, image-generation tools, or document/chart vision. Route to a vision-capable model (e.g. Kimi K2.5, GPT-4o, Gemini, Claude with vision, GLM-4.5V/4.6V).

**Vision-capable Tier 1/2 (e.g. Kimi K2.5):** Use for routine or moderate tasks that may involve images — screenshots, photo analysis, docs, image-generation orchestration — without moving to premium vision models.

### Tier 2: Mid ($1-5/M tokens)

| Model | Input | Output | Best For |
|-------|-------|--------|----------|
| Claude Sonnet | $3.00 | $15.00 | Balanced performance |
| GPT-4o | $2.50 | $10.00 | Multimodal tasks |
| Gemini Pro | $1.25 | $5.00 | Long context |

### Tier 3: Premium ($10-75/M tokens)

| Model | Input | Output | Best For |
|-------|-------|--------|----------|
| Claude Opus | $15.00 | $75.00 | Complex reasoning |
| GPT-4.5 | $75.00 | $150.00 | Frontier tasks |
| o1 | $15.00 | $60.00 | Multi-step reasoning |
| o3-mini | $1.10 | $4.40 | Reasoning on budget |

*Prices as of Feb 2026. Check provider docs for current rates.*

## Task Classification

Before executing any task, classify it:

### ROUTINE → Use Tier 1

**Requires image/vision** → Do not assign to text-only models (GLM 5, etc.). Use a vision-capable model from Tier 1/2 or 3 (e.g. Kimi K2.5, GPT-4o, Gemini, Claude, GLM-4.5V).

Characteristics:
- Single-step operations
- Clear, unambiguous instructions
- No judgment required
- Deterministic output expected

Examples:
- File read/write operations
- Status checks and health monitoring
- Simple lookups (time, weather, definitions)
- Formatting and restructuring text
- List operations (filter, sort, transform)
- API calls with known parameters
- Heartbeat and cron tasks
- URL fetching and basic parsing

### MODERATE → Use Tier 2

Characteristics:
- Multi-step but well-defined
- Some synthesis required
- Standard patterns apply
- Quality matters but isn't critical

Examples:
- Code generation (standard patterns)
- Summarization and synthesis
- Draft writing (emails, docs, messages)
- Data analysis and transformation
- Multi-file operations
- Tool orchestration
- Code review (non-security)
- Search and research tasks

### COMPLEX → Use Tier 3

Characteristics:
- Novel problem solving required
- Multiple valid approaches
- Nuanced judgment calls
- High stakes or irreversible
- Previous attempts failed

Examples:
- Multi-step debugging
- Architecture and design decisions
- Security-sensitive code review
- Tasks where cheaper model already failed
- Ambiguous requirements needing interpretation
- Long-context reasoning (>50K tokens)
- Creative work requiring originality
- Adversarial or edge-case handling

## Decision Algorithm

```
function selectModel(task):
    # Rule 1: Vision override (Tier 1/2 includes text-only models)
    if task.requiresImageInput or task.requiresVision:
        return VISION_CAPABLE_MODEL  # e.g. Kimi K2.5, GPT-4o, Gemini, Claude; do not use GLM 5 or other text-only
    
    # Rule 2: Escalation override
    if task.previousAttemptFailed:
        return nextTierUp(task.previousModel)
    
    # Rule 3: Explicit complexity signals
    if task.hasSignal("debug", "architect", "design", "security"):
        return TIER_3
    
    if task.hasSignal("write", "code", "summarize", "analyze"):
        return TIER_2
    
    # Rule 4: Default classification
    complexity = classifyTask(task)
    
    if complexity == ROUTINE:
        return TIER_1
    elif complexity == MODERATE:
        return TIER_2
    else:
        return TIER_3
```

## Behavioral Rules

### For Main Session

1. **Default to Tier 2** for interactive work
2. **Suggest downgrade** when doing routine work: "This is routine - I can handle this on a cheaper model or spawn a sub-agent."
3. **Request upgrade** when stuck: "This needs more reasoning power. Switching to [premium model]."

### For Sub-Agents

1. **Default to Tier 1** unless task is clearly moderate+
2. **Batch similar tasks** to amortize overhead
3. **Report failures** back to parent for escalation

### For Automated Tasks

1. **Heartbeats/monitoring** → Always Tier 1
2. **Scheduled reports** → Tier 1 or 2 based on complexity
3. **Alert responses** → Start Tier 2, escalate if needed

## Communication Patterns

When suggesting model changes, use clear language:

**Downgrade suggestion:**
> "This looks like routine file work. Want me to spawn a sub-agent on DeepSeek for this? Same result, fraction of the cost."

**Upgrade request:**
> "I'm hitting the limits of what I can figure out here. This needs Opus-level reasoning. Switching up."

**Explaining hierarchy:**
> "I'm running the heavy analysis on Sonnet while sub-agents fetch the data on DeepSeek. Keeps costs down without sacrificing quality where it matters."

## Cost Impact

Assuming 100K tokens/day average usage:

| Strategy | Monthly Cost | Notes |
|----------|--------------|-------|
| Pure Opus | ~$225 | Maximum capability, maximum spend |
| Pure Sonnet | ~$45 | Good default for most work |
| Pure DeepSeek | ~$8 | Cheap but limited on hard problems |
| **Hierarchy (80/15/5)** | **~$19** | Best of all worlds |

The 80/15/5 split:
- 80% routine tasks on Tier 1 (~$6)
- 15% moderate tasks on Tier 2 (~$7)
- 5% complex tasks on Tier 3 (~$6)

**Result: 10x cost reduction vs pure premium, with equivalent quality on complex tasks.**

## Integration Examples

### OpenClaw

```yaml
# config.yml - set default model
model: anthropic/claude-sonnet-4

# In session, switch models
/model opus  # upgrade for complex task
/model deepseek  # downgrade for routine

# Spawn sub-agent on cheap model
sessions_spawn:
  task: "Fetch and parse these 50 URLs"
  model: deepseek
```

**OpenRouter (Tier 1 with vision or text-only):**

```yaml
# Tier 1 with vision — Kimi K2.5 (multimodal)
model: openrouter/moonshotai/kimi-k2.5
# Heartbeats, cron, image-involving tasks: K2.5 handles text and vision.

# Tier 1 text-only — GLM 5 (no vision)
# model: openrouter/z-ai/glm-5  # exact ID TBD on OpenRouter Z.AI
# Routine text-only only; for image tasks use Kimi K2.5 or another vision-capable model.
```

### Claude Code

```
# In CLAUDE.md or project instructions
When spawning background agents, use claude-3-haiku for:
- File operations
- Simple searches  
- Status checks

Reserve claude-sonnet-4 for:
- Code generation
- Analysis tasks
```

### General Agent Systems

```python
def get_model_for_task(task_description: str) -> str:
    routine_signals = ['read', 'fetch', 'check', 'list', 'format', 'status']
    complex_signals = ['debug', 'architect', 'design', 'security', 'why']
    
    desc_lower = task_description.lower()
    
    if any(signal in desc_lower for signal in complex_signals):
        return "claude-opus-4"
    elif any(signal in desc_lower for signal in routine_signals):
        return "deepseek-v3"
    else:
        return "claude-sonnet-4"
```

## Anti-Patterns

**DON'T:**
- Run heartbeats on Opus
- Use premium models for file I/O
- Keep expensive model when task is clearly routine
- Spawn sub-agents on premium models by default
- Use GLM 5 (or any text-only Tier 1/2 model) for image/vision tasks — e.g. photo analysis, screenshot understanding, image-generation skills, or any tool that takes image input

**DO:**
- Start mid-tier, adjust based on task
- Spawn helpers on cheapest viable model
- Escalate explicitly when stuck
- Track cost per task type to optimize further

## Extending This Skill

To customize for your use case:

1. **Adjust tier definitions** based on your provider/budget
2. **Add domain-specific signals** to classification rules
3. **Track actual complexity** vs predicted to improve heuristics
4. **Set budget alerts** to catch runaway premium usage
```

## File: `examples/claude-code.md`
```markdown
# Claude Code / Codex Integration

## Add to CLAUDE.md

Add this section to your project's `CLAUDE.md` or global instructions:

```markdown
## Model Routing

Before executing tasks, classify by complexity:

### ROUTINE (spawn on haiku/cheap)
- File read/write operations
- Status checks and lookups
- Formatting and list operations
- Simple Q&A

### MODERATE (use current model)
- Code generation
- Summarization
- Draft writing
- Data analysis

### COMPLEX (request upgrade if needed)
- Multi-step debugging
- Architecture decisions
- Security reviews
- Tasks where previous attempt failed

When spawning background agents, default to claude-3-haiku for routine work.
When stuck on a problem, suggest upgrading to opus.
```

## Behavioral Examples

### Routine Task

User: "Read config.json and show me the port number"

Agent behavior:
- Classifies as ROUTINE (file read + simple lookup)
- If on expensive model, suggests: "This is routine - I can spawn a background agent for this"
- Executes on cheapest available

### Moderate Task

User: "Write a Python function to validate email addresses"

Agent behavior:
- Classifies as MODERATE (code generation)
- Uses current mid-tier model
- No model change needed

### Complex Task

User: "This test p
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
