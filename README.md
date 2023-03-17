**Guide**:

1) python app preparation
- pull repo
- cd kreoshine-backend
- make virtual environment for python as you want
- install requirements.txt (or pip-freeze.txt)
- activate it
- be sure that "kreoshine-backend/settings/.secrets.toml" is exist (make it available)
- if your target system is Linux-based, be sure that content of secret file like this:
```angular2html
[server.admin]
sudo_passwd = "passwd-of-your-local-user-allowed-sudo"
```
- if your target system is Windows, change "kreoshine-backend/settings/dev_support/windows.toml" with your expectations

2) postgres initialization
- make docker available at your workstation
- create volume for postgresql ``` docker create volume postgres_data ```
- create postgres container with a database named "kreoshine":
```angular2html
docker run -d --hostname postgres --name postgres -p 5432:5432 -e POSTGRES_DB=kreoshine -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -v postgres_data:/var/lib/postgresql/data postgres
```

3) run backend application ``` python3 run.py ```
