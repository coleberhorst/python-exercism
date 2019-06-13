STATUS_WIN = 1
STATUS_LOSE = -1
STATUS_ONGOING = 0


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.WORD = word
        self.guesses = set()

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game is over.")
        if char not in self.guesses and char in self.WORD:
            self.guesses.add(char)
            if all(c in self.guesses for c in self.WORD):
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join(c if c in self.guesses else '_' for c in self.WORD)

    def get_status(self):
        return self.status
