from kivy.app import App
from kivy.uix.button import Button


class FirstKivyApp(App):
    def build(self):
        return Button(
            text='Button',
            pos=(50, 50),
            size_hint=(0.1, 0.10))


if __name__ == '__main__':
    FirstKivyApp().run()
