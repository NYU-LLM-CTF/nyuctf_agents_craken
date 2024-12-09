# Encrypt10n (2)
> We made a memory dump on the criminal machine after entering the crime scene. Our investigator thought he was using encryption software to hide the secret. can you help me to detect it?

> Q2 : crew{password}

## About the Challenge
We got a encrypted flag file and we need to decrypt it using `TrueCrypt` software

## How to Solve?
To solve this, we need to install `TrueCrypt` first, and then upload the flag there and you need to input the `TrueCrypt` password


[Image extracted text: TrueCrypt
Volumes
System
Favorites
Tgols
Settings
Help
Drive
Volume
Size
Encryption
Igorithm
Type
D:lflag
9.8 MB
AES
Normal
WARNING; Using_TrueCrpt
notsecure
Wipe Cache
Volume
D: flag
Select Eile...
Never save history
Volume Iools_
Select Device
Dismount
Luto-Mount Devices
Dismount All
Exit]


In this case i mounted the flag into `Z:` drive. Now open the drive, and you will see there is a file called `flaaaaaaaaaaaaaaaaaaaaaaaag.txt`. Open the file and decode it using `base64` 14 times


[Image extracted text: Recipe
0
Input
D 9
TUt
4TS {
UI
A-Ld-LO-Yt=
SESWaGhNVnBvVmtSS QyTXlUalphUjJoVFRXMW9
bGRYZUcSaUlXUnpWMWhvlVZKRINuQlVMIJGVFRGUIZtRkhPVmhTTUhCNVZHeGF jMWRO
UZtoaFJsslhUWp3VkZacVJuZFNWalpSVDFkclUwMHlhRmxXYlhCTFRrWlJlRmRzYUZSaVJuQnhl3hrVTFsVIVsWlhivVpPVFZad2VGVXlk
REJXTVZweVkwlndXROV4YOhKWIZXUkdaVWRPUOUSVIpHaGhNSEJZVmlOUlMxUnRWaZRqUldVIlsZGIWRIJYTlcSVIZtUlhWV3MIWsxWFVu
Strict mode
cFdNVZhZVIZaSlIxTnNaRIZXYkZwNLZGUkdVMklSUmtaUFYyaHBVbGhDTmxkVVFtRmpNVIIwVTJOaldHSlhhRmhaVkVaMlZrWmF jVkpOzEd?
UZEzQXaXbFZhYT JGVINuTmhNMmhYLIRGd2FGWIVSbFpsUmlSMVUyczFXRkpZUWSoVZ6QjRZakZaZUZWc 2FFOVdlbXh6VIdOYWQyVkdW:Gxr
UkVKWFRLlndvilSZUhkWGJGcFhZMGhLVjJGcldreFdha3BQVWpKSIIxcEdaRTVOUlhCSIZqRmFVMUIAVlhoWFdHaFlZbXhhVjFsc2FHOVds
From Base64
bXhaWTBaaldGWnNjRmxaTUZVMVIWVXhXRIZIYOZkTlYyaDJWMVphUzFJeFRuTmFSbFpYWltadmVsWkdWbUZaVjFKRIRslmFVRIISYUhCVmJH
ENaREZrVjFadEIWVkSWbkF3VIcwMVMxlkhTbGhoUmloYVZrVmFNMVpyV2IGalZrcDFXalpPVGxacmIzZFhiRlpyWXpGVmVWTnVTbFJoTTFK
Alphabet
Remove non-alphabet chars
WVZGYzFiMWRHYkZWUZEzQnNVbTFTZWxsVldsTmhSVEZaWVclblYxlXphSEpXVkVaclVqRldjMkZGTIZkaGVsWjVWMWQwWVdReVZrZFdibEpy
A-Za-
z0-9+/=
VWtWS2IxbF] jRWRsVmxKelZtNUSXROpHYOZoWklGSIBWMnhhVOZWclpHRldNMmhJVIRJeFIxSxlSaZhoUlRWNFYwVktSbFpxUZpSVO1XeFhl
VmhvWVZKWFVsWlpiWFIzWpGVZNWTnRPVmRTYlhoNVZtMDFhMVI4V2SOalNHaFdWakSvYZxaclZYaFhSbFpGwVVaalRtRnNXazFXYWtKclv6
Rk9SMVplVWxCV2JGcFlXV3RvUTJJeFdrZFdiWVphVml4c05WVnRkRzlWUmxsNVIVWm9XbGRJUWxoVklGcGhZMVpPYIZWcldrNVdNVlzVmxS
Strict mode
SO5GWXhlIWGxUYT JSVVlsVmFWbFpOzUhkTklWcHlWMjFHYWxacmNEQlZiVEV3VmpKSZNsTnJiRmROYmxKeVdYcEdWbVF3TVVsaVIwlnNZVEZ3
VZkWGVHOVJNVkpIVId4YvlWsldjSESWYIRGVFYyeHNjbGRzVGLoUlZFWjZWVEkxYjFZeFdYcGhSMmhoVWtWYVIWc
ZXbXRrVmxaMFpVWk9x
RkpyYOZwVZExcGhXVlpzVjFSclpGZGlhelZYVlcxeklWlXhXblJsUjBaWFlrWktWMVpYTIVOVIZsWlZUVVJyUFE9PQ==
From Base64
2360
1758
Raw
Bytes
Alphabet
A-Za-20-9+/=
Remove non-alphabet chars
Output
WJ
crew{Tru33333_
Crypt_wlth_VOl4tlllty!}
Strict mode
From Base64
Alphabet
A-Za-z0-9+ /
Remove non-alphabet chars
Strict mode
STEP
BAKEI
Auto Bake
5 1
0 33
6ms
Raw
Bvzes]


```
crew{Tru33333_Crypt_w1th_V014t1l1ty!}
```