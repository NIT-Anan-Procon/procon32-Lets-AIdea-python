.PHONY: setup
setup:
	@python3 -m venv venv
	@direnv allow
	@pip3 install wheel
	@pip3 install -r requirements.txt
	@mkdir -p image_captioning_pytorch/tutorials/models
	@mkdir -p image_captioning_pytorch/tutorials/data
	@wget https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip
	@wget https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip
	@unzip vocap.zip
	@unzip pretrained_model.zip
	@mv decoder-5-3000.pkl encoder-5-3000.pkl ./image_captioning_pytorch/tutorials/models
	@mv vocap.pkl ./image_captioning_pytorch/tutorials/data
	@rm -rf vocap.zip pretrained_model.zip