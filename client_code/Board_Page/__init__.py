from ._anvil_designer import Board_PageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Nft_Item import Nft_Item
from ..Checkout_Page import Checkout_Page
class Board_Page(Board_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.loadboard()

  def back(self):
    self.CP_board.clear()
    self.loadboard()
  
  def render_checkout(self, name):
    self.CP_board.clear()
    self.CP_board.add_component(Checkout_Page(name, self.back))
  
  def loadboard(self):
    nfts = anvil.server.call("get_all_nfts").search()
    board_panel = GridPanel()
    for i, nft in enumerate(nfts):
      c = Nft_Item(name = nft['name'], description = nft['decription'], button_text = f"Buy: ${nft['price']}", image = nft['image'], button_callback = self.render_checkout) 
      board_panel.add_component(c, row=str(i//3), width_xs=4)
    self.CP_board.add_component(board_panel)