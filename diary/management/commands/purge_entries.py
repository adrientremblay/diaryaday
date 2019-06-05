from django.core.management.base import BaseCommand
from django_q.tasks import async_task

# Now this script or any imported module can use any part of Django it needs.


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        async_task('diary.tasks.purge', hook='hooks.print_result', task_name = "PURGE ENTRIES")
