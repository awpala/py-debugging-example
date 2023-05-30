# Python Example: Simple Database Console Application

## Overview

See [here](https://docs.google.com/document/d/1dvYPF8IUaanns3J5ztvIPo4zxVkEcgolYpHni2NP28U/) for a step-by-step guide for debugging this application.

To run this application, issue the following terminal command from the top-level project directory (i.e., `/python-example`):
```bash
python main.py <filename> 
```
(where `<filename>` is the desired filename intended to store the database data, e.g., `users.txt`)

## Description of Files

| Filename | Description |
|:--|:--|
| `main.py` | contains the entrypoint of the application |
| `user.py` | defines the central entity ***user*** via corresponding class `User`, which in turn populates the constituent database |
| `database.py` | defines the class `Database` which performs create/read/update/delete (i.e., full "CRUD") operations |
| `utils.py` | defines helper utilities for parsing user inputs |
| `file_manager.py` | defines the class `FileManager` which performs file read/write operations on the underlying database file (e.g., `users.txt`), in order to persist the users in local memory between runs of the application |
