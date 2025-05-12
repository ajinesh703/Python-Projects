from PIL import Image

# Convert message to binary string
def to_binary(msg):
    return ''.join([format(ord(c), '08b') for c in msg])

# Hide message in image
def hide_message(img_path, message, output_path='output.png'):
    img = Image.open(img_path)
    encoded = img.copy()
    width, height = img.size
    binary_msg = to_binary(message) + '1111111111111110'  # End pattern
    msg_idx = 0

    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for n in range(3):  # R, G, B
                if msg_idx < len(binary_msg):
                    pixel[n] = pixel[n] & ~1 | int(binary_msg[msg_idx])
                    msg_idx += 1
            encoded.putpixel((x, y), tuple(pixel))
            if msg_idx >= len(binary_msg):
                encoded.save(output_path)
                print(f"✅ Message hidden in {output_path}")
                return
    print("❌ Image not big enough to hold the message.")

# Extract message from image
def extract_message(img_path):
    img = Image.open(img_path)
    binary_msg = ''
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = img.getpixel((x, y))
            for n in range(3):
                binary_msg += str(pixel[n] & 1)
    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ''
    for c in chars:
        if c == '11111110': break
        message += chr(int(c, 2))
    print("🔓 Hidden message:", message)

# Example usage:
if __name__ == "__main__":
    choice = input("Hide or Reveal? (h/r): ").lower()
    if choice == 'h':
        img_path = input("Enter image path (PNG recommended): ")
        message = input("Enter your secret message: ")
        hide_message(img_path, message)
    elif choice == 'r':
        img_path = input("Enter stego image path: ")
        extract_message(img_path)
    else:
        print("❌ Invalid choice.")
