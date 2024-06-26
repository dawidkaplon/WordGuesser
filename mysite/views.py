from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate
from django.http import Http404

from users.models import CustomUser
from string import ascii_letters

# Create your views here.


def index(request):
    current_language = get_language()
    if request.method == "POST":
        length = request.POST.get("word_length")
        if length not in (None, "Word's length"):
            return redirect(f"/{current_language}/words/get/length:{length}")

    return render(request, "index.html")


def translate(language):
    current_language = get_language()
    try:
        activate(language)
    finally:
        activate(current_language)

def user_statistics(request, user_email):
    user = CustomUser.objects.get(email=user_email)
    if user == request.user or request.user.is_superuser:
        return render(request, "user_statistics.html", {"user": user})
    else:
        raise Http404


class Game:
    reset_flag = True
    active_rows = 1  # Current row user is guessing
    box_colors = {}
    keyboard_bg_colors = {}
    keyboard_text_colors = {}

    win = 1
    """
    Flag to check if user correctly guessed all letters.
    If at least one letter is wrong, this variable will be changed to 0
    """

    def gameplay(request):
        global letters, current_user

        try:
            word = request.session["word"]
            word_length = [str(num + 1) for num in range(len(word["word"]))]

            if Game.reset_flag:
                try:
                    current_user = CustomUser.objects.get(email=word["user"])
                    current_user.number_of_games_played += 1
                    current_user.save()
                except CustomUser.DoesNotExist:
                    pass

                Game.active_rows = 1
                Game.box_colors = {}
                Game.keyboard_bg_colors = {}
                Game.keyboard_text_colors = {}
                Game.win = 1
                letters = {}
                for row in "12345":
                    for index in word_length:
                        # If user didnt guess any letter yet, input values should be an empty strings.
                        letters[f"row{row}col{index}"] = ""
                Game.reset_flag = False

            if request.method == "POST":
                if "give-up" in request.POST:
                    return render(request, "loss_page.html", {"word": word})
                else:
                    Game.win = 1

                    if "" in list(request.POST.values()):
                        messages.warning(request, _("Given word is not long enough!"))

                    elif any(
                        list(
                            value not in ascii_letters
                            for value in list(request.POST.values())[1:]
                        )
                    ):
                        messages.warning(request, _("Given value is not a letter!"))

                    else:
                        for key, value in request.POST.items():
                            if "token" not in key:
                                letters[key] = value.upper()

                        for key, value in letters.items():
                            if f"row{Game.active_rows}" in key:
                                Game.keyboard_text_colors[value] = "white"

                                if value in word["word"]:
                                    if word["word"][int(key[-1]) - 1] == value:
                                        """Letter is correctly guessed (correct index)"""
                                        Game.box_colors[key] = "lightgreen"
                                        Game.keyboard_bg_colors[value] = "lightgreen"
                                    else:
                                        """Letter is present in the word, but not at the chosen spot"""
                                        Game.box_colors[key] = "orange"
                                        if (
                                            Game.keyboard_bg_colors.get(value)
                                            == "lightgreen"
                                        ):
                                            pass
                                        else:
                                            Game.keyboard_bg_colors[value] = "orange"
                                        Game.win = 0
                                else:
                                    """Letter is not present in the word"""
                                    Game.box_colors[key] = "silver"
                                    Game.keyboard_bg_colors[value] = "silver"
                                    Game.win = 0

                        Game.active_rows += 1

                        if Game.win == 1:
                            """Win case"""
                            try:
                                current_user.number_of_wins += 1
                                current_user.save()
                            except:
                                pass
                            return render(request, "win_page.html", {"word": word})

                        if Game.active_rows == 6:
                            """Loss case"""
                            return render(request, "loss_page.html", {"word": word})

            return render(
                request,
                "game.html",
                {
                    "word": word,
                    "word_length": word_length,
                    "letters": letters,
                    "active_rows": Game.active_rows,
                    "box_colors": Game.box_colors,
                    "keyboard_bg_colors": Game.keyboard_bg_colors,
                    "keyboard_text_colors": Game.keyboard_text_colors,
                },
            )

        except KeyError:
            raise Http404
