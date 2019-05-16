use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table chemotherapy (
    `patient_id`  varchar(12) default '',
    `chemo_way`  varchar(12) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
