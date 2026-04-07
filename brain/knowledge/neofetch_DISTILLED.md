---
id: neofetch
type: knowledge
owner: OA_Triage
---
# neofetch
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h3 align="center"><img src="https://i.imgur.com/ZQI2EYz.png" alt="logo" height="100px"></h3>
<p align="center">A command-line system information tool written in bash 3.2+</p>

<p align="center">
<a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
<a href="https://github.com/dylanaraps/neofetch/releases"><img src="https://img.shields.io/github/release/dylanaraps/neofetch.svg"></a>
<a href="https://repology.org/metapackage/neofetch"><img src="https://repology.org/badge/tiny-repos/neofetch.svg" alt="Packaging status"></a>
</p>

<img src="https://i.imgur.com/GFmC5Ad.png" alt="neofetch" align="right" height="240px">

Neofetch is a command-line system information tool written in `bash 3.2+`. Neofetch displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.

The overall purpose of Neofetch is to be used in screen-shots of your system. Neofetch shows the information other people want to see. There are other tools available for proper system statistic/diagnostics.

The information by default is displayed alongside your operating system's logo. You can further configure Neofetch to instead use an image, a custom ASCII file, your wallpaper or nothing at all.

<img src="https://i.imgur.com/lUrkQBN.png" alt="neofetch" align="right" height="240px">

You can further configure Neofetch to display exactly what you want it to. Through the use of command-line flags and the configuration file you can change existing information outputs or add your own custom ones.

Neofetch supports almost 150 different operating systems. From Linux to Windows, all the way to more obscure operating systems like Minix, AIX and Haiku. If your favourite operating system is unsupported: Open up an issue and support will be added.


### More: \[[Dependencies](https://github.com/dylanaraps/neofetch/wiki/Dependencies)\] \[[Installation](https://github.com/dylanaraps/neofetch/wiki/Installation)\] \[[Wiki](https://github.com/dylanaraps/neofetch/wiki)\]

```

### File: CONTRIBUTING.md
```md
# How to Contribute

<!-- vim-markdown-toc GFM -->

* [Coding Conventions](#coding-conventions)
    * [ShellCheck](#shellcheck)
    * [No no's](#no-nos)
    * [If Statements](#if-statements)
    * [Case Statements](#case-statements)
* [Making changes to Neofetch](#making-changes-to-neofetch)
    * [Adding support for a new Operating System / Distribution.](#adding-support-for-a-new-operating-system--distribution)

<!-- vim-markdown-toc -->


## Coding Conventions

- Use `bash` built-ins wherever possible.
- Try not to pipe (`|`) at all.
- Limit usage of external commands `$(cmd)`.
- Indent 4 spaces.
- Use [snake_case](https://en.wikipedia.org/wiki/Snake_case) for function
  and variable names.
- Keep lines below `100` characters long.
- Use `[[ ]]` for tests.
- Quote **EVERYTHING**.

### ShellCheck

For your contribution to be accepted, your changes need to pass
ShellCheck.

```sh
shellcheck neofetch
```

**Note**: If you have trouble installing ShellCheck. You can open a pull
request on the repo and our Travis.ci hook will run ShellCheck for you.


### No no's

- Don’t use GNU conventions in commands.
    - Use POSIX arguments and flags.
- Don’t use `cut`.
    - Use `bash`'s built-in [parameter expansion](http://wiki.bash-hackers.org/syntax/pe).
- Don’t use `echo`.
    - Use `printf "%s\n"`
- Don’t use `bc`.
- Don’t use `sed`.
    - Use `bash`'s built-in [parameter expansion](http://wiki.bash-hackers.org/syntax/pe).
- Don’t use `cat`.
    - Use `bash`'s built-in syntax (`file="$(< /path/to/file.txt)")`).
- Don’t use `grep "pattern" | awk '{ printf }'`.
    - Use `awk '/pattern/ { printf }'`
- Don’t use `wc`.
    - Use `${#var}` or `${#arr[@]}`.


### If Statements

If the test only has one command inside of it; use the compact test
syntax. Otherwise the normal `if`/`fi` is just fine.

```sh
# Bad
if [[ "$var" ]]; then
    printf "%s\n" "$var"
fi

# Good
[[ "$var" ]] && printf "%s\n" "$var"

# Also good (Use this for longer lines).
[[ "$var" ]] && \
    printf "%s\n" "$var"
```


### Case Statements

Case statements need to be formatted in a specific way.

```sh
# Good example (Notice the indentation).
case "$var" in
    1)  printf "%s\n" 1 ;;
    2)
        printf "%s\n" "1"
        printf "%s\n" "2"
    ;;

    *)
        printf "%s\n" "1"
        printf "%s\n" "2"
        printf "%s\n" "3"
    ;;
esac
```

## Making changes to Neofetch

### Adding support for a new Operating System / Distribution.

Adding support for a new OS/Distro requires adding the Name, Logo and
Colors of the OS/Distro to the `get_distro_ascii()` function.

The function is located right at the bottom of the script, one function
above `main()`. Inside this function you’ll find an alphabetical list of
each OS/Distro.

Find the spot in the list your new OS/Distro fits into and start
implementing your changes.

If your OS/Distro requires changes to the actual information gathering
functions then you can make these changes in the `get_*` functions.

**Syntax**:

- You have to escape back-slashes (`\`). (eg `\\`)
- You can use `${c1}` to `${c6}`to color the ascii.
    - These are evaluated *after* we read the file.


**Example**:

```sh
        "CRUX"*)
            set_colors 4 5 7 6
            read -rd '' ascii_data <<'EOF'
${c1}         odddd
      oddxkkkxxdoo
     ddcoddxxxdoool
     xdclodod  olol
     xoc  xdd  olol
     xdc  ${c2}k00${c1}Okdlol
     xxd${c2}kOKKKOkd${c1}ldd
     xdco${c2}xOkdlo${c1}dldd
     ddc:cl${c2}lll${c1}oooodo
   odxxdd${c3}xkO000kx${c1}ooxdo
  oxdd${c3}x0NMMMMMMWW0od${c1}kkxo
 oooxd${c3}0WMMMMMMMMMW0o${c1}dxkx
docldkXW${c3}MMMMMMMWWN${c1}Odolco
xx${c2}dx${c1}kxxOKN${c3}WMMWN${c1}0xdoxo::c
${c2}xOkkO${c1}0oo${c3}odOW${c2}WW${c1}XkdodOxc:l
${c2}dkkkxkkk${c3}OKX${c2}NNNX0Oxx${c1}xc:cd
${c2} odxxdx${c3}xllod${c2}ddooxx${c1}dc:ldo
${c2}   lodd${c1}dolccc${c2}ccox${c1}xoloo
EOF
        ;;
```

```

### File: LICENSE.md
```md
The MIT License (MIT)

Copyright (c) 2015-2021 Dylan Araps

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

### File: .github\ISSUE_TEMPLATE.md
```md
## Description

If you're suggesting a new feature then just a description will suffice.

- [ ] Does this issue still occur in the master branch? (**Required if issue**)


#### Neofetch version

## Screenshot

## Config file

## Verbose log

1. Run `neofetch -vv 2> neofetchlog`
2. Upload the contents of `neofetchlog` to pastebin, gist or equivalent.




```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## Description

Only fill in the fields below if relevant.


## Features

## Issues

## TODO

```

