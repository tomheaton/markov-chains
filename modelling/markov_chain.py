import random


class MarkovChain:

    def __init__(self):
        self.memory = {}

    def learn_key(self, key: any, value: any) -> None:
        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append(value)

    def learn(self, text: str) -> None:
        tokens = text.split(" ")  # Tokenize the text.
        bigrams = [(tokens[i], tokens[i + 1]) for i in range(0, len(tokens) - 1)]
        for bigram in bigrams:
            self.learn_key(bigram[0], bigram[1])

    def next(self, current_state) -> str:
        next_possible = self.memory.get(current_state)

        if not next_possible:
            next_possible = self.memory.keys()

        return random.sample(next_possible, 1)[0]

    def babble(self, amount: int, state: str = '') -> str:
        if not amount:
            return state

        next_word = self.next(state)

        if not next_word:
            return state

        return f'{state} {self.babble(amount - 1, next_word)}'

    def display_memory(self) -> None:
        print(f'{self.memory}')
