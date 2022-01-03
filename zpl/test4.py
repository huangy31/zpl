with Image(filename=savepath + ".pdf[0]") as img:
    img.save(filename=savepath + ".png")

fd_img = open(savepath + ".png", 'r')
img = ImagePillow.open(fd_img)
#img = resizeimage.resize_contain(img, [100, 150])
img.save(savepath + ".png", dpi=[203,203])
fd_img.close()
# convert png to zpl
# im = pilloImg.open(savepath+".png")

convert = ZPLConvert(savepath + ".png")
# convert.set_compress_hex(True)
result = convert.convert(None, True)
f = open(savepath + ".zpl", "wb")
f.write(result)
f.close()
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect((host, 9100))
f = open(savepath + ".pdf", "rb")
l = f.read(1024)
while l :
    _logger.error(l)
    mysocket.send(bytes(l))
    l = f.read(1024)
f.close()
mysocket.close()