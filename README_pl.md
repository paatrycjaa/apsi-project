# Moduł innowacji - aplikacja
Aplikacja webowa przeznaczona do użytku w ramach działalności szkół wyższych, służąca do zgłaszania, opiniowania oraz procesowania pomysłów na temat innowacji, które użytkownicy chcieliby wprowadzić w środowisku akademickim.

## Zarys technologiczny
Aplikacja zbudowana jest w stacku technologicznym:
 - Django (backend) - Python
 - AngularJS (frontend) - JavaScript, HTML, CSS
 - MySQL (baza danych)

Dodatkowo aplikacja przygotowana została do konteneryzacji z użyciem Dockera - stworzono pliki Dockerfile definiujące obrazy wszystkich części aplikacji.

## Wymagania
* [Docker](https://docs.docker.com/get-docker/)
* [docker compose](https://docs.docker.com/compose/) (przy dalszym rozwoju aplikacji)

## Instalacja
* Sklonuj repozytorium do folderu dedykowanego aplikacji:
`git clone https://github.com/paatrycjaa/apsi-project.git`
* `cd apsi-project`

## Uruchomienie lokalnie z docker-compose
Aby uruchomić serwer deweloperski wraz z konterenem z bazą danych MySQL, użyj polecenia:
```
(sudo) docker-compose up
```
Aby zakończyć działanie aplikacji i usunąć wszystkie utworzone przez nią elementy (włącznie z volume'ami), użyj polecenia:
```
docker-compose down -v
```

## Deployment
Aplikacja może być obsługiwana w wykorzystaniem dowolnych narzędzi, które współpracują z Django.

Sugerowanym rozwiązaniem jest jednak wykorzystanie:
 - [Gunicorn](https://gunicorn.org/) - serwera do obsługi połączenia z interfejsem aplikacji (WSGI)
 - [nginx](https://www.nginx.com/) - serwera webowego do obsługi reverse-proxy

Jeśli istnieje taka możliwość, polecanym rozwiązaniem jest również wykorzystanie platformy Kubernetes, z którą będzie można uruchomić i zarządzać przygotowanymi skonteneryzowanymi komponentami aplikacji.

