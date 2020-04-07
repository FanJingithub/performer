use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table chemotherapy (
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
