from kivy.app import App
from kivy.uix.button import Button


class SpecialButton(Button):
    def __init__(self, **kwargs):
        super(SpecialButton, self).__init__(**kwargs)
        self.text = 'Button'
        self.pos = (50, 50)
        self.size_hint = (0.1, 0.1)


class FirstKivyApp(App):
    def build(self):
        return SpecialButton()


if __name__ == '__main__':
    FirstKivyApp().run()
