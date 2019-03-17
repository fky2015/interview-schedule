#!/bin/bash
cat add_dummy_data.py | tr '\n' ';' | sed 's/^/"&/g' | sed 's/$/&"/g' | xargs python manage.py shell -c

