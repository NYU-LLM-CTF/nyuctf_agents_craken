# reguest
> HTTP requests and libraries are hard. Sometimes they do not behave as expected, which might lead to vulnerabilities.

## About the Challenge
We were given a website and the source code (You can get the source code [here](chall.zip)). The website is pretty plain, here is the preview


[Image extracted text: Usage:
Look
the
code
Overwriting
cookies
With
default value
This
must
be secure
Prepared
request
cookies
are
[( 'PHPSESSID "
922682077210adb07fe7e97d313e6f74') , ( 'role
guest')]
Sending request_
Request
cookies
are:
[('PHPSESSID"
922682077210adb07fe7e97d313e6f74' ) ,
('role
guest' )]
Response
is
Guest:
Nope
;-)]


## How to Solve?
If we check on the source code (Especially `backend.py` file), to get the flag there are 2 conditions that must been met

```python
@app.route('/whoami')
def whoami():
	role = request.cookies.get('role','guest')
	really = request.cookies.get('really', 'no')
	if role == 'admin':
		if really == 'yes':
			resp = 'Admin: ' + os.environ['FLAG']
		else:
			resp = 'Guest: Nope'
	else:
		resp = 'Guest: Nope'
	return Response(resp, mimetype='text/plain')
```

First, a cookie named `role` must be set to `admin`, and second, a cookie named `really` must be set to `yes`. After setting the cookies in the HTTP request header, you will receive the flag.


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
HTTP /11
HTTP/11
200
Host :
124
14:10014
Server:
Werkzeug/? -
3 Python/ 3
11- -
User-Agent
Hozilla/5
(Vindous
IT
10 _
Vin64;
*64;
rv:109
Gecko/:O1OO101
Dat e
Fri
10 Har
2023 10: 03:15
GHT
Firefor/110_
Content
Type
text /plain;
charset-uc f-8
Aecept
Content-Lengch:
332
cert /htul
applicat
on / xhthltxnl , application/xnl;q-0.9
image/ avif,inage /vebp ,* /*;4=
Connection:
close
Lccept-Lanquage
Eo
en ; 4-0_
Usage:
Lool
che
code
Aecept
Encoding:
Jzip ,
deflace
Connect
on -
close
Overvrit
coolies
vith
default
value
This
must
be
secure
Upgrade
Ins
cure-
Requests:
Prepared
reqest
cookies
are:
role
suest
really
Yes
Coolie
role
adin
really-yes
12 Sending
request
10
13
Request
coolies
are:
rol-
suesc
really
Yes
15
Soneone
drunk:
16
Response
is:
Adin:
EIO
R3Qu3sts_
413
5013T1u 35
Zelrd
dont
set
confused}
18
ing]


```
ENO{R3Qu3sts_4r3_s0m3T1m3s_we1rd_dont_get_confused}
```