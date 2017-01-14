import requests

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        data = requests.get(
            'http://bws.buscape.com.br/service/findOfferList/'
            'lomadee/65717751673178504d42633d/BR/?format=json&results=30&'
            'sourceId=35734515&allowedSellers=903294,77,1261,114286&page=1'
        ).json()['offer']
        context['products'] = [dict(
            name=prod['offer'].get('offername'),
            image=prod['offer'].get('thumbnail'),
            price=prod['offer'].get('price'),
            link=prod['offer'].get('links'),
        ) for prod in data]
        return context
