## Run locally using Virtualenv

- Create a virtualenv: `python3 -m venv .venv` (only need to run once).
- Activate the virtualenv: `. .venv/bin/activate`
- Install requirements within virtualenv: `pip3 install -r requirements.txt` (only when requirements change)
- Deactivate virtualenv: `deactivate`

Run flask app:

```
export FLASK_APP=src.main
export FLASK_DEBUG=1
flask run
```

Visit http://localhost:5000 to view the app.

## Build and run

`docker build . -t web-app-demo`

`docker run -p 5000:5000 web-app-demo`

## Lint

`black src --check`

## Unit Tests

`python -m pytest`
