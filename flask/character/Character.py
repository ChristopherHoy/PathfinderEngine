import json
import math


# TODO: Add abilitity to add/remove to/from scores ass override
# TODO: Add functionality to init from json

class Character:
    # Int Type
    hit_points = 0
    level = 0
    hero_points = 0
    experience_points = 0

    # String Type
    name = ""

    # Coices Type
    character_class = ""
    background = ""
    ancestry = ""
    alignment = ""  # Options based on ancestry
    size = ""  # Options based on ancestry
    deity = ""  # Options based on ancestry

    def __init__(self):
        return

    def __str__(self):
        dict_repr = {
            "hit_points": self.hit_points,
            "level": self.level,
            "hero_points": self.hero_points,
            "experience_points": self.experience_points,
            "name": self.name,
            "character_class": self.character_class,
            "background": self.background,
            "ancestry": self.ancestry,
            "alignment": self.alignment,
            "size": self.size,
            "deity": self.deity
        }

        json.dumps(dict_repr)


class Level:
    score = 1


class Proficiency:
    score = 0
    titles = [
        "untrained",
        "trained",
        "expert",
        "master",
        "legendary"
    ]

    def __init__(self, score: int) -> None:
        self.score = score

    def __str__(self) -> str:
        return json.dumps({
            "title": self.get_proficiency(),
            "score": self.score
        })

    def __int__(self) -> int:
        return self.score

    def __add__(self, other):
        return Proficiency(self.score + int(other))

    def __sub__(self, other):
        return Proficiency(self.score - int(other))

    def get_proficiency(self):
        return self.titles[self.score - self.score % 2]


class AbilityScore:
    score = 0

    def __init__(self, score: int) -> None:
        self.score = score

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        return {
            "modifier": self.get_modifier(),
            "score": self.score
        }

    def get_modifier(self):
        return math.floor((self.score - 10) / 2)

    def __int__(self) -> int:
        return self.score

    def __add__(self, other):
        return AbilityScore(self.score + int(other))

    def __sub__(self, other):
        return AbilityScore(self.score - int(other))


class Ability:
    constitution: AbilityScore = AbilityScore(0)
    charisma: AbilityScore = AbilityScore(0)
    wisdom: AbilityScore = AbilityScore(0)
    intelligence: AbilityScore = AbilityScore(0)
    dexterity: AbilityScore = AbilityScore(0)
    strength: AbilityScore = AbilityScore(0)

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        repr_dict = {}
        abilities = self.abilitites_list()
        for ability in abilities:
            repr_dict[ability] = self.get(ability, AbilityScore(0)).to_dict()
        return repr_dict

    def get(self, attr: str, default: any = None) -> any:
        return getattr(self, attr, default)

    def set(self, attr: str, value: any = None) -> None:
        setattr(self, attr, value)

    def get_modifier(self, ability: str) -> int:
        return self.get(ability, AbilityScore(0)).get_modifier()

    @staticmethod
    def abilitites_list():
        return [
            "constitution",
            "charisma",
            "wisdom",
            "intelligence",
            "dexterity",
            "strength"
        ]


class Ancestry:
    size = ""
    speed = 0
    hit_points = 0

    alignment_options = []
    deity_options = []
    heritage_options = []
    ability_boosts = []
    ability_flaws = []
    language_options = []
    languages = []
    traits = []
    abilities = None

    def __init__(self, abilities: Ability) -> None:
        self.abilities = abilities
        pass

    @staticmethod
    def get_from_json(json_string: str):
        pass

    def boost(self):
        for ability in self.ability_boosts:
            current_score = self.abilities.get(ability, AbilityScore(0))
            if current_score.score < 18:
                current_score += 2
            else:
                current_score += 1

    def flaw(self):
        for ability in self.ability_flaws:
            self.abilities.set(ability, self.abilities.get(ability, AbilityScore(0)) - 2)

    def additional_languages(self) -> int:
        return self.abilities.get_modifier('intelligence')


class Skill:
    # TODO: Make the score for each of these its own SkillScore Class
    # Class must have
    # proficiency
    # key ability
    # abilities reference
    # items reference
    # base score
    # armour reference

    acrobatics: Proficiency = Proficiency(0)
    arcana: Proficiency = Proficiency(0)
    athletics: Proficiency = Proficiency(0)
    crafting: Proficiency = Proficiency(0)
    deception: Proficiency = Proficiency(0)
    diplomacy: Proficiency = Proficiency(0)
    intimidation: Proficiency = Proficiency(0)
    lore: Proficiency = Proficiency(0)
    medicine: Proficiency = Proficiency(0)
    nature: Proficiency = Proficiency(0)
    occultism: Proficiency = Proficiency(0)
    performance: Proficiency = Proficiency(0)
    religion: Proficiency = Proficiency(0)
    society: Proficiency = Proficiency(0)
    stealth: Proficiency = Proficiency(0)
    survival: Proficiency = Proficiency(0)
    thievery: Proficiency = Proficiency(0)

    ability_score_map = {
        "acrobatics": "dexterity",
        "arcana": "intelligence",
        "athletics": "strength",
        "crafting": "intelligence",
        "deception": "charisma",
        "diplomacy": "charisma",
        "intimidation": "charisma",
        "lore": "intelligence",
        "medicine": "wisdom",
        "nature": "wisdom",
        "occultism": "intelligence",
        "performance": "charisma",
        "religion": "wisdom",
        "society": "intelligence",
        "stealth": "dexterity",
        "survival": "wisdom",
        "thievery": "dexterity"
    }

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return json.dumps({
            "acrobatics": self.acrobatics,
            "arcana": self.arcana,
            "athletics": self.athletics,
            "crafting": self.crafting,
            "deception": self.deception,
            "diplomacy": self.diplomacy,
            "intimidation": self.intimidation,
            "lore": self.lore,
            "medicine": self.medicine,
            "nature": self.nature,
            "Occultism": self.occultism,
            "performance": self.performance,
            "religion": self.religion,
            "society": self.society,
            "stealth": self.stealth,
            "survival": self.survival,
            "thievery": self.thievery
        })

    def get(self, attr: str, default: any = None) -> any:
        return getattr(self, attr, default)

    def set(self, attr: str, value: any = None) -> None:
        setattr(self, attr, value)

    def skills_list(self) -> list:
        return list(self.ability_score_map.keys())


class CharacterClass:
    key_ability: str = ""
    hit_point_per_level: int = 0
    hit_point_modifier: str = ""
    initial_proficiencies: list = []
    class_feats: list = []
    level: Level | None = None
    skills: Skill | None = None
    abilities: Ability | None = None
    ancestry: Ancestry | None = None

    def __init__(self, skills: Skill, abilities: Ability, level: Level, ancestry: Ancestry) -> None:
        self.skills = skills
        self.abilities = abilities
        self.level = level
        self.ancestry = ancestry

    def level_up(self) -> dict:
        return {
            "class_feats": self.level_class_feats(),
            "skill_feats": self.level_skill_feats(),
            "general_feats": self.level_general_feats(),
            "ancestry_feats": self.level_ancestry_feats(),
            "skills": self.level_ability_boost(),
            "abilities": self.level_ability_boost(),
            "hp_updated_to": self.level_hit_points()
        }

    def level_hit_points(self) -> int | None:
        to_add = self.hit_point_per_level + self.abilities.get_modifier(self.hit_point_modifier)
        self.ancestry.hit_points += to_add
        return self.ancestry.hit_points

    def level_class_feats(self) -> bool | None:
        pass

    def level_skill_feats(self) -> bool | None:
        pass

    def level_general_feats(self) -> bool | None:
        pass

    def level_ancestry_feats(self) -> bool | None:
        pass

    def level_skill_increase(self) -> list | None:
        return_arr = []
        next_level = self.level.score + 1

        for skill in self.skills.skills_list():
            skill_score: Proficiency = self.skills.get(skill, Proficiency(0))
            if (skill_score.score - 3) % 2 == 0 and skill_score.score != 0:
                if skill_score.score < 6 and next_level < 7:
                    return_arr.append({skill: self.skills.get(skill, Proficiency(0))})
                elif skill_score.score < 8 and next_level < 15:
                    return_arr.append({skill: self.skills.get(skill, Proficiency(0))})

        return return_arr

    def level_ability_boost(self) -> list | None:
        return_arr = []
        next_level = self.level.score + 1

        for ability in self.abilities.abilitites_list():
            ability_score = self.abilities.get(ability, AbilityScore(0))
            if next_level % 5 == 0:
                if ability_score.score < 18:
                    return_arr.append({ability: 2})
                else:
                    return_arr.append({ability: 1})

        return return_arr

    def boost_key_ability(self):
        current_score = self.abilities.get(self.key_ability, AbilityScore(0))

        if current_score.score < 18:
            current_score += 2
        else:
            current_score += 1


class SavingThrowScore:
    score: int = 0

    def __init__(self, score: int) -> None:
        self.score = score

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        return {
            "score": self.score
        }

    def __int__(self) -> int:
        return self.score

    def __add__(self, other):
        return SavingThrowScore(self.score + int(other))

    def __sub__(self, other):
        return SavingThrowScore(self.score - int(other))


class SavingThrow:
    # TODO: Make the score for each of these its own SavingThrowsScore Class
    # Class must have
    # proficiency
    # key ability
    # abilities reference
    # items reference
    # base score

    will: SavingThrowScore = SavingThrowScore(0)
    reflex: SavingThrowScore = SavingThrowScore(0)
    fortitude: SavingThrowScore = SavingThrowScore(0)
    abilities = None

    def __init__(self, abilities: Ability):
        self.abilities = abilities
        pass

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            "reflex": self.reflex.to_dict(),
            "will": self.will.to_dict(),
            "fortitude": self.fortitude.to_dict()
        }


class Perception:
    abilities = None

    def __init__(self, abilities: Ability):
        self.abilities = abilities

# TODO: Armour Class
# TODO: Damage Class
