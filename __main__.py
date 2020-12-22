
from time import sleep

from request.Update_nameday import Update_nameday
from request.Update_to_txt import Update_to_txt

while True:
    update_name_day = Update_nameday()
    nameday = update_name_day.update_nameday()
    update_to_txt = Update_to_txt()

    update_to_txt.update_to_txt(nameday)

    print(nameday)
    sleep(60)



