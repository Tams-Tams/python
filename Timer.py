import time #importing module time
a = time() #time in seconds from 1970 1.1. 00:00:00:00 till now
sleep(10) #here you can measure time and do something (I wanted to measure the code "sleep(10)" which waits 10 seconds)
b = time() #time in seconds from 1970 1.1. 00:00:00:00 till now
time_from_line_2_to_line_4 = b - a
