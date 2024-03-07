from PIL import Image, ImageDraw
import random

# Function to generate a random scribble
def generate_scribble(width, height, scribble_count=10):
    # Create a new image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    for _ in range(scribble_count):
        # Random starting point for the scribble
        start_x = random.randint(0, width)
        start_y = random.randint(0, height)
        
        # Generate random scribble lines
        for _ in range(random.randint(20, 50)):  # Number of segments in a scribble
            end_x = start_x + random.randint(-20, 20)
            end_y = start_y + random.randint(-20, 20)
            
            # Draw a line segment
            draw.line([start_x, start_y, end_x, end_y], fill='black', width=1)
            
            # Update the start point for the next segment
            start_x, start_y = end_x, end_y
            
    return image

# Generate and show the scribble
width, height = 800, 600  # Canvas size
scribble_image = generate_scribble(width, height, 1)
scribble_image.show()

# Save the image
scribble_image.save('scribble.png')
