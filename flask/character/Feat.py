import Character
from feats.alchemist_feats import *


class AllFeats:
    def __init__(self):
        return

    @staticmethod
    def get_valid_feats(feat_classification: str, character: Character = None) -> list:
        all_feats = BaseFeat.__subclasses__()
        print(all_feats)
        valid_feats = []
        for feat in all_feats:
            conditions = [
                feat.classification == feat_classification,
                character.level <= character.level,
                feat.requirements_satisfied(character)
            ]
            if all(conditions):
                valid_feats.append(feat)
        return valid_feats


print(AllFeats().get_valid_feats("alchemist"))
