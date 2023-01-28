import random
from datetime import datetime, timedelta

# list of destination and duration in the format "!Hong Kong, 16h7m"
#
dest_and_dur = ["!Mugla, 11h2m" ,"!London, 7h37m" ,"!Jaipur, 15h9m" ,"!Vancouver, 4h41m" ,"!Orlando, 2h36m" ,"!Amsterdam, 7h57m" ,"!Macau, 16h9m" ,"!Kyoto, 13h40m" ,"!Barcelona, 8h29m" ,"!Johor Bahru, 19h8m" ,"!Dammam, 13h49m" ,"!Venice, 9h2m" ,"!Singapore, 19h9m" ,"!Krakow, 9h14m" ,"!Melbourne, 20h43m" ,"!New York City, 1h17m" ,"!TelAviv, 12h3m" ,"!Heraklion, 10h57m" ,"!Moscow, 9h50m" ,"!Shenzhen, 16h6m" ,"!Sydney, 19h51m" ,"!Guangzhou, 16h2m" ,"!Bangkok, 17h28m" ,"!Johannesburg, 17h4m" ,"!Istanbul, 10h42m" ,"!Lisbon, 7h38m" ,"!Medina, 13h13m" ,"!Chennai, 17h9m" ,"!Prague, 8h50m" ,"!Cancun, 3h43m" ,"!Dublin, 7h3m" ,"!Mumbai, 16h3m" ,"!Zhuhai, 16h8m" ,"!Kolkata, 16h7m" ,"!Brussels, 8h1 minute" ,"!Saint Petersburg, 9h3m" ,"!Shanghai, 14h43m" ,"!Lima, 8h10m" ,"!Vienna, 9h7m" ,"!Antalya, 11h14m" ,"!Riyadh, 13h44m" ,"!Stockholm, 8h23m" ,"!Frankfurt, 8h24m" ,"!Copenhagen, 8h17m" ,"!Los Angeles, 4h51m" ,"!Delhi, 14h59m" ,"!Phuket, 18h16m" ,"!Madrid, 8h1 minute" ,"!Jakarta, 20h9m" ,"!Jerusalem, 12h7m" ,"!San Francisco, 5h2m" ,"!AbuDhabi, 14h19m" ,"!Miami, 2h58m" ,"!Munich, 8h46m" ,"!Krabi, 18h14m" ,"!Rome, 9h19m" ,"!Auckland, 17h45m" ,"!Paris, 7h59m" ,"!Batam, 19h11m" ,"!Milan, 8h46m" ,"!Berlin, 8h34m" ,"!Dubai, 14h17m" ,"!Osaka, 13h43m" ,"!Florence, 9h4m" ,"!Agra, 15h12m" ,"!Guilin, 15h48m" ,"!Las Vegas, 4h24m" ,"!Jeju, 14h15m" ,"!Buenos Aires, 11h35m" ,"!Warsaw, 9h7m" ,"!Mecca, 13h34m" ,"!Bangalore, 17h3m" ,"!Pattaya, 17h34m" ,"!Porto, 7h31m" ,"!Hong Kong, 16h7m" ,"!Marrakesh, 8h16m" ,"!Beijing, 13h42m" ,"!Budapest, 9h23m" ,"!Chiang Mai, 16h46m" ,"!Cairo, 11h58m" ,"!Fukuoka, 14h6m" ,"!Honolulu, 9h49m" ,"!Rhodes, 11h6m" ,"!Hanoi, 16h26m" ,"!Seoul, 13h42m" ,"!Nice, 8h45m" ,"!Hurghada, 12h28m" ,"!Kuala Lumpur, 18h55m" ,"!Da Nang, 17h5m" ,"!Tokyo, 13h23m" ,"!Taipei, 15h33m"]


# list to store modified lines
modified_lines = []

for dest_and_dur_item in dest_and_dur:
    # line in original format
    line = "origin='toronto', destination='Toronto', duration='7h30m', flight='ACA912', airline='West Jet', departureTime='March 5, 2023', seats='26', price='$125'"

    # Split the destination and duration
    destination, duration = dest_and_dur_item.split(", ")

    #Removing the exclamation mark
    destination = destination[1:]

    # Replace the destination and duration in the line
    line = line.replace("origin='toronto'", "origin='" + destination + "'")
    line = line.replace("duration='7h30m'", "duration='" + duration + "'")

    # change last three digits of flight code
    flight_code = line.split("flight='")[1].split("'")[0]
    new_flight_code = flight_code[:-3] + str(random.randint(100, 999))
    line = line.replace(flight_code, new_flight_code)

    # set the departure time to a random date in 2023 in the same format
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    departure_time = random_date.strftime("%B %d, %Y")
    line = line.replace("departureTime='March 5, 2023'", "departureTime='" + departure_time + "'")

    # change seats to a random number between 1 and 9
    line = line.replace("seats='26'", "seats='" + str(random.randint(1, 9)) + "'")

    # add the modified line to the list
    modified_lines.append(line)

for item in modified_lines:
    print(item)
