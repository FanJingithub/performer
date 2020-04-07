#!/bin/bash
sudo -S cp ../supervisor/Test.conf /etc/supervisor/conf.d/ << EOF
13298698385fj^
EOF

sudo -S supervisorctl reload << EOF
13298698385fj^
EOF

sudo -S supervisorctl start Test << EOF
13298698385fj^
EOF
    