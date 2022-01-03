
class MarkovChain:

    def __init__(self):
        self.memory = {}

    def learn_internal(self, key: any, value: any):
        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append(value)

    def learn(self, text: str):
        # Tokenize the text.
        tokens = text.split(" ")
        x = [(tokens[i], tokens[i+1]) for i in range(0, len(tokens) - 1)]
        for element in x:
            self.learn_internal(element[0], element[1])

    def display_memory(self):
        print(f'{self.memory}')
