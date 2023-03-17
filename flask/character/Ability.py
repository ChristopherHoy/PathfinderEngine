class Ability:
    score = 0
    def __init__(self, score):
        self.score = score
        return


class Stregnth(Ability):
    name = "Stregnth"
    description = "Strength measures your character’s physical power. Strength is important if your character plans to engage in hand-to-hand combat. Your Strength modifier gets added to melee damage rolls and determines how much your character can carry."

    def __init__(self, score):
        super().__init__(score)
        return


class Dexterity(Ability):
    name = "Dexterity"
    description = "Dexterity measures your character’s agility, balance, and reflexes. Dexterity is important if your character plans to make attacks with ranged weapons or use stealth to surprise foes. Your Dexterity modifier is also added to your character’s AC and Reflex saving throws."

    def __init__(self, score):
        super().__init__(score)
        return


class Constitution(Ability):
    name = "Constitution"
    description = "Constitution measures your character’s overall health and stamina. Constitution is an important statistic for all characters, especially those who fight in close combat. Your Constitution modifier is added to your Hit Points and Fortitude saving throws."

    def __init__(self, score):
        super().__init__(score)
        return


class Intelligent(Ability):
    name = "Intelligence"
    description = "Intelligence measures how well your character can learn and reason. A high Intelligence allows your character to analyze situations and understand patterns, and it means they can become trained in additional skills and might be able to master additional languages."

    def __init__(self, score):
        super().__init__(score)
        return


class Wisdom(Ability):
    name = "Wisdom"
    description = "Wisdom measures your character’s common sense, awareness, and intuition. Your Wisdom modifier is added to your Perception and Will saving throws."

    def __init__(self, score):
        super().__init__(score)
        return


class Charisma(Ability):
    name = "Charisma"
    description = "Charisma measures your character’s personal magnetism and strength of personality. A high Charisma score helps you influence the thoughts and moods of others."

    def __init__(self, score):
        super().__init__(score)
        return