from groq import Groq
import base64

# Initialize Groq client
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

def generate_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # Changed to an available Groq model
            messages=[{"role": "system", "content": prompt}],
            max_tokens=1000,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return "I'm sorry, I encountered an error while processing your request."

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def handle_user_input():
    age = input("Please enter your age: ")
    gender = input("Please enter your gender: ")
    image_path = input("Please enter the path to your image file: ")

    try:
        encoded_image = encode_image(image_path)
    except Exception as e:
        print(f"Error reading image file: {e}")
        return

    prompt = f"""You are given a patient who is facing a disease shown in the provided image. The patient is {age}.

Possible Disease Detected: (List the possible diseases based on the image.)

CHARACTERISTICS: (5-10 words describing key features of the disease.)

SYMPTOMS: (10-15 words listing common symptoms associated with the disease.)

TREATMENTS:

Allopathic: (Name of medication, dosage, frequency)
Homeopathic: (Name of remedy, dosage, frequency)
Ayurvedic: (Name of treatment or herb, dosage, frequency)"""

if __name__ == "__main__":
    handle_user_input()