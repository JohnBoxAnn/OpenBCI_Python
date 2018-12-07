# -*- coding:utf-8 -*-
import plugin_interface as plugintypes

class PluginPrint(plugintypes.IPluginExtended):
    """
        Print OpenBCI values to stdout

        Args:
            None

    """

    # init
    def __init__(self):
        print("Print init")

    # activate
    def activate(self):
        print("Print activated")

    # deactivate
    def deactivate(self):
        print("Print deactivated")

    # show help
    def show_help(self):
        print("Do not need any parameter, just printing stuff.")

	# called with each new sample
    def __call__(self, sample):
        if sample:
            # print impedance if supported
            if self.imp_channels > 0:
                sample_string = "ID: %f\n%s\n%s\n%s" %(sample.id, str(sample.channel_data)[1:-1], str(sample.aux_data)[1:-1], str(sample.imp_data)[1:-1])
            else:
                sample_string = "ID: %f\n%s\n%s" %(sample.id, str(sample.channel_data)[1:-1], str(sample.aux_data)[1:-1])
            print("---------------------------------")
            print(sample_string)
            print("---------------------------------")
    
# DEBBUGING
	# try:
	#     sample_string.decode('ascii')
	# except UnicodeDecodeError:
	#     print("Not a ascii-encoded unicode string")
	# else:
	#     print(sample_string)

