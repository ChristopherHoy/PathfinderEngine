from ..base_classes import Ancestry, Heritage


class ChameleonGnome(Heritage):
    name = "Chameleon Gnome"


class FeyTouchedGnome(Heritage):
    name = "Fey-Touched Gnome"


class SensateGnome(Heritage):
    name = "Sensate Gnome"


class UmbralGnome(Heritage):
    name = "Umbral Gnome"


class WellspringGnome(Heritage):
    name = "Wellspring Gnome"


class Gnome(Ancestry):
    name = "Gnome"
    hit_points = 8
    size = "small"
    speed = 25
    ability_boosts = ["constitution", "charisma", "any"]
    ability_flaws = ["strength"]
    languages = ["common", "gnomish", "sylvan"]
    language_options = ["draconic", "dwarven", "elven", "goblin", "jotun", "orcish"]
    traits = ["gnome", "humanoid"]
    heritage_options = [
        ChameleonGnome(),
        FeyTouchedGnome(),
        SensateGnome(),
        UmbralGnome(),
        WellspringGnome()
    ]
