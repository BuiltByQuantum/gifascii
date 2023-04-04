import os
import requests
from PIL import Image, ImageDraw, ImageFont, ImageSequence, ImageEnhance
import numpy as np
from io import BytesIO
import imageio

def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def create_ascii_art(image, font_size=10):
    ascii_chars = " .:-=+*%@#"

    image = image.convert("RGB")

    # Increase brightness and saturation
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.7)
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(2.0)

    font = ImageFont.truetype("/Library/Fonts/cour.ttf", font_size)
    char_width, char_height = font.getmask("A").getbbox()[2:]
    width = image.width // char_width
    height = image.height // char_height

    ascii_img = Image.new("RGBA", (image.width, image.height), (15, 15, 15, 255))
    draw = ImageDraw.Draw(ascii_img)

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x * char_width, y * char_height))
            luma = (0.2126 * pixel[0] + 0.7152 * pixel[1] + 0.0722 * pixel[2]) / 255
            char = ascii_chars[min(int(luma * len(ascii_chars)), len(ascii_chars) - 1)]
            draw.text((x * char_width, y * char_height), char, font=font, fill=pixel)

    return ascii_img

def process_gif(image):
    frames = []
    for frame in ImageSequence.Iterator(image):
        ascii_img = create_ascii_art(frame)
        frames.append(np.array(ascii_img))
    return frames

def save_to_files(url, is_gif, ascii_art):
    if not os.path.exists("PROCESSED"):
        os.mkdir("PROCESSED")

    if not os.path.exists("COMPLETE"):
        os.mkdir("COMPLETE")

    image_name = url.split("/")[-1].split(".")[0]
    original_image = download_image(url)
    original_image.save(f"PROCESSED/{image_name}.{original_image.format.lower()}")

    if is_gif:
        imageio.mimsave(f"COMPLETE/{image_name}.gif", ascii_art, format="GIF", fps=15)
    else:
        ascii_art.save(f"COMPLETE/{image_name}.png")

def main(url):
    image = download_image(url)

    if image.format.lower() == "gif":
        is_gif = True
        ascii_art = process_gif(image)
    else:
        is_gif = False
        ascii_art = create_ascii_art(image)

    save_to_files(url, is_gif, ascii_art)

if __name__ == "__main__":
    url = input("Enter the image/gif URL: ")
    main(url)
