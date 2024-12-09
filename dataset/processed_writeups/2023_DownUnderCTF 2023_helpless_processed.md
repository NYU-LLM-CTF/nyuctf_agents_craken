# helpless
> I accidentally set my system shell to the Python help() function! Help!!

> The flag is at /home/ductf/flag.txt.

> The password for the ductf user is ductf.

## About the Challenge
We are given an SSH server, and when we log in, we are immediately in the Python help() function.


[Image extracted text: daffainfo@dapos:
$
ssh ductf@2023
ductf
dev ~p30022
ductf@2023.ductf
dev
password:
The
programs
included with the
Ubuntu system
are free software;
the
exact
distribution
terms
for
each
program
are
described
in
the
individual files
in /usr/share/doc/*/copyright
Ubuntu
comes with
ABSOLUTELY
NO WARRANTY ,
to the
extent
permitted by
applicable
Law
The
programs
included with the
Ubuntu system
are free software;
the
exact
distribution
terms
for
each
program
are
described
in
the
individual files
in
lusr/share_
doc/*/copyright_
Ubuntu
comes with
ABSOLUTELY
NO
WARRANTY ,
to the extent permitted by
applicable
Law
Last login:
Sun Sep
13:29:54
2023
from
10.152.0.17
Welcome
to
Python
3.10' s help utility!
If
this
is
your
first time using Python 
you should definitely
check
out
the
tutorial
on
the internet
at
https: //docs.python .
10/tutorial/
org/3 .]


## How to Solve?
At first, I tried to spawn a shell using `+` followed by `!sh`, but it didn't work.


[Image extracted text: "x[index]
"x[index: index]
"x(arguments
X.attri
'await
X"
+X
~XI
shl]


And then i checked every command in `help()` function and I found there is `:e` command where we can examine a file


[Image extracted text: "+x"
"_X"
~X"
Examine
/home/ductf/flag.txtl]



[Image extracted text: daffainfo@dapos:
DUCTF {sometimes_less_is_more}]


```
DUCTF{sometimes_less_is_more}
```