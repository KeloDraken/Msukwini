from django.shortcuts import render
from msukwini.core.forms import CreateFeedbackForm

from msukwini.core.posts.models import Post


def index(request):
    posts = Post.objects.all()

    if not request.method == "POST":
        feedback_form = CreateFeedbackForm()
    else:
        feedback_form = CreateFeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
        else:
            print("FAILED")

    context = {"posts": posts, "form": feedback_form}
    return render(request, "index.html", context)
