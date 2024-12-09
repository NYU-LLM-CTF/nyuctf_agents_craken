# Truth
> Kuronushi traveled far away from his country to learn something about himself. He never sure about his identity. Untill One day, he met a sage who gave him a book of truth. The sage said " To understand about yourself,Erase the title and find the Bigger case"

> Submit the flag on this format ARA2023{} Separate the sentences with _

## About the Challenge
Given a PDF file that is locked using a password (You can get the file [here](Truth.pdf))

## How to Solve?
To solve this problem, I use `pdfcrack` to bruteforce the PDF using the `rockyou.txt` wordlist


[Image extracted text: kaliokali)-[~/Desktop]
pdfcrack -f
Truth.pdf
lusr share
/wordlists/rockyou.txt
PDF
version
1.7
Security Handler:
Standard
~1060
Length: 128
Encrypted Metadata:
True
FileID: 077el0eba516a741a6285385042f5027
U: df507156115f50098c3d8c6fdbld662200000ooooooooooooooooooooooooooo
7a46addd4179a8ab90812ae8876369522d5facc72245be4f2803559473767d57
Average
Speed:
46186
W/s 
Current
Word:
iluvannie
Average Speed: 44856
w/s
Current
Word
erindunn
Average Speed: 44223.2 w/s
Current Word:
uscrip
found
user-passuord:
subarukun]


The password for the PDF is `subarukun` and when I open the file, the PDF contains a kind of story that has 4 pages


[Image extracted text: Truth Amongst the pages Of Purana
Sumeru's story is
wild ride from the very start. when you enter the region, you Il meet
researcher known as haypasia.
alter the smell Of incense gets to the traveler's nose, they'Il
fall
asleep and connect directly with
tree, where you'Il hear the words
world:
~forget me
after hanging Under with tighnari for a while and clearing out a withering zone, he will
tell Nilou that irminsul is the world tree that contains all the wisdom; and it has recently been
corrupted  this corruption is the reason for the appearance of withering zone and Diseases like
cleazar that collei suffers from,
later, you'IL head over to
Sumeru city hoping to
audience with lesser lord
kusanali_
soon
after; you'Il go to port ormos and meet dori in an attempt to get the divine capsule
that can help you. you'Il witness the effects this capsule had on an eremite as alhaitham gets
his hand on it.
the next day,
spend a good time with dunyarzad at the subzeruz festival. towards the end,
the grand sage from the akademiya
prevent nilou from performing the dance of subzeruz
as he says "go celebrate the birth of that god t0 your heart's content
the traveler Learns the meaning of this line soon enough because It turns out that we're
1n a
repetitive dream of some sort where were stuck O the same day of the subzeruz festival.
after multiple attempts at stopping the samsara_
finally able to do it with the help of
nahida a.ka_
lesser lord Kusanali by asking nilou to perform her dance_
soon after the end of samsara, YOu set to learn more about the akademiya's plan by
trying to turn setaria on your side.
setaria is the personal secretary for grand sage, but she is
one of the few people in the akademiya who belong to the desert
get
you'II
will
you re]


And then in the question there is a hint `Erase the title and find the Bigger case`. So I removed the title and searched for words that were capitalized


[Image extracted text: (kaliokali)-[~/Desktop]
grep
[A-Z]+ Wt
pdf
txt
Sumeru
Under
Nilou
Diseases
Sumeru
Learns
Kusanali
Even
Find
Nahida
Desert]


If only the capital letters are taken, a flag will be formed

```
ARA2023{SOUNDS_LIKE_FANDAGO}
```