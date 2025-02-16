from langgraph.graph import StateGraph, START
from typing_extensions import TypedDict
from sql_utils import write_query, execute_query
from llm_model import llm

class State(TypedDict):
    question: str
    query: str
    result: str
    answer: str

def generate_answer(state: State):
    """Generate a response using SQL data or direct conversation."""
    if "answer" in state:
        # If a direct answer exists, return it
        return {"answer": state["answer"]}
    else:
        # Generate a response using SQL data
        prompt = (
            f"Given the following user question, corresponding SQL query, "
            f"and SQL result, answer the user question in human understandable form, no sql query no sql output,"
            f"and if you don;t have answer or can't find the appropriate reply just reply, i don;t have this information\n\n"
            f"Question: {state['question']}\n"
            f"SQL Query: {state['query']}\n"
            f"SQL Result: {state['result']}"
        )
        response = llm.invoke(prompt)
        return {"answer": response.content}

def build_chatbot_graph():
    """Builds and compiles the chatbot logic graph."""
    graph_builder = StateGraph(State).add_sequence(
        [write_query, execute_query, generate_answer]
    )
    graph_builder.add_edge(START, "write_query")
    return graph_builder.compile()
