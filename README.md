# Image to ASCII Art Converter

This Python script (`Image_to_ASCII_Art_Converter/img_to_ascii_art.py`) converts an image to ASCII art. It resizes the image, converts it to grayscale, and then maps the pixel values to ASCII characters to create an ASCII representation of the image.

## Requirements

- Python 3.x
- Pillow (PIL)

## Installation

To run this script, you'll need to have Python and Pillow installed. You can install Pillow using pip:

```
pip install pillow
```

## Usage
1. Clone the repository or download the repository.
2. Navigate to the directory containing the script and run script.
    ```
    cd Image_to_ASCII_Art_Converter
    python img_to_ascii_art.py
    ```

3. Enter the absolute path to the image you want to convert when prompted.
4. After script is executed, a .txt file containing the ASCII art will be created and saved to `Image_to_ASCII_Art_Converter/result_ascii_art` directory. The directory will be created if it does not exist.

## Output
The ASCII art will be saved in a text file named `result_text.txt` inside the `Image_to_ASCII_Art_Converter/result_ascii_art` directory. The directory will be created if it does not exist.

## Configurable Settings
The script includes a few settings that you can customize to fit your needs:

`MAX_SIZE`: The maximum number of pixels for the longest side of the resized image. Adjust this value to change the size of the output ASCII art. The default value is 100.

`TEXT_HEIGHT_ADJUST`: The adjustment factor to compensate for the difference in width and height of the text characters compared to pixels. This helps maintain the aspect ratio in the ASCII art. The default value is 0.6.

`TEXT_WIDTH_ADJUST`: Another adjustment factor for width compensation. The default value is 1.6.

To change these settings, simply modify the corresponding values in `Image_to_ASCII_Art_Converter/img_to_ascii_art.py`.