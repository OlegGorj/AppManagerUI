from ._anvil_designer import AppCodesListFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AppCodesListForm(AppCodesListFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.content_panel.set_event_handler('x-app-code-full-view', self.app_code_full_view)
    self.repeating_panel_1.set_event_handler('x-app-code-full-view', self.app_code_full_view)


    self.data = [
      {
        'portfolio': 'ccoe', 'app_code': 'abc0', 'active': 'true'
      },
      {
        'portfolio': 'ccoe', 'app_code': 'abc1', 'active': 'true'
      },
      {
        'portfolio': 'ccoe', 'app_code': 'abc2', 'active': 'true'
      }
    ]
    self.repeating_panel_1.items = self.data
    
    print(self.data)
    
  def app_code_full_view(self, app_code, **event_args):
    print(f'AppCodesListForm: app_code_full_view handler: {app_code}')
    self.parent.raise_event('x-app-code-full-view', app_code=app_code)
