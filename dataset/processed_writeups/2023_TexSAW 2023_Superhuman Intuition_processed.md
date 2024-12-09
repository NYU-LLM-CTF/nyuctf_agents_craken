# Superhuman Intuition
> Alice: "Now I am not sure who made this sculpture, but just from looking at it, I can tell that the artists has a YouTube channel. Not only that, I can tell you the exact date they created their channel!"

> Bob: "Impossible! There is no way that you can deduct all that information from just glancing at a sculplture!"

> Alice: "Oh yes I can Bob, and I will tell you the date right now. The artist created their YouTube channel on..."

> Note: The flag will be the date that the artist created their YouTube channel. The flag's format is texsaw{mm-dd-yyyy}.

## About the Challenge
We were given an image of a sculpture. First, we need to determine the artist who created the sculpture, and then we need to find their YouTube channel.


[Image extracted text: ]


## How to Solve?
To know who made the sculpture, im using `Google Reverse Image`


[Image extracted text: Quantum Man
Search
Find image source
C
Sculpture by Julian Voss-Andreae
More images
Visual matches
Search
Text
Translate
contessagallery com
Julian Voss-Andreae
Did you find these results useful?
Yes
No
Waiting for play google com__]


The artist name is `Julian Voss-Andreae`. So I tried to find his youtube channel by searching his name on Google


[Image extracted text: Julian Voss-Andreae Youtube
X
0
AlI
Videos
Images
News
Shopping
More
Tools
About 24,500 results (0.33 seconds)
YouTube
https_/lwwwyoutube com
user
julianvossandreae
Julian Voss-Andreae
Julian Voss-Andreae_
@julianvossandreae.
julianvossandreae 713 subscribers 81 videos.
Sculptures by Julian Voss-Andreae (WWW:JulianVossAndreae.com).
You visited this page on 4/16/23.]


We found his Youtube channel. If we want to know when the artist created his Youtube channel, we can check in the `About` menu


[Image extracted text: Julian Voss-Andreae
Subscribe
@julianvossandreae 716 subscribers 81 videos
Sculptures by Julian Voss-Andreae (WWWJulianVossAndreae com)
HOME
VIDEOS
SHORTS
PLAYLISTS
COMMUNITY
CHANNELS
ABOUT
Description
Stats
Sculptures by Julian Voss-Andreae (WWWJulianVossAndreae com)
Joined Feb 27,2009
167,474 views]


```
texsaw{02-27-2009}
```