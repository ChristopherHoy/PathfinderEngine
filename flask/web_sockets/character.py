from utils.globals import globals
from utils.message import Message
from flask_socketio import join_room, leave_room, emit
from utils.auth_token import validated
from flask import request
from utils.roll import D6
from utils.response import error, success
from utils.db import connect as db

def roll_abilities():
    dice = D6()
    return sorted([sum(sorted(dice.roll(4))[1::]) for x in range(6)])


def get_character_stats(character_id):
    base_query = "\
        SELECT a.name, b.name as race, c.name as class, d.name as eye_color, a.age FROM pathfinder.pathfinder_character a \
        inner join pathfinder.race b on a.race_id=b.id \
        inner join pathfinder.class c on a.class_id=c.id \
        inner join pathfinder.eye_color d on a.eye_color=d.id \
        where character_id=%(character_id)s"

    character_traits = "\
        select c.id, sum(a.score) as score, c.name from pathfinder.modifier a \
        inner join pathfinder.character_trait_modifier b on a.id=b.modifier_id \
        inner join pathfinder.character_trait c on b.trait_id=c.id \
        where a.character_id=%(character_id)s group by c.id"

    skills = "\
        select c.id, sum(a.score) as score, c.name, d.name as attribute from pathfinder.modifier a \
        inner join pathfinder.skill_modifier b on a.id=b.modifier_id \
        inner join pathfinder.skill c on b.skill_id=c.id \
        inner join (\
            select e.id, sum(g.score), e.name from pathfinder.modifier g \
            inner join pathfinder.attribute_modifier f on g.id=f.modifier_id \
            inner join pathfinder.attribute e on f.attribute_id=e.id \
            where g.character_id=%(character_id)s group by e.id\
        ) d on c.attribute_id=d.id \
        where a.character_id=%(character_id)s group by c.id"

    saves = "\
        select c.id, sum(a.score) as score, c.name from pathfinder.modifier a \
        inner join pathfinder.save_modifier b on a.id=b.modifier_id \
        inner join pathfinder.save c on b.save_id=c.id \
        where a.character_id=%(character_id)s group by c.id"

    attributes = "\
        select c.id, sum(a.score) as score, c.name from pathfinder.modifier a \
        inner join pathfinder.attribute_modifier b on a.id=b.modifier_id \
        inner join pathfinder.attribute c on b.attribute_id=c.id \
        where a.character_id=%(character_id)s group by c.id"

    
    # TODO: Traits and Feats 

@globals.socketio.on('get_stats')
@validated
def on_get_stats(data):
    return
 

# Roll attributes when starting a new character
@globals.socketio.on('roll_ability_scores')
@validated
def on_roll_ability_scores(data):
    ability_scores = roll_abilities()
    return success(ability_scores)


# Set attributes when starting a new character
@globals.socketio.on('set_ability_scores')
@validated
def on_set_ability_scores(data):
    str = data.get("str", None)
    dex = data.get("dex", None)
    con = data.get("con", None)
    intel = data.get("int", None)
    wis = data.get("wis", None)
    cha = data.get("cha", None)
    character_id = data.get("character_id", None)

    sql = "insert into pathfinder.modifier (score, character_id) values (%(score)s, %(character_id)s)"

    conn = db()
    curr = conn.cursor(dictionary=True)

    for key, score in [("Strength", str), ("Dexterity", dex), ("Constitution", con), ("Intelligence", intel), ("Wisdom", wis), ("Charisma", cha)]:

        curr.execute(sql, {"score": score, "character_id": character_id})
        last_id = curr.lastrowid

        linking ="insert into pathfinder.attribute_modifier (attribute_id, modifier_id) select id, %(id)s from pathfinder.attribute where name=%(key)s"
        curr.execute(linking, {"id": int(last_id), "key": key})

    conn.commit()
    curr.close()
    conn.close()

    return success("Success")