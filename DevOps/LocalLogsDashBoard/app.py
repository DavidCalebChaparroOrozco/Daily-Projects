# Import necessary libraries
from flask import Flask, render_template, request
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import os
import time
from collections import defaultdict
import re

app = Flask(__name__)

# Configuration

# Default directory containing log files
LOG_DIRECTORY = './logs'  
# Supported log file extensions
ALLOWED_EXTENSIONS = {'.log', '.txt'}  
# Seconds between automatic refreshes
REFRESH_INTERVAL = 30  

# Sample log patterns to detect
LOG_PATTERNS = {
    'error': re.compile(r'error|exception|fail|critical', re.IGNORECASE),
    'warning': re.compile(r'warning', re.IGNORECASE),
    'info': re.compile(r'info|notice', re.IGNORECASE)
}

# Scan the log directory and return all valid log files
def get_log_files():
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)
        return []
    
    log_files = []
    for filename in os.listdir(LOG_DIRECTORY):
        filepath = os.path.join(LOG_DIRECTORY, filename)
        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            if ext.lower() in ALLOWED_EXTENSIONS:
                log_files.append({
                    'name': filename,
                    'path': filepath,
                    'size': os.path.getsize(filepath),
                    'modified': time.ctime(os.path.getmtime(filepath))
                })
    return sorted(log_files, key=lambda x: x['modified'], reverse=True)

# Analyze a log file and return statistics.
def analyze_log_file(filepath):
    """
    Returns: {
        'total_lines': int,
        'log_levels': dict,
        'last_lines': list,
        'timestamps': list (if detected)
    }
    """
    if not os.path.exists(filepath):
        return None
    
    stats = {
        'total_lines': 0,
        'log_levels': defaultdict(int),
        'last_lines': [],
        'timestamps': []
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # Read last 100 lines for display
            lines = f.readlines()
            stats['total_lines'] = len(lines)
            stats['last_lines'] = lines[-100:] if len(lines) > 100 else lines
            
            # Analyze log levels
            for line in lines:
                for level, pattern in LOG_PATTERNS.items():
                    if pattern.search(line):
                        stats['log_levels'][level] += 1
                
                # Simple timestamp extraction (can be improved)
                if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line):
                    stats['timestamps'].append(line[:50])  # Store beginning of line with timestamp
            
        return stats
    
    except Exception as e:
        print(f"Error reading log file {filepath}: {e}")
        return None

# Create a pie chart showing log level distribution
def create_log_level_chart(log_stats):
    if not log_stats or not log_stats['log_levels']:
        return None
    
    labels = list(log_stats['log_levels'].keys())
    values = list(log_stats['log_levels'].values())
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(
        title='Log Level Distribution',
        margin=dict(t=40, b=0, l=0, r=0)
    )
    return fig.to_html(full_html=False)

# Create a timeline chart if timestamps are detected
def create_timeline_chart(log_stats):
    if not log_stats or len(log_stats['timestamps']) < 3:
        return None
    
    # Simple timeline - counts per day (can be improved)
    date_counts = defaultdict(int)
    for line in log_stats['timestamps']:
        date_match = re.search(r'\d{4}-\d{2}-\d{2}', line)
        if date_match:
            date_counts[date_match.group()] += 1
    
    if not date_counts:
        return None
    
    dates = sorted(date_counts.keys())
    counts = [date_counts[date] for date in dates]
    
    fig = go.Figure(data=[go.Scatter(x=dates, y=counts, mode='lines+markers')])
    fig.update_layout(
        title='Log Entries Over Time',
        xaxis_title='Date',
        yaxis_title='Number of Entries',
        margin=dict(t=40, b=40, l=40, r=40)
    )
    return fig.to_html(full_html=False)

@app.route('/')
# Main dashboard page showing available log files
def index():
    log_files = get_log_files()
    return render_template('index.html', log_files=log_files, refresh_interval=REFRESH_INTERVAL)

@app.route('/view_log/<filename>')
# View details of a specific log file
def view_log(filename):
    filepath = os.path.join(LOG_DIRECTORY, filename)
    log_stats = analyze_log_file(filepath)
    
    if not log_stats:
        return render_template('error.html', message="Log file not found or could not be read.")
    
    # Generate visualizations
    level_chart = create_log_level_chart(log_stats)
    timeline_chart = create_timeline_chart(log_stats)
    
    return render_template(
        'log_view.html',
        filename=filename,
        log_stats=log_stats,
        level_chart=level_chart,
        timeline_chart=timeline_chart,
        refresh_interval=REFRESH_INTERVAL
    )

@app.route('/tail_log/<filename>')
# Return the last part of the log file (for AJAX updates)
def tail_log(filename):
    filepath = os.path.join(LOG_DIRECTORY, filename)
    log_stats = analyze_log_file(filepath)
    
    if not log_stats:
        return "Log file not found or could not be read.", 404
    
    return render_template('log_content.html', log_lines=log_stats['last_lines'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)