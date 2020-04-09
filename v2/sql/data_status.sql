use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists data_status;

create table data_status (
    `patient_id`  varchar(12)  default '',
    `base`  varchar(20) default "0",
    `lab`  varchar(20) default "0",
    `pathology`  varchar(20) default "0",
    `surgery`  varchar(20) default "0",
    `chemotherapy`  varchar(20) default "0",
    `radiotherapy`  varchar(20) default "0",
    `follow_up`  varchar(20) default "0"
) engine=innodb         default charset=utf8;
