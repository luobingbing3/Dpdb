USE `Dpdb`;
DROP procedure IF EXISTS `sp_insertStuCoach`;

DELIMITER $$
USE `Dpdb`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertStuCoach`(
   IN p_student_id      bigint,
   IN p_student_name    varchar(128),
   IN p_gender          varchar(20),
   IN p_age             int,
   IN p_height 			int,
   IN p_coach_name 		varchar(128),
   IN p_coach_id        int
)
BEGIN
    if ( select exists (select 1 from coach where id = p_coach_id and name_ = p_coach_name) ) THEN
        
        UPDATE coach SET  id = p_coach_id,
						   name_ = p_coach_name
                           WHERE id = p_coach_id and name_ = p_coach_name;
	ELSE
		insert INTO coach (id, name_)
          VALUES ( p_coach_id,p_coach_name);
    END IF;
    
    if ( select exists (select 1 from student where id = p_student_id and name_ = p_student_name) ) THEN
        
        UPDATE student SET  id = p_student_id,
						    name_ = p_student_name,
                            gender = p_gender,
                            age = p_age,
                            height = p_height,
                            coach_id = p_coach_id
                           WHERE id = p_student_id and name_ = p_student_name;
	ELSE
		insert INTO student (id, name_,gender,age,height,coach_id)
          VALUES ( p_student_id,p_student_name,p_gender,p_age,p_height,p_coach_id);
    END IF;
END$$

DELIMITER ;