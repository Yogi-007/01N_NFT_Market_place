from ._anvil_designer import Checkout_PageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Checkout_Page(Checkout_PageTemplate):
  def __init__(self, id, back_cb, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_checkout(id)
    self.back_cb = back_cb

  def update_checkout(self,id):
    nft = anvil.server.call('get_nft_details', id)
    self.LB_name.text = nft["name"]
    self.LB_decription.text = nft["decription"]
    self.LB_price.text = f'${nft["price"]} USD'
    self.IMG_checkout.source = nft["image"] 

  def BT_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_cb()

