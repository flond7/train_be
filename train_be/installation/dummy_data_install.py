from api.models import Railway, Video, Question, User

r = Railway(name='Venezia - Trieste', description='Tratta da Venezia a Trieste')
r.save()
r = Railway(name='Tarvisio - Roma', description='Tratta da Tarvisio a Roma')
r.save()

v = Video(name='Video 1', url='xxxx', description='Descrizione primo video', duration= 1500, railway=1)
v.save()
v = Video(name='Video 2', url='xxxx', description='Descrizione secondo video', duration= 1500, railway=1)
v.save()

q = Question(text='Question 1 text', answerOne='1', answerTwo='2', answerThree='3', correct='2', video=1)
q.save()
q = Question(text='Question 2 text', answerOne='1', answerTwo='2', answerThree='3', correct='1', video=1)
q.save()
q = Question(text='Question 3 text', answerOne='1', answerTwo='2', answerThree='3', correct='3', video=1)
q.save()