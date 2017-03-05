#!/usr/bin/env python

'''

pull.py: wrapper for "pull" for Singularity Hub command line tool.

ENVIRONMENTAL VARIABLES that are found for this executable:


   SINGULARITY_CONTAINER: maps to container name: shub://vsoch/singularity-images
   SINGULARITY_ROOTFS: the root file system location
   SINGULARITY_HUB_PULL_FOLDER: maps to location to pull folder to
   SINGULARITY_METADATA_DIR: if defined, will write paths to file pulled here


Copyright (c) 2016-2017, Vanessa Sochat. All rights reserved. 

"Singularity" Copyright (c) 2016, The Regents of the University of California,
through Lawrence Berkeley National Laboratory (subject to receipt of any
required approvals from the U.S. Dept. of Energy).  All rights reserved.
 
This software is licensed under a customized 3-clause BSD license.  Please
consult LICENSE file distributed with the sources of this project regarding
your rights to use or distribute this software.
 
NOTICE.  This Software was developed under funding from the U.S. Department of
Energy and the U.S. Government consequently retains certain rights. As such,
the U.S. Government has been granted for itself and others acting on its
behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software
to reproduce, distribute copies to the public, prepare derivative works, and
perform publicly and display publicly, and to permit other to do so. 


'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append('..')

from shub.main import PULL
from shell import get_image_uri
from logman import logger
import os
import sys


def main():
    '''main is a wrapper for the client to hand the parser to the executable functions
    This makes it possible to set up a parser in test cases
    '''
    logger.info("\n*** STARTING SINGULARITY HUB PYTHON PULL ****")
    from defaults import LAYERFILE, DISABLE_CACHE, getenv

    # What image is the user asking for?
    container = getenv("SINGULARITY_CONTAINER", required=True)
    pull_folder = getenv("SINGULARITY_HUB_PULL_FOLDER")
    
    image_uri = get_image_uri(container)
    
    if image_uri == "shub://":

       additions = PULL(image=container,
                        pull_folder=pull_folder,
                        layerfile=LAYERFILE)

    else:
        logger.error("uri %s is not currently supported for pull. Exiting.",image_uri)
        sys.exit(1)


if __name__ == '__main__':
    main()