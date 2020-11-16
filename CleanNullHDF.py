#!/usr/bin/env python

# script supports either python2 or python3
#
# Attempts to do HTTP Gets with urllib2(py2) urllib.requets(py3) or subprocess
# if tlsv1.1+ isn't supported by the python ssl module
#
# Will download csv or json depending on which python module is available
#

import os
import sys

def cleanFile(filepath):
    if os.path.getsize(filepath)<10240:
        print(filepath+"is removed and the size is "+ str(os.path.getsize(filepath)));
        os.remove(filepath);

def cleanFiles(filepath):
    fileList = os.listdir(filepath);
    for file in fileList:
        filepathName = os.path.join(filepath, file);
        print(filepathName);
        if os.path.isdir(filepathName):
            cleanFiles(filepathName);
        elif os.path.isfile(filepathName):
            cleanFile(filepathName);

if __name__ == '__main__':
    try:
        filepath = "ndvi";
        cleanFiles(filepath);
    except KeyboardInterrupt:
        sys.exit(-1);
