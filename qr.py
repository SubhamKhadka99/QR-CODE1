import qrcode
data= "https://www.instagram.com/skop.gg/"
qr = qrcode.QRCode
qr=qrcode.QRCode(
    version=1 ,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,

)
qr.add_data(data)
qr.make(fit=True)
img= qr.make_image(fill='black', back_color= 'white')
img.save("qrcode_example.png")
img.show()
