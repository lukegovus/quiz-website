import random as rd 

 '''
 -Some potential data structures to hold questions. All rough. Code probably has errors!
 -Use pandas etc to read in values and load them into data struct.
 -Need to generate more question dicts on the fly. '''
questions =[
    {
        "meta" : {"category" :"category1",
                    "id": 0},
        "question-text": "Lorem ipsum",
        'ans-correct': {"value": "test-value",
                        "guesses": 0},
        'ans-incorrect-1':{"value": "wrong ans", 
                            "guesses": 0},
        'ans-incorrect-2': {"value": "wrong ans2",
                             "guesses": 0},
        'ans-incorect-3': {"value": "wrong ans3",
                            "guesses" : 0}
    }