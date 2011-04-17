import os, sys

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(root_dir, 'lib'))

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.appstats import recording
from app import app

if __name__ == '__main__':
    run_wsgi_app(recording.appstats_wsgi_middleware(app))
  