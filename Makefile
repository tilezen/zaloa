upload: zip
	aws lambda update-function-code \
	  --region us-east-1 \
	  --function-name zaloa \
	  --zip-file fileb://zaloa.zip

zip:
	# rm -rf zaloa.zip
	# TODO remove virtualenv itself
	# virtualenv env
	# env/bin/pip install Pillow enum34
	zip -9 zaloa.zip zaloa.py
	# (cd env/lib/python2.7/site-packages && zip -r9 ../../../../zaloa.zip *)

.PHONY: zip
