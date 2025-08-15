import os
from PIL import Image

def resize_and_convert_images(input_folder, output_folder, size=(800, 800), output_format="PNG"):
    """
    Resizes and converts all images in the input folder and saves them to the output folder.
    
    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to save processed images.
        size (tuple): New image size (width, height).
        output_format (str): Desired output format (e.g., "PNG", "JPEG").
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        try:
            with Image.open(file_path) as img:
                img_resized = img.resize(size)
                base_name = os.path.splitext(file_name)[0]
                save_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
                img_resized.save(save_path, output_format)
                print(f"Processed: {file_name} → {save_path}")
        except Exception as e:
            print(f"Skipping {file_name} - Error: {e}")

if __name__ == "__main__":
    input_dir = "images_input"   # Folder with original images
    output_dir = "images_output" # Folder to save resized images
    resize_and_convert_images(input_dir, output_dir, size=(800, 800), output_format="PNG")
