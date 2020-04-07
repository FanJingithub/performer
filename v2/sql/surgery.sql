use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists surgery;

create table surgery (
    `patient_id`  varchar(20) default '',
    `resection_way`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
