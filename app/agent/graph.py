from langgraph.graph import StateGraph, START, END

from app.agent.state import AgentState
from app.agent.retrieve import retrieve_context
from app.agent.analyze import analyze_incident


def build_graph():

    graph = StateGraph(AgentState)

    # Add nodes
    graph.add_node("retrieve", retrieve_context)
    graph.add_node("analyze", analyze_incident)

    # Define workflow
    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "analyze")
    graph.add_edge("analyze", END)

    return graph.compile()