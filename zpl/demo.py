import os
from PIL import Image
import zpl

l = zpl.Label(100,60)
height = 0
l.origin(0,0)
l.write_text("Problem?", char_height=10, char_width=8, line_width=60, justification='C')
l.endorigin()

height += 13
image_width = 5
l.origin((l.width-image_width)/2, height)
image_height = l.write_graphic(
    Image.open(os.path.join(os.path.dirname(zpl.__file__), 'trollface-large.png')),
    image_width)
l.endorigin()

height += image_height + 5
l.origin(22, height)
l.write_barcode(height=70, barcode_type='U', check_digit='Y')
l.write_text('07000002198')
l.endorigin()

height += 20
l.origin(0, height)
l.write_text('Happy Troloween!', char_height=5, char_width=4, line_width=60,
             justification='C')
l.endorigin()

print(l.dumpZPL())
l.preview()