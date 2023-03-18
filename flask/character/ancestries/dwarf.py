from ..base_classes import Ancestry, Heritage


class AncientBloodedDwarf(Heritage):
    name = "Ancient-Blooded Dwarf"


class DeathWardenDwarf(Heritage):
    name = "Death Warden Dwarf"


class ForgeDwarf(Heritage):
    name = "Forge Dwarf"


class RockDwarf(Heritage):
    name = "Rock Dwarf"


class StrongBloodedDwarf(Heritage):
    name = "Strong-Blooded Dwarf"


class Dwarf(Ancestry):
    name = "Dwarf"
    hit_points = 10
    size = "medium"
    speed = 20
    ability_boosts = ["constitution", "wisdom", "any"]
    ability_flaws = ["charisma"]
    languages = ["common", "dwarven"]
    language_options = ["gnomish", "goblin", "jotun", "orcish", "terran", "undercommon"]
    traits = ["dwarf", "humanoid"]
    heritage_options = [
        AncientBloodedDwarf(),
        DeathWardenDwarf(),
        ForgeDwarf(),
        RockDwarf(),
        StrongBloodedDwarf()
    ]
