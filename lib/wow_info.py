class WOWStage:
    levels = []

    def __init__(self, country, landmark, levels_href):
        self.country = country
        self.landmark = landmark
        self.levels_href = levels_href


class WOWLevel:
    answers = []

    def __init__(self, level_number, letters, answers_href):
        self.level_number = level_number
        self.letters = letters
        self.answers_href = answers_href
