from langchain import hub
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from typing_extensions import TypedDict, Annotated
from db_connection import db
from llm_model import llm

class QueryOutput(TypedDict):
    """Generated SQL query."""
    query: Annotated[str, ..., "Syntactically valid SQL query."]

query_prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")

def is_sql_query(question):
    """Determine if the question requires an SQL query or not."""
    keywords = ["show", "fetch", "retrieve", "get", "list", "display", "query", "data", "table"]
    return any(keyword in question.lower() for keyword in keywords)

def write_query(state):
    """Decide whether to generate an SQL query or just respond conversationally."""
    question = state["question"]

    if is_sql_query(question):
        # Generate SQL Query if question is database-related
        prompt = query_prompt_template.invoke({
            "dialect": db.dialect,
            "top_k": 10,
            "table_info": db.get_table_info(),
            "input": question,
        })
        structured_llm = llm.with_structured_output(QueryOutput)
        result = structured_llm.invoke(prompt)
        return {"query": result["query"]}
    else:
        # Let LLaMA 3 respond conversationally
        response = llm.invoke(f"You're a friendly assistant. Answer the user: {question}")
        return {"answer": response.content}

def execute_query(state):
    """Execute SQL query if one was generated."""
    if "query" in state:
        execute_query_tool = QuerySQLDatabaseTool(db=db)
        return {"result": execute_query_tool.invoke(state["query"])}
    return state  # If no query, return unchanged state
