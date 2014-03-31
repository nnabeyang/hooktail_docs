from builders.hooktail import HooktailBuilder
from builders.rst import ReSTBuilder

def setup(app):
  app.add_builder(HooktailBuilder)
  app.add_builder(ReSTBuilder)
 
