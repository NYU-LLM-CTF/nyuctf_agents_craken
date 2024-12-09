# Mascot
> Very gracious host!!

## About the Challenge
We were given a website where we can play tic-tac-toe games.


[Image extracted text: ]


## How to Solve?
When I want to check the source code, trying to win the game. The result is nothing. And then I decided to test some interesting endpoint like `.git` or `robots.txt`. And then there is `.git` folder exposed.


[Image extracted text: Index of / git
ch54906117587.cheng run/.git/
Getting Started
#519502 Name Link B_
#927384 Race Conditi_.
#502758 RCE and Co_
Exploit Datz
Index of /.git
Name
Last modified
Size Description
Parent Directory
HEAD
2023-04-01 05.30
21
branches/
2023-04-01 05.30
config
2023-04-01 05.30
270
description
2023-04-01 05.30
73
hooks/
2023-04-01 05.30
index
2023-04-01 05.30 [.6K
(infol
2023-04-01 05.30
Jegs
2023-04-01 05.30
objectsz
2023-04-01 05.30
packed-refs
2023-04-01 05.30
112
refst
2023-04-01 05.30
Apache/2.4.52 (Ubuntu) Server at ch54906117587.cheng run Port 80]


After checking the `config` file, we will see a GitHub repository.


[Image extracted text: ch54906117587.ch.eng run/ git/conf X
ch54906117587.cheng run/.git/config
Getting Started
#519502 Name Link B.
#927384 Race Conditi__
#502758 RCE and Co_
[core]
repositoryformatversion
filemode
true
bare
false
logallrefupdates
true
[remote
origin" ]
url
https://github
com/kaustubhbhule/ lemons
popsicles
fetch
trefs/heads/* refs/remoteslorigin/*
[branch
main"]
remote
origin
merge
refs/heads/main]


Check the repository, we will see a file called `FLAGGGGG.md`. Open that file to obtain the flag


[Image extracted text: kaustubhbhule Create FLAGGGGG.n
boxicons
FLAGGGGG.md
indexhtml
scriptjs
stylecss]



[Image extracted text: main
lemons-popsicles
FLAGGGGG.md
kaustubhbhule Create FLAGGGGGmd
8?
contributor
lines (1 sloc)
26 Bytes
VishwaCTF{OctOc@t_MaScOt}]


```
VishwaCTF{0ctOc@t_Ma5c0t}
```