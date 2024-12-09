# Blue's Clues 8/8: C2
> The pipeline executes on the gitlab server itself. It must be some kind of persistence. Find the C2.

> Flag Format: <domain_name>

> Lowercase.

> Example: a.b.google.com

## About the Challenge
We need to find the C2 domain name

## How to Solve?
Without using any KQL syntax, check the `url.path` result


[Image extracted text: Discover
logs--
Filter your data
KQL syntax
Ffn
2f7
L:2
uri
url path
Popular fields
url path
Top values
uri query
{server-status
46.6
[apilv4ljobs/request
19.5
Available fields
43
{machinel
event.uri
{HealthService
8%
threat enrichments indicatorurl
domain
lobr7CrUaaoy5LL8u3RqT6gL_
3.0%
threat enrichments indicatorurl
(-{metrics
2.0%
extension
{metadatalinstance
1.6%
threat enrichments indicatorurl
fragment
1.1%
threat enrichments indicatorurlfull
{machine
0.3%
threat enrichments indicatorurl
original
{Lenv
0.1%
threat enrichments indicatorurl
Other
4.3%
password
threat enrichments indicatorurlpath
Calculated from 81.474 sample records
using]


You will notice there is a very long URL path called `obr7CrUaaoy5LL8u3RqT6gLBTkdO5pzAqUs4JMcqsFRWulE8tgQA7EqqRD_Gx0MgO6HSwMlj5TleRRXMwcblsFn2o2enyUpuCsEf-d8ExZjl1eI2T4Mm0V`. Press the plus button to add the URL path into KQL syntax


[Image extracted text: Discover
logs-
Filter your data using KQL syntax
url path: /obr7CrUaaoySLL8u3RqT6gLBTkdOSpzAqUs4JMcqsFRWulE8tgQAZEqqRD_GxOMgO6HSwMIjS TleRRXMwcblsFn2o2
url.full
4,821 hits
Available fields
http Ilrezfiphealthcheck-
threat enrichments indicatorurl.full
f9fsh8dqbjfwasfZ zOLazurefd netlo
br7CrUaaoySLL8u3RqT6gLBTkdO5
threat indicator.url.full
Oct
Apr
pZAqUs4JMcqsFRWulE8tgQAZEqQR
2020
url.full
DGxOMgO6HSwMIjSTleRRXMwcbls
Feb 27
FnzozenyUpuCsEf-
Empty fields
d8ExZjlel2TAMmOV
Vch4co
There are no empty fields.
http:|Irezfiphealthcheck-f9fs_
100%
Document
Calculated from 4,821 records.
Meta fields
@timestamp
Apr
Multi fields
gent
type
packetbe
url full.text
Rezifp-GitLab-Ser
ne-
twork_traffic
@timestamp
Apr
Visualize
gent.type
packetb
Rezifp-GitLab-Seri
network_traffic.ht
Rows per page: 500]


Now check the `url.full` result to obtain the C2 server name

```
rezfiphealthcheck-f9fsh8dqbjfwasf7.z01.azurefd.net
```