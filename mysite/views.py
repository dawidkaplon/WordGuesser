from django.shortcuts import render, redirect
from copy import deepcopy

# Create your views here.


def index(request):
    return render(request, "index.html")


class Game:
    reset_flag = True
    active_rows = 1  # Current row user is already guessing (from 1-5)

    def gameplay(request):
        global letters

        try:
            word = request.session["word"]
            word_length = [str(num + 1) for num in range(len(word["word"]))]
            if Game.reset_flag:
                Game.active_rows = 1
                letters = {}
                for row in "12345":
                    for index in word_length:
                        # If user didnt guess any letter yet, input values should be an empty strings
                        letters[f"row{row}col{index}"] = ""

            if "word" in request.session:
                # del request.session["word"]
                pass

            if request.method == "POST":
                Game.reset_flag = False  # Avoid clearing the letters dict if user already make a guess
                if "" in request.POST.values():
                    pass
                else:
                    Game.active_rows += 1
                    for key, value in request.POST.items():
                        letters[key] = value.upper()
                    for key, value in letters.items():
                        print(key, value)
                    
                    """
                     todo: make validating the letters system: 
                     check if user's letter is present in current word;
                     if it is, check if letter is at valid position. 
                     If yes, make input field green, if no, make it orange
                     If letter is not present in the word, leave the input box grey.
                     Imo it should be done by comparing last values added 
                     to the dictionary (by column indexes) with actual letters in the word
                    """

            return render(
                request,
                "game.html",
                {
                    "word": word,
                    "word_length": word_length,
                    "letters": letters,
                    "active_rows": Game.active_rows,
                },
            )

        except KeyError:
            return redirect("/404/")


def error404(request):
    return render(request, "error404.html")
