class card:

    def __init__(self, name, cost, discard_reward, production, color, reward=0):
        self.name = name
        self.cost = cost
        self.discard_reward = discard_reward
        self.production = production
        self.reward = reward
        self.color = color

class cost:

    def __init__(self, grey, black, green, yellow, blue):
        self.grey = grey
        self.black = black
        self.green = green
        self.yellow = yellow
        self.blue = blue


class production:

    def __init__(self, grey, black, green, yellow, blue):
        self.grey = grey
        self.black = black
        self.green = green
        self.yellow = yellow
        self.blue = blue

class discard_reward:

    def __init__(self, grey, black, green, yellow, blue):
        self.grey = grey
        self.black = black
        self.green = green
        self.yellow = yellow
        self.blue = blue
