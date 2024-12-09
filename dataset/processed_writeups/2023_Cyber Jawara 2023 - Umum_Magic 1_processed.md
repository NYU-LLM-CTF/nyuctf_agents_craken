# Magic 1
> Another warmup with PHP web app.

## About the Challenge
We were given a source code (You can download the source code [here](magic-1.zip)) and website, here is the preview of the source code


[Image extracted text: https:IImagic-1.ctf cyberjawara.id
Im not a robot
reCAPTCHA
Privacy
Terms
Choose File
No file chosen
Upload]


The website only has 1 functionality where we can upload a file and the file can be accessed in `results` endpoint

## How to Solve?
Even though we can upload some file, there are some restriction here

```php
function canUploadImage($file) {
    $fileExtension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $fileMimeType = $finfo->file($file['tmp_name']);
    $maxFileSize = 500 * 1024;
    return (strpos($fileMimeType, 'image/') === 0 &&
        $file['size'] <= $maxFileSize &&
        strlen($file['name']) >= 30
    );
}
...
...
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['image'])) {
    if (canUploadImage($_FILES['image'])) {
        move_uploaded_file($_FILES['image']['tmp_name'], 'results/original-' . $_FILES['image']['name']);
        $resizedImagePath = resizeImage($_FILES['image']);
    } else {
        $error = 'Please upload different file.';
    }
}
```

We need to upload an image where the file size is equal or less than 500 * 1024, and the file name is equal or greater than 30 characters. We need to insert the PHP payload into the image, for example `<?php system("cat /flag.txt"); ?>`.


[Image extracted text: https:IImagic-1.ctf cyberjawara idgresultsloriginal-awikwokawikwokawikwokawikwokawikwokawikwoks php
DPNG
HHDR?
vj2 PJtEXtprofileC12023{4nOth3r_unrestricted_file_upload__}r
V
YIDATxvv6vmVP DA 00801 vaK
#,00-w002OP00010 90000 POUWc0R{JQVwv01v 6[s8~+9900pv990v ROU8u? {00-@s~KS
10Q000L90VL? 46 Bn 0[00@~ 80000000-8000 00D0O{002n+D1-00480; 0Vm?oPO?
KBO6zy0^& .heV~ 0000800000QR0O[fV KN00008000 V0/wvvvv Qv]Y-6e+G@vn @ONO(S
288"
2@D
?w
20110ON?2]


```
CJ2023{4n0th3r_unrestricted_file_upload__}
```