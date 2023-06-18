from ._anvil_designer import Owned_PageTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Nft_Item import Nft_Item

class Owned_Page(Owned_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.loadboard()
  def render_nfts(self, nam):
    alert("Feature To be Added!")
  def loadboard(self):
    nfts = anvil.server.call("get_my_nfts")
    if len(nfts) > 0:
      self.LB_NoNfts.visible = False
    board_panel = GridPanel()
    for i, nft in enumerate(nfts):
      c = Nft_Item(name = nft['name'], description = nft['decription'], button_text = f"REVOKE", image = nft['image'], button_callback = self.render_nfts) 
      board_panel.add_component(c, row=str(i//3), width_xs=4)
    self.CP_board.add_component(board_panel)
