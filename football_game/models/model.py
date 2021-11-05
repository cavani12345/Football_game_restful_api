from football_game import db

# this is model for team
class Team(db.Model):
    __tablename__="teams"

    id = db.Column(db.Integer, primary_key=True,unique=True)
    name = db.Column(db.String(50),nullable=False)

    def __init__(self,name):
        self.name = name

# this is model for tournament

class Tournament(db.Model):
    __tablename__="tournaments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)

    # create relationship
    #upcommings = db.relationship('UpMarch', backref='tournaments', lazy='dynamic')
    #finished = db.relationship('FinishedMarch', backref='tournaments', lazy='dynamic')

    def __init__(self,name):
        self.name = name

# this is upcoming match model

class UpMarch(db.Model):
    __tablename__='upcomming_matches'
    
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String(100),nullable=False)
    away_team = db.Column(db.String(100),nullable=False)
    tournament = db.Column(db.String(100),nullable=False)
    start_time = db.Column(db.String(100),nullable=False)
    kickoff = db.Column(db.String(100),nullable=False)
    status = db.Column(db.String(50),nullable=False)

    def __init__(self,home_team,away_team,tournament,start_time,kickoff):
        self.home_team = home_team
        self. away_team = away_team
        self.tournament = tournament
        self.start_time  = start_time
        self.kickoff = kickoff
        self.status = 'upcoming'

    
# this is finished match model 

class FinishedMarch(db.Model):
    __tablename__='finished_matches'
    
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String(100),nullable=False)
    home_score = db.Column(db.Integer,nullable=False)
    away_team = db.Column(db.String(100),nullable=False)
    away_score = db.Column(db.Integer,nullable=False)
    tournament = db.Column(db.String(100),nullable=False)
    start_time = db.Column(db.String(100),nullable=False)
    status = db.Column(db.String(50),nullable=False)


    def __init__(self,home_team,home_score,away_team,away_score,tournament,start_time):
        self.home_team = home_team
        self.home_score = home_score
        self.away_score = away_score
        self. away_team = away_team
        self.tournament = tournament
        self.start_time  = start_time
        self.status = 'Finished'



