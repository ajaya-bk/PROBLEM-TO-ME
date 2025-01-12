from models.base_model import BaseModel
from models.database import Database

class Problem(BaseModel):
    """
    Problem class representing a community problem.
    Inherits from BaseModel to demonstrate inheritance.
    """
    db = Database() # Shared database instance for all problems.

    def __init__(self, title, description, location, reporter):
        """
        Initialize a new Problem instance with the given details.
        """
        self.title = title
        self.description = description
        self.location = location
        self.reporter = reporter

    def save(self):
        """
        Save the problem details to the database.
        """
        query = "INSERT INTO problems (title, description, location, reporter) VALUES (?, ?, ?, ?)"
        Problem.db.execute_query(query, (self.title, self.description, self.location, self.reporter))

    @staticmethod
    def fetch_all():
        """
        Fetch all problems from the database.
        """
        query = "SELECT * FROM problems"
        return Problem.db.fetch_all(query)
