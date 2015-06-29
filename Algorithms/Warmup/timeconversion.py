# Enter your code here. Read input from STDIN. Print output to STDOUT

from datetime import datetime

time = datetime.strptime(raw_input(), "%I:%M:%S%p")
print time.strftime("%H:%M:%S")