# rsa
> I think I did my RSA right...

## About the Challenge
We got 3 files, `flag.enc`, `public.pem` and `private.pem`. And we need to decrypt the `flag.enc`

## How to Solve?
Well, because we've got the private key, we can decrypt file directly. In this case im using `CyberChef` to decrypt the flag


[Image extracted text: Recipe
Input
+ D9g
IAcre | Vo eQ&IAiierxsCBVxakeoyE
Ax02X Usohe+A_SFs "73B.IeeT.C iEH@ cR ENQP (  IEU t'
"NAK; Jsoxa  AawuAeso
e&zzo BE/.I
RSA Decrypt
(BniaEExyE
(ae PYBWAo- 87+EzJrec j
RSA Private Kev (PEM)
BEGIN
RSA PRIVATE
KEY _
MIICWWIBAAKBgQDJTZEROqf1384il8XiqfglUlVucqQJaqhmim
GABZNHLBojFkIL
Kev Password
Encryption Scheme
RAW
128
Raw Bytes
Output
0 0 @ :
NULNULAULNULNWLNULAULNULNWLNULAULNULNUL
hulnMLNMLAuLAMLNMLNMLAuLAMLNMLNMLAuLAMLNMLNMLAuLAMLNMLNMLAuLAMLNMLNMLAuLAMLNMLNMLAuLAMLNMLNMLAuLAML
NULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULNULi
ctf{keep_your_private_keys
private}]


```
ictf{keep_your_private_keys_private}
```