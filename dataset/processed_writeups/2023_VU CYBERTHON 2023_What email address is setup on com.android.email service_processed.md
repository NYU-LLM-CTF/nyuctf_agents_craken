# What email address is setup on com.android.email service
> What email address is setup on com.android.email service?

## About the Challenge
We need to find the email address that set up on com.android.email

## How to Solve?
We can find the email address by exporting the SQLite Database first from `/userdata/root/data/com.android.email/databases/Emailprovider.db`


[Image extracted text: Name
Size
Type
EmailProvider db
ular File
Export Eiles_
EmailProviderBody.db
Iular File
Export File Hash List_
pgp.db
Iular File
Add to Custom Content Image (ADD)
pgp.db-journal
Treyular File]


Open the SQLite database using `DB Browser for SQlite` software and import the database. In the `Account` table, we can see the email


[Image extracted text: Newv Database
Open Database
Write
Changes
Revert
Changes
Open Project
Save Project
Attach Database
Close
Database Structure
Browvse Data
Edit Pragmas
Execute SQL
Table:
Account
Filter in any column
displayName
emailAddress
syncKey
syncLookback
syncInterval
hostAuthKeyRecv
hostAu
Filter
Filter
Filter
Filter
Filter
Filter
Filter
Filter
Joohnnycashz@gmail com Joohnnycash7@gmail com'NULL
4 -1]


```
Joohnnycash7@gmail.com
```