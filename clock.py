
#from python advanced sceduler->userguide->interval->

from apscheduler.schedulers.blocking import BlockingScheduler
from Honey import send_msg


# def job_function():
#     print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', seconds=5)

sched.start()


#host it in server for sending it without internet...we use heroku

#add requirements to add external dependencies