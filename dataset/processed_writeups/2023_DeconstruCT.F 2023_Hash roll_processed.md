# Hash roll
> Augustine's friend took a important file of augustine and stashed it.

> He was able to grab all the files from his friend's machine but he is worried that the files are encrypted.

> Help him get the file back

## About the Challenge
We got 2 files, `nothing.pdf` and also `encrypted1.zip` (This is a zip protected password) and we need to find the password for `encrypted1.zip` 

## How to Solve?
Open the `nothing.pdf` first, and then tried to use `CTRL + a` keyboard shortcut to select all texts


[Image extracted text: Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching; but you're too shy
to say it]


You will notice there was very small text at the bottom of the PDF file. Now, press `CTRL + c` to copy the text and `CTRL + v` to paste the text into a text editor (in this case, I'm using Notepad). We got some interesting results.

```
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy
to say it
29ebf2f279da44f69a35206885cd2dbc might be something you need
```

Afterward, I tried searching the MD5 hash on Google, and we found out that the password for the zip file is `diosesamor`


[Image extracted text: Google
"29ebf2f279da44f69a35206885cd2dbc"
Ucjuay
Jul 23,2015
29ebf2f279da44f69a35206885cd2dbc santyelmaslindo@hotmail es
29ebf2f279da44f69a35206885cd2dbc susana_alarconi@hotmail com
Pastebin.com
https Ilpastebin com
DB DE HOTEL.CLAN-UPCO
27, 2013
x504 = boomrasta = 29ebf2f279da44f69a35206885cd2dbc = 1
adriandiazpava5@hotmail.com = 190.66.153.96 =
https Ilpastebin com
Translate this page
HACKED BY F3LOMAN
Nosalgasconellos com
Mar 13,2013
722 mari m mcml32@hotmail.com 5b243bec911020e1fe77b6c484fa5193. 723
Zafiro Coceres zafiro154@gmail com 29ebf2f279da44f69a35206885cd2dbc .
Paste2 org
https Ilpaste2 org
Translate this page
Viewing Paste aEt3ahFz
29ebf2f279da44f69a35206885cd2dbc:diosesamor:
29f239ff16bb8a22df46014044c0559d:welcomme. 29f491121c63af2a883378c50e1f8d9f:startrek:
Aug]


Extract the zip file, and you will find one file called `flag.jpg`. Open it to obtain the flag.


[Image extracted text: encrypted1.zip
ZIP archive; unpacked size 146,035 bytes
Vame
Size
Packed
Iype
Modified
CRC32
File folder
flagjpg
146,035
143,736
JPG File
5/29/2022 1331
flag-jpg
60%
dsc{N3v3r_9OnNA_gIv3_yOu_up}]


```
dsc{N3v3r_9OnNA_gIv3_y0u_up}
```