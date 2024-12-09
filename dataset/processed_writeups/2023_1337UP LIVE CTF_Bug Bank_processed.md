# Bug Bank
> Welcome to BugBank, the world's premier banking application for trading bugs! In this new era, bugs are more valuable than gold, and we have built the ultimate platform for you to handle your buggy assets. Trade enough bugs and you have the chance to become a premium member. And in case you have any questions, do not hesitate to contact your personal assistant. Happy trading!

## About the Challenge
We were given a website without the source code. Here is the preview of the website


[Image extracted text: BugBank
Logout
Welcome wkwkwkwkwl
0 Bugs
AccountID: 36407880-8327-4772-8802-ff4285c0307b
TRANSFER BUGS
SETTINGS
Sun; 19 Nov 2023 10:24:17 GMT
Sender: wkwkwkwkw_personal_support | Recipient: wkwkwkwkw
Welcome to BugBank:
am your personal support concat: As soon as we build our chat function, you can send me messages. Until then; please do not send any transactions! It
gives me a notification and
need to check them:_
Cheers wkwkwkwkw_personal_support
Value: 0]


And in order to get the flag, we need to have at least 10000 bugs on our account and then buy the `Premium Flag Feature`


[Image extracted text: Premium Flag Feature
Experience exclusivity like never before with our Premium Flag Feature. For just 10,000 bugs, unlock prestigious benefits and stand out in the BugBank community:
Embrace the emblem of distinction, because you're not just trading bugs; you're making a statement!
UPGRADE]


## How to Solve?
There are 2 ways to solve this chall. The intended way from the author:
```
Get the ID of your support account via GraphQL, then send it a DOM Clobbering payload to hijack the service worker and sniff all the traffic:

https://portswigger.net/research/hijacking-service-workers-via-dom-clobbering
```

But in this case I solved it using an unintended way. So I created two accounts and then sent a negative value (Example: -10000000) to another account and then buy the flag


[Image extracted text: Premium Flag Feature
Thank you for joining the premium clubl
INTIGRITI{h3y_whO_541d_yOu_cOuld_clobb3r_7h3_dOm}]


```
INTIGRITI{h3y_wh0_541d_y0u_c0uld_cl0bb3r_7h3_d0m}
```