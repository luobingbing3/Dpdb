USE `Dpdb`;
DROP procedure IF EXISTS `sp_insertData`;

DELIMITER $$
USE `Dpdb`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertData`(
   IN p_coach_id             bigint,
   IN p_student_id           bigint,
   IN p_date_                date,
   IN p_number_               int,
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
    if ( select exists (select 1 from lesson where coach_id = p_coach_id and student_id = p_student_id and date_ = p_date_ and number_ = p_number_) ) THEN
        
        UPDATE lesson SET  number_ = p_number_,
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
                           WHERE coach_id = p_coach_id and student_id = p_student_id and date_ = p_date_ and number_ = p_number_;
	ELSE
		insert INTO lesson (coach_id,student_id, date_, number_,weight,blood_pressure_before,
          blood_pressure_after,heart_rate,body_fat_chest,body_fat_abdomen,
          body_fat_leg,body_fat,chest_circumference_max,waistline_navel,
          hipline,WHR,arms,thigh_circumference,calf_circumference,push_up,
          trx,squat,plank,balance_left,balance_right)
          VALUES ( p_coach_id,
				   p_student_id,
				   p_date_,
				   p_number_,
				   p_weight,
				   p_blood_pressure_before,
				   p_blood_pressure_after,
				   p_heart_rate,
				   p_body_fat_chest,
				   p_body_fat_abdomen,
				   p_body_fat_leg,
				   p_body_fat,
				   p_chest_circumference_max,
				   p_waistline_navel,
				   p_hipline,
				   p_WHR,
				   p_arms,
				   p_thigh_circumference,
				   p_calf_circumference,
				   p_push_up,
				   p_trx,
				   p_squat,
				   p_plank,
				   p_balance_left,
				   p_balance_right);
      
    END IF;
END$$

DELIMITER ;