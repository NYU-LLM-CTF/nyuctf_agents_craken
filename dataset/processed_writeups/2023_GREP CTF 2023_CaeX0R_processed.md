# CaeX0R
> I pressed shift key 10 times and lost the flag. Can you find my flag.

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

#c=['162', '177', '188', '169', '136', '187', '138', '145', '172', '187', '138', '145', '172', '190', '152', '156', '187', '195', '177', '142']
#a=REDACTED
```

This Python code defines a script that performs a simple encryption on a flag using XOR cipher. The encryption key is a random integer between 1 and 1000 generated using the `randint()` function from the random module.

## How to Solve?
As you can see in the `enc.py` file, the seed is not really random because that function only generate a random integer between 0 and 1000. So to solve I have created the script to bruteforce the key from 0 to 1000

```python
c=['162', '177', '188', '169', '136', '187', '138', '145', '172', '187', '138', '145', '172', '190', '152', '156', '187', '195', '177', '142']

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
python3 solve_caex0r.py | grep "{" -a | grep "_"
```


[Image extracted text: root@LAPTOP-FIL3RGSH
~#
python3 solve_caexOr. py
grep "{"
~a
grep
ev{nO]MVk [MVky_[ IOvI
ufk~_l]F{l]F{iOKlOfY
AR_JkXirOXiro] {X
Rm
QBOZ {Hyb_Hyb_MkoHOB}]


As you can see the last result was interesting, So i put that string into caesar cipher decoder (You can use [dcode.fr](https://www.dcode.fr/caesar-cipher) to do this)


[Image extracted text: Search for a tool
SEARCH
TOOL ON DCODE BY KEYWORDS:
g. type 'sudoku'
BROWSE THE FEULL DCODE TOOLS' LIST
Results
CAESAR CIPHER DECODER
CAESAR SHIFTED CIPHERTEXT @
Brute-Force mode: the 25 shifts (for the alphabet
QBOZ {Hyb_Hyb_MkoHOB}
ABCDEFGHIJKLMNOPQRSTUVWXYZ
are tested and sorted from most
probable
east probable_
+23
(+3)
TERC {Kbe_Kbe_PnrKOE}
+14
(+12) CNAL {Tkn_Tkn_YwaTON}
Test all possible shifts (26-letter alphabet A-Z)
+19
(+7)
XIVG{Ofi_ofi_TrvooI}
DECRYPT (BRUTEFORCE)
+16
(+10) ALYJ{Ril_Ril_WuyROL}
~7
+19)
JUHS{Aru_Aru_FdhAOU}
MANUAL DECRYPTION
AND PARAMETERS
+13
(+13) DOBM{Ulo_Ulo_Zxbuoo}
SHIFT /KEY (NUMBER):
+10
(+16) GREP {Xor_Xor_CaeXOR}
USE THE ENGLISH ALPHABET (26 LETTERS FROM A To Z)
+20
(+6)
WHUF {Neh_Neh_SquNOH}
USE THE ENGLISH ALPHABET AND ALSO SHIFT THE DIGITS 0-9
USE THE LATIN ALPHABET IN THE TIME OF CAESAR (23 LETTERS;
NO J, U OR W)
+3
(+23)
NYLW{Evy_Evy_JhIEOY}
USE THE ASCII TABLE (0-127) As ALPHABET
+1
(+25)
PANY {Gxa_Gxa_LjnGOA}]


```
GREP{Xor_Xor_CaeX0R}
```