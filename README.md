## Run locally using Virtualenv

- Create a virtualenv: `python3 -m venv .venv` (only need to run once).
- Activate the virtualenv: `. .venv/bin/activate`
- Install requirements within virtualenv: `pip3 install -r requirements.txt` (only when requirements change)
- Deactivate virtualenv: `deactivate`

## Build and run

`docker build . -t web-app-demo`

`docker run web-app-demo --animal_name="dolly" --animal_type="sheep"`

## Lint

`black src --check`

## Unit Tests

`python -m pytest`
