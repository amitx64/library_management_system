import sqlite3
from sqlite3 import Error


class DBconnection:
    def __init__(self):
        self.database = "LMS.db"
        self.sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                                sname text,
                                                phone text,
                                                fname text,
                                                student_id text NOT NULL PRIMARY KEY
                                            ); """

        self.sql_create_books_table = """ CREATE TABLE IF NOT EXISTS books (
                                                        bname text,
                                                        aname text,
                                                        category text,
                                                        book_id text NOT NULL PRIMARY KEY
                                                    ); """

        self.sql_create_issue_book_table = """ CREATE TABLE IF NOT EXISTS issued (
                                                                    book_id text PRIMARY KEY,
                                                                    student_id text,
                                                                    FOREIGN KEY(book_id) REFERENCES book(book_id)
                                                                    FOREIGN KEY(student_id) REFERENCES book(student_id)
                                                                ); """

        # create a database connection
        self.conn = self.create_connection(self.database)

        # create tables
        if self.conn is not None:
            # create projects table
            self.create_table(self.conn, self.sql_create_students_table)
            self.create_table(self.conn, self.sql_create_books_table)
            self.create_table(self.conn, self.sql_create_issue_book_table)
        else:
            print("Error! cannot create the database connection.")

    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    @staticmethod
    def create_table(conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)