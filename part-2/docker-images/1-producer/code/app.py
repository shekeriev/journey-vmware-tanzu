import random
import platform
from flask import Flask

a = ['Blue', 'Black', 'Yellow', 'White', 'Green', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Red']
b = ['Tigers', 'Lions', 'Crocodiles', 'Horses', 'Donkeys', 'Dogs', 'Cats', 'Bears', 'Pandas', 'Coalas', 'Chameleons', 'Lizards']
c = ['Fat', 'Fast', 'Slow', 'Tall', 'Short', 'Weak', 'Strong', 'Slim']
d = ['Eat', 'Dream', 'Like', 'Adore', 'Trow', 'Love', 'Dislike']
e = ['Oranges', 'Bananas', 'Tomatoes', 'Potatoes', 'Onions', 'Cucumbers', 'Nuts']

app = Flask(__name__)

@app.route('/')
def main():
  s = "<h5>Recently discovered facts:</h5>\n"
  s = s + "<ul>\n"
  for i in range(1, 6):
    s = s + "<li>" + a[random.randrange(10)] + " " + b[random.randrange(11)] + " Are " + c[random.randrange(7)] + " And " + d[random.randrange(6)] + " " + e[random.randrange(6)] + "</li>\n"
  s = s + "</ul>\n"
  s = s + "<hr>\n"
  s = s + "<small><i>Served by <b>" + platform.node() + "</b></i></small>\n"
  return s