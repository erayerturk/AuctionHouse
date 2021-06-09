from typing import List

from django.core.paginator import Paginator
from ninja import Router

from django.shortcuts import get_object_or_404
from backend.models import AntiqueItems, Bids, AutoBid, AutoBidSettings
from backend.schemas import BidSchema, AntiqueItemListSchema, AntiqueItemsSchema, BidsListSchema, SettingsSchema

from ninja.security import HttpBasicAuth

router = Router()

users = {'user1': {'id': 1, 'password': 'user1'}, 'user2': {'id': 2, 'password': 'user2'}}


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        print(username, password)
        if username in users.keys() and password == users[username]['password']:
            return users[username]['id']


@router.post("/login", auth=BasicAuth())
def login(request):
    return {"user_id": request.auth}


@router.get("/list-antique-items", response={200: AntiqueItemListSchema})
def list_items(request, per_page: int, page: int):
    paginator = Paginator(AntiqueItems.objects.filter(), per_page)
    antique_items: List[AntiqueItems] = list(paginator.get_page(page).object_list)
    return 200, {"per_page": per_page, "page": page, "antique_items": antique_items}


@router.get("/item-details/{item_id}", response={200: AntiqueItemsSchema})
def item_details(request, item_id: int):
    item = get_object_or_404(AntiqueItems, pk=item_id)
    return 200, item


@router.post("/change-auto-bid/{item_id}")
def change_auto_bid(request, item_id: int, to_activate: bool, user_id: int):
    auto_bid = AutoBid.objects.get_or_create(antique_item_id=item_id, user=user_id)
    if not to_activate == auto_bid[0].is_automatic:
        auto_bid[0].is_automatic = to_activate
        auto_bid[0].save()

    return "OK"


@router.get("/get-auto-bid/{item_id}")
def get_auto_bid(request, item_id: int, user_id: int):
    auto_bid = AutoBid.objects.get_or_create(antique_item_id=item_id, user=user_id)
    return {'auto_bid_status': auto_bid[0].is_automatic}


@router.post("/add-bid/{antique_item_id}")
def add_bid(request, antique_item_id: int, user_id: int, payload: BidSchema):
    data = payload.dict()
    data['antique_item'] = get_object_or_404(AntiqueItems, pk=antique_item_id)
    data['user'] = user_id

    last_bid = Bids.objects.filter(antique_item_id=antique_item_id, user=user_id).order_by('-timestamp')
    if len(last_bid) == 0 or data['bid_price'] > last_bid[0].bid_price:
        if len(last_bid) > 0 and last_bid[0].user == data['user']:
            return
        bid = Bids.objects.create(**data)

        settings = {}
        for obj in AutoBidSettings.objects.all():
            settings[f'user{obj.user}'] = {'balance': obj.balance, 'bid_increase': obj.bid_increase_amount}
        auto_bids = AutoBid.objects.filter(antique_item_id=antique_item_id, is_automatic=True).order_by('-updated_at')
        if len(auto_bids) == 1:
            data['user'] = auto_bids[0].user
            data['bid_price'] = bid.bid_price + settings[f'user{auto_bids[0].user}']['bid_increase']
            if data['bid_price'] < settings[f'user{auto_bids[0].user}']['balance'] and auto_bids[0].user != bid.user:
                bid = Bids.objects.create(**data)
                return {"bid": bid.bid_price}
        elif len(auto_bids) > 1:
            while settings['user1']['balance'] > bid.bid_price and settings['user2']['balance'] > bid.bid_price:
                for auto_bid in auto_bids:
                    if auto_bid.user != bid.user:
                        data['user'] = auto_bid.user
                        bid.bid_price += settings[f'user{auto_bid.user}']['bid_increase']
                        data['bid_price'] = bid.bid_price
                        bid = Bids.objects.create(**data)

        return {"bid": bid.bid_price}

    return {"result": "OK"}


@router.get("/get-historical-bids/{item_id}", response={200: BidsListSchema})
def get_historical_bids(request, item_id: int):
    bids = Bids.objects.filter(antique_item_id=item_id).order_by('-timestamp')
    historical_bids_list: List[Bids] = list(bids)
    return 200, {'historical_bid': historical_bids_list}


@router.get("/get-settings")
def get_settings(request, user_id: int):
    settings = AutoBidSettings.objects.get_or_create(user=user_id)
    return {'balance': settings[0].balance, 'bid_increase': settings[0].bid_increase_amount}


@router.post("/save-settings")
def save_settings(request, payload: SettingsSchema):
    data = payload.dict()
    settings = get_object_or_404(AutoBidSettings, user=data['user_id'])
    settings.balance = data['balance']
    settings.bid_increase_amount = data['bid_increase']
    settings.save()
    return "OK"
