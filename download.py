#!/usr/bin/env python2

import os
from os import path
import urlparse
import urllib

items = set()

if not path.isdir("images"):
    os.makedirs("images")

with open("links", "r") as f:
    for item in f:
        item = item.strip()
        if item == "" or item[0] == '#':
            continue
        name = path.basename(urlparse.urlsplit(item).path)
        if name in items:
            continue
        items.add(name)
        f = path.join("images", name)
        if path.isfile(f):
            print "Skipping '%s', already downloaded!" % item
            continue
        print "Downloading '%s'..." % item
        urllib.urlretrieve(item, f)

for f in os.listdir("images"):
    if not path.basename(f) in items:
        print "Deleting '%s'..." % path.basename(f)
        os.unlink(path.join("images", f))
