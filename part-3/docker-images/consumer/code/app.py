import platform
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  with open('app.tpl') as f:
    template = f.read()

  result = template.replace("{HOST}", platform.node())

  response = requests.get('http://producer:5000')

  result = result.replace("{FACTS}", response.text)

  return result