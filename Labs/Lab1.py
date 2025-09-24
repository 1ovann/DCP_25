import py5

mode = 0  # 0 = smile face, 1 = red circle, 2 = blue rectangle, 3 = amanita

def setup():
    py5.size(600, 600)
    py5.no_cursor()
    py5.rect_mode(py5.CENTER)  # easier to size from center

def mouse_pressed():
    global mode
    mode = (mode + 1) % 4  # toggle modes on click

def draw():
    py5.background(0)
    if mode == 0:
        draw_smiley()
    elif mode == 1:
        draw_red_circle()
    elif mode == 2:
        draw_blue_rectangle()
    elif mode == 3:
        draw_amanita()

def draw_smiley():
    x, y = py5.mouse_x, py5.mouse_y
    face_r = 40
    py5.no_stroke()
    py5.fill(0, 200, 0)
    py5.circle(x, y, face_r * 2)

    r = int(x / py5.width * 255)
    g = int(y / py5.height * 255)
    b = int((x + y) / (py5.width + py5.height) * 255)

    py5.fill(r, g, b)
    py5.circle(x - 12, y - 12, 10)
    py5.circle(x + 12, y - 12, 10)
    py5.circle(x, y, 8)

    py5.no_fill()
    py5.stroke(0)
    py5.stroke_weight(3)
    py5.arc(x, y + 12, 30, 20, 0, py5.PI)
    py5.no_stroke()

def draw_red_circle():
    cx, cy = py5.width // 2, py5.height // 2
    dx = py5.mouse_x - cx
    dy = py5.mouse_y - cy
    dist_from_center = (dx * dx + dy * dy) ** 0.5 # diameter with pythagoras
    py5.no_stroke()
    py5.fill(220, 40, 40)
    py5.circle(cx, cy, dist_from_center)

def draw_blue_rectangle(): #NEED TO FINISH NEXT WEEEK!!!!!
    cx, cy = py5.width // 2, py5.height // 2

    # base size
    base_w = py5.width
    base_h = py5.height / 3

    py5.fill(25, 25, 112)
    py5.rect(cx, cy, base_w, base_h)

def draw_amanita(): #NEEDS TO BE FIXED
    x, y = py5.mouse_x, py5.mouse_y
    cap_d = 80
    stem_w, stem_h = 18, 46

    # leg
    py5.no_stroke()
    py5.fill(200)               # light gray
    py5.rect(x, y + cap_d*0.28, stem_w, stem_h)

    # cap (filled semicircle)
    py5.fill(220, 40, 40)       # red
    py5.circle(x, y, cap_d)     # full circle
    py5.rect(x, y + cap_d*0.25, cap_d, cap_d*0.5)

    # white dots
    py5.fill(255)
    py5.circle(x - cap_d*0.28, y - cap_d*0.20, cap_d*0.12)
    py5.circle(x,               y - cap_d*0.16, cap_d*0.10)
    py5.circle(x + cap_d*0.25,  y - cap_d*0.24, cap_d*0.11)

py5.run_sketch()
