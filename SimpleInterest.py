import sys
if len(sys.argv) == 4:
    script_name = sys.argv[0]   # script name
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    principal = 10000
    rate = 5.0
    time = 10
simple_interest = (principal * rate * time) / 100
print("Principal Amount is:", principal)
print("Rate of Interest is:", rate)
print("Time Period is:", time)
print("Simple Interest is:", simple_interest)
