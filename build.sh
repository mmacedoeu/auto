#!/bin/bash

if [ $# -eq 0 ] ; then
  echo "No arguments supplied"
  VERSION="latest"
else
  VERSION=$1
fi

find . | grep [.]sh$ | xargs chmod +x
#sed -i 's/sudo//g' install.sh &&\
docker build -t registry.gitlab.com/gabriel-technologia/autoprovisionamento:${VERSION} .
if [ "$?" -eq "0" ]; then
  docker push registry.gitlab.com/gabriel-technologia/autoprovisionamento:${VERSION}
else
  echo "Docker build failed."
fi
