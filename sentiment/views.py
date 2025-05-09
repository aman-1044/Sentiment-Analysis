# views.py
from django.shortcuts import render
from .predictor import predict_sentiment  # Import the function from predictor.py

def result(request):
    if request.method == 'POST':
        # Get text input from the form (from 'home.html' or another HTML page)
        text = request.POST['text']  # Assuming there's a form with an input field named 'text'
        
        # Call the prediction function
        prediction = predict_sentiment(text)
        
        # Render the result in a template (e.g., result.html)
        return render(request, 'sentiment/result.html', {'text': text, 'prediction': prediction})

    return render(request, 'sentiment/home.html')  # If not POST, show the home page

