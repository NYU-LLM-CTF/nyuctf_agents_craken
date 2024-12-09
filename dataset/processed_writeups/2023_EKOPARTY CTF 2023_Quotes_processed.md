# Quotes
> No one will ever think about haxor quotes with flags inside.

## About the Challenge
There is a bot called `BotServ` which has many functions, such as being able to search for quotes, being able to display quotes, etc.


[Image extracted text: BotServ
BotServ allows you
to have
bot
on
your
own channel -
BotServ
It has been created for
users that can
t host
or
BotServ configure a bot,
or
for
use
on
networks that don't
BotServ
allow user bots_
Available commands
are listed
BotServ
below;
to
use
them,
type /msg BotServ
command 
For
BotServ
more information
on
a
specific command,
type
BotServ
Imsg
BotServ
HELP
command 
BotServ
HELP
Displays this list and give information about commands
BotServ
QUOTES
Random Haxor Quotes
BotServ
BotServ
Bot will join
a
channel whenever there is
at least
BotServ
1
user(s)
on
it_]


## How to Solve?
First, we need to search `EKO` in the quotes list using this command

```
/msg BotServ QUOTES SEARCH EKO
```

The result:
```
06:44 <Test> Hola QUOTES SEARCH EKO
06:44 <Test> BotServ Random quotes matching your query: 313337
```

Interesting, now we need to print the flag using the ID we just obtained using this command

```
/msg BotServ QUOTES #general get 313337
```


[Image extracted text: 06:44
<Test>
Hola
QUOTES SEARCH EKO
06:44
<Test>
BotServ
Random quotes matching your query:
313337
06:45
<Test>
ChanServ
has left IRC (go_ctf_site services_ctf_site
06:46
<Test>
Hola QUOTES #general
313337
06:46
<Test>
BotServ
Random quote #313337 :
deserve this my
friend EKO{b4slc_search}'
get
"You]


```
EKO{b4s1c_search}
```