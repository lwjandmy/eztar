import json
from config import *


def load_plugins_from_suffix(suffix_name):
	return json.loads(open(plugins_path + suffix_name + '.json').read())


if __name__ == '__main__':
	print('test:')
	plugin = load_plugins_from_suffix('tar')
	print(plugin)
	print(plugin['decompress_command'])
