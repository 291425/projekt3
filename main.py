from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import shuffle
global points, counts




points = [
        ['paryz.jpg', 48.858347  , 2.29455],
        ['krakow.jpg', 50.061389, 19.938333],
        ['egipt.jpg', 30.05, 31.233333],
        ['barcelona.jpg', 41.387917, 2.169919],
        ['ny.jpg', 40.716667, -74],
        ['palackultury.jpg', 52.232222, 21.008333],
        ['bigben.jpg', 53.430864, -2.960692],
        ['rio.jpg', -22.951389, -43.210833],
        ]
shuffle(points)
counts=len(points)
class Form(BoxLayout):   
    def draw_marker(self):
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text = "{:.5f}".format(self.latitude)
        self.search_long.text = "{:.5f}".format(self.longitude)
        
    def check_points(self):
        r=3
        
        if self.my_image.source in ['start.jpg','meta.jpg']:
            pass
        else:
            if (self.latitude-self.curr_img[1])**2 + (self.longitude -self.curr_img[2])**2 <= r**2:
                self.my_score.text=str(int(self.my_score.text)+1)
                self.my_button_check.disabled = True
            else:
                self.my_button_check.disabled = True
        
            
        
                
    def next_img(self):
        self.my_button_check.disabled = False
        if len(points)>=1:
            self.curr_img=points.pop()
            self.my_image.source = self.curr_img[0]
            self.my_button_next.text='Dalej'
        else:
            self.my_image.source = 'meta.jpg'
            self.my_button_next.disabled = True
            self.my_button_check.disabled = True
            self.my_button_next.text='Quiz skończony'
    
    
        


class MapViewApp(App):
    pass

MapViewApp().run()