from PIL import Image

def paint_top_tiles():
    start_position = (16, 8)

    paint_vertical_border_with_black(start_position)
    paint_vertical_border_with_black((63, 8))
    paint_horizontal_border_with_black((16, 31), 3)
    paint_horizontal_border_with_black(start_position, 3)

    positions_to_paint_top_pattern = [(17, 9), (31, 9), (47, 9)]

    for position_to_paint in positions_to_paint_top_pattern:
        paint_top_pattern(position_to_paint)

    paint_area_with_color((17, 25), 46, 6)

def paint_middle_tiles():
    start_position = (16, 56)

    paint_vertical_border_with_black(start_position)
    paint_vertical_border_with_black((63, 56))
    paint_horizontal_border_with_black((16, 79), 3)

    positions_to_paint_top_pattern = [(17, 56), (31, 56), (47, 56)]

    for position_to_paint in positions_to_paint_top_pattern:
        paint_top_pattern(position_to_paint)

    paint_area_with_color((17, 72), 46, 7)

def paint_vertical_border_with_black(start_position):
    paint_y_axis_with_black(start_position, (start_position[0], start_position[1] + 23))

def paint_y_axis_with_black(start, end):
    y_distance = end[1] - start[1]
    for y in range(y_distance):
        image.putpixel((start[0], start[1] + y), (0, 0, 0))

def paint_horizontal_border_with_black(start_position, tiles_amount):
    distance = tiles_amount * 16
    paint_x_axis_with_black(start_position, (start_position[0] + distance, start_position[1]))

def paint_x_axis_with_black(start, end):
    x_distance = end[0] - start[0]
    for x in range(x_distance):
        image.putpixel((start[0] + x, start[1]), (0, 0, 0))

def paint_top_pattern(start_position):
    pattern_position = (0, 48)
    for y in range(16):
        for x in range(16):
            pixel_copy = image.getpixel((pattern_position[0] + x,pattern_position[1] + y))
            position_to_paint = (start_position[0] + x,start_position[1] + y)
            image.putpixel(position_to_paint, pixel_copy)

def paint_top_pattern_until_this_y(start_position, y_limit):
    pattern_position = (0, 48)
    for y in range(y_limit):
        for x in range(16):
            pixel_copy = image.getpixel((pattern_position[0] + x, pattern_position[1] + y))
            position_to_paint = (start_position[0] + x, start_position[1] + y)
            image.putpixel(position_to_paint, pixel_copy)

def paint_area_with_color(start_position, max_x, max_y):
    pixel_color_position = (start_position[0], start_position[1] - 1)
    color = image.getpixel(pixel_color_position)

    for y in range(start_position[1], start_position[1] + max_y):
        for x in range(start_position[0], start_position[0] + max_x):
            image.putpixel((x, y), color)

imagem_path = r"C:\Users\crist\PycharmProjects\BlockTileSetCreator\Castle.png"
image = Image.open(imagem_path)

paint_top_tiles()

paint_middle_tiles()

image.save("Castle.png")

if image:
    image.close()
