import os
from PIL import Image, ImageOps

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
MAX_SIZE = 100 # Max number of pixel for the longest side

# Multiply resized img width/height by a factor,
# to compensate for the character that does not have the same width and height like pixels
TEXT_HEIGHT_ADJUST = 0.6
TEXT_WIDTH_ADJUST = 1.6

def resize_img(img, max_size=MAX_SIZE) -> Image:
    """
    Resize image while maintaining aspect ratio and adjusting for text dimensions.

    Args:
    - img (PIL.Image.Image): Image to resize
    - max_size (int): Maximum size for the longest side

    Output:
    - PIL.Image.Image: Resized image
    """
    width, height = img.size

    # Calculate aspect ratio
    if width > height:
        aspect_ratio = height/width
        new_width = max_size
        new_height = int(max_size * aspect_ratio * TEXT_HEIGHT_ADJUST)
    else:
        aspect_ratio = width/height
        new_height = max_size
        new_width = int(max_size * aspect_ratio * TEXT_WIDTH_ADJUST)

    return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

def convert_to_grayscale(img) -> Image:
    """
    Convert the image to grayscale.

    Args:
    - img (PIL.Image.Image): Image to convert

    Output:
    - PIL.Image.Image: Grayscale image
    """
    return ImageOps.grayscale(img)

def convert_to_ascii(img) -> str:
    """
    Convert the grayscale image to ASCII art.
    
    Args:
    - img (PIL.Image.Image): Grayscale image to convert

    Output:
    - ascii_img (str): ASCII art representation of the image
    """
    
    img_pixel = img.getdata()
    ascii_line_img = ""
    bin_num = 255//(len(ASCII_CHARS)) + 1

    for pixel in img_pixel:
        ascii_line_img = ascii_line_img + ASCII_CHARS[pixel//bin_num]

    width = img.size[0]
    ascii_img = "\n".join(ascii_line_img[i:(i+width)] for i in range(0, len(img_pixel), width))

    return ascii_img

def main():
    # Read image
    img_path = input("Enter path to image: ")
    img = Image.open(str(img_path), "r")
    img = resize_img(img)
    img = convert_to_grayscale(img)
    img = convert_to_ascii(img)

    # Create directory to store converted ascii art
    dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_ascii_art')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    # Write converted ascii art to text file
    with open(os.path.join(dir_path, 'result_text.txt'), 'w') as f:
        f.write(img)

if __name__ == "__main__":
    main()