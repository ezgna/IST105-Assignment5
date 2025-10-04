from django.shortcuts import render
from django.http import HttpResponse
from .forms import PuzzleForm
import math, random

def healthz(request):
    return HttpResponse("ok", status=200)

def index(request):
    context = {"form": PuzzleForm()}
    if request.method == "POST":
        form = PuzzleForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["number"]
            t = form.cleaned_data["text"]

            # Number Puzzle
            is_even = (n % 2 == 0)
            number_result = {
                "parity": "even" if is_even else "odd",
                "calc": math.isqrt(n) if (is_even and n >= 0) else (n ** 3),
                "calc_label": "square root" if is_even else "cube"
            }

            # Text Puzzle
            binary = " ".join(format(ord(c), "08b") for c in t)
            vowels = sum(1 for c in t if c.lower() in "aeiou")
            text_result = {"binary": binary, "vowel_count": vowels}

            # Treasure Hunt (1–100, 5 tries random guess)
            secret = random.randint(1, 100)
            steps = []
            win = False
            for i in range(1, 6):
                g = random.randint(1, 100)
                if g == secret:
                    steps.append(f"Try {i}: guessed {g} → HIT")
                    win = True
                    break
                steps.append(f"Try {i}: guessed {g} → miss (secret is {secret})")
            treasure_result = {"secret": secret, "steps": steps, "win": win}

            context.update({
                "form": form,
                "number_result": number_result,
                "text_result": text_result,
                "treasure_result": treasure_result,
                "submitted": True,
            })
        else:
            context["form"] = form
    return render(request, "puzzle/index.html", context)