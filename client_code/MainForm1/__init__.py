from ._anvil_designer import MainForm1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..WelcomeForm import WelcomeForm

from ..AppCodesListForm import AppCodesListForm
from ..AppCodeForm import AppCodeForm
from ..AppCodeFullView import AppCodeFullView
from .. import Globals


class MainForm1(MainForm1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.content_panel_1.set_event_handler('x-app-code-full-view', self.app_code_full_view)
    self.content_panel_1.visible = False
    self.content_panel_2.visible = False
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

  def link_2_click(self, **event_args):
    self._title.content = 'App Codes'

    _data = [
      {
        'id':'0', 'portfolio': 'ccoe', 'app_code': 'abc0', 'active': 'true', 'status': 'received'
      },
      {
         'id':'2', 'portfolio': 'ccoe', 'app_code': 'abc1', 'active': 'true', 'status': 'received'
      },
      {
         'id':'10', 'portfolio': 'ccoe', 'app_code': 'abc2', 'active': 'true', 'status': 'received'
      }
    ]
    self.link_2.role = 'selected'
    self.content_panel_1.clear()
    self.current_form = AppCodesListForm(data=_data)
    self.content_panel_1.add_component(self.current_form, slot="default")
    self.content_panel_1.visible = True
 
  def app_code_full_view(self, data, **event_args):
    print(f'MainForm1: app_code_full_view handler: data: {data}')
    self.content_panel_2.clear()
    self.content_panel_2.add_component(AppCodeForm(data=data))
    self.content_panel_2.visible = True

  def call_api(self):
    import requests
    URL = "http://maps.googleapis.com/maps/api/geocode/json"
    location = "delhi technological university"
    PARAMS = {'address':location}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    