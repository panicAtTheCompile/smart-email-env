TASKS = [
    {
        "name": "classification_easy",
        "email": "Meeting rescheduled to tomorrow at 3 PM.",
        "label": "normal"
    },
    {
        "name": "extraction_medium",
        "email": "Please send the report by 5th April. It's urgent.",
        "expected": {
            "date": "5th April",
            "priority": "high"
        }
    },
    {
        "name": "response_hard",
        "email": "I have not received my refund yet. Please check.",
        "expected_response": "apology + refund status"
    }
]