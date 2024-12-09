# Chandi Bot 6
> We finally found the source code. Can you dig through find the secret?

> https://github.com/1nv8rzim/Chandi-Bot

## About the Challenge
We need to find the flag inside `Chandi-Bot` repository

## How to Solve?
Open the repository and then go to `Pull requests` menu


[Image extracted text: Code
Issues
82  Pull requests
Actions
Projects
Secu
Firs
If you knov
Filters
ispr isclosed
Clear current search query; filters,
sorts
32
Open
2 Closed
8 8 Update gitignore
#3 by opabjumbs was closed
hour ago
Fix packages
by Inv8rzim was merged last week
and]


Choose the first [pull request](https://github.com/1nv8rzim/Chandi-Bot/pull/1) and then choose `fixed helpers errors` commit to obtain the flag


[Image extracted text: fixed helpers errors
88
fix-packages (#1)
MaxFusco committed last week
commands/main-go (Q
82,6
+82,6 @@ func StartScheduledTasks()
func
StopScheduledTasks() {
if len( ScheduledEvents)
> 0 {
quit
'RS{GIT_CHECKOUT
THIS_FLAG}"
85
quit
kill"
87]


```
RS{GIT_CHECKOUT_THIS_FLAG}
```