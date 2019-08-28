use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table surgery (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
