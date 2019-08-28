use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table data_status (
    `patient_id`  varchar(12)  default '',
    `base`  INT default 0,
    `lab`  INT default 0,
    `pathology`  INT default 0,
    `surgery`  INT default 0,
    `chemotherapy`  INT default 0,
    `radiotherapy`  INT default 0,
    `follow_up`  INT default 0
) engine=innodb         default charset=utf8;
