import datetime
import argparse

EVENT_FILE = 'events.txt'

def get_today():
    return datetime.datetime.now().strftime("%d-%m")

def check_reminders(file_path):
    today = get_today()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            found = False
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    name, date = parts
                    if date == today:
                        print(f"🔔 Reminder: {name} is today!")
                        found = True
            if not found:
                print("📭 No reminders for today.")
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"💥 Unexpected error: {e}")

def add_event(file_path, name, date):
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"{name},{date}\n")
        print(f"✅ Added event: {name} on {date}")
    except Exception as e:
        print(f"💥 Could not add event: {e}")

# 🌐 CLI Interface
parser = argparse.ArgumentParser(description="CLI Reminder Tool")
parser.add_argument('--add', nargs=2, metavar=('EVENT', 'DATE'), help='Add new event: Name Date(dd-mm)')
parser.add_argument('--check', action='store_true', help='Check today\'s reminders')

args = parser.parse_args()

if args.add:
    add_event(EVENT_FILE, args.add[0], args.add[1])
elif args.check:
    check_reminders(EVENT_FILE)
else:
    print("📌 Use '--add \"Event Name\" dd-mm' to add or '--check' to check today's reminders.")