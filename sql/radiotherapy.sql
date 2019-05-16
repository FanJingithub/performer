use MData;

grant select, insert, update, delete on MData.* to 'fanjin'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table radiotherapy (
    `patient_id`  varchar(12) default '',
    `radio_count`  varchar(12) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
