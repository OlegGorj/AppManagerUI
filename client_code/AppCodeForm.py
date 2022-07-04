import json

from ._anvil_designer import AppCodeFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .EnvironmentsListForm import EnvironmentsListForm


class AppCodeForm(AppCodeFormTemplate):
  def __init__(self, data=None, **properties):
    # Set Form properties and Data Bindings.
    self._data = data
    self.column_panel_1.visible = False
    self.column_panel_1.set_event_handler('x-env-full-view', self.env_item_click)
    
    if 'request' in self._data:
      request_obj = json.loads(self._data['request'])
      print(f'request_obj: {request_obj}')
      self.column_panel_1.add_component(EnvironmentsListForm(data=request_obj['environments']))
      self.column_panel_1.visible = True
    
    self.init_components(**properties)

  def env_item_click(self, data, **event_args):
    self.parent.raise_event('x-env-full-view', data=data)

