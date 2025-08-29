import openai

# Example prompt
prompt = "Write a short story about AI"

# Temperature settings
temperatures = [0.1, 0.5, 0.9]

for temp in temperatures:
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=temp
    )
    print(f"\nTemperature: {temp}")
    print(response.choices[0].message['content'])
