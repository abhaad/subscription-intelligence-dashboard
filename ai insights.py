import google.generativeai as genai

# 🔑 Add your API key here
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

def generate_insight(total_spend, waste_amount):
    prompt = f"""
    Analyze this subscription data:
    Total Spend: ₹{total_spend}
    Waste Amount: ₹{waste_amount}

    Give a short actionable insight.
    """

    response = model.generate_content(prompt)
    return response.text


# Example test
if __name__ == "__main__":
    insight = generate_insight(8000, 2350)
    print(insight)
