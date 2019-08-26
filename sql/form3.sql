use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table form3 (
    `xm`  varchar(12) default '',
    `xb`  varchar(12) default '',
    `nl`  varchar(12) default '',
    `sj_0`  varchar(12) default '',
    `sj_1`  varchar(12) default '',
    `sj_2`  varchar(12) default '',
    `sj_3`  varchar(12) default '',
    `sj_4`  varchar(12) default '',
    `lx_0`  varchar(12) default '',
    `lx_1`  varchar(12) default '',
    `lx_2`  varchar(12) default '',
    `lx_3`  varchar(12) default '',
    `lx_4`  varchar(12) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
