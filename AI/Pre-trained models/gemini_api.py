from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Cual es la diferencia entre Artificial Intelligence y Machine Learning? (en cortas palabras)"
)

print(response.text)