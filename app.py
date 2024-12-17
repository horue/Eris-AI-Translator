from flask import Flask, render_template, request
from langs import *
from api import *

from groq import Groq

client = Groq(
    api_key=key,
)

def use_ai(language, prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Translate for me the sentence to {language}: {prompt}. Just answer me with the translation. No '' needed. It must be the most human possible translation, like it was made by a native. Respect the given signals, like ! or ?",
            }
        ],
        model="llama3-8b-8192",
    )
    an = chat_completion.choices[0].message.content
    return an




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    final = "" 
    language = "English"  
    
    if request.method == 'POST':
        texto = request.form.get('texto_input')
        language = request.form.get('lang') 
        
        print(f"Texto recebido: {texto}")
        print(f"Idioma selecionado: {language}")
        
        if texto: 
            final = use_ai(language=language, prompt=texto)
        else:
            final = "Por favor, insira um texto válido."
    
  
    return render_template('index.html', texto=final, language=language)

if __name__ == '__main__':
    app.run(debug=True)
