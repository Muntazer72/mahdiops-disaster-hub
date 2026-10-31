from flask import Flask, render_template, request, redirect, url_for
import os
import google.generativeai as genai
from PIL import Image

app = Flask(__name__)

# Apni Gemini API Key yahan dal dena
genai.configure(api_key="YAHAN_APNI_GEMINI_API_KEY_DAL_DENA")

# Uploads folder setup
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# In-memory list for hackathon demo items
found_items = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form.get('location')
        file = request.files.get('image')
        
        if file and file.filename != '':
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Gemini Multimodal AI Call
            try:
                img = Image.open(filepath)
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                prompt = "Analyze this lost or found item image and give a professional, short 1-line title and description of the item."
                response = model.generate_content([prompt, img])
                ai_description = response.text
            except Exception as e:
                ai_description = "Item reported successfully. AI analysis pending."

            # Add to top of list
            found_items.insert(0, {
                'location': location,
                'image': filename,
                'details': ai_description
            })
            
            return redirect(url_for('index'))

    return render_template('index.html', items=found_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
