use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists follow_up;

create table follow_up (
    `patient_id`  varchar(20) default '',
    `recurrance`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
