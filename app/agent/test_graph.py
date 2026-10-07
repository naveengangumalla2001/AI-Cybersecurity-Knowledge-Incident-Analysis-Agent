from app.agent.graph import build_graph


agent = build_graph()


state = {
    "incident": """
    A web server received 5000 failed login attempts
    from multiple IP addresses within 10 minutes.
    """,

    "context": "",

    "analysis": {}
}


result = agent.invoke(state)


print("\nLangGraph Agent executed successfully!")

print("\nFinal Analysis:")
print(result["analysis"])