def classify_ticket(issue: str):

    issue = issue.lower()

    if "refund" in issue:
        return "refund"

    elif "order" in issue or "shipping" in issue:
        return "shipping"

    elif "login" in issue or "password" in issue:
        return "account"

    elif "error" in issue or "crash" in issue:
        return "technical"

    return "other"