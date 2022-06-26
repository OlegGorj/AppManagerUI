from ._anvil_designer import AppCodeFullViewTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AppCodeFullView(AppCodeFullViewTemplate):
  def __init__(self, data=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self._app_code = ""
    
    self._data = data
    print(f'AppCodeFullView: init: data: {data}')
    