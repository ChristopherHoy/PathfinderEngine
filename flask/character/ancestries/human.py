from ..base_classes import Ancestry, Heritage


class HalfOrcHuman(Heritage):
    name = "Half-orc"


class HalfElfHuman(Heritage):
    name = "Half-elf"


class HumanHuman(Heritage):
    name = "Human"


class Human(Ancestry):
    name = "Human"
    hit_points = 8
    size = "medium"
    speed = 25
    ability_boosts = ["any", "any"]
    ability_flaws = []
    languages = ["common"]
    language_options = [""]
    traits = ["human", "humanoid"]
    heritage_options = [
        HalfOrcHuman(),
        HalfElfHuman(),
        HumanHuman()
    ]
