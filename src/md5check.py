#!/usr/bin/env python
#########################################################################
# File Name: forEveryFile.py
# Author: xhp
# mail: xiehuipeng@semptian.com
# Created Time: 2016-01-21
#########################################################################
# -*-coding:utf-8-*-

import os, sys
import hashlib

def foreveryfile(path, func=None, *args):
    if not os.path.exists(path):
        sys.stderr.write('{0} No such directory\n'.format(path))
        return False
    for parent, dirs, files in os.walk(path):
        #print 'path={0}, parent={1}'.format(path, parent)
        #for d in dirs:
        #print dirs
        for f in files:
            fname = os.path.join(parent,f)
            if func:
                func(fname, *args)
    return True

def md5sum(filename, func=None, *args):
    """
    if not os.path.isfile(filename):
        sys.stderr.write('{0} is not a file\n'.format(filename))
        return None"""
    fp = open(filename, 'r')
    content = fp.read();
    fp.close()
    fmd5 = hashlib.md5(content).hexdigest()
    #print 'md5 = ', fmd5
    if func:
        return func(filename, fmd5, *args)
    else:
        return fmd5
    
def saveas(oldname, newname, dealnew=None, path=None):
    if path:
        pass
    else:
        if dealnew:
            newname = dealnew(newname)
        if oldname == newname:
            return True
        #print 'newname', newname
        os.rename(oldname, newname)
        
def md5rename(path='./'):
    foreveryfile(path, md5sum, saveas, lambda o:'{}.jpg'.format(o))
    
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        #print path
        foreveryfile(path, md5sum, saveas, lambda o:'{}.jpg'.format(o))
    else:
        print 'plesase input path'