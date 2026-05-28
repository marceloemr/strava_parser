import csv
import sqlite3
from datetime import datetime
from argparse import ArgumentParser

VALID_ACTIVITIES = {
    "Walk": "Walk", 
    "Caminhada": "Walk", 
    "Run": "Run", 
    "Corrida": "Run"
}

def main(csv_file: str, db_file: str):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activities (
        ActivityId INTEGER PRIMARY KEY,
        Date TEXT,  -- ISO-8601
        ActivityName TEXT,
        Type TEXT,
        Distance REAL,
        ElapsedTime INTEGER,
        MovingTime INTEGER
    )
    """)

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        header = next(reader)

        for row in reader:
            if not row or len(row) < 19:
                continue

            activity_id = row[0]
            date = row[1]
            activity_name = row[2]
            activity_type = row[3]
            elapsed_time = row[5]
            moving_time = row[16]
            distance = row[17]

            if activity_type not in VALID_ACTIVITIES.keys():
                continue

            dt = datetime.strptime(date, "%b %d, %Y, %I:%M:%S %p")
            iso_date = dt.strftime("%Y-%m-%d %H:%M:%S")

            activity_type = VALID_ACTIVITIES[activity_type]

            cursor.execute("""
            INSERT OR IGNORE INTO activities
            (ActivityId, Date, ActivityName, Type, Distance, ElapsedTime, MovingTime)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                activity_id,
                iso_date,
                activity_name,
                activity_type,
                distance,
                elapsed_time,
                moving_time
            ))

    conn.commit()
    conn.close()

    print("CSV data successfully imported into SQLite.")

if __name__ == '__main__':
    parser = ArgumentParser(
            prog='ParseActivities',
            description='Parse activities.csv file exported from strava into a sqlite database')
    parser.add_argument('-c', '--csv_file', required=True)
    parser.add_argument('-d', '--db_file', required=True)

    args = parser.parse_args()

    main(args.csv_file, args.db_file)
