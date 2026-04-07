---
id: lobster
type: knowledge
owner: OA_Triage
---
# lobster
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
Welcome to the Lobster programming language!
============================================


Lobster is a statically typed programming language with a Python-esque
syntax that combines the advantages of an expressive type system and
compile-time memory management with a very lightweight, friendly and
terse syntax, by doing most of the heavy lifting for you.

The homepage has more on [the "why" of Lobster](http://strlen.com/lobster/).

Read the full
[documentation](http://aardappel.github.io/lobster/README_FIRST.html)
on how to use it, or skip straight to the
[getting started](http://aardappel.github.io/lobster/getting_started.html) guide.


Lobster is licensed under the Apache v2 license.

Wouter van Oortmerssen

![CI](https://github.com/aardappel/lobster/workflows/CI/badge.svg)
[![Discord Chat](https://img.shields.io/badge/chat-discord-blue)](https://discord.gg/szJPYdX)
[![Twitter Follow](https://img.shields.io/twitter/follow/wvo.svg?style=social)](https://twitter.com/wvo)

```

### File: bin\steam_appid.txt
```txt
480
```

### File: docs\command_line_usage.html
```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>Using Lobster from the command line</title>
  <style>
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    div.columns{display: flex; gap: min(4vw, 1.5em);}
    div.column{flex: auto; overflow-x: auto;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    /* The extra [class] is a hack that increases specificity enough to
       override a similar rule in reveal.js */
    ul.task-list[class]{list-style: none;}
    ul.task-list li input[type="checkbox"] {
      font-size: inherit;
      width: 0.8em;
      margin: 0 0.8em 0.2em -1.6em;
      vertical-align: middle;
    }
    .display.math{display: block; text-align: center; margin: 0.5rem auto;}
  </style>
  <link rel="stylesheet" href="github.css" />
  <link rel="icon" type="image/svg" href="lobster.svg" />
</head>
<body>
<header id="title-block-header">
<h1 class="title">Using Lobster from the command line</h1>
</header>
<h2 id="basic-usage">Basic usage</h2>
<p>If you have a file <code>helloworld.lobster</code> that contains</p>
<pre><code>print &quot;Hello, World!&quot;</code></pre>
<p>then running it like so will compile and run it:</p>
<pre><code>bin/lobster helloworld.lobster</code></pre>
<h2 id="command-line-options">Command line options</h2>
<p>Format: <code>lobster [ OPTIONS ] [ FILE ] [ -- ARGS ]</code></p>
<ul>
<li><p><code>FILE</code> : main Lobster file to compile &amp;
run.</p></li>
<li><p><code>-- ARGS</code> pass args to the running Lobster program,
available from <code>command_line_arguments()</code>. Must be last on
the command-line.</p></li>
<li><p><code>--pak</code> or <code>--rpak</code> : generates a pakfile
(currently always called "<code>default.lpak</code>") in the same folder
as the <code>.lobster</code> file it reads, and doesn't run the program
afterwards. If you run lobster with no arguments at all, it will try to
load "<code>default.lpak</code>" from the same folder it resides in.
Only <code>--rpak</code> includes runnable code in the pak, useful with
jit mode runs, whereas without is useful with executables build with
<code>--cpp</code>. Distributing programs created in lobster can be as
simple as packaging up the lobster executable with a runnable pakfile.
The pakfile contains the libtcc C code, and any data files you have
specified with the <code>pakfile</code> keyword, see “Distributing
Lobster programs” in the <a
href="implementation.html">implementation</a> documentation.</p></li>
<li><p><code>--cpp</code> : compiles to a .cpp file. Please make sure to
follow <a href="implementation.html">implementation</a> on how to use
this feature. Useful if you’ve created something in Lobster that could
use a bit more speed, for a shipping build. Not recommend to be used
during development.</p></li>
<li><p><code>--import RELDIR</code> specifies a dir relative to FILE
from which <code>import</code> (and <code>pakfile</code>) statements can
be resolved, or any loading the running program does. Does the same as
adding <code>import from "RELDIR"</code> to the top of your
program.</p></li>
<li><p><code>--runtime-no-asserts</code> : Compile with asserts off,
don't use unless you know what you're doing.</p></li>
<li><p><code>--runtime-asserts</code> : Compile with asserts on
(default).</p></li>
<li><p><code>--runtime-stack-traces</code> : Compile with asserts on +
line info + function tracking for better runtime errors (stack traces)
and profiling. Small effect on speed.</p></li>
<li><p><code>--runtime-debug</code> : Same as verbose, but now tones
inlining way down to get better stack traces. Larger effect on
speed.</p></li>
<li><p><code>--runtime-debug-dump</code>: In addition, creates a memory
dump file on error.</p></li>
<li><p><code>--runtime-debugger</code>: Automatically breaks into the
graphical debugger on errors.</p></li>
<li><p><code>--main MAIN</code> : after compiling FILE, if present,
compile this file and run it. This is useful when running Lobster from
an editor, where you may be editing a module that is not the main file,
would like to see that it compiles by itself, but to run it need to be
launching the main Lobster program it belongs to (e.g.
<code>main.lobster</code> in the same folder).</p></li>
<li><p><code>--wait</code> : makes the compiler wait for commandline
input before it exits. Useful in Windows batch files.</p></li>
<li><p><code>--noconsole</code> : Close console window
(Windows)</p></li>
<li><p><code>--verbose</code> : verbose mode, outputs additional stats
about the program being compiled/run. <code>--debug</code> outputs even
more, only useful for working on the compiler.</p></li>
<li><p><code>--silent</code> : Only output errors.</p></li>
<li><p><code>--full-error</code> : Lobster is able to generate
<em>compile time stack traces</em> when the typechecker fails, but those
can get long, so by default they get truncated. Use this option to not
truncate them, and also dump additional information on free/local
variables in the function context.</p></li>
<li><p><code>--gen-builtins-html</code> : dumps a help file of all
builtin functions the compiler knows about to
<code>builtin_functions_reference.html</code>.
<code>--gen-builtins-names</code> dumps a plain text list of functions,
useful for adding to syntax highlighting files etc.</p></li>
<li><p><code>--parsedump</code> : dumps internal representations of the
program as AST. Only useful for compiler development or if you are
really curious.</p></li>
<li><p><code>--non-interactive-test</code> : Quit after running 1 frame.
Useful for running graphical programs as part of a test suite.</p></li>
<li><p><code>--query</code>: Ask the compiler to answer a query about
definitions in the program being compiled. When is this mode, the
compiler does not try to do a full compilation, but simply tries to
answer the query, including ignoring errors or aborting half-way if it
has to. This option is for use by an IDE or LSP server implementation.
All further args are passed to the query. The first arg is the kind of
query (e.g. <code>definition</code> or <code>complete</code>). The
second arg is the file this query should take place in (as a relative
path, i.e <code>foo/bar.lobster</code>). The 3rd arg is the line where
the query should happen. The 4th arg is the identifier the query is
about. The rest of the args depend on the query type, if any. For
<code>definition</code> a response will be the location of the
definition. For <code>complete</code>, it will return a list of possible
fields/methods.</p></li>
</ul>
<p>Lobster source code may start with a shebang <code>#!</code> so you
can embed the command-line in a Lobster script.</p>
<h2 id="default-directories">Default directories</h2>
<p>It's useful to understand the directories lobster uses, both for
reading source code files and any data files the program may use:</p>
<ul>
<li><p>the root repo directory: This is the main folder that has the
default <code>bin modules data docs samples tests</code> folders inside
of it.</p></li>
<li><p>the auxiliary directory: this is where the main
<code>.lobster</code> file being compiled resides.</p></li>
<li><p>the directory for writing files: the same as auxiliary on desktop
platforms, but often a special directory on mobile platforms.</p></li>
<li><p>On Linux additionally it can load files from
<code>/usr/share/lobster/</code> (or whatever path was configured for
install by CMake, see <code>DATADIR</code>) if the above paths don't
work. This is to allow package managers to install Lobster in the system
directories.</p></li>
</ul>
<p>Additionally, if any of these folders contains a <code>modules</code>
directory, it will load source code from there as well.</p>
<p>Any of the Lobster builtin commands that load data files specify
paths relative to either the main or auxiliary directories (and either /
or \ may be used as path separators). If you package up a Lobster
program for distribution, all these files can be packed into a pakfile,
see <code>--pak</code>.</p>
<h2 id="output">Output</h2>
<p>Running lobster may result in a compiler error, that generally look
something like this:</p>
<pre><code>mygame.lobster(960): error: unknown identifier: highscor</code></pre>
<p>If compiled correctly, running will give you output from your own
print statements, and additionally at some point may cause a runtime
error, which can look something like this:</p>
<pre><code>pythtree.lobster(15): VM error: division by zero
in block -&gt; pythtree.lobster(16)
   i = 0
in block -&gt; pythtree.lobster(16)
in function: branch -&gt; pythtree.lobster(29)
   poly = [[1.000000, 0.000000, 0.000000, 0.000000]:xyzw, [-1.000000, ...]:xyzw, ....]
   len = 4
   scale = 0.700000
   max = 11.000000
   n = 0
in block -&gt; pythtree.lobster(29)</code></pre>
<p>This is called a stack trace. Besides the error and the line it
happened on, it will show all functions and blocks that called that
code, in reverse order, with any local variables and their values. This
helps you get an idea where the problem came from and helps in
debugging.</p>
</body>
</html>

```

### File: docs\C_style language Cheat Sheet for Lobster.html
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>C-style language Cheat Sheet for Lobster</title>

<style type="text/css">
table, tr, td {font-size: 10pt;border: 1pt solid #DDDDDD; border-Collapse: collapse; max-width:1200px; vertical-align:top}
</style></head>
<body>
<div style="text-align: center;"><big style="font-family: Consolas;"><big><big>C-style
language to Lobster Cheat Sheet</big></big></big><br style="font-family: Consolas;">
<span style="font-family: Consolas;"></span><br style="font-family: Consolas;">
</div>
<table style="width: 100%; font-family: Consolas; text-align: left; margin-left: auto; margin-right: auto;" border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td>Since
every programmer usually knows at least one C-style language
(C/C++/C#/Java/JavaScript/PHP etc.), a quick way to get to know Lobster
is seeing how it differs from what you're familiar with. Where C-style
languages differ I will by default pick C# (as being the most
&nbsp;"average" of the range), though sometimes may show multiple
language alternatives (as noted in the comments). This document mostly
focusses on things that are different, i.e. you will not see how a + b
in Lobster is the same as a + b in C#.</td>
</tr>
</tbody>
</table>
<div style="text-align: center;"><big><big><span style="font-family: Consolas;"><br>
Basics</span></big></big><br style="font-family: Consolas;">
<br style="font-family: Consolas;">
</div>
<table style="font-family: Consolas; width: 100%; height: 100%; text-align: left; margin-left: auto; margin-right: auto;" border="1" cellpadding="4" cellspacing="0">
<tbody>
<tr>
<td style="font-weight: bold;"><big>Lobster
version</big></td>
<td style="font-weight: bold;"><big>C-style
version</big></td>
<td style="font-weight: bold;"><big>Comments</big></td>
</tr>
<tr><td>a = 1</td><td>a = 1;</td><td>Assign existing variable.</td></tr><tr><td>var a = 1</td><td>int a = 1;</td><td>Create new variable, type thru type inference.</td></tr><tr><td>let a = 1</td><td>const int a = 1;</td><td>Create constant variable.</td></tr>


<tr>
<td>let a, b&nbsp;= 1, 2</td>
<td>int a = 1; int b = 2;</td>
<td>Define multiple at once.</td>
</tr>
<tr>
<td>let a, b&nbsp;= f()</td>
<td>int a = f(&amp;b);</td>
<td>Define multiple from a function returning multiple values.</td>
</tr>
<tr>
<td style="white-space: nowrap;">let v&nbsp;= [ 1, 2, 3 ]</td>
<td>int[] v = new int[] { 1, 2, 3 };</td>
<td>The type of vectors is inferred. They are also resizable, so they are probably more
akin a C# List than an array.</td>
</tr>
<tr>
<td>let w&nbsp;= v + v</td>
<td style="white-space: nowrap;">vec3 w = new Vec3;<br>w.x = v.x + v.x;<br>w.y = v.y + v.y;<br>w.z = v.z + v.z;</td>
<td>Vector operation exist for most operators and functions.</td>
</tr>
<tr>
<td>nil</td>
<td>null</td>
<td>Nil is more strict in lobster, in that a reference type which can
be nil is different from those that are never nil, and you explicitly
convert between them.</td>
</tr>
<tr>
<td>a or b and c</td>
<td>(a || b) &amp;&amp; c</td>
<td>These are really the only operators that are different.</td>
</tr>
<tr>
<td>let a&nbsp;= f() or g()</td>
<td>var a = f();<br>
if (a == null) a = g();</td>
<td>The or operator works slightly differently in that
rather than returning true, it returns whatever value was true (and
true is everything that is not nil, false, 0 or 0.0)</td>
</tr>
</tbody>
</table>
<div style="text-align: center;"><br style="font-family: Consolas;">
<br style="font-family: Consolas;">
<big><big><span style="font-family: Consolas;">Control
Structures</span></big></big><br style="font-family: Consolas;">
<br style="font-family: Consolas;">
</div>
<table style="font-family: Consolas; width: 100%; height: 100%; text-align: left; margin-left: auto; margin-right: auto;" border="1" cellpadding="4" cellspacing="0">
<tbody>
<tr>
<td style="font-weight: bold;"><big>Lobster
version</big></td>
<td style="font-weight: bold;"><big>C-style
version</big></td>
<td style="font-weight: bold;"><big>Comments</big></td>
</tr>
<tr>
<td>if a: b else: c</td>
<td>if (a) b; else c</td>
<td></td>
</tr>
<tr>
<td>if a:<br>
&nbsp; &nbsp; b<br>
&nbsp; &nbsp; c<br>
else:<br>
&nbsp; &nbsp; d<br>
&nbsp; &nbsp; e</td>
<td>if (a) {<br>&nbsp; &nbsp; b;<br>&nbsp; &nbsp; c;<br>} else {<br>&nbsp; &nbsp;&nbsp;d;<br>&nbsp; &nbsp;&nbsp;e;<br>}</td>
<td></td>
</tr>
<tr>
<td>for(m) i: print i</td>
<td>for (int i = 0; i &lt; m; i++) print(i);</td>
<td></td>
</tr>
<tr>
<td>for m: print _</td>
<td>for (int i = 0; i &lt; m; i++) print(i);</td>
<td></td>
</tr>
<tr>
<td>for(m) i:<br>
&nbsp; &nbsp; print i</td>
<td>for (int i = 0; i &lt; m; i++) {<br>
&nbsp; &nbsp; print(i);<br>
}</td>
<td></td>
</tr>
<tr>
<td>while a: b</td>
<td>while (a) b;</td>
<td></td>
</tr>

<tr>
<td>for(list) a, i:<br>&nbsp; &nbsp; print a<br>&nbsp; &nbsp; print i</td>
<td>for(int i = 0; i &lt; list.size(); i++) {<br>&nbsp; &nbsp; auto a = list[i];<br>&nbsp; &nbsp; print(a);<br>&nbsp; &nbsp; print(i);<br>}</td>
<td>Where `a` is the item at index `i` of `list.</td>
</tr>

<tr>
<td>for(list):<br>&nbsp; &nbsp; print _<br>&nbsp; &nbsp; print _i</td>
<td>for(int _i = 0; _i &lt; list.size(); _i++) {<br>&nbsp; &nbsp; auto _ = list[_i];<br>&nbsp; &nbsp; print(_);<br>&nbsp; &nbsp; print(_i);<br>}</td>
<td>Where `_` is the item at index `_i` of `list`. Here `_` and `_i` are anonymous parameters that Lobster auto populates. They must be prefixed with `_`, and are assigned by their declaration order in the body. </td>
</tr>

<tr>
<td>for(list) a: print a</td>
<td>foreach (var a in list) print(a);</td>
<td></td>
</tr>
<tr><td>let a = switch i:<br>&nbsp; &nbsp; case 1: "no"<br>&nbsp; &nbsp; case 2, 4..6: "yes"<br>&nbsp; &nbsp; default: "maybe"</td><td>switch (i) {<br>&nbsp; &nbsp; case 1:<br>&nbsp; &nbsp; &nbsp; &nbsp; a = "no";<br>&nbsp; &nbsp; &nbsp; &nbsp; break;<br>&nbsp; &nbsp; case 2:<br>&nbsp; &nbsp; case 4:<br>&nbsp; &nbsp; case 5:<br>&nbsp; &nbsp; case 6:<br>&nbsp; &nbsp; &nbsp; &nbsp; a = "yes";<br>&nbsp; &nbsp; &nbsp; &nbsp; break;<br>&nbsp; &nbsp; default:<br>&nbsp; &nbsp; &nbsp; &nbsp; a = "maybe";<br>}</td><td></td></tr><tr>
<td>let r = map(list) x: x * x</td>
<td>var r = new List();<br>
foreach(var x in list) r.Add(x * x);</td>
<td>(map needs: import std)
</td>
</tr>
<tr>
<td>let r = map(list) x: x * x</td>
<td>var r = list.ConvertAll(x =&gt; x * x);</td>
<td>C# and pretty much all programming languages except for
Java (&lt; 8) can nowadays use some form of lambdas that are similar but not
quite as powerful as the ones in Lobster (for example, you can't use
"return" to break out of a loop).</td>
</tr>
<tr>
<td>let r = filter list: _ &gt; 0</td>
<td>var r = new List();<br>
foreach (var x in list) if (x
&gt; 0) r.Add(x);</td>
<td></td>
</tr>
<tr>
<td style="white-space: nowrap;">let r = exists list: _ &gt; 0</td>
<td style="white-space: nowrap;">var r = false;<br>
foreach (var x in list) if (x
&gt; 0) { r = true; break; }</td>
<td></td>
</tr>

</tbody>
</table>
<div style="text-align: center;"><br style="font-family: Consolas;">
<br style="font-family: Consolas;">
<big><big><span style="font-family: Consolas;">Function
Definitions
and Scope</span></big></big><br style="font-family: Consolas;">
<br style="font-family: Consolas;">
</div>
<table style="font-family: Consolas; width: 100%; height: 100%; text-align: left; margin-left: auto; margin-right: auto;" border="1" cellpadding="4" cellspacing="0">
<tbody>
<tr>
<td style="font-weight: bold;"><big>Lobster
version</big></td>
<td style="font-weight: bold;"><big>C-style
version</big></td>
<td style="font-weight: bold;"><big>Comments</big></td>
</tr>
<tr><td>def&nbsp;name(a:int, b:int) -&gt; int:<br>&nbsp; &nbsp;&nbsp;return a + b</td><td>int name(int a, int b) { return a + b; }</td><td>In Lobster it is unusual to specify types, especially the return type.</td></tr><tr>
<td>def&nbsp;name(a, b):<br>&nbsp; &nbsp; return a + b</td>
<td>T&nbsp;name&lt;T&gt;(T a, T b) { return a + b; }</td>
<td>By default function are declared without types, and automatically inferred on use.<br></td>
</tr>
<tr>
<td>def&nbsp;name(a, b):<br>
&nbsp; &nbsp; return a + b</td>
<td>T&nbsp;name&lt;T&gt;(T a, T b) {<br>
&nbsp; &nbsp; return a + b;<br>
}</td>
<td>For multiple lines, use indentation.</td>
</tr>
<tr>
<td style="white-space: nowrap;">def&nbsp;magnitude(v::xy):<br>&nbsp; &nbsp; return sqrt(x * x + y * y)</td>
<td style="white-space: nowrap;">// inside class xy<br>
float&nbsp;magnitude() { return sqrt(x * x + y * y); }</td>
<td>The :: way to indicate a type (v is of type xy) allows you to access
object elements directly rather than having to write v.x etc. This is
similar to writing a&nbsp;method, though Lobster makes no such distinction.</td>
</tr>
<tr><td>// inside class/struct xy<br>def&nbsp;magnitude():<br>&nbsp; &nbsp; return sqrt(x * x + y * y)</td><td>// inside class xy<br>
float&nbsp;magnitude() { return sqrt(x * x + y * y); }</td><td>This is an equivalent way of writing the above when inside the scope of a class/struct (see below).</td></tr><tr>
<td>v.magnitude()</td>
<td>v.magnitude()</td>
<td>On a function call, you can move the first argument to
before the call, for <span style="font-style: italic;">any</span>
function, not just "methods".</td>
</tr>
<tr>
<td>def&nbsp;name(x:X): return 0<br>
def name(y:Y): return 1</td>
<td>/* inside class X */ int name() { return 0; }<br>
/* inside class Y */ int name() { return 1; }</td>
<td>You write multiple function implementations for multiple types,
which can then be called and resolved either statically (overloading)
or dynamically (dynamic dispatch) depending on the situation. These
functions can work on user defined
types or builtin ones. They can be written by whoever wrote the type
(even in-line in the class definition), or completely separately. </td>
</tr>

<tr>
<td>let f&nbsp;= def(a, b):&nbsp;a + b</td>
<td>var f = (int a, int b) =&gt; a + b</td>
<td>Function value in C#</td>
</tr>
<tr>
<td>let f&nbsp;= def(a, b): a + b</td>
<td>auto f = [](int a, int a) { return a + b; }</td>
<td>Function value in C++</td>
</tr>
<tr>
<td>def&nbsp;fold(xs, init, fun): <br>&nbsp;&nbsp;&nbsp; for(xs): init = fun(init, _)<br>&nbsp;&nbsp;&nbsp; return init</td>
<td>T fold&lt;T&gt;(List&lt;T&gt; xs, T init, Func&lt;T, T, T&gt; fun) {<br>&nbsp; &nbsp; foreach (var x in xs) init = fun(init, x);<br>&nbsp; &nbsp; return init;<br>}</td>
<td>How to write a <span style="font-style: italic;">Higher Order Function</span>:
a function that takes a function argument. In this case "fold": take a
list, and apply the function to each element and the previous result,
effectively "folding" the list into a single value.</td>
</tr>
<tr>
<td>let r = fold(list, 0) a, b: a + b</td>
<td>var r = fold(list, 0, (a, b) =&gt; a + b);</td>
<td>How to call that function with a function value. This sums all values in a list.</td>
</tr>
<tr>
<td>let r = fold(list, 0): _a + _b</td>
<td>var r = fold(list, 0, (a, b) =&gt; a + b);</td>
<td>Anonymous arguments in lexical order, see language reference.</td>
</tr>
<tr>
<td>let r = fold(list, 0) a, b:<br>&nbsp; &nbsp; print a<br>&nbsp; &nbsp;&nbsp;a +&nbsp;b</td>
<td>var r = fold(list, 0, (a, b) =&gt; {<br>&nbsp; &nbsp; print(a);<br>&nbsp; &nbsp; return a + b;<br>});</td>
<td>Note how in most languages lambda syntax becomes messy when you
want to use them with a larger body, and looking very different from
builtin control structures.</td>
</tr>
<tr>
<td>let r = fold(list, 0) a, b:<br>&nbsp; &nbsp; if a &lt; 0: return a<br>&nbsp; &nbsp;&nbsp;a +&nbsp;b</td>
<td>/* not possible */</td>
<td>Another way in which lambdas in most languages differ from Lobster:
you cannot return/break
from the loop, making them often useless as control structures. In
Lobster, they function just like real constrol structures would. By
default, return returns from the lexically enclosing named function.</td>
</tr>
<tr>
<td>def&nbsp;f():<br>&nbsp; &nbsp; g()<br>&nbsp; &nbsp; return 0<br>def&nbsp;g():<br>&nbsp; &nbsp; if something: return 1 from f<br>&nbsp; &nbsp; return 0</td>
<td>int f() {<br>&nbsp; &nbsp; try { g(); return 0; }<br>&nbsp; &nbsp; catch (int x) { return x; }<br>}<br>int g() {<br>&nbsp; &nbsp; if (something) throw 1;<br>&nbsp; &nbsp; return 0;<br>}</td>
<td>Return even allows you to specify which function to return from,
which in other languages you can do with exception handling. In fact,
exception handling in Lobster is not a language feature, it is simply
some utility functions (try/catch/...) implemented on top of
return/from (implemented in exception.lobster).</td>
</tr>










<tr>
<td>def&nbsp;mret(): return 1, 2</td>
<td style="white-space: nowrap;">int mret(out int o)
{ o = 2; return 1; }</td>
<td></td>
</tr>
<tr>
<td>let a, b&nbsp;= mret()</td>
<td>var b; var a = mret(&amp;b);</td>
<td></td>
</tr>




</tbody>
</table>
<div style="text-align: center;"><br style="font-family: Consolas;">
<br style="font-family: Consolas;">
<big><big><span style="font-family: Consolas;">User
Defined Types</span></big></big><br style="font-family: Consolas;">
<br style="font-family: Consolas;">
</div>
<table style="font-family: Consolas; width: 100%; height: 100%; text-align: left; margin-left: auto; margin-right: auto;" border="1" cellpadding="4" cellspacing="0">
<tbody>
<tr>
<td style="font-weight: bold;"><big>Lobster
version</big></td>
<td style="font-weight: bold;"><big>C-style
version</big></td>
<td style="font-weight: bold;"><big>Comments</big></td>
</tr>
<tr>
<td>struct xy:<br>&nbsp; &nbsp;&nbsp;x:float<br>&nbsp; &nbsp;&nbsp;y:float</td>
<td>public struct xy { float x; float y; }</td>
<td><br></td>
</tr>
<tr>
<td>struct xy&lt;T&gt;<br>&nbsp; &nbsp;&nbsp;x:T<br>&nbsp; &nbsp;&nbsp;y:T</td>
<td>public struct xy&lt;T&gt; { T x; T y; }</td>
<td>Generics: unlike functions, these are explicitly specified in Lobster.</td>
</tr>

<tr>
<td>struct xyz : xy:<br>&nbsp; &nbsp;&nbsp;z:float</td>
<td>public struct xyz : xy { float z; }</td>
<td>Inheritance.</td>
</tr>
<tr>
<td>let v&nbsp;= xyz { 1, 0, 0 }</td>
<td>var v = new xyz(1, 0, 0)</td>
<td>You'd actually have to define the constructor in C# to
be able to do this.</td>
</tr><tr><td>struct xy:<br>&nbsp; &nbsp; x:float<br>&nbsp; &nbsp; y:float<br>&nbsp; &nbsp; def&nbsp;magnitude():<br>&nbsp; &nbsp; &nbsp; &nbsp; return sqrt(x * x + y * y)</td><td>public class xy {<br>&nbsp; &nbsp; float x;<br>&nbsp; &nbsp; float y;<br>
&nbsp; &nbsp; float&nbsp;magnitude() {<br>&nbsp; &nbsp; &nbsp; &nbsp; return x * x + y * y;<br>&nbsp; &nbsp; }<br>}</td><td>Intendation based syntax, with inline function definition (automatic this argument).</td></tr><tr><td>enum color:<br>&nbsp; &nbsp; red = 1<br>&nbsp; &nbsp; green<br>&nbsp; &nbsp; blue<br>&nbsp; &nbsp; yellow = 10</td><td>enum color {<br>&nbsp; &nbsp; red = 1,<br>&nbsp; &nbsp; green,<br>&nbsp; &nbsp; blue,<br>&nbsp; &nbsp; yellow = 10<br>}</td><td></td></tr>







</tbo
... [TRUNCATED]
```

### File: docs\engine.html
```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>Lobster built-in engine functionality</title>
  <style>
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    div.columns{display: flex; gap: min(4vw, 1.5em);}
    div.column{flex: auto; overflow-x: auto;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    /* The extra [class] is a hack that increases specificity enough to
       override a similar rule in reveal.js */
    ul.task-list[class]{list-style: none;}
    ul.task-list li input[type="checkbox"] {
      font-size: inherit;
      width: 0.8em;
      margin: 0 0.8em 0.2em -1.6em;
      vertical-align: middle;
    }
    .display.math{display: block; text-align: center; margin: 0.5rem auto;}
  </style>
  <link rel="stylesheet" href="github.css" />
  <link rel="icon" type="image/svg" href="lobster.svg" />
</head>
<body>
<header id="title-block-header">
<h1 class="title">Lobster built-in engine functionality</h1>
</header>
<p>Lobster comes with "batteries included": a small (games/graphics)
engine that allows you to start drawing straight away. This doc collects
some notes on the built-in functionality.</p>
<h2 id="basics">Basics</h2>
<p>The basic list of <a href="builtin_functions_reference.html">builtin
functions</a> is worth browsing first, as well as the <a
href="shooter_tutorial.html">shooter tutorial</a> for some basic
explanation of how to render stuff. Most examples in the
<code>samples</code> dir are graphical and provide further examples.</p>
<p>While it easy to render stuff with simple functions like
<code>gl.rect</code>, <code>gl.line</code> and stuff, for anything more
advanced some understanding of OpenGL style rendering is required.</p>
<h2 id="default-rendering-environment">Default rendering
environment</h2>
<p>After you call <code>gl.window</code> you are left with a default
black background, a white drawing color, and the <code>color</code>
shader set.</p>
<h2 id="shaders">Shaders</h2>
<p>All basic shaders, including <code>color</code>, can be found in
<code>data/shaders/default.materials</code>.</p>
<p>You can use one of the many useful shaders from there with
<code>gl.set_shader</code>, but more fun is to use a custom shader. You
can define these in-line in your Lobster program as well, an example of
that can be found in
<code>samples/custom_shader_metaballs.lobster</code>.</p>
<p>Lobster uses glsl shaders compatible with OpenGL 3+ and OpenGL ES 3+,
and you'll have to look elsewhere to learn the details of this
language.</p>
<p>Lobster wraps these shaders in a custom declaration language, to cut
down on some of the boilerplate of putting a vertex and pixel shader
together.</p>
<p>Lets look at the <code>textured</code> shader as an example:</p>
<pre><code>SHADER textured
    VERTEX
        INPUTS apos:4 atc:2
        UNIFORMS mvp
        gl_Position = mvp * apos;
        itc = atc;
    PIXEL
        INPUTS itc:2
        UNIFORMS tex0 col
        frag_color = texture(tex0, itc) * col;</code></pre>
<p>In all caps we have keywords that help declare these shaders for you.
We have a <code>VERTEX</code> and <code>PIXEL</code> part
(alternatively, you could have only a <code>COMPUTE</code> part).</p>
<p>The inputs to the vertex shader must match your vertex attributes,
specify the number of components you care about after <code>:</code>,
and come from a fixed set of:</p>
<ul>
<li><code>apos</code> (position, 2 or 3 components in the vertex buffer,
but usually 4 in the shader to work with matrix transforms).</li>
<li><code>anormal</code> (3 components).</li>
<li><code>atc</code> (texture coordinate, 2 components).</li>
<li><code>acolor</code> (4 components)</li>
<li><code>aweights</code> and <code>aindices</code> (used with character
animation).</li>
</ul>
<p>The outputs of the vertex shader are automatically the same as the
pixel shader inputs, here <code>itc</code> (interpolated texture
coordinate).</p>
<p>Using <code>UNIFORMS</code> you declare variables automatically
provided by the engine:</p>
<ul>
<li><code>mvp</code>: the Model View Projection matrix composed of the
various <code>gl.scale</code>, <code>gl.translate</code> and
<code>gl.rotate</code> transforms (the <code>mv</code> part) and the
<code>gl.ortho</code> or <code>gl.perspective</code> transforms (the
<code>p</code> part).</li>
<li><code>col</code>: set by <code>gl.color</code>.</li>
<li><code>camera</code>: position of the camera relative to the
primitive being rendered.</li>
<li><code>light1</code> and <code>lightparams1</code>: set by
<code>gl.light</code>.</li>
<li><code>framebuffer_size</code>: size in pixels.</li>
<li><code>bones</code>: see character animation shaders.</li>
<li><code>pointscale</code>: used with point rendering.</li>
</ul>
<p>In addition you can add any custom uniforms with a
<code>UNIFORM</code> declaration, for example by adding
<code>UNIFORM float time</code> to the shader and
<code>gl.set_uniform("time", gl.time())</code> you can animate your
shader to the current time.</p>
<p>Following these is the raw glsl implementing the shader. This is the
body of the shader, if you want to add additional helper functions,
write a <code>VERTEXFUNCTIONS</code> or <code>PIXELFUNCTIONS</code>
block before the shader. The functions declared here will be available
to all shaders following it.</p>
<p>Additionally <code>DEFINE name val</code> defines macros to be used
in the shaders below.</p>
<p>For compute shaders, e.g. <code>COMPUTE 8 8</code> at the end of the
uniforms declares the dispatch size.</p>
<p>Any more details, see <code>glshader.cpp</code> ;)</p>
</body>
</html>

```

### File: docs\getting_started.html
```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>Quick Getting Started Guide.</title>
  <style>
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    div.columns{display: flex; gap: min(4vw, 1.5em);}
    div.column{flex: auto; overflow-x: auto;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    /* The extra [class] is a hack that increases specificity enough to
       override a similar rule in reveal.js */
    ul.task-list[class]{list-style: none;}
    ul.task-list li input[type="checkbox"] {
      font-size: inherit;
      width: 0.8em;
      margin: 0 0.8em 0.2em -1.6em;
      vertical-align: middle;
    }
    .display.math{display: block; text-align: center; margin: 0.5rem auto;}
  </style>
  <link rel="stylesheet" href="github.css" />
  <link rel="icon" type="image/svg" href="lobster.svg" />
</head>
<body>
<header id="title-block-header">
<h1 class="title">Quick Getting Started Guide.</h1>
</header>
<h2 id="get-pre-built-binaries-windows-mac-linux">Get pre-built binaries
(Windows, Mac, Linux)</h2>
<h3 id="latest-version-from-ci">Latest version from CI</h3>
<p>If you don't want to deal with building it yourself, go to <a
href="https://github.com/aardappel/lobster/actions?query=workflow%3ACI">github
CI</a> (click on the latest succesful run to get a list of binaries at
the bottom). These are 64-bit for all platforms.</p>
<p>Note: if you're NOT seeing a list of artifacts at the bottom of each
run, that may be because you're not logged in to github.</p>
<p>Now get https://github.com/aardappel/lobster (download zip). This has
all the data files and examples. Place the binary you obtained in
<code>bin</code> folder of the repo (not <code>/bin</code>).</p>
<h3 id="releases">Releases</h3>
<p>There may occasionally be builds on
https://github.com/aardappel/lobster/releases
(<code>lobster_&lt;date&gt;_&lt;platform&gt;.zip</code> and
<code>Source code (zip)</code>), but these are usually way behind using
the most recent builds above, so not recommended.</p>
<h2 id="or-build-it-yourself">Or, build it yourself!</h2>
<h3 id="linux">Linux</h3>
<p>Pre-Requirements: Git, CMake, a C++17 compiler, Mesa dev files
(<code>apt-get install mesa-common-dev</code>).</p>
<pre><code>git clone https://github.com/aardappel/lobster.git
cd lobster/dev
cmake -DCMAKE_BUILD_TYPE=Release
make -j8
cd ..
bin/lobster samples/pythtree.lobster</code></pre>
<h3 id="windows">Windows</h3>
<p>Pre-Requirements: VS2022 Community edition or better, C++ desktop
tools installed.</p>
<p>Get https://github.com/aardappel/lobster using your favorite git tool
(best), or just download a <code>.zip</code> from there otherwise.</p>
<p>Open <code>dev\lobster\lobster.sln</code>, ensure
<code>Release</code> is selected in the top bar,
<code>Build -&gt; Build Solution</code>, then close if no errors.</p>
<h3 id="mac">Mac</h3>
<p>Pre-Requirements: Latest XCode &amp; CMake.</p>
<p>Get https://github.com/aardappel/lobster using your favorite git tool
(best), or just download a <code>.zip</code> otherwise.</p>
<p>From the terminal, in the <code>dev</code> folder, run
<code>sh build_osx.sh</code> which will generate an Xcode project in the
<code>xcode-cmake</code> sub-folder.</p>
<p>Open <code>dev/xcode-cmake/Lobster.xcodeproj</code>, ensure
<code>lobster &gt; My Mac</code> is selected as scheme in the top bar,
<code>Product -&gt; Build for -&gt; Profiling</code> (to get a Release
build), then close if no errors.</p>
<p>Alternatively from the terminal from the <code>xcode-cmake</code>
folder:</p>
<p><code>xcodebuild -toolchain clang -configuration Release -target lobster</code></p>
<h2 id="running-it">Running it</h2>
<p>You now have a <code>lobster</code> executable in your
<code>bin</code> folder. You can run this with any Lobster file as
argument to run it, for example
<code>bin/lobster.exe samples/pythtree.lobster</code> should work.</p>
<h2 id="more-docs">More Docs</h2>
<p>For more advanced usage, including how to run it from an editor,
check the rest of <a href="README_FIRST.html">the docs</a></p>
</body>
</html>

```

### File: docs\github.css
```css
/* GitHub stylesheet for MarkdownPad */
/* Author: Nicolas Hery - http://nicolashery.com */
/* Version: d5e7ce436666e7d4a2eeb12e7f8261dacceb3565 */
/* Source: https://github.com/nicolahery/markdownpad-github */

/* RESET
=============================================================================*/

html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
}

/* BODY
=============================================================================*/

body {
  font-family: Helvetica, arial, freesans, clean, sans-serif;
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  background-color: #fff;
  padding: 20px;
  max-width: 960px;
  margin: 0 auto;
}

body>*:first-child {
  margin-top: 0 !important;
}

body>*:last-child {
  margin-bottom: 0 !important;
}

/* BLOCKS
=============================================================================*/

p, blockquote, ul, ol, dl, table, pre {
  margin: 15px 0;
}

/* HEADERS
=============================================================================*/

h1, h2, h3, h4, h5, h6 {
  margin: 20px 0 10px;
  padding: 0;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
}

h1 tt, h1 code, h2 tt, h2 code, h3 tt, h3 code, h4 tt, h4 code, h5 tt, h5 code, h6 tt, h6 code {
  font-size: inherit;
}

h1 {
  font-size: 28px;
  color: #000;
}

h2 {
  font-size: 24px;
  border-bottom: 1px solid #ccc;
  color: #000;
}

h3 {
  font-size: 18px;
}

h4 {
  font-size: 16px;
}

h5 {
  font-size: 14px;
}

h6 {
  color: #777;
  font-size: 14px;
}

body>h2:first-child, body>h1:first-child, body>h1:first-child+h2, body>h3:first-child, body>h4:first-child, body>h5:first-child, body>h6:first-child {
  margin-top: 0;
  padding-top: 0;
}

a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
  margin-top: 0;
  padding-top: 0;
}

h1+p, h2+p, h3+p, h4+p, h5+p, h6+p {
  margin-top: 10px;
}

/* LINKS
=============================================================================*/

a {
  color: #4183C4;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* LISTS
=============================================================================*/

ul, ol {
  padding-left: 30px;
}

ul li > :first-child, 
ol li > :first-child, 
ul li ul:first-of-type, 
ol li ol:first-of-type, 
ul li ol:first-of-type, 
ol li ul:first-of-type {
  margin-top: 0px;
}

ul ul, ul ol, ol ol, ol ul {
  margin-bottom: 0;
}

dl {
  padding: 0;
}

dl dt {
  font-size: 14px;
  font-weight: bold;
  font-style: italic;
  padding: 0;
  margin: 15px 0 5px;
}

dl dt:first-child {
  padding: 0;
}

dl dt>:first-child {
  margin-top: 0px;
}

dl dt>:last-child {
  margin-bottom: 0px;
}

dl dd {
  margin: 0 0 15px;
  padding: 0 15px;
}

dl dd>:first-child {
  margin-top: 0px;
}

dl dd>:last-child {
  margin-bottom: 0px;
}

/* CODE
=============================================================================*/

pre, code, tt {
  font-size: 12px;
  font-family: Consolas, "Liberation Mono", Courier, monospace;
}

code, tt {
  margin: 0 0px;
  padding: 0px 0px;
  white-space: nowrap;
  border: 1px solid #eaeaea;
  background-color: #f8f8f8;
  border-radius: 3px;
}

pre>code {
  margin: 0;
  padding: 0;
  white-space: pre;
  border: none;
  background: transparent;
}

pre {
  background-color: #f8f8f8;
  border: 1px solid #ccc;
  font-size: 13px;
  line-height: 19px;
  overflow: auto;
  padding: 6px 10px;
  border-radius: 3px;
}

pre code, pre tt {
  background-color: transparent;
  border: none;
}

/* QUOTES
=============================================================================*/

blockquote {
  border-left: 4px solid #DDD;
  padding: 0 15px;
  color: #777;
}

blockquote>:first-child {
  margin-top: 0px;
}

blockquote>:last-child {
  margin-bottom: 0px;
}

/* HORIZONTAL RULES
=============================================================================*/

hr {
  clear: both;
  margin: 15px 0;
  height: 0px;
  overflow: hidden;
  border: none;
  background: transparent;
  border-bottom: 4px solid #ddd;
  padding: 0;
}

/* TABLES
=============================================================================*/

table th {
  font-weight: bold;
}

table th, table td {
  border: 1px solid #ccc;
  padding: 6px 13px;
}

table tr {
  border-top: 1px solid #ccc;
  background-color: #fff;
}

table tr:nth-child(2n) {
  background-color: #f8f8f8;
}

/* IMAGES
=============================================================================*/

.markdown-body img {
  max-width: 100%
}

```

### File: docs\implementation.html
```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>The Lobster C++ Implementation</title>
  <style>
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    div.columns{display: flex; gap: min(4vw, 1.5em);}
    div.column{flex: auto; overflow-x: auto;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    /* The extra [class] is a hack that increases specificity enough to
       override a similar rule in reveal.js */
    ul.task-list[class]{list-style: none;}
    ul.task-list li input[type="checkbox"] {
      font-size: inherit;
      width: 0.8em;
      margin: 0 0.8em 0.2em -1.6em;
      vertical-align: middle;
    }
    .display.math{display: block; text-align: center; margin: 0.5rem auto;}
  </style>
  <link rel="stylesheet" href="github.css" />
  <link rel="icon" type="image/svg" href="lobster.svg" />
</head>
<body>
<header id="title-block-header">
<h1 class="title">The Lobster C++ Implementation</h1>
</header>
<p>This document gives hints on how to work with the Lobster C++ code in
terms of building, extending, reusing, and compiling Lobster code to
C++.</p>
<p>Lobster has been released under the Apache 2 open source license.</p>
<h2 id="building-lobster">Building Lobster</h2>
<p>Lobster uses recent C++17 features, so will need Visual Studio 2022
(the free community edition will do), latest Xcode, or a very recent GCC
/ Clang to be compiled.</p>
<p>Lobster uses OpenGL, SDL 2.x and FreeType, these are included in the
repo, so should compile out of the box with no further external
dependencies.</p>
<p>All source code and other files related to building Lobster for all
platforms sit in the <code>dev</code> folder.</p>
<p>Lobster should be built for 64-bit platforms where possible. It will
still also build on 32-bit Wasm &amp; Android. This does not affect
Lobster data type sizes, e.g. <code>int</code> and <code>float</code>
types are 64-bit on all platforms.</p>
<p>Lobster can be built with a JIT (on desktop platforms, convenient
during development, as it can run Lobster source "instantly"), or by
compiling to C++ (possible on all platforms, required on non-desktop),
see below.</p>
<h3 id="windows">Windows</h3>
<p>Open up <code>dev\lobster\lobster.sln</code> with Visual Studio, and
ensure <code>Release</code> mode is selected. The project is set up to
build lobster.exe in the <code>bin</code> folder, and will be ready for
use as described either from the <a
href="command_line_usage.html">command line</a> or <a
href="vscode_ide.html">VS Code</a> / <a
href="sublime_ide.html">SublimeText</a> / <a
href="notepadpp_ide.html">Notepad++</a>.</p>
<h3 id="os-x-ios">OS X (&amp; iOS)</h3>
<p>You need to first generate the Xcode project using CMake, run
<code>sh build_osx.sh</code> from the <code>dev</code> folder, to
generate an Xcode project in the <code>xcode-cmake</code>
sub-folder.</p>
<p>Open <code>dev/xcode-cmake/Lobster.xcodeproj</code>, ensure
<code>lobster &gt; My Mac</code> is selected as scheme in the top bar,
<code>Product -&gt; Build for -&gt; Profiling</code> (to get a Release
build), then close if no errors.</p>
<p>Alternatively from the terminal from the <code>xcode-cmake</code>
folder:</p>
<p><code>xcodebuild -toolchain clang -configuration Release -target lobster</code></p>
<p>This results in a <code>bin/lobster</code> you can use.</p>
<p>To develop Lobster code on OS X, use the command line version. Many
OS X editors support running a command line compiler, e.g. VSCode,
SublimeText, or Komodo Edit with Tools -&gt; Run Command.</p>
<p>How to turn a Lobster program into an App Bundle for distribution:
TBD Need to see how to set this up using CMake. You'll likely want to
produce a pak file (see <a href="command_line_usage.html">command
line</a>) to make sticking this extra data in a bundle easier.</p>
<p>For iOS be sure to read how to compile to C++ below, since iOS
doesn't support in Lobster's default JIT mode. How to make the above
CMake project work for iOS: TBD.</p>
<h3 id="linux">Linux</h3>
<p>You can build with CMake on Linux:</p>
<p>This requires a C++17 compiler, and the mesa dev files should be
installed (<code>apt-get install mesa-common-dev</code>).</p>
<pre><code>cd dev
cmake -DCMAKE_BUILD_TYPE=Release &amp;&amp; make -j8</code></pre>
<p>It creates <code>bin/lobster</code>. Run it to access the samples,
e.g. <code>bin/lobster samples/pythtree.lobster</code></p>
<p>Note the <code>LOBSTER_ENGINE</code> CMake option, which is by
default on. You can turn this off to get a command-line only version of
Lobster that does not depend on OpenGL, SDL, FreeType etc.</p>
<h3 id="android">Android</h3>
<p>Make sure you have the latest <a
href="https://developer.android.com/studio">Android Studio</a>
installed, and follow instructions to add the <a
href="https://developer.android.com/studio/projects/install-ndk.md">NDK</a></p>
<p>In Android Studio, use "Open" to open the
<code>dev/android-project</code> dir. It may complain about not knowing
where the NDK lives, either let it fix this automatically, or manually
modify the path in <code>local.properties</code></p>
<p>Using the desktop lobster exe, build your desired Lobster program
using the <code>--pak</code> option, such that all assets end up in a
single file (see below for more information). Place the result in
<code>dev/android-project/app/src/main/assets/default.lpak</code> so it
will automatically be picked up by the build process and added to the
APK. Also compile your Lobster code to C++ as described below.</p>
<p>You should now be able to just press run. Wait for the build, and see
it launch on an attached Android device. Note that Lobster requires a
device that supports GLES 3.0 and Android version 4.3 (Jellybean).
Emulators often do not support ES3, you'll see a shader compile error in
logcat if this happens.</p>
<p>If there are errors running, check logcat.</p>
<p>Things to change if you want to release your app in the Google Play
store (these instructions may be out of date):</p>
<ul>
<li><p>Generate your own signing key with <code>keytool</code>. Make
sure to also delete any old debug copy of the app from your device, or
you’ll get a signature mismatch error.</p></li>
<li><p>Change the name to something else in
<code>app/src/main/res/values/strings.xml</code>.</p></li>
<li><p>Change the .png files in <code>app/src/main/res/</code> with your
own application icon.</p></li>
<li><p>You may want to change the package name from
<code>org.libsdl.app</code> to your own. This needs to be done in 3
places, <code>app/build.gradle</code>, and
<code>app/src/main/java/org/libsdl/app/SDLActivity.java</code> (both at
the top of that file and the directory path itself!). Alternatively
create a new class and inherit from <code>SDLActivity</code>.</p></li>
</ul>
<h3 id="webassembly-emscripten">WebAssembly / Emscripten</h3>
<p>You need the <a
href="https://kripken.github.io/emscripten-site/docs/getting_started/downloads.html">Emscripten
toolchain</a> installed, as well as GNU make (on windows that means
installing <a
href="http://gnuwin32.sourceforge.net/packages/make.htm">this</a>).</p>
<p>Before you build, gather your lobster distribution files (see below)
and place them in <code>dev/emscripten/assets</code>. They will be
automatically picked up by the build process this way.</p>
<p>The Wasm implementation does not support the JIT, so you should first
compile your <code>.lobster</code> code to C++, as described in the
section "Compiling Lobster code to C++" below.</p>
<p>To build, go to <code>dev/emscripten</code>, and type
<code>make -j8</code>. This should produce a lobster.[wasm|js|html|data]
in the same directory (the latter containing whatever you placed in
<code>assets</code>).</p>
<p>You can now run it with
<code>emrun --browser chrome lobster.html --verbose</code> or if that
doesn't work, <code>emrun --no_browser lobster.html --verbose</code> and
manually navigate to
<code>http://localhost:6931/lobster.html?--verbose</code> in your
browser. Note that just loading up the html in your browser directly may
not work because of security restrictions. Alternatively place all the
generated files on a webserver, and load from there.</p>
<h2 id="distributing-lobster-programs.">Distributing Lobster
programs.</h2>
<p>While the above instructions will build you the lobster executable,
to distribute a Lobster program to others, you will need to distribution
files. These must be (including correct paths):</p>
<ul>
<li><p><code>default.lpak</code>. This is the Lobster pakfile file you
obtain from compiling your program with the <code>--pak</code> option,
it includes:</p>
<ul>
<li><p>The bytecode.</p></li>
<li><p><code>data/shaders/default.materials</code> (these are the
minimum shader definitions needed for to render anything, and is
implicitly loaded by <code>gl.window</code>).</p></li>
<li><p>Any other files/directories you have specified with
<code>pakfile</code>, e.g:
<code>gl.load_texture(pakfile ”mypath/myfile.png”)</code>.
<code>pakfile</code> can prefix filenames or directories (ending in
<code>/</code>), in which case all files in the directory will
(non-recursively) be added. You can specify a filter with
<code>#foo</code> at the end of a pakfile string which causes only
filenames that contain <code>foo</code> to be added. When running with
<code>--verbose</code> you can see what files are added/loaded from a
pakfile, and which are loaded individually.</p></li>
</ul></li>
<li><p>Any files your code references that are not in the pakfile (e.g.
<code>gl.load_texture(”mypath/myfile.png”)</code> ).</p></li>
<li><p>On Windows, you’ll need to include
<code>bin\openvr_api.dll</code> and/or <code>bin\steam_api.dll</code>
next to <code>lobster.exe</code> ONLY if you use functions starting with
<code>vr.</code> or <code>steam.</code> respectively.</p></li>
</ul>
<p>Where you place these files depends on the platform, on Windows /
Linux it is next to the lobster executable, on OS X / iOS it is the
application bundle under Contents, on Android it’s under assets in the
.apk, and with Emscripten there’s an assets directory also.</p>
<h2 id="compiling-lobster-code-to-c">Compiling Lobster code to C++</h2>
<p>Rather than directly executing with a JIT, Lobster can also be
translated to C++, for a further speed boost. This is useful when
releasing a shipping build to customers, but hopefully not necessary
during development. It is necessary for building for mobile/web
platforms.</p>
<p>With the <code>--cpp</code> option on the command-line, the compiler
will generate <code>dev/compiled_lobster/src/compiled_lobster.cpp</code>
(currently, you MUST compile it from the root of the repo, e.g.
<code>bin/lobster --cpp somepath/my.lobster</code>, otherwise this will
likely fail). This file contains a <code>main()</code> and is otherwise
self-contained such that when you compile it with the build files for
any platform (see instructions above) substituting it for the standard
<code>main.cpp</code>, you’ll end up with an executable that runs only
that specific program.</p>
<p>On Windows, there are project files in
<code>dev/compiled_lobster</code> that will automatically pick up the
compiled lobster code.</p>
<p>On Linux, building in <code>dev</code> like above, then instead
<code>cmake -DLOBSTER_TOCPP=ON -DCMAKE_BUILD_TYPE=Release .</code> will
automatically substitute the compiled lobster main program. Build with
<code>make -j8</code> or similar.</p>
<p>For Emscripten, there's a <code>cpp</code> make target (which is the
default).</p>
<h2 id="extending-lobster">Extending Lobster</h2>
<p>Besides using Lobster as a stand-alone programming language as-is,
there are 2 ways of extending Lobster, by adding your code to Lobster,
or adding Lobster to your project.</p>
<p>Note that unlike other scripting languages, Lobster has been designed
as a stand-alone language first, rather than a plug-in scripting system
(more like Python and Ruby, not like Lua and UnrealScript). You use
Lobster code as your "main program", with the "engine" being the library
you call into. Most game engines are the opposite: the engine code is
the main program, and the scripting language is being called into. For
that reason, adding your own code to Lobster is by the far the
preferable way of building an application that uses Lobster, and will
generally be a much more productive environment.</p>
<p>The thinking here is that you use C++ purely to write performance
critical code, which can usually be contained in libraries. For the
non-performance critical code, which includes the general setup of your
main program determining how things fit together, you are much better
off using a friendlier language, like Lobster. It means that changing
the structure of your project is much quicker, and it is easier to
experiment with new game ideas based on your C++ libraries. Iterations
in Lobster can be done more rapidly and more safely, often in less code,
than C++.</p>
<h3 id="adding-your-code-to-lobster">Adding your code to Lobster</h3>
<p>Depending on what you want to write, the current engine functionality
of Lobster may not be sufficient. Lobster adds C++ functions to the
language in a modular fashion, in the Visual Studio project you can see
all things added to Lobster in 2 places:</p>
<ul>
<li><p>The "builtins" folder, which should really be part of any Lobster
implementation. <code>buitins.cpp</code> is the most important one that
adds vector &amp; math operations etc., without which the language would
be hard to use. <code>file.cpp</code> adds file I/O related functions,
and <code>lobsterreader.cpp</code> allows you to parse data structures
in lobster syntax from a running program.</p></li>
<li><p>The engine folder. This contains all graphics/font/audio etc
functionality. <code>graphics.cpp</code> / <code>font.cpp</code> build
on top of the above mentioned 3 libraries, and can either be kept, or
replaced entirely by functions that use a different rendering system.
You can turn Lobster into a console-only language in one step by simply
removing the engine folder from the project.</p></li>
</ul>
<p>You can always run Lobster with the <code>--gen-builtins-html</code>
option to get an overview of all functions currently added to the system
(the current list is <a
href="builtin_functions_reference.html">here</a>). To add/remove
functionality is generally as easy as adding/removing the corresponding
<code>.cpp</code> file.</p>
<p>Lobster uses some macros to allow you to define a native function in
one location without declarations needed elsewhere. To learn how to
write your own .cpp of native functions, best to start with a simple
example, such as <code>audio.cpp</code>, then browse through more
complex examples in <code>builtin.cpp</code> and
<code>graphics.cpp</code>.</p>
<p>He
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
