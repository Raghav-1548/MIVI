from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

def load_image(image_path):
    try:
        return Image.open(image_path)
    except IOError:
        print(f"Error: Unable to open image file '{image_path}'. Please check the file path and try again.")
        return None


def main():

    print("Loading the BLIP image captioning model...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
    print("Model loaded successfully.")

    while True:

        image_path = input("Enter the path to your image file (or 'q' to quit): ")

        if image_path.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break

        image = load_image(image_path)
        if image is None:
            continue

        inputs = processor(images=image, return_tensors="pt")

        print("Generating caption...")
        with torch.no_grad():
            output = model.generate(**inputs, max_new_tokens=50)


        caption = processor.decode(output[0], skip_special_tokens=True)

        print("Generated caption:")
        print(caption)

        print("\n")


if __name__ == "__main__":
    main()