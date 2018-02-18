#Retrieve environment variables' values
#To set those up go to: Control Panel-> System and Security-> System-> Adv. Properties (Sidebar)-> Env. Variables (at the bottom)
#Then add the new (user) variables: a name to access it (upper case-only preferably) and the corresponding value

import os

#os.environ returns a dictionary, so to get the env. variable (the value), get it using the corresponding key (env. variable name)
log_in_id = os.environ.get('LOG_IN_ID')
log_in_pass = os.environ.get('LOG_IN_PASS')
print(log_in_id, log_in_pass)