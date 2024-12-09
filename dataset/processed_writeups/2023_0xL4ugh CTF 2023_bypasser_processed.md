# bypasser
> `-`

## About the Challenge
We are given a website. There is a login page and we need to bypass the login page


[Image extracted text: ONLY FOR CORP
Please enter your username and password!
Email
Password
Forgot_password?
Login]


## How to Solve?
After asking a hint to the admin, we know we need to bypass the login page but there are some filter. So the website is filtering some characters such as
```
' " ) % = SPACE
```
After doing some research and I found this [blog](https://www.invicti.com/blog/web-security/fragmented-sql-injection-attacks/) , i can bypass the login page by using this payload
```
user: \
pass: or/**/1/**/#
```

After that we will be redirected into `otp.php` endpoint


[Image extracted text: LOGIN
Please Enter OTP Code
Enter The Code
Forgot_password?
Login]


After redirected into `otp.php` endpoint. My burpsuite receive a lot of new javascript endpoint and I found `/bypasser/js/ExternalCustom.js` file and that is a obfuscated javascript


[Image extracted text: Content
Length:
1853
Connect
on:
close
Content-
Type:
application/ Javascript
var
Oxfd9_=
XED
179 X4B
X65 *791*31 *32 *33"
1x76
Xe XeC"
X23 *70' x61
x73 *73 *771 Xep *72 x64"
X651 *EE  *63
x72 *79
x701*74"
x41*45
x53"
x76
Xe1 *ec
Xe9
X64
Xel *74 *es
XZE *70 *e8
x70"
123
165
IED
K61
x69 *eC "
165 *EE
163"
x73
x74 *72 Xes
XEE
Xe7
Xes
Xe6 *79"
X64
Xe5
X63
x72 *791*701*74
x70 *61
x721 *73
X65"
x73 XEC Xe9 X63 Xe5"
x68
*74  *ED   *ec"
123
IED
X651*731*73 *61 *67
165"
Xe8
x731*651 *66
XEc  *EP1*631*611*741*691 *EP
XEB"
x4F
x54
x50 XZE
x701x68
x70"
XEA
x73
Xeb
XEE"
270
IEF *73 *74"
123 KGF
174 *70"
Xeb
x74
X70 *76
X61
Xec
X691 *64-
X61 *747
Xes
XZE
x70'
Xeb
x70"
x74
x31 xed Xef *30
xefixee *421*301*61 *721*64 xZe *701*68
x70"]
fuct
on logear ( )
Var
Oz9eccrz=
Ox fd9_[0]
passwordEncryp=
CryptoJs
Ox fd92[4]]
Oxfd92[3]] (F
Oxfd9z[z]
Oxfd9z[1]] ()
OxSeccxz,
format
CryptoJSlesJson
Oxfd92[18] ]
Oxfd92[5] ,
email:;
Oxfd9_ [6]
Oxfd9_[1]] () ,passvord:passvordEncryp
toString(]


After i deobfuscate the file, I found new endpoint named `t1mo0onB0ard.php` and we will get the flag

```
0xL4ugh{YOU_ARE_A_DEBUGGER}
```