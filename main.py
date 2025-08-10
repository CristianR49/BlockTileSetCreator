from PIL import Image

def paint_single_tile():
    start_position = (0, 8)

    paint_top_pattern(start_position)

    paint_bottom_pattern((start_position[0], start_position[1] + 12))

    paint_horizontal_border_with_black_between_the_patterns(start_position, 1)

    paint_all_black_borders_around_one_collumn(start_position)



def paint_top_tiles_with_dividers():
    start_position = (16, 8)

    paint_top_pattern_on_three_aside_collumns(start_position)

    paint_all_black_borders_around_three_collumns(start_position)

    paint_area_with_color(start_position, 46, 7)

    paint_y_axis_with_black((31, 19), (31, 31))

    paint_y_axis_with_black((48, 19), (48, 31))

def paint_middle_tiles():
    start_position = (16, 56)

    paint_all_black_borders_minus_top_around_three_collumns(start_position)

    paint_top_pattern_on_three_aside_collumns(start_position)

    paint_area_with_color(start_position, 46, 7)

def paint_bottom_tiles():
    start_position = (16, 104)

    paint_all_black_borders_minus_top_around_three_collumns(start_position)

    paint_top_pattern_on_three_aside_collumns(start_position)

    paint_horizontal_border_with_black_between_the_patterns(start_position, 3)

    paint_bottom_pattern_on_three_aside_collumns(start_position)

def paint_top_tiles_without_dividers():
    start_position = (64, 56)

    paint_top_pattern_on_three_aside_collumns(start_position)

    paint_all_black_borders_around_three_collumns(start_position)

    paint_area_with_color(start_position, 46, 7)

def paint_horizontal_line():
    start_position = (64, 8)

    paint_top_pattern_on_three_aside_collumns(start_position)

    paint_all_black_borders_around_three_collumns(start_position)

    paint_horizontal_border_with_black_between_the_patterns(start_position, 3)

    paint_bottom_pattern_on_three_aside_collumns(start_position)

def paint_vertical_line_top():
    start_position = (112, 8)

    paint_top_pattern(start_position)

    paint_area_with_color(start_position, 14, 7)

    paint_all_black_borders_around_one_collumn(start_position)

def paint_vertical_line_middle():
    start_position = (112, 56)

    paint_top_pattern(start_position)

    paint_area_with_color(start_position, 14, 7)

    paint_all_black_borders_minus_top_around_one_collumn(start_position)

def paint_vertical_line_bottom():
    start_position = (112, 104)

    paint_top_pattern(start_position)

    paint_bottom_pattern((start_position[0], start_position[1] + 12))

    paint_horizontal_border_with_black_between_the_patterns(start_position, 1)

    paint_all_black_borders_minus_top_around_one_collumn(start_position)




def paint_vertical_border_with_black(start_position):
    paint_y_axis_with_black(start_position, (start_position[0], start_position[1] + 23))

def paint_y_axis_with_black(start, end):
    y_distance = end[1] - start[1]
    for y in range(y_distance):
        image.putpixel((start[0], start[1] + y), (0, 0, 0))

def paint_horizontal_border_with_black(start_position, tiles_amount):
    distance = tiles_amount * 16
    paint_x_axis_with_black(start_position, (start_position[0] + distance, start_position[1]))

def paint_horizontal_border_with_black_between_the_patterns(start_position, tiles_amount):
    start_position = (start_position[0], start_position[1] + 11)

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
    print(start_position)
    start_position = (start_position[0] + 1, start_position[1] + 16)
    pixel_color_position = (start_position[0], start_position[1] - 1)
    color = image.getpixel(pixel_color_position)

    for y in range(start_position[1], start_position[1] + max_y):
        for x in range(start_position[0], start_position[0] + max_x):
            image.putpixel((x, y), color)

def paint_bottom_pattern(start_position):
    pattern_position = (0, 65)
    for y in range(11):
        for x in range(16):
            pixel_copy = image.getpixel((pattern_position[0] + x,pattern_position[1] + y))
            position_to_paint = (start_position[0] + x,start_position[1] + y)
            image.putpixel(position_to_paint, pixel_copy)

def paint_all_black_borders_around_three_collumns(start_position):
    paint_vertical_border_with_black(start_position)
    paint_vertical_border_with_black((start_position[0] + 47, start_position[1]))
    paint_horizontal_border_with_black((start_position[0], start_position[1] + 23), 3)
    paint_horizontal_border_with_black(start_position, 3)

def paint_all_black_borders_around_one_collumn(start_position):
    paint_vertical_border_with_black(start_position)
    paint_vertical_border_with_black((start_position[0] + 15, start_position[1]))
    paint_horizontal_border_with_black((start_position[0], start_position[1] + 23), 1)
    paint_horizontal_border_with_black(start_position, 1)

def paint_all_black_borders_minus_top_around_three_collumns(start_position):
    paint_vertical_border_with_black(start_position)
    paint_vertical_border_with_black((start_position[0] + 47, start_position[1]))
    paint_horizontal_border_with_black((start_position[0], start_position[1] + 23), 3)

def paint_all_black_borders_minus_top_around_one_collumn(start_position):
    paint_vertical_border_with_black(start_position)
    paint_vertical_border_with_black((start_position[0] + 15, start_position[1]))
    paint_horizontal_border_with_black((start_position[0], start_position[1] + 23), 1)

def paint_top_pattern_on_three_aside_collumns(start_position):
    positions_to_paint_top_pattern = [(start_position[0] + 1, start_position[1]),
                                      (start_position[0] + 15, start_position[1]),
                                      (start_position[0] + 31, start_position[1])]

    for position_to_paint in positions_to_paint_top_pattern:
        paint_top_pattern(position_to_paint)

def paint_bottom_pattern_on_three_aside_collumns(start_position):
    start_position = (start_position[0] + 1, start_position[1] + 12)
    positions_to_paint_top_pattern = [(start_position[0], start_position[1]),
                                      (start_position[0] + 14, start_position[1]),
                                      (start_position[0] + 30, start_position[1])]

    for position_to_paint in positions_to_paint_top_pattern:
        paint_bottom_pattern(position_to_paint)

imagem_path = r"C:\Users\crist\PycharmProjects\BlockTileSetCreator\Castle.png"
image = Image.open(imagem_path)

paint_single_tile()

paint_top_tiles_with_dividers()

paint_middle_tiles()

paint_bottom_tiles()

paint_top_tiles_without_dividers()

paint_horizontal_line()

paint_vertical_line_top()

paint_vertical_line_middle()

paint_vertical_line_bottom()

image.save("Castle.png")

if image:
    image.close()
