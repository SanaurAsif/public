import json
import sys

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = 'add.json'
except Exception as e:
    print(f"Error: {e}")
    print("Usage: python cat.py [file_name]")
    sys.exit()

json_obj = json.load(open(file_name, 'r'))

for num, account in enumerate(json_obj['accounts']):
    print(f" [{num + 1}] {account['name']} - {account['username']} - {account['tg_id']} - {account['number']}")
