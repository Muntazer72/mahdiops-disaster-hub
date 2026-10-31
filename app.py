from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Snowflake Infrastructure & Mock Data Simulation
SNOWFLAKE_REGIONS = [
    {"region": "Multan Central", "infrastructure_status": "High Risk", "road_blocked": True, "water_supply": "Compromised"},
    {"region": "BZU Sector 4", "infrastructure_status": "Moderate", "road_blocked": False, "water_supply": "Stable"},
    {"region": "Industrial Zone", "infrastructure_status": "Critical", "road_blocked": True, "water_supply": "Failed"}
]

# Solana Agent Registry Simulation
SOLANA_AGENTS = [
    {"agent_id": "MahdiOps-Node-72", "status": "Verified & Active", "uptime": "99.9%", "network": "Solana Mainnet-Beta"},
    {"agent_id": "Disaster-Relief-Bot-01", "status": "Synchronized", "uptime": "98.5%", "network": "Solana Devnet"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis_result = None
    selected_region = "Multan Central"
    
    if request.method == 'POST':
        selected_region = request.form.get('region', 'Multan Central')
        language = request.form.get('language', 'en')
        
        # Handle file upload for Gemma / Gemini multimodal assessment
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != '':
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Simulated Multi-lingual AI Analysis Response based on Challenge 1 requirements
                if language == 'ur':
                    analysis_result = f"🚨 ہنگامی تجزیہ (AI): علاقہ '{selected_region}' میں سڑکیں بند ہیں اور فوری امداد کی ضرورت ہے۔ تصویر کی بنیاد پر خطرے کی سطح: شدید (Critical)۔"
                elif language == 'ru':
                    analysis_result = f"🚨 Экстренный анализ (AI): В регионе '{selected_region}' зафиксированы повреждения инфраструктуры. Уровень угрозы: Высокий."
                else:
                    analysis_result = f"🚨 Gemma AI Triage Report: Region '{selected_region}' shows severe structural impact and bridge obstruction. Priority Level: HIGH. Immediate dispatch required."

    return render_template('index.html', 
                           analysis_result=analysis_result, 
                           regions=SNOWFLAKE_REGIONS, 
                           agents=SOLANA_AGENTS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
