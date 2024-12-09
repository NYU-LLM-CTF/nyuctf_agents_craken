# Baby’s First IoT Flag 2
> Part 2 - What company makes the processor for this device? https://fccid.io/Q87-WRT54GV81/Internal-Photos/Internal-Photos-861588. Submit the answer to port 6318.

## About the Challenge

We just given some link to a report for internal photos of a wireless component and we need to find the company who’s make the processor


[Image extracted text: Baby's First loT
2
100
See introduction for complete context:
Part 2 - What company makes the processor for this
device? https:I/fccid.i0/Q87-WRTSAGV81/Internal-
Photos/Internal-Photos-861588.Submit the answer
to port 6318.
Flag
Submit
Flag]


## How to Solve

To find the company who’s has built the processor, i found some [wiki](https://infodepot.fandom.com/wiki/Linksys_WRT54G_v8.1) for the router


[Image extracted text: Serial
Num_
MDFO
FCC
ID
Q87-WRTSAGV81
CPU Type
Broadcom BCM5354KFBG
BCM5354K chip
rev
Soc)
MIPS
Rev
CPU Speed
240MHz]


It seems the company is `Broadcom`, then we try submit it


[Image extracted text: sinon@LAPTOP-2VOH1439
mnt/d/a/bountylctf$ printf
BroadcomIn|0
nc
35.225.17.48 6318
Enter the
company
that manufactures
the processor
for the FCC
ID Q87-WRTS4GV81
Access granted!
The Flag is {Processor_Re
con} ! sinon@LAPTOP-2VOH1439:
mnt/dla;
/bounty/ctfs]


```
{Processor_Recon}
```