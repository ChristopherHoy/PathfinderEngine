from ..base_classes import Ancestry, Heritage


class ArcticElf(Heritage):
    name = "Arctic Elf"


class CavernElf(Heritage):
    name = "Cavern Elf"


class SeerElf(Heritage):
    name = "Seer Elf"


class WhisperElf(Heritage):
    name = "Whisper Elf"


class WoodlandElf(Heritage):
    name = "Woodland Elf"


class Elf(Ancestry):
    name = "Elf"
    hit_points = 6
    size = "medium"
    speed = 30
    ability_boosts = ["dexterity", "intelligence", "any"]
    ability_flaws = ["constitution"]
    languages = ["common", "elven"]
    language_options = ["celestial", "draconic", "gnoll", "gnomish", "goblin", "orcish", "sylvan"]
    traits = ["elf", "humanoid"]
    heritage_options = [
        ArcticElf(),
        CavernElf(),
        SeerElf(),
        WoodlandElf(),
        WhisperElf()
    ]
