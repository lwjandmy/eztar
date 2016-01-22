#!/usr/bin/env python3
import sys
import os.path
import re
from compress import compress_file
from decompress import decompress_file


def process_file_name(file_name):
	suffix_name = re.search('''[^\.]+$''', file_name).group()
	if os.path.exists(file_name):
		# file exist, decompress it
		decompress_file(file_name, suffix_name)
	else:
		# file not exist, compress to file
		compress_file(file_name, suffix_name)


def main():
	if len(sys.argv) < 2 :
		print('Usage: eztar file-name [file-name] [file-name] ...')
		return

	for arg in sys.argv[1:]:
		process_file_name(arg)


if __name__ == '__main__':
	main()
