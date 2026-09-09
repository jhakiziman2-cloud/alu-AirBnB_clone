# AirBnB Clone - The Console

## Description

This project is the first step towards building a full-stack clone
of the AirBnB web application. It implements a command interpreter
(a custom, limited "shell") used to manage the objects of the
application: `BaseModel`, `User`, `State`, `City`, `Amenity`,
`Place`, and `Review`.

The console allows you to:

* Create new objects (e.g. a new `User` or `Place`)
* Retrieve objects from a file
* Perform operations on objects (e.g. count, destroy)
* Update object attributes
* Destroy objects

Objects are serialized to and deserialized from a JSON file
(`file.json`) through a `FileStorage` engine, so data persists
between sessions.

## Data Flow

```
<class 'BaseModel'> <-> Dictionary <-> JSON string <-> file
```

Every class in the project inherits from `BaseModel`, which
implements the shared logic for object initialization, string
representation, and (de)serialization.

## Installation

1. Clone this repository.
2. No third-party dependencies are required; only the Python 3
   standard library is used.

## How to Start the Console

Run the console in interactive mode:

```
$ ./console.py
(hbnb)
```

Or in non-interactive mode:

```
$ echo "help" | ./console.py
```

## How to Use

The console understands the following commands:

| Command   | Usage                                                 | Description                                           |
|-----------|--------------------------------------------------------|---------------------------------------------------------|
| `help`    | `help [command]`                                       | Displays help about a command                           |
| `quit`    | `quit`                                                  | Exits the console                                        |
| `EOF`     | `EOF` (Ctrl+D)                                          | Exits the console                                        |
| `create`  | `create <class name>`                                   | Creates a new instance, saves it, and prints its `id`    |
| `show`    | `show <class name> <id>`                                 | Prints the string representation of an instance          |
| `destroy` | `destroy <class name> <id>`                              | Deletes an instance based on the class name and id       |
| `all`     | `all [<class name>]`                                     | Prints all string representations of all instances       |
| `update`  | `update <class name> <id> <attribute name> "<value>"`    | Updates an instance's attribute and saves the change      |

## Examples

```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', ...}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) quit
$
```

## Running the Tests

All unit tests live in the `tests/` directory and use the
`unittest` module. Run the full suite with:

```
$ python3 -m unittest discover tests
```

Or run a single test file:

```
$ python3 -m unittest tests/test_models/test_base_model.py
```

## Authors

See the [AUTHORS](AUTHORS) file for the list of contributors.
