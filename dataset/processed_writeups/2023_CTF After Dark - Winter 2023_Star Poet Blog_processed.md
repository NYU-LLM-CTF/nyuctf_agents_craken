# Star Poet Blog
> oh dear... someone finding my password.txt i could not bear... but no fear... encrypted it i did to make it unclear... (*note: flag is all lowercase). Visit https://star-poet-blog.acmcyber.com.

## About the Challenge
We were given a plain website like this


[Image extracted text: the archive of upcoming star poet edgar allan poe
(last updated 1840)
about me
poetly_L0L: what's 4 poem?
poems
annabel lee
spirits_of the dead
dream
dream within a dream
the raven]


If we open the poems link, the website given us some poem i think? (The endpoint is `https://web/archive/annabel_lee.txt`)


[Image extracted text: "Annabel
Lee
By Edgar Allan
Poe
It
was
many
ana
many
year
ag0
In
kingdom
the
sea_
That
maiden
there lived
whom
you
may
know
By
the
name
of
Annabel Lee;
And
this
maiden
sne
lived
with
other
thought
Than
love
and
loved
me
was
child
and
she
Nas
child,
this
kingdom by
the
sea,
But
loved
with
love
that
Was
more
than
love_
and
my
Annabel
Lee_
With
love
that
the winged seraphs
of Heaven
Coveted
her
anc
me
And
this
Nas
the
reason
that,
a80 _
this
kingdom by the
sea
Wind
blew
out
cloud,
chilling
My
beautiful
Annabel Lee;
So
that
her
highborn
kinsmen
came
And
bore
her
away
from
me_
To
shut
her
in
sepulchre
this
kingdom by
the
sea_
The angels
not half
s0 happy in Heaven
long]


## How to Solve?
If we check the description of the flag, we need to read the content of `password.txt`. So we can easily just access `https://star-poet-blog.acmcyber.com/archive/password.txt`


[Image extracted text: flag{1377_
2127_3343_
4241_5864}
https:/ /en.wikipedia.org/wiki
Book_
cipher]


Im using `dcode.fr` website to decipher the flag cipher but the tool didn't output anything. And then I tried to explore the website and I found an interesting information


[Image extracted text: what is a poem
poem
stanza
line
word]


So to get the flag, we need to explore all the poem on the website and we need each part of the flag. For example `1337` that means
* Poem: 1
* Stanza: 3
* Line: 3
* Word: 7

And then we know the first part of the flag is `sepulchre`. Try to find all the flag parts and we will get the final flag

```
flag{sepulchre_tombstone_spirit_grains_nevermore}
```