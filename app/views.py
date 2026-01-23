from django.shortcuts import render
import random
from app.models import Question,Option
# Create your views here.




from django.http import HttpResponse

def showfile(request):
    return render(request,"index.html")





def Quiz(request):


# Gettinng Questions and options from database
    QUESTION_COUNT = 7
    # Step 1: taken all id's list. first try with direct random.sample method but it gives only one number as output eg.55
    ids = list(Question.objects.values_list('id', flat=True))

    # for Safety check == if no. of question are less than question count ie.7 later fetch all question
    if len(ids) < QUESTION_COUNT:
        QUESTION_COUNT = len(ids)
      
    # Step 2: Pick random IDs
    random_ids = random.sample(ids, QUESTION_COUNT)

    # Step 3: Fetch questions + options efficiently
    questions = (
        Question.objects
        .filter(id__in=random_ids)
        .prefetch_related('Option')
    )
    



    
    # Send to template
    return render(request, "QuizZone.html", {"questions": questions})
   