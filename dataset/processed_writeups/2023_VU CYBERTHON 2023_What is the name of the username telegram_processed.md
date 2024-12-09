# What is the name of the username telegram
> What is the name of the username telegram?

## About the Challenge
We need to find the name of the username telegram

## How to Solve?
Go to `root/data/org.telegram.mesengger.web/files` (Don't check `org.telegram.mesengger`). And then extract `cache4.db` SQLite database


[Image extracted text: cache4.db-wal
cache4.db-shm
cachetdb
Blue_9_p-pXcflrmFIBAAAAvXYQk-mCwZU_vS jpg
Export Eiles__
Blue_8_dk_wwlghOFACAAAAfz9xrxibeuw_v5 jpg
Export File Hash List__
Blue
p-pXcflrmFIBAAAAvXYQk-mCwZU_v5 jpg
Add to Custom Content Image (ADD)
Rlie 6 | lix?TFc ISVACAAAARIAvl
SOMkM v5inn]


Open the database file using `DB Browser for SQLite` software and then find `users` table and you will find the `uid`


[Image extracted text: Database Structure
Browvse Data
Edit Pragmas
Execute SQL
Table:
users
uid
name
status
data
Filter
[Filter
[Filter
Filter
5398345740 iL..);;
1666470314 BLOB
2 5719323092 john cash;=
1666508479 BLOB
5754490378 marcus;; ;marcusssss129 1666508750 BLOB]


```
5719323092
```