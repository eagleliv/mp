from django.shortcuts import render

# class Game_Utils():
#     def game(self, request):
#         if request.POST:
#             h = request.POST.get('hhh')
#             print(h)
#         return h

class Hero():
    def __init__(self, name = 100, hp = 100, level = 1, mp = 100, streight = 100, stamina = 100):
        self.name = name
        self.hp = hp
        self.level = level
        self.mp = mp
        self.streight = streight
        self.stamina = stamina
        self.character = {'Name': self.name, 'health point': self.hp, 'level': self.level, 'manna point': self.mp, 'streight': self.streight, 'stamina': self.stamina}

    def show_character(self):
        return self.character

    def enemy_move(self):
        from random import randint
        self.hp -= (randint(1, 50) - randint(1, 50))
        self.character['health point'] = self.hp
        print('Enemy damage + Health point restore ->', self.hp)

    # def your_move(self, request):
    #     while True:
    #         # just_move = int(input('Input move (in steps) -> '))
    #         # hit = int(input('Input numbers of hit -> '))
    #         # evasion = int(input('Input numbers of evasion -> '))
    #         # super_hit = int(input('Input numbers of super hit -> '))
    #         # defend = int(input('Input defend -> '))
    #
    #         if (just_move + hit * 8 + evasion * 9 + defend * 12) > self.character['stamina'] or (hit * 11 + defend * 6) > self.character['streight'] or (evasion * 16) > self.character['manna point']:
    #             print('Error. Please try again')
    #         else:
    #             if (self.character['stamina'] - (just_move + hit * 8 * 3 + evasion * 9 + defend * 12)) < 50:
    #                 super_hit = 0
    #                 print('Cant do super hit')
    #             break
    #
    #
    #     self.stamina -= (just_move + hit * 8 + evasion * 9 + defend * 12 + super_hit - just_move * 1.2)
    #     self.streight -= (hit * 11 + defend * 6 - hit * 1.2)
    #     self.mp -= (evasion * 16 - evasion * 1.2)
    #
    #     self.character['stamina'] = self.stamina
    #     self.character['streight'] = self.streight
    #     self.character['manna point'] = self.mp
    #
    #     print('\n' + 'Character after your the move ')
    #
    #     return self.enemy_move(), self.show_character()
