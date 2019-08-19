- scrap basic from herodb
- integrate with https://github.com/joke2k/faker  (perhaps add a provider!?)
- create installer (wheel) and push to devpi
- write a beautiful makefile https://itnext.io/docker-makefile-x-ops-sharing-infra-as-code-parts-ea6fa0d22946


https://devpi.net/docs/devpi/devpi/stable/+d/quickstart-releaseprocess.html#initializing-a-basic-server-and-index

$ devpi use https://devpi.speag.com
using server: https://devpi.speag.com/ (not logged in)
no current index: type 'devpi use -l' to discover indices
venv for install/set commands: /home/crespo/devp/userhero/.venv
only setting venv pip cfg, no global configuration changed
/home/crespo/devp/userhero/.venv/pip.conf: no config file exists
always-set-cfg: no

$ devpi login crespo
password for user crespo: 
logged in 'crespo' at None, credentials valid for 10.00 hours

$ devpi use
using server: https://devpi.speag.com/ (logged in as crespo)
no current index: type 'devpi use -l' to discover indices
venv for install/set commands: /home/crespo/devp/userhero/.venv
only setting venv pip cfg, no global configuration changed
/home/crespo/devp/userhero/.venv/pip.conf: no config file exists
always-set-cfg: no

$ devpi index --create dev
PUT https://devpi.speag.com/crespo/dev
404 Not Found: no user 'crespo'



$ devpi logout