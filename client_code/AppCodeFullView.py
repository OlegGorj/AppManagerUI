from ._anvil_designer import AppCodeFullViewTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AppCodeFullView(AppCodeFullViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self._app_code = ""
    

  @property
  def app_code(self):
    return self._app_code

  @app_code.setter
  def app_code(self, value):
    self._app_code = value