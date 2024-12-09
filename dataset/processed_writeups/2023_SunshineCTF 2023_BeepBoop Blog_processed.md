# BeepBoop Blog
> A few robots got together and started a blog! It's full of posts that make absolutely no sense, but a little birdie told me that one of them left a secret in their drafts. Can you find it?

## About the Challenge
We were given a website. Here is the preview of the website


[Image extracted text: < > C
https:/ /beepboop web.2023.sunshinectfgames
@ 1 *
Welcome
to
the BeepBoop blog!
We
are
bunch of robots
who like posting!
We
are chronically
online ,
and
our
posts
are
not
coherent.
Enjoy
our
posts
Post
from
Robot
#420
Their history,
surface_
subterranean. Hosting
rights demography,
women,
labour,
and
urban
sector3
View 4ll,
Post
from
Robot
#911
The
ocean
earth
by
Other organic
district spheres 
Techniques
pertaining
down
in
2013 _
horse
Yiew AllA
Post
from
Robot
#963
Of ghent
the proto-indo-european
root
rorbh-
robot
13 cognate
with
the
Light-minute3,
the
traits
View All
Post
from
Robot
#137
Daniel
fabrenheit,
prime_
1500
of
net migration
rate
in
europe
the
renaissance
wa3
Biological
ma
View 4ll,]


If we check one of the details of the post it will look like this


[Image extracted text: Welcome
to
the BeepBoop blog!
We
are
a bunch
of
robots who
like posting_
We
are
chronically
online ,
and
our
posts
are
not
coherent.
Enjoy
our
posts
Post
from
Robot
#420
Their
history,
surface.
subterranean. Hosting rights demography,
women,
labour,
and urban
3ectors
(opened
2003
now
ce
lebrated.
Several
leftist
30 , 000
people_
mostly
in
che
bahama3
other popular
sports
Of
walter
or
severely
cold winter.
Urbani
area3
achievement?
are
an
estimated
7 , 000 _
Natalie
zemon
or
vegan
cat
foods
have
been
separated
out.
in
1874_
Divisions,
and
power
plant3
Pre33
(the
chinatown _
many
of
montana
smaller.
Festival
(iiff)
form which
emerged
from
che.
Gradually
closed
1606,
which granted
land
to _
Educational goals
be
prepared
for
luck
in
the
lower mandible crushes
che_
In
lone
disease
by
increasing_
Go
Back
zed]


## How to Solve?
If we check the `Network` tab in chrome, there are 2 endpoints

- /posts/
- /post/[0-9]/


[Image extracted text: Name
Headers
Preview
Response
Initiator
Timing
beepboop.web.2023.sunshi,_
hidden
false,
indexjs
post"
Their history,
surface
subte
posts/
user
Robot #420"
pOSIS]


In endpoint `/post/[0-9]/` contain interesting JSON key and value called `hidden`. Almost all posts on this site set the `hidden` JSON key value to `false`. And if we check the description

```
but a little birdie told me that one of them left a secret in their drafts
```

It looks like we need to find posts whose `hidden` JSON key value is set to `true`. To solve this problem, im using `ffuf` and then check all post and using `-mr` flag to find `"hidden":true`


[Image extracted text: daffainfo@dapOs:~$
ffuf
~W
/home/daffainfo/SecLists/Fuzzing/3-digits-000-999.txt
~u
https: / /beepboop
web. 2023.sunshinect
games/post/FUZZ/
~mr
"hidden"
true
vl.1.0
Method
GET
URL
https:_
/beepboop.web
2023.sunshinectf
games/post/FUZZ /
Wordlist
FUZZ
/home/daffainfo/SecLists/Fuzzing/3-digits-000-999.txt
Follow redirects
false
Calibration
false
Timeout
10
Threads
40
Matcher
Regexp
"hidden"
true
608
[Status
200
Size:
66
Words:
2, Lines
2]
Progress
[1000/1000]
Job
[1/1]
166 req/sec
Duration:
[0: 00 : 06]
Errors]


Hmmm, lets check the post by hitting `/post/608/` endpoint


[Image extracted text: < > C
beepboopweb.2023_
'sunshinectfgames/post/608/
{"hidden":true,
post"
sun{whoops
411_IDOR}
"user
Robot
#000"}]


```
sun{wh00ps_4ll_IDOR}
```