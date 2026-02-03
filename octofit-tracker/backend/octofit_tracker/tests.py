from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Alpha')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'Alpha')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Alpha', members=["test@example.com"])
        self.assertEqual(team.name, 'Alpha')
        self.assertIn("test@example.com", team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@example.com', activity='Run', duration=30)
        self.assertEqual(activity.activity, 'Run')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Alpha', points=100)
        self.assertEqual(leaderboard.team, 'Alpha')
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user_email='test@example.com', workout='Pushups', suggestion='Do 20 reps')
        self.assertEqual(workout.workout, 'Pushups')
        self.assertEqual(workout.suggestion, 'Do 20 reps')
