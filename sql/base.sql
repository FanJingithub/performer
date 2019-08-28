use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table base (
    `patient_id`  varchar(20) default '',
    `name`  varchar(20) default '',
    `sex`  varchar(20) default '',
    `age`  varchar(20) default '',
    `marriage`  varchar(20) default '',
    `site`  varchar(20) default '',
    `stage`  varchar(20) default '',
    `grade`  varchar(20) default '',
    `surgery`  varchar(20) default '',
    `radiotherapy`  varchar(20) default '',
    `chemotherapy`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
