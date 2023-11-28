from datetime import datetime

dateTimeNow = datetime.now()
secondPassed = dateTimeNow.timestamp()

print('Seconds since January 1, 1970:',f"{secondPassed:,}", "or", f"{secondPassed:.3}", "in scientific notation")
print(dateTimeNow.strftime("%b %d %Y"))