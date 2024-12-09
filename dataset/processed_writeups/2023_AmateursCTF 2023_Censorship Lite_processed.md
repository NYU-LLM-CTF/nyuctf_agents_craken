# Censorship Lite
> There was clearly not enough censorship last time. This time it's lite:tm:. I'm afraid now you'll never get in to my system! Unfortunate for those pesky CTFers. Better social engineer an admin for the flag!!!!

## About the Challenge
We got a python script called `main.py`. Here is the content of `main.py`

```python
#!/usr/local/bin/python
from flag import flag

for _ in [flag]:
    while True:
        try:
            code = ascii(input("Give code: "))
            if any([i in code for i in "\lite0123456789"]):
                raise ValueError("invalid input")
            exec(eval(code))
        except Exception as err:
            print(err)
```

So, this script will execute our input, but we can't input `\`, `l`, `i`, `t`, `e`, and also a numbers (0-9). We cannot use unicode character because of `ascii()`

## How to Solve?
To solve this problem, we don't need to execute an OS command. But how? As you can see the package `flag` was already imported into the code and also the value of flag was assigned to `_` variable.

```python
from flag import flag

for _ in [flag]:
    ...
```

Do you know there is a built-in function called `vars()`? This function returns a dictionary of an object. For example:


[Image extracted text: Python
10.6 (main,
29
2023_
11.10
38)
[GCC
11.3.0]
on
linux
Type "help"
"copyright
"credits
or
"license"
for
more
information .
>>>
var
"test
>>>
vars()
{
__name_
~_main__
doc_
None
~_package__
None
loader_
<class
frozen_importlib.Builtin
Importer
~_spec
None
annotations__
{} ,
builtins_
<module
builtins
(built-in)>,
var
t
est
}
May]


So, to print the value of variable `flag` or `_`, we can use this payload

```python
vars()[flag]
vars()[_]
```

Because we can't input character `l` in the program, we can only use the second payload


[Image extracted text: daffainfoddapos
$
nc
amt
rs
31671
Give code:
varsO)[_]
'amateursCTF {shOuld' v3_r3strict3D_plr3nTh3ticaLs_Inst3aD}
Give code:]


```
amateursCTF{sh0uld'v3_r3strict3D_p4r3nTh3ticaLs_1nst3aD}
```