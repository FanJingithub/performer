use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists pathology_0;

create table pathology_0 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_1;

create table pathology_1 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_2;

create table pathology_2 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_3;

create table pathology_3 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_4;

create table pathology_4 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_5;

create table pathology_5 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_6;

create table pathology_6 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_7;

create table pathology_7 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_8;

create table pathology_8 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

drop table if exists pathology_9;

create table pathology_9 (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;

