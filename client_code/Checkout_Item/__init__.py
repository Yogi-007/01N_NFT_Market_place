from ._anvil_designer import Checkout_ItemTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe
class Checkout_Item(Checkout_ItemTemplate):
  def __init__(self, id, back_cb, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_checkout(id)
    self.back_cb = back_cb

  def update_checkout(self,id):
    nft = anvil.server.call('get_nft_details', id)
    self.nft = nft
    self.LB_name.text = nft["name"]
    self.LB_decription.text = nft["decription"]
    self.LB_price.text = f'${nft["price"]} USD'
    self.IMG_checkout.source = nft["image"] 

  def BT_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_cb()

  def BT_purchase_click(self, **event_args):
    
    if anvil.users.get_user() == None:
      anvil.users.login_with_form()
    user = anvil.users.get_user()
    if user == None:
      alert("Please Sign In to Buy!")
      return
    if user['owned_nfts'] and self.nft['id_name'] in user['owned_nfts']:
      alert("You already own this NFT!")
      return
    token, info = stripe.checkout.get_token(amount=self.nft['price']*100, currency="USD", title=self.nft['name'], description=self.nft['decription'])
    try:
      anvil.server.call("charge_user", token, user["email"], self.nft["id_name"])
      alert("Purchase Successful")
    except Exception as e:
      alert(str(e))
