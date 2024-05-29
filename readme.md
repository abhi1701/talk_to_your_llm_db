# 📊 LLM-Powered SQL Query Generator & Natural Language Responder

Welcome to the **LLM-Powered SQL Query Generator & Natural Language Responder** project! This project leverages the power of Python, LangChain, OpenAI API, and MySQL to create an intelligent system that can answer natural language questions by generating and executing SQL queries, then presenting the results in a human-readable format.

## 🚀 Project Overview

This project demonstrates an end-to-end solution that integrates a language model with a SQL database to provide intelligent responses to user queries. The main components and their functions are as follows:

1. **User Input:** Users can ask questions in natural language through an interactive web interface.
2. **Schema Awareness:** The system utilizes the database schema to understand the structure of the data, ensuring the SQL queries are accurate and relevant.
3. **SQL Query Generation:** An LLM (Language Model) generates a SQL query based on the user's question and the database schema.
4. **Query Execution:** The generated SQL query is executed against a MySQL database to fetch the relevant data.
5. **Natural Language Response Generation:** The results of the SQL query are processed by another LLM to generate a natural language response.
6. **Interactive Interface:** The final response is displayed to the user through a user-friendly Streamlit app, making the interaction seamless and intuitive.

## 🛠️ Technologies Used

- **Python:** The main programming language used for scripting and integrating various components.
- **LangChain:** A framework for managing LLM chains and prompt templates.
- **OpenAI API:** Provides natural language understanding and generation capabilities.
- **MySQL:** The backend database for storing and retrieving data.
- **Streamlit:** A Python library used to create an interactive web application.

## 📂 Project Structure



## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.8+**
- **MySQL**
- **pip** (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/llm-sql-query-generator.git
    cd llm-sql-query-generator
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your MySQL database:**

    Ensure you have a MySQL database running. Update the database URI in the script with your database credentials:

    ```python
    db_uri = "mysql+mysqlconnector://<username>:<password>@<host>:<port>/<database>"
    ```

4. **Set your OpenAI API key:**

    Replace the placeholder API key with your actual OpenAI API key:

    ```python
    os.environ['OPENAI_API_KEY'] = "your-openai-api-key"
    ```

### Running the Application

To run the application, follow these steps:

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Open your web browser:**

    Once the Streamlit app is running, open your web browser and navigate to `http://localhost:8501`. You will see the interactive interface where you can enter natural language questions.

3. **Interact with the app:**

    Enter your question in the input field and submit it. The system will generate a SQL query, execute it on the MySQL database, and present the results in a natural language format.

## 📈 How It Works

### Detailed Workflow

1. **User Input:**
    - Users enter a question in natural language into the input field of the Streamlit app.

2. **SQL Query Generation:**
    - The system uses the provided database schema to help the LLM generate an appropriate SQL query that answers the user's question.

3. **Query Execution:**
    - The generated SQL query is executed on the MySQL database to fetch the relevant data.

4. **Natural Language Response:**
    - The raw results from the SQL query are processed by another LLM to convert them into a clear and concise natural language response.

5. **Response Presentation:**
    - The final natural language response is displayed to the user in the Streamlit app, making the interaction intuitive and user-friendly.

## 🎉 Features

- **Intelligent Query Generation:** Automatically generates accurate SQL queries based on natural language questions and database schema.
- **Natural Language Responses:** Converts SQL query results into clear and concise natural language responses.
- **Interactive Interface:** Provides a user-friendly interface for seamless interaction through Streamlit.
- **Schema Awareness:** Utilizes the database schema to enhance the accuracy and relevance of SQL query generation.

## 📝 Dependencies

The project relies on several Python packages, which are listed in the `requirements.txt` file. These include:

- **langchain:** For managing LLM chains and prompt templates.
- **langchain-core:** Core utilities for langchain.
- **langchain-community:** Community utilities for langchain.
- **langchain-openai:** OpenAI integration for langchain.
- **mysql-connector-python:** MySQL connector for Python.
- **streamlit:** For creating the interactive web application.

To install all the dependencies, run:

```bash
pip install -r requirements.txt
```

```plaintext
.
├── app.py               # Streamlit app code
├── main.py              # Main script to run the LLM and database integration
├── requirements.txt     # List of required Python packages
└── README.md            # Project README file
```