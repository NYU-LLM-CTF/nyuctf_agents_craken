# X-Is for blabla
> Recently my friend was buy helmet called RFC 2616, pretty strange huh?

## About the Challenge
Given a plain website (There are only pictures and text), but when you look at the HTML code there is a new file called `readme.html` which contains something like a story


[Image extracted text: Brendo merupakan youtuber mukbang dari Jepang_
Brendo setiap mengupload video youtube nya menggunakan browser yang hits
Omaga.
Tentunya di laptop komputer Brendo menggunakan sistem operasi Wengdows agar bisa bekerja secara produktif:
Ohh ya; akhir
akhir banyak kasus stalker kepada youtuber di Jepang; oleh karena itu Brendo tidak suka diikuti oleh stalker:
Biasanya, setelah melakukan streaming Brendo selalu membeli Kue yang berada di dekat rumahnya.
Tempat toko kue tersebut ada di jalan No. 1337, selain ke dari toko tersebut enak ada alasan lain Brendo
membeli ke di tempat tersebut:
Itu karena sang penjaga toko adalah perempuan cantik bernama Araa, oleh karena itu Brendo mencoba mendekati perempuan tersebut untuk menjadi pacarnya_
yaitu
sering]


## How to Solve?
To solve this chall, we must adjust the conditions of `readme.html.` So there are 5 conditions that must be met to get the flag:

* Language must be set to `ja` (Japan)
* Browser must be set to `Omaga`
* Set operation system to `Wengdows`
* Tracker settings
* Then there is a `Cake` that must be set (There are 2 conditions namely the `Number 1337` and the name of the girl is `Araa`)

The HTTP request will be looks like this


[Image extracted text: GET
Iweb . php HTTP/1.1
Host:
103.152.242.116:5771
User-Agent: Omaga
Accept-Language:
ja
Sec-CH-UA-Platform: Wengdows
Cookie:
Kue-eyJubyI6IjEzMzciLCJuYWlhIjoiQXJhysJg
DNT :
1]


And in the response a flag will appear


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
[Jeb
php HTTP/1.1
HTTP/1-1
200
Host :
103-15_
243-116- 5771
Dat e
Su
Feb
2023
11.33:15
GIT
User-Agent
Onaga
Server
Apache/ 2 _
(Debian)
Lccept
X-Povered-By:
PHP / 7 -
cexe/htzl
applicat
on / xhcultxul
application/xhl;q-0
1mage
avif,inage/vebp ,  / ;TF0
Vary
Aecept
Encoding
Lccept
Language-
Content -
Length:
392
Aecept
Enco
ding:
szip
deflace
Connection:
close
Sec
CH-Ul-Plat forn:
Wengdovs
Content-
Type
cext /htnl; charset-UTF-8
Connection:
close
Coolie
Kue
eyJubyIGIjEzMzciLCJululhoiIGIlFyquEifoz=
10
IDOCTIPE
htul>
10
ade-Ins
Cur =
Requests:
<cencer?
DIT
<hlz
12
BREITDO
BARUHUDA
13
</h1>
<hr>
<br>
<1-~
reade
htul
15
srcz"https: / /1-Pining-
con/ 564x/54/06/46/540
Jidch=
50Opx
he_
ghc =
50Opx
<b>
cencer
Fonnichiva
1/5<br>
Qoomaagaa 2/5<br>
Wengdovs
User
huh?
3 /5<br>
Oke gaada lagi
Yg ngikutin
Fanu
4/5<br>
htnl>
Upgr=
<ing]


```
ARA2023{H3ad_1s_ImP0rt4Nt}
```