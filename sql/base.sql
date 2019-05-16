use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table base (
    `patient_id`  varchar(12) default '',
    `name`  varchar(12) default '',
    `sex`  varchar(12) default '',
    `stage`  varchar(12) default '',
    `surgery`  varchar(12) default '',
    `radiotherapy`  varchar(12) default '',
    `age`  varchar(12) default '',
    `marriage`  varchar(12) default '',
    `grade`  varchar(12) default '',
    `chemotherapy`  varchar(12) default '',
    `site`  varchar(12) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
