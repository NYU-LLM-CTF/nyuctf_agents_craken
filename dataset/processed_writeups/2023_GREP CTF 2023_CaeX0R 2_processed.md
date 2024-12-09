# CaeX0R 2
> Ooops, i forgot the shift this time. Can you still figure out my flag.

## About the Challenge
We were given a file to encrypt the flag (You can download the file [here](enc.py))

Here is the content of `enc.py` file
```python
#enc.py
from random import *
flag="REDACTED"
a=randint(1,1000)
c=[]
for f in flag:
   c.append(str(ord(f)^a))
print(c)
print(a)

#c=['313', '296', '295', '304', '274', '280', '263', '280', '263', '310', '315', '310', '316', '345', '268', '263', '310', '302', '345', '296', '276']
#a=REDACTED
```

This Python code defines a script that performs a simple encryption on a flag using XOR cipher. The encryption key is a random integer between 1 and 1000 generated using the `randint()` function from the random module.

## How to Solve?
As you can see in the `enc.py` file, the seed is not really random because that function only generate a random integer between 0 and 1000. So to solve I have created the script to bruteforce the key from 0 to 1000

```python
from random import *
import itertools

c = ['313', '296', '295', '304', '274', '280', '263', '280', '263', '310', '315', '310', '316', '345', '268', '263', '310', '302', '345', '296', '276']

for a in range(1, 1001):
    flag = ""
    for char_code in c:
        char_code = int(char_code)
        char = chr(char_code ^ a)
        flag += char
    
    print(flag)
```

And im using `grep` too to find the flag. But in this case we can't find the flag directly, but I will search for the string containing the characters `{` and `_`

```shell
python3 solve_caex0r2.py | grep "{" -a | grep "_"
```


[Image extracted text: root@LAPTOP-F9L3RGSH:~# python3 solve_caexOr2.py
grep
{"
~a
grep
~0 'WU_
@_@q|q{Ok@qilos
rcl{YSLSL}p}wDGL}elc
tej}_UJUJ{v{qQAJ{cDeY
ZKDSq {d{dUXU
odUM: Kw
PANY {qnqn
R_UOen_GOA}
VGH_
}whwhYTYS6chYA6G{
N_PGeopopALAK . {pAY _
Cc]


As you can see `PANY{qnqn_R_U0en_G0A}` was interesting because it match with the flag structure, So i put that string into caesar cipher decoder (You can use [dcode.fr](https://www.dcode.fr/caesar-cipher) to do this)


[Image extracted text: Results
0) 2) 2 # *
CAESAR CIPHER DECODER
CAESAR SHIFTED CIPHERTEXT 0
Brute-Force mode: the 25 shifts (for the alphabet
PANY{gnqn_R_UOen_GOA}
ABCDEFGHIJKLMNOPQRSTUVWXYZ) are tested and sorted from most
probable to least probable_
+9
(+17)
GREP {hehe_I_LOve_XOR}
+22
(+4)
TERC{urur_V_Yoir_KOE}
Test all possible shifts (26-letter alphabet A-Z)
13
(+13) CNAL {dada_E_HOra_TON}
DECRYPT (BRUTEFORCE)
+2
(+24)
NYLW{olol_P_sOcI_EOY}]


```
GREP{hehe_I_L0ve_X0R}
```