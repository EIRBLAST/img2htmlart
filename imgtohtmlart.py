from PIL import Image
import sys
import os

grey_scale_chars = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """

def resize_image(image, new_size=(200, 200)):
    """ Resize the image to the specified size """
    return image.resize(new_size,Image.Resampling.LANCZOS)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {os.path.basename(__file__)} <input_file>")
        sys.exit(1)

    output_file_name = os.path.splitext(sys.argv[1])[0] + '.html'
    with open(output_file_name, 'w') as output_file:
        output_file.write("<!DOCTYPE html><head><style>body {font-family: 'Courier New', monospace; font-size: 2px;}</style></head><body>")
        
        image = Image.open(sys.argv[1])
        image = resize_image(image)  # Resize the image

        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixel = image.getpixel((x, y))

                gray_scale = (pixel[0] + pixel[1] + pixel[2]) / 3
                grey_char = grey_scale_chars[int((len(grey_scale_chars)-1) * gray_scale / 255)]

                pixel_color = '#%02x%02x%02x' % pixel  # convert tuple to hex string

                html_pixel = f'<font size="1" color="{pixel_color}">{grey_char}</font>'
                output_file.write(html_pixel)

            output_file.write("<br>\n")

        output_file.write("</body></html>")