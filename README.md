## Build and run locally

- Create a virtualenv: `python3 -m venv .venv` (only need to run once).
- Activate the virtualenv: `. .venv/bin/activate`
- Install requirements within virtualenv: `pip3 install -r requirements.txt` (only when requirements change)
- Deactivate virtualenv (when done using it): `deactivate`

Run flask app:

```
export FLASK_APP=src.main
export FLASK_DEBUG=1  # hot-reloads application when code changes 
flask run
```

Visit http://localhost:5000 to view the app.

### Lint

Within virtualenv: `black src --check`

### Unit Tests

Within virtualenv: `python -m pytest`

## Build and run with Docker

Build the repo and tag the resulting image with "web-app-demo:latest":

`docker build . -t web-app-demo`

Run the image in a container named "web-app-demo-container", and forward the container port
5000 to the host port 5000:

`docker run -p 5000:5000 --name web-app-demo-container web-app-demo`

### Lint

`docker run web-app-demo black src --check`

If the container is already running (with container name "web-app-demo-container"),
lint can also be executed with `docker exec`:

`docker exec web-app-demo-container black src --check`

### Unit Tests

`docker run web-app-demo python -m pytest`

If the container is already running (with container name "web-app-demo-container"),
unit tests can also be executed with `docker exec`:

`docker exec web-app-demo-container python -m pytest`

