class Player(dict):
    def __init__(self, id, name):
        dict.__init__(self, id=id, name=name)
        self.id = id
        self.name = name
