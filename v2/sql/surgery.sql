use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists surgery_0;

create table surgery_0 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_1;

create table surgery_1 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_2;

create table surgery_2 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_3;

create table surgery_3 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_4;

create table surgery_4 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_5;

create table surgery_5 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_6;

create table surgery_6 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_7;

create table surgery_7 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_8;

create table surgery_8 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists surgery_9;

create table surgery_9 (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

