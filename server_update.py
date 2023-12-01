import time
from flask import Flask
import signal
import git 
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)



@app.route('/<data>', methods=['GET'])
def home(data):
    if data == "update":
        #อัพเดทโค้ดเว็บ
        web = git.cmd.Git('/var/www/html_linaro')
        web.pull()
        time.sleep(5)
        #อัพเดทโค้ด hottub python
        # machine = git.cmd.Git('/home/linaro/hottub_linaro')
        # machine.pull()
        # time.sleep(10)
        cmd = 'sudo reboot'
        os.system(cmd)

    return data

if __name__ =="__main__":
    # signal.signal(signal.SIGTERM, run_loop)
    app.run(debug=True, port=5006, host='0.0.0.0', threaded=True)
   
  
