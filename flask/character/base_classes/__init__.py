import json
import math


# TODO: Once all this is set up, will need to think of user flow
#   What deity and alignments can be chosen, how to choose and set them
#   Choosing heritage options
#   Choosing Languages
#   What boosts to choose and what are available to choose based on previous choices
#   How do we fit these into the __init__ flow for the character (state-machine diagram?)

# TODO: Add abilitity to add/remove to/from scores as override (misc modifiers)
# TODO: Add functionality to init from json


class Character:
    # Int Type
    level = 0
    hero_points = 0
    experience_points = 0

    # String Type
    name = ""

    # Coices Type
    character_class = None
    skills = None
    abilities = None
    ancestry = None
    items = None
    armour_class = None
    difficulty_class = None
    attack = None
    background = None

    alignment = ""  # Options based on ancestry
    size = ""  # Options based on ancestry
    deity = ""  # Options based on ancestry

    def __init__(self, ancestry, character_class, background):
        self.ancestry: Ancestry = ancestry(self)
        self.background: Background = background(self)
        self.character_class: CharacterClass = character_class(self)

        # Should always be the same
        self.saving_throws = SavingThrows(self)
        self.perception = Perception(self)

        return

    @property
    def hit_points(self):
        return self.ancestry.hit_points


class Proficiency:
    score = 0
    character: Character = None
    titles = [
        "untrained",
        "trained",
        "expert",
        "master",
        "legendary"
    ]

    def __init__(self, score: int, character: Character) -> None:
        self.score = score
        self.character = character

    def __str__(self) -> str:
        return json.dumps({
            "title": self.get_proficiency(),
            "score": self.score
        })

    def __int__(self) -> int:
        return self.score + self.character.level

    def __add__(self, other):
        return Proficiency(self.score + int(other), self.character)

    def __sub__(self, other):
        return Proficiency(self.score - int(other), self.character)

    def get_proficiency(self) -> str:
        return self.titles[self.score - self.score % 2]

    def calculate(self):
        if self.score == 0:
            return self.score
        return self.score + self.character.level


class AbilityScore:
    base_score: int = 0
    name: str = ""

    # Use character for abilities, items, armour, defence reference
    character: Character = None

    def __init__(self, name: str, character: Character, base_score: int = 0) -> None:
        self.name = name
        self.character: Character = character
        self.character.abilities = self
        self.base_score: int = base_score

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        response_dict = {
            "total_score": self.calculate(),
            "item_bonus": self.character.items.get_modifier(self.name),
            "base_score": self.base_score,
            "modifier": self.get_modifier()
        }

        return response_dict

    def __int__(self) -> int:
        return self.calculate()

    def __add__(self, other):
        new_base_score = self.base_score + int(other)
        return AbilityScore(
            name=self.name,
            character=self.character,  # will have the same character ref
            base_score=new_base_score
        )

    def __sub__(self, other):
        new_base_score = self.base_score - int(other)
        return AbilityScore(
            name=self.name,
            character=self.character,  # will have the same character ref
            base_score=new_base_score
        )

    def __cmp__(self, other) -> int:
        if self.calculate() > int(other):
            return 1
        if self.calculate() < int(other):
            return -1
        return 0

    def boost(self) -> None:
        if self.calculate() < 18:
            self.base_score += 2
        else:
            self.base_score += 1

    def flaw(self) -> None:
        self.base_score -= 2

    def calculate(self) -> int:
        item_bonus = self.character.items.get_modifier(self.name)
        return self.base_score + item_bonus

    def get_modifier(self) -> int:
        return math.floor((self.calculate() - 10) / 2)


class Abilities:
    list_of_abilities: list = [
        "constitution",
        "charisma",
        "wisdom",
        "intelligence",
        "dexterity",
        "strength"
    ]
    abilities_list: list[AbilityScore] = []

    def __init__(self, character: Character) -> None:
        for ability in self.list_of_abilities:
            self.abilities_list.append(
                AbilityScore(
                    name=ability,
                    character=character
                )
            )

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        repr_dict = {}
        abilities = self.abilities_list
        for ability in abilities:
            repr_dict[ability.name] = ability.to_dict()
        return repr_dict

    def get(self, name: str, default: any = None) -> any:
        for ability in self.abilities_list:
            if ability.name == name:
                return ability
        return default

    def set(self, name: str, value: AbilityScore = None) -> bool:
        repl_index = None
        repl_ability = None
        for index, ability in enumerate(self.abilities_list):
            if ability.name == name:
                repl_index = index
                repl_ability = value

        if repl_index:
            self.abilities_list[repl_index] = repl_ability
            return True
        return False

    def set_base_score(self, name: str, value: any = None) -> bool:
        for ability in self.abilities_list:
            if ability.name == name:
                ability.base_score = value
                return True
        return False

    def get_modifier(self, ability: str) -> int:
        return self.get(ability).get_modifier()


class Ancestry:
    name: str = ""
    size: str = ""
    speed: int = 0
    hit_points: int = 0

    alignment_options: list = []
    deity_options: list = []
    heritage_options: list = []
    ability_boosts: list = []
    ability_flaws: list = []
    language_options: list = []
    languages: list = []
    traits: list = []

    def __init__(self, character: Character) -> None:
        self.character = character
        self.character.ancestry = self

    def boost(self) -> None:
        for ability in self.ability_boosts:
            self.character.abilities.get(ability).boost()

    def flaw(self) -> None:
        for ability in self.ability_flaws:
            self.character.abilities.get(ability).flaw()

    # May need to be overriden for humans
    def additional_languages(self) -> int:
        return self.character.abilities.get_modifier('intelligence')


class SkillScore:
    base_score: int = 0
    name: str = ""
    key_ability: str = ""

    # Use character for abilities, items, armour, defence reference
    character: Character = None
    proficiency: Proficiency = None

    def __init__(
            self,
            name: str,
            character: Character,
            key_ability: str,
            proficiency: Proficiency,
            base_score: int = 0
    ) -> None:
        self.name = name
        self.character = character
        self.proficiency = proficiency
        self.key_ability = key_ability
        self.base_score = base_score

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        response_dict = {
            "total_score": self.calculate(),
            "ability_bonus": self.character.abilities.get_modifier(self.key_ability),
            "item_bonus": self.character.items.get_modifier(self.name),
            "proficiency_bonus": self.proficiency.calculate(),
            "armour_penalty": 0
        }

        if self.key_ability in ["strength", "dexterity"]:
            response_dict["armour_penalty"] = self.character.armour_class.check_penalty

        return response_dict

    def __int__(self) -> int:
        return self.calculate()

    def __add__(self, other):
        new_base_score = self.base_score + int(other)
        return SkillScore(
            name=self.name,
            character=self.character,  # will have the same character ref
            key_ability=self.key_ability,
            proficiency=self.proficiency,  # will have the same character ref
            base_score=new_base_score
        )

    def __sub__(self, other):
        new_base_score = self.base_score - int(other)
        return SkillScore(
            name=self.name,
            character=self.character,  # will have the same character ref
            key_ability=self.key_ability,
            proficiency=self.proficiency,  # will have the same character ref
            base_score=new_base_score
        )

    def __cmp__(self, other) -> int:
        if self.calculate() > int(other):
            return 1
        if self.calculate() < int(other):
            return -1
        return 0

    # Modifier is a sum of Proficiency modifier, ability modifier, item effects and
    def calculate(self) -> int:
        ability_bonus = self.character.abilities.get_modifier(self.key_ability)
        item_bonus = self.character.items.get_modifier(self.name)
        proficiency_bonus = self.proficiency.calculate()

        armour_penalty = 0
        if self.key_ability in ["strength", "dexterity"]:
            armour_penalty = self.character.armour_class.check_penalty

        return self.base_score + ability_bonus + item_bonus + proficiency_bonus + armour_penalty


class Skills:
    skills_list: list[SkillScore] = []
    character: Character = None
    ability_score_map: dict = {
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

    def __init__(self, character: Character, proficiencies: dict) -> None:
        self.character = character
        self.character.skills = self
        for skill, ability in self.ability_score_map.items():
            self.skills_list.append(
                SkillScore(
                    name=skill,
                    character=character,
                    key_ability=ability,
                    proficiency=proficiencies.get(skill, Proficiency(0, self.character)),
                )
            )

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        skills_dict = {}
        for skill in self.skills_list:
            skills_dict[skill.name] = skill.to_dict()
        return skills_dict

    def get(self, name: str, default: any = None) -> any:
        for skill in self.skills_list:
            if skill.name == name:
                return skill
        return default

    def set(self, name: str, value: SkillScore = None) -> bool:
        repl_index = None
        repl_skill = None
        for index, skill in enumerate(self.skills_list):
            if skill.name == name:
                repl_index = index
                repl_skill = value

        if repl_index:
            self.skills_list[repl_index] = repl_skill
            return True
        return False

    def set_base_score(self, name: str, value: any = None) -> bool:
        for skill in self.skills_list:
            if skill.name == name:
                skill.base_score = value
                return True
        return False

    @property
    def list_of_skills(self) -> list:
        return list(self.ability_score_map.keys())


class CharacterClass:
    key_ability: str = ""
    hit_point_per_level: int = 0
    hit_point_modifier: str = ""
    initial_proficiencies: dict = {}
    class_feats: list = []

    character: Character = None
    dc_proficiency: Proficiency = None
    perception_proficiency: Proficiency = None
    saving_throw_proficiencies: dict[str:Proficiency] = {}
    attack_proficiencies: dict[str: Proficiency] = {}
    armour_proficiencies: dict[str: Proficiency] = {}

    ancestry: Ancestry = None

    def __init__(self, character: Character) -> None:
        self.character = character
        self.character.character_class = self
        self.character.skills = Skills(character, self.initial_proficiencies)
        self.dc_proficiency = Proficiency(2, self.character)

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
        to_add = self.hit_point_per_level + self.character.abilities.get_modifier(self.hit_point_modifier)
        self.ancestry.hit_points += to_add
        return self.ancestry.hit_points

    # Will need to override
    def level_class_feats(self) -> bool | None:
        pass

    # Will need to override
    def level_skill_feats(self) -> bool | None:
        pass

    # Will need to override
    def level_general_feats(self) -> bool | None:
        pass

    # Will need to override
    def level_ancestry_feats(self) -> bool | None:
        pass

    # May need to override
    def level_skill_increase(self) -> list | None:
        return_arr = []
        next_level = self.character.level + 1

        for skill in self.character.skills.skills_list:
            if (skill.calculate() - 3) % 2 == 0 and skill.calculate() != 0:
                if skill.calculate() < 6 and next_level < 7:
                    return_arr.append(skill.to_dict())
                elif skill.calculate() < 8 and next_level < 15:
                    return_arr.append(skill.to_dict())

        return return_arr

    # May need to override
    def level_ability_boost(self) -> list | None:
        return_arr = []
        next_level = self.character.level + 1

        for ability in self.character.abilities.abilitites_list():
            ability_score = self.character.abilities.get(ability)
            if next_level % 5 == 0:
                if ability_score.score < 18:
                    return_arr.append({ability: 2})
                else:
                    return_arr.append({ability: 1})

        return return_arr

    def boost_key_ability(self) -> None:
        self.character.abilities.get(self.key_ability).boost()


class SavingThrowScore:
    base_score: int = 0
    name: str = ""
    key_ability: str = ""

    # Use character for abilities, items, armour, defence reference
    character: Character = None
    proficiency: Proficiency = None

    def __init__(
            self,
            name: str,
            character: Character,
            key_ability: str,
            proficiency: Proficiency,
            base_score: int = 0
    ) -> None:
        self.name = name
        self.character = character
        self.proficiency = proficiency
        self.key_ability = key_ability
        self.base_score = base_score

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        response_dict = {
            "total_score": self.calculate(),
            "ability_bonus": self.character.abilities.get_modifier(self.key_ability),
            "item_bonus": self.character.items.get_modifier(self.name),
            "proficiency_bonus": self.proficiency.calculate(),
        }

        return response_dict

    def __int__(self) -> int:
        return self.calculate()

    def __add__(self, other):
        new_base_score = self.base_score + int(other)
        return SavingThrowScore(
            name=self.name,
            character=self.character,  # will have the same character ref
            key_ability=self.key_ability,
            proficiency=self.proficiency,  # will have the same character ref
            base_score=new_base_score
        )

    def __sub__(self, other):
        new_base_score = self.base_score - int(other)
        return SavingThrowScore(
            name=self.name,
            character=self.character,  # will have the same character ref
            key_ability=self.key_ability,
            proficiency=self.proficiency,  # will have the same character ref
            base_score=new_base_score
        )

    def __cmp__(self, other) -> int:
        if self.calculate() > int(other):
            return 1
        if self.calculate() < int(other):
            return -1
        return 0

    def calculate(self) -> int:
        ability_bonus = self.character.abilities.get_modifier(self.key_ability)
        item_bonus = self.character.items.get_modifier(self.name)
        proficiency_bonus = self.proficiency.calculate()

        return self.base_score + ability_bonus + item_bonus + proficiency_bonus


class SavingThrows:
    saving_throw_list: list = []
    ability_score_map: dict = {
        "will": "wisdom",
        "fortitude": "constitution",
        "reflex": "dexterity"
    }

    def __init__(self, character: Character) -> None:
        self.character = character
        self.character.skills = self
        for st, ability in self.ability_score_map.items():
            proficiency = self.character.character_class.saving_throw_proficiencies.get(
                st, Proficiency(0, self.character)
            )
            self.saving_throw_list.append(
                SavingThrowScore(
                    name=st,
                    character=character,
                    key_ability=ability,
                    proficiency=proficiency,
                )
            )

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        st_dict = {}
        for st in self.saving_throw_list:
            st_dict[st.name] = st.to_dict()
        return st_dict

    def get(self, name: str, default: any = None) -> any:
        for st in self.saving_throw_list:
            if st.name == name:
                return st
        return default

    def set(self, name: str, value: SkillScore = None) -> bool:
        repl_index = None
        repl_st = None
        for index, st in enumerate(self.saving_throw_list):
            if st.name == name:
                repl_index = index
                repl_st = value

        if repl_index:
            self.saving_throw_list[repl_index] = repl_st
            return True
        return False

    def set_base_score(self, name: str, value: any = None) -> bool:
        for st in self.saving_throw_list:
            if st.name == name:
                st.base_score = value
                return True
        return False

    @property
    def list_of_saving_throws(self) -> list:
        return list(self.ability_score_map.keys())


class Perception:
    character: Character = None
    base_score: int = 0

    def __init__(self, character: Character, base_score: int = 0) -> None:
        self.character: Character = character
        self.character.perception = self
        self.base_score: int = base_score

    def calculate(self) -> int:
        wisdom: int = self.character.abilities.get_modifier('wisdom')
        item_bonus: int = self.character.items.get_modifier('perception')
        proficiency_bonus: int = self.character.character_class.perception_proficiency.calculate()

        return self.base_score + wisdom + item_bonus + proficiency_bonus


class Background:

    # 1 boost chosen from list, another is a free boost
    name: str = ""
    boost_choies: list = []
    training: list = []
    character: Character = None

    def __init__(self, character: Character) -> None:
        self.character = character
        self.character.background = self


class ArmourClass:
    character: Character = None
    base_score: int = 10

    def __init__(self, character: Character, base_score: int = 10) -> None:
        self.character: Character = character
        self.character.armour_class = self
        self.base_score: int = base_score

    def calculate(self) -> int:
        armour = self.character.items.current('armour')
        shield = self.character.items.current('shield')

        sheld_bonus = shield.ac_bonus if shield is not None else 0
        item_bonus = self.character.items.get_modifier('armour_class')
        proficiency_bonus = self.character.character_class.armour_proficiencies[armour.armour_type].calculate()

        dexterity = self.character.abilities.get_modifier('dexterity')
        if dexterity > armour.dex_cap:
            dexterity = armour.dex_cap

        return self.base_score + dexterity + item_bonus + proficiency_bonus + sheld_bonus


class DifficultyClass:
    character: Character = None
    base_score: int = 10

    def __init__(self, character: Character, base_score: int = 10) -> None:
        self.character: Character = character
        self.character.difficulty_class = self
        self.base_score: int = base_score

    def calculate(self) -> int:
        key_ability = self.character.character_class.key_ability

        item_bonus = self.character.items.get_modifier('difficulty_class')
        key_ability_bonus = self.character.abilities.get_modifier(key_ability)
        proficiency_bonus = self.character.character_class.dc_proficiency.calculate()

        return self.base_score + key_ability_bonus + item_bonus + proficiency_bonus


class Heritage:
    name: str = ""

    def __str__(self):
        return json.dumps(self.to_json())

    def to_json(self):
        return {
            "name": self.name
        }
