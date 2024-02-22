from PIL import Image, ImageOps
import random

# Load your images (replace 'image_path' with the actual file paths)
background = Image.open('background_path.png')
object_1 = Image.open('object_1_path.png')
object_2 = Image.open('object_2_path.png')
overlay = Image.open('overlay_path.png')

# Example function to randomly place an object on the background
def place_randomly(base_img, overlay_img):
    max_x = base_img.width - overlay_img.width
    max_y = base_img.height - overlay_img.height
    random_x = random.randint(0, max_x)
    random_y = random.randint(0, max_y)
    base_img.paste(overlay_img, (random_x, random_y), overlay_img)
    return base_img

# Create a new composite image
composite = background.copy()

# Randomly place objects
composite = place_randomly(composite, object_1)
composite = place_randomly(composite, object_2)

# Add an overlay (e.g., for effects)
composite.paste(overlay, (0, 0), overlay)

# Save the final image
composite.save('final_composite_image.png')
