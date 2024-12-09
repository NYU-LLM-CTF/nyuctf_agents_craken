# snowy rock
> am loves puzzles and his dad working in alaska sent a message hidden within for him to uncover
Can you decode it?

## About the Challenge
We got an image and we need to find the flag there (You can download the flag [here](snowy_rock_fi.jpg))

## How to Solve?
First, we need to use `binwalk` to extract the zip file from the image

```bash
binwalk -e snowy_rock_fi.jpg
```


[Image extracted text: DECIMAL
HEXADECIMAL
DESCRIPTION
Oxo
JPEG image data,
JFIF
standard
1.01
13250
0x33C2
TIFF image data,
big-endian ,
offset
of
first image directory:
28624
Ox6FDO
Copyright string:
"Copyright (c)
1998 Hewlett-Packard Company
WARNING
Extractor
execute
failed
to
run
external
extractor
jar Xvf
%e
[Errno
2]
No such file
or
director
y
jar
jar Xvf
%e
might
not
be
installed
correctly
248341
Ox3CA15
Zip
archive data, encrypted
at
least
v2.0
to
extract
compressed Size:
1037 ,
unc
ompressed
size
2289
name
snowyrock.txt
249548
Ox3CECC
End
of
archive ,
footer
length:
22
Zip]


You will see an error but that's okay, that happen because of the zip file was a password-protected file. And then we need to bruteforce the password of the zip file using `john`

```bash
zip2john file.zip > hash.txt
john -w=/usr/share/wordlists/rockyou.txt hash.txt
```


[Image extracted text: default
input encoding:
UTF-8
Loaded
password hash
(PKZIP [32/64])
Mill
run
OpenMP
threads
Press
Ctrl-C
to abort, almost
any
other
for status
llsnoubird
(3CA1S.Zip/snowyrock.txt)
1g 0:00:00:01
DONE
(2023-08-06
06:42 )
0.6666g/5
8918Kp/5
8918Kc/5
8918KC/5
1202822149
1lppt068955
Use
the
show"
option
display all
the cracked passwords reliably
Session completed.
Using
key]


As you can see, the password is `11snowbird`. Extract the file and you will got `snowyrock.txt`. Now, because of the title of the chall and also the `snowyrock.txt` content, I decided to use `stegsnow` to retrieve hidden messages in `snowyrock.txt`

```
stegsnow -C snowyrock.txt
```

This command will run `stegsnow` without using a password


[Image extracted text: (kaliokali)-[~]
stegsnow
Desktop/ snowyrock.txt
OFTHA62GMFBGUX3FIJYFQZSZONBGKX3FGMZHS7I=]


Decode the output using `base64` and also `rot13`


[Image extracted text: Recipe
Input
OFTHA6ZGMFBGUX3FIJYFQZSZONBGKX3FGMZHS7IA
From Base32
Alphabet
A-Z2-7=
Remove non-alphabet chars
ROT13
Rotate lower case chars
Rotate upper case chars
Amount
Rotate numbers
13
Output
dsc{SnOw_rocKs_for_r341}]


```
dsc{SnOw_rOcKs_fOr_r34l}
```