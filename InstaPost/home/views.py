from io import BytesIO

from PIL import Image, ImageFont, ImageDraw
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .form import PostForm


# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'post': post})
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

def generate_post_image(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    template_path = 'static/asset/template.jpg'
    font_path = 'static/asset/font.ttf'

    template_image = Image.open(template_path)

    draw = ImageDraw.Draw(template_image)

    font = ImageFont.truetype(font_path, size=20)

    position = (50, 50)  # Adjust the coordinates based on your template
    text = f"{post.heading}\n\n{post.paragraph}\n\n{post.pubdate}"

    draw.multiline_text(position, text, font=font, fill='black')

    edited_image_io = BytesIO()
    template_image.save(edited_image_io, format='JPEG')

    response = HttpResponse(edited_image_io.getvalue(), content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename=post_{post_id}_image.jpg'

    return response
