upload: zip
	aws lambda update-function-code \
	  --region us-east-1 \
	  --function-name zaloa \
	  --zip-file fileb://zaloa.zip

zip: zaloa.zip
	zip -9 zaloa.zip zaloa.py

download-base-zip:
	aws s3 cp s3://mapzen.software/tile/zaloa/lambda-base.zip zaloa.zip

build-base-zip:
	./build-base-zip.sh

upload-base-zip: zaloa.zip
	aws s3 cp zaloa.zip s3://mapzen.software/tile/zaloa/lambda-base.zip

clean:
	rm -rf zaloa.zip env

.PHONY: zip download-base-zip build-base-zip upload-base-zip
