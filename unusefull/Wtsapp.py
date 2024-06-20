import os
from os import system, listdir, makedirs
from PIL import Image

C = open(r"../keys/C", "r").readline()

def generate_images(prompt: str):
    system(f'python -m BingImageCreator --prompt "{prompt}" -U "{C}"')
    image_files = listdir("../output")
    if not image_files:
        print("No images found. Make sure the BingImageCreator has downloaded images.")
    return image_files[-4:]

class ShowImage:
    def __init__(self, image_list: list) -> None:
        self.image_list = image_list

    def open(self, image_number):
        if image_number < len(self.image_list):
            try:
                image_path = os.path.join("../output", self.image_list[image_number])
                img = Image.open(image_path)
                img.show()
            except Exception as e:
                print(f"Error opening image {self.image_list[image_number]}: {e}")
                self.open(image_number + 1)
        else:
            print("No more images to open.")

    def close(self, image_number):
        if image_number < len(self.image_list):
            try:
                image_path = os.path.join("../output", self.image_list[image_number])
                img = Image.open(image_path)
                img.close()
            except Exception as e:
                print(f"Error closing image {self.image_list[image_number]}: {e}")
                self.close(image_number + 1)
        else:
            print("No more images to close.")

# Ensure the "output" directory exists
makedirs("../output", exist_ok=True)

# Example usage:
prompt_text = "ironman"
image_list = generate_images(prompt_text)

# Display the first image
show_images = ShowImage(image_list)
show_images.open(1)
