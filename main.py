from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        # Set window size for mobile-like appearance
        Window.size = (360, 640)
        
        # Create a layout
        layout = BoxLayout(orientation='vertical')
        
        # Add a label
        label = Label(
            text='Hello, Kivy!',
            font_size='24sp',
            color=(1, 1, 1, 1)
        )
        
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyApp().run() 