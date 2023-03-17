CREATE TABLE `pathfinder`.`trait` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`ability` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`feat_classification` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`feat` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    `duration` int DEFAULT -1,
    `active` tinyint(1),
    `classification_id` int NOT NULL,
    KEY `feat_classification_id` (`classification_id`),
    CONSTRAINT `feat_classification_id` FOREIGN KEY (`classification_id`) REFERENCES `pathfinder`.`feat_classification` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`feat_trait` (
    `id` int NOT NULL AUTO_INCREMENT,
    `trait` int DEFAULT -1,
    `feat` int DEFAULT -1,
    KEY `ft_trait_id` (`trait`),
    KEY `ft_feat_id` (`feat`),
    CONSTRAINT `ft_trait_id` FOREIGN KEY (`trait`) REFERENCES `pathfinder`.`trait` (`id`),
    CONSTRAINT `ft_feat_id` FOREIGN KEY (`feat`) REFERENCES `pathfinder`.`feat` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`proficiency` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    `score` int DEFAULT 0,
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`skill` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    `key_ability` int DEFAULT -1,
    `proficiency` int DEFAULT -1,
    KEY `skill_key_ability` (`key_ability`),
    KEY `skill_proficiency` (`proficiency`),
    CONSTRAINT `skill_key_ability` FOREIGN KEY (`key_ability`) REFERENCES `pathfinder`.`ability` (`id`),
    CONSTRAINT `skill_proficiency` FOREIGN KEY (`proficiency`) REFERENCES `pathfinder`.`proficiency` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`skill_modifier` (
    `id` int NOT NULL AUTO_INCREMENT,
    `score` int DEFAULT 0,
    `skill` int DEFAULT -1,
    `feat` int DEFAULT -1,
    KEY `skill_modifier_feat` (`skill`),
    KEY `skill_modifier_skill` (`feat`),
    CONSTRAINT `skill_modifier_feat` FOREIGN KEY (`feat`) REFERENCES `pathfinder`.`feat` (`id`),
    CONSTRAINT `skill_modifier_skill` FOREIGN KEY (`skill`) REFERENCES `pathfinder`.`skill` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`ability_modifier` (
    `id` int NOT NULL AUTO_INCREMENT,
    `score` int DEFAULT 0,
    `ability` int DEFAULT -1,
    `feat` int DEFAULT -1,
    KEY `ability_modifier_feat` (`skill`),
    KEY `ability_modifier_ability` (`ability`),
    CONSTRAINT `ability_modifier_feat` FOREIGN KEY (`feat`) REFERENCES `pathfinder`.`feat` (`id`),
    CONSTRAINT `ability_modifier_ability` FOREIGN KEY (`ability`) REFERENCES `pathfinder`.`ability` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`save` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    `key_ability` int DEFAULT -1,
    `proficiency` int DEFAULT -1,
    KEY `save_key_ability` (`key_ability`),
    KEY `save_proficiency` (`proficiency`),
    CONSTRAINT `save_key_ability` FOREIGN KEY (`key_ability`) REFERENCES `pathfinder`.`ability` (`id`),
    CONSTRAINT `save_proficiency` FOREIGN KEY (`proficiency`) REFERENCES `pathfinder`.`proficiency` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`save_modifier` (
    `id` int NOT NULL AUTO_INCREMENT,
    `score` int DEFAULT 0,
    `save` int DEFAULT -1,
    `feat` int DEFAULT -1,
    KEY `save_modifier_feat` (`save`),
    KEY `save_modifier_save` (`feat`),
    CONSTRAINT `save_modifier_feat` FOREIGN KEY (`feat`) REFERENCES `pathfinder`.`feat` (`id`),
    CONSTRAINT `save_modifier_save` FOREIGN KEY (`save`) REFERENCES `pathfinder`.`save` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`class` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    `hp_ability` int DEFAULT -1,
    `key_ability` int DEFAULT -1,
    `details` json,
    PRIMARY KEY (`id`),
    KEY `class_hp_ability_id` (`hp_ability`),
    KEY `class_key_ability_id` (`key_ability`),
    CONSTRAINT `class_hp_ability_id` FOREIGN KEY (`hp_ability`) REFERENCES `ability` (`id`),
    CONSTRAINT `class_key_ability_id` FOREIGN KEY (`key_ability`) REFERENCES `ability` (`id`)
);

CREATE TABLE `pathfinder`.`class_leveling` (
    `id` int NOT NULL AUTO_INCREMENT,
    `feat_type` varchar(255) DEFAULT NULL,
    `feat` int DEFAULT -1,
    `class` int DEFAULT -1,
    PRIMARY KEY (`id`),
    KEY `cl_feat_id` (`feat`),
    KEY `cl_class_id` (`class`),
    CONSTRAINT `cl_feat_id` FOREIGN KEY (`feat`) REFERENCES `feat` (`id`),
    CONSTRAINT `cl_class_id` FOREIGN KEY (`class`) REFERENCES `class` (`id`)
);

CREATE TABLE `pathfinder`.`action` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    `uses_per_day` int DEFAULT -1,
    `feat` int DEFAULT -1,
    PRIMARY KEY (`id`),
    KEY `action_feat_id` (`feat`),
    CONSTRAINT `action_feat_id` FOREIGN KEY (`feat`) REFERENCES `feat` (`id`)
);

CREATE TABLE `pathfinder`.`action_trait` (
    `id` int NOT NULL AUTO_INCREMENT,
    `action` int DEFAULT -1,
    `trait` int DEFAULT -1,
    KEY `at_action_id` (`action`),
    KEY `at_trait_id` (`trait`),
    CONSTRAINT `at_action_id` FOREIGN KEY (`action`) REFERENCES `pathfinder`.`action` (`id`),
    CONSTRAINT `at_trait_id` FOREIGN KEY (`trait`) REFERENCES `pathfinder`.`trait` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`item` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` TEXT,
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`item_trait` (
    `id` int NOT NULL AUTO_INCREMENT,
    `item` int DEFAULT -1,
    `trait` int DEFAULT -1,
    KEY `it_item_id` (`item`),
    KEY `it_trait_id` (`trait`),
    CONSTRAINT `it_trait_id` FOREIGN KEY (`trait`) REFERENCES `pathfinder`.`trait` (`id`),
    CONSTRAINT `it_item_id` FOREIGN KEY (`item`) REFERENCES `pathfinder`.`item` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`eye_color` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`race` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `date_added` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`pathfinder_character` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `race_id` int NOT NULL,
  `class_id` int NOT NULL,
  `eye_color` int NOT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pc_user_id` (`user_id`),
  KEY `fk_pc_race_id` (`race_id`),
  KEY `fk_pc_class_id` (`class_id`),
  CONSTRAINT `fk_pc_class_id` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`),
  CONSTRAINT `fk_pc_race_id` FOREIGN KEY (`race_id`) REFERENCES `race` (`id`),
  CONSTRAINT `fk_pc_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
);

CREATE TABLE `pathfinder`.`character_feat` (
    `id` int NOT NULL AUTO_INCREMENT,
    `feat` int DEFAULT -1,
    `character` int DEFAULT -1,
    KEY `cf_feat_id` (`feat`),
    KEY `cf_character_id` (`character`),
    CONSTRAINT `cf_feat_id` FOREIGN KEY (`feat`) REFERENCES `pathfinder`.`feat` (`id`),
    CONSTRAINT `cf_character_id` FOREIGN KEY (`character`) REFERENCES `pathfinder`.`pathfinder_character` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`character_item` (
    `id` int NOT NULL AUTO_INCREMENT,
    `item` int DEFAULT -1,
    `character` int DEFAULT -1,
    KEY `ci_item_id` (`item`),
    KEY `ci_character_id` (`character`),
    CONSTRAINT `ci_item_id` FOREIGN KEY (`item`) REFERENCES `pathfinder`.`item` (`id`),
    CONSTRAINT `ci_character_id` FOREIGN KEY (`character`) REFERENCES `pathfinder`.`pathfinder_character` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`character_action` (
    `id` int NOT NULL AUTO_INCREMENT,
    `action` int DEFAULT -1,
    `character` int DEFAULT -1,
    KEY `ca_action_id` (`action`),
    KEY `ca_character_id` (`character`),
    CONSTRAINT `ca_action_id` FOREIGN KEY (`action`) REFERENCES `pathfinder`.`action` (`id`),
    CONSTRAINT `ca_character_id` FOREIGN KEY (`character`) REFERENCES `pathfinder`.`pathfinder_character` (`id`),
    PRIMARY KEY (`id`)
);

CREATE TABLE `pathfinder`.`room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room_name` varchar(255) DEFAULT NULL,
  `owner` int DEFAULT NULL,
  `date_added` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_owner` (`owner`),
  CONSTRAINT `fk_owner` FOREIGN KEY (`owner`) REFERENCES `user` (`id`)
);

CREATE TABLE `pathfinder`.`room_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `room_id` int NOT NULL,
  `date_added` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `room_id` (`room_id`),
  CONSTRAINT `fk_room_id` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
);

insert into pathfinder.ability (name, description) values  (
    "Stregnth",
    "Strength measures your character’s physical power. Strength is important if your character plans to engage in hand-to-hand combat. Your Strength modifier gets added to melee damage rolls and determines how much your character can carry."
);

insert into pathfinder.ability (name, description) values  (
    "Dexterity",
);

insert into pathfinder.ability (name, description) values  (
    "Constitution",
    "Constitution measures your character’s overall health and stamina. Constitution is an important statistic for all characters, especially those who fight in close combat. Your Constitution modifier is added to your Hit Points and Fortitude saving throws."
);

insert into pathfinder.ability (name, description) values  (
    "Intelligence",
    "Intelligence measures how well your character can learn and reason. A high Intelligence allows your character to analyze situations and understand patterns, and it means they can become trained in additional skills and might be able to master additional languages."
);

insert into pathfinder.ability (name, description) values  (
    "Wisdom",
    "Wisdom measures your character’s common sense, awareness, and intuition. Your Wisdom modifier is added to your Perception and Will saving throws."
);

insert into pathfinder.ability (name, description) values  (
    "Charisma",
    "Charisma measures your character’s personal magnetism and strength of personality. A high Charisma score helps you influence the thoughts and moods of others."
);

alter table class add column hp_points_per_level int default 0;
alter table class add column hp_points_per_level int default 0;

alter table feat add column prerequesite int default -1;
alter table feat add foreign key (prerequesite) references feat(id);
alter table feat add column level int default 1;
alter table feat add column number_choices int default 1;

insert into pathfinder.feat_classification (name, description) values ('Alchemist', 'Alchemist specific feat');
insert into pathfinder.feat_classification (name, description) values ('General', 'Alchemist specific feat');
insert into pathfinder.feat_classification (name, description) values ('Skill', 'Skill specific feat');
insert into pathfinder.feat_classification (name, description) values ('Ancestry', 'Ancestry specific feat');
insert into pathfinder.feat_classification (name, description) values ('Utility', 'Utility feats used to help the engine run');