import os
from datetime import datetime
from rembg import remove

class BackgroundRemover:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def process_images(self):
        today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        processed_folder = os.path.join(self.output_folder, today)
        os.makedirs(processed_folder, exist_ok=True)
        for filename in os.listdir(self.input_folder):
            if filename.endswith((".jpg",".jpeg","png")):
                input_path = os.path.join(self.input_folder, filename)
                output_path = os.path.join(processed_folder, filename)
                self.remove_background(input_path, output_path)
                # _move_originals

    def remove_background(self, input_path, output_path):
        with open(input_path, 'rb') as inp, open(output_path, 'wb') as outp:
            background_output = remove(inp.read())
            outp.write(background_output)

    def move_originals(self):
        pass

