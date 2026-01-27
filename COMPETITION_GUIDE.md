# SQL Query Writer Agent Competition

## Organized by MindBridge AI

Welcome to the SQL Query Writer Agent Competition! This competition challenges you to build an intelligent agent that can translate natural language questions into SQL queries for a relational database.

---

## Table of Contents

1. [Competition Overview](#competition-overview)
2. [Objectives](#objectives)
3. [LLM Access Options](#llm-access-options)
4. [Getting Started](#getting-started)
5. [Understanding Python Environments](#understanding-python-environments)
6. [Project Structure](#project-structure)
7. [Submission Requirements](#submission-requirements)
8. [How Your Code Will Be Evaluated](#how-your-code-will-be-evaluated)
9. [Database Schema](#database-schema)
10. [Tips and Resources](#tips-and-resources)
11. [FAQ](#faq)

---

## Competition Overview

Your task is to create an **AI-powered agent** that can:

1. Accept natural language questions from users (e.g., "What are the top 5 best-selling products?")
2. Understand the database schema and structure
3. Generate valid SQL queries that answer the user's question

### Required: Open Source Models via Ollama

For this competition, you **must use open source LLMs** through [Ollama](https://ollama.com/). You have two options for accessing these models:

1. **Carleton University LLM Server** (Recommended) - Access powerful models without local hardware requirements
2. **Local Ollama Installation** - Run models on your own machine

See the [LLM Access Options](#llm-access-options) section for detailed setup instructions.

---

## Objectives

### Primary Objective

Build a SQL Query Writer Agent that accurately translates natural language questions into executable SQL queries for the provided bike store database.

### Evaluation Criteria

Your submission will be evaluated on:

1. **Accuracy**: Does the generated SQL correctly answer the user's question?
2. **Robustness**: Can your agent handle various types of questions (aggregations, joins, filters, etc.)?
3. **Error Handling**: Does your agent gracefully handle invalid or ambiguous questions?
4. **Code Quality**: Is your code well-organized, documented, and maintainable?
5. **Innovation**: Creative approaches and novel solutions are encouraged!

---

## LLM Access Options

You have two options for accessing open source LLMs via Ollama. Choose the one that works best for you.

### Option 1: Carleton University LLM Server (Recommended)

Carleton's Research Computing Services provides access to a powerful LLM server with multiple open source models. This is the **recommended option** as it doesn't require local GPU resources.

#### How to Request Access

1. Go to [https://carleton.ca/rcs/llm-access/](https://carleton.ca/rcs/llm-access/)
2. Fill out the access request form with:
   - Your **Carleton University email** (required)
   - List of models you need
3. You will receive API endpoint details and authentication credentials

#### Using the Carleton Server

Once you have access, configure your environment:

```bash
# Set environment variables (add to .env file)
OLLAMA_HOST=<provided-server-url>
# Additional auth variables as provided by RCS
```

The Carleton server uses Ollama-compatible REST API endpoints, so you can use the standard `ollama` Python package:

```python
import ollama

# Configure client to use Carleton server
client = ollama.Client(host='<carleton-server-url>')

# Generate a response
response = client.chat(
    model='llama3.3',
    messages=[{'role': 'user', 'content': 'Write a SQL query to count all customers'}]
)
print(response['message']['content'])
```

### Option 2: Local Ollama Installation

If you prefer to run models locally or want to develop offline, you can install Ollama on your own machine.

#### System Requirements

- **macOS**: Apple Silicon (M1/M2/M3) recommended, Intel supported
- **Linux**: NVIDIA GPU recommended for larger models
- **Windows**: WSL2 with NVIDIA GPU support

#### Installation

**macOS/Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download from [https://ollama.com/download](https://ollama.com/download)

#### Pulling Models

After installation, pull the models you want to use:

```bash
# Pull a model (downloads it locally)
ollama pull llama3.2

# List available models
ollama list

# Run a model interactively (to test)
ollama run llama3.2
```

> **Note:** You are encouraged to explore different open source models available on [Ollama's model library](https://ollama.com/library). Different models have different strengths - experiment to find what works best for SQL generation tasks!

---

## Getting Started

### Prerequisites

Before starting, ensure you have:

1. **Python** installed on your system (we recommend Python 3.11+)
2. **Git** for version control
3. A **Kaggle account** (for downloading the dataset via kagglehub)
4. **LLM Access** - Either:
   - Access to Carleton's LLM server (request at [carleton.ca/rcs/llm-access](https://carleton.ca/rcs/llm-access/)), OR
   - Local Ollama installation (see [LLM Access Options](#llm-access-options))

### Setting Up Your Environment

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/araskay/carleton_competition.git
   cd carleton_competition
   ```

2. **Create a virtual environment** (see [Understanding Python Environments](#understanding-python-environments) below)

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Kaggle credentials** (required for downloading the dataset):
   - Go to [Kaggle](https://www.kaggle.com/) and sign in
   - Navigate to your account settings
   - Create a new API token (this downloads `kaggle.json`)
   - Place `kaggle.json` in `~/.kaggle/` (Linux/Mac) or `C:\Users\<username>\.kaggle\` (Windows)

5. **Run the template** to verify everything works:
   ```bash
   python main.py
   ```

---

## Understanding Python Environments

If you're new to Python development, this section explains virtual environments and package management.

### What is a Virtual Environment?

A virtual environment is an **isolated Python installation** that keeps your project's dependencies separate from other projects. This prevents conflicts between different projects that might need different versions of the same package.

### Why Use Virtual Environments?

- **Reproducibility**: Others can recreate your exact environment
- **Isolation**: Project dependencies don't conflict with each other
- **Clean Development**: Easy to start fresh if something goes wrong

### Creating a Virtual Environment

There are several tools for managing Python environments. Here are the most common:

#### Option 1: venv (Built into Python)

```bash
# Create a virtual environment
python -m venv myenv

# Activate it (Linux/Mac)
source myenv/bin/activate

# Activate it (Windows)
myenv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Deactivate when done
deactivate
```

#### Option 2: conda (Anaconda/Miniconda)

```bash
# Create environment with specific Python version
conda create -n myenv python=3.11

# Activate it
conda activate myenv

# Install packages
pip install -r requirements.txt

# Deactivate when done
conda deactivate
```

#### Option 3: pyenv (Advanced)

```bash
# Install specific Python version
pyenv install 3.11.9

# Create virtual environment
pyenv virtualenv 3.11.9 myenv

# Activate it
pyenv activate myenv

# Install packages
pip install -r requirements.txt
```

### Understanding requirements.txt

The `requirements.txt` file lists all Python packages your project needs. Each line specifies a package and its version:

```
package_name==1.2.3
```

The `==` ensures the **exact version** is installed, which is crucial for reproducibility.

#### How to Add Packages

1. **Install the package** in your virtual environment:
   ```bash
   pip install package_name
   ```

2. **Check the installed version**:
   ```bash
   pip show package_name
   ```

3. **Add to requirements.txt** with the exact version:
   ```
   package_name==X.Y.Z
   ```

#### Generating requirements.txt Automatically

You can generate a requirements.txt from your current environment:

```bash
pip freeze > requirements.txt
```

**Warning**: This includes ALL packages in your environment. It's often better to manually list only the packages you directly use, as indirect dependencies will be installed automatically.

### Understanding runtime.txt

The `runtime.txt` file specifies the **exact Python version** your project requires. The format is:

```
python-X.Y.Z
```

For example:
```
python-3.11.9
```

This ensures evaluators use the same Python version you developed with.

---

## Project Structure

Your submission should follow this structure:

```
your_submission/
├── runtime.txt          # Python version (REQUIRED)
├── requirements.txt     # Package dependencies (REQUIRED)
├── agent.py             # Your QueryWriter implementation (REQUIRED)
├── main.py              # Interactive testing interface (PROVIDED)
├── db/
│   ├── __init__.py
│   └── bike_store.py    # Database loader (PROVIDED)
└── src/                 # Additional source code (optional)
    ├── __init__.py
    └── ...
```

### Required Files

| File | Description |
|------|-------------|
| `runtime.txt` | Contains the Python version (e.g., `python-3.11.9`) |
| `requirements.txt` | Lists all package dependencies with exact versions |
| `agent.py` | Contains your `QueryWriter` class implementation |

### Provided Files

| File | Description |
|------|-------------|
| `main.py` | Interactive interface for testing your agent |
| `db/bike_store.py` | Downloads and loads the bike store dataset into DuckDB |

---

## Submission Requirements

### 1. Python Version (runtime.txt)

Create a `runtime.txt` file with your exact Python version:

```
python-3.11.9
```

To find your Python version:
```bash
python --version
# Output: Python 3.11.9
```

### 2. Dependencies (requirements.txt)

List ALL packages your project needs with **pinned versions**:

```
# Core dependencies (already included)
duckdb==1.1.3
sqlalchemy==2.0.36
kagglehub==0.3.4
ollama==0.4.7

# Add your additional dependencies below, for example:
# langchain==0.3.7
# langchain-ollama==0.2.3
```

**Important**:
- Use `==` for exact versions, not `>=` or `~=`
- Include ALL packages you import (directly or indirectly)
- Test your requirements.txt in a fresh environment before submitting

### 3. Agent Implementation (agent.py)

Your `agent.py` must contain a `QueryWriter` class with the following interface:

```python
class QueryWriter:
    def __init__(self, db_path: str = 'bike_store.db'):
        """
        Initialize the QueryWriter.

        Args:
            db_path (str): Path to the DuckDB database file.
        """
        # Your initialization code here
        pass

    def generate_query(self, prompt: str) -> str:
        """
        Generate a SQL query from a natural language prompt.

        Args:
            prompt (str): The natural language question.
                         Example: "What are the top 5 most expensive products?"

        Returns:
            str: A valid SQL query that answers the question.
                 Example: "SELECT product_name, list_price FROM products ORDER BY list_price DESC LIMIT 5"
        """
        # Your implementation here
        pass
```

**Important Requirements:**
- The `generate_query` method must accept a natural language prompt and return a SQL query string
- Return ONLY the SQL query, no explanations or markdown formatting
- The returned query must be valid SQL that can be executed against the bike store database

### 4. Code Organization

- Keep your code clean and well-documented
- Use meaningful variable and function names
- Handle errors gracefully
- You may add additional helper methods or classes to `agent.py`
- You may create additional files in a `src/` directory if needed

---

## How Your Code Will Be Evaluated

### Environment Setup

Your submission will be set up using the following process:

```bash
# Read Python version from runtime.txt
PYTHON_VERSION=$(cut -d- -f2 runtime.txt)

# Create virtual environment (using pyenv)
pyenv install -s $PYTHON_VERSION
pyenv virtualenv $PYTHON_VERSION submission-env
pyenv activate submission-env

# Install dependencies
pip install -r requirements.txt
```

### Evaluation Process

Your `QueryWriter` class will be evaluated against a **hidden evaluation dataset** containing natural language prompts and expected SQL queries. The evaluation will:

1. Import your `QueryWriter` class from `agent.py`
2. Initialize it with the bike store database
3. Call `generate_query()` with various natural language prompts
4. Compare the results of executing your generated queries against expected results

```python
# Example of how your agent will be evaluated
from agent import QueryWriter

agent = QueryWriter(db_path='bike_store.db')

# For each prompt in the evaluation dataset:
generated_sql = agent.generate_query("What are the top 5 most expensive products?")
# Execute and compare results...
```

**Note:** The evaluation dataset is not available to students. Design your agent to handle a variety of question types.

### What This Means for You

1. **Test in a clean environment**: Before submitting, create a fresh virtual environment and verify your code runs with only the packages in `requirements.txt`

2. **Pin all versions**: Unpinned dependencies might install different versions, breaking your code

3. **Don't rely on global packages**: If it's not in `requirements.txt`, assume it won't be available

4. **Test your QueryWriter class**: Make sure your `generate_query` method works correctly with various types of questions

5. **Use `main.py` for testing**: Run `python main.py` to interactively test your agent during development

---

## Database Schema

The bike store database is sourced from the [Bike Store Sample Database](https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database) on Kaggle. It contains the following tables:

### Tables Overview

| Table | Description |
|-------|-------------|
| `brands` | Bicycle brands |
| `categories` | Product categories |
| `customers` | Customer information |
| `order_items` | Individual items in orders |
| `orders` | Customer orders |
| `products` | Products available for sale |
| `staffs` | Store staff members |
| `stocks` | Inventory levels by store |
| `stores` | Store locations |

### Exploring the Schema

Run the database loader to see the full schema:

```bash
python -c "from db.bike_store import BikeStoreDb, get_schema_info; BikeStoreDb(); print(get_schema_info())"
```

Or use the helper function in your code:

```python
from db.bike_store import get_schema_info

schema = get_schema_info()
for table, columns in schema.items():
    print(f"\nTable: {table}")
    for col in columns:
        print(f"  - {col['name']}: {col['type']}")
```

---

## Tips and Resources

### Tips for Success

1. **Start Simple**: Get a basic prompt working before adding complexity
2. **Test Incrementally**: Test your agent with various types of questions
3. **Provide Schema Context**: LLMs need to know the database structure to write correct SQL
4. **Handle Errors**: Not every question can be answered - handle these gracefully
5. **Validate SQL**: Consider validating generated SQL before execution

### Example Questions to Test

- "How many customers are there?"
- "What are the top 5 most expensive products?"
- "Show me all orders from 2018"
- "Which store has the most inventory?"
- "What is the total revenue by brand?"
- "List all staff members and their stores"

### Useful Resources

**Example Implementations:**
- [Query Writer Agent Example](https://github.com/araskay/query_writer_agent) - A reference implementation of a SQL query writer agent
- [Agentic Design Patterns](https://github.com/araskay/agentic_patterns) - Overview of common agentic design patterns

**Documentation:**
- [DuckDB Documentation](https://duckdb.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Ollama Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Ollama Python Library](https://github.com/ollama/ollama-python)
- [LangChain SQL Agent](https://python.langchain.com/docs/tutorials/sql_qa/)
- [LangChain Ollama Integration](https://python.langchain.com/docs/integrations/llms/ollama/)
- [Carleton LLM Access](https://carleton.ca/rcs/llm-access/)

---

## FAQ

### Q: Which LLM models can I use?

**A**: You must use **open source models via Ollama**. You can access these through the Carleton University LLM server or by running Ollama locally. See [LLM Access Options](#llm-access-options) for details.

### Q: Can I use OpenAI, Anthropic, or other commercial APIs?

**A**: No. This competition requires the use of open source models through Ollama. This ensures a level playing field and gives you experience with self-hosted LLM solutions.

### Q: What if I don't have a powerful GPU?

**A**: Use the Carleton University LLM server! It provides access to large models (up to 235B parameters) without requiring local hardware. Request access at [carleton.ca/rcs/llm-access](https://carleton.ca/rcs/llm-access/).

### Q: How do I configure my code for evaluation?

**A**: Use environment variables for the Ollama host and model name. This allows evaluators to easily point your code at their infrastructure. See the "Making Your Code Flexible" section under [LLM Access Options](#llm-access-options).

### Q: Can I add additional files?

**A**: Yes! You can organize your code however you like. Just ensure `agent.py` contains your `QueryWriter` class and all imports work correctly.

### Q: What if the dataset download fails?

**A**: Ensure you have valid Kaggle credentials set up. See the [Getting Started](#getting-started) section.

### Q: Can I use a different database?

**A**: No. All submissions must use the provided bike store database in DuckDB to ensure fair evaluation.

### Q: How do I know what Python version I have?

**A**: Run `python --version` in your terminal.

### Q: My code works but fails during evaluation. Why?

**A**: Common issues:
- Missing packages in `requirements.txt`
- Unpinned package versions
- Relying on packages installed globally but not listed
- Hardcoded file paths that only work on your machine

---

## Need Help?

If you have questions about the competition:

1. Check this guide and the FAQ first
2. Review the provided template code
3. Post your question in the Discord channel
4. Contact **Dr. Aras Kayvan** at [aras.kayvan@mindbridge.ai](mailto:aras.kayvan@mindbridge.ai)

Good luck and happy coding!

---

*Organized by MindBridge AI*
