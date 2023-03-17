INSERT INTO pathfinder.class (name, description, hp_ability, key_ability, details, hp_points_per_level) values (
    'Alchemist',
    'There’s no sight more beautiful to you than a strange brew bubbling in a beaker, and you consume your ingenious elixirs with abandon. You’re fascinated by uncovering the secrets of science and the natural world, and you’re constantly experimenting in your lab or on the go with inventive concoctions for every eventuality. You are fearless in the face of risk, hurling explosive or toxic creations at your foes. Your unique path toward greatness is lined with alchemical brews that push your mind and body to their limits.',
    3,
    4,
    '{}',
    8
);

INSERT INTO pathfinder.feat (name, description, duration, active, classification_id, level, prerequesite) values (
    'Alchemical Familiar',
    'You have used alchemy to create life, a simple creature formed from alchemical materials, reagents, and a bit of your own blood.',
    -1, 1, 1, 1, -1
);

INSERT INTO pathfinder.feat (name, description, duration, active, classification_id, level, prerequesite, number_choices) values (
    'Crafting - Trained',
    'You are trained in crafting',
    -1, 1, 5, 1, -1, 1
);

INSERT INTO pathfinder.trait(name) values ('Crafting');
INSERT INTO pathfinder.trait(name) values ('Trained');


INSERT INTO pathfinder.feat (name, description, duration, active, classification_id, level, prerequesite) values (
    'Alchemical Savant',
    'You can identify alchemical items quickly.',
    -1, 1, 1, 1, 2
);