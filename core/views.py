import requests

from django.views.generic import TemplateView, DetailView

from core.models import Post


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_reviews(self):
        response = requests.get('https://graph.facebook.com/v2.9/16000029635'
                '45861/ratings?access_token=EAACEdEose0cBAH62i51NqBpwCX7fVUj'
                'pXpRjmBZCZAeTJk8R1ihMfjUuxMER5YaIeAwNRBj8qU9bHtOlERxKzMZBC3'
                'ZA5AExhDGh29gUfY0YYUYWcfDbxcmO7yt3GscypBZCIea3GF5UGpPvmBwMJ'
                'cSKKOQlzylIXxvpEHJraelZAYFrdU3ZCR1peiErXCy5ZCYZD')
        return [dict(
            texto=dado.get('review_text'),
            nome=dado.get('reviewer').get('name')) for dado in response.json()[
            'data'] if dado.get('review_text')]

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['reviews'] = self.get_reviews()
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
