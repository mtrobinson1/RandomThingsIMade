import re
from datetime import datetime
import pytz

# Define the current and desired date/time formats
current_format = '%Y-%m-%d %I:%M%p'  # Example: 2023-05-08 06:13pm
desired_format = '%B %d, %Y at %I:%M:%S %p %Z'  # Example: May 8, 2023 at 06:13:00 PM EST

# Regular expression to match the date/time in current format
date_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}[ap]m')

def reformat_date(match):
    date_str = match.group(0)
    datetime_obj = datetime.strptime(date_str, current_format)
    est_timezone = pytz.timezone('EST')
    datetime_obj_est = datetime_obj.replace(tzinfo=pytz.utc).astimezone(est_timezone)
    return datetime_obj_est.strftime(desired_format)

# Read the journal file
with open('journal.txt', 'r', encoding='utf-8') as file:
    journal_content = file.read()

# Replace all date/time strings with the new format
updated_journal_content = date_pattern.sub(reformat_date, journal_content)

# Save the updated content back to a new file
with open('updated_journal.txt', 'w', encoding='utf-8') as file:
    file.write(updated_journal_content)

