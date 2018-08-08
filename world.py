import location


class world:

    name = ''
    age = 0

    width = 0
    height = 0

    density = 0

    def __init__(self, name, width, height, density):
        self.name = name
        self.width = width
        self.height = height
        self.density = density
