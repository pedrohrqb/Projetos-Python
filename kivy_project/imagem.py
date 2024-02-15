from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img = AsyncImage(source ='https://fscl01.fonpit.de/userfiles/6727621/image/2016/HeroS-random/AndroidPIT-super-mario-run.jpg', size_hint=(1, .5), pos_hint={'center_x':.5, 'center_y':.5})
        return img
    
if __name__ == '__main__':
    app = MainApp()
    app.run()