CREATE TABLE `ONS_Weeklies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `week_number` int NOT NULL,
  `week_ended` date NOT NULL,
  `uk` int DEFAULT NULL,
  `england` int DEFAULT NULL,
  `wales` int DEFAULT NULL,
  `scotland` int DEFAULT NULL,
  `northern_ireland` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
