# https://cs50.harvard.edu/python/2022/psets/1/meal/

# In meal.py, implement a program that prompts the user for a time and outputs whether
#  it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t
#  output anything at all. Assume that the user’s input will be formatted in 24-hour
#  time as #:## or ##:##. And assume that each meal’s time range is inclusive. For
#  instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time
#  for breakfast.

def main():
    time = convert(input("Time: ").strip())
    if time >= 7 and time <= 8:
        print("Breakfast time!")
    elif time >= 12 and time <= 13:
        print("Lunch time!")
    elif time >= 18 and time <= 19:
        print("Dinner time!")

# converts time, a str in 24-hour format, to the corresponding number of hours as a float.
#  For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should
#  return 7.5 (i.e., 7.5 hours).
def convert(time):
    split = time.split(":")
    if (len(split) != 2):
        print("Invalid time format!")
        print("Expected input is 24-hour time as #:## or ##:##")
        exit(1)

    hrs = float(split[0])
    min = float(split[1])
    if (hrs < 0 or hrs > 23 or min < 0 or min > 60):
        print("Invalid time format!")
        print("Expected input is 24-hour time as #:## or ##:##")
        exit(1)

    return hrs + min/60

if __name__ == "__main__":
    main()