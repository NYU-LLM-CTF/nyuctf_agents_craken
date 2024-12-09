# ChapGPyT
> I've made ChatGPT implemented a challenge. I hope you can solve this verry hard challenge

## About the Challenge
We were given a website to test and this website only have 2 endpoints. First is `/post_message` where we can input our message and then in the response we got some random string. Here is the HTTP request and response when I tried to send a random message using `/post_message` endpoint


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
post
{post
Qessage
HTIP/11
HTTP / 1
200
Or
Host
chatgyt
ruble_
host
Server
ngin:/1-
18_
(Ubucuh
User-Agent
Hozilla/5
(Vindous
IT
Vin64;
*64;
rv:109
Sun _
Jul
2023
14:59:22
GHT
GeckoZOlOOlOl Firefor/lls_
Content
Type
cext/html
charset-uc f-8
Accept
Conneccion:
elose
Accept-Language
en-US ,en;4-0
Content
Lencth:
32
Aecept
Encoding:
szip ,
deflace
Content
Type
applicat
on / *-U -
TorMcUL
encoded
df8311b3SdO_dfl7fbh4d644e313bla6-
Content-
Lengch:
Origin
http
( ( chatopyt
ruble
host
10 Connect
on:
close
Re ferer
http
((chatoyt
ruble
host /Post _
message
messagezd
Dace]


And then the second endpoint is `/get_message/$id`. We need to input the output from the `/post_message` endpoint into the `$id`. So for example `/get/message/df8311b35d02df17fb4d644e313b1a62`


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
GET
{set
message/df8311635402df17fh4d6442313bla83
HTTP/1.1
HTTP/1
200
OK
Host
chatgpyt . rumble-host
Server
ngin:/1-
18
(Ubucuh
User-
Agent
Hozilla/5
(Vindous
Vin64;
*64;
17:109
Dace
Sun ,
Jul
2023
15 : 04: 07
GHT
Gecko/CO1OO1O1
Firefor/115.0
Content
Type=
tert /htul;
charset-uc f-8
Accept
Content
Length:
Accept-Language:
Eol
US
en ; 4-0_
Connect
on:
close
Aecept-Encoding:
gzip ,
deflace
Origin:
http
( ( chatopyt
ruble
host
Connect
on:
close
Re ferer:
http: / /chatcpyt
rlble
host /Post
message]


Our input will be reflected in the response

## How to Solve?
At first, i got stuck for so long because i already tried some web exploitation such as Arbitrary File Upload, SSTI, etc. And then I tried to search the random string in google and also tried to crack the random string, it turns out that is a number that has been hashed using `MD5`


[Image extracted text: Enter up to 20 non-salted hashes,
one per line:
df8311635d02df17fb4d644e313b1a62
Tmnot a robot
reCAPTCHA
Privacy
TTenns
Crack Hashes
Supports: LM
NTLM;
md2
ma4
md5
mdS(mds_
hex)
mdS-half, shal, sha224_
sha256, sha384, sha512, ripeMD16o
whirlpool, MySQL 4.1+ (shal(sha
bin))
Qubesv3 1BackupDefaults
Hash
Type
Result
df8311635d02df17fb4d644e313bla62
md5
117359]


Now, I tried to check another message with id `c4ca4238a0b923820dcc509a6f75849b`. That hash is equivalent to 1


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
GET
get_hessage/e4ca4238306923820dcc509a6f7584Sb
HTTP/1.1
HTTP/1
200
Host
chat gyt
ruble
host
Server:
nginx/1
(Ubucu)
User-Agent
Hozilla/5
(Vindous
IT
10.0;
Vin64;
{64;
17:109
Dace
St
Jul
2023
15 : 09:46
GHT
Gecko/ZOlOO1ol
Firefor/115
Content-
Type:
tert/htul
charsetzuc f-8
Aecept
on:
elose
Lccept-Language:
en-US
en ;
Content-Length:
Aecept
Encoding:
Jzip ,
deflace
Origin:
http
( (chatopyt
ruble
host
CSR ( GrindingChat GPTUnt
IItGives-oulChallangelol}
Connection:
close
Re ferer:
http: / /chatoyt
ruble
host /Post
message
10
Conn
470 -]

```
CSR{GrindingChatGPTUntilItGivesYOuAChallangeLol}
```