from ._anvil_designer import HomeFormTemplate
from anvil import *

class HomeForm(HomeFormTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.parent.clear()

