---
id: fast-graphrag
type: knowledge
owner: OA_Triage
---
# fast-graphrag
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h1 align="center">
  <img width="800" src="banner.png" alt="circlemind fast-graphrag">
</h1>
<h4 align="center">
  <a href="https://github.com/circlemind-ai/fast-graphrag/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="fast-graphrag is released under the MIT license." alt="Fast GraphRAG by Circlemind"/>
  </a>
  <a href="https://github.com/circlemind-ai/fast-graphrag/blob/main/CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen" alt="PRs welcome!" />
  </a>
  <a href="https://circlemind.co">
    <img src="https://img.shields.io/badge/Project-Page-Green" alt="Circlemind Page" />
  </a>
  <img src="https://img.shields.io/badge/python->=3.10.1-blue">
</h4>
<p align="center">
  <p align="center"><b>Streamlined and promptable Fast GraphRAG framework designed for interpretable, high-precision, agent-driven retrieval workflows. </b> </p>
</p>

<h4 align="center">
  <a href="#install">Install</a> |
  <a href="#quickstart">Quickstart</a> |
  <a href="https://discord.gg/DvY2B8u4sA">Community</a> |
  <a href="https://github.com/circlemind-ai/fast-graphrag/issues/new?assignees=&labels=&projects=&template=%F0%9F%90%9E-bug-report.md&title=">Report Bug</a> |
  <a href="https://github.com/circlemind-ai/fast-graphrag/issues/new?assignees=&labels=&projects=&template=%F0%9F%92%A1-feature-request.md&title=">Request Feature</a>
</h4>

> [!NOTE]
> Using *The Wizard of Oz*, `fast-graphrag` costs $0.08 vs. `graphrag` $0.48 — **a 6x costs saving** that further improves with data size and number of insertions.

## Features

- **Interpretable and Debuggable Knowledge:** Graphs offer a human-navigable view of knowledge that can be queried, visualized, and updated.
- **Fast, Low-cost, and Efficient:** Designed to run at scale without heavy resource or cost requirements.
- **Dynamic Data:** Automatically generate and refine graphs to best fit your domain and ontology needs.
- **Incremental Updates:** Supports real-time updates as your data evolves.
- **Intelligent Exploration:** Leverages PageRank-based graph exploration for enhanced accuracy and dependability.
- **Asynchronous & Typed:** Fully asynchronous, with complete type support for robust and predictable workflows.

Fast GraphRAG is built to fit seamlessly into your retrieval pipeline, giving you the power of advanced RAG, without the overhead of building and designing agentic workflows.

## Install

**Install from source (recommended for best performance)**

```bash
# clone this repo first
cd fast_graphrag
poetry install
```

**Install from PyPi (recommended for stability)**

```bash
pip install fast-graphrag
```

## Quickstart

Set the OpenAI API key in the environment:

```bash
export OPENAI_API_KEY="sk-..."
```

Download a copy of *A Christmas Carol* by Charles Dickens:

```bash
curl https://raw.githubusercontent.com/circlemind-ai/fast-graphrag/refs/heads/main/mock_data.txt > ./book.txt
```

Optional: Set the limit for concurrent requests to the LLM (i.e., to control the number of tasks processed simultaneously by the LLM, this is helpful when running local models)
```bash
export CONCURRENT_TASK_LIMIT=8
```

Use the Python snippet below:

```python
from fast_graphrag import GraphRAG

DOMAIN = "Analyze this story and identify the characters. Focus on how they interact with each other, the locations they explore, and their relationships."

EXAMPLE_QUERIES = [
    "What is the significance of Christmas Eve in A Christmas Carol?",
    "How does the setting of Victorian London contribute to the story's themes?",
    "Describe the chain of events that leads to Scrooge's transformation.",
    "How does Dickens use the different spirits (Past, Present, and Future) to guide Scrooge?",
    "Why does Dickens choose to divide the story into \"staves\" rather than chapters?"
]

ENTITY_TYPES = ["Character", "Animal", "Place", "Object", "Activity", "Event"]

grag = GraphRAG(
    working_dir="./book_example",
    domain=DOMAIN,
    example_queries="\n".join(EXAMPLE_QUERIES),
    entity_types=ENTITY_TYPES
)

with open("./book.txt") as f:
    grag.insert(f.read())

print(grag.query("Who is Scrooge?").response)
```

The next time you initialize fast-graphrag from the same working directory, it will retain all the knowledge automatically.

## Examples
Please refer to the `examples` folder for a list of tutorials on common use cases of the library:
- `custom_llm.py`: a brief example on how to configure fast-graphrag to run with different OpenAI API compatible language models and embedders;
- `checkpointing.ipynb`: a tutorial on how to use checkpoints to avoid irreversible data corruption;
- `query_parameters.ipynb`: a tutorial on how to use the different query parameters. In particular, it shows how to include references to the used information in the provided answer (using the `with_references=True` parameter). 

## Contributing

Whether it's big or small, we love contributions. Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. Check out our [guide](https://github.com/circlemind-ai/fast-graphrag/blob/main/CONTRIBUTING.md) to see how to get started.

Not sure where to get started? You can join our [Discord](https://discord.gg/DvY2B8u4sA) and ask us any questions there.

## Philosophy

Our mission is to increase the number of successful GenAI applications in the world. To do that, we build memory and data tools that enable LLM apps to leverage highly specialized retrieval pipelines without the complexity of setting up and maintaining agentic workflows.

Fast GraphRAG currently exploit the personalized pagerank algorithm to explore the graph and find the most relevant pieces of information to answer your query. For an overview on why this works, you can check out the HippoRAG paper [here](https://arxiv.org/abs/2405.14831).

## Open-source or Managed Service

This repo is under the MIT License. See [LICENSE.txt](https://github.com/circlemind-ai/fast-graphrag/blob/main/LICENSE) for more information.

The fastest and most reliable way to get started with Fast GraphRAG is using our managed service. Your first 100 requests are free every month, after which you pay based on usage.

<h1 align="center">
  <img width="800" src="demo.gif" alt="circlemind fast-graphrag demo">
</h1>

To learn more about our managed service, [book a demo](https://circlemind.co/demo) or see our [docs](https://docs.circlemind.co/quickstart).

```

### File: benchmarks\README.md
```md
## Benchmarks
We validate the benchmark results provided in [HippoRAG](https://arxiv.org/abs/2405.14831), as well as comparing with other methods:
- NaiveRAG (vector dbs) using the OpenAI embedder `text-embedding-3-small`
- [LightRAG](https://github.com/HKUDS/LightRAG) 
- [GraphRAG](https://github.com/gusye1234/nano-graphrag) (we use the implementation provided by `nano-graphrag`, based on the original [Microsoft GraphRAG](https://github.com/microsoft/graphrag))

### Results
**2wikimultihopQA**
| # Queries |  Method  | All queries % | Multihop only % |
|----------:|:--------:|--------------:|----------------:|
|         51||||
|           |  VectorDB|           0.49|             0.32|
|           |  LightRAG|           0.47|             0.32|
|           |  GraphRAG|           0.75|             0.68|
|           |**Circlemind**|           **0.96**|             **0.95**|
|        101||||
|           |  VectorDB|           0.42|             0.23|
|           |  LightRAG|           0.45|             0.28|
|           |  GraphRAG|           0.73|             0.64|
|           |**Circlemind**|           **0.93**|             **0.90**|

**Circlemind is up to 4x more accurate than VectorDB RAG.**

**HotpotQA**
| # Queries |  Method  | All queries % |
|----------:|:--------:|--------------:|
|        101|||
|           |  VectorDB|           0.78|
|           |  LightRAG|           0.55|
|           |  GraphRAG|             -*|
|           |**Circlemind**|           **0.84**|

*: crashes after half an hour of processing

Below, find the insertion times for the 2wikimultihopqa benchmark (~800 chunks):
|  Method  |  Time (minutes)  |
|:--------:|-----------------:|
|  VectorDB|              ~0.3|
|  LightRAG|               ~25|
|  GraphRAG|               ~40|
|**Circlemind**|              ~1.5|

**Circlemind is 27x faster than GraphRAG while also being over 40% more accurate in retrieval.**

### Run it yourself
The scripts in this directory will generate and evaluate the 2wikimultihopqa datasets on a subsets of 51 and 101 queries with the same methodology as in the HippoRAG paper. In particular, we evaluate the retrieval capabilities of each method, mesauring the percentage of queries for which all the required evidence was retrieved. We preloaded the results so it is enough to run `evaluate_dbs.xx` to get the numbers. You can also run `create_dbs.xx` to regenerate the databases for the different methods.  

A couple of NOTES:
- you will need to set an OPENAI_API_KEY;
- LightRAG and GraphRAG could take a over an 1 hour to process and they can be expensive;
- when pip installing LightRAG, not all dependencies are added; to run it we simply deleted all the imports of each missing dependency (since we use OpenAI they are not necessary).
- we also benchmarked on the HotpotQA dataset (we will soon release the code for that as well).

The output will look similar to the following (the exact numbers could vary based on your graph configuration)
```
Evaluation of the performance of different RAG methods on 2wikimultihopqa (51 queries)

VectorDB
Loading dataset...
[all questions] Percentage of queries with perfect retrieval: 0.49019607843137253
[multihop only] Percentage of queries with perfect retrieval: 0.32432432432432434

LightRAG [local mode]
Loading dataset...
Percentage of queries with perfect retrieval: 0.47058823529411764
[multihop only] Percentage of queries with perfect retrieval: 0.32432432432432434

GraphRAG [local mode]
Loading dataset...
[all questions] Percentage of queries with perfect retrieval: 0.7450980392156863
[multihop only] Percentage of queries with perfect retrieval: 0.6756756756756757

Circlemind
Loading dataset...
[all questions] Percentage of queries with perfect retrieval: 0.9607843137254902
[multihop only] Percentage of queries with perfect retrieval: 0.9459459459459459


Evaluation of the performance of different RAG methods on 2wikimultihopqa (101 queries)

VectorDB
Loading dataset...
[all questions] Percentage of queries with perfect retrieval: 0.4158415841584158
[multihop only] Percentage of queries with perfect retrieval: 0.2318840579710145

LightRAG [local mode]
Loading dataset...
[all questions] Percentage of queries with perfect retrieval: 0.44554455445544555
[multihop only] Percentage of queries with perfect retrieval: 0.2753623188405797

GraphRAG [local mode]
Loading dataset...
[all questions] Percentage of queries with perfect retrieval: 0.7326732673267327
[multihop only] Percentage of queries with perfect retrieval: 0.6376811594202898

Circlemind
Loading dataset...
[all questions] Percentage of queries with perfect retrieval: 0.9306930693069307
[multihop only] Percentage of queries with perfect retrieval: 0.8985507246376812
```

```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct - Fast GraphRAG

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to make participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behaviour that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologising to those affected by our mistakes,
and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
overall community

Examples of unacceptable behaviour include:

* The use of sexualised language or imagery, and sexual attention or advances
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying and enforcing our standards of
acceptable behaviour and will take appropriate and fair corrective action in
response to any instances of unacceptable behaviour.

Project maintainers have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, or to ban
temporarily or permanently any contributor for other behaviours that they deem
inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behaviour may be
reported to the community leaders responsible for enforcement at .
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://contributor-covenant.org/), version
[1.4](https://www.contributor-covenant.org/version/1/4/code-of-conduct/code_of_conduct.md) and
[2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.md),
and was generated by [contributing-gen](https://github.com/bttger/contributing-gen).

```

### File: CONTRIBUTING.md
```md
<!-- omit in toc -->
# Contributing to Fast GraphRAG

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->
## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Code Contribution](#your-first-code-contribution)
- [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
- [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)


## Code of Conduct

This project and everyone participating in it is governed by the
[Fast GraphRAG Code of Conduct](https://github.com/circlemind-ai/fast-graphrag/blob/main/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to .


## I Have a Question

First off, make sure to join the discord community: https://discord.gg/McpuSEkR

Before you ask a question, it is best to search for existing [Issues](https://github.com/circlemind-ai/fast-graphrag/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/circlemind-ai/fast-graphrag/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (python, os, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.

## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project licence.

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions. If you are looking for support, you might want to check Discord first.
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/circlemind-ai/fast-graphrag/issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect all important information about the bug

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to security@circlemind.co

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/circlemind-ai/fast-graphrag/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).

<!-- You might want to create an issue template for bugs and errors that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Fast GraphRAG, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Perform a [search](https://github.com/circlemind-ai/fast-graphrag/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/circlemind-ai/fast-graphrag/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- **Explain why this enhancement would be useful** to most Fast GraphRAG users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

```

### File: mock_data.txt
```txt
A CHRISTMAS CAROL

CHARACTERS

Bob Cratchit, clerk to Ebenezer Scrooge.
Peter Cratchit, a son of the preceding.
Tim Cratchit ("Tiny Tim"), a cripple, youngest son of Bob Cratchit.
Mr. Fezziwig, a kind-hearted, jovial old merchant.
Fred, Scrooge's nephew.
Ghost of Christmas Past, a phantom showing things past.
Ghost of Christmas Present, a spirit of a kind, generous,
and hearty nature.
Ghost of Christmas Yet to Come, an apparition showing the shadows
of things which yet may happen.
Ghost of Jacob Marley, a spectre of Scrooge's former partner in business.
Joe, a marine-store dealer and receiver of stolen goods.
Ebenezer Scrooge, a grasping, covetous old man, the surviving partner
of the firm of Scrooge and Marley.
Mr. Topper, a bachelor.
Dick Wilkins, a fellow apprentice of Scrooge's.

Belle, a comely matron, an old sweetheart of Scrooge's.
Caroline, wife of one of Scrooge's debtors.
Mrs. Cratchit, wife of Bob Cratchit.
Belinda and Martha Cratchit, daughters of the preceding.

Mrs. Dilber, a laundress.
Fan, the sister of Scrooge.
Mrs. Fezziwig, the worthy partner of Mr. Fezziwig.

STAVE ONE




MARLEY'S GHOST


Marley was dead, to begin with. There is no doubt whatever about that.
The register of his burial was signed by the clergyman, the clerk, the
undertaker, and the chief mourner. Scrooge signed it. And Scrooge's name
was good upon 'Change for anything he chose to put his hand to. Old
Marley was as dead as a door-nail.

Mind! I don't mean to say that I know of my own knowledge, what there is
particularly dead about a door-nail. I might have been inclined, myself,
to regard a coffin-nail as the deadest piece of ironmongery in the
trade. But the wisdom of our ancestors is in the simile; and my
unhallowed hands shall not disturb it, or the country's done for. You
will, therefore, permit me to repeat, emphatically, that Marley was as
dead as a door-nail.

Scrooge knew he was dead? Of course he did. How could it be otherwise?
Scrooge and he were partners for I don't know how many years. Scrooge
was his sole executor, his sole administrator, his sole assign, his sole
residuary legatee, his sole friend, and sole mourner. And even Scrooge
was not so dreadfully cut up by the sad event but that he was an
excellent man of business on the very day of the funeral, and solemnised
it with an undoubted bargain.

The mention of Marley's funeral brings me back to the point I started
from. There is no doubt that Marley was dead. This must be distinctly
understood, or nothing wonderful can come of the story I am going to
relate. If we were not perfectly convinced that Hamlet's father died
before the play began, there would be nothing more remarkable in his
taking a stroll at night, in an easterly wind, upon his own ramparts,
than there would be in any other middle-aged gentleman rashly turning
out after dark in a breezy spot--say St. Paul's Churchyard, for
instance--literally to astonish his son's weak mind.

Scrooge never painted out Old Marley's name. There it stood, years
afterwards, above the warehouse door: Scrooge and Marley. The firm was
known as Scrooge and Marley. Sometimes people new to the business called
Scrooge Scrooge, and sometimes Marley, but he answered to both names. It
was all the same to him.

Oh! but he was a tight-fisted hand at the grindstone, Scrooge! a
squeezing, wrenching, grasping, scraping, clutching, covetous old
sinner! Hard and sharp as flint, from which no steel had ever struck out
generous fire; secret, and self-contained, and solitary as an oyster.
The cold within him froze his old features, nipped his pointed nose,
shrivelled his cheek, stiffened his gait; made his eyes red, his thin
lips blue; and spoke out shrewdly in his grating voice. A frosty rime
was on his head, and on his eyebrows, and his wiry chin. He carried his
own low temperature always about with him; he iced his office in the
dog-days, and didn't thaw it one degree at Christmas.

External heat and cold had little influence on Scrooge. No warmth could
warm, no wintry weather chill him. No wind that blew was bitterer than
he, no falling snow was more intent upon its purpose, no pelting rain
less open to entreaty. Foul weather didn't know where to have him. The
heaviest rain, and snow, and hail, and sleet could boast of the
advantage over him in only one respect. They often 'came down'
handsomely, and Scrooge never did.

Nobody ever stopped him in the street to say, with gladsome looks, 'My
dear Scrooge, how are you? When will you come to see me?' No beggars
implored him to bestow a trifle, no children asked him what it was
o'clock, no man or woman ever once in all his life inquired the way to
such and such a place, of Scrooge. Even the blind men's dogs appeared to
know him; and, when they saw him coming on, would tug their owners into
doorways and up courts; and then would wag their tails as though they
said, 'No eye at all is better than an evil eye, dark master!'

But what did Scrooge care? It was the very thing he liked. To edge his
way along the crowded paths of life, warning all human sympathy to keep
its distance, was what the knowing ones call 'nuts' to Scrooge.

Once upon a time--of all the good days in the year, on Christmas
Eve--old Scrooge sat busy in his counting-house. It was cold, bleak,
biting weather; foggy withal; and he could hear the people in the court
outside go wheezing up and down, beating their hands upon their breasts,
and stamping their feet upon the pavement stones to warm them. The City
clocks had only just gone three, but it was quite dark already--it had
not been light all day--and candles were flaring in the windows of the
neighbouring offices, like ruddy smears upon the palpable brown air. The
fog came pouring in at every chink and keyhole, and was so dense
without, that, although the court was of the narrowest, the houses
opposite were mere phantoms. To see the dingy cloud come drooping down,
obscuring everything, one might have thought that nature lived hard by,
and was brewing on a large scale.

The door of Scrooge's counting-house was open, that he might keep his
eye upon his clerk, who in a dismal little cell beyond, a sort of tank,
was copying letters. Scrooge had a very small fire, but the clerk's fire
was so very much smaller that it looked like one coal. But he couldn't
replenish it, for Scrooge kept the coal-box in his own room; and so
surely as the clerk came in with the shovel, the master predicted that
it would be necessary for them to part. Wherefore the clerk put on his
white comforter, and tried to warm himself at the candle; in which
effort, not being a man of strong imagination, he failed.

'A merry Christmas, uncle! God save you!' cried a cheerful voice. It was
the voice of Scrooge's nephew, who came upon him so quickly that this
was the first intimation he had of his approach.

'Bah!' said Scrooge. 'Humbug!'

He had so heated himself with rapid walking in the fog and frost, this
nephew of Scrooge's, that he was all in a glow; his face was ruddy and
handsome; his eyes sparkled, and his breath smoked again.

'Christmas a humbug, uncle!' said Scrooge's nephew. 'You don't mean
that, I am sure?'

'I do,' said Scrooge. 'Merry Christmas! What right have you to be merry?
What reason have you to be merry? You're poor enough.'

'Come, then,' returned the nephew gaily. 'What right have you to be
dismal? What reason have you to be morose? You're rich enough.'

Scrooge, having no better answer ready on the spur of the moment, said,
'Bah!' again; and followed it up with 'Humbug!'

'Don't be cross, uncle!' said the nephew.

'What else can I be,' returned the uncle, 'when I live in such a world
of fools as this? Merry Christmas! Out upon merry Christmas! What's
Christmas-time to you but a time for paying bills without money; a time
for finding yourself a year older, and not an hour richer; a time for
balancing your books, and having every item in 'em through a round dozen
of months presented dead against you? If I could work my will,' said
Scrooge indignantly, 'every idiot who goes about with "Merry Christmas"
on his lips should be boiled with his own pudding, and buried with a
stake of holly through his heart. He should!'

'Uncle!' pleaded the nephew.

'Nephew!' returned the uncle sternly, 'keep Christmas in your own way,
and let me keep it in mine.'

'Keep it!' repeated Scrooge's nephew. 'But you don't keep it.'

'Let me leave it alone, then,' said Scrooge. 'Much good may it do you!
Much good it has ever done you!'

'There are many things from which I might have derived good, by which I
have not profited, I dare say,' returned the nephew; 'Christmas among
the rest. But I am sure I have always thought of Christmas-time, when
it has come round--apart from the veneration due to its sacred name and
origin, if anything belonging to it can be apart from that--as a good
time; a kind, forgiving, charitable, pleasant time; the only time I know
of, in the long calendar of the year, when men and women seem by one
consent to open their shut-up hearts freely, and to think of people
below them as if they really were fellow-passengers to the grave, and
not another race of creatures bound on other journeys. And therefore,
uncle, though it has never put a scrap of gold or silver in my pocket, I
believe that it _has_ done me good and _will_ do me good; and I say, God
bless it!'

The clerk in the tank involuntarily applauded. Becoming immediately
sensible of the impropriety, he poked the fire, and extinguished the
last frail spark for ever.

'Let me hear another sound from _you_,' said Scrooge, 'and you'll keep
your Christmas by losing your situation! You're quite a powerful
speaker, sir,' he added, turning to his nephew. 'I wonder you don't go
into Parliament.'

'Don't be angry, uncle. Come! Dine with us to-morrow.'

Scrooge said that he would see him----Yes, indeed he did. He went the
whole length of the expression, and said that he would see him in that
extremity first.

'But why?' cried Scrooge's nephew. 'Why?'

'Why did you get married?' said Scrooge.

'Because I fell in love.'

'Because you fell in love!' growled Scrooge, as if that were the only
one thing in the world more ridiculous than a merry Christmas. 'Good
afternoon!'

'Nay, uncle, but you never came to see me before that happened. Why give
it as a reason for not coming now?'

'Good afternoon,' said Scrooge.

'I want nothing from you; I ask nothing of you; why cannot we be
friends?'

'Good afternoon!' said Scrooge.

'I am sorry, with all my heart, to find you so resolute. We have never
had any quarrel to which I have been a party. But I have made the trial
in homage to Christmas, and I'll keep my Christmas humour to the last.
So A Merry Christmas, uncle!'

'Good afternoon,' said Scrooge.

'And A Happy New Year!'

'Good afternoon!' said Scrooge.

His nephew left the room without an angry word, notwithstanding. He
stopped at the outer door to bestow the greetings of the season on the
clerk, who, cold as he was, was warmer than Scrooge; for he returned
them cordially.

'There's another fellow,' muttered Scrooge, who overheard him: 'my
clerk, with fifteen shillings a week, and a wife and family, talking
about a merry Christmas. I'll retire to Bedlam.'

This lunatic, in letting Scrooge's nephew out, had let two other people
in. They were portly gentlemen, pleasant to behold, and now stood, with
their hats off, in Scrooge's office. They had books and papers in their
hands, and bowed to him.

'Scrooge and Marley's, I believe,' said one of the gentlemen, referring
to his list. 'Have I the pleasure of addressing Mr. Scrooge, or Mr.
Marley?'

'Mr. Marley has been dead these seven years,' Scrooge replied. 'He died
seven years ago, this very night.'

'We have no doubt his liberality is well represented by his surviving
partner,' said the gentleman, presenting his credentials.


It certainly was; for they had been two kindred spirits. At the ominous
word 'liberality' Scrooge frowned, and shook his head, and handed the
credentials back.

'At this festive season of the year, Mr. Scrooge,' said the gentleman,
taking up a pen, 'it is more than usually desirable that we should make
some slight provision for the poor and destitute, who suffer greatly at
the present time. Many thousands are in want of common necessaries;
hundreds of thousands are in want of common comforts, sir.'

'Are there no prisons?' asked Scrooge.

'Plenty of prisons,' said the gentleman, laying down the pen again.

'And the Union workhouses?' demanded Scrooge. 'Are they still in
operation?'

'They are. Still,' returned the gentleman, 'I wish I could say they were
not.'

'The Treadmill and the Poor Law are in full vigour, then?' said Scrooge.

'Both very busy, sir.'

'Oh! I was afraid, from what you said at first, that something had
occurred to stop them in their useful course,' said Scrooge. 'I am very
glad to hear it.'

'Under the impression that they scarcely furnish Christian cheer of mind
or body to the multitude,' returned the gentleman, 'a few of us are
endeavouring to raise a fund to buy the Poor some meat and drink, and
means of warmth. We choose this time, because it is a time, of all
others, when Want is keenly felt, and Abundance rejoices. What shall I
put you down for?'

'Nothing!' Scrooge replied.

'You wish to be anonymous?'

'I wish to be left alone,' said Scrooge. 'Since you ask me what I wish,
gentlemen, that is my answer. I don't make merry myself at Christmas,
and I can't afford to make idle people merry. I help to support the
establishments I have mentioned--they cost enough: and those who are
badly off must go there.'

'Many can't go there; and many would rather die.'

'If they would rather die,' said Scrooge, 'they had better do it, and
decrease the surplus population. Besides--excuse me--I don't know that.'

'But you might know it,' observed the gentleman.

'It's not my business,' Scrooge returned. 'It's enough for a man to
understand his own business, and not to interfere with other people's.
Mine occupies me constantly. Good afternoon, gentlemen!'

Seeing clearly that it would be useless to pursue their point, the
gentlemen withdrew. Scrooge resumed his labours with an improved opinion
of himself, and in a more facetious temper than was usual with him.

Meanwhile the fog and darkness thickened so, that people ran about with
flaring links, proffering their services to go before horses in
carriages, and conduct them on their way. The ancient tower of a church,
whose gruff old bell was always peeping slyly down at Scrooge out of a
Gothic window in the wall, became invisible, and struck the hours and
quarters in the clouds, with tremulous vibrations afterwards, as if its
teeth were chattering in its frozen head up there. The cold became
intense. In the main street, at the corner of the court, some labourers
were repairing the gas-pipes, and had lighted a great fire in a brazier,
round which a party of ragged men and boys were gathered: warming their
hands and winking their ey
... [TRUNCATED]
```

### File: benchmarks\create_dbs.sh
```sh
# 2wikimultihopqa benchmark
# Creating databases
python vdb_benchmark.py -n 51 -c
python vdb_benchmark.py -n 101 -c
python lightrag_benchmark.py -n 51 -c
python lightrag_benchmark.py -n 101 -c
python nano_benchmark.py -n 51 -c
python nano_benchmark.py -n 101 -c
python graph_benchmark.py -n 51 -c
python graph_benchmark.py -n 101 -c

# Evaluation (create reports)
python vdb_benchmark.py -n 51 -b
python vdb_benchmark.py -n 101 -b
python lightrag_benchmark.py -n 51 -b --mode=local
python lightrag_benchmark.py -n 101 -b --mode=local
python nano_benchmark.py -n 51 -b --mode=local
python nano_benchmark.py -n 101 -b --mode=local
python graph_benchmark.py -n 51 -b
python graph_benchmark.py -n 101 -b
```

### File: benchmarks\evaluate_dbs.sh
```sh
echo "Evaluation of the performance of different RAG methods on the 2wikimultihopqa (51 queries)";
echo;
echo "VectorDB";
python vdb_benchmark.py -n 51 -s
echo;
echo "LightRAG [local mode]";
python lightrag_benchmark.py -n 51 -s --mode=local
echo;
echo "GraphRAG [local mode]";
python nano_benchmark.py -n 51 -s --mode=local
echo;
echo "Circlemind"
python graph_benchmark.py -n 51 -s

echo "Evaluation of the performance of different RAG methods on the 2wikimultihopqa (101 queries)";
echo;
echo "VectorDB";
python vdb_benchmark.py -n 101 -s
echo;
echo "LightRAG [local mode]";
python lightrag_benchmark.py -n 101 -s --mode=local
echo;
echo "GraphRAG [local mode]";
python nano_benchmark.py -n 101 -s --mode=local
echo;
echo "Circlemind";
python graph_benchmark.py -n 101 -s
```

### File: benchmarks\graph_benchmark.py
```py
"""Benchmarking script for GraphRAG."""

import argparse
import asyncio
import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

import numpy as np
import xxhash
from _domain import DOMAIN, ENTITY_TYPES, QUERIES
from dotenv import load_dotenv
from tqdm import tqdm

from fast_graphrag import GraphRAG, QueryParam
from fast_graphrag._utils import get_event_loop


@dataclass
class Query:
    """Dataclass for a query."""

    question: str = field()
    answer: str = field()
    evidence: List[Tuple[str, int]] = field()


def load_dataset(dataset_name: str, subset: int = 0) -> Any:
    """Load a dataset from the datasets folder."""
    with open(f"./datasets/{dataset_name}.json", "r") as f:
        dataset = json.load(f)

    if subset:
        return dataset[:subset]
    else:
        return dataset


def get_corpus(dataset: Any, dataset_name: str) -> Dict[int, Tuple[int | str, str]]:
    """Get the corpus from the dataset."""
    if dataset_name == "2wikimultihopqa" or dataset_name == "hotpotqa":
        passages: Dict[int, Tuple[int | str, str]] = {}

        for datapoint in dataset:
            context = datapoint["context"]

            for passage in context:
                title, text = passage
                title = title.encode("utf-8").decode()
                text = "\n".join(text).encode("utf-8").decode()
                hash_t = xxhash.xxh3_64_intdigest(text)
                if hash_t not in passages:
                    passages[hash_t] = (title, text)

        return passages
    else:
        raise NotImplementedError(f"Dataset {dataset_name} not supported.")


def get_queries(dataset: Any):
    """Get the queries from the dataset."""
    queries: List[Query] = []

    for datapoint in dataset:
        queries.append(
            Query(
                question=datapoint["question"].encode("utf-8").decode(),
                answer=datapoint["answer"],
                evidence=list(datapoint["supporting_facts"]),
            )
        )

    return queries


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="GraphRAG CLI")
    parser.add_argument("-d", "--dataset", default="2wikimultihopqa", help="Dataset to use.")
    parser.add_argument("-n", type=int, default=0, help="Subset of corpus to use.")
    parser.add_argument("-c", "--create", action="store_true", help="Create the graph for the given dataset.")
    parser.add_argument("-b", "--benchmark", action="store_true", help="Benchmark the graph for the given dataset.")
    parser.add_argument("-s", "--score", action="store_true", help="Report scores after benchmarking.")
    args = parser.parse_args()

    print("Loading dataset...")
    dataset = load_dataset(args.dataset, subset=args.n)
    working_dir = f"./db/graph/{args.dataset}_{args.n}"
    corpus = get_corpus(dataset, args.dataset)

    if args.create:
        print("Dataset loaded. Corpus:", len(corpus))
        grag = GraphRAG(
            working_dir=working_dir,
            domain=DOMAIN[args.dataset],
            example_queries="\n".join(QUERIES),
            entity_types=ENTITY_TYPES[args.dataset],
        )
        grag.insert(
            [f"{title}: {corpus}" for _, (title, corpus) in tuple(corpus.items())],
            metadata=[{"id": title} for title in tuple(corpus.keys())],
        )
    if args.benchmark:
        queries = get_queries(dataset)
        print("Dataset loaded. Queries:", len(queries))
        grag = GraphRAG(
            working_dir=working_dir,
            domain=DOMAIN[args.dataset],
            example_queries="\n".join(QUERIES),
            entity_types=ENTITY_TYPES[args.dataset],
        )

        async def _query_task(query: Query) -> Dict[str, Any]:
            answer = await grag.async_query(query.question, QueryParam(only_context=True))
            return {
                "question": query.question,
                "answer": answer.response,
                "evidence": [
                    corpus[chunk.metadata["id"]][0]
                        if isinstance(chunk.metadata["id"], int)
                        else chunk.metadata["id"]
                    for chunk, _ in answer.context.chunks
                ],
                "ground_truth": [e[0] for e in query.evidence],
            }

        async def _run():
            await grag.state_manager.query_start()
            answers = [
                await a
                for a in tqdm(asyncio.as_completed([_query_task(query) for query in queries]), total=len(queries))
            ]
            await grag.state_manager.query_done()
            return answers

        answers = get_event_loop().run_until_complete(_run())

        with open(f"./results/graph/{args.dataset}_{args.n}.json", "w") as f:
            json.dump(answers, f, indent=4)

    if args.benchmark or args.score:
        with open(f"./results/graph/{args.dataset}_{args.n}.json", "r") as f:
            answers = json.load(f)

        try:
            with open(f"./questions/{args.dataset}_{args.n}.json", "r") as f:
                questions_multihop = json.load(f)
        except FileNotFoundError:
            questions_multihop = []

        # Compute retrieval metrics
        retrieval_scores: List[float] = []
        retrieval_scores_multihop: List[float] = []

        for answer in answers:
            ground_truth = answer["ground_truth"]
            predicted_evidence = answer["evidence"]

            p_retrieved: float = len(set(ground_truth).intersection(set(predicted_evidence))) / len(set(ground_truth))
            retrieval_scores.append(p_retrieved)

            if answer["question"] in questions_multihop:
                retrieval_scores_multihop.append(p_retrieved)

        print(
            f"Percentage of queries with perfect retrieval: {np.mean([1 if s == 1.0 else 0 for s in retrieval_scores])}"
        )
        if len(retrieval_scores_multihop):
            print(
                f"[multihop] Percentage of queries with perfect retrieval: {
                    np.mean([1 if s == 1.0 else 0 for s in retrieval_scores_multihop])
                }"
            )

```

### File: benchmarks\lightrag_benchmark.py
```py
"""Benchmarking script for GraphRAG."""

import argparse
import asyncio
import json
import os
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

import numpy as np
import xxhash
from dotenv import load_dotenv
from lightrag import LightRAG, QueryParam
from lightrag.lightrag import always_get_an_event_loop
from lightrag.llm import gpt_4o_mini_complete
from lightrag.utils import logging
from tqdm import tqdm

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("nano-vectordb").setLevel(logging.WARNING)

@dataclass
class Query:
    """Dataclass for a query."""

    question: str = field()
    answer: str = field()
    evidence: List[Tuple[str, int]] = field()


def load_dataset(dataset_name: str, subset: int = 0) -> Any:
    """Load a dataset from the datasets folder."""
    with open(f"./datasets/{dataset_name}.json", "r") as f:
        dataset = json.load(f)

    if subset:
        return dataset[:subset]
    else:
        return dataset


def get_corpus(dataset: Any, dataset_name: str) -> Dict[int, Tuple[int | str, str]]:
    """Get the corpus from the dataset."""
    if dataset_name == "2wikimultihopqa" or dataset_name == "hotpotqa":
        passages: Dict[int, Tuple[int | str, str]] = {}

        for datapoint in dataset:
            context = datapoint["context"]

            for passage in context:
                title, text = passage
                title = title.encode("utf-8").decode()
                text = "\n".join(text).encode("utf-8").decode()
                hash_t = xxhash.xxh3_64_intdigest(text)
                if hash_t not in passages:
                    passages[hash_t] = (title, text)

        return passages
    else:
        raise NotImplementedError(f"Dataset {dataset_name} not supported.")


def get_queries(dataset: Any):
    """Get the queries from the dataset."""
    queries: List[Query] = []

    for datapoint in dataset:
        queries.append(
            Query(
                question=datapoint["question"].encode("utf-8").decode(),
                answer=datapoint["answer"],
                evidence=list(datapoint["supporting_facts"]),
            )
        )

    return queries


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="LightRAG CLI")
    parser.add_argument("-d", "--dataset", default="2wikimultihopqa", help="Dataset to use.")
    parser.add_argument("-n", type=int, default=0, help="Subset of corpus to use.")
    parser.add_argument("-c", "--create", action="store_true", help="Create the graph for the given dataset.")
    parser.add_argument("-b", "--benchmark", action="store_true", help="Benchmark the graph for the given dataset.")
    parser.add_argument("-s", "--score", action="store_true", help="Report scores after benchmarking.")
    parser.add_argument("--mode", default="local", help="LightRAG query mode.")
    args = parser.parse_args()

    print("Loading dataset...")
    dataset = load_dataset(args.dataset, subset=args.n)
    working_dir = f"./db/lightrag/{args.dataset}_{args.n}"
    corpus = get_corpus(dataset, args.dataset)

    if not os.path.exists(working_dir):
        os.mkdir(working_dir)
    if args.create:
        print("Dataset loaded. Corpus:", len(corpus))
        grag = LightRAG(
            working_dir=working_dir,
            llm_model_func=gpt_4o_mini_complete,
            log_level=logging.WARNING
        )
        grag.insert([f"{title}: {corpus}" for _, (title, corpus) in tuple(corpus.items())])
    if args.benchmark:
        queries = get_queries(dataset)
        print("Dataset loaded. Queries:", len(queries))
        grag = LightRAG(
            working_dir=working_dir,
            llm_model_func=gpt_4o_mini_complete,
            log_level=logging.WARNING
        )

        async def _query_task(query: Query, mode: str) -> Dict[str, Any]:
            answer = await grag.aquery(
                query.question, QueryParam(mode=mode, only_need_context=True, max_token_for_text_unit=9000)
            )
            chunks = [
                c.split(",")[1].split(":")[0].lstrip('"')
                for c in re.findall(r"\n-----Sources-----\n```csv\n(.*?)\n```", answer, re.DOTALL)[0].split("\r\n")[
                    1:-1
                ]
            ]
            return {
                "question": query.question,
                "answer": "",
                "evidence": chunks[:8],
                "ground_truth": [e[0] for e in query.evidence],
            }

        async def _run(mode: str):
            answers = [
                await a
                for a in tqdm(
                    asyncio.as_completed([_query_task(query, mode=mode) for query in queries]), total=len(queries)
                )
            ]
            return answers

        answers = always_get_an_event_loop().run_until_complete(_run(mode=args.mode))

        with open(f"./results/lightrag/{args.dataset}_{args.n}_{args.mode}.json", "w") as f:
            json.dump(answers, f, indent=4)

    if args.benchmark or args.score:
        with open(f"./results/lightrag/{args.dataset}_{args.n}_{args.mode}.json", "r") as f:
            answers = json.load(f)

        try:
            with open(f"./questions/{args.dataset}_{args.n}.json", "r") as f:
                questions_multihop = json.load(f)
        except FileNotFoundError:
            questions_multihop = []

        # Compute retrieval metrics
        retrieval_scores: List[float] = []
        retrieval_scores_multihop: List[float] = []

        for answer in answers:
            ground_truth = answer["ground_truth"]
            predicted_evidence = answer["evidence"]

            p_retrieved: float = len(set(ground_truth).intersection(set(predicted_evidence))) / len(set(ground_truth))
            retrieval_scores.append(p_retrieved)

            if answer["question"] in questions_multihop:
                retrieval_scores_multihop.append(p_retrieved)

        print(
            f"Percentage of queries with perfect retrieval: {np.mean([1 if s == 1.0 else 0 for s in retrieval_scores])}"
        )
        if len(retrieval_scores_multihop):
            print(
                f"[multihop] Percentage of queries with perfect retrieval: {
                    np.mean([1 if s == 1.0 else 0 for s in retrieval_scores_multihop])
                }"
            )

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
