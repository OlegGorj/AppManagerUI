from ._anvil_designer import MainForm1Template
from anvil import *

from .. import Globals
from ..HomeForm import HomeForm
# from ..AppCodesFormV1 import AppCodesFormV1
from ..AppCodesListForm import AppCodesListForm


class MainForm1(MainForm1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def reset_links(self, **event_args):
    self.link_1.role = ''
    self.link_2.role = ''
    
  def link_1_click(self, **event_args):
    global number_of_clicks
    self.reset_links()
    self.link_1.role = 'selected'
    self.content_panel.clear()
    self.content_panel.add_component(HomeForm())
    Globals.number_of_clicks += 1

  def link_2_click(self, **event_args):
    self.link_2.role = 'selected'
    self.content_panel.clear()
    self.content_panel.add_component(AppCodesListForm())


