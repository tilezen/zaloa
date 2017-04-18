upload: zip
	aws lambda update-function-code \
	  --region us-east-1 \
	  --function-name pngcombiner \
	  --zip-file fileb://pngcombiner.zip

zip:
	# rm -rf pngcombiner.zip
	# TODO remove virtualenv itself
	# virtualenv env
	# env/bin/pip install Pillow
	zip -9 pngcombiner.zip pngcombiner.py
	# [ -d env/lib/python2.7/site-packages ] && (cd env/lib/python2.7/site-packages && zip -r9 ../../../../pngcombiner.zip *)

.PHONY: zip
