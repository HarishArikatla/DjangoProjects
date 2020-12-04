from . models import Devpyjp
 
def images_view(request):
    images = Devpyjp.objects..all()
    context={
         'images':images,
           }
 
    return render(request,'templates/image.html',context)