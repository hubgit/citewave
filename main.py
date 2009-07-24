#!/usr/bin/env python

import logging
import os
import wsgiref.handlers

from google.appengine.api.labs import taskqueue
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

def DocumentHandler():
  return 1

def main():
  application = webapp.WSGIApplication([
      (r'/document', DocumentHandler),
  ], debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()

