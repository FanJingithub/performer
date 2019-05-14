use MData;

grant select, insert, update, delete on MData.* to 'fanjin'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table data_status (
    `patient_id`  varchar(12)  default '',
    `base`  INT default 0,
    `lab`  INT default 0
) engine=innodb         default charset=utf8;
