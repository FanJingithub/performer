use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists radiotherapy_0;

create table radiotherapy_0 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_1;

create table radiotherapy_1 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_2;

create table radiotherapy_2 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_3;

create table radiotherapy_3 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_4;

create table radiotherapy_4 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_5;

create table radiotherapy_5 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_6;

create table radiotherapy_6 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_7;

create table radiotherapy_7 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_8;

create table radiotherapy_8 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists radiotherapy_9;

create table radiotherapy_9 (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

