from diary.models import Entry

def purge():
    entries = Entry.objects.filter(essential=False)
    for e in entries:
        e.delete()
    return ("Successfully deleted " + str(len(entries)) + " entries.")
