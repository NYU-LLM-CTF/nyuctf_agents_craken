# Employee Evaluation
> This company sucks. They're ranking all the employees against one another, and they keep putting security to the sideline. The CISO told me that they don't care about actual code quality, just fancy buzzwords and looking nice. I want to get out of here, but I can't without this dang secret code. It's for, uh, good things, and not sharing secrets. This exposed evaluation script seems like a good start. Can you help me out?

## About the Challenge
We got a server to connect, here is a preview of the challenge


[Image extracted text: *-**
*-**
SwampCo
Employee
Evaluation Scriptm
Using
new ,
robust,
and blazingly
fast
BASH workflow ,
lookup
of
your
best
employee
score
is
easier
than
ever--all
from
the
safe
comfort
of
familiar
shell
environment
*-***
*-*
*-*
*-**
*-**
To
start,
enter
the
employee
name
test
Employee
not
found
Please consult your records .]


The first thing that comes to my mind is `bash jail`

## How to Solve?
At first I tried to use `ls` payload and here was the result


[Image extracted text: *-*****
*-*******
SwampCo
Employee
Evaluation Scriptm
Using
new ,
robust,
and blazingly
fast
BASH workflow ,
lookup
of
your
best employee
score
is
easier
than
ever--all
from
the
safe
comfort
of
familiar
shell environment
*-**
*-*
*-*
*-**
*-*
*-*
To
start,
enter
the
employee ' $
name
sh
Iapplrun:
line
44:
S{employee_
sh `_score}:
bad
substitution]


It looks like we need to close the curly brackets first and then execute an OS command. In this case, the flag was located in env variables


[Image extracted text: SwampCo
Employee
Evaluation Scriptm
Using
new ,
robust,
and blazingly
fast
BASH workflow ,
lookup
of
best
employee
score
is easier
than
ever--all
from
the
safe
comfort
of
familiar
shell
environment
To
start,
enter
the
employee "
name
} `printenv
{
Employee
} ` printenv
{
score:
}employee_james_score-16
employee_ethan_score-56
employee_vic_score-81
PWD-/app
employee_alex_score-00
emp
loyee_cole_score-57
employee_phoenix_score-89
employee_
omar_
score-74
emp
loyee_adam_score-84
employee_jon_score-41
SHLVL-0
employee_daniel_score-48
employee_john_score-19
employee_wilson_score-61
employee_jack_score-80
secret_
never_reveal_pls_thx_
FswampCTF {eval_clt_prOc_3nvirOn_2942}
employee_scott_score-94
employee_ben_score-47
usr/bin/printenv{_score
your]


```
swampCTF{eva1_c4t_pr0c_3nvir0n_2942}
```