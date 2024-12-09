# Secure Platform
> Take a look at my super secure website. I only let people access the flag I hid there if they're just as secure as I am!

## About the Challenge
We need to find the flag on the website We were given. The website is just a plain website and there is a button to get the flag


[Image extracted text: Very Secure App
Welcome to my
secure
application! Click the button below to get your
Beware, I only give it out to people who are just as secure as I am:
Getyour flagl
flag'
very]


## How to Solve?
Press `Get your flag!` button and we will be redirected to a simple page like this


[Image extracted text: Your platform isn't secure enough' I only like platforms with an EAL of 6 or higher:
Your platform is "Windows" , Id much rather it be "INTEGRITY-] 78B".]


To solve this, we need to change the HTTP request header value named `sec-ch-ua-platform` from `Windows` to `INTEGRITY-178B`


[Image extracted text: what a secure OS! of course You can have my
flag!!
flag {shOuldv3_us3d_n4vlg4tOr}]


```
flag{sh0uldv3_us3d_n4v1g4t0r}
```