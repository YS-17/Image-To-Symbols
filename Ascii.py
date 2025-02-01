from PIL import Image


# Path to your image
img_path = r"___.jpeg"  # Use a raw string or double backslashes


# Define a more detailed set of ASCII characters

# ASCII_CHARS = "@%#*+=-:!$^&/?. "
ASCII_CHARS = "@%#*+=-:. "

def pixel_to_ascii(pixel):
    # Ensure the index is within the range of ASCII_CHARS
    index = pixel // (256 // len(ASCII_CHARS))
    return ASCII_CHARS[min(index, len(ASCII_CHARS) - 1)]

def image_to_ascii(image_path, new_width=150):
    # Load the image
    img = Image.open(image_path)
    
    # Convert the image to grayscale
    img = img.convert('L')
    
    # Resize the image
    width, height = img.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.55)  # Adjust for font aspect ratio
    img = img.resize((new_width, new_height))
    
    # Convert image pixels to ASCII characters
    pixels = img.getdata()
    ascii_str = "".join([pixel_to_ascii(pixel) for pixel in pixels])
    
    # Split the string into multiple lines
    ascii_img = "\n".join([ascii_str[i:(i+new_width)] for i in range(0, len(ascii_str), new_width)])
    
    return ascii_img

# Generate ASCII art
ascii_art = image_to_ascii(img_path)

# Save the ASCII art to a text file
ascii_art_path = "high_quality_ascii_art.txt"
with open(ascii_art_path, "w") as f:
    f.write(ascii_art)

print(f"High-quality ASCII art saved to {ascii_art_path}")