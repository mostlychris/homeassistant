import subprocess
import sys
params = sys.argv[1]
cmd = "/config/alexa/alexa_remote_control.sh " + params
x = subprocess.check_output(cmd, shell=True)
print(x.decode("utf-8"))
