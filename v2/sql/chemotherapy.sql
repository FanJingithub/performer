use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists chemotherapy_0;

create table chemotherapy_0 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_1;

create table chemotherapy_1 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_2;

create table chemotherapy_2 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_3;

create table chemotherapy_3 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_4;

create table chemotherapy_4 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_5;

create table chemotherapy_5 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_6;

create table chemotherapy_6 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_7;

create table chemotherapy_7 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_8;

create table chemotherapy_8 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists chemotherapy_9;

create table chemotherapy_9 (
    `patient_id`  varchar(20) default '',
    `chemo_way`  varchar(20) default '',
    `chemo_way_other`  varchar(50) default '',
    `last_chemo`  varchar(20) default '',
    `chemo_time_0`  varchar(20) default '',
    `chemo_time_1`  varchar(20) default '',
    `chemo_time_2`  varchar(20) default '',
    `chemo_way_0`  varchar(20) default '',
    `chemo_way_1`  varchar(20) default '',
    `chemo_way_2`  varchar(20) default '',
    `desc_0`  varchar(20) default '',
    `desc_1`  varchar(20) default '',
    `desc_2`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

