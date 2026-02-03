from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(host='localhost', port=27017)
        db = client['octofit_db']

        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Create unique index on email for users
        db.users.create_index('email', unique=True)

        # Sample users (superheroes)
        users = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'name': 'Steve Rogers', 'email': 'cap@marvel.com', 'team': 'marvel'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'dc'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'dc'},
        ]
        db.users.insert_many(users)

        # Teams
        teams = [
            {'name': 'marvel', 'members': ['ironman@marvel.com', 'cap@marvel.com']},
            {'name': 'dc', 'members': ['batman@dc.com', 'superman@dc.com']},
        ]
        db.teams.insert_many(teams)

        # Activities
        activities = [
            {'user_email': 'ironman@marvel.com', 'activity': 'Running', 'duration': 30},
            {'user_email': 'cap@marvel.com', 'activity': 'Cycling', 'duration': 45},
            {'user_email': 'batman@dc.com', 'activity': 'Swimming', 'duration': 25},
            {'user_email': 'superman@dc.com', 'activity': 'Flying', 'duration': 60},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'team': 'marvel', 'points': 75},
            {'team': 'dc', 'points': 85},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user_email': 'ironman@marvel.com', 'workout': 'Chest Day', 'suggestion': 'Bench Press'},
            {'user_email': 'cap@marvel.com', 'workout': 'Leg Day', 'suggestion': 'Squats'},
            {'user_email': 'batman@dc.com', 'workout': 'Cardio', 'suggestion': 'Treadmill'},
            {'user_email': 'superman@dc.com', 'workout': 'Full Body', 'suggestion': 'Deadlift'},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
