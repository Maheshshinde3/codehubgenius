from django.shortcuts import render
import random
from app.models import Question,Option
# Create your views here.




from django.http import HttpResponse

def showfile(request):
    return render(request,"index.html")





def Quiz(request):

# Fetch random ids of questions
    if 'quiz_questions' in request.session:
        random_ids = request.session['quiz_questions']
    
    else:
        QUESTION_COUNT = 7
        all_ids = list(Question.objects.values_list('id', flat=True))
    
        if len(all_ids) < QUESTION_COUNT:
            QUESTION_COUNT = len(all_ids)

        random_ids = random.sample(all_ids, QUESTION_COUNT)
        request.session['quiz_questions'] = random_ids


    # # Fetch questions + options efficiently
    questions = (
        Question.objects
        .filter(id__in=random_ids)
        .prefetch_related('Option')
    )
   
    
    score = 0
    total = questions.count()
    result = None
    correct_answers = {}

    # Checked weather the selected options are correct or not 
    if request.method == 'POST':
        for question in questions:

            #get selected options
            selected_option_id = request.POST.get(f"question_{question.id}")

            if selected_option_id:
                try:
                    #if selected options are correct increase score
                    optionvalue = Option.objects.get(id=selected_option_id, question=question)
                    if optionvalue.is_correct:
                        score += 1
                except:
                    Option.DoesNotExist
            
            #get all Truly correct options
            correct_option = Option.objects.filter(
                question = question,
                is_correct = True
                ).first()

            # Get just user selected correct answers. to show user which options he selected correctly.
            question.correct_answer = (
            correct_option.text if correct_option else None
            )

        #Stored result in dictionary
        result = {
            "score": score, #Stored score of user
            "total": total  #Stored total no. of questions or score
        }

        # clear quiz after submission
        request.session.pop('quiz_questions', None)          

    return render(request, "QuizZone.html", {
        "questions": questions,
        "result": result,
    })
    # return render(request, "QuizZone.html", {"questions": questions})
    
   