def setup():
    size(700, 280)
    colorMode(HSB, 255)
def draw():
    rect_height = height / 7
    y_positions = range(0, height, rect_height)
    for y in y_positions:
        color_pos = map(y, 0, height, 0, 255)  # not Python's map
        fill(color_pos, 210, 210)
        stroke(27)
        strokeWeight(2)
        rect(0, y, width, y + rect_height)
        if __name__ == '__main__':
            draw()