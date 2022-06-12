from ._anvil_designer import AppCodeShortViewTemplate
from anvil import *

class AppCodeShortView(AppCodeShortViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def app_code_link_click(self, **event_args):
    """"""
    print(f'app code: {self.app_code_label.text}')

