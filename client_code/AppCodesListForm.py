from ._anvil_designer import AppCodesListFormTemplate
from anvil import *

class AppCodesListForm(AppCodesListFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


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
    

