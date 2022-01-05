label = """
^XA 
^FO100,100 
^BQN,2,10 
^FDMM,AAC-42
^FS 
^XZ

^XA

^FO140,15
^A0,40,40
^FD
Total Weight : 50 KG
^FS

^FO140,60
^A0,40,40
^FD
shipment_count: 34
^FS

^FO140,105
^A0,40,40
^FD
HUB: DEL
^FS


^XZ
"""

# import zebra
from zebra import Zebra
# z = Zebra('ZDesigner ZT220-200dpi ZPL')
z = Zebra('zpllabelprinter')
z.output(label)
# print(z.getqueues())
