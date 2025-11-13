from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about_uos(request):
    return HttpResponse("""
        <h1>About Me</h1>
        <p>My name is <strong>Awais</strong>.</p>
        <p>I am a student at the University of Suffolk (UoS).</p>

        <h2>My Experience at UoS</h2>
        <p>
            I have really enjoyed my time at UoS. The faculty and staff 
            have been very supportive, and I've had the opportunity to 
            learn a lot in my courses. Especially, I appreciate the 
            practical approach to learning that UoS emphasizes through 
            projects and group work.
        </p>
    """)