from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
import time
class BoxLayoutExample(FloatLayout):
    startHealth = 100
    startSeconds = 1677041749.9353511
    #instead of using this random number for start seconds
    #we should use the time the game was launched
    changedTime = time.time() - startSeconds
    changedValue = changedTime/1800
    #decreases 1 every half day
    changedFinal = 100 -int(changedValue)
    status = "Status: "
    if changedFinal >= 75:
        status += " Healthy"
    elif changedFinal >= 50:
        status += " Hungry"
    elif changedFinal > 0:
        status += " Needs help"
    else:
        status += " Dead"
    
class MainWiget(Widget):
    pass

class PetWheel(App):
    pass

PetWheel().run()