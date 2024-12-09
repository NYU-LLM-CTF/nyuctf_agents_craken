# ECC not only for Dummies
> This time you will need to use all logic that you have

## About the Challenge
We were given a server to connect and also the source code. So we can input 8 questions and we need to guess the cards too (You can download the source code [here](ecc_not_only_for_dummies.zip))


[Image extracted text: Hello
there
Would
you
like
to play
a little game?
have
written
values
(yes
no)
on
cards
am curious
if
you
are
able to
guess
which
values
are
You
can
ask
me
logic questions
know you
re smart ,
50
won
Lways be
honest
about
the
answers
No worries
will fool
you only
times
0 . Question:
test
Question
resolves
to:
True
1.Question:
test
Question
resolves
to:
True
2.Question:
test
Question
resolves
to:
False
3.Question:
test
Question
resolves
to:
True
4.Question:
test
Question
resolves
to:
True
5.Question:
test
Question
resolves
to:
True
6.Question:
test
Question
resolves
to:
False
7.Question:
test
Question
resolves
to:
True
You have
used
all
the questions
Now tell
me
one
by
one
what
have
written
down
on
the cards
Your response
test
Your
answer
did
not
include
all
the
cards
they]


## How to Solve?
To solve this chall, im using PyJail payload and I inputted it when the bot asked us to input the question

```
breakpoint()
```

After enterring Python debugger, run this command to obtain the flag

```
open("/jailed/flag.txt").read()
```


[Image extracted text: 0.Question: breakpoint()
~Return--
<string-(1)<module>()->None
(Pdb) open(" / jailed/flag
txt").read()
justcTF{SUnd_SOmetim3s_It$_EvEn_fOlvuble}
(Pdb)
Time
limit exceeded _
Try
again!]


```
justCTF{S4nd_S0metim3s_It$_EvEn_$0lv4ble}
```