#!/usr/bin/python3
"""Reloads file storage""
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
