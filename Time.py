from datetime import datetime

status = "STOP"
prev_status = None
current_status = None
time_base = None
time_count = None
time_count_sum = None

while status != "q":
    if status == "P":
        now_time = datetime.now()
        time_count = (now_time-time_base)+time_count_sum
        print("Time Base: ", time_base, "Current Time: ", now_time, "Time Count: ", time_count, "Sum: ", time_count_sum, "Status: ", current_status)
    else:
        current_status = status
        if prev_status == None:
            time_base = datetime.now()
            time_count = time_base-time_base
            time_count_sum = time_count
            prev_status = current_status
        elif prev_status == "STOP":
            time_base = datetime.now()
            time_count = time_base-time_base
            prev_status = current_status
        elif prev_status == "START":
            stop_time = datetime.now()
            time_count = stop_time-time_base
            time_count_sum += time_count
            prev_status = current_status
    status = input("Enter Status: ")
