use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table follow_up (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
