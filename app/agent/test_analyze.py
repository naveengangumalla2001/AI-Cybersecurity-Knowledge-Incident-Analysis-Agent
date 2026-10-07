from app.agent.analyze import analyze_incident


state = {
    "incident": """
    A web server received 5000 failed login attempts
    from multiple IP addresses within 10 minutes.
    """,

    "context": """
    # Brute Force Attack

    A brute force attack is an authentication attack
    in which an attacker repeatedly attempts to gain
    access to an account or service.

    Common indicators include:
    - Large number of failed login attempts
    - Repeated authentication attempts
    - Multiple IP addresses targeting accounts

    Defensive measures include:
    - Rate limiting
    - Multi-Factor Authentication
    - Monitoring authentication logs
    """,

    "analysis": {}
}


result = analyze_incident(state)

print("\nAnalyze node executed successfully!")

print("\nAnalysis:")
print(result["analysis"])