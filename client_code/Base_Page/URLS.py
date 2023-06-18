import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home_Page import Home_Page
from ..Board_Page import Board_Page
from ..Owned_Page import Owned_Page
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .Base_Page import Module1
#
#    Module1.say_hello()
#
urls = {"home": Home_Page, "board": Board_Page, "my-nfts": Owned_Page}
