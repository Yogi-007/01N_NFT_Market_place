from ._anvil_designer import Home_PageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Board_Page import Board_Page
class Home_Page(Home_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def BT_visitStore_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.CP_Home.clear()
    self.CP_Home.add_component(Board_Page())
    

