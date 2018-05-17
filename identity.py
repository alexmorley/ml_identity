#!/bin/python3

import sys
from mltools import processormanager as pm
#import identity

PM=pm.ProcessorManager()

def do_nothing():
    """
       Do Nothing
    """
    return 0

do_nothing.name="identity.do_nothing"
do_nothing.version="v0.01"

PM.registerProcessor(do_nothing)

if not PM.run(sys.argv):
    exit(-1)
