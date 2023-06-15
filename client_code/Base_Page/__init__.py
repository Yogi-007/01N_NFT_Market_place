from ._anvil_designer import Base_PageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Home_Page import Home_Page
from ..Owned_Page import Owned_Page
class Base_Page(Base_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.go_to_home()
    self.change_sign_in_text()
    # Any code you write here will run before the form opens.
  def go_to_home(self):
    self.content_panel.clear()
    self.content_panel.add_component(Home_Page())
  
  def toggle_owned_link(self):
    self.HL_owned.visible = anvil.users.get_user() != None
  
  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.HL_Sign.text = email
    else:
      self.HL_Sign.text = "Sign In"
    self.toggle_owned_link() 
  
  def HL_title_click(self, **event_args):
    self.go_to_home()

  def HL_owned_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Owned_Page())

  def HL_Sign_click(self, **event_args):
    user = anvil.users.get_user() 
    if user:
      logout = confirm("Do you want to Logout ?")
      if logout:
        anvil.users.logout()
        self.go_to_home()
    else:  
      anvil.users.login_with_form()
    self.change_sign_in_text()
    

    



