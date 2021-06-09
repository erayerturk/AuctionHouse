from typing import List, Any

from ninja import Schema
from ninja.orm import create_schema

from backend.models import Bids, AntiqueItems

BidSchema = create_schema(Bids, exclude=['id', 'user', 'timestamp', 'antique_item'])
AntiqueItemsSchema = create_schema(AntiqueItems)

BidSchemaFull = create_schema(Bids)


class AntiqueItemListSchema(Schema):
    per_page: int
    page: int
    antique_items: List[AntiqueItemsSchema] = []


class BidsListSchema(Schema):
    historical_bid: List[BidSchemaFull] = []


class SettingsSchema(Schema):
    user_id: int
    balance: str
    bid_increase: str
