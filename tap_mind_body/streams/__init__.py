from tap_mind_body.streams.classes import ClassesStream
from tap_mind_body.streams.clients import ClientsStream
from tap_mind_body.streams.locations import LocationsStream
from tap_mind_body.streams.sales import SalesStream
from tap_mind_body.streams.class_descriptions import ClassDescriptionsStream
from tap_mind_body.streams.class_schedules import ClassSchedulesStream
from tap_mind_body.streams.class_visits import ClassVisitsStream
from tap_mind_body.streams.waitlist_entries import WaitlistEntriesStream
from tap_mind_body.streams.client_purchases import ClientPurchasesStream
from tap_mind_body.streams.contracts import ContractsStream
from tap_mind_body.streams.gift_cards import GiftCardsStream
from tap_mind_body.streams.packages import PackagesStream
from tap_mind_body.streams.products import ProductsStream
from tap_mind_body.streams.services import ServicesStream
from tap_mind_body.streams.custom_payment_methods import CustomPaymentMethodsStream
from tap_mind_body.streams.accepted_card_types import AcceptedCardTypesStream



AVAILABLE_STREAMS = [
    ClassesStream,
    ClientsStream,
    LocationsStream,
    SalesStream,
    ClassSchedulesStream,
    ClassDescriptionsStream,
    ClassVisitsStream,
    WaitlistEntriesStream,
    ClientPurchasesStream,
    ContractsStream,    
    GiftCardsStream,
    PackagesStream,
    ProductsStream,
    ServicesStream,
    CustomPaymentMethodsStream,
    AcceptedCardTypesStream,
]

__all__ = [s.__name__ for s in AVAILABLE_STREAMS]