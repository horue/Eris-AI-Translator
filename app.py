from flask import Flask, render_template, request, send_file
from langs import *
from api import *
from gtts import *
import os

from groq import Groq

client = Groq(
    api_key=key,
)

def use_ai(language, prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Translate the following sentence to {language}: {prompt}. Just answer with the translation. It must be the most natural and human translation possible, as if made by a native speaker. Respect the punctuation marks like ! or ?. Just answer the translation, direct to the point."
            }
        ],
        model="gemma2-9b-it",
    )
    an = chat_completion.choices[0].message.content
    return an




app = Flask(__name__)

# Mapeamento de idiomas
language_map = {
    "Español": "es",
    "English": "en",
    "Japanese": "ja",
    "German": "de"
}

@app.route('/', methods=['GET', 'POST'])
def home():
    final = ""
    language = "English"
    if request.method == 'POST':
        texto = request.form.get('texto_input')
        language = request.form.get('lang')

        if texto:
            final = use_ai(language=language, prompt=texto)
        else:
            final = "Por favor, insira um texto válido."
    
    return render_template('index.html', texto=final, language=language)


@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    texto = request.form.get('texto_input')
    language = request.form.get('lang')

    if texto:        
        # Definir o nome do arquivo de áudio
        tts_audio_file = f"audio/{texto}_tts.mp3" 
        tts = gTTS(text=texto, lang=language_map.get(language, "en"))
        r = tts.save(tts_audio_file)
        
        return r
    else:
        return "Erro: Texto não encontrado", 400

@app.route('/audio/<filename>')
def play_audio():
    filename = generate_audio()
    return send_file(f'audio/{filename}', as_attachment=True)


@app.route('/models_test')
def models_test():
    return render_template('models_test.html')

@app.route('/', methods=['GET', 'POST'])
def models():
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
    if not os.path.exists('audio'):
        os.makedirs('audio')
    app.run(debug=True)
