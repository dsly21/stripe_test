from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import stripe

from items.models import Item

stripe.api_key = ("sk_test_51MZpjjFrJdNuKCiEtA5yLya42yHIAgLJkYMYpV"
                 "QpVDTppNuKrxd0Xg5UU8Nta1BTKanBcxNxx8QqK7u9Z0pmrJWq00BbGLDCsL")


def get_session_id_view(request, item_id: int):
    product_item = get_object_or_404(Item, pk=item_id)

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        # try expect

        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": 50,
                    "product_data":
                        {
                            "name": product_item.name,
                        }
                },
                "quantity": 1,
            },
        ],
        mode="payment",
    )
    return JsonResponse(session)


def get_item_card_view(request, item_id: int):
    product_item = get_object_or_404(Item, pk=item_id)

    context = {
        'product_item': product_item
    }
    return render(request, 'item_card.html', context)
