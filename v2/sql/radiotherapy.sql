use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists radiotherapy;

create table radiotherapy (
    `patient_id`  varchar(20) default '',
    `radio_count`  varchar(20) default '',
    `radio_start`  varchar(20) default '',
    `radio_end`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
