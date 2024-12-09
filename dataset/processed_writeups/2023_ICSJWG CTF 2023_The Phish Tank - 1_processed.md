# The Phish Tank - 1
> Snowpoint has an internal mail server, which is used by field engineers on computers that do not have access to the Internet. Some of these engineers have reported emails that look suspiciously like phishing attempts. The internal mail server is very basic, and because it is located on an internal network, the Snowpoint staff did not spend much time configuring security or encryption. Consequently, all emails are sent over unencrypted SMTP.

> Network traffic from these emails is ingested into Malcolm. Since this network is not connected to the Internet, Snowpoint’s security team would like you to look at these emails and, if they do prove to be phishing emails, determine how they were sent from an internal network. The first step is identifying the source of the suspicious emails.

> What is the IP address of the computer that sent the phishy emails?

> Flag format: IP Address. Example: 192.168.1.20

## About the Challenge
We need to find the IP address of the computer that sent the phishy emails

## How to Solve?
In this case im using `Arkime` dashboard instead of `Malcolm` dashboard.First, im using this query in the search filter to find any logs that related to `SMTP` protocol

```
protocols == smtp
```


[Image extracted text: protocols
smtp
Seaich
Custom
Stant
2023/04/05 21.45.36
End
2023/05/11 22.45.36
Bounding
Last Packet
Interval
Auto
01.00:00
50 per page
Showing
50 of 113 entries
Fetch Viz Data
This cluster is set to hide the graph if a time range f 30 days or greater is requested
Click the "Fetch Viz Data" button above t0 fetch visualization data for this query (or open the dropdown for more options).
Protocols
Data
Log Type
Start Time
Stop Time
Src IP
Country
Src Port
Dst IP
Country
Dst Port
Packets
Databytes
Tags
IInfo
Source
Bytes
smtp
smtp
zeek
files
2023/05/05
2023/05/05
114
Celestic
06.11-50
06.11-50
celestic
snowpoint
smtp
tcp
Icp
smtp
zeek
smtp
2023/05/05
2023/05/05
10.140.32.126
50842
10.140.1.3
Celestic
Sender
savannah snorunt@snowpoint-field org
06.11.50
06.11.50
celestic
Receiver-
candice abomasnow@snowpoint-fieldorg
snowpoint
Subject
Evening Report from Field Station-€
tcp
tcp
smtp
zeek
conn
2023/05/05
2023/05/05
10.140.32.126
50842
10.140.1.3
853
Celestic
06.11.40
06.11-50
2,117
celestic
snowpoint
smtp
tcp
Icp
smtp
sumcata
alert
2023/05/05
2023/05/05
10.140.1.3
10.140.32.126
50842
565
Celestic
06.11.40
06.11.50
565
celestic
snowpoint
smtp
tcp
smip
tcp
arkime
session
2023/05/05
2023/05/05
10.140.32.126
50842
10.140.1.3
853
snowpoint
Sender
savannah snorunt@snowpoint-field org
06.11.40
06.11-50
2,453
Celestic
Receiver -
candice
abomasnow@snowpoint-field org
smtp statusco
Subject
Evening Report from Field Station €
de 250
smtp
celestic
smip
smtp
zeek
files
2023/05/05
2023/05/05
114
Celestic
06.09.11
06.09.11
celestic
snowpoint
days]


There are 113 entries. If we check the entries one by one, I found an interesting email


[Image extracted text: 7926695986393418560
Content-Type: textlplain; charset-"us-ascii"
MIME-Version:
Content-Transfer-Encoding: 7bit
Grace
Have you received any weird emails lately?
just received an email about an account expiration; but the attached Iink did not go anywhere
Wanted t0
get your thoughts on this
Isaiah
79266959863
3418560]


So we need to find an email about account expiration and I found an email from `10.140.1.105` about account expiration, a PDF report, and a DOCM file that might be malware.


[Image extracted text: tcp
Icp
smtp
zeek
smtp
2023/05/05
2023/05/05
10.140.1.105
35744
10.140.1.3
Celestic
Sender
candice abomasnow@snowpoint-field org
01.09.19
01.09.19
celestic
Receiver -
isaiah piloswine@snowpoint-field org
snowpoint
Subject -
Account Expirationl
lease Open Immediatellyl
AIl Sessions
9 Link
Actions
230504
waSUTcGkXbfuXkKjjNHXA
Root Id: CBIVUm MPhhOO6pBC9
Time
2023/05/05 01.09.19
2023/05/05 01.09.19
Node-
celestic
Protocols -
tcp
smtp
IP Protocol
tcp
Src IPIPort -
10.140.1.105
35744
Dst IPIPort -
10.140.1.3
25
Celestic
celestic
snowpoint
Email
Subjects
Account ExpirationIli Please Open Immediatellyl
Senders
candice abomasnow@snowpoint-field org
Destinations
isaiah piloswine@snowpoint-field org
SMTP Hello
snowpoint-email-server
Taps]


[Image extracted text: smtp
tcp
smtp
tcp
arkime
session
2023/05/05
2023/05/05
10.140.1.105
60772
10.140.1.3
40,066
snowpoint
Sender
candice abomasnow@snowpoint-field org
01.19.18
01.19.28
43,712
Celestic
Receiver
sergio snover@snowpoint-field
smtp statusco
Subject
Annual Report Attachedl Do not Missll
de 250
Filenames
annual_report docm
smtp
celestic
kDownload PCAP
Source Raw
1 Destination Raw
9 Link
Actions
230504-4wPZgIRbIZBDwZi_KB_ANYTE
community Id: 1F76YWA+HIGwRIw pg YNdBqfy63U=
Time   2023/05/05 01.19.18
2023/05/05 01.19.28
Node
celestic
Protocols
smtp
tcp
IP Protocol
tcp
Src
Packets 40
Bytes 42,538
Databytes 39,890
Dst -
Packets 15
Bytes 1,174
Databytes 176
Etheret -
Src Mac e8.b5.d0.24.e9 4a OUI Dell Inc
Dst Mac e8b5.dO-1d.d1.13
OUI Dell Inc
Src IPIPort -
10.140.1.105
60772
Dst IPIPort -
10.140.1.3
25
Payload8
Src 65686c6120736e6f
ehlo sno
Dst 32323020736e6177
220 snow
Celestic
celestic
smtp
smtp statuscode 250
snowpoint
org
Taps]


```
10.140.1.105
```