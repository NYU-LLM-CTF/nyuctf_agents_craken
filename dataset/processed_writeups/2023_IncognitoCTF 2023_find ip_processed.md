# find ip
> `-`

## About the Challenge
We need to find the ip to the machine

## How to Solve?
I found the IP by checking this repository (You can access the repository [here](https://github.com/kristenchavis01/dotfiles)) and there is a folder named `.ssh`. And then if we open the `known_hosts` file we can get the IP address


[Image extracted text: dotfiles
ssh
known_hosts
kristenchavis01   Initial commit
Code
Blame
lines
loc)
843 Bytes
170.187.232.216 ssh-ed25519
AAAACBNzaCllZDIL
170.187.232.216 ssh-rsa
AAAAB3NzaClyc2EAAAAD
170.187.232.216 ecdsa-sha2-nistp256
AAAAEZVj]


```
ictf{170.187.232.216}
```