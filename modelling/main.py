from markov_chain import MarkovChain


if __name__ == '__main__':
    print("Creating Markov Chain...")

    markov_chain = MarkovChain()
    markov_chain.learn("I am Sam. Sam I am. I do not like green eggs and ham.")
    markov_chain.display_memory()
