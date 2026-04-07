---
id: context-mapping
type: knowledge
owner: OA_Triage
---
# context-mapping
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Context Mapping

Context Maps describe the contact between bounded contexts and teams with a collection of patterns. There are nine context map patterns and three different team relationships. The context map patterns describe a variety of perspectives like service provisioning, model propagation or governance aspects. This diversity of perspectives enables you to get a holistic overview of team and bounded context relationships.

Context Maps can be used to analyze existing systems or application landscapes, but they are also suitable for upfront design considerations. However, we have realized that many folks struggle to get started with the context mapping patterns based on the definitions in the existing DDD books. This GitHub repository aims to give you some help with context maps with a cheat sheet and a starter kit for Miro.

## Overview of the context map team relationships and patterns

### Team Relationships

#### Mutually Dependent

<img src="resources/mutual-dependent.jpg" alt="Mutually Dependent" width=300/>

Two teams or bounded contexts are mutually dependent when their software artifacts or systems need to be delivered together to be successful and work. You will often see a close, reciprocal link between data, functionality and capabilities of these teams. Those teams also need a lot of communication between each other in order to coordinate their efforts (see Partnership pattern).

#### Upstream Downstream

<img src="resources/upstream-downstream.jpg" alt="Upstream / Downstream" width=300/>

Actions of an upstream team will have an effect on the downstream team, but actions of the downstream do not have a significant impact on the upstream team. "The upstream team may succeed independently of the fate of the downstream team" (Quote from the [DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/)).

#### Free

<img src="resources/free.jpg" alt="Free" width=300/>

A Bounded Context or a team that works in it is free if changes in other Bounded Contexts do not influence its success or failure. There is, therefore, no organizational or technical link of any kind between these teams.

### Context Map Patterns

Most publications in the Domain-Driven Design community currently describe nine context mapping patterns. 

#### Open-host Service

<img src="resources/ohs.jpg" alt="Open-host Service" height=150/>

"A protocol that gives access to your subsystem as a set of services. Open the protocol so that all who need to integrate with you can use it. Enhance and expand the protocol to handle new integration requirements, except when a single team has idiosyncratic needs. Then, use a one-off translator to augment the protocol for that special case so that the shared protocol can stay simple and coherent." ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

The team providing an Open-host Service is usually in an upstream position whereas the clients using it are downstream teams. The teams on the downstream are free to be conformists or to build anticorruption layers.

#### Conformist

<img src="resources/cf.jpg" alt="Conformist" height=150/>

"Eliminate the complexity of translation between bounded contexts by slavishly adhering to the model of the upstream team. Although this cramps the style of the downstream designers and probably does not yield the ideal model for the application, choosing conformity enormously simplifies integration. Also, you will share a ubiquitous language with your upstream team. The upstream is in the driver’s seat, so it is good to make communication easy for them. Altruism may be sufficient to get them to share information with you." ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

#### Anticorruption Layer

<img src="resources/acl.jpg" alt="Anticorruption Layer" height=150/>

"As a downstream client, create an isolating layer to provide your system with functionality of the upstream system in terms of your own domain model. This layer talks to the other system through its existing interface, requiring little or no modification to the other system. Internally, the layer translates in one or both directions as necessary between the two models." ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

#### Shared Kernel

<img src="resources/shared-kernel.jpg" alt="Shared Kernel" width=300/>

"Designate with an explicit boundary some subset of the domain model that the teams agree to share. Keep this kernel small. Within this boundary, include, along with this subset of the model, the subset of code or of the database design associated with that part of the model. This explicitly shared stuff has special status, and shouldn’t be changed without consultation with the other team." ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

#### Partnership

<img src="resources/partnership.jpg" alt="Partnership" width=300/>

"Where development failure in either of two contexts would result in delivery failure for both, forge a partnership between the teams in charge of the two contexts. Institute a process for coordinated planning of development and joint management of integration. 
The teams must cooperate on the evolution of their interfaces to accommodate the development needs of both systems. Interdependent features should be scheduled so that they are completed for the same release." ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

#### Customer / Supplier Development

<img src="resources/customer-supplier.jpg" alt="Customer / Supplier" width=300/>

"When two teams are in an upstream-­downstream relationship, where the upstream team may succeed independently of the fate of the downstream team, the needs of the downstream come to be addressed in a variety of ways with a wide range of consequences. [...] Establish a clear customer/supplier relationship between the two teams, meaning downstream priorities factor into upstream planning. Negotiate and budget tasks for downstream requirements so that everyone understands the commitment and schedule." ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

#### Published Language

<img src="resources/published-language.jpg" alt="Published Language" width=300/>

"The translation between the models of two bounded contexts requires a common language. [...] Use a well-documented shared language that can express the necessary domain information as a common medium of communication, translating as necessary into and out of that language." ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

Widely known examples of a Published Language are iCalendar or vCard. Published language is often combined with an open-host service.

#### Separate Ways

<img src="resources/separate-ways.jpg" alt="Separate Ways" width=300/>

When two bounded contexts have no significant relationship they can be separated.
"Declare a bounded context to have no connection to the others at all, allowing developers to find simple, specialized solutions within this small scope" ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

#### Big Ball Of Mud

<img src="resources/bbom.jpg" alt="Big Ball Of Mud" width=300/>

A (part of a) system which is a mess by having mixed models and inconsistent boundaries. Don't let this lousy model propagate into the other Bounded Contexts. Big Ball Of Mud is a demarcation of a bad model or system quality. You want to make sure, that this mess does not propagate into other bounded contexts.

## Best practices for Context Maps

There is no need to put all the patterns and team relationships into one big context map. Such a context map will grow over time, and it will become hard to understand. You will be forced to explain such a complex context map to big amount of various stakeholders who all have different perspectives due to their roles or the nature of their work. Therefore, it is recommended to mind those hints:

- Prefer small context maps for explicit questions
- Document and explain the patterns you are going to use
- Work with different perspectives and multiple context maps for those perspectives

### Small context maps for explicit questions

Context Maps are able to answer a high variety of questions such as:

- how does the model of a given system propagate through an application landscape?
- which kind of influence does a certain team have on others?
- who has an influence on a given team?
- how are politics being played?

As you can see: these questions are very specific, and we can answer them based on a big context map but such a context map will sooner or later turn into an information overload.

Therefore: 

Work with smaller context maps, aimed to answer specific questions. Only include those patterns to these smaller context maps that help you in answering these questions.

### Document and explain the patterns you are going to use

Context Mapping is a powerful technique to visualize relationships between systems and teams. However, they can become hard to understand for people who are not experienced with Domain-Driven Design or the context mapping patterns. Even some pattern names are not self-explanatory for certain groups of stakeholders and the same applies to some of the definitions.

Therefore:

Before you start drawing context maps you should decide which of the patterns you are going to use, and you will do yourself and the stakeholders of your context map a big favour by providing an explanation of those patterns. Make sure that all folks working with your context map do understand the patterns. Examples are always a good idea for such explanations.

## Context Map Cheat Sheet

Here is a cheat sheet containing brief descriptions of the context mapping patterns:

![Context Map Cheat Sheet](resources/context-map-cheat-sheet.png)

## Remote Context Mapping Starter Kit for Miro

If you perform context mapping with Miro, there is a board backup that gets you started with all the objects for the patterns, team relationships and boundaries. In addition to that the Miro board contains a few examples to get you started:

![Remote Context Mapping Starter Kit for Miro](resources/RemoteContextMappingStarterKit.jpg)

[Link to Miro Board Backup](resources/Remote-Context-Mapping-Starter-Kit.rtb)

You can also check out (and comment) [a read-only version of the starter kit on Miro](https://miro.com/app/board/o9J_kqtuB6A=/)

## Context Mapping with Context Mapper

If you want to maintain your context maps in your code repo, [Context Mapper](https://contextmapper.org/) allows you to describe your contexts in a text file and generate a diagram from it. [Context Mapper](https://contextmapper.org/) is available [online (in the browser via Gitpod)](https://contextmapper.org/docs/online-ide/) or via IDE plugins for [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=contextmapper.context-mapper-vscode-extension) and [Eclipse](https://marketplace.eclipse.org/content/context-mapper/).

## Further Reading

- [Dynamic Reteaming](https://leanpub.com/dynamicreteaming) 
- [Pioneers, Settlers & Town Planners](http://wardleypedia.org/mediawiki/index.php/Pioneers_settlers_town_planners)
- [Team Topologies](https://teamtopologies.com/)
- [Visualising Sociotechnical Architecture with Context Maps](https://speakerdeck.com/mploed/visualizing-sociotechnical-architectures-with-context-maps)

## Contributors

Thanks to all [existing and future contributors](https://github.com/ddd-crew/context-mapping/graphs/contributors) and to the following individuals who have all contributed to the Context Map Cheat Sheet:

- [Kacper Gunia](https://twitter.com/cakper)
- [Nick Tune](https://github.com/ntcoding)

## Contributions and Feedback

The Context Map Cheat Sheet is freely available for you to use. In addition, your feedback and ideas are welcome to improve the technique or to create alternative versions.

If you have questions you can ping us or open an [Issue](https://github.com/ddd-crew/context-map-cheat-sheet/issues/new/choose).

Feel free to also send us a pull request with your examples or experience reports.

You can also comment directly on the [Miro board of the Context Map Cheat Sheet](https://miro.com/app/board/o9J_kqrI8ck=/)

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International
License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

```

### File: LICENCE.md
```md
Attribution-ShareAlike 4.0 International

=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
	wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More_considerations
     for the public:
	wiki.creativecommons.org/Considerations_for_licensees

=======================================================================

Creative Commons Attribution-ShareAlike 4.0 International Public
License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution-ShareAlike 4.0 International Public License ("Public
License"). To the extent this Public License may be interpreted as a
contract, You are granted the Licensed Rights in consideration of Your
acceptance of these terms and conditions, and the Licensor grants You
such rights in consideration of benefits the Licensor receives from
making the Licensed Material available under these terms and
conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.

  c. BY-SA Compatible License means a license listed at
     creativecommons.org/compatiblelicenses, approved by Creative
     Commons as essentially the equivalent of this Public License.

  d. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.

  e. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  f. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  g. License Elements means the license attributes listed in the name
     of a Creative Commons Public License. The License Elements of this
     Public License are Attribution and ShareAlike.

  h. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  i. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  j. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  k. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  l. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  m. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part; and

            b. produce, reproduce, and Share Adapted Material.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. Additional offer from the Licensor -- Adapted Material.
               Every recipient of Adapted Material from You
               automatically receives an offer from the Licensor to
               exercise the Licensed Rights in the Adapted Material
               under the conditions of the Adapter's License You apply.

            c. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.

       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

  b. ShareAlike.

     In addition to the conditions in Section 3(a), if You Share
     Adapted Material You produce, the following conditions also apply.

       1. The Adapter's License You apply must be a Creative Commons
          license with the same License Elements, this version or
          later, or a BY-SA Compatible License.

       2. You must include the text of, or the URI or hyperlink to, the
          Adapter's License You apply. You may satisfy this condition
          in any reasonable manner based on the medium, means, and
          context in which You Share Adapted Material.

       3. You may not offer or impose any additional or different terms
          or conditions on, or apply any Effective Technological
          Measures to, Adapted Material that restrict exercise of the
          rights granted under the Adapter's License You apply.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database;

  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material,

     including for purposes of Section 3(b); and
  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.

  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, TH
... [TRUNCATED]
```

