import sched
import time

def schedule_func(evnt_time,func,*args):
    s = sched.scheduler(time.time,time.sleep)
    s.enterabs(evnt_time,1,func,argument=args)
    print(f"{func.__name__}() scheduled for {time.asctime(time.localtime(evnt_time))}")
    s.run()

schedule_func(time.time()+2,print,"Howdy")