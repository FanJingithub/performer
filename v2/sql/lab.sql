use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists lab_0;

create table lab_0 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_1;

create table lab_1 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_2;

create table lab_2 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_3;

create table lab_3 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_4;

create table lab_4 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_5;

create table lab_5 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_6;

create table lab_6 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_7;

create table lab_7 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_8;

create table lab_8 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists lab_9;

create table lab_9 (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

