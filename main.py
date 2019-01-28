from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config
from gameplayer import GamePlayer
from random import randint


class TicTacToeApp(App):

    title = 'Tic Tac Toe'
    board = []
    choices = ["X","O"]
    game_over = False
    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8], # Horizontal
        [0,3,6], [1,4,7], [2,5,8], # Vertical
        [0,4,8], [2,4,6]           # Diagonal
    ]


    # On application build handler
    def build(self):
        Config.set('graphics', 'width', '450')
        Config.set('graphics', 'height', '450')
        Config.set('graphics','resizable', False)
        self.layout = StackLayout()
        for x in range(9):
            bt = Button(text='',color= (0.8,0.8,0.8,1), font_size=120, width=150, height=150, size_hint=(None, None), id=str(x), background_color=(0.4, 0.65, 0.90, 1.0))
            bt.bind(on_release=self.btn_pressed)
            self.board.append(bt)
            self.layout.add_widget(bt)
        return self.layout

    # On application start handler
    def on_start(self):
        self.init_players();

    # On button pressed handler
    def btn_pressed(self, button):

        if len(button.text.strip()) < 1: # Continue only if the button has no mark on it...
            button.text = self.player
            self.bot.make_move(self.board, self.winning_combos)
            self.check_winner()

    # Initializes players
    def init_players(self):
        self.bot = GamePlayer(self.choices[randint(0,1)]);
        self.player = "X" if self.bot.choice == "O" else "O"
        if randint(0,1) == 1:
            self.bot.make_move(self.board, self.winning_combos)
            greeting = "Hello Player! Bot plays first! You are playing with \"" + self.player + "\""
        else:
            greeting = "Hello Player! You are playing with \"" + self.player + "\""
        self.popup_message(greeting)


    # Checks winner after every move...
    def check_winner(self):
        for combo in self.winning_combos:
            if self.board[combo[0]].text == self.board[combo[1]].text == self.board[combo[2]].text and self.board[combo[0]].text != '':
                self.game_over = True
                if self.board[combo[0]].text == self.player:
                    self.popup_message('Player wins!')
                else:
                    self.popup_message('Bot wins!')


    # Resets game state by deleting button values...
    def reset_game(self, popup):
        if self.game_over:
            for button in self.board:
                button.text = ''
            self.game_over = False

    def popup_message(self, msg, title="Welcome!"):
        popup = Popup(title=title, content=Label(text=msg), size=(435, 100), size_hint=(None, None))
        popup.bind(on_dismiss=self.reset_game)
        popup.open()


if __name__ == '__main__':
    TicTacToeApp().run()
