use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table form3 (
    `patient_id`  varchar(20) default '',
    `xm`  varchar(20) default '',
    `xb`  varchar(20) default '',
    `xb_other`  varchar(50) default '',
    `nl`  varchar(20) default '',
    `sj_0`  varchar(20) default '',
    `sj_1`  varchar(20) default '',
    `sj_2`  varchar(20) default '',
    `sj_3`  varchar(20) default '',
    `sj_4`  varchar(20) default '',
    `lx_0`  varchar(20) default '',
    `lx_1`  varchar(20) default '',
    `lx_2`  varchar(20) default '',
    `lx_3`  varchar(20) default '',
    `lx_4`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
