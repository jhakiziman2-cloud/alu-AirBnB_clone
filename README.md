# **AirBnB Clone - The Console**

## **Description**

This project is the first step in building an AirBnB clone. The goal of this project is to create a command-line interpreter that can be used to manage AirBnB objects.

The command interpreter will allow users to create, retrieve, update, and destroy objects. It will also provide a simple way to manage the data used by the application.

The project is built using Python and introduces important concepts such as:

* Python packages
* Object-oriented programming
* Serialization and deserialization
* JSON files
* UUIDs
* Datetime
* Unit testing
* Command interpreters
* *args and **kwargs

### **Command Interpreter**

The command interpreter is a program that provides an interactive command-line interface for managing objects in the AirBnB application.

It works similarly to a shell, but instead of executing general operating-system commands, it executes commands specifically designed for this project.

### **How to Start It**

First, make sure the *console.py* file is executable:


*chmod +x console.py*


Then start the console with:

*bash*
./console.py


You should see:


*(hbnb)*


 *How to Use It*

Once the console is running, commands can be entered at the `(hbnb)` prompt.

For example:

*$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$


You can also use **help** to display information about available commands:


*(hbnb)* help


To exit the console:


*(hbnb)* quit


### **Non-Interactive Mode**

The console can also be used in non-interactive mode by piping commands into it.

For example:

*bash*
echo "help" | ./console.py


You can also place commands inside a file:

help
quit


Then run:


*cat test_help | ./console.py*


## **Project Structure**

The project will contain Python modules, models, storage, and tests as development continues.

An example of the project structure is:

```
alu-AirBnB_clone/
│
├── console.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   └── ...
│
├── tests/
│   └── ...
│
├── README.md
└── AUTHORS
```

### **Testing**

Unit tests are written using Python's unittest module.

To run all tests:

*python3 -m unittest discover tests


A specific test file can also be executed:


*python3 -m unittest tests/test_models/test_base_model.py


### **Authors**

This project is a team project. All contributors are listed in the AUTHORS file.

