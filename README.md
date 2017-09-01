# Convert your Timetable to iCal

Infohub provides this

![](timetable.png)

with no way to convert to a sensible calendar format.

To convert it iCal

- install the module:
    - `pip install https:// `
- download the timetable CSV file from Infohub
- and run:
    - `timetable_to_ical --module=COMP20010 --input=CM801-5.csv`
- You need to tell it the module name, because it is not encoded in the CSV file.

This will output a file `COMP20010.ics` in the current directory, which you can easily import to iCal:

![](ical.png)

# Suggestions

Any suggestions to modify or improve it are welcome. The script is pretty simple, and it is easy to add other information into the event.
