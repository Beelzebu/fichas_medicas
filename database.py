# -*- coding: utf-8 -*-
import sqlite3


class Serializable:

    def query(self) -> str:
        """Query to insert this object to the database"""
        pass

    def values(self) -> tuple:
        """Values from this object to replace in the query"""
        pass

    def save(self) -> None:  # TODO: get database instance and execute query
        pass


class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        """Function to create connection to database and create default tables"""
        pass

    def save(self, entity: Serializable):
        """Function to save `fichas` on the database"""
        pass

    def find_one(self, ficha_id: int):
        """Fetch the document that matches with the provided id or None if not found"""
        pass

    def find_all(self) -> []:
        """Fetch all documents from the database and return them as a list"""
        pass


class SQLiteDatabase(Database):

    def __init__(self):
        super().__init__()

    def connect(self):
        self.connection = sqlite3.connect('local.db').cursor()
        # TODO: create tables

    def save(self, entity: Serializable):
        if not isinstance(entity, Serializable):
            raise ValueError("object is not an instance of Serializable")
        self.connection.execute(entity.query(), entity.values())


class MySQLDatabase(Database):

    def __init__(self):
        super().__init__()

    def connect(self):
        pass

    def save(self, entity: Serializable):
        pass
