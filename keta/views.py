from django.http import HttpResponse
from django.shortcuts import render
from . forms import SearchForm
from . import ProcessRequest

def index(request):
    context = {}
    search_form = SearchForm()
    context['search_form'] = search_form
    context['books'] = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        context['form'] = form
        if form.is_valid():
            search_text = form.cleaned_data['search_text']
            type_of_search = form.cleaned_data['advance_search']
            if type_of_search == 'isbn':
                books = [None] * 1
                books[0] = ProcessRequest.process_isbn(search_text)
                print('The prices are {} and the vendors are {}'.format(books[0].prices, books[0].vendors))
                context['books'] = books
                return render(request, 'keta/index.html', context)
            elif type_of_search == 'title':
                context['books'] = ProcessRequest.process_title(search_text)
                return render(request, 'keta/index.html', context)
            else:
                print('search {} type {}'.format(search_text, type_of_search))
                return HttpResponse('<h1> Post Method {{search_text}}</h1>')


    return render(request, 'keta/index.html', context)

# def get_name(request):
#     form = NameForm()
#     return render(request, 'keta/name.html', {'form': form})
#
# def display_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         return render(request, 'keta/display_name.html', {'form':form})
#     else:
#         return HttpResponseNotFound('<h1>Page not found</h1>')
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'keta/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'keta/results.html', {'question': question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'keta/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('keta:results', args=(question.id,)))
#
