time = input("Please enter time: ").strip()

hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)

total_minutes = hours * 60 + minutes

if 7 * 60 <= total_minutes <= 8 * 60:
    print("breakfast time")
elif 12 * 60 <= total_minutes <= 13 * 60:
    print("lunch time")
elif 18 * 60 <= total_minutes <= 19 * 60:
    print("dinner time")
