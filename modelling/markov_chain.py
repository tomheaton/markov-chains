import random


class MarkovChain:

    def __init__(self):
        self.memory = {}

    def learn_key(self, key: any, value: any):
        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append(value)

    def learn(self, text: str):
        # Tokenize the text.
        tokens = text.split(" ")
        x = [(tokens[i], tokens[i + 1]) for i in range(0, len(tokens) - 1)]
        for element in x:
            self.learn_key(element[0], element[1])

    def next(self, current_state):
        next_possible = self.memory.get(current_state)

        if not next_possible:
            next_possible = self.memory.keys()

        return random.sample(next_possible, 1)[0]

    def babble(self, amount, state=''):
        if not amount:
            return state

        next_word = self.next(state)

        if not next_word:
            return state

        return state + ' ' + self.babble(amount - 1, next_word)

    def display_memory(self):
        print(f'{self.memory}')
