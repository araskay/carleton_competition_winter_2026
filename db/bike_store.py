"""
Bike Store Database Loader

Loads the Kaggle bike store dataset into a DuckDB database.
This provides the relational database for the SQL Query Writer Agent competition.

Dataset source: https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database
"""

import os
import duckdb
import kagglehub
from sqlalchemy import create_engine


class BikeStoreDb:
    """
    A class to download and load the bike store dataset into DuckDB.

    Attributes:
        db_path (str): Path to the DuckDB database file.
        download_path (str): Path where the dataset is downloaded.
    """

    def __init__(self, db_path='bike_store.db'):
        """
        Initialize the BikeStoreDb and create the database.

        Args:
            db_path (str): Path where the DuckDB database will be created.
                          Defaults to 'bike_store.db' in the current directory.
        """
        self.db_path = db_path
        self.download_path = self._download_data()
        self._create_db()

    @staticmethod
    def _download_data():
        """
        Download the latest version of the bike store dataset from Kaggle.

        Returns:
            str: Path to the downloaded dataset directory.
        """
        path = kagglehub.dataset_download("dillonmyrick/bike-store-sample-database")
        print(f"Downloaded dataset to {path}")
        return path

    def _create_db(self):
        """
        Create DuckDB tables from all CSV files in the downloaded dataset.

        Each CSV file becomes a table with the same name (without .csv extension).
        """
        con = duckdb.connect(database=self.db_path, read_only=False)
        csv_count = 0
        for fname in os.listdir(self.download_path):
            fpath = os.path.join(self.download_path, fname)
            if fname.lower().endswith(".csv"):
                csv_count += 1
                # Create a table name from the filename (without extension)
                table_name = os.path.splitext(fname)[0]

                # Create a DuckDB table by reading the CSV with automatic detection
                con.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS {table_name} AS
                    SELECT * FROM read_csv_auto('{fpath}');
                    """
                )
        con.close()
        print(f"Created {csv_count} tables in {self.db_path}")

    def get_engine(self):
        """
        Get a SQLAlchemy engine connected to the DuckDB database.

        Returns:
            sqlalchemy.engine.Engine: SQLAlchemy engine for database operations.
        """
        engine = create_engine(f"duckdb:///{self.db_path}")
        return engine


def get_schema_info(db_path='bike_store.db'):
    """
    Retrieve schema information for all tables in the database.

    Args:
        db_path (str): Path to the DuckDB database file.

    Returns:
        dict: Dictionary mapping table names to their column information.
    """
    con = duckdb.connect(database=db_path, read_only=True)

    # Get all table names
    tables = con.execute("SHOW TABLES").fetchall()

    schema_info = {}
    for (table_name,) in tables:
        # Get column information for each table
        columns = con.execute(f"DESCRIBE {table_name}").fetchall()
        schema_info[table_name] = [
            {"name": col[0], "type": col[1]} for col in columns
        ]

    con.close()
    return schema_info


if __name__ == "__main__":
    # Example usage: Initialize the database
    print("Initializing Bike Store Database...")
    db = BikeStoreDb()

    # Display schema information
    print("\nDatabase Schema:")
    print("-" * 50)
    schema = get_schema_info()
    for table, columns in schema.items():
        print(f"\nTable: {table}")
        for col in columns:
            print(f"  - {col['name']}: {col['type']}")
