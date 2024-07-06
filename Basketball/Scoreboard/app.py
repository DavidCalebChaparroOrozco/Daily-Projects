from flask import Flask, render_template, request, redirect, url_for, jsonify
from threading import Timer

app = Flask(__name__)

# Initialization of global variables
data = {
    "home_team": None,
    "away_team": None,
    "home_score": 0,
    "away_score": 0,
    "home_fouls": 0,
    "away_fouls": 0,
    "quarter": 1,
    "time_remaining": 1 * 60,  # time in seconds
    "halftime": False,
    "overtime": 0,
    "winner": None,
    "game_started": False,
    "halftime_duration": 1.5 * 60  # 15 minutes for halftime
}

# Function to reset the game data
def reset_game():
    global data
    data.update({
        "home_team": None,
        "away_team": None,
        "home_score": 0,
        "away_score": 0,
        "home_fouls": 0,
        "away_fouls": 0,
        "quarter": 1,
        "time_remaining": 1 * 60,  # time in seconds
        "halftime": False,
        "overtime": 0,
        "winner": None,
        "game_started": False,
        "halftime_duration": 1.5 * 60  # 15 minutes for halftime
    })

# Function to update the game time
def update_time():
    global data
    if not data['game_started']:
        Timer(1, update_time).start()
        return

    if data['halftime']:
        if data['halftime_duration'] > 0:
            data['halftime_duration'] -= 1
        else:
            data['halftime'] = False
            data['quarter'] += 1
            data['time_remaining'] = 1 * 60  # Reset quarter time
    elif data['time_remaining'] > 0:
        data['time_remaining'] -= 1
    elif data['quarter'] == 2:
        data['halftime'] = True
        data['halftime_duration'] = 1.5 * 60  # Reset halftime duration
    elif data['quarter'] < 4:
        data['quarter'] += 1
        data['time_remaining'] = 1 * 60  # Reset quarter time
    elif data['home_score'] == data['away_score']:
        data['overtime'] += 1
        data['time_remaining'] = 0.5 * 60  # Overtime period
    else:
        if data['home_score'] > data['away_score']:
            data['winner'] = data['home_team']
        else:
            data['winner'] = data['away_team']
    Timer(1, update_time).start()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        home_team = request.form.get('home_team')
        away_team = request.form.get('away_team')
        if home_team and away_team:
            data['home_team'] = home_team
            data['away_team'] = away_team
            data['game_started'] = True
            return redirect(url_for('scoreboard'))
    return render_template('index.html')

@app.route('/scoreboard', methods=['GET', 'POST'])
def scoreboard():
    global data
    if request.method == 'POST':
        if 'reset' in request.form:
            reset_game()
            return redirect(url_for('index'))
        elif 'add_score' in request.form:
            if not data['halftime'] and not data['winner']:
                team = request.form['team']
                points = int(request.form['points'])
                data[f"{team}_score"] += points
        elif 'add_foul' in request.form:
            if not data['halftime'] and not data['winner']:
                team = request.form['team']
                data[f"{team}_fouls"] += 1
        elif 'back_to_index' in request.form:
            return redirect(url_for('index'))

        # Determine winner
        if data['quarter'] > 4 and data['home_score'] != data['away_score']:
            data['winner'] = data['home_team'] if data['home_score'] > data['away_score'] else data['away_team']
        
    return render_template('scoreboard.html', data=data)

@app.route('/get_time')
def get_time():
    global data
    return jsonify(
        time_remaining=data['time_remaining'], 
        quarter=data['quarter'], 
        overtime=data['overtime'], 
        winner=data['winner'], 
        halftime=data['halftime'], 
        halftime_duration=data['halftime_duration']
    )

if __name__ == '__main__':
    Timer(1, update_time).start()  # Start the time update
    app.run(debug=True)
