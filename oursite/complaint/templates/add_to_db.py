from .models import *
from .forms import *

def createComplaint(data):
    complaint.create(data)

def createProgress(data):
    progress.created(data)

