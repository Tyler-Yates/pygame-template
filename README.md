# pygame-template

Template for pygame games

## Module Hierarchy

To avoid cyclical imports, there is a hierarchy of modules.
Modules should only import from modules lower than them on
this list.

```
controllers
frameprocessors
scenes
state
interfaces
util
```

Thus, the `util` module should not import any other modules.

## Game State

Game state is handled by a central dataclass.
Any state that should persist between play sessions should live in this class.
