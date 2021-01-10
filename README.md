# apsi-project
Project for Analysis and design of information systems course at WUT-EITI

## Prerequisites
* [Docker](https://docs.docker.com/get-docker/) & [docker compose](https://docs.docker.com/compose/)

## Installation
* Clone repository to desired directory
`git clone https://github.com/paatrycjaa/apsi-project.git`
* `cd apsi-project`

## Run with docker
To set up and run django development server together with MySQL database use:
```
(sudo) docker-compose up
```

## Database modifications
If database modifications are made one needs to ensure that a new volume is used.
Volumes can be listed using:
```
docker volume ls
```
To check which container uses given volume run:
```
docker ps -a --filter volume=<VOLUME_NAME>
```
To delete volume run:
```
docker volume rm <VOLUME_NAME>
```
Unused volumes can be removed using:
```
docker volume prune
```
### Connecting to running database in container
```
docker exec -it apsi-project_db_1 mysql -u root -proot ideas_db
```