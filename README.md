# python-gpio-mysql

Install docker

```bash
curl -sSL https://get.docker.com | sh
```

Install dependencies

```bash
sudo apt-get install docker-compose python3-venv mariadb-server mariadb-client
```

Pull down the source

```bash
sudo mkdir /opt/telemetry
sudo chown pi:pi /opt/telemetry
git clone https://github.com/jcustenborder/python-gpio-mysql.git /opt/telemetry
cd /opt/telemetry
ln -s telemetry.service /usr/lib/systemd/system/telemetry.service
```


Setup a python virtual environment. This allows our code to be isolated from anything that happens to python on the system.

```bash
python3 -m venv venv
```

```bash
source ./venv/bin/activate
pip install -r requirements.txt
```

Setup the database. *If you run this more than once it will delete the contents of the database.*

```bash
cat telemetry.sql | sudo mysql
```

Start the collection process.

```bash
./run.sh
```