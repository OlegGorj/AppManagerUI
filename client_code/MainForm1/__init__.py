from ._anvil_designer import MainForm1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .. import Globals
from ..WelcomeForm import WelcomeForm

from ..AppCodesListForm import AppCodesListForm
from ..AppCodeForm import AppCodeForm


class MainForm1(MainForm1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel_1.set_event_handler('x-app-code-full-view', self.app_code_full_view)


  def reset_links(self, **event_args):
    self.link_1.role = ''
    self.link_2.role = ''
    
  def link_1_click(self, **event_args):
    global number_of_clicks
    self.reset_links()
    self.link_1.role = 'selected'
    self.content_panel_1.clear()
    self.content_panel_1.add_component(WelcomeForm())
    # Globals.number_of_clicks += 1

  def link_2_click(self, **event_args):
    self.link_2.role = 'selected'
    self.content_panel_1.clear()
    self.content_panel_1.add_component(AppCodesListForm())

  def app_code_full_view(self, app_code, **event_args):
    print('MainForm1: app_code_full_view handler')
    self.content_panel_2.clear()
    self.content_panel_2.add_component(AppCodeForm(app_code=app_code))

