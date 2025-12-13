import time

hour = int(time.strftime('%H'))

if hour < 12:
    print("Good Morning ☀️")
elif hour < 17:
    print("Good Afternoon 🌤️")
else:
    print("Good Evening 🌙")
