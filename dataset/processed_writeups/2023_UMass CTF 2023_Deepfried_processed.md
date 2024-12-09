# Deepfried
> `-`

## About the Challenge
We were given a source code (You can download the file [here](DeepFried.zip))


[Image extracted text: Upload an image to fry with your caption.
Choose File
No file chosen
Alternatively,
an
image URL here.
Submit
(Image should be less than ~250 KB
put]


## How to Solve?
If we check the the source code, we will see there is a folder called `restriced_memes` and inside the folder there is an image called `TheFlag.jpg` so I'm assumming we need to access `/restricted_memes/TheFlag.jpg` to obtain the flag


[Image extracted text: TheFlag jpg
100%
UMASS
CYBERSEC
CLUB
UMASS{PLACEHOLDER}]


But we can't access that endpoint directly because that endpoint can only be accessed locally.

```javascript
router.all('/restricted_memes/:img', async (req,res, next)=>{
    if(req.ip === '::ffff:127.0.0.1') {
        next();
    } else {
       return res.status(403).send("Unauthorized Request");
    }
})
```

So, the idea here. We need to input `http://127.0.0.1:3000/restricted_memes/TheFlag.jpg` in the `Image URL` form


[Image extracted text: deepfried web ctf.umasscybersec
2 >
C
Not secure
deepfriedweb ctfumasscybersecorg 3000/captionsubmit
UMASS
CYBERSEC
CLUB
Image Censored for Security
See
txt in this directory for the
UMASSS
Flag
flag:
flag:]


As we can see in the image, the flag was located in `flag.txt` directory. So we need to input `http://127.0.0.1:3000/restricted_memes/flag.txt` in the `Image URL` form


[Image extracted text: test]


Press `CTRL + U` to check the source code


[Image extracted text: Line
wrap
<div
id-"stuff"
<div
id="content" style=
text-align:
center;
<hlxtest< /hlx<br>
src="VUIBULNZdkBNbyRfQVByMGSUYVJ fMSEpIUkhfQo=" >
<[div>
<[div>
<img]


You will see there is a Base64 string in `img` tag. Decode the msg using `Base64` Decoder to obtain the flag

```
UMASS{v@Mo$_APr0nTaR_1!i!I!}
```