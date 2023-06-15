from ._anvil_designer import Home_PageTemplate
from anvil import *

class Home_Page(Home_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
