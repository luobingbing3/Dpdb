/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2016/8/19 0:18:36                            */
/*==============================================================*/
create database dpdb;

use dpdb;

drop table if exists coach;

drop table if exists lesson;

drop table if exists student;

/*==============================================================*/
/* Table: coach                                                 */
/*==============================================================*/
create table coach
(
   id                   int,
   name                 varchar(128)
);

/*==============================================================*/
/* Table: lesson                                                */
/*==============================================================*/
create table lesson
(
   id                   int not null auto_increment,
   coach_id             int,
   student_id           int,
   date                 date,
   number               int,
   weight               int,
   height               int,
   index3               int,
   primary key (id)
);

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   id                   int not null,
   name                 varchar(128),
   age                  int,
   coach_id             int,
   primary key (id)
);

