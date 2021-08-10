#!/usr/bin/python
import os
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/streetcube/")
# sys.path.insert(0,"/home/parth/Documents/streetcube/")

from streetcube import app as application
application.secret_key = '1425630poijuytpoi4'

if __name__ =="__main__":
	application.run(debug=True)