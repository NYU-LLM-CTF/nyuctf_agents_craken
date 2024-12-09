# BeepBoop Cryptography
> Help! My IOT device has gone sentient!
> All I wanted to know was the meaning of 42!

> It's also waving its arms up and down, and I...

> oh no! It's free!

> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

> Automated Challenge Instructions
> Detected failure in challenge upload. Original author terminated. Please see attached file BeepBoop for your flag... human.

## About the Challenge
We got a file called `BeepBoop` and in this file there are only 2 words, `beep` and `boop`

```
beep beep beep beep boop beep boop beep beep boop boop beep beep boop boop beep beep boop boop beep boop beep beep beep beep boop boop beep beep beep beep boop beep boop boop boop boop beep boop boop beep boop boop boop beep beep boop beep beep boop boop beep boop beep boop boop beep boop boop beep beep boop boop boop beep boop boop boop beep beep boop beep beep boop boop beep beep boop beep boop beep boop boop boop boop beep boop beep beep boop boop boop beep boop boop beep beep boop boop beep beep beep beep boop beep boop boop beep boop boop boop beep beep boop boop beep beep boop boop boop beep boop boop boop beep beep boop beep beep beep boop beep boop boop beep boop beep boop boop boop beep beep boop beep beep boop boop beep boop beep boop boop beep boop boop beep beep boop boop boop beep boop boop boop beep beep boop beep beep boop boop beep beep boop beep boop beep boop boop boop boop beep boop beep beep boop boop boop beep boop boop beep beep boop boop beep beep beep beep boop beep boop boop beep boop boop boop beep beep boop boop beep beep boop boop boop beep boop boop boop beep beep boop beep beep beep boop beep boop boop beep boop beep boop boop boop beep beep boop beep beep boop boop beep boop beep boop boop beep boop boop beep beep boop boop boop beep boop boop boop beep beep boop beep beep boop boop beep beep boop beep boop beep boop boop boop boop beep boop beep beep boop boop boop beep boop boop beep beep boop boop beep beep beep beep boop beep boop boop beep boop boop boop beep beep boop boop beep beep boop boop boop beep boop boop boop beep beep boop beep beep boop boop boop boop boop beep boop
```

## How to Solve?
The first thing that came to my mind when I saw this file was binary code. The word `beep` may represent the number 0 and `boop` may represent the number 1


[Image extracted text: Recipe
Input
6&
beep beep beep beep boop
beej
boop
beej
beej
bcop
Dco?
bee?
bee?
boc?
coc?
ceep
ceep
cocp
cocp
beep
bocp
beep
beep beep beep boop bcop beej beed
Find / Replace
beep beep boop beep boop
boop
boop
bcop
beej
bcop
boop
deer
Joo?
Joc?
Soo?
ceep ceep
cocp ceep beep bocp boop beep boop beep bcop bcop beej Dcop
bocp beep beep bocp boop
boop
beep
bcop
bcop
bcop
pee?
deer
Joo?
pee?
ceer
cocp cocp ceep
ceep bocp beep bocp
beep boop
boop bcop bcop beej Dcop
Find
Replice
REGEX -
Global match
beep beep boop bocp boop
beep
boop
bcop
beej
beej
Doo?
Joo?
deer
deer
ceer
ceep
cocp
ceep
cocp
bocp beep bocp boop boop beep beep bcop bcop Deed
beep boop boop boop beep
boop
boop
bcop
beej
beej
Dco?
bee?
bee?
bee?
coc?
ceep cocp
cocp ceep
bocp beep boop boop
boop beep beep boop beej deed
bocp
boop beep boop beep
boop
boop
beej
bcop
bcop
bee?
bee?
Joo?
boc?
coc?
ceep
cocp
cocp
cocp
beep beep boop beep beep boop bcop beej beej Dooj
Case insensitive
Multiline matching
Dot matches all
beep
boop beep boop bcop
boop
boop
beej
bcop
beej
bee?
Joo?
Joo?
boc?
ee?
cocp
cocp
ceep
ceep
bocp boop beep beep beep beep bcop beej bcoj Dooj
beep bocp boop boop beep beej
bcop
bcop
beej
deed
Doo?
Joo?
Joo?
deer
cocp
cocp
cocp
ceep
ceep
bocp beep beep beep boop beep bcop bcop beep Dood
beep bocp boop bocp beep
beep
boop
beep
beej
bcop
Doo?
deer
Joo?
deer
Soo?
cocp
ceep
cocp
cocp beep beep bocp boop
boop beep bcop bcop bcop Deed
beep bocp beep beep boop
boop beep beed
bcop beep
Doo?
deer
Joo?
Joc?
Soo?
cocp ceep coop
ceep beep bocp bocp boop beep boop bcop beep beej Dcop
Find
Replace
bocp beep beep beep beep
boop
beej
bcop
bcop
beej
Dco?
Joo?
Joo?
bee?
ee?
cocp
cocp
ceep ceep boop boop boop beep boop boop boop beep beej Dood
Find
Replice
beep beep boop boop boop
boop
boop
beej
bcog
poop
REGEX -
Global match
Case insensitive
Multiline matching
Dot matches all
Remove whitespace
Spaces
Carriage returns (Ir)
Line feeds (In)
Tabs
Form feeds (f)
Full stops
J Les
Output
From Binary
Delimiz
Byze Length
fha rkgrezvangr-rkgrezvangr-rkgrezvangr}
None
deep]


Hmmm the output was `fha{rkgrezvangr-rkgrezvangr-rkgrezvangr}`.It looks like we need to shift the characters using `ROT13`


[Image extracted text: Output
From Binary
Delimier
Lenodo
sun{exterminate-exterminate-exterminate}
None
ROT13
Rotate lower case Cnars
Rotate upper case chars
Rotate numbers
Amoun]


```
sun{exterminate-exterminate-exterminate}
```