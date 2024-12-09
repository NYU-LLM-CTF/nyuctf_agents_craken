# Git er' done
> I've made my first website but I still have a lot of tasks to do. Can you check it out and give me some feedback?

## About the Challenge
We were given a very simple website that contain To-Do list


[Image extracted text: Welcome to my website!
To-do:
add
more cats
setup automatic cloning from git repository
more
pink
add hits counter
make more lists]


## How to Solve?
Because the title of the challenge is about `git`. So I accessed `.git/config` endpoint and we got the git config


[Image extracted text: config
File
Edit
View
[core]
repositoryformatversion
filemode
true
bare
false
logallrefupdates
true
[remote
origin" ]
url
https://gitlab.com/WalmartDeli/exposed-repository.git
fetch
+refs/heads_
:refs_
remotes/origin/*
[branch
'main" ]
remote
origin
merge
refs/heads/main]


I went to https://gitlab.com/WalmartDeli/exposed-repository.git and then there is a file called `flag.txt`


[Image extracted text: Initial commit
Payton Harmon authored
week ago
main
exposed-repository
flag txt
flag:txt
32 bytes
texsaw{Oh_
no
my_
glt_15_3xp053d!}]


```
texsaw{0h_n0_my_g1t_15_3xp053d!}
```