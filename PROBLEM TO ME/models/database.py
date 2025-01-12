import sqlite3

class Database:
    def __init__(self, db_name="community_problems.db"):
        """
        Initializes the database connection and creates the table if it doesn't exist.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            location TEXT NOT NULL,
            reporter TEXT NOT NULL
        )
        '''
        self.execute_query(query)

    def execute_query(self, query, params=()):
        """
        Executes a query with optional parameters.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query):
        """
        Executes a query and fetches all results.
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
