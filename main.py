import qrcode

def generate_qr():
    # Prompt the user for input text or URL
    user_data = input("Enter the URL or text to encode into a QR code: ").strip()
    
    # Prompt for custom filename (with a default fallback)
    output_filename = input("Enter the output image filename (default: custom_qr.png): ").strip()
    if not output_filename:
        output_filename = "custom_qr.png"
    elif not output_filename.endswith(".png"):
        output_filename += ".png"

    # Configure QR code parameters
    qr = qrcode.QRCode(
        version=1,  # Controls size (1 is a 21x21 matrix, up to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (~30%)
        box_size=10, # Size of each square (pixel width)
        border=4,    # Border thickness in boxes (minimum is 4)
    )
    
    # Pass the user data to the instance
    qr.add_data(user_data)
    qr.make(fit=True)

    # Render the image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the output file
    img.save(output_filename)
    print(f"\nSuccess! QR code saved as '{output_filename}'")

if __name__ == "__main__":
    generate_qr()