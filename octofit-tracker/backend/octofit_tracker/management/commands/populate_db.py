from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True),
            User(email='cap@marvel.com', name='Captain America', team='Marvel', is_superhero=True),
            User(email='thor@marvel.com', name='Thor', team='Marvel', is_superhero=True),
            User(email='hulk@marvel.com', name='Hulk', team='Marvel', is_superhero=True),
            User(email='superman@dc.com', name='Superman', team='DC', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='DC', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True),
            User(email='flash@dc.com', name='Flash', team='DC', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', type='Running', duration=30, date='2025-10-30'),
            Activity(user='Superman', type='Flying', duration=60, date='2025-10-30'),
            Activity(user='Batman', type='Martial Arts', duration=45, date='2025-10-30'),
            Activity(user='Hulk', type='Weightlifting', duration=50, date='2025-10-30'),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Workouts
        workouts = [
            Workout(name='Super Strength', description='Lift heavy objects', difficulty='Hard'),
            Workout(name='Speed Run', description='Run at super speed', difficulty='Medium'),
            Workout(name='Flight Training', description='Practice flying', difficulty='Medium'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
