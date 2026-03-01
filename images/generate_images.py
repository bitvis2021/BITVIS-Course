from PIL import Image, ImageDraw, ImageFont
import os

# Create 16 test images
for i in range(1, 17):
    # Create a new image with white background
    img = Image.new('RGB', (200, 150), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Generate a random color for the background
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    d.rectangle([(0, 0), (200, 150)], fill=(r, g, b))
    
    # Add text
    text = f'Image {i}'
    # Try to use a default font
    try:
        font = ImageFont.truetype('arial.ttf', 20)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position
    bbox = d.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (200 - text_width) // 2
    y = (150 - text_height) // 2
    
    # Draw text in white
    d.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Save the image
    filename = f'{i}.png'
    img.save(filename)
    print(f'Generated {filename}')

print('All images generated successfully!')