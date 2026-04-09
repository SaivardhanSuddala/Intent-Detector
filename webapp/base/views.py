from django.shortcuts import render
from django.http import HttpResponse
import pickle,os
from django.conf import settings


model_path = os.path.join(settings.BASE_DIR, "model.pkl")
vect_path = os.path.join(settings.BASE_DIR, "vect.pkl")



model=pickle.load(open(model_path,'rb'))
vect=pickle.load(open(vect_path,'rb'))

def home(request):
    result=0
    if request.method=="POST":
        text=request.POST.get("text")
        if text:
            vect_t=vect.transform([text])
            result=model.predict(vect_t)[0]
    return render(request,"index.html",{"result":result})