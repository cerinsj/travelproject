from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from product.models import TravelPlace




class latest_feed(Feed):
    title="TRAVEL"
    link="/drcomments/"
    description="Travel is useful for a tour planning. It helps in deciding the best tour packages."
    def items(self):
        return TravelPlace.objects.order_by('date')[:3]
    def item_title(self,place):
        return place.name
    def item_description(self,place):
        return truncatewords(place.desc,10)
    def item_link(self,place):
        return reverse("homepage")
        



