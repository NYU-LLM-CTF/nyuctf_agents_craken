# RFC standard for security policy information
> The Lithuanian company Altacom uses one of the latest RFC standard formats for presenting security policy information.

> This standard makes it easier for security specialists to identify the contacts they should reach out to in order to report a vulnerability to the organization.

> Please help me find the email address to report any vulnerabilities found.

> Flag format: VU{email@address.com}

## About the Challenge
We need to know the email that company use to receive vulnerability report

## How to Solve?
After finding about Altacom company on google, I found the official website (https://www.altacom.eu/). And if we want to know the email that company use to receive vulnerability report, you can access `/.well-known/security.txt` endpoint


[Image extracted text: Contact:
mailto:report@altacom
Expires
2024-02
10708
10:00.000z
Preferred-Languages
lt_
Canonical:
IWWw.altacom
eu/
well-known/ security
txt
Policy:
https
{ WWW
altacom.eulprivacy-policy/
https]


```
report@altacom.eu
```