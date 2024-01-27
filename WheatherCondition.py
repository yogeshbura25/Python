Temperature = float(input())
if Temperature < 0:
    print("Freezing weather")
elif 0 <= Temperature < 10:
    print("Very Cold weather")
elif 0 <= Temperature < 20:
    print("Cold weather")
elif 20 <= Temperature < 30:
    print("Normal")
elif 30 <= Temperature < 40:
    print("Hot")
elif Temperature >= 40:
    print("Very Hot")