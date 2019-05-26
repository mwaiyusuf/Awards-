from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from __future__ import unicode_literals 
from .models import Image,Location,tags,Profile,Review,NewsLetterRecipients,Like,Project 
from .forms import NewImageForm, UpdatebioForm, ReviewForm, NewProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login')
def home  (request):
    # Display all projects here:

    if request.GET.get('search_term'):
        projects = Project.search_project(request.GET.get('search_term'))

    else:
        projects = Project.objects.all()

    form = NewsLetterForm
    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('home_projects')

    return render(request, 'index.html', {'projects':projects, 'letterForm':form})
def project(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()
    else:
        form = ReviewForm()

        # return HttpResponseRedirect(reverse('image', args=(image.id,)))

    return render(request, 'image.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})
