#!/usr/bin/python3
"""Initializes the models package by creating a unique FileStorage
instance for the application and reloading any previously saved
objects from the JSON file.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
