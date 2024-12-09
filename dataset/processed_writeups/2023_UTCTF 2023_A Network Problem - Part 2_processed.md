# A Network Problem - Part 2
> Update: smb port has been moved to 8445 from 445 on networking-misc-p2

> betta.utctf.live has other interesting ports. Lets look at 8445 this time.

## About the Challenge
We were given a SMB server to connect `betta.utctf.live:8445`

## How to Solve?
To get the flag you need to connect to the server using `smbclient` because this is SMB protocol. You don't need an username and password because the server allow anonymous login. First you need to know the `Sharename` on the server. You can use this command

```
smbclient --no-pass -L //betta.utctf.live
```


[Image extracted text: (kaliokali)-[~]
smbclient
no-pass
Ilbetta.utctf.live
Sharename
Type
Comment
WorkShares
Disk
Sharing of work files
BackUps
Disk
File Backups
IPC$
IPC
IPC Service ( Samba Server)
Reconnecting
with SMB1
for workgroup listing
smbxcli_negprot
smbl_done
No compatible protocol
selected by
server
protocol negotiation failed:
NT_STATUS_INVALID_NETWORK_RESPONSE
Unable
connect with SMBI
no workgroup available]


And then I connect to `WorkShares` using this command

```
smbclient -U '%' -N \\\\betta.utctf.live\\WorkShares
```

Go to `shares\IT\Itstuff\` and get the `notetoIT` file to get the flag


[Image extracted text: smb:
Wed
Mar
14:45:05
2023
Wed
Mar
14:45:05
2023
Shares
Wed
Mar
14:45:05
2023
9974088
blocks of
size
1024 .
6106316
blocks available
smb:
shares/IT Itstuffi
smb
shares  IT Itstuffl>
Wed
Mar
14:45:05
2023
Wed
Mar
14:45:05
2023
notetoIT
380
Wed
Mar
14:45:05
2023
9974088
blocks
of size
1024 .
6106316
blocks available
smb:
Ishares  IT Itstuffi >
get notetoIT
getting
file
shares  IT ItstuffinotetoIT
size
380
as notetoIT
(0.4
KiloBytes/sec) (average
0.4
KiloBytes/sec)
Gmio
Sshares  ITNItstuff >]


Here is the content of the file
```
I don't understand the fasination with the magic phrase "abracadabra", but too many people are using them as passwords. Crystal Ball, Wade Coldwater, Jay Walker, and Holly Wood all basically have the same password. Can you please reach out to them and get them to change thier passwords or at least get them append a special character? 

-- Arty F.

utflag{out-of-c0ntrol-access}
```

```
utflag{out-of-c0ntrol-access}
```