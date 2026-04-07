---
id: mixter
type: knowledge
owner: OA_Triage
---
# mixter
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
Mixter
======
Mixter is a project to discover CQRS/Event sourcing through koans in multiple languages.

At this point the koans have been ported to 5 languages: C#, Java 8, Scala, PHP and Javascript.

Starting
-------

1. Checkout `master` branch
2. Execute `./run` script
3. You will have to make tests pass green, then to go to next test, execute `./next`

See few slides on http://devlyon.fr/mixter, it explains the main steps and goals for each.

You can view one solution for each language with a small Web API on branches [lang]-solution.

Feedback is required
--------------------

Feel free to use issues in this repo to give your feedback, to propose some improvements,
to ask for other languages...and even better to submit pull requests.

Explanations of some implementation details
-------------------------------------------

We have done some choices that we consider implementation details, but that can hurt
some people. So we try to explain them here.

### About events publication mecanism in CQRS/ES, there are two main well known options :

1) use an AggregateRoot base class that accumulate uncommitted events that are picked by Repository on Save of the aggregate.

2) use DomainEvents.Raise(event) static call from AggregateRoot protected Apply method

We chose a third way that consists of passing an IEventPublisher (with Publish method) to each aggregate method to raise events.
There is no more need to call Repository.Save and it avoids static method call.

### We use a DecisionProjection concept to keep track of "transient state" of aggregates.

We thought this "transient state" as a special projection (like Read model ones) to take further decision in the aggregate,
that's why we call it DecisionProjection. We kept this class private inside the aggregate.

### Commands and command handlers are not shown here for now, for simplicity, it has been left implicit through method of aggregates.

Perhaps something to introduce in further version.

Any questions ?
---------------

You can contact us through GitHub or on Twitter : @clem_bouillier, @florentpellet, @jeanhelou, @ouarzy.


Add new languages
---------
If you want to fork with your preferred language, you only need to follow some rules.

The KoanCli script is based on a naming convention in commit message.
 * Failing tests should contain `[Test KO]`
 * Resolving tests should contain `[Test OK]`

Currently the KoanCli script isn't dynamic and tests number must be static to know the correspondence between a test and a step.
Here number of tests per step:
 * Step 1, delete command: 4 tests
 * Step 2, timeline messages: 1 tests
 * Step 3, subscription aggregate: 4 tests
 * Step 4, aggregates interaction: 4 tests
 * Step 5, command handler: 2 tests


Changelog
---------

### V2
 * Create KoanCli: no git knowledge required. You simply call run script to starting, and next to jump at next step. (#3)
 * Remove reply message (#7)
 * Rename publish to quack (#16)
 * Fix several bug specific at languages (#15, #5, #4)
 * Make PHP version work with PHP 7.2 (#36)

### V1 (obsolete)
First version, use during a Mix-IT workshop 2015 : http://www.mix-it.fr/session/1041/agilite-par-le-code-grace-a-cqrs-et-eventsourcing


```

### File: index.html
```html
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">

		<title>Workshop CQRS & EventSourcing discovery - Slides</title>

		<meta name="description" content="Workshop CQRS & EventSourcing discovery">

		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, minimal-ui">

		<link rel="stylesheet" href="slideResources/reveal.css">
		<link rel="stylesheet" href="slideResources/black.css" id="theme">
		<style>
			.reveal .right {
				text-align: right;
			}
			
			.reveal .left {
				text-align: left;
			}
			
			.reveal .small {
				font-size: 0.7em;
			}
			
			.reveal .pictures {
				display: inline-flex;
				justify-content: space-between;
				list-style-type: none;
				text-align: center;
				margin: 0;
				width: 100%;
				align-items: center;
			}
			
			.reveal .bigPicture {
				max-width: 80%;
			}
			
			.reveal .legend {
				position: absolute;
				bottom: 0;
				margin: 0;
				width: 100%;
				font-size: 0.7em;
			}
			
			.reveal .learnStep {
				line-height: 1.4em;
				font-size: 0.7em;
			}
		</style>
	</head>

	<body>
		<div class="reveal">
			<div class="slides">
				<section>
					<h1>CQRS & EventSourcing discovery</h1>
					<p>Workshop</p>
					<br />
					<p class="right small">Florent @florentpellet</p>
					<p class="right small">Clément @clem_bouillier</p>
					<p class="right small">Jean @jeanhelou</p>
					<p class="right small">Emilien @ouarzy</p>
				</section>
				<section>
					<h1>Who are we ?</h1>
					<ul>
						<li>4 passionate guys initiated this workshop in 2015</li>
						<li>Feel free to give some feedbacks on GitHub</li>
					</ul>
					<ul class="pictures small" style="margin-top: 2em;">
						<li>
							<div><img src="slideResources/clement_bouillier.jpg" alt="Clément" /></div>
							<div>Clément</div>
							<div>@clem_bouillier</div>
						</li>
						<li>
							<div><img src="slideResources/emilien_pecoul.jpg" alt="Emilien" /></div>
							<div>Emilien</div>
							<div>@ouarzy</div>
						</li>
						<li>
							<div><img src="slideResources/florent_pellet.jpg" alt="Florent" /></div>
							<div>Florent</div>
							<div>@florentpellet</div>
						</li>
						<li>
							<div><img src="slideResources/jean_helou.jpg" alt="Jean" /></div>
							<div>Jean</div>
							<div>@jeanhelou</div>
						</li>
					</ul>
				</section>
				<section>
					<h2>CQRS Concept</h2>
					<img class="bigPicture" src="slideResources/cqrs.png" alt="CQRS" />
					<p class="right legend">Ref. "Conceptual CQRS" - Alberto Brandolini</p>
				</section>
				<section>
					<h2>Event Sourcing Concept</h2>
					<img class="bigPicture" src="slideResources/eventsourcing.jpg" alt="Event Sourcing" />
					<p class="left legend">NB: DecisionProjection is also called State</p>
					<p class="right legend">Ref. Jérémie Chassaing</p>
				</section>
				<section>
					<h2>The new unicorn</h2>
					<p>We’ll revolutionize the web!</p>
					<p>We’ll create a product like Twitter but better ...</p>
					<h4>A revolution!</h4>
					<img src="slideResources/unicorn.jpg" alt="unicorn" />
				</section>
				<section>
					<h2>Mixter</h2>
					<p>Instead tweet...</p>
					<p>we'll quack!</p>
					<img src="slideResources/unicorn2.jpg" alt="unicorn" />
				</section>
				<section style="height: 90%">
					<h2>Event Storming mixter</h2>
					<img src="slideResources/eventstorming_prepa_2.jpg" alt="eventstorming 2" style="position: absolute;bottom: 1em;left: -1em;height: 8em;" />
					<img src="slideResources/eventstorming_prepa_1.jpg" alt="eventstorming 1" style="position: absolute;top: 2.4em;left: 0;" />
					<img src="slideResources/eventstorming_prepa_3.jpg" alt="eventstorming 3" style="position: absolute;bottom: 2em;top: 2em;" />
					<img src="slideResources/eventstorming_prepa_4.jpg" alt="eventstorming 4" style="position: absolute;bottom: 0;right: -0.5em;width: 13em;" />
					<p class="left legend">Ref. "Event Storming" - Alberto Brandolini</p>
				</section>
				<section data-background="url(slideResources/eventstorming.jpg) center center no-repeat fixed white" data-background-size="contain">
				</section>
				<section data-background="url(slideResources/eventstorming_workshop.jpg) center center no-repeat fixed white" data-background-size="contain">
				</section>
				<section>
					<h2>Test Driven Workshop</h2>
					<ul>
						<li>Working in pairs</li>
						<li>Execute "run" script and read instructions</li>
						<br />
						<li><span style="color: #ff2c2d">Red Test</span> => <span style="color: #98E04C">Green Test</span></li>
						<br />
						<li>
							3 steps (+2 Bonus)
							<ul>
								<li><b>C</b>ommand DeleteMessage</li>
								<li><b>Q</b>uery Timeline Message</li>
								<li><b>E</b>vents in aggregate</li>
							</ul>
						</li>
					</ul>
				</section>
				<section>
					<h2>Focus on Core Domain</h2>
					<ul>
						<li>
							Do not change
							<ul>
								<li>Tests code</li>
								<li>Infrastructure code</li>
							</ul>
						</li>
						<br />
						<li>You can see Identity context implementation as example</li>
					</ul>
				</section>
				<section>
					<h2>GIT Repository</h2>
					<p class="left">git clone https://github.com/DevLyon/mixter.git</p>
					<p class="left">./run</p>
					<br />
					<p class="left">Slide : http://devlyon.fr/mixter/</p>
				</section>
				<section>
					<h2>1. Delete Command</h2>
					<p class="left">What we will learn :</p>
					<ul class="learnStep">
						<li>publish events from aggregate,</li>
						<li>use projection for decision inside aggregate (contains only "state" for future decision, DO NOT keep all state like in an entity)</li>
						<li>Implement "business rules" that insure aggregate consistency (based on decision projection and command=method parameters)</li>
					</ul>
					<p class="left"><b>In brief : the C of CQRS</b></p>
					<ul class="pictures">
						<li><img src="slideResources/step1_1.jpg" alt="eventstorming" /></li>
						<li><img src="slideResources/step1_2.png" alt="cqrs" /></li>
					</ul>
				</section>
				<section>
					<h2>2. Timeline messages Projection</h2>
					<p class="left">What we will learn :</p>
					<ul class="learnStep">
						<li>Create another model for Query (Projection, TimelineMessageProjection)</li>
						<li>Transform events in a projection model through an EventHandler</li>
						<li>A projection repository (in-memory) with its interface is given</li>
					</ul>
					<p class="left"><b>In brief : Q of CQRS</b></p>
					<ul class="pictures">
						<li><img src="slideResources/step2_1.jpg" alt="eventstorming" /></li>
						<li><img src="slideResources/step2_2.png" alt="cqrs" /></li>
					</ul>
				</section>
				<section>
					<h2>3. Subscription Aggregate</h2>
					<p class="left">What we will learn :</p>
					<ul class="learnStep">
						<li>Create a new aggregate (Subscription)</li>
						<li>Raise events from it : UserFollowed and UserUnfollowed</li>
						<li>Create a decision projection for it</li>
						<li>Implement replay of events (event sourced aggregate)</li>
					</ul>
					<p class="left"><b>In brief : C of CQRS + Event Sourcing</b></p>
					<ul class="pictures">
						<li><img src="slideResources/step3_1.jpg" alt="eventstorming" /></li>
						<li><img src="slideResources/step3_2.jpg" alt="eventsourcing" /></li>
					</ul>
				</section>
				<section>
					<h2>4. Aggregates interaction</h2>
					<p class="left">What we will learn :</p>
					<ul class="learnStep">
						<li>Coordinate several aggregates to limit coupling</li>
						<li>Concept of " Eventual consistency"</li>
					</ul>
					<ul class="pictures">
						<li><img src="slideResources/step4.jpg" alt="eventstorming" /></li>
					</ul>
				</section>
				<section>
					<h2>5. Command Handler</h2>
					<p class="left">What we will learn :</p>
					<ul class="learnStep">
						<li>Integrate previous code from Message & Identity contexts in a command</li>
						<li>Write some web infrastructure code executing the command</li>
					</ul>
					<p class="small left">
						=> Request Rest to execute delete Message command, with session validity verification<br />
						NB : no tests for this step for now…
					</p>
					<ul class="pictures">
						<li><img src="slideResources/step5.png" alt="cqrs" /></li>
					</ul>
				</section>
				<section>
					<h1>CQRS & EventSourcing discovery</h1>
					<p>Thanks!</p>
					<br />
					<p class="right small">Florent @florentpellet</p>
					<p class="right small">Clément @clem_bouillier</p>
					<p class="right small">Jean @jeanhelou</p>
					<p class="right small">Emilien @ouarzy</p>
				</section>
			</div>
		</div>

		<script src="slideResources/head.min.js"></script>
		<script src="slideResources/reveal.min.js"></script>

		<script>
			Reveal.initialize({
				history: true,
				transition: 'convex'
			});
		</script>
	</body>
</html>

```

### File: run.ps1
```ps1
$languages = @{ "js"="origin/js/v2.1"; "csharp"="origin/csharp/v2.3";"csharp-core"="origin/csharp-core/v2.1"; "java"="origin/java/v2.2"; "scala"="origin/scala/v2.2"; "php"="origin/php/v2.1"; "fsharp"="origin/fsharp/v2.2" }
$testsNbByStep = @{ 1=4; 2=1; 3=4; 4=4; 5=2 }

$masterBranch = "origin/master"
$testBranch = "test"
$solutionBranch = "solution"
$workshopBranch = "workshop"

$batWrapperTemplate = @"
@echo off

PowerShell -ExecutionPolicy Bypass -File @@scriptname@@.ps1
"@

$nextCommandTemplate = @"
git add -A 
git commit -m "Resolve test"
git merge --no-edit @@nexttag@@
"@

$jumpToNextStepCommandTemplate = @"
git add -A
git commit -m "Abort test"
git checkout -b $workshopBranch-@@nexttag@@ @@nexttag@@ 
git merge --no-edit @@nexttag@@-test1 *> `$null`
git checkout --ours . 
git add . 
git commit -m "Merge with test branch" 
"@

$displayNextStepMessageTemplate = @"
Write-Host ""
Write-Host ""
Get-Content stepsDoc/step@@stepNum@@.txt | Write-Host -f green
Write-Host ""
Write-Host ""
"@

$displayNextTestMessageTemplate = @"
Write-Host ""
Write-Host ""
Write-Host -f green "========================"
Write-Host -f green "===  STEP @@stepNum@@ - Test @@testNum@@ ==="
Write-Host -f green "========================"
Write-Host ""
Write-Host ""
"@

$jumpToEndStepCommandTemplate = @"
git add -A
git commit -m "Abort test"
git checkout -b $workshopBranch-end $solutionBranch
"@

$displayEndMessageTemplate = @"
Write-Host ""
Write-Host ""
Get-Content stepsDoc/end.txt | Write-Host -f green
Write-Host ""
Write-Host ""
"@

function AskParametreWithValues($name, $values){
    do {
        $value = Read-Host ($name + " (" + ($values -join ", ") + ")")
    } while(-Not ($values -contains $value))

    return $value
}

function askLanguage(){
	AskParametreWithValues "Language" $languages.Keys
}

function generateTagsForStep($stepNum){
	[array]$testTags = 1..$testsNbByStep.$stepNum | %{ "step" + $stepNum + "-test" + $_ }
	[array]$stepTags = ("step" + $stepNum)
	
	$testTags + $stepTags
}

function generateTags(){
	1..$testsNbByStep.Count | %{ generateTagsForStep $_ }
}

function getCurrentTestTag(){
	"step" + $currentStep + "-test" + $currentTestOfStep
}

function getNextTestTag(){
	if($testsNbByStep.$currentStep -le $currentTestOfStep){
		"step" + ($currentStep + 1) + "-test1"
	} else {
		"step" + $currentStep + "-test" + ($currentTestOfStep + 1)
	}
}

function getNextTestNum(){
	if($testsNbByStep.$currentStep -le $currentTestOfStep){
		return 1
	} else {
		return ($currentTestOfStep + 1)
	}
}

function getCurrentStepTag(){
	"step" + $currentStep
}

function getNextStepTag(){
	"step" + ($currentStep + 1)
}

function resetTestCounter(){
	$script:currentStep = 1
	$script:currentTestOfStep = 1
}

function nextTest(){
	if($testsNbByStep.$currentStep -le $currentTestOfStep){
		$script:currentStep++
		$script:currentTestOfStep = 1
	} else {
		$script:currentTestOfStep++
	}
}

function hasNextTestForCurrentStep(){
	$currentTestOfStep -lt $testsNbByStep.$currentStep
}

function hasNextStep(){
	$currentStep -lt $testsNbByStep.Count
}

function clean(){
	Write-Host "Clean repository..."

	git clean -d -x -f > $null
	git reset --hard HEAD > $null
	git checkout master > $null
	git branch -D $testBranch *> $null
	git branch -D $solutionBranch *> $null
	git branch -D $workshopBranch *> $null
	git branch -D ($workshopBranch + "-end") *> $null
	generateTags | %{ git branch -D ($workshopBranch + "-" + $_) } *> $null
	generateTags | %{ git tag -d $_ } *> $null
}

function extraCommitHashOfLog($line){
	$parts = $line.split(' ')
	$parts[0]
}

function isFailedTestCommit($line){
	$line -like '* KO]*'
}

function addStepNavigationCommand($nextStepTag, $nextStepNum){
	$nextCommandContent = $jumpToNextStepCommandTemplate.Replace("@@nexttag@@", $nextStepTag) + "`r`n" + $displayNextStepMessageTemplate.Replace("@@stepNum@@", $nextStepNum)
	
	$nextCommandContent | out-file 'jumpToNextStep.ps1' -enc ascii
	git add jumpToNextStep.ps1 > $null

	git commit -m "Add step navigation commands" > $null
}

function addEndStepNavigationCommand(){
	$nextCommandContent = $jumpToEndStepCommandTemplate + "`r`n" + $displayEndMessageTemplate

	$nextCommandContent | out-file 'jumpToNextStep.ps1' -enc ascii
	git add jumpToNextStep.ps1 > $null

	git commit -m "Add end step navigation commands" > $null
}

function pickCommitForSolution($line){
	$hash = extraCommitHashOfLog $line

	Write-Host -NoNewline "."

	$isKoTest = isFailedTestCommit $line
	$isFirstTestOfStep = $currentTestOfStep -eq 1
	if($isKoTest -and $isFirstTestOfStep){
		if((hasNextStep)) {
			addStepNavigationCommand (getNextStepTag) ($currentStep + 1)
		} else {
			addEndStepNavigationCommand
		}
	}

	git cherry-pick $hash > $null

	if($isKoTest -and $isFirstTestOfStep){
		git tag (getCurrentStepTag) > $null

		Write-Host ((getCurrentStepTag) + " Ok")
	}

	if($isKoTest){
		nextTest
	}
}

function getCommitLog($branch){
	git log $branch --pretty=tformat:'%h %s' --reverse -E HEAD..
}

function initializeNavigationScript(){
	$batWrapperTemplate.Replace("@@scriptname@@", 'jumpToNextStep') | out-file 'jumpToNextStep.bat' -enc ascii
	$batWrapperTemplate.Replace("@@scriptname@@", 'next') | out-file 'next.bat' -enc ascii
	
	git add jumpToNextStep.bat > $null
	git add next.bat > $null
	
	git commit -m "Add bat wrapper to navigation commands" > $null
}

function initializeSolutionBranch($referenceBranch){
	Write-Host "Initialize solution branch"

	resetTestCounter

	git checkout -b $solutionBranch $masterBranch > $null
	initializeNavigationScript
	getCommitLog $referenceBranch | %{ pickCommitForSolution $_ }

	Write-Host "Done"
}

function addNavigationCommand($nextTestTag, $nextTestNum, $currentStepNum){
	$nextCommandContent = $nextCommandTemplate.Replace("@@nexttag@@", $nextTestTag)
	if((getNextTestNum) -eq 1) {
		$nextCommandContent += "`r`n" + $displayNextStepMessageTemplate.Replace("@@stepNum@@", $currentStepNum + 1)
	} else {
		$nextCommandContent += "`r`n" + $displayNextTestMessageTemplate.Replace("@@stepNum@@", $currentStepNum).Replace("@@testNum@@", $nextTestNum)
	}

	$nextCommandContent | out-file 'next.ps1' -enc ascii
	git add next.ps1 > $null

	git commit -m "Add test navigation commands" > $null
}

function addEndNavigationCommand(){
	$nextCommandContent = $nextCommandTemplate.Replace("@@nexttag@@", $testBranch) + "`r`n" + $displayEndMessageTemplate
	$nextCommandContent | out-file 'next.ps1' -enc ascii
	git add next.ps1 > $null

	git commit -m "Add end test navigation commands" > $null
}

function pickCommitForTest($line){
	$hash = extraCommitHashOfLog $line
	
	Write-Host -NoNewline "."

	git cherry-pick $hash > $null

	if (isFailedTestCommit $line) {
		if((hasNextStep) -or (hasNextTestForCurrentStep)) {
			addNavigationCommand (getNextTestTag) (getNextTestNum) ($currentStep)
		} else {
			addEndNavigationCommand
		}

		git tag (getCurrentTestTag) > $null
		Write-Host ((getCurrentTestTag) + " Ok")

		nextTest
	}
}

function getCommitLogWithoutGreenTest($branch){
	git log $branch --pretty=tformat:'%h %s' --grep '[^K]\][^\[]' --grep '^[^\[]' --reverse -E HEAD..
}

function initializeTestBranch(){
	Write-Host "Initialize test branch"

	resetTestCounter

	git checkout -b $testBranch $masterBranch > $null
	getCommitLogWithoutGreenTest $solutionBranch | %{ pickCommitForTest $_ }

	Write-Host "Done"
}

function initializeWorkflow(){
	Write-Host "Initialize workspace"
	
	resetTestCounter

	git checkout -b $workshopBranch (getCurrentTestTag)
}

function customInitialize(){
	if (Test-Path ./initialize.bat) {
		& ./initialize.bat
	}
}

function displayWarningIfNotMaster(){
	$currentBranch = git name-rev --name-only HEAD
	if($currentBranch -ne "master") {
		$confirmation = Read-Host "Are you sure you want to reinit everything? All your work will be lost! (y/N)"
		if ($confirmation.ToLower() -ne 'y') {
			exit  
		}
	}
}

displayWarningIfNotMaster

$selectedLanguage = askLanguage

clean
initializeSolutionBranch $languages.$selectedLanguage
initializeTestBranch
initializeWorkflow

customInitialize

Write-Host "Koan OK"
Write-Host ""
Write-Host ""
Get-Content stepsDoc/step1.txt | Write-Host -f green
Write-Host ""
Write-Host ""

```

