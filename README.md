# ASCII Art Converter and Discord Bot

Convert your images and GIFs into stunning ASCII art, and share them with your friends on Discord using our awesome bot!

## Features

- Convert images and animated GIFs into ASCII art
- Adjust brightness, saturation, and contrast for a better result
- Share your ASCII art on Discord with a slash command

## Usage

### Image/GIF to ASCII Art Converter

The converter script consists of several functions that work together to convert an image or GIF into ASCII art.

1. `download_image(url)`: Downloads an image or GIF from the given URL and returns a PIL Image object.
2. `create_ascii_art(image, font_size=10)`: Converts a single image frame into an ASCII art image. This function adjusts the brightness and saturation of the image and maps its pixels to ASCII characters.
3. `process_gif(image)`: Iterates through the frames of an animated GIF, converts each frame into ASCII art, and returns a list of the converted frames.
4. `save_to_files(url, is_gif, ascii_art)`: Saves the original image or GIF and the converted ASCII art to separate folders.
5. `main(url)`: The main function that uses the above functions to download an image or GIF, convert it to ASCII art, and save the result.

To use the script, run it and enter the URL of the image or GIF you want to convert when prompted. The script will download the image, convert it to ASCII art, and save both the original and the converted files in separate folders.

### Discord Bot

To implement a Discord bot that can convert images and GIFs to ASCII art, follow these steps:

1. Install the required libraries: `pip install discord-py discord-py-slash-command`
2. Create a new Python script for the bot and import the necessary libraries and the main functions from the ASCII art converter script.
3. Set up the bot, add a slash command, and define a function that will handle the `/gifascii` command. This function should use the `main(url)` function from the converter script to process the image or GIF and send the result to the chat.
4. Run the bot script, and invite the bot to your Discord server.

To use the bot, enter the `/gifascii` slash command followed by the URL of the image or GIF you want to convert. The bot will process the image and send the ASCII art as a file in the chat.

Enjoy creating and sharing ASCII art with your friends on Discord!
