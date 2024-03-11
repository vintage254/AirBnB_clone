#!/usr/bin/python3
"""
This package represents a database structure using classes.

Modules:
    base_model: Defines the BaseModel class.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
