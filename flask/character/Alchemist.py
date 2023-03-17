from Base import BaseClass
from Feat import AllFeats
from flask.character.Character import Character


class Alchemist(BaseClass):
    name = "Alchemist"
    description = "There’s no sight more beautiful to you than a strange brew bubbling in a beaker, " \
                  "and you consume your ingenious elixirs with abandon. You’re fascinated by " \
                  "uncovering the secrets of science and the natural world, and you’re constantly " \
                  "experimenting in your lab or on the go with inventive concoctions for every " \
                  "eventuality. You are fearless in the face of risk, hurling explosive or toxic " \
                  "creations at your foes. Your unique path toward greatness is lined with alchemical " \
                  "brews that push your mind and body to their limits."
    levels = [
        ["Initial Proficiencies", "Ancestry", "Background", "Alchemy", "Formula Book", "Research Field",
         "Alchemist Feat", "2 Common Formulae"],
        ["Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["General Feat", "Skill Increase", "2 Common Formulae"],
        ["Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["Ability Boosts", "Ancestry Feat", "Field Discovery", "Powerful Alchemy", "Skill Increase",
         "2 Common Formulae"],
        ["Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["Alchemical Weapon Expertise", "General Feat", "Iron Will", "Perpetual Infusions", "Skill Increase",
         "2 Common Formulae"],
        ["Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["Alchemical Expertise", "Alertness", "Ancestry Feat", "Double Brew", "Skill Increase", "2 Common Formulae"],
        ["Ability Boosts", "Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["General Feat", "Juggernaut", "Perpetual Potency", "Skill Increase", "2 Common Formulae"],
        ["Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["Ancestry Feat", "Greater Field Discovery", "Light Armor Expertise", "Skill Increase", "Weapon Specialization",
         "2 Common Formulae"],
        ["Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["Ability Boosts", "Alchemical Alacrity", "Evasion", "General Feat", "Skill Increase", "2 Common Formulae"],
        ["Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["Ability Boosts", "Alchemical Alacrity", "Evasion", "General Feat", "Skill Increase", "2 Common Formulae"],
        ["Alchemist Feat", "Skill Feat", "2 Common Formulae"],
        ["General Feat", "Light Armor Mastery", "Skill Increase", "2 Common Formulae"],
        ["Baility Boosts", "Alchemist Feat", "Skill Feat", "2 Common Formulae"]
    ]

    def __init__(self):
        super().__init__()
        return

    def level_up(self, character: Character = None):
        level_steps = self.levels[character.level - 1]
        return [
            {
                "Title": "Choose 1 General Feat",
                "Choices": AllFeats().get_valid_feats("general", character),

            }
        ]
