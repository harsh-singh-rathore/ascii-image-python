from processImage.processing import resize_image, cvt_to_grayscale, pixel_to_ascii, cvt_ascii_to_img
from PIL import Image

def main(new_width=100):
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except Exception as e:
        raise FileNotFoundError('File not found')

    
    new_image_data = pixel_to_ascii(cvt_to_grayscale(resize_image(image, new_width)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


if __name__=="__main__":
    main(600)
