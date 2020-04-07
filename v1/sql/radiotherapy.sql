use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table radiotherapy (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
