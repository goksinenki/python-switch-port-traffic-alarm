# python-switch-port-traffic-alarm
Port Traffic/Bandwidth Monitor Script

That's an Switch Port Traffic monitor program is checking the switch uplink port traffic and send mail notifications if the bandwidth exceeds 1.5 Gbps (you 
can modify the value)

The process includes:

1- Script is making SSH connection to network device and checking the uplink port traffic 
2- Write the output to a file
3- Parse the file and compare the values with the threshold value here is 1.5 Gbps (1500000000 bit/sec) 
4- Send email if it exceeds the value

You can add the script to a cronjob and can execute it every 3 minutes...etc

Do not forget to allow mail relay from your mail server for your script.

Here is a screenshot below.

![image](https://user-images.githubusercontent.com/917944/130779969-bd256025-47d5-4633-8483-6088475bb0c0.png)



INSTALLATION (Windows/Linux)

Installation

Just install the required modules/libraries to your python project directory if you do not have them

smtplib, xlsxwriter, csv, openpyxl

For example:

pip install openpyxl
pip install paramiko 

Please look at http://www.paramiko.org/installing.html if you have problems with installing modules

Open ip.txt and replace hostnames and ip addresses with your network device information. Open monitor.py and replace the required e-mail addresses with your information.

Then, execute traffic.py

python traffic.py

If you like you can schedule that script before the production time (Sunday nights) to be sure that all critical devices are up at production time.

That's all !
