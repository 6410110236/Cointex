from kivy.app import App

import random

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Rectangle



#Check collides
def collides(rect1, rect2):
    r1x, r1y = rect1[0]
    r2x, r2y = rect2[0]
    r1w, r1h = rect1[1]
    r2w, r2h = rect2[1]

    return (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y)


#Class Main Menu
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        #self.sound = SoundLoader.load('music1.mp3')
        self.soundButton = SoundLoader.load('button1.mp3')

        layout1 = FloatLayout()

        background = Image(source='screen2.jpg', allow_stretch=True, keep_ratio=False)
        layout1.add_widget(background)

        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.image = Image(source='alice-aris.gif', size_hint=(None, None), size=(200, 200))
        layout.add_widget(self.image)

        self.multi_button = Button(text='Multi Player', on_press=self.switch_to_Multi,size_hint=(None, None), size=(200, 50))
        self.multi_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.multi_button)

        self.setting_button = Button(text='Setting', size_hint=(None, None), size=(200, 50) )
        self.setting_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.setting_button)
        

        self.add_widget(layout1)
        self.add_widget(layout)

    def switch_to_Multi(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'multi45'


    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music1.mp3')
        if self.sound:
            self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

#Multi 45 Mode
class GameMultiCoin45Screen(Screen) :
    def __init__(self, **kw):
        super(GameMultiCoin45Screen, self).__init__(**kw)
        self.game_multi_45_widget = GameMultiCoin45()
        self.add_widget(self.game_multi_45_widget)

        self.soundButton = SoundLoader.load('button1.mp3')
        self.soundButton.volume = 0.3  # ตั้งระดับเสียงเพลงใหม่
        self.soundwin = SoundLoader.load('winsound.mp3')
        self.soundwin.volume = 1  # ตั้งระดับเสียงเพลงใหม่

        # Add a "Stop Game" button
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(200, 50), pos_hint={'top': 0.95, 'right': 1})
        self.button_stop_game = Button(text='Stop Game', on_press=self.stop_game, size_hint=(None, None), size=(180, 50))
        layout.add_widget(self.button_stop_game)
        self.add_widget(layout)
        
        self.is_game_running = True  # Flag to track the state of the game
        self.schedule = None  # Initialize the schedule variable

    def stop_game(self, instance):
        self.soundButton.play() 
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()

            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Pause', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep1win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()

            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Player1 Win!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep2win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()

            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Player2 Win!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gameDraw(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()

            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Draw!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def restart_game(self, instance):
        self.soundButton.play() 
        self.sound.play()
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
            # Start the countdown timer
            self.start_countdown()

            # Dismiss the Popup
            self.popup.dismiss()

            # Reset character positions and scores
            self.game_multi_45_widget.hero.pos = (250, 250)
            self.game_multi_45_widget.monster.pos = (1700, 250)
            self.game_multi_45_widget.scorep1 = 0
            self.game_multi_45_widget.scorep1_label.text = "Score Player 1 : 0"
            self.game_multi_45_widget.scorep2 = 0
            self.game_multi_45_widget.scorep2_label.text = "Score Player 2 : 0"

            # Reset timer label
            self.game_multi_45_widget.timer_label.text = "Time left: 45 seconds"
            self.countdown_time = 45

    
            self.game_multi_45_widget._keyboard = Window.request_keyboard(self.game_multi_45_widget._on_keyboard_closed, self.game_multi_45_widget)
            self.game_multi_45_widget._keyboard.bind(on_key_down=self.game_multi_45_widget._on_key_down)
            self.game_multi_45_widget._keyboard.bind(on_key_up=self.game_multi_45_widget._on_key_up)

            # Switch back to the game screen
            self.manager.current = 'multi45'

    def switch_to_main_menu(self, instance):
        self.soundButton.play() 
        self.restart_game(None)
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
      
        # Close the Popup
        self.popup.dismiss()
        self.game_multi_45_widget.hero.pos = (250,250)
        self.game_multi_45_widget.monster.pos = (1700,250)

        self.game_multi_45_widget.scorep1 = 0
        self.game_multi_45_widget.scorep1_label.text = "Score Player 1 : 0"
        self.game_multi_45_widget.scorep2 = 0
        self.game_multi_45_widget.scorep2_label.text = "Score Player 2 : 0"

        self.game_multi_45_widget.timer_label.text = "Time left: 45 seconds"
        self.countdown_time = 45
    
        # Switch to the main menu screen
        self.manager.current = 'main_menu'

    def on_pre_enter(self, *args):
        # เริ่มต้นนับถอยหลังเมื่อเข้าหน้าจอ
        self.countdown_time = 45  # ระบุเวลาถอยหลังในวินาที
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        # หยุดนับถอยหลังเมื่อออกจากหน้าจอ
        Clock.unschedule(self.schedule)

    def update_timer(self, dt):
        #เรียกใช้ scorep1 จาก class GameMultiCoin45
        self.scorep1 = self.game_multi_45_widget.scorep1 
        self.scorep2 = self.game_multi_45_widget.scorep2 
        # Decrement the countdown time if the game is running
        if self.is_game_running:
            self.countdown_time -= 1
        
            # Update the timer label in your game widget
            self.game_multi_45_widget.timer_label.text = f"Time left: {self.countdown_time} seconds"
 
            if self.countdown_time <= 0:
                # Stop the countdown timer when time runs out
                self.stop_countdown()
                if self.scorep1 > self.scorep2 :
                    self.soundwin.play()
                    self.stop_gamep1win(None)
                if self.scorep1 < self.scorep2 :
                    self.soundwin.play()
                    self.stop_gamep2win(None)
                if self.scorep1 == self.scorep2 :
                    self.soundwin.play()
                    self.stop_gameDraw(None)
 
    def stop_countdown(self):
        if self.schedule is not None:
            # Unschedule the function responsible for updating the countdown timer
            self.schedule.cancel()
    def start_countdown(self):
        if self.is_game_running:  # Check if the game is running
            # Schedule a function to update the countdown timer every second
            self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music4.mp3')
        self.sound.volume = 0.1  # ตั้งระดับเสียงเพลงใหม่
        if self.sound:
            #self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_multi_45_widget.change_character_imageP1(new_image_source)
    def change_character_imageP2(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_multi_45_widget.change_character_imageP2(new_image_source)  

class GameMultiCoin45(Widget) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_label = Label(text="Time left: 45 seconds", pos=(300, 700), size=(200, 200), font_size=20)
        self.add_widget(self.timer_label)

        self.scorep1 = 0
        self.scorep2 = 0

        self.scorep1_label = Label(text="Score Player 1 : 0", pos=(100, 800), size=(200, 200),font_size=40)
        self.add_widget(self.scorep1_label)

        self.scorep2_label = Label(text="Score Player 2 : 0", pos=(500, 800), size=(200, 200),font_size=40)
        self.add_widget(self.scorep2_label)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.move_step, 0)

        self.keepcoinsound = SoundLoader.load('coinkeep.mp3')
        if self.keepcoinsound:
            self.keepcoinsound.volume = 0.7  # ตั้งระดับเสียงเพลงใหม่
        

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='screen10.jpeg', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:

            Line(rectangle=(30, 865, 345, 65), width=2)  # Rectangle around Score Player 1
            Line(rectangle=(430, 865, 345, 65), width=2)
            #generate cat charector
            self.hero = Image(source="character1.png", pos=(250, 250), size=(140, 140))

            #generate monster charector
            self.monster = Image(source="character2.png", pos=(1700, 250), size=(140, 140))

            #generate coins
            self.coin1 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin2 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin3 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))


    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = (value[0], value[0]/2.5)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
       if self.parent.is_game_running and self.parent.manager.current == 'multi45':
            self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        if self.parent.is_game_running and self.parent.manager.current == 'multi45':
            text = keycode[1]
            if text in self.pressed_keys:
                self.pressed_keys.remove(text)
                
    def move_step(self, dt):
        cur_x1 = self.hero.pos[0]
        cur_y1 = self.hero.pos[1]
        step1 = 500 * dt

        # Adjust the hero's position based on key presses
        if 'w' in self.pressed_keys and cur_y1 + step1 + self.hero.height < self.image.height:
            cur_y1 += step1
            print("w")

        if 's' in self.pressed_keys and cur_y1 - step1 > 0:
            cur_y1 -= step1
            print("s")

        if 'a' in self.pressed_keys and cur_x1 - step1 > 0:
            cur_x1 -= step1
            print("a")

        if 'd' in self.pressed_keys and cur_x1 + step1 + self.hero.width < self.image.width:
            cur_x1 += step1
            print("d")

        self.hero.pos = (cur_x1, cur_y1)

        cur_x2 = self.monster.pos[0]
        cur_y2 = self.monster.pos[1]
        step2 = 500 * dt

        if 'i' in self.pressed_keys and cur_y2 + step2 + self.monster.height < self.image.height:
            cur_y2 += step2
            print("i")

        if 'k' in self.pressed_keys and cur_y2 - step2 > 0:
            cur_y2 -= step2
            print("k")

        if 'j' in self.pressed_keys and cur_x2 - step2 > 0:
            cur_x2 -= step2
            print("j")

        if 'l' in self.pressed_keys and cur_x2 + step2 + self.monster.width < self.image.width:
            cur_x2 += step2
            print("l")

        self.monster.pos = (cur_x2, cur_y2)

        if collides((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) or collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)) or collides((self.hero.pos, self.hero.size), (self.coin3.pos, self.coin3.size)):


            self.keepcoinsound.play()

            if collides ((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) == True :
                self.coin1.pos = (random.randint(0, self.image.width - self.coin1.width),
                             random.randint(0, self.image.height - self.coin1.height))
            if collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)) :
                self.coin2.pos = (random.randint(0, self.image.width - self.coin2.width),
                             random.randint(0, self.image.height - self.coin2.height))
            if collides((self.hero.pos, self.hero.size), (self.coin3.pos, self.coin3.size)) :
                self.coin3.pos = (random.randint(0, self.image.width - self.coin3.width),
                             random.randint(0, self.image.height - self.coin3.height))
                
            self.scorep1 += 1
            self.scorep1_label.text = "Score Player 1 : " + str(self.scorep1)

    
        if collides((self.monster.pos, self.monster.size), (self.coin1.pos, self.coin1.size)) or collides((self.monster.pos, self.monster.size), (self.coin2.pos, self.coin2.size)) or collides((self.monster.pos, self.monster.size), (self.coin3.pos, self.coin3.size)):

            self.keepcoinsound.play()


            if collides ((self.monster.pos, self.monster.size), (self.coin1.pos, self.coin1.size)) == True :
                self.coin1.pos = (random.randint(0, self.image.width - self.coin1.width),
                             random.randint(0, self.image.height - self.coin1.height))
            if collides((self.monster.pos, self.monster.size), (self.coin2.pos, self.coin2.size)) :
                self.coin2.pos = (random.randint(0, self.image.width - self.coin2.width),
                             random.randint(0, self.image.height - self.coin2.height))
            if collides((self.monster.pos, self.monster.size), (self.coin3.pos, self.coin3.size)) :
                self.coin3.pos = (random.randint(0, self.image.width - self.coin3.width),
                             random.randint(0, self.image.height - self.coin3.height))
                
            self.scorep2 += 1
            self.scorep2_label.text = "Score Player 2 : " + str(self.scorep2)

class MyGame(App):
    def build(self):
        self.screen_manager = ScreenManager()

        main_menu = MainMenu(name='main_menu')

        game_multi_45 = GameMultiCoin45Screen(name = 'multi45')


        self.screen_manager.add_widget(main_menu)

        self.screen_manager.add_widget(game_multi_45)


        return self.screen_manager

if __name__ == '__main__':
    app = MyGame()
    app.run()