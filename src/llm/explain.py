from openai import OpenAI
client = OpenAI()

def generate_explanation(commodity, market, date, actual, expected, deviation):
    prompt = f"""
    Explain simply why the price of {commodity} in {market} on {date}
    deviated by {deviation:.2f}%. 
    Actual price: {actual}. Expected price: {expected}.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
