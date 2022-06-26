from ._anvil_designer import AppCodeFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AppCodeForm(AppCodeFormTemplate):
  def __init__(self, data=None, **properties):
    # Set Form properties and Data Bindings.
    self._data = data

    self.init_components(**properties)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.parent.clear()

