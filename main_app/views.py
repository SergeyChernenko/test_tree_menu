from django.shortcuts import render
from  .models import Tree
from mptt.forms import TreeNodeChoiceField

def details(request,element):
    obj = Tree.objects.get(pk=element)
    category = TreeNodeChoiceField(queryset=obj.get_descendants(),
                                   start_level=obj.level)
    return render(request, 'main.html', {'tree': category.queryset})



def tree_get(request):
    tree = Tree.objects.all()
    return render(request, 'main.html', {'tree': tree})




