# Corny Kernel
> Use our corny little driver to mess with the Linux kernel at runtime!

> $ socat file:$(tty),raw,echo=0 tcp:corny-kernel.chal.uiuc.tf:1337

## About the Challenge
We were given a `c` file called `pwnymodule.c` and here is the content of `pwnymodule.c`

```c
// SPDX-License-Identifier: GPL-2.0-only

#define pr_fmt(fmt) KBUILD_MODNAME ": " fmt

#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>

extern const char *flag1, *flag2;

static int __init pwny_init(void)
{
	pr_alert("%s\n", flag1);
	return 0;
}

static void __exit pwny_exit(void)
{
	pr_info("%s\n", flag2);
}

module_init(pwny_init);
module_exit(pwny_exit);

MODULE_AUTHOR("Nitya");
MODULE_DESCRIPTION("UIUCTF23");
MODULE_LICENSE("GPL");
MODULE_VERSION("0.1");
```

This code is a basic linux kernel module. This code will print the first part of the flag when the module is loaded

```c
static int __init pwny_init(void)
{
	pr_alert("%s\n", flag1);
	return 0;
}

...

module_init(pwny_init);
```

And the code will print the second part of the flag when the module is unloaded

```c
static void __exit pwny_exit(void)
{
	pr_info("%s\n", flag2);
}

...

module_exit(pwny_exit);
```

And in this chall, we need to connect to the server and inside the server there is 1 file called pwnymodule.ko.gz


[Image extracted text: proof-of-work:
disabled
EZ
mount
-n
-t
proc
~0 nosuid
noexec, nodev proc
Iproc/
mkdir
~p
Idev Isys Ietc
mount
~n
-t
devtmpfs
~0
mode=0755,nosuid,noexec
devtmpfs
Idev
mount
~n
-t
~0
nosuid, noexec, nodev
sys /sys
cd
Iroot
exec setsid
cttyhack
ash
-1
Iroot
# ls
pwnymodule
ko . gz
sysfs]


## How to Solve?
First, we need to gunzip the file first using `gunzip` command

```bash
gunzip pwnymodule.ko.gz
```


[Image extracted text: Iroot
gunzip pwnymodule.ko.gz
Iroot
# ls
pwnymodule
ko
Iroot
#]


And then we need to load this module inside the server using `insmod` command

```bash
insmod pwnymodule.ko
```


[Image extracted text: Iroot
insmod pwnymodule
ko
[
172.328397]  pwnymodule:
uiuctf{muster_]


As you can see we have the first part of the flag, and then we need to unload the module using `rmmod` command

```
rmmod pwnymodule.ko
```

And then print the kernel messages by using `dmesg` command to obtain the second part of the flag


[Image extracted text: [
0.192704]
with arguments:
0.192705]
linit
E
0.192705]
with
environment
[
0.192706]
HOME=/
192707]
TERM-linux
E
0 . 199992]
mount (31) used greatest stack depth:
[
172
328397] pwnymodule:
uiuctf{muster_
[
265 .041009] pwnymodule:
k3rNEI_haCk3r}]


```
uiuctf{m4ster_k3rNE1_haCk3r}
```