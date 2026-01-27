"""
SQL Query Writer Agent

This file contains the QueryWriter class that generates SQL queries from natural language.
Implement your agent logic in this file.
"""

import os
from db.bike_store import get_schema_info


def get_ollama_client():
    """
    Get Ollama client configured for either Carleton server or local instance.

    Set OLLAMA_HOST environment variable to use Carleton's LLM server.
    Defaults to local Ollama instance.
    """
    import ollama
    host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
    return ollama.Client(host=host)


def get_model_name():
    """
    Get the model name from environment or use default.

    Set OLLAMA_MODEL environment variable to specify which model to use.
    """
    return os.getenv('OLLAMA_MODEL', 'llama3.2')


class QueryWriter:
    """
    SQL Query Writer Agent that converts natural language to SQL queries.

    This class is the main interface for the competition evaluation.
    You must implement the generate_query method.
    """

    def __init__(self, db_path: str = 'bike_store.db'):
        """
        Initialize the QueryWriter.

        Args:
            db_path (str): Path to the DuckDB database file.
        """
        self.db_path = db_path
        self.schema = get_schema_info(db_path=db_path)
        self.client = get_ollama_client()
        self.model = get_model_name()

        # TODO: Add any additional initialization here
        # For example:
        # - Set up prompt templates
        # - Initialize any additional components (e.g., LangChain agents)
        # - Load any additional resources

    def generate_query(self, prompt: str) -> str:
        """
        Generate a SQL query from a natural language prompt.

        This method is called by the evaluation system. It must:
        1. Accept a natural language question as input
        2. Return a valid SQL query string

        Args:
            prompt (str): The natural language question from the user.
                         Example: "What are the top 5 most expensive products?"

        Returns:
            str: A valid SQL query that answers the question.
                 Example: "SELECT product_name, list_price FROM products ORDER BY list_price DESC LIMIT 5"

        Note:
            - The query will be executed against the bike store DuckDB database
            - Return ONLY the SQL query, no explanations or markdown formatting
            - Handle edge cases gracefully (return a reasonable query or raise an exception)
        """
        # ============================================================
        # YOUR IMPLEMENTATION HERE
        # ============================================================
        #
        # Example implementation using Ollama directly:
        #
        # schema_text = self._format_schema()
        #
        # system_prompt = f"""You are a SQL expert. Given the following database schema:
        # {schema_text}
        #
        # Generate a SQL query to answer the user's question.
        # Return ONLY the SQL query, no explanations."""
        #
        # response = self.client.chat(
        #     model=self.model,
        #     messages=[
        #         {'role': 'system', 'content': system_prompt},
        #         {'role': 'user', 'content': prompt}
        #     ]
        # )
        # return response['message']['content'].strip()
        #
        # ============================================================

        raise NotImplementedError("Implement the generate_query method!")

    def _format_schema(self) -> str:
        """
        Format the database schema as a string for the LLM prompt.

        Returns:
            str: A formatted string representation of the database schema.
        """
        schema_parts = []
        for table_name, columns in self.schema.items():
            cols = ", ".join([f"{col['name']} ({col['type']})" for col in columns])
            schema_parts.append(f"Table {table_name}: {cols}")
        return "\n".join(schema_parts)
