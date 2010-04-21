
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath( __file__ )))
sys.path.append(os.path.dirname(os.path.realpath( __file__ )) + '/labs')

import pyroutes
from pyroutes import application

import labs.web.index


if __name__ == '__main__':
    from pyroutes import utils
    utils.devserver(application)
