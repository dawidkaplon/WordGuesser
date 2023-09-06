from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "index.html")


def game(request):
    try:
        word = request.session["word"]
        word_length = [str(num + 1) for num in range(len(word['word']))]
        letters = {}
        
        if len(letters.keys()) == 0:
            for num in '12345':
                for index in word_length:
                    # If user didnt guess any letter yet, input values should be empty
                    letters[f'row{num}_col{index}'] = ''   
        
        if "word" in request.session:
            # del request.session["word"]
            pass
        
        if request.method == 'POST':
            if '' in request.POST.values():
                pass
            else:
                for key, value in request.POST.items():
                    letters[key] = value.upper()
                for key, value in letters.items():
                    print(key, value)


        return render(request, "game.html", {"word": word, 'word_length': word_length, 'letters': letters})

    except KeyError:
        return redirect("/404/")


def error404(request):
    return render(request, "error404.html")
