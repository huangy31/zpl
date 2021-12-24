from zebra import Zebra
z = Zebra()
Q=z.getqueues()
z.setqueue(Q[0])
z.setup(direct_thermal=True, label_height=None, label_width=None)
z.autosense()
z.print_config_label()