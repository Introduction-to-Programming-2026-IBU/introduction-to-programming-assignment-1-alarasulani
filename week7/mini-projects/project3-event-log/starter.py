# starter.py — Event Log Reporter
# Project 3 | Intermediate | 35–45 minutes
#
# Run from this folder:
#   python starter.py

import csv

# ── Step 1: Data structures ───────────────────────────────────────────────────
room_counts   = {}
type_counts   = {}
day_attendees = {}
all_events    = []

# ── Step 2: Single pass through CSV ───────────────────────────────────────────
with open("bookings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        room       = row["room"]
        event_type = row["event_type"]
        date       = row["date"]
        attendees  = int(row["attendees"])

        # Room counts
        room_counts[room] = room_counts.get(room, 0) + 1

        # Event type counts
        type_counts[event_type] = type_counts.get(event_type, 0) + 1

        # Day totals (sum of attendees)
        day_attendees[date] = day_attendees.get(date, 0) + attendees

        # Store full row for later filtering
        all_events.append(row)

# ── Step 3: Find busiest day ─────────────────────────────────────────────────
busiest_day = max(day_attendees, key=day_attendees.get)
busiest_count = day_attendees[busiest_day]

# ── Step 4: Filter + sort large events ────────────────────────────────────────
large_events = [row for row in all_events if int(row["attendees"]) > 50]

large_events_sorted = sorted(
    large_events,
    key=lambda row: int(row["attendees"]),
    reverse=True
)

# ── Step 5: Print report ──────────────────────────────────────────────────────
print("=== Community Centre Booking Report ===")

print("\nBookings by Room:")
for room in sorted(room_counts):
    print(f"  {room:<7}: {room_counts[room]} events")

print("\nBookings by Event Type:")
for etype in sorted(type_counts):
    print(f"  {etype:<8}: {type_counts[etype]} events")

print(f"\nBusiest Day: {busiest_day}  ({busiest_count} total attendees)")

print("\nLarge Events (> 50 attendees):")
for event in large_events_sorted:
    print(f"  {event['date']} | {event['room']:<6} | {event['event_type']:<8} | {int(event['attendees']):>3} attendees")