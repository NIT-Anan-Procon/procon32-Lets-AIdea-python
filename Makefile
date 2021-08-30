SHELL=/bin/bash

.PHONY: setup
setup:
	@pip3 install wheel
	@pip3 install -r requirements.txt --no-warn-script-location
	@mkdir -p image_captioning_pytorch/tutorials/models
	@mkdir -p image_captioning_pytorch/tutorials/data
	@wget -nc https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip
	@wget -nc https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip
	@unzip vocap.zip
	@unzip pretrained_model.zip
	@mv decoder-5-3000.pkl encoder-5-3000.pkl ./image_captioning_pytorch/tutorials/models
	@mv vocab.pkl ./image_captioning_pytorch/tutorials/data
	@rm -rf vocap.zip pretrained_model.zip