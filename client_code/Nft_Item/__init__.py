from ._anvil_designer import Nft_ItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Nft_Item(Nft_ItemTemplate):
  def __init__(self, name, description, image, button_callback, button_text, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.LB_com_name.text = name
    self.LB_com_des.text = description
    self.BT_com.text = button_text
    self.IMG_com.source = image
    self.button_callback = button_callback
    # Any code you write here will run before the form opens.

  def BT_com_click(self, **event_args):
    self.button_callback(self.LB_com_name.text.lower())
    

