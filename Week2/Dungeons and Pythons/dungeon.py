class Dungeon:

    def __init__(self, filename):
        self.dungeonfile = open(filename, "r")

    def print_map(self):
        content = self.dungeonfile.read()
        self.dungeonfile.close()
        print (content)
        return content
