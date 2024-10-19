from flask import Flask, request, jsonify, render_template, redirect, url_for
from groq import Groq

app = Flask(__name__)

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homescreen')
def homescreen():
    return render_template('homescreen.html')

@app.route('/ai-consultation')
def ai_consultation():
    return render_template('ai-consultation.html')

@app.route('/myrecords')
def myrecords():
    return render_template('myrecords.html')

@app.route('/imagecap')
def imagecap():
    return render_template('imagecap.html')

@app.route('/contactdoc')
def contactdoc():
    return render_template('contactdoc.html')

@app.route('/api/login', methods=['POST'])
def login():
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    name = request.form.get('name')
    if mobile and password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 400

@app.route('/api/submit-symptoms', methods=['POST'])
def submit_symptoms():
    try:
        age = request.form.get('age')
        gender = request.form.get('gender')
        symptoms = request.form.get('symptoms')
        # Form the prompt using the inputs from the form
        prompt = f"""I am a doctor. My patient is a {age} year old {gender}. They have the following pre-medical history and symptoms: {symptoms}. Generate the response in about 80 grammatically correct words in the following format:
DISEASE: (Tell their disease name based on their pre-medical history, give just 1 disease found , age, and social habits. Just the name. If you really think there's no such disease, just say "I'm sorry, I need more information in order to determine the disease.")
Characteristics: (5-10 words)
SYMPTOMS: (If you really think there are no such symptoms for their condition, just say "I'm sorry, I need more information in order to determine accurate symptoms." Do the same if they answer "none" for current symptoms.) (10-15 words)

TREATMENT: (10-15 words. If there is no disease or symptoms, just say "Drink more water💧 it's never a bad idea!")
PRESCRIPTION: (About 10 words. You must tell the name of medicine only. You cannot answer "I cannot advise" or "go see a doctor." You must tell the medical drug name based on their age, medical history, and symptoms accurately. And also include the dosage of the tablet prescribed (in mg) .Please take the prescribed tablet "[NUMBER OF TIMES PER DAY] [BEFORE/AFTER] [MEAL]" (If there is no disease or symptoms, just say "Since there are no disease or symptoms, I cannot prescribe!"))
Leave a line after Disease, Symptoms, Treatment, and Prescription. Also, do the same for:
AYURVEDIC:
HOMEOPATHIC:
ALLOPATHIC:

Prescribe the tablet with dosage and number of times the tablet has to be taken and before meals or after meal for all Ayurvedic, Allopathic, Homeopathic, Do not give individual Disease treatment and all """
        # Make API call to get prediction
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama3-70b-8192",
            temperature=0.5,
            max_tokens=500,
            top_p=1,
            stream=False,
            stop=None
        )
        # Extract the AI's response
        ai_response = response.choices[0].message.content.strip()
        return jsonify({"response": ai_response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)