use Test;

grant select, insert, update, delete on Test.* to 'root'@'localhost' identified by '1';

drop table if exists lab;

create table lab (
    `patient_id`  varchar(20) default '',
    `CEA`  varchar(20) default '',
    `CA199`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
