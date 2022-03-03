open_delay = 60
cleanup_time = 35

def runtime_string_to_minutes(runtime_string) -> int:
    runtime_string_split = runtime_string.split(':')
    return int(runtime_string_split[0])*60+int(runtime_string_split[1])

def pad_runtime(runtime) -> int:
    runtime_rounded = 5 * round((runtime)/5)
    if runtime_rounded < runtime:
        runtime_rounded = runtime_rounded + 5
    return runtime_rounded

def minutes_to_time_string(time):
    hours = int(time/60)
    minutes = str(time-(60*hours))
    hours = str(hours)
    if len(hours) == 1:
        hours = "0"+hours
    if len(minutes) == 1:
        minutes = "0"+minutes
    return f"{hours}:{minutes}"

def generate_showtimes(today,runtime_string):
    runtime = runtime_string_to_minutes(runtime_string)
    runtime_pad = pad_runtime(runtime)
    weekday = today.weekday()+3
    
    open_time = ((8*60) if weekday < 4 else int(10.5*60)) + 60
    end_time = (23*60) if weekday < 4 else int(23.5*60)

    total_mintes = end_time - open_time
    
    showtimes = []

    while total_mintes > runtime_pad + 35:
        total_mintes = total_mintes - (runtime_pad + (0 if len(showtimes)==0 else 35))
        showtime = f"  {minutes_to_time_string(open_time+total_mintes)} - {minutes_to_time_string(open_time+total_mintes+runtime)}" 
        showtimes.append(showtime)

    showtimes.reverse()
    return showtimes

def main():
    print(minutes_to_time_string(123))

if __name__ == "__main__":
    main()
