from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django import forms
from .models import *
from Account.models import *

def list(request):
    trainees = Trainee.objects.all()
    context = {'trainees': trainees}
    return render(request, 'trainee/list.html', context)

    

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, pk=id)
    
    if request.method == 'POST':
  
        name = request.POST.get('name')
        account_id = request.POST.get('Account_id')
        profile_image = request.FILES.get('profile_image')

      
        if name and 0 < len(name) <= 100:
            trainee.name = name
            trainee.id_obj = get_object_or_404(Account, pk=account_id)
            if profile_image:
                trainee.image = profile_image

            trainee.save()
            return redirect('list')
        else:
        
            context = {
                'trainee': trainee,
                'error': 'Invalid name'
            }
            return render(request, 'trainee/update.html', context)
    
    context = {
        'trainee': trainee,
        'accounts': Account.objects.all() 
    }
    return render(request, 'trainee/update.html', context)

    
def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, pk=id)

    if request.method == 'POST':
        trainee.delete()
        return JsonResponse({'success': True})

    return render(request, 'trainee/delete.html', {'trainee': trainee})

    

def show_details_trainee(request, id):
    trainee = get_object_or_404(Trainee, pk=id)
    return render(request, 'trainee/showDetails.html', {'trainee': trainee})
def create(request):
    if request.method == 'POST':
        form = NewTraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return render(request, 'trainee/create.html', {'form': form, 'error': 'Invalid data'})
    else:
        form = NewTraineeForm()
    
    return render(request, 'trainee/create.html', {'form': form})


class NewTraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'id_obj', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter trainee name', 'class': 'form-control'}),
            'id_obj': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_obj'].choices = [(account.id, account.name) for account in Account.objects.all()]