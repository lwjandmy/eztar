# eztar
An easy way to use tar,gzip,etc. files.


## Get & Install & UnInstall
git clone git@github.com:lwjandmy/eztar.git

cd eztar

sudo ./install.sh

sudo ./uninstall.sh


## Requirement
Python3

tar, gzip, etc. (options)


## Usage
### To get help:

tar

### To tar 'data' file(or directory) to 'data.tar':

eztar data.tar

### To untar 'data.tar' file to 'data':

eztar data.tar  (yes, there are same command string)


## How it works
When we type 'eztar data.tar', eztar will check if 'data.tar' file exist, if exist, do decompress; if not exist, do compress. 
### compress
Firstly, get the suffix file name, example: get 'tar' from 'data.tar'.

Then load tar.json in plugins directory.

Finally, execute command strings stored in 'compress_command' in json.
### decompress
same as compress


## Contribute to plugins
cd eztar/plugins

cp tar.json new-file-type.json  # copy an exist plugin, then change it to a new one

vim new-file-type.json  # change 'compress_command' and 'decompress_command'. '{IN}' means in-file name, '{OUT}' means out-file name.

 # Finish!

 # (options) Test your new plugin:

touch data  # generate a file

eztar data.new-file-type  # compress data file

 # check printed command strings to see if command strings are correct; check the folder whether there is a data.new-file-type file.

rm data  # remove data file

eztar data.new-file-type  # decompress data.new-file-type file

 # check printed command strings to see if command strings are correct; check the folder whether there is a data file.


## Contact to me
E-Mail: lwjandmy@qq.com
