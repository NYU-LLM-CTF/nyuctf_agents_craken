# Urban Odissey
> I can't remember the city where I lost my trail. Can you help me find my secret map of the treasure?

## About the Challenge
We were given a `pcapng` file that contains a lot of requests about city (You can download the file [here](urban_odissey.pcapng))

## How to Solve?
When I analyzed the file, there is 1 unusual HTTP request like the image below:


[Image extracted text: POst
HTTP/1.17
Host:
127.0.0
1:8077
JUser-Agent: python-requests/2.28.1
Accept-Encoding:
gzip,
deflatel
Accept:
xlx
Connection:
keep-alive
IContent-Length:
67
Jontent-Type: application/X-w-form-urlencoded
s3cr3t-TGFOOjESL jAZMDcZMTkOMjAWjKZLCBMb2SnojcYLjgWjOOOTcSMDAONZAAHTTP/1.1
200
OKI
Server:
Werkzeug/2.3.4 Python/3.9.71
Date:
Wed ,
25
Oct
2023 09:52:26
GMTI
IContent-Type:
text/html;
charset-utf-8
IContent-Length:
43
Connection:
closel
alpr fBperg
jaq3elat u0j
1
p4a 9Bpelcg
1g]


When I tried to decode the string, the result was the latitude and longitude of a location


[Image extracted text: Karvy Stock
Mahanagar
Hor
Rroking Limited
St
19.06076194200696,72.8564497900
Restaurants
Hotels
Things to do
Transit
P
Parking
Pharmacies
A
A
LIC
Tresind Mumbai
100]
Saved
Fine Dining
sssS
Kotak Mahindra Bank
312q
Transrail
Hfezt
Icp
Lighting Limite
<Ra
Recents
Madarsa E Haidery
drfer fafez
Ahle Sunnat
Shia Masjid
100]
Raza Mosque
{M
T 4ia
New Good Luck Medical
& General Stores
YUL
2
cq
Overhead
PIC
19203'38.7"N 72251'23.2"E
Club Acoustics
#feapal & JRG4
Tank
Teti
Guitar Institute
19.060762, 72.856450
Prestige 101 BKC
Wockhardt Towers
al818 ziarf
TUV SUD
A
Bandra Kurla
Service-
allmark Business Plaza
Directions
Save
Nearby
Send to
Share
77HT
BKC METRO STATION
TagT TMT
phone
44h
TOSTEM STUDIO
14 Rrn
Mumbai
Aluminium
TUV SUD
Service-
Sant Dnyaneshwar Nagar; Bandra East; Mumbai,
National Stoc
Maharashtra 400051, India
Vaibhav Chambers
d1 *3
Service
3V64+8H4 Mumbai, Maharashtra, India
t in BKC
TUV SUD
Service-
84 - Hfarv
Add a missing place
MRz 3T._
Top rated
Food and Drug
Add your business
Administration
TUV SUD
317 4 3144
Service-
4r17T4_
Central GST Bhawan
Add a label
(Erstwhile Utpad,_
Hzat vigd
H4T.
{
1
;
8
1
8]


Now, let's find `Mumbai` inside the `pcapng` file and there is 1 HTTP request that contains that string


[Image extracted text: POst
HTTP/1.17
Host:
127.0.0.1:8077
JUser-Agent: python-requests/2.28-
Accept-Encod
gzip,
deflatel
Accept:
xlx
Connection:
keep-alive
Content-Length:
11
Jontent-Type: application/X-w-form-urlencoded
kcity-MumbaiHTTP/1.1
200 OK
Server:
Werkzeug/2.3.4
Python/3.9_
Date:
Wed ,
25
Oct
2023 09:52:32
GMTI
kContent-Type:
text /html;
charset-utf-8
IContent-Length:
80
Connection:
closel
l3Jkbmx lbnsxdF93NHNudFIOMDBfZDFmZFFjdWxox2 J1dFINdW  INDF fMXNFYzRoMHRpY18ZMDEWMHO
ing:]


Decode the body response using `Base64` encoding

```
srdnlen{1t_w4snt_t00_d1ff1cult_but_Mumb41_1s_c4h0tic_30100}
```