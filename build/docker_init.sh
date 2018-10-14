#!/bin/bash

/usr/bin/pip3 install -r /build/requirements.txt

cd /build && /usr/local/bin/pyinstaller -F src/main/DockerContainerInitializationApplication.py

VERSION=$(cat /VERSION)
DPKG_PACKAGE_ROOT=/dpkg/config-manager_$VERSION

mkdir -p $DPKG_PACKAGE_ROOT/usr/local/bin
mkdir -p $DPKG_PACKAGE_ROOT/DEBIAN

cp /build/dist/DockerContainerInitializationApplication $DPKG_PACKAGE_ROOT/usr/local/bin/config-manager
cat > $DPKG_PACKAGE_ROOT/DEBIAN/control <<EOL
Package: config-manager
Version: $VERSION
Section: base
Priority: optional
Architecture: amd64
Depends:
Maintainer: Gabor Vereb <gabor@vereb.it>
Description:

EOL

dpkg-deb --build $DPKG_PACKAGE_ROOT

exec tail -f /dev/null
