# inspect
> Don't think too much. Just push to production http://chall.foobar.nitdgplug.org:30045/

> Rest API was boring so I used modern technology.

## About the Challenge
We were given a website and we need to get the flag from that website


[Image extracted text: 2 >
C
Not secure
chall foobar nitdgplug org 30045
Cannot
GET]


## How to Solve?
After getting stuck for a while because I tried a lot of endpoint like `robots.txt` / `.git` / etc. But the website always return `404 Not Found`. And then I decided to doing some research about REST API and the alternative. Luckily I found `graphql` keyword and tried to access graphql endpoint.


[Image extracted text: 9
C
Not secure
chall foobar nitdgplugorg 30045/graphql?
1 *
GraphiQL
Prettify
Merge
Copy
History]


And when I tried to input `{` in the form, I found a field named `secret` and I tried to execute GraphQL using this query


[Image extracted text: {sh
secret
events
bookings
schema
[Flag!] Self descriptive]



[Image extracted text: GraphiQL
Prettify
Merge
Docs
Search:
secret
(Use
fref
syntax for
regexp
search)
{secret
text
errors
message
"String
cannot represent value:
text: | "GLUG{giv3_4_mAN_4_FiSh}| '
"locations
line
column"
path" :
secret
"text"
message
"String
cannot represent
value:
text:
1 "GLUG{a_CO1d_
day_1N_HEl1}| "
locations
"line"
column"
path" .
secret
"text"
message
"String
cannot represent value:
text:
1 "GLUG{THe
13th_leTZer_ofCoURSE}| '
locations
"line"
column
QUERY VARIABLES
Copy
History]


As you can see the result of the query is 75 different flags, but it's impossible to test the flag one by one. And im thinking, `Usually the flag is relatable with the chall, for example this chall is about graphql so the flag usually related to graphql`

I tried to search using `ph` (I took the 2 lettter from `graphql` keyword). And luckily I got the flag


[Image extracted text: Search:
phl
(Use
/re/
syntax for regexp
search)
coLumn
path": [
secret
44 ,
text"
message
"String
cannot represent
value:
"GLUG{Insp3c7_In_gr4phq6} |
}"
locations
"line
column
path
flag:]


```
GLUG{1nsp3c7_1n_gr4phq6}
```