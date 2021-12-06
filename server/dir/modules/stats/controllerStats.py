
import threading

class ControllerStats:

    def __init__(self):
        pass

    def get_process_stats(self):
        
        proccess_list = []

        for thread in threading.enumerate():
            proccess_list.append(thread.name)
        
        return proccess_list

    

    # get thread id and name