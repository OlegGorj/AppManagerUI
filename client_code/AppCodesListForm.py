from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ._anvil_designer import AppCodesListFormTemplate


class AppCodesListForm(AppCodesListFormTemplate):
  def __init__(self, data=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.set_event_handler('x-app-code-item-click', self.app_code_item_click)
    self._data = data
    self.repeating_panel_1.items = self._data
    
  def app_code_item_click(self, app_code, **event_args):
    print(f'AppCodesListForm: app_code_item_click handler: {app_code}')
    for item in self._data:
      if item['app_code'] == app_code:
        self.parent.raise_event('x-app-code-full-view', data=item)
