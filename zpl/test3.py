from zebra import Zebra

z = Zebra()
# Constructor with optional printer queue

Q=z.getqueues()
# Return a list containing available printer queues
print(Q)


# z.setqueue(Q[0])
# Set the printer queue
print(Q[0])


# z.setup(direct_thermal=True, label_height=None, label_width=None)
# Set up the label printer using EPL2. Parameters are not set if they are None.
#   Not necessary if using AutoSense (hold feed button while powering on)
#     direct_thermal - True if using direct thermal labels
#     label_height   - tuple (label height, label gap) in dots
#     label_width    - in dots


# z.autosense()
# Run AutoSense by sending an EPL2 command
# Get the printer to detect label and gap length and set the sensor levels

# z = Zebra('ZDesigner ZT220-200dpi ZPL')
z = Zebra('zpllabelprinter')
z.print_config_label()
# Send an EPL2 command to print label(s) with current config settings