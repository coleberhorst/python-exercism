STATUS_WIN = 1
STATUS_LOSE = -1
STATUS_ONGOING = 0


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.WORD = word
        self.guess_list = []
        self.mask = "*" * len(word)

    def guess(self, char):
        self.remaining_guesses -= 1
        try:
            if char in self.guess_list:
                raise ValueError("{} already guessed for {}".format(char, self.mask))
            elif char in self.WORD:
                self.mask[self.WORD.index(char)] # TODO handle multiple duplicate characters
                print("{} is in {}!".format(char, self.mask))
                self.guess_list.append(char)
            else:
                print("{} is not in {}.".format(char, self.mask))
                self.guess_list.append(char)
        except:
            pass
        print("guessed: {}".format(self.guess_list))

    def get_masked_word(self):
        print(self.mask)

    def get_status(self):
        if self.remaining_guesses < 0 and "*" in self.mask:
            self.status = STATUS_LOSE
        elif "*" not in self.mask:
            self.status = STATUS_WIN
        return self.status
