use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists data_status;

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
