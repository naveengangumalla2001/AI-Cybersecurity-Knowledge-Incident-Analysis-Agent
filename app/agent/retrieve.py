from app.agent.state import AgentState
from app.rag.retriever import get_retriever


def retrieve_context(state: AgentState):

    incident = state["incident"]

    retriever = get_retriever()

    documents = retriever.invoke(incident)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return {
        "context": context
    }