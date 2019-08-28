use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table lab (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
