#!/bin/bash

set -e

origpath="$PWD"

rm -rf env
virtualenv env
env/bin/pip install Pillow enum34

cd env/lib/python2.7/site-packages
cp -L $(ldd PIL/_imaging.so|grep libjpeg|awk '{print $3}') PIL/
patchelf --set-rpath PIL PIL/_imaging.so

zip -r9 ../../../../zaloa.zip *

cd "$origpath"

rm -rf env
