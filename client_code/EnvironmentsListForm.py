from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ._anvil_designer import EnvironmentsListFormTemplate
class EnvironmentsListForm(EnvironmentsListFormTemplate):
  def __init__(self, data=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.set_event_handler('x-item-click', self.item_click)
    self._data = data
    self.repeating_panel_1.items = self._data
    
  def item_click(self, env_name, **event_args):
    for item in self._data:
      if item['name'] == env_name:
        self.parent.raise_event('x-env-full-view', data=item)
        print(f'EnvironmentsListForm: raising event: {env_name}')
