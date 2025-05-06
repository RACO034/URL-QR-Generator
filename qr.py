import qrcode;
import validators;

#Get and validate URL input
url =  input("Enter the URL to be encoded in the QR code: ")
if not validators.url(url):
    print("Invalid URL. Please enter a valid URL.")
    exit()

#Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
pngName = input("Enter the name of the file to save the QR code: ") + ".png"

img.save(pngName)
print("QR code generated and saved as qr_code.png")