from PIL import Image, ImageDraw
import random

def draw_bezier(draw, control_points, width, fill):
    """Draw a bezier curve with varying width"""
    steps = 10
    for i in range(steps):
        t = i / float(steps)
        x = int((1-t)**3 * control_points[0][0] + 3 * (1-t)**2 * t * control_points[1][0] + 3 * (1-t) * t**2 * control_points[2][0] + t**3 * control_points[3][0])
        y = int((1-t)**3 * control_points[0][1] + 3 * (1-t)**2 * t * control_points[1][1] + 3 * (1-t) * t**2 * control_points[2][1] + t**3 * control_points[3][1])
        r = width / 2
        draw.ellipse((x-r, y-r, x+r, y+r), fill=fill)

def generate_scribble(width, height):
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    for _ in range(10):  # Number of scribbles
        start_x, start_y = random.randint(0, width), random.randint(0, height)
        control_points = [(start_x, start_y)]
        for _ in range(3):  # Generate control points for Bezier curve
            point = (random.randint(0, width), random.randint(0, height))
            control_points.append(point)
        
        # Draw bezier with varying line width
        draw_bezier(draw, control_points, random.randint(1, 3), 'black')
    
    return image

# Generate and show the scribble
scribble_image = generate_scribble(800, 600)
scribble_image.show()
