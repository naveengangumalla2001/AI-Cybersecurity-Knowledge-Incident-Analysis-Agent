from app.agent.retrieve import retrieve_context


state = {
    "incident": """
    A web server received 5000 failed login attempts
    from multiple IP addresses within 10 minutes.
    """,
    "context": "",
    "analysis": {}
}


result = retrieve_context(state)

print("\nRetrieve node executed successfully!")

print("\nRetrieved Context:")
print(result["context"])