import qrcode

def generate_qr():

    user_data = input("Enter the URL or text to encode into a QR code: ").strip()
    
    output_filename = input("Enter the output image filename (default: custom_qr.png): ").strip()
    if not output_filename:
        output_filename = "custom_qr.png"
    elif not output_filename.endswith(".png"):
        output_filename += ".png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(user_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    img.save(output_filename)
    print(f"\nSuccess! QR code saved as '{output_filename}'")

if __name__ == "__main__":
    generate_qr()