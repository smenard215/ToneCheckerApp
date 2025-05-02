from django.shortcuts import render
from textblob import TextBlob

def analyze_text(request):
    sentiment = None
    message = ""
    if request.method == "POST":
        message = request.POST.get("message", "")
        if message:  
            blob = TextBlob(message)
            polarity = blob.sentiment.polarity

            if polarity > 0.1:
                sentiment = "Positive 😊"
            elif polarity < -0.1:
                sentiment = "Negative 😬"
            else:
                sentiment = "Neutral 😐"
    
    return render(request, "analyzer/home.html", {
        "sentiment": sentiment,
        "message": message
    })