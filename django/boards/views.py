from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User

# Create your views here.

def home(request, error=None):
	boards = Board.objects.all()
	return render(request, "home.html", {"boards":boards, "error":error})

def topic(request, id_board):
	board = get_object_or_404(Board, pk=id_board)
	return render(request, "topic.html", {"board": board})

def new(request, id_board):
	board = get_object_or_404(Board, pk=id_board)
	user = User.objects.first()
	if request.method == "POST":
		subject = request.POST["subject"]
		message = request.POST["message"]
		topic = Topic.objects.create(
				subject=subject,
				board=board,
				created_by=user
			)
		post = Post.objects.create(
				message=message,
				topic=topic,
				created_by=user
			)
		return redirect("topic", id_board=board.pk)
	return render(request, "new_topic.html", {"board":board})
