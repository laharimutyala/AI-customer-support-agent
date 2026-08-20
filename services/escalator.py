def should_escalate(issue: str):

    issue = issue.lower()

    escalation_keywords = [
        "angry",
        "lawsuit",
        "legal",
        "court",
        "fraud",
        "manager",
        "complaint"
    ]

    for keyword in escalation_keywords:
        if keyword in issue:
            return True

    return False