Required Packages:

- > flask
- > flask-marshmallow
- > keras v2.2.5
- > tensorflow v1.14

Pipfile is already present. Only thing to do is install dependencies using:

If virtual environment is not activated:

pipenv install or pipenv install --dev

If virtual environment is already activated:

pipenv sync or pipenv sync --dev

Once the packages are installed, just run:

python app.py

This will start local server.
