/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2016/8/22 15:28:54                           */
/*==============================================================*/

create database Dpdb;

use Dpdb;

drop table if exists coach;

drop table if exists lesson;

drop table if exists student;

/*==============================================================*/
/* Table: coach                                                 */
/*==============================================================*/
create table coach
(
   id                   int not null,
   name                 varchar(128),
   primary key (id)
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

