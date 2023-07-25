I use this repo for testing CI/CD.

## Build and run locally

- Create a virtualenv: `python3 -m venv .venv` (only need to run once).
- Activate the virtualenv: `. .venv/bin/activate`
- Install requirements within virtualenv: `pip3 install -r requirements.txt` (only when requirements change)
- Deactivate virtualenv (when done using it): `deactivate`

### Run flask app

```
export FLASK_APP=src.main
export FLASK_DEBUG=1  # hot-reloads application when code changes 
flask run
```

Flask defaults to port 5000. You can select a different port with `flask run -p <port>`.

Visit http://localhost:5000 to view the app.

Start up the database in the background and forward the container port 6379 to the host port 6379:

`docker run -d -p 6379:6379 redis`

### Lint

Within virtualenv: `black src --check`

### Unit Tests

Within virtualenv: `python -m pytest ./src`

### Integration Tests

Within virtualenv: `python -m pytest ./test`

## Build and run with Docker

Build the repo and tag the resulting image with "web-app-demo:latest":

`docker build . -t web-app-demo`

Create a network named "web-app-demo" to allow the app container to connect to the database container:

`docker network create web-app-demo`

Start up the database container named "database", connect it to the web-app-demo network, and expose its port 6379:

`docker run -d -p 6379:6379 --network web-app-demo --name database redis`

Run the image in a container named "web-app-demo-container", connect it to the web-app-demo network,
expose its port 5000, and tell it how to reach the database container:

`docker run -p 5000:5000 --name web-app-demo-container --network web-app-demo -e REDIS_HOST=database web-app-demo`

Note: the REDIS_HOST environment variable must match the container name used for the database.
This will not work for generated container names.

### Lint

`docker run web-app-demo black src --check`

If the container is already running (with container name "web-app-demo-container"),
lint can also be executed with `docker exec`:

`docker exec web-app-demo-container black src --check`

### Unit Tests

`docker run web-app-demo python -m pytest ./src`

If the container is already running (with container name "web-app-demo-container"),
unit tests can also be executed with `docker exec`:

`docker exec web-app-demo-container python -m pytest ./src`

## Build and run with docker compose

Start the database and web app: `docker-compose up`

Note: This does not allow changing the ports these applications run on.

To delete the running containers and docker network: `docker-compose down`

Note: killing the process running `docker-compose up` stops the containers but does not delete them.

### Integration tests

After running `docker-compose up`, integration tests can be run within the virtualenv:

`python -m pytest ./test`

## Interact with database

Requires [installing redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)

```
$ redis-cli -p 6379
127.0.0.1:6379> monitor
OK
```

## Endpoints

- Get some friendly greetings at /
- Check app status at /statusz
- View supported animals at /animals
- Get an animal noise at /animals/<animal_name>
- Get the page hit count at /hits (requires database)
