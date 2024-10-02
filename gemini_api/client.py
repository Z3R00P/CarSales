import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_car_ai_bio(model, brand, year):
    prompt = '''Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.'''.format(brand, model, year)
    genai.configure(api_key=os.getenv("GENAI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
