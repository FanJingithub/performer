use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists follow_up_0;

create table follow_up_0 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_1;

create table follow_up_1 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_2;

create table follow_up_2 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_3;

create table follow_up_3 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_4;

create table follow_up_4 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_5;

create table follow_up_5 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_6;

create table follow_up_6 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_7;

create table follow_up_7 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_8;

create table follow_up_8 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists follow_up_9;

create table follow_up_9 (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

