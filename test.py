# from matplotlib.pyplot import text, savefig
# import matplotlib.pyplot as plt


# with open(r'ascii_image.txt', 'r') as file:
#     data = file.read()

# plt.rcParams['font.family'] = 'monospace'
# plt.tight_layout()
# plt.axis("off")
# text(0, 0, data, fontsize=1)
# savefig("out.png")

import text_to_image

# encoded_image_path = text_to_image.encode("Hello World!", "image.png")
encoded_image_path = text_to_image.encode_file("ascii_image.txt", "output_image.png")

# decoded_text = text_to_image.decode("encoded_image.png")
# decoded_file_path = text_to_image.decode_to_file("encoded_image.png", "output_text_file.txt")