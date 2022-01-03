from PIL import Image
import zpl
from zebra import Zebra

height = 100
width = 60
# z = Zebra('ZDesigner ZT220-200dpi ZPL')
z = Zebra('zpllabelprinter')
label = zpl.Label(height, width, 8)
label.write_graphic(Image.open('trollface-large.png'), width)
z.output(label.dumpZPL())
label.preview()

# class Print:

#  def __init__(self):
#   self.zebra = Zebra()
#   self.printers = self.zebra.getqueues()


#  def print_out(self, queue, height, width):
#     z = Zebra(queue)
#     label = zpl.Label(height, width, 8)
#     label.write_graphic(Image.open("trollface-large.png"), width)
#     z.output(label.dumpZPL())
#     label.preview()

