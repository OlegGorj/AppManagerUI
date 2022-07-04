from ._anvil_designer import EnvironmentFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EnvironmentForm(EnvironmentFormTemplate):
  def __init__(self, data=None, **properties):
    self.item = data
    self.init_components(**properties)

