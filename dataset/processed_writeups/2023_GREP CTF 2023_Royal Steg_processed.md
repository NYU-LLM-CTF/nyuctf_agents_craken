# Royal Steg
> Then Jesus turned, and seeing them following, said to them, 'what do you SEEK?

> - JOHN 1:38

## About the Challenge
We were given a file (You can download the file [here](steg.jpg)) and we need to find the flag using that picture

## How to Solve?
To solve this, Im using `stegseek` first to extract hidden data from files by performing bruteforce attack. Here is the command to bruteforce the image using `rockyou.txt` wordlist

```shell
stegseek steg.jpg /usr/share/wordlists/rockyou.txt
```


[Image extracted text: kaligkali)-[~/Desktop]
stegseek steg-jpg
lusr/share_
/wordlists/rockyou.txt
StegSeek
0.6
https: //github
com/RickdeJager/StegSeek
[i]
Found
passphrase:
cuteessort37"
[i] Original filename
'orig.zip"
[i] Extracting
to
'steg. jpg
out
the file
jpg
out
does
already exist.
overwrite
(y/n)
'steg]


We got password-protected zip file. Now we need to crack the zip password to obtain the flag by using `JohnTheRipper`. Here is the command I used

```shell
zip2john steg.jpg.out > hash_steg.txt
john -w=/usr/share/wordlists/rockyou.txt hash_steg.txt
john --show hash_steg.txt
```

The `zip2john` tool is used to extract the password hash from a password-protected ZIP file, and the next step is to crack the password hash contained in the `hash_steg.txt` file using the `rockyou.txt` wordlist.


[Image extracted text: kaligkali)-[~/Desktop]
zip2john
out
hash_steg txt
ver
1.0
efh 5455
efh 7875
out/flag txt PKZIP Encr:
2b
chk, TS
chk,
cmplen-39, decmpl
en-27
crc-OEA4D68A ts-6ESC
cs-6e5c type-0
kaligkali)-[~/Desktop]
john
~W-/usr/share/wordlists/rockyou.txt
hash_steg.txt
default
input encoding
UTF-8
Loaded
password hash (PKZIP [32/64])
No password
hashes left
to
crack
(see FAQ)
kaligkali)-[~/Desktop]
john
show hash_steg_
txt
steg: jpg out/flag_
txt: Jesuslove:
txt:steg. jpg
out :
steg.jpg
out
password hash cracked,
0 left
jpg_
steg
steg
jpg _
Using
flag]


Open the password-protected zip file using `jesuslove` as the password and you will obtain the flag


[Image extracted text: File
Edit
Selection
View
Go
Run
Terminal
Help
Restricted Mode
intended for safe code browsing: Trust this windov
= flag txt
home
kali
fr-NKr76u
= flag txt
grepCTF{two_13v3ls_Of_stzg}
~cache]


```
grepCTF{tw0_l3v3ls_0f_st3g}
```