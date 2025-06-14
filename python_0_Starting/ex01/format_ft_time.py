from datetime import datetime
import time

now = datetime.now()

seconds = time.time()
scientific_notation = "{:.2e}".format(seconds)


print(f"Seconds since January 1, 1970: {seconds} or "
      f"{scientific_notation} in scientific notation")
print(now.strftime("%b %d %Y"))
