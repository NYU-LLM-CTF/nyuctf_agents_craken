# Out of the Bucket 2
> This is a continuation of "Out of the Bucket". Take a look around and see if you find anything!

## About the Challenge
We got a exposed bucket GCP and inside the bucket there's a GCP credentials


[Image extracted text: ~biay
D ' COIJci LoJcooalCdo,#JC
1 0 / 0
Diay
<Size>29</Size>
</Contents>
<Contents>
<Keyzsecret/funny
json< /Key>
<Generation>1705174300570372</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified-2024-01-13719:31:40.6072</LastModified>
<ETag>
d1987ade72e435073728c0b6947a7aee"< /ETag>
<Size>2369</Size>
</Contents>
<Contents>]



[Image extracted text: type"
service
account
project
id"
out-of-the-bucket
private_key_
id
2leOc4cSef7ld9df424d40eed4042ffc2e0af224
private_key
Lc t
BEGIN
PRIVATE
KEY--
nMIIEVQIBADANBgkqhkiGIwOBAQEFAASCBKcwggS jAgEAAoIBAQDWxpWEDNiWgMzz | nxDDF64CspqiGPxkrHfhs4 /PX8BrxNjUMPF
G4hmOVOpGblAkfuE n62NErJVZIgQCowrBdFGbPxQc
IRQJKZrCFfKOWSHLvnngr4UiSCSr6OM33dfpD+v
nQSLkEQheYcXmHwh/W=
t4t7urC2i7OJdH+Y4Qw_
AZJNULo/SwWl Intx8i3FIDAgMBAAECggEABaGapVCO6RVNaQltffL+d7MS8296GHWmX34B6bqDlP7S nhe
hpx43LlKDUKogfs8 jgVMOANVEyDfhrYsVQWDZ5T60Qzp7bP2
nOzSDSACZpFzdflvXzOhero8ykwM3keQiCIKWYkeMGSX8oHyWr lf
udtAyebt /PC4HS9FLBioo3bAy8vL3o0Ob7+raVyJQQKBgQD3 IWaDSqSs 7HOrlOs_
In7IUhPlTDYhbLh 7pupbzDGzu9wCFCMItwTEm
CHkbP461CLSQoT
nTS6TO6Fs4xvnTKtBdPeisSgiIwKBgQDeetmpSgsk8ynnp6fx0 / LiuO3AzxpTYcP8
nixaXLQI6CI4jQP2+P+F
WL76FTZbubIdNm4LQyxvDeK82xQy18
nszeOxfJeoQKBgGQqSoxdwwbtFSLkbrAnnJIsPCvxHvIhskPUslyVNjKjpBdS28GJInej3
KIINOcA8ef7uSB3QYXug8LQi o2z7trMlpzq3nAoGAMPhD | nOSMqRsrc6xtMivzmQmWDSzgKX9OAAmEZ6rVebPufFYF jmHGFDqlRhc
EeZEZvbTjnyBgjcz26pJyVlvpU4bbstshUSaECgYEA7ZESXuaNVOEr 3emHiAz4 |noEStvFgzMDi8dILH+PtC3JZEnguVjMy2fceQH}
69kdpvJ3J556
nJWgkWLCz8hxtLcQPfDJuOYE=
n-
~END
PRIVATE
KEY_
In
client
email
image-server@out-of-the-bucket
iam.
gserviceaccount _
com
"client
id
102040203348783466577
auth uri
https
laccounts.google.com/o/oauth2/auth
token
uri
'https : / /oauth2
googleapis
com/token
auth_provider_
x509
cert
url
https
Iwww
googleapis
com/oauthz/vllcerts
"client
x509
cert
url"
'https : / /WWW. googleapis
com
robot/vl/metadata_
x509 / image-server84lout-of-the
universe
domain
googleapis.com']


## How to Solve?
First, we need to deploy Google Cloud SDK docker

```bash
docker run -it gcr.io/google.com/cloudsdktool/cloud-sdk:latest /bin/bash
```

And then inside the container, import the GCP credential

```bash
gcloud auth activate-service-account image-server@out-of-the-bucket.iam.gserviceaccount.com --key-file=file.json
gcloud config set project out-of-the-bucket
```

If we ran `gcloud storage list` command, we will see there are 2 buckets:


[Image extracted text: #
gcloud storage
ls
gs: / flag-images/
gS : / /out-of-the-bucket/]


Hmmm we `flag-images` bucket looks interesting, try to download every file inside that bucket using this command

```
gsutil -m cp -r gs://flag-images .
```


[Image extracted text: #
gsutil
-m
Cp
-r
gs: /  flag-images
Copying gs: / flag-images/256x192/ad.png_
Copying gs: / flag-images/256x192/ag.png_
Done
Copying gs: / /flag-images/256x192/ae-png
Done
Copying gs: / /flag-images/256x192/af .png
Done
Copying gs: / /flag-images/256x192/ai.png
Done
Copying gs: / flag-images/256x192/al.png-
Done
Copying gs: / /flag-images/256x192/am.png
Done
Copying gs: / /flag-images/256x192/a0.png
Done
Copying gs: / /flag-images/256x192/aq-png
Done
Copying gs: / flag-images/256x192/ar
png
Done
Copying gs: / /flag-images/256x192/as.png
Done
Copying gs: / flag-images/256x192/at.png-
Done
Copying gs: / /flag-images/256x192/bg-png
Done
Copying gs: / flag-images/256x192/aw.png_
Done]


This will download the file recursively and the flag is located in the `xa.png` file


[Image extracted text: xa.png
uoftctfisJrvlc3_Acceun7s_c4n_83_uns4f34]


## Flag
```
uoftctf{s3rv1c3_4cc0un75_c4n_83_un54f3}
```