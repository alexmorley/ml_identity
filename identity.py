#!/bin/python3

## Simplest Possible Processor ##
import sys
from mltools import processormanager as pm

PM=pm.ProcessorManager()

def do_nothing():
    """
       Do Nothing
    """
    return 0

do_nothing.name="identity.do_nothing"
do_nothing.version="v0.01"

PM.registerProcessor(do_nothing)

from mltools import mdaio

## Second Simplest Possible Processor
def copy_mda(input, output): 
    """
    Copy .mda file from input to output.

    Parameters
    ----------
    input : INPUT
        Path of mda file to read.
    output : OUTPUT
        Path of mda file to write. 
    """
    X=mdaio.readmda(input)
    mdaio.writemda(X,output,dtype='int16')
    return 0

copy_mda.name="identity.copy_mda"
copy_mda.version="v0.01"

PM.registerProcessor(copy_mda)

def double_mda(input, output, chunk):
    """
    Read in chunks of .mda file, double them, write as chunks to output.
    
    Parameters
    ----------
    input : INPUT
        Path of mda file to read.
    output : OUTPUT
        Path of mda file to write. 
    """
    raise(Exception, 'not yet implemented')


if not PM.run(sys.argv):
    exit(-1)
