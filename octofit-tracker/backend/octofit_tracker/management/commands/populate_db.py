from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Creating users...')
        tony = User.objects.create(email='tony@stark.com', username='IronMan', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', username='Batman', team=dc)
        clark = User.objects.create(email='clark@kent.com', username='Superman', team=dc)

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=steve, type='swim', duration=45, date=timezone.now())
        Activity.objects.create(user=bruce, type='cycle', duration=60, date=timezone.now())
        Activity.objects.create(user=clark, type='run', duration=50, date=timezone.now())

        self.stdout.write('Creating workouts...')
        Workout.objects.create(name='Pushups', description='Do 3 sets of 15 pushups', suggested_for='all')
        Workout.objects.create(name='Plank', description='Hold plank for 1 minute', suggested_for='core')

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
