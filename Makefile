SHELL=/bin/bash

.PHONY: setup
setup:
	@mkdir $HOME/tmp
	@export TMPDIR=$HOME/tmp
	@pip3 install wheel
	@pip3 install -r requirements.txt --no-warn-script-location
	@rm -rf ~/tmp/
