CREATE TABLE `attribute` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `attribute_modifier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `modifier_id` int NOT NULL,
  `attribute_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `am_modifier_id` (`modifier_id`),
  KEY `am_attribute_id` (`attribute_id`),
  CONSTRAINT `am_attribute_id` FOREIGN KEY (`attribute_id`) REFERENCES `attribute` (`id`),
  CONSTRAINT `am_modifier_id` FOREIGN KEY (`modifier_id`) REFERENCES `modifier` (`id`)
)

CREATE TABLE `character_trait` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `character_trait_modifier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `modifier_id` int NOT NULL,
  `trait_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ct_trait_id` (`trait_id`),
  KEY `ct_modifier_id` (`modifier_id`),
  CONSTRAINT `ct_modifier_id` FOREIGN KEY (`modifier_id`) REFERENCES `modifier` (`id`),
  CONSTRAINT `ct_trait_id` FOREIGN KEY (`trait_id`) REFERENCES `character_trait` (`id`)
)

CREATE TABLE `class` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `eye_color` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `modifier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `score` int DEFAULT NULL,
  `character_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `character_id` (`character_id`),
  CONSTRAINT `modifier_ibfk_1` FOREIGN KEY (`character_id`) REFERENCES `pathfinder_character` (`id`)
)

CREATE TABLE `modifier_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `modifier_group_modifier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `modifier_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mgm_group_id` (`group_id`),
  KEY `mgm_modifier_id` (`modifier_id`),
  CONSTRAINT `mgm_group_id` FOREIGN KEY (`group_id`) REFERENCES `modifier_group` (`id`),
  CONSTRAINT `mgm_modifier_id` FOREIGN KEY (`modifier_id`) REFERENCES `modifier` (`id`)
)

CREATE TABLE `pathfinder_character` (
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
)

CREATE TABLE `race` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room_name` varchar(255) DEFAULT NULL,
  `owner` int DEFAULT NULL,
  `date_added` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_owner` (`owner`),
  CONSTRAINT `fk_owner` FOREIGN KEY (`owner`) REFERENCES `user` (`id`)
)

CREATE TABLE `room_user` (
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
)

CREATE TABLE `save` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `score` int DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `save_modifier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `modifier_id` int NOT NULL,
  `save_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sm_save_id` (`save_id`),
  KEY `ct_modifier_id` (`modifier_id`),
  CONSTRAINT `sm_modifier_id` FOREIGN KEY (`modifier_id`) REFERENCES `modifier` (`id`),
  CONSTRAINT `sm_save_id` FOREIGN KEY (`save_id`) REFERENCES `save` (`id`)
)

CREATE TABLE `skill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `attribute_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `skill_attribute_id` (`attribute_id`),
  CONSTRAINT `skill_attribute_id` FOREIGN KEY (`attribute_id`) REFERENCES `attribute` (`id`)
)

CREATE TABLE `skill_modifier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `modifier_id` int NOT NULL,
  `skill_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `skm_modifier_id` (`modifier_id`),
  KEY `skm_skill_id` (`skill_id`),
  CONSTRAINT `skm_modifier_id` FOREIGN KEY (`modifier_id`) REFERENCES `modifier` (`id`),
  CONSTRAINT `skm_skill_id` FOREIGN KEY (`skill_id`) REFERENCES `skill` (`id`)
)

CREATE TABLE `skill_rank` (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` int DEFAULT NULL,
  `skill_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `skill_id` (`skill_id`),
  CONSTRAINT `sr_skill_id` FOREIGN KEY (`skill_id`) REFERENCES `skill` (`id`)
)

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `date_added` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
)

