import os
import time
#from slacker import Slacker

ip_jobplanet = ['104.20.73.240','104.20.72.240']
ip_api_jobplanet = ['104.20.176.8','104.20.177.8']
dig_jobplanet = ['dig www.jobplanet.co.kr @210.220.163.82', 'dig www.jobplanet.co.kr @219.250.36.130']
dig_api_jobplanet = ['dig api.jobplanet.co.kr @210.220.163.82', 'dig api.jobplanet.co.kr @219.250.36.130']

#slack_bot_token = 'xoxb-132785230309-vr1hAiKd6GOzEYyRkq5mSCrp'
#slack = Slacker(slack_bot_token)

def skt_dns(dig_job, ip_job):
    f = open("./dig_SKT_DNS.txt", "a")

    for dig in dig_job:
        answer = os.system(dig)

        for ip in ip_job:
            if str(answer).find(ip):
                result = "{}: DNS = %s, %s = true \n".format(time.ctime()) %(dig, ip)
                f.write(result)
                #slack.chat.post_message(channel="#qa_engineering", text=result)
            else:
                result = "{}: DNS = %s, %s = true \n".format(time.ctime()) % (dig, ip)
                f.write(result)

    f.close()

for i in range(1, 2):
    skt_dns(dig_jobplanet, ip_jobplanet)
 #   skt_dns(dig_api_jobplanet, ip_api_jobplanet)