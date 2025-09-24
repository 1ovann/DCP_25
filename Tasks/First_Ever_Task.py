import py5

def setup():
    py5.size(400, 400)
    py5.no_stroke()

    # background square
    py5.background(230, 50, 40)   # red

    # big circle
    py5.fill(255, 245, 90)        # yellow
    py5.circle(200, 210, 310)

    # triangle
    py5.fill(120, 250, 250)       # cyan
    py5.triangle(200, 30, 60, 350, 340, 350)

    # ellipse
    py5.fill(190)                 # light gray
    py5.ellipse(200, 200, 145, 75)

    # circle
    py5.fill(0)
    py5.circle(200, 200, 55)

py5.run_sketch()
