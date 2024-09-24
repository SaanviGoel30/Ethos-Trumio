import openai

openai.api_key = "your_api_key"
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text
