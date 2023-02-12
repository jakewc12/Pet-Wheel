import xdrlib
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout

class WidgetsExample(GridLayout):
    my_text = StringProperty("0")
    count = 0
    count_enable = BooleanProperty(False)
    def on_button_click(self):
        if self.count_enable:
            self.count+=1
            self.my_text = str(self.count)
    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            # OFF
            widget.text = "OFF"
            self.count_enable = False
        else:
            # ON
            widget.text = "ON"
            self.count_enable = True

class StackLayoutExample(StackLayout):
    pass
   #def __init__(self, **kwargs):
    #   super().__init__(**kwargs)
    #   l = Label(text="body",font_size='20sp',size_hint=(None,None),size=(dp(500),dp(500)))
    #   self.add_widget(l)
       #for i in range(0,10):
       #     b = Label(text=str(i+1), size_hint=(None,None),size=(dp(100),(dp(100))))
       #     self.add_widget(b)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass
#class BoxLayoutExample(BoxLayout):
 #   pass
""""
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="A")
        self.add_widget(b1)
        self.add_widget(b2)
"""

TheLabApp().run()