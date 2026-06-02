from google import genai

client = genai.Client(
    api_key= "Your API key"
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in short"
)
print(response.text)
