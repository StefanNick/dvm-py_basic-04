from PIL import Image


monro_image = Image.open("monro_1.jpg")

monro_red, monro_green, monro_blue = monro_image.split()

number_of_px_offset = 50


monro_red_left = monro_red.crop(
    (number_of_px_offset, 0, monro_red.width, monro_red.height)
)
monro_red_right = monro_red.crop(
    (
        number_of_px_offset / 2,
        0,
        monro_red.width - number_of_px_offset / 2,
        monro_red.height,
    )
)
monro_red_overlay = Image.blend(monro_red_left, monro_red_right, 0.5)


monro_blue_left = monro_blue.crop(
    (0, 0, monro_blue.width - number_of_px_offset, monro_blue.height)
)
monro_blue_right = monro_blue.crop(
    (
        number_of_px_offset / 2,
        0,
        monro_blue.width - number_of_px_offset / 2,
        monro_blue.height,
    )
)
monro_blue_overlay = Image.blend(monro_blue_left, monro_blue_right, 0.5)


monro_green_overlay = monro_green.crop(
    (
        number_of_px_offset / 2,
        0,
        monro_green.width - number_of_px_offset / 2,
        monro_green.height,
    )
)


monro_final_overlay = Image.merge(
    "RGB", (monro_red_overlay, monro_blue_overlay, monro_green_overlay)
)
monro_final_overlay.save("monro_final_overlay.jpg")

monro_miniature = Image.open("monro_final_overlay.jpg")
monro_miniature.thumbnail((80, 80))
monro_miniature.save("monro_miniature.jpg")
