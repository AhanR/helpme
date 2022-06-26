import json
from turtle import pos
from django.http import HttpResponse
from django.shortcuts import render

currentUser = "Ahan Ray"

def index (req) :
	posts =  [{"author" : "Ahan Ray", "postId" : '10', "postContent" : "This is the first post"}, {"author" : "Da goat", "postId" : '11', "postContent" : "This is the second post"}]
	params = {"posts" : {"This" : "is", "good" : "yes"},
				"name" : "Ahan Ray"}
	return render(req, 'index.html', params)

def makepost(req) :
    content = req.GET.get("postContent")
    params = {"name" : currentUser, "postContent" : content, "postStatus" : "false", "errorMessage" : "This is an error message"}
    return render(req, 'post.html', params)