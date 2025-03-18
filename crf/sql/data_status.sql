use CRF;

drop table if exists data_status;

create table data_status (
    `patient_id`  varchar(64)  default '',
    `base`  varchar(256) default "0",
    `physical_exam`  varchar(256) default "0",
    `lab`  varchar(256) default "0",
    `special_exam`  varchar(256) default "0",
    `radiology_colonoscopy`  varchar(256) default "0",
    `colonoscopy_pathology`  varchar(256) default "0",
    `msi_mmr`  varchar(256) default "0",
    `gene`  varchar(256) default "0",
    `clinical_stage`  varchar(256) default "0",
    `before_evaluate`  varchar(256) default "0",
    `treatment`  varchar(256) default "0",
    `after_evaluate`  varchar(256) default "0",
    `adverse_event`  varchar(256) default "0",
    `concomitant_medication`  varchar(256) default "0",
    `follow_up`  varchar(256) default "0"
) engine=innodb         default charset=utf8;
