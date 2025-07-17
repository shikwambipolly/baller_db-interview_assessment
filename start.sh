#!/bin/sh

# Wait for MongoDB to be ready using Python
echo "Waiting for MongoDB..."
python -c "
import socket, time
while True:
    try:
        s = socket.create_connection(('mongodb', 27017), timeout=2)
        s.close()
        break
    except Exception:
        time.sleep(1)
"
echo "MongoDB is up."

# Only seed if not already done
if [ ! -f "/data/.seeded" ]; then
  echo "Seeding the database..."
  python seed.py && touch /data/.seeded
else
  echo "Database already seeded."
fi

# Run seed and then the app
exec uvicorn main:app --host 0.0.0.0 --port 8000