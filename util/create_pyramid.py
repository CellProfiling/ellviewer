import os
from PIL import Image


Image.MAX_IMAGE_PIXELS = 10000000000
image_folder = "images"
output_folder = "pyramid"
dest_extension = ".jpg"


file_list = os.listdir(image_folder)
for file in file_list:
    file_without_extension = os.path.splitext(os.path.basename(file))[0]

    image = Image.open(os.path.join(image_folder, file))
    image.save(os.path.join(output_folder, file_without_extension + dest_extension))
    width = image.width
    height = image.height

    z_levels = int(max(width / 1024 + (1 if width % 1024 > 0 else 0),
                       height / 1024 + (1 if height % 1024 > 0 else 0)))
    for i in range(8):
        if z_levels <= pow(2, i):
            z_levels = i
            break
    for curr_z_level in range(1, z_levels + 1, 1):
        z_dim = 1024 * pow(2, (curr_z_level - 1))

        width_tiles = int(width / z_dim) + (1 if width % z_dim > 0 else 0)
        height_tiles = int(height / z_dim) + (1 if height % z_dim > 0 else 0)
        for i in range(width_tiles):
            for j in range(height_tiles):
                x_crop = z_dim * i
                y_crop = z_dim * j
                im_crop = image.crop((x_crop, y_crop, x_crop + z_dim, y_crop + z_dim))
                image_name = file_without_extension + '_z' + str(z_dim) + '_x' + str(x_crop) + '_y' + str(
                    y_crop) + dest_extension
                im_crop.thumbnail((1024, 1024))
                im_crop.save(os.path.join(output_folder, image_name))

    image.thumbnail((1024, 1024))
    image.save(os.path.join(output_folder, file_without_extension + "_base" + dest_extension))
