#!/bin/bash

sudo -S mkdir /srv/MData_all/CRF/log << EOF
cvm@fj123
EOF

sudo -S supervisorctl reload << EOF
cvm@fj123
EOF
        