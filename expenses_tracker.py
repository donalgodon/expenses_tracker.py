def expense_tracker(expenses, budget, limit):
    total_expenses = sum(amount for _, amount in expenses)
    average_expense = total_expenses / len(expenses) if expenses else 0
    max_expense = max(expenses, key=lambda x: x[1])[1] if expenses else 0

    alert_message = f"Alert! You have exceeded the spending limit of {limit}." if total_expenses > limit else "Within the limit."
    recommendation = f"You exceeded your budget by {total_expenses - budget}." if total_expenses > budget else "Within the budget."

    return {
        "Total": total_expenses,
        "Average": average_expense,
        "Maximum": max_expense,
        "Alert": alert_message,
        "Recommendation": recommendation
    }

# Example usage
expenses_list = [("Food", 50), ("Transport", 20), ("Entertainment", 30)]
budget = 100
limit = 80

result = expense_tracker(expenses_list, budget, limit)
for key, value in result.items():
    print(f"{key}: {value}")
