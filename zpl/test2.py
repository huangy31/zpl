from PIL import Image
import zpl
from zebra import Zebra

class Print:

 def __init__(self):
  self.zebra = Zebra()
  self.printers = self.zebra.getqueues()


 def print_out(self, queue, height, width):
    z = Zebra(queue)
    label = zpl.Label(height, width, 8)
    label.write_graphic(Image.open("trollface-large.png"), width)
    z.output(label.dumpZPL())
    label.preview()

# def __main__():

# if __name__ == "__main__":
#     __main__()