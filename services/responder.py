def generate_response(category: str):

    responses = {
        "refund":
            "We apologize for the inconvenience. Refunds usually take 5 business days. Our support team is reviewing your request.",

        "shipping":
            "Your shipment is being reviewed. Please allow 24 hours for an update.",

        "account":
            "Please try resetting your password. If the issue persists, our support team will assist you.",

        "technical":
            "We are sorry for the inconvenience. Our technical team is investigating the issue.",

        "other":
            "Thank you for contacting support. Our team will get back to you shortly."
    }

    return responses.get(category, responses["other"])