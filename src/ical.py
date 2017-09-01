import pandas as pd
import re
import datetime as dt
from icalendar import Calendar, Event
from optparse import OptionParser
import logging

logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)

_author__ = "Aonghus Lawlor"
__copyright__ = "Copyright (c) 2017"
__credits__ = ["Aonghus Lawlor"]
__license__ = "All Rights Reserved"
__version__ = "1.0.0"
__maintainer__ = "Aonghus Lawlor"
__email__ = "aonghus.lawlor@ucd.ie"
__status__ = "Development"


def tt_to_ical(options):
    input_file = options.input
    module = options.module

    logging.info('module: %s', module)
    logging.info('reading from: %s', input_file)

    df = None
    try:
        df = pd.read_csv(input_file)
    except:
        logging.info("could not read input file %s", input_file)
        return

    cal = Calendar()
    cal.add('prodid', '-//UCD Timetable to iCal//ucd.ie//')
    cal.add('version', '2.0')

    prev_ws = None
    day_delta = {"Mon": 0,
                 'Tue': 1,
                 'Wed': 2,
                 'Thu': 3,
                 'Fri': 4,
                 'Sat': 5,
                 'Sun': 6}

    for i in range(len(df)):
        row = df.iloc[i]
        ws = row['Week Starting']

        if pd.isnull(ws):
            curr_ws = prev_ws
        else:
            curr_ws = ws
            prev_ws = ws

        start_hr = int(row['Start Time'].split(':')[0])
        length_mins = int(re.split('(\d+)mins', row['Length'])[1])
        ws_dt = dt.datetime.strptime(curr_ws, '%d %b %Y')
        start = ws_dt + dt.timedelta(days=day_delta[row['Day']], hours=start_hr)
        # print(ws, curr_ws, ws_dt, ws_dt.strftime("%A %H:%M %d-%m-%y"), ' => ', start.strftime("%A %H:%M %d-%m-%y"))


        event = Event()
        event.add('summary', "{}: {}".format(module, row["Type"]))
        event.add('description', "{} {}".format(module, row["Type"]))
        event.add('location', "{}".format(row['Room & Capacity']))
        event.add('dtstart', start)
        event.add('dtend', start + dt.timedelta(minutes=length_mins))
        event['uid'] = '{}/{}@ucd.ie'.format(start.isoformat(), i)
        event.add('priority', 5)

        cal.add_component(event)

    output_file = '{}.ics'.format(module)
    logging.info("writing to %s", output_file)
    f = open(output_file, 'wb')
    f.write(cal.to_ical())
    f.close()


def main():
    parser = OptionParser()
    parser.add_option("--module", dest="module", default="COMPXXXXX", type=str)
    parser.add_option("--input", dest="input", default=None, type=str)

    (options, args) = parser.parse_args()

    tt_to_ical(options)
    return


if __name__ == '__main__':
    main()
