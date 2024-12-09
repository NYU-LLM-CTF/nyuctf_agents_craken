# Blue's Clues 3/8: Source IP
> Martin has no idea who this user is, it's not a Rezifp employee and it has admin privileges. From which IP was this user created, by which user, using which user agent, and using which type of gitlab token?

> Flag format: <creator_username>|<source_ip>|<user_agent>|<gitlab_token_type>

> Not case sensitive.

> Example: myaccount|127.0.0.1|someuseragent|SomeTokenType

## About the Challenge
We need to find the some information for example, username, source ip, etc that created `yvandescreds` account

## How to Solve?
First, I searched the username in the KQL syntax and then I want to find the log that contains string `username`. And if we check the result of `gitlab.username` search field, the result is `mimine1965` created that user


[Image extracted text: Discover
logs-
'username" and "yvandescreds"
usernam
1,291 hits
Available fields
1,500
gitlab username
gitlab username
json username
July
August
threat enrichments indicatorurl:
Top values
Apr 16,2022
username
yvandescreds
99.8%
threat indicator.url username
mimine1965
0.2%
uriusername
Calculated from 1,291 records_
Empty fields
Document
931
message
There are no empty fields.
Visualize
{"method
POST
path
@timestamp Apr
12 ,
2023
Meta fields
{users
sign_out gitlab
Apr
12 ,
2023
11:39:18.975
message
Cannot
index
event publi
@timestamp
Apr
12
2023]


After that, I changed the KQL syntax like the image below because I want to find the log when `mimine1965` created `yvandescreds`. Choose the oldest logs and you will obtain some information


[Image extracted text: Discover
New
Open
Share
Alerts
Inspect
logs-*
"mimine1965" and "yvandescreds"
Expanded document
View:
Single document
Surrounding documents
K <
5 of 5
X
ip
5 hits
Available fields
60
host
0S
platform
ubuntu
apache access ssl cipher
host
0S
type
linux
client.ip
May
June
July
August
2022
host
0S
version
20
04.6 LTS
(Focal Fossa)
client nat.ip
Apr 15,2022
input.type
destinationip
destinationnatip
Documents
Field statistics
file.path
Ivar /log/gitlab/gitlab-rails /api_json
dll pe.description
field sorted
offset
45,177
dns resolved_ip
@timestamp
Document
message
enterprisesearch change authenticati
@timestamp
Apr
12
20'
{"time
2023-04-12T03 :14:58. 5892"
severit
on_token ciphertext
INFO"
duration_S
:0.69511 _
db_duration_
file pe description
Apr
12 ,
2023
10:16:50.421
message
:0.37209 ,
view_duration_s
:0.32302 ,
statu
Cannot
index
event
pub-
:201 _
method"
POST
{apilv4/user
gitlab meta pipeline_id
@timestamp
Apr
12 ,
20,
params
1{
email"
value
"Yvan
Des
Creds@rezi
fp.com'
},{"
name
value
gitlab meta remote_ip
Des
Creds" }, {"key
username
value
yvan
gitlab meta subscription_plan
Apr
12 , 2023
10:16:50.421
message
descreds
}, {"key"
password'
value
[FILTER
Cannot
index
event
ED]"}, {"key
admin"
value" :null}] ,
host
gitlab remote_ip
@timestamp
Apr
12
20'
0. 0.0.4'
remote_ip
10 .0
0 . 5
127
0.0.1"_
hostip
curl/8.0.1
route
api
:version/user
user_id
username
mimine1965
token
json metapipeline_id
Apr
12 ,
2023
10:14:59.371
message
type
PersonalAccessToken
token_id" :4,
{"time
2023-04-12103
eue_
duration_s
0 . 020833 _
redis_calls
:30, "re
json meta remote_ip
@timestamp
Apr 12 ,
20,
dis_duration_s
006811 _
redis_read
bytes
json meta subscription_plan
cache
calls
gitla
67_
redis_write
bytes
5497 ,
redis_cache_
call
log
log
log
log . (
path'
'key"
Yva
'key"
pub;]


```
mimine1965|10.0.0.5|curl/8.0.1|PersonalAccessToken
```