"""
SQL Query Writer Agent - Main Entry Point

This file provides an interactive interface for testing your QueryWriter agent.
Your agent implementation should be in agent.py.

Usage:
    python main.py

LLM Configuration:
    Set these environment variables to configure Ollama:
    - OLLAMA_HOST: Ollama server URL (default: http://localhost:11434)
    - OLLAMA_MODEL: Model to use (default: llama3.2)
"""

import os
import duckdb
from db.bike_store import BikeStoreDb
from agent import QueryWriter


def initialize_database(db_path: str = 'bike_store.db'):
    """
    Initialize the bike store database.
    Downloads data from Kaggle and creates DuckDB tables.
    """
    print("Initializing database...")
    db = BikeStoreDb(db_path=db_path)
    return db


def execute_query(sql: str, db_path: str = 'bike_store.db'):
    """
    Execute a SQL query against the DuckDB database.

    Args:
        sql (str): The SQL query to execute.
        db_path (str): Path to the DuckDB database.

    Returns:
        list: Query results as a list of tuples.
    """
    con = duckdb.connect(database=db_path, read_only=True)
    try:
        result = con.execute(sql).fetchall()
        return result
    finally:
        con.close()


def main():
    """
    Main function to run the SQL Query Writer Agent interactively.
    """
    db_path = 'bike_store.db'

    # Initialize the database
    initialize_database(db_path)

    # Initialize the QueryWriter agent
    print("Initializing QueryWriter agent...")
    agent = QueryWriter(db_path=db_path)

    # Show configuration
    print("\n" + "=" * 60)
    print("SQL Query Writer Agent - Interactive Mode")
    print("=" * 60)
    print(f"\nOllama Host: {os.getenv('OLLAMA_HOST', 'http://localhost:11434')}")
    print(f"Model: {os.getenv('OLLAMA_MODEL', 'llama3.2')}")
    print("\nDatabase loaded with the following tables:")
    for table_name in agent.schema.keys():
        print(f"  - {table_name}")
    print("\nType 'quit' or 'exit' to stop the agent.")
    print("=" * 60 + "\n")

    # Main interaction loop
    while True:
        try:
            # Get user input
            user_query = input("\nEnter your question: ").strip()

            if user_query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break

            if not user_query:
                continue

            # Generate SQL from natural language using the QueryWriter
            print("\nGenerating SQL query...")
            sql = agent.generate_query(user_query)
            print(f"\nGenerated SQL:\n{sql}")

            # Execute the query
            print("\nExecuting query...")
            results = execute_query(sql, db_path)

            # Display results
            print(f"\nResults ({len(results)} rows):")
            for row in results[:10]:  # Show first 10 rows
                print(row)
            if len(results) > 10:
                print(f"... and {len(results) - 10} more rows")

        except NotImplementedError as e:
            print(f"\nError: {e}")
            print("Please implement the generate_query method in agent.py!")
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
