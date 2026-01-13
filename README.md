# Meet ***JULIUS***, your personal AI task assistant!

JULIUS is your personal task and event assistant that helps you manage your weekly schedule. This project includes both a command-line interface and a web-based interface with a Flask backend.

## Features

- 📅 Add events with day of week, time, and priority levels
- 🗑️ Remove events from your schedule
- 👀 View your weekly schedule organized by day
- ⚡ Priority levels (High, Medium, Low) with color coding
- 🌐 Beautiful web interface
- 💻 Command-line interface option

## Files Included

- `julius-task-tracker.py` - Original command-line interface
- `julius_api.py` - Flask backend API server
- `index.html` - Web-based user interface

## Prerequisites

Before you begin, make sure you have Python installed on your computer:

- **Python 3.6 or higher** is required
- Check if Python is installed by opening your terminal and typing:
  ```bash
  python3 --version
  ```
  
If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

## Installation & Setup

Follow these steps to run JULIUS locally on your computer:

### Step 1: Download the Project

1. Click the green **"Code"** button on GitHub
2. Select **"Download ZIP"**
3. Extract the ZIP file to a folder on your computer

Alternatively, if you have Git installed:
```bash
git clone https://github.com/YOUR-USERNAME/julius-task-tracker.git
cd julius-task-tracker
```

### Step 2: Install Dependencies

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and navigate to the project folder:

```bash
cd path/to/julius-task-tracker
```

Install the required Python packages:

```bash
pip3 install flask flask-cors
```

**Note:** If `pip3` doesn't work, try `pip` or `python3 -m pip install flask flask-cors`

### Step 3: Start the Backend Server

Run the Flask backend:

```bash
python3 julius_api.py
```

You should see output like:
```
JULIUS Flask API Server Starting...
API will be available at: http://localhost:8080
 * Running on http://127.0.0.1:8080
 * Debugger is active!
```

**Important:** Keep this terminal window open! The server needs to stay running.

### Step 4: Open the Web Interface

1. Find the `index.html` file in your project folder
2. Double-click it to open in your web browser
3. The JULIUS web interface should now appear!

### Step 5: Start Using ***JULIUS***

The web interface has three main sections:

1. **Add Event** - Create new events with:
   - Event title
   - Day of week (Monday - Sunday)
   - Time (e.g., "2:00 PM" or "14:00")
   - Priority (High, Medium, Low)

2. **View Schedule** - See all your events organized by day of the week with color-coded priorities

3. **Help** - View available commands and features

## Troubleshooting

### "Python command not found"
- Try `python3` instead of `python`
- On Windows, try `py` instead

### "Port already in use" or Backend Not Connecting
If you see errors about port 5000 or 8080 being in use:

1. Open `julius_api.py`
2. Find the last line: `app.run(debug=True, port=8080, host='127.0.0.1')`
3. Change `8080` to a different number like `3000` or `5001`
4. Restart the server
5. In the web interface, update the "Python Backend URL" field to match the new port (e.g., `http://localhost:3000`)

### Backend URL Configuration
Make sure the "Python Backend URL" field at the top of the web page matches where your Flask server is running (default: `http://localhost:8080`)

### CORS Errors
If you see CORS errors in the browser console, make sure:
- Flask and flask-cors are properly installed
- The backend server is running
- You're opening `index.html` directly (not through a web server)

## Command-Line Version

If you prefer the original command-line interface:

```bash
python3 julius-task-tracker.py
```

Follow the on-screen prompts to manage your events.

## Technology Stack

- **Backend:** Python, Flask, Flask-CORS
- **Frontend:** HTML, CSS, JavaScript
- **Storage:** In-memory (events persist while server is running)

## Future Enhancements

Potential features for future development:
- Persistent storage (database or file-based)
- Export schedule to calendar formats
- Recurring events
- Notifications and reminders
- Multiple week support

## Support

If you encounter any issues:
1. Make sure Python 3 is installed
2. Verify all dependencies are installed (`pip3 install flask flask-cors`)
3. Check that the Flask server is running (terminal should show "Running on...")
4. Check browser console for error messages (Right-click → Inspect → Console)

## License

This project is open source and available for personal and educational use.

---

**Enjoy using JULIUS! Have a blessed day! 🎉**
