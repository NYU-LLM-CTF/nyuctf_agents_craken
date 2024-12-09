# Missing Kitty
> My kitty is missing. Can you find her ? Last seen saying meow meow under the blanket !!

## About the Challenge
We were given a file (You can download the file [here](Missing.jpg)) and we need to find the flag using that picture

## How to Solve?
To solve this, Im using `stegseek` first to extract hidden data from files by performing bruteforce attack. Here is the command to bruteforce the image using `rockyou.txt` wordlist

```shell
stegseek Missing.jpg /usr/share/wordlists/rockyou.txt
```


[Image extracted text: (kaliokali)-[~]
stegseek Desktop/Missing. jpg /usr/share/wordlists/rockyou
txt
StegSeek
0. 6
https
github.com/RickdeJager/StegSeek
[1]
Found passphrase:
kitty123
[i]
Original filename
secret
txt"
[i] Extracting
"Missing. jpg.out"
the file
'Missing. Jpg
out
does already exist _
overurite
(y/n)]


We got txt file. If we open the file, we got this message

```
Dk what's this, some kitten language

memmemmmmeemmememeemeemmmeemeemmmeemeeeemmemmmmmmeemeememeeeemmemmemmmmmmeememeemeememmemeeememmmeeememmmeeeemmemmemeemmmmmmememmmmmememmemmmeemmeememmemeemeeemmeemmmmemeemeemmmeemeemmmeeeemmemmemmmmmmeeeemmemeemeeeemeeemememmemmmmmmeemmeemmeemeeeemeeemememeemeeemmeemmemmmmemmmmmmeememmmmeemmememeeemmemmmemeeemmmemmmmmmemmemmemmemmmmmmeemmmmemeemeememmemmmmmmeemmemmmeemmememeemeemmmeememmemeemmeeemeememmmmeeememmmeemmememeemmemmmmemeeemmmmmememmmmmememmemememmmeemmmmemeememeemeemmememmemmmmmmeememmemeeememmmmemeemmmmemmmmmmeememmmmeemmememeeemmemmeemmememmemmeeemeeemmeemmemmmmmmeeeemmemeemeeeemeeemememeeemmemmmemmmmmmeemmeeemeememmemeemmeemmeeememmmmmmememmeemmeemmeemeemmmeemmmmemeemmeeemmemmmmmmmeeememmmemmmmmmeeeemeemememmeemeeemeeemmeemmeemmeemmeemeeememmmemeeeeemeemeemmmmeemmmemeeememmmeeememmmeemeemmmeemmemememeeeeemeememeemmeemmmemeeememmmeeememmmmeemmeemeemeeemmeeeeeme
```

Change the character `m` to 0 and character `e` to 1. And then decode the binary to obtain the flag


[Image extracted text: Recipe
Input
+
D9
memmemmmmeemmememeemeemmmeemeemmmeemeeeemmemmmmmmeemeememeeeemmemmemmmmmmeememeemeememmemeeememmme
Find
Replace
eememmmeeeemmemmemeemmmmmmememmmmmememmemmmeemmeememmemeemeeemmeemmmmemeemeemmmeemeemmmeeeemmemmem
mmmmmeeeemmemeemeeeemeeemememmemmmmmmeemmeemmeemeeeemeeemememeemeeemmeemmemmmmemmmmmmeememmmmeemme
Find
Replace
SIMPLE STRING
memeeemmemmmemeeemmmemmmmmmemmemmemmemmmmmmeemmmmemeemeememmemmmmmmeemmemmmeemmememeemeemmmeememme
meemmeeemeememmmmeeememmmeemmememeemmemmmmemeeemmmmmememmmmmememmemememmmeemmmmemeememeemeemmememm
emmmmmmeememmemeeememmmmemeemmmmemmmmmmeememmmmeemmememeeemmemmeemmememmemmeeemeeemmeemmemmmmmmeee
Global match
Case insensitive
emmemeemeeeemeeemememeeemmemmmemmmmmmeemmeeemeememmemeemmeemmeeememmmmmmememmeemmeemmeemeemmmeemmm
memeemmeeemmemmmmmmmeeememmmemmmmmmeeeemeemememmeemeeemeeemmeemmeemmeemmeemeeememmmemeeeeemeemeemm
mmeemmmemeeememmmeeememmmeemeemmmeemmemememeeeeemeememeemmeemmmemeeememmmeeememmmmeemmeemeemeeemme
Multiline
matching
Dot matches all
eeeeme
Find
Replace
Find
SIMPLE STRING
Replace
888
Raw Bytes
Output
0 0 @
5
Global match
Case insensitive
HHello my kitty,
Finally you found
her .
am
delighted_
Multiline
matching
Dot matches all
Take it,
here
s your gift
{Sw33t_llttle_kltt3n}
From Binary
Delimiter
Byte Length
Space
STEP
BAKEI
Auto Bake
111
3m5
Raw
Bytes
flag]


```
GREP{steghide,Sw33t_l1ttle_k1tt3n}
```