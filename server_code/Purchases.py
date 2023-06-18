import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def charge_user(token, email, nft_idname):
  stripe_customer = anvil.stripe.new_customer(email, token)
  price = app_tables.nfts.get(id_name=nft_idname)["price"]
  user = anvil.users.get_user()
  if user['owned_nfts'] == None:
    user['owned_nfts'] = []
  if nft_idname in user['owned_nfts']:
    return
  result = stripe_customer.charge(amount = price*100, currency = "USD")
  user['owned_nfts'] += [nft_idname]

