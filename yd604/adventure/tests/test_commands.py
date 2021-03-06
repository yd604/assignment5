from unittest import TestCase
from play import load_advent_dat
from game import Game

class CommandTest(TestCase):

    def setUp(self):
        game = Game()
        load_advent_dat(game)
        self.words = set(w.synonyms[0].text for w in game.vocabulary.values())
        self.words.remove('suspend')

    def test_intransitive_commands_should_not_throw_exceptions(self):
        for word in self.words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
            game.do_command([word])

    def test_transitive_commands_should_not_throw_exceptions(self):
        for word in self.words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
            game.do_command(['enter'])  # so we are next to lamp
            game.do_command([word, 'lamp'])
            
    def test_do_commands_for_the_case_y(self):
        game = Game()
        load_advent_dat(game)
        game.start()
	# This will test if argument to callback is True
	game.yesno_callback = self.assertTrue
	# Run the actual test
	game.do_command(['y'])
        
    def test_do_commands_for_the_case_yes(self):
        game = Game()
        load_advent_dat(game)
        game.start()
	# This will test if argument to callback is True
        game.yesno_callback = self.assertTrue
        game.do_command(['yes'])    
        
    def test_do_commands_for_the_case_n(self):
        game = Game()
        load_advent_dat(game)
        game.start()
	# This will test if argument to callback is False
        game.yesno_callback = self.assertFalse
        game.do_command(['n'])
        
    def test_do_commands_for_the_case_no(self):
        game = Game()
        load_advent_dat(game)
        game.start()
	# This will test if argument to callback is False
        game.yesno_callback = self.assertFalse
        game.do_command(['no'])
        
    def test_do_commands_for_the_case_none(self):
        game = Game()
        load_advent_dat(game)
        game.start()
	# This will test if argument to callback is invalid
        game.yesno_callback = self.assertIsNone
        game.do_command(['None'])
