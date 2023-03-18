from ..base_classes import Ancestry, Heritage


class GutsyHalfling(Heritage):
    name = "Gutsy Halfling"


class HillockHalfling(Heritage):
    name = "Hillock Halfling"


class NomadicHalfling(Heritage):
    name = "Nomadic Halfling"


class TwilightHalfling(Heritage):
    name = "Twilight Halfling"


class WildwoodHalfling(Heritage):
    name = "Wildwood Halfling"


class Halfling(Ancestry):
    name = "Halfling"
    hit_points = 6
    size = "small"
    speed = 25
    ability_boosts = ["dexterity", "wisdom", "any"]
    ability_flaws = ["strength"]
    languages = ["common", "halfling"]
    language_options = ["dwarven", "elven", "gnomish", "goblin"]
    traits = ["halfling", "humanoid"]
    heritage_options = [
        GutsyHalfling(),
        HillockHalfling(),
        NomadicHalfling(),
        TwilightHalfling(),
        WildwoodHalfling()
    ]
