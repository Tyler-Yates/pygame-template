# pygame-template

Template for pygame games

## Development

### Setup

You will need to create a virtual environment to develop or run this application:
```bash
virtualenv --python=python3.9 venv
source venv/bin/activate
```

Next, install the requirements:
```bash
pip install -Ur requirements.txt
```

### Tests and Code Style

This repo uses `tox` to run unit tests and perform code style cleanup and static analysis checks.

`tox` is not included in the requirements file so install it into the venv:
```bash
pip install tox
```

Then, simply run `tox`.

## Module Hierarchy

To avoid cyclical imports, there is a hierarchy of modules.
Modules should only import from modules lower than them on
this list.

```
controllers
frameprocessors
state
interfaces
util
constants
```

Thus, the `constants` module should not import any other modules.

## Game State

Game state is handled by a central dataclass.
Any state that should persist between play sessions should live in this class.
