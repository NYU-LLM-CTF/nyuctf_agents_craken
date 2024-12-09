# Arctic Penguin
> I love penguins. They are so cute. One of my favourite penguin is missing. He was last seen under snow in north pole near arctic circle. There are news that he has been kidnapped by someone. Can you find him. Wait i've a picture, here you go. Please find him asap !

> PS. He likes buildings. A MAN trapped him in a building of SNOW.

## About the Challenge
We were given a file (You can download the file [here](pengu.jpg)) and we need to find the flag using that picture

## How to Solve?
To solve this, Im using `stegseek` first to extract hidden data from files by performing bruteforce attack. Here is the command to bruteforce the image using `rockyou.txt` wordlist

```shell
stegseek Missing.jpg /usr/share/wordlists/rockyou.txt
```


[Image extracted text: (kaliokali)-[~]
stegseek Desktop/pengu. jpg
StegSeek
0. 6
https
github.com/RickdeJager/StegSeek
Found passphrase:
ilovpenguin
[i]
Original filename
Burj
txt
[i]
Extracting
pengu. jpg
out
the
file
pengu. jpg
out
does already exist
overwrite
(y/n)]


We have a `txt` file now, but it contains only tabs and spaces. Afterwards, if we check the metadata of the picture


[Image extracted text: Resolution
Resolution
XMP
Toolkit
Image :: ExifTool
12.44
Creator
snowygraphy
Comment
send money
snowman
Image Width
1080
Image Height
1801
Encoding
Process
Baseline DCT , Huffman coding
Bits
per
Sample]


After searching about `Snow steganography`. Now im using stegsnow to get the flag, but we don't know the flag right? I came across this [tool](https://github.com/0xHasanM/SnowCracker) to brute stegsnow password. Here is the command I used to crack the password

```shell
python3 snowcracker.py -c Y -f /home/kali/pengu\ \(5\).jpg.out -w /usr/share/wordlists/rockyou.txt | grep _ -B 1
```

So I performed brute-force attack using `rockyou.txt` wordlist and then grep the string that contain character `_`


[Image extracted text: python3 snowcracker.py
Ihome/kali/pengu |
I(51). jpg
out
lusr/ share/wordlists/rockyou.txt
grep
Siiewa kieklk #i '
Password
abc123
Message
!uzl.eieaviw h 1
Password
diana
Message
Xfwsutbtiied?npa
Password
carmen
Message
to/
eg<feoeelsn
Password
scorpio
Message
foniaDii
eltaeilwg
Password
carter
Message
wInVeNklorotlenhe
Password
juliana
Message
gOap
hsgoosakaeaebnp
Password
juancarlos
Message
trteatiso
brhllonsiusd
Password
copper
Message
hiolals
1 B :sinyabt
Password
nissan
Message
iiyeaen eaoooed
lk-uan
Password
262626
Message
suintsea.
potarssr
Password
kendra
Message
gesbfs
:ogaots
Password
snowman
Message
Pnguln
on Burj]


```
GREP{snowman,P3ngu1n_on_Burj}
```