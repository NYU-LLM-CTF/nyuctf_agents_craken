# What is the name of WhatsApp user which has phone number +37062166565
> What is the name of WhatsApp user which has phone number +37062166565?

## About the Challenge
We need to find the name of WhatsApp user

## How to Solve?
We can find the email by exporting the SQLite Database first from `/userdata/root/data/com.whatsapp/databases/wa.db`


[Image extracted text: wa.dO-wal
419
wa db
248
Export Eiles:
axolotldb
1220
Export File Hash List_
media.db-wal
214
stickersdb
Add to Custom Content Image (ADD)
1208
032e0
0Q 00
0Q 00
OO-0Q
00 00 00 00
0Q 00 00]


Open the SQLite database using `DB Browser for SQlite` software and import the database. In the `wa_contacts` table, we can see the name of WhatsApp user


[Image extracted text: number
raw_contact_id
display_
name
phon
[Filter
[Filter
[Filter
Filter
00 +37062166565
10 Marcus
NULL
NULLI NULL
0 1525
Sask papildymas
1577
Klientu aptarnavimas
033
Greitoji pagalba
011
Gaisrine
022
Policija
0 117
5 PILDYK informac_]


```
Marcus
```