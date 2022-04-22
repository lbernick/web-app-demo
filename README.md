## Using Virtualenv
Create a virtualenv: `python3 -m venv .venv` (only need to run once).
Using the virtualenv: `. .venv/bin/activate`
Install requirements within virtualenv: `pip3 install -r requirements.txt` (only when requirements change)
Deactivate virtualenv: `deactivate`

## Lint

`black app --check`

## Unit Tests

`python -m pytest`
