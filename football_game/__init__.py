from flask.globals import request, session
from flask.json import jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import or_
import csv



app = Flask(__name__) 

app.config['SECRET_KEY'] = "gameservice"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/football_game_db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
app.config['JSON_SORT_KEYS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)

from football_game.models.model import Team,Tournament,UpMarch,FinishedMarch

@app.route('/upcomming',methods=['POST'])
def upcomming():
    csv_data = csv.reader(open('football_game/result_played.csv'))
    teams = Team.query.all()
    datas = []
    no_duplicate = []
    for row in csv_data:
        datas.append(row[0])
    
    # remove duplicate team 
    for data in datas:
        if data not in no_duplicate:
            team = Team(data)
            db.session.add(team)
            db.session.commit()
            no_duplicate.append(data)
            print(no_duplicate)

    return jsonify({'data':len(no_duplicate)})



# get list of matches by team
@app.route('/matches/team/<int:id>')
def matches(id):
    team = Team.query.get(id)
    team_name = team.name
    matches = []


    finished_matches = FinishedMarch.query.filter(or_(FinishedMarch.home_team==team_name,FinishedMarch.away_team==team_name)).all()
    for finished_match in finished_matches:
        fin_dict = {}
        fin_dict['home_team']= finished_match .home_team
        fin_dict['home_score']= finished_match .home_score
        fin_dict['away_team']= finished_match .away_team
        fin_dict['away_score']= finished_match .away_score
        fin_dict['tournament']= finished_match.tournament
        fin_dict['start_time']= finished_match .start_time
        fin_dict['status']= finished_match .status
        matches.append(fin_dict)

    up_matches = UpMarch.query.filter(or_(UpMarch.home_team==team_name,UpMarch.away_team==team_name)).all()
    for up_match in up_matches:
         dict_match = {} 
         dict_match['home_team']= up_match.home_team
         dict_match['away_team']= up_match.away_team
         dict_match['tournament']= up_match.tournament
         dict_match['start_time']= up_match.start_time
         dict_match['kickoff']= up_match.kickoff
         dict_match['status']= up_match.status
         matches.append(dict_match)
    
    
    return jsonify(matches)
# get list of matches by team filter by status
@app.route('/matches/team_by_status/<int:id>')
def team_by_status(id):
    if not 'status' in request.args:
        return jsonify({'result':'Invalid Parameter'})
    team = Team.query.get(id)
    team_name = team.name
    status = request.args.get("status")
    matches = []

    if status == 'finished':
        finished_matches = FinishedMarch.query.filter(or_(FinishedMarch.home_team==team_name,FinishedMarch.away_team==team_name)).all()
        for finished_match in finished_matches:
            fin_dict = {}
            fin_dict['home_team']= finished_match.home_team
            fin_dict['home_score']= finished_match.home_score
            fin_dict['away_team']= finished_match.away_team
            fin_dict['away_score']= finished_match.away_score
            fin_dict['tournament']= finished_match.tournament
            fin_dict['start_time']= finished_match.start_time
            fin_dict['status']= finished_match.status
            matches.append(fin_dict)
        return jsonify(matches)
    
    up_matches = UpMarch.query.filter(or_(UpMarch.home_team==team_name,UpMarch.away_team==team_name)).all()
    for up_match in up_matches:
         dict_match = {} 
         dict_match['home_team']= up_match.home_team
         dict_match['away_team']= up_match.away_team
         dict_match['tournament']= up_match.tournament
         dict_match['start_time']= up_match.start_time
         dict_match['kickoff']= up_match.kickoff
         dict_match['status']= up_match.status
         matches.append(dict_match)
    return jsonify(matches)


# get list of matches by tournament

@app.route('/matches/tournament/<int:id>')
def matches_tournamet(id):
    tournament = Tournament.query.get(id)
    name = tournament.name
    matches = []


    finished_matches = FinishedMarch.query.filter(FinishedMarch.tournament==name).all()
    for finished_match in finished_matches:
        fin_dict = {}
        fin_dict['home_team']= finished_match .home_team
        fin_dict['home_score']= finished_match .home_score
        fin_dict['away_team']= finished_match .away_team
        fin_dict['away_score']= finished_match .away_score
        fin_dict['tournament']= finished_match.tournament
        fin_dict['start_time']= finished_match .start_time
        fin_dict['status']= finished_match .status
        matches.append(fin_dict)

    
    up_matches = UpMarch.query.filter(UpMarch.tournament==name).all()
    for up_match in up_matches:
         dict_match = {} 
         dict_match['home_team']= up_match.home_team
         dict_match['away_team']= up_match.away_team
         dict_match['tournament']= up_match.tournament
         dict_match['start_time']= up_match.start_time
         dict_match['kickoff']= up_match.kickoff
         dict_match['status']= up_match.status
         matches.append(dict_match)

    return jsonify(matches)


# get matches by tournament filter by status

@app.route('/matches/tournament_by_status/<int:id>')
def team_by_tournament(id):
    if not 'status' in request.args:
        return jsonify({'result':'Invalid Parameter'})
    tournament = Tournament.query.get(id)
    name = tournament.name
    status = request.args.get("status")
    matches = []

    if status == 'finished':
        finished_matches = FinishedMarch.query.filter(FinishedMarch.tournament==name).all()
        for finished_match in finished_matches:
            fin_dict = {}
            fin_dict['home_team']= finished_match.home_team
            fin_dict['home_score']= finished_match.home_score
            fin_dict['away_team']= finished_match.away_team
            fin_dict['away_score']= finished_match.away_score
            fin_dict['tournament']= finished_match.tournament
            fin_dict['start_time']= finished_match.start_time
            fin_dict['status']= finished_match.status
            matches.append(fin_dict)
        return jsonify(matches)
    
    up_matches = UpMarch.query.filter(FinishedMarch.tournament==name).all()
    for up_match in up_matches:
         dict_match = {} 
         dict_match['home_team']= up_match.home_team
         dict_match['away_team']= up_match.away_team
         dict_match['tournament']= up_match.tournament
         dict_match['start_time']= up_match.start_time
         dict_match['kickoff']= up_match.kickoff
         dict_match['status']= up_match.status
         matches.append(dict_match)
    return jsonify(matches)







