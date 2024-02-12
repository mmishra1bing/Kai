# import django_filters
# from django_filters.filters import ChoiceFilter
# from django_filters import DateTimeFromToRangeFilter

# from .models import Item


# CATEGORY = (
#     ('Bundles', 'Bundles'),
#     ('Finished Products', 'Finished Products'),
#     ('Raw Material', 'Raw Material'),
# )


# class OrderFilter(django_filters.FilterSet):
#     # date_created = django_filters.DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(
#     #     attrs={'type': 'date'}
#     # )
#     # )
#     # status = ChoiceFilter(choices=STATUS)
#     category = ChoiceFilter(choices=CATEGORY)

#     class Meta:
#         model = Item
#         fields = [
#             'sku',
#             'name',
#             'tags',
#             'category',
#             'stock_status',
#             'available_stock'
#         ]