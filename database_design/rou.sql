/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2016/8/23 10:22:21                           */
/*==============================================================*/

drop database if exists Dpdb;

create database Dpdb CHARACTER SET utf8 COLLATE utf8_general_ci;

use Dpdb;

drop table if exists coach;

drop table if exists lesson;

drop table if exists student;

/*==============================================================*/
/* Table: coach                                                 */
/*==============================================================*/
create table coach
(
   id                   bigint not null,
   name_                varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci,
   primary key (id)
);

/*==============================================================*/
/* Table: lesson                                                */
/*==============================================================*/
create table lesson
(
   id                   bigint not null auto_increment,
   coach_id             bigint,
   student_id           bigint,
   date_                date,
   number_               int,
   weight               float,
   blood_pressure_before int,
   blood_pressure_after int,
   heart_rate           int,
   body_fat_chest       int,
   body_fat_abdomen     int,
   body_fat_leg         int,
   body_fat             float,
   chest_circumference_max float,
   waistline_navel      float,
   hipline              float,
   WHR                  float,
   arms                 float,
   thigh_circumference  float,
   calf_circumference   float,
   push_up              int,
   trx                  int,
   squat                int,
   plank                int,
   balance_left         int,
   balance_right        int,
   primary key (id)
);

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   id                   bigint not null,
   name_                varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci,
   gender               varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
   age                  int,
   height               int,
   coach_id             bigint,
   primary key (id)
);

SET SQL_SAFE_UPDATES = 0;