from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "index.html")


class Game:
    reset_flag = True
    active_rows = 1  # Current row user is already guessing (1-5)
    box_colors = {}

    def gameplay(request):
        global letters

        try:
            word = request.session["word"]
            word_length = [str(num + 1) for num in range(len(word["word"]))]
            if Game.reset_flag:
                Game.active_rows = 1
                Game.box_colors = {}
                letters = {}
                for row in "12345":
                    for index in word_length:
                        # If user didnt guess any letter yet, input values should be an empty strings
                        letters[f"row{row}col{index}"] = ""

            if request.method == "POST":
                Game.reset_flag = False  # Avoid clearing the letters dict if user already made a guess
                if "" in request.POST.values():
                    pass
                else:
                    for key, value in request.POST.items():
                        if 'token' not in key:
                            letters[key] = value.upper()
                    for key, value in letters.items():
                        if f'row{Game.active_rows}' in key:
                            if value in word['word']:
                                if word['word'][int(key[-1]) - 1] == value:
                                    Game.box_colors[key] = 'lightgreen'
                                else:
                                    Game.box_colors[key] = 'orange'
                            else:
                                Game.box_colors[key] = '#C0C0C0'
                    Game.active_rows += 1

            return render(
                request,
                "game.html",
                {
                    "word": word,
                    "word_length": word_length,
                    "letters": letters,
                    "active_rows": Game.active_rows,
                    "box_colors": Game.box_colors,
                },
            )

        except KeyError:
            return redirect("/404/")


def error404(request):
    return render(request, "error404.html")
