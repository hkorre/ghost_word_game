#!/usr/bin/env python2.7

from bot import Bot
from word_list import Word_List


class Game_Engine:

    def __init__(self):
        self.players = []
        self.wordList = Word_List()
        self.is_gameOver = False
        self.turn = 0
        self.fragment = ''

        num_humans = int(input("How many human players? "))
        for i in range(num_humans):
            entry = {}
            name = 'Human ' + str(i)
            entry['name'] = name
            entry['is_human'] = True
            entry['object'] = None
            self.players.append(entry)

        num_bots = int(input("How many bots? "))
        for j in range(num_bots):
            entry = {}
            name = 'Bot ' + str(j)
            entry['name'] = name
            entry['is_human'] = False
            entry['object'] = Bot(j)
            self.players.append(entry)

        print("Game_Engine created.")

    def get_is_gameOver(self):
        return self.is_gameOver

    def _is_validFragment(self, _fragment):
        sublist = self.wordList.get_sublist(_fragment)
        if self.wordList.is_wordOfFour(_fragment):
            return False
        elif len(sublist) >= 2:
            return True
        elif len(sublist) == 1 and sublist[0] != _fragment:
            return True
        return False

    def play_turn(self):
        print('\n')

        letter = None

        player_idx = self.turn % len(self.players)

        player_name = self.players[player_idx]['name']
        is_human = self.players[player_idx]['is_human']

        print('Turn ' + str(self.turn) + '.')
        print('Player ' + player_name + ' turn.')
        print('Fragment is ' + self.fragment + '.')

        if is_human is True:
            letter = raw_input("What letter do you pick? ")

        else:
            bot = self.players[player_idx]['object']
            letter = bot.pick_letter(self.fragment)


        if letter is None:
            self.is_gameOver = True
            print('No valid letter pick!')
            return


        self.fragment = self.fragment + letter
        is_validFragment = self._is_validFragment(self.fragment)

        if is_validFragment is False:
            self.is_gameOver = True
            print('Invalid letter pick!')
            return
            
        print('Letter picked is - ' + letter)

        self.turn += 1




if __name__ == "__main__":
    game = Game_Engine()
    while game.get_is_gameOver() is not True:
        game.play_turn()
    print("GAME OVER!")


