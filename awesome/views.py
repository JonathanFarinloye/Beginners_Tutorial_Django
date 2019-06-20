from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')


def counter(request):
    if request.method == 'POST':
        vow = 0
        for i in request.POST['input-stuff']:
            if i in 'aeiou':
                vow += 1
        return render(request, 'count.html', {'count': vow})
    return redirect('home')