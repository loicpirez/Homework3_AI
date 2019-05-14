#!/usr/bin/env python
import flask
import sys
sys.path.insert(0, 'src/')
from homework import getIAResult

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
  return getIAResult()

app.run()


