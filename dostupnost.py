import time
import requests
import csv

RUNTIME = 7 * 24 * 60 * 60
INTERVAL = 10 * 60
START = time.time()
FILE_PATHS = ["homepage.csv", "infopage.csv"]
URLS = ["https://www.ui42.sk/", "https://www.ui42.sk/o-nas"]
TITLES = ['merana URL', 'datum a cas merania', 'chybovy kod HTTP requestu', 'velkost nacitaneho HTML kodu', 'cas od requestu po koniec nacitavania']

START_TIME = time.localtime()
for i in range(2):
    with open(FILE_PATHS[i], 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(TITLES)

while time.time() - START < RUNTIME:
    for i in range(2):
        file_path = FILE_PATHS[i]
        url = URLS[i]
        currentTime = time.asctime(time.localtime())
        response = requests.get(url)
        statusCode = response.status_code
        size = len(response.content)
        responseTime = response.elapsed.total_seconds()
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            row = [url, currentTime, statusCode, size, responseTime]
            writer.writerow(row)
    time.sleep(INTERVAL)
END_TIME = time.localtime()

with open("stats.txt", "w") as f:
    f.write(f"Cas monitorovacieho merania: {int(RUNTIME / 60)} minut\n")
    f.write(f"Zaciatok: {START_TIME[2]}.{START_TIME[1]}.{START_TIME[0]} {START_TIME[3]}:{START_TIME[4]}:{START_TIME[5]}\n")
    f.write(f"Koniec: {END_TIME[2]}.{END_TIME[1]}.{END_TIME[0]} {END_TIME[3]}:{END_TIME[4]}:{END_TIME[5]}\n")
    f.write(f"Interval: {int(INTERVAL / 60)} minut")