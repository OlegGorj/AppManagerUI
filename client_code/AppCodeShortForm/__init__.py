from ._anvil_designer import AppCodeShortFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AppCodeShortForm(AppCodeShortFormTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)


  def app_code_link_click(self, **event_args):
    # Notification(f'{self.app_code_label.text}').show()
    # self.parent.add_component(AppCodeFullView())
    # if confirm("Are you sure you want to delete {}?".format(self.item['title'])):
    self.parent.raise_event('x-app-code-item-click', app_code=self.app_code_link.text)
    

    