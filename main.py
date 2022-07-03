from PIL import Image
from os import listdir
from random import randint

image_dir = r".\images"
images_name = listdir(image_dir)

# user parameters
final_size_x = 10000
final_size_y = 10000
image_size = 128
padding = 60

range_x = final_size_x // (image_size + padding)
range_y = final_size_y // (image_size + padding)

print(range_x * range_y)

main_sheet = Image.new("RGBA", (final_size_x, final_size_y))

for y in range(range_y):
    for x in range(range_x):
        image_sheet = Image.new("RGBA", (image_size + padding, image_size + padding))

        ramdom_number = randint(0, len(images_name)-1)
        image = Image.open(image_dir+"\\"+images_name[ramdom_number])
        image_sheet.paste(image, (int(padding/2), int(padding/2)), image)

        rotation = randint(-60, 60) - 45
        image_sheet = image_sheet.rotate(rotation)

        x_pos = x * (image_size + padding)
        y_pos = y * (image_size + padding)

        if not y % 2 == 0:
            x_pos -= int((image_size + padding) / 2)

        main_sheet.paste(image_sheet, (x_pos, y_pos), image_sheet)


main_sheet.save(r'.\results\new.png', 'png')

print('done')
input()