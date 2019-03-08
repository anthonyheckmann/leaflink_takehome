# ｌｅａｆｌｉｎｋ Takehome
## Prerequisites
* docker
* docker-compose
* Internet access to access:
  * images from hub.docker.com (*need postgres:alpine, python:alpine*)
  * **PyPi** module repository pypi.org (*need psycopg2, Flask-SQLAlchemy, sentry-sdk*)
  * **Alpine** packages from repo: pkgs.alpinelinux.org (*need postgresql-dev, gcc, python3-dev, musl-dev*)
## Startup
1. Type `docker-compose up -d` and it should bind the Flask app to port 8082
   * If there is a problem, you may retry running  with the command:
        ```
        docker-compose down &&\
        docker-compose up --build -d
        ```
    * This will remove previous attempt, recreate containers and restart them.

1. Next type `curl localhost:8082` and you should see the words _It works_
2. Try `docker-compose logs` to see more details of the running containers
3. You may edit `SENTRY_SDK_URL` in _docker-compose.yml_ *Line 28* if you'd like to set your own Sentry account. [sentry.io here](sentry.io)
## Caveats
### **TL;DR;** try running *docker-compose* with *sudo*
* Depending on your system, docker may be unhappy about forwarding port 8082. Try running the `docker-compose` command as *root*, or as `sudo docker-compose`
* Similarly, docker my complain about mounted volumes, again try running as *root* or prefix `sudo`
* Also, docker may complain about insufficient access to the docker server or daemon. The solution