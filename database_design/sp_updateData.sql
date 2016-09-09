USE `Dpdb`;
DROP procedure IF EXISTS `sp_updateData`;

DELIMITER $$
USE `Dpdb`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updateData`(
   IN p_id                  bigint,
   IN p_weight               float,
   IN p_blood_pressure_before int,
   IN p_blood_pressure_after int,
   IN p_heart_rate           int,
   IN p_body_fat_chest       int,
   IN p_body_fat_abdomen     int,
   IN p_body_fat_leg         int,
   IN p_body_fat             float,
   IN p_chest_circumference_max float,
   IN p_waistline_navel      float,
   IN p_hipline              float,
   IN p_WHR                  float,
   IN p_arms                 float,
   IN p_thigh_circumference  float,
   IN p_calf_circumference   float,
   IN p_push_up              int,
   IN p_trx                  int,
   IN p_squat                int,
   IN p_plank                int,
   IN p_balance_left         int,
   IN p_balance_right        int
)
BEGIN
    if ( select exists (select 1 from lesson where  id = p_id) ) THEN

        UPDATE lesson SET
						   weight = p_weight,
						   blood_pressure_before = p_blood_pressure_before,
						   blood_pressure_after = p_blood_pressure_after,
						   heart_rate = p_heart_rate,
						   body_fat_chest = p_body_fat_chest,
						   body_fat_abdomen = p_body_fat_abdomen,
						   body_fat_leg = p_body_fat_leg,
						   body_fat = p_body_fat,
						   chest_circumference_max = p_chest_circumference_max,
						   waistline_navel = p_waistline_navel,
						   hipline  = p_hipline,
						   WHR = p_WHR,
						   arms = p_arms,
						   thigh_circumference = p_thigh_circumference,
						   calf_circumference = p_calf_circumference,
						   push_up = p_push_up,
						   trx = p_trx,
						   squat = p_squat,
						   plank = p_plank,
						   balance_left = p_balance_left,
						   balance_right = p_balance_right
                           WHERE id = p_id;

    END IF;
END$$

DELIMITER ;