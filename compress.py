import os
import string
from plugin_manager import load_plugins_from_suffix


def compress_file(file_name, suffix_name):
	plugin = load_plugins_from_suffix(suffix_name)
	compress_cmd = plugin['compress_command'].format(IN = file_name[:-len(suffix_name)-1], OUT = file_name)
	print('compress execute: ' + compress_cmd)
	os.system(compress_cmd)
