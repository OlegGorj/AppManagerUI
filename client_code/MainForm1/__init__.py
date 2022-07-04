from ._anvil_designer import MainForm1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..WelcomeForm import WelcomeForm

from ..AppCodesListForm import AppCodesListForm
from ..AppCodeShortForm import AppCodeShortForm
from ..AppCodeForm import AppCodeForm
# from ..AppCodeFullView import AppCodeFullView
from ..EnvironmentForm import EnvironmentForm
from .. import Globals


class MainForm1(MainForm1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.content_panel_1.set_event_handler('x-app-code-full-view', self.app_code_full_view)
    self.content_panel_2.set_event_handler('x-env-full-view', self.env_full_view)
    
    self.content_panel_1.visible = False
    self.content_panel_2.visible = False
    self.content_panel_3.visible = False
    self._title = RichText(align='center', content='', format='markdown',font_size='24', spacing_above=0, spacing_below=0, tag='title')
    self.title_card.add_component(self._title)

  def reset_links(self, **event_args):
    self.link_1.role = ''
    self.link_2.role = ''
  
  def link_1_click(self, **event_args):
    self._title.content = 'Welcome'

    self.reset_links()
    self.link_1.role = 'selected'
    self.content_panel_1.clear()
    self.content_panel_1.add_component(WelcomeForm())

  def app_codes_link_click(self, **event_args):
    self._title.content = 'App Codes'
    self.link_2.role = 'selected'
    self.content_panel_1.clear()
    self.content_panel_1.add_component(AppCodesListForm(data=Globals.onbordings), slot="default")
    self.content_panel_1.visible = True
 
  def app_code_full_view(self, data, **event_args):
    self.content_panel_2.clear()
    self.content_panel_2.add_component(AppCodeForm(data=data))
    self.content_panel_2.visible = True

  def env_full_view(self, data, **event_args):
    print(f'MainForm1: env_full_view: data: {data}')
    self.content_panel_3.clear()
    self.content_panel_3.add_component(EnvironmentForm(data=data))
    self.content_panel_3.visible = True
    
  def call_api(self):
    import requests
    URL = "http://maps.googleapis.com/maps/api/geocode/json"
    location = "delhi technological university"
    PARAMS = {'address':location}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    
  def applications_link_click(self, **event_args):
    self._title.content = 'Applications'
    self.link_3.role = 'selected'
