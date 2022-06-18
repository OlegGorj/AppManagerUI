from ._anvil_designer import AppCodeShortViewTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..AppCodeFullView import AppCodeFullView


class AppCodeShortView(AppCodeShortViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def app_code_link_click(self, **event_args):
    """"""
    print(f'app code: {self.app_code_label.text}')
    # Notification(f'{self.app_code_label.text}').show()
    # self.parent.add_component(AppCodeFullView())
    # if confirm("Are you sure you want to delete {}?".format(self.item['title'])):
    
    self.parent.raise_event('x-app-code-full-view', app_code=self.app_code_label.text)


    