# Fr1endship Forever
> This is going to be a double hunt...

> My childhood Fr1end James has posted something about the project he made on his socials (just to flaunt). Today is our submission day and my Fr1end James is absent. Yesterday when we met him, he told me, "Mark can you submit my project also with yours, as I will be going out of the city tomorrow morning." He forgot to tell me anything about his project. He is not even picking up my phone.

> Help me find him and of course his project.

## About the Challenge
We need to find james account first to get more hints

## How to Solve?
When I tried to find in some social media (Twitter, LinkedIn, etc.) using `Fr1end James` keyword. I've found an account which I believe this account related to the chall


[Image extracted text: Frlend James
Top
Latest
People
Photos
Videos
James @FrlendJames
Mar 30
Our Endsem_Last_Minute-Project is getting recognization.
Happy to hear that W!L
0
0 2
Il
483
Crcd@craddiocactced
Anroo
0Cio]


When I tried to stalk that account, I've got more hints


[Image extracted text: James @FrlendJames
Mar 30
Our Endsem_Last_Minute-Project is getting recognization
Happy to hear that !!
0 2
Il
485]


[Image extracted text: James @Fr IendJames
Nov 25,2022
ohhl
accidentally added a comment somewhere that should not be told
openly:
I]


[Image extracted text: James @FrlendJames
Nov 24,2022
the version control is superb:
our project is
gr8_
Il
doing]


I belive the flag was located in GitHub and inside the comment. And then the repository is related to `endsem_last_minute`. I decided to search the repository first in GitHub using `endsem_last_minute` keyword


[Image extracted text: endsem_last_minute
Filter by
result (108 ms)
Code
Your-James/Endsem_Last_Minute-Project
Repositories
Python
Updated on Nov 27, 2022
Issues
82
Pull requests]


Open that repository and go to commit history. Find a commit with `Update Suggester.cpp` title to obtain the flag


[Image extracted text: Update Suggestercpp
88
main
Your-James committed on Nov 27,2022
Verified
Showing 1 changed file with 1 addition and
deletion:
Suggester_cpp (Q
@@
-115,7 +115,
@@
void
getDetails()
115
115
116
116
117
117
118
got it!
VishwaCTF {LbjtQY 449yfcD}
118
Oops
119
119
int main()
120
120
121
121
[ISTORING DATA]


```
VishwaCTF{LbjtQY_449yfcD}
```