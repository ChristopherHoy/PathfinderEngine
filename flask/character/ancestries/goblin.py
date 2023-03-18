from ..base_classes import Ancestry, Heritage


class CharhideGoblin(Heritage):
    name = "Charhide Goblin"


class IrongutGoblin(Heritage):
    name = "Irongut Goblin"


class RazortoothGoblin(Heritage):
    name = "Razortooth Goblin"


class SnowGoblin(Heritage):
    name = "Snow Goblin"


class UnbreakableGoblin(Heritage):
    name = "Unbreakable Goblin"


class Goblin(Ancestry):
    hit_points = 6
    size = "small"
    speed = 25
    ability_boosts = ["dexterity", "charisma", "free"]
    ability_flaws = ["wisdom"]
    languages = ["common", "goblin"]
    language_options = ["draconic", "dwarven", "gnoll", "gnomish", "halfling", "orcish"]
    traits = ["goblin", "humanoid"]
    heritage_options = [
        CharhideGoblin(),
        IrongutGoblin(),
        RazortoothGoblin(),
        SnowGoblin(),
        UnbreakableGoblin()
    ]