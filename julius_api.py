from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for GitHub Pages to connect

event_list = []
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def time_key(event):
    time_str = event["time"]
    formats = ["%I:%M %p", "%H:%M", "%I %p", "%H"]
    for fmt in formats:
        try:
            return datetime.strptime(time_str, fmt).time()
        except ValueError:
            continue
    return datetime.strptime("12:00", "%H:%M").time()

@app.route('/api/events', methods=['GET'])
def get_events():
    """View all events organized by day"""
    # Organize events by day of week
    schedule = {}
    for day in DAYS_OF_WEEK:
        events_this_day = [e for e in event_list if e["day"] == day]
        events_this_day.sort(key=time_key)
        schedule[day] = events_this_day
    
    return jsonify({
        'events': event_list,
        'schedule': schedule,
        'days_of_week': DAYS_OF_WEEK
    })

@app.route('/api/events', methods=['POST'])
def add_event():
    """Add a new event"""
    data = request.json
    
    # Validate day
    day = data.get('day', '').capitalize()
    if day not in DAYS_OF_WEEK:
        return jsonify({'error': 'Invalid day of the week'}), 400
    
    # Validate required fields
    title = data.get('title', '').strip()
    time = data.get('time', '').strip()
    
    if not title:
        return jsonify({'error': 'Title cannot be empty'}), 400
    if not time:
        return jsonify({'error': 'Time cannot be empty'}), 400
    
    # Handle priority
    priority = data.get('priority', 'medium').lower()
    if priority not in ['high', 'medium', 'low']:
        priority = 'medium'
    
    event = {
        'id': len(event_list) + 1,
        'title': title.title(),
        'day': day,
        'time': time,
        'priority': priority.capitalize()
    }
    
    event_list.append(event)
    return jsonify({
        'message': f"'{title}' added on {day} at {time} ({priority.capitalize()} priority)!",
        'event': event
    }), 201

@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def remove_event(event_id):
    """Remove an event by ID"""
    global event_list
    
    # Find event by ID
    event_to_remove = None
    for i, event in enumerate(event_list):
        if event.get('id') == event_id:
            event_to_remove = event_list.pop(i)
            break
    
    if event_to_remove:
        return jsonify({
            'message': f"{event_to_remove['title']} has been removed from your schedule.",
            'event': event_to_remove
        })
    else:
        return jsonify({'error': 'Event not found'}), 404

@app.route('/api/help', methods=['GET'])
def get_help():
    """Get help information"""
    help_text = {
        'title': "JULIUS - Your Personal Task and Event Assistant",
        'commands': [
            {
                'name': 'Add Event',
                'description': 'Add a new event to your weekly schedule with title, day, time, and priority.'
            },
            {
                'name': 'Remove Event',
                'description': 'Remove an existing event from your schedule.'
            },
            {
                'name': 'View Schedule',
                'description': 'View all events scheduled for the week, organized by day.'
            },
            {
                'name': 'Help',
                'description': 'Display available commands and how to use JULIUS.'
            }
        ]
    }
    return jsonify(help_text)

if __name__ == '__main__':
    print("\nJULIUS Flask API Server Starting...")
    print("API will be available at: http://localhost:8080")
    print("\nEndpoints:")
    print("  GET    /api/events  - View all events")
    print("  POST   /api/events  - Add new event")
    print("  DELETE /api/events/<id> - Remove event")
    print("  GET    /api/help    - Get help information")
    print("\nMake sure to install dependencies: pip install flask flask-cors")
    app.run(debug=True, port=8080, host='127.0.0.1')