from ._anvil_designer import EnvironmentShortFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EnvironmentShortForm(EnvironmentShortFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def item_click(self, **event_args):
    self.parent.raise_event('x-item-click', env_name=self.env_name_link.text)

