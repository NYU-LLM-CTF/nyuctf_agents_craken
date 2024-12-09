# Easy pwn
> `-`

## About the Challenge
We need to get the country name, city name, and IP evidence


## How to Solve?
We get a twitter username @7amada_Elbes. And then he had 1 post and you can access [here](https://twitter.com/7amada_Elbes/status/1626186898631806977)


[Image extracted text: Hamada ELbes
7amada_Elbes
Replying to
YourAnonNews
Hahaha finally iam a hacker now
could hack the camera in my street
HRa)]


After doing some research (I find on google using `find camera online` keyword), I found the webcam website and you can also access it [here](http://www.insecam.org/en/view/858775/)


[Image extracted text: Country:
Egypt
Country codez
EG
Region:
As Suways
Suez
Latitude:
29.973710
197.166.232.101.60001
City:]


```
0xL4ugh{Egypt_Suez_197.166.232.101}
```