# zipper
> Stare into the zip and the zip stares back.

## About the Challenge
We were given a zip file that contains a lot of `txt` files


[Image extracted text: flag zip'
ZIP archive, unpacked
31,049 bytes
Name
Size
Packed
Type
Modified
CRC32
So
many flags
So
many
choices
File folder
Part
amateursCiF
'{ZlBP3d_
flag201.txt
Text Document
7/16/2023 8.39
F36DF199
flagO.txt
Text Document
7/16/2023 8.39
EZ6D2FEE
flag1.txt
:
Text Document
7/16/2023 8.39
4BEEE438
flag2.txt
Text Document
7/16/2023 8.39
669C11C5
flag3.txt
25
Text Document
7/16/2023 8.39
644C3BDC
flag4.txt
16
Text Document
7/16/2023 8.39 _
1E20828F
flag5.txt
Text Document
7/16/2023 8.39 _
C1029F83
flag6.txt
Text Document
7/16/2023 8.39
4AZIFFO2
flag7 txt
40
Text Document
7/16/2023 8.39
852FFA13
flag8.txt
Text Document
7/16/2023 8.39
50B8D32C
flag9.txt
48
Text Document
7/16/2023 8.39
B1BZDZFD
1O.txt
Text Document
7/16/2023 8.39
36ECZEZF
flag11.txt
Text Document
7/16/2023 8.39
6BF863DD
flag12.txt
Text Document
7/16/2023 8.39
EABC62DD
flag13.txt
Text Document
7/16/2023 8.39
SA16EBD3
flag14.txt
Text Document
7/16/2023 8.39
6443F46F
flag15.txt
Text Document
7/16/2023 8.39
2D63B0B1
flag16.txt
Text Document
7/16/2023 8.39
B457C4F0
flag17.txt
Text Document
7/16/2023 8.39
D8CIEIF2
18.txt
Text Document
7/16/2023 8.39
AOAEEADE
flag19.txt
Text Document
7/16/2023 8.39
DA3D8104
flag2O.txt
26
Text Document
7/16/2023 8.39 _
CEIEZEBE
flag21.txt
47
Text Document
7/16/2023 8.39
EF3C3922
flag22.txt
Text Document
7/16/2023 8.39
75ECSBZF
flag23.txt
Text Document
7/16/2023 8.39
FDIOOEDA
flag24.txt
Text Document
7/16/2023 8.39
94B42C25
flag25.txt
20
Text Document
7/16/2023 8.39
54740887
flag26.txt
Text Document
7/16/2023 8.39
6FB3D937
flag27.txt
49
Text Document
7/16/2023 8.39
870F6COD
flag28.txt
Text Document
7/16/2023 8.39
5B344126
flag29.txt
Text Document
7/16/2023 8.39
0C636B12
Selected
file; 14 bytes
Total 1035 files, 31,032 bytes
flag
size
flag"
flag"]


## How to Solve?
First, you can get the first part by using `exiftool` and then check `comment` metadata


[Image extracted text: daffainfo@dapos:
$
exiftool
zip
ExifTool Version
Number
12.40
File
Name
zip
Directory
File
Size
142
KiB
File
Modification
Date/Time
2023:07:16 22:43:38+07:00
File Access
Date/Time
2023:07:20
06:29:17+07:00
File
Inode Change
Date/Time
2023:07:20 06:29:17+07:00
File
Permissions
~rw-r-
Comment
So
many flags .
So many choices _
Part
1:
amateursCTF {zlPP3d_
flag
flag .]


```
Part 1: amateursCTF{z1PP3d_
```

And then to obtain the second part, we need to check the information about the `zip` file first by using `zipinfo` command


[Image extracted text: daffainfo@dapOS:~$ zipinfo flag.zip
Archive:
zip
Zip file
size
144920 bytes
number f entries:
1037
drwxrwxrwx
2
unx
b-
stor 80-Jan-01
00:00 flag/
?rW-
unx
14 b-
defN 23-Jul-16
08:39 flag/flag201.txt
drwxrwxr-X
unx
17
b-
defN 23-Jul-16
08:39 flag/
?rW-
unx
47
b-
defN 23-Jul-16 08:39 flag/flago.txt
flag]


Why are there two directories with the same name, and why does the second one have 17 bytes in it? If you unzip it manually, one of the directories will be overwritten; that's why we need to extract it differently.

To extract the flag, I created a python program to extract the file using a `file_` as a prefix

```python
import zipfile
z = zipfile.ZipFile('flag.zip')
for i, f in enumerate(z.filelist):
    f.filename = 'file_{0:03}'.format(i)
    z.extract(f)
```

And then use `strings` and `grep` to find the second part


[Image extracted text: daffainfo@dapos
/forensic$ strings
grep
"Part
2"
Part
2:
inSid3_4_
daffainfo@dapOs:
[forensic$]


```
Part 2: in5id3_4_
```

For the third part, you can use `exiftool` again and find `Zip File Comment` metadata


[Image extracted text: LIP
Cf
OAJJJJJJJ]
Compressed
Size
Uncompressed
Size
Zip File
Name
flag/
Zip File Comment
Part
3:
laY3r_Of
Warning
[minor]
Use the Duplicates option
to extract
Zip
Zip]


And for the last part, when you unzip the file you will notice there is a file with the same name


[Image extracted text: flag199.txt
Text Document
7/16/2023 8.39
77087541
flag2O0.txt
32
Text Document
7/16/2023 8.39
28E4D78F
flag201.txt
16   Text Document
7/16/2023 8.39
F36DF19g
flag201.txt
Text Document
7/16/2023 8.39
EZEB28ZE
flaa202.txt
Text Document
7/16/2023 839
8F48D9F7]


Open it and you will obtain the flag


[Image extracted text: flag201.txt
File
Edit
View
Part
4:
_Zips}]


```
amateursCTF{z1PP3d_in5id3_4_laY3r_0f_Zips}
```