import os
import string
from plugin_manager import load_plugins_from_suffix


def decompress_file(file_name, suffix_name):
	plugin = load_plugins_from_suffix(suffix_name)
	decompress_cmd = plugin['decompress_command'].format(IN = file_name, OUT = file_name[:-len(suffix_name)-1])
	print('decompress execute: ' + decompress_cmd)
	os.system(decompress_cmd)


