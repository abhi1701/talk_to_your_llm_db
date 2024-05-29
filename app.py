import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = "sk-proj-7AiuD5zGPaGMGEIXt0WQT3BlbkFJ21RllAYfIKdEdj2xp4Yh"

# Initialize SQL Database
db_uri = "mysql+mysqlconnector://root:Microsoft#1234@localhost:3306/Chinook"
db = SQLDatabase.from_uri(db_uri)

# Function to retrieve schema
def get_schema(_):
    return db.get_table_info()

# Function to run SQL query
def run_query(query):
    return db.run(query)

# Initialize Language Learning Model (LLM)
llm = ChatOpenAI()

# Define Streamlit app
def main():
    st.title("Talk to your AI 🤖")
    
    # Get user question
    question = st.text_input("Ask any question about your sales:")

    # Execute full_chain when user hits submit
    if st.button("Submit"):
        # Define the SQL prompt
        sql_template = """
        Based on the table schema below, write a SQL query that would answer the user's question:
        {schema}

        Question: {question}
        SQL Query:
        """
        sql_prompt = ChatPromptTemplate.from_template(sql_template)

        # Define the full_chain prompt
        full_template = """
        Based on the table schema below, question, SQL query, and SQL response, write a natural language response:
        {schema}

        Question: {question}
        SQL Query: {query}
        SQL Response: {response}
        """
        full_prompt = ChatPromptTemplate.from_template(full_template)

        # Define SQL chain
        sql_chain = (
            RunnablePassthrough.assign(schema=get_schema)
            | sql_prompt
            | llm.bind(stop="\nSQL Result:")
            | StrOutputParser()
        )

        # Define full_chain
        full_chain = (
            RunnablePassthrough.assign(query=sql_chain).assign(
                schema=get_schema,
                response=lambda vars: run_query(vars["query"])
            )
            | full_prompt
            | llm
            | StrOutputParser()
        )

        # Invoke the full_chain with the user's question
        full_chain_output = full_chain.invoke({"question": question})

        # Retrieve the generated SQL query from the sql_chain
        sql_query = sql_chain.invoke({"question": question})

        # Display the SQL query and the final LLM response
        
        st.write("LLM Response:", full_chain_output)

if __name__ == "__main__":
    main()
