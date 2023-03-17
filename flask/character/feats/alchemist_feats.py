class BaseFeat:
    classification = "placeholder"
    name = "placeholder"
    description = "placeholder"
    level = 1

    def __init__(self):
        return

    def requirements_satisfied(self, character) -> bool:
        return self.level <= character.level


class AlchemicalFamiliar(BaseFeat):
    def __init__(self):
        super().__init__()
        self.classification = "alchemist"
        self.name = "Alchemical Familiar"
        self.description = "You have used alchemy to create life, a simple creature formed from alchemical materials, " \
                           "reagents, and a bit of your own blood. This alchemical familiar appears to be a small " \
                           "creature of flesh and blood, though it might have some unusual or distinguishing aspects " \
                           "depending on your creative process. Like other familiars, your alchemical familiar " \
                           "assists you in your laboratory and on adventures. The familiar uses your Intelligence " \
                           "modifier to determine its Perception, Acrobatics, and Stealth modifiers "
        self.level = 1


class AlchemicalSavant(BaseFeat):
    def __init__(self):
        super().__init__()
        self.classification = "alchemist"
        self.name = "Alchemical Savant"
        self.description = "You can identify alchemical items quickly. When using the Crafting skill to Identify " \
                           "Alchemy on an alchemical item you hold, you can do so as a single action, which has the " \
                           "concentrate and manipulate traits, instead of spending 10 minutes. If you have the " \
                           "formula for the item you are attempting to identify, you gain a +2 circumstance bonus to " \
                           "your check, and if you roll a critical failure, you get a failure instead. "
        self.level = 1

    def requirements_satisfied(self, character) -> bool:
        return super().requirements_satisfied(character) and character.skills.proficiency == "Trained"


class FarLobber(BaseFeat):
    def __init__(self):
        super().__init__()
        self.classification = "alchemist"
        self.name = "Far Lobber"
        self.description = "You’ve learned how to throw a longer distance. When you throw an alchemical bomb, " \
                           "it has a range increment of 30 feet instead of the usual 20 feet. "
        self.level = 1


class QuickBomber(BaseFeat):
    def __init__(self):
        super().__init__()
        self.classification = "alchemist"
        self.name = "Quick Bomber"
        self.description = "You keep your bombs in easy-to-reach pouches from which you draw without thinking. You " \
                           "Interact to draw a bomb, then Strike with it. "
        self.level = 1

