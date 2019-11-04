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
from tap_mind_body.streams.active_session_times import ActiveSessionTimesStream
from tap_mind_body.streams.appointment_options import AppointmentOptionsStream
from tap_mind_body.streams.session_types import SessionTypesStream
from tap_mind_body.streams.bookable_items import BookableItemsStream
from tap_mind_body.streams.schedule_items import ScheduleItemsStream
from tap_mind_body.streams.staff_appointments import StaffAppointmentsStream
from tap_mind_body.streams.active_client_memberships import ActiveClientMembershipsStream
from tap_mind_body.streams.client_account_balances import ClientAccountBalancesStream
from tap_mind_body.streams.client_services import ClientServicesStream
from tap_mind_body.streams.client_visits import ClientVisitsStream
from tap_mind_body.streams.contact_logs import ContactLogsStream
from tap_mind_body.streams.client_contracts import ClientContractsStream
from tap_mind_body.streams.client_formula_notes import ClientFormulaNotesStream
from tap_mind_body.streams.client_indexes import ClientIndexesStream
from tap_mind_body.streams.client_referral_types import ClientReferralTypesStream
from tap_mind_body.streams.custom_client_fields import CustomClientFieldsStream
from tap_mind_body.streams.custom_client_fields import CustomClientFieldsStream
from tap_mind_body.streams.required_client_fields import RequiredClientFieldsStream
from tap_mind_body.streams.enrollments import EnrollmentsStream
from tap_mind_body.streams.sites import SitesStream
from tap_mind_body.streams.programs import ProgramsStream
from tap_mind_body.streams.resources import ResourcesStream
from tap_mind_body.streams.staff import StaffStream
from tap_mind_body.streams.staff_permissions import StaffPermissionsStream
from tap_mind_body.streams.cross_reigional_client_associations import CrossReigonalClientAssociationsStream





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
    ActiveSessionTimesStream,
    AppointmentOptionsStream,
    SessionTypesStream,
    BookableItemsStream,
    ScheduleItemsStream,
    StaffAppointmentsStream,
    ActiveClientMembershipsStream,
    ClientAccountBalancesStream,
    ClientServicesStream,
    ClientVisitsStream,
    ContactLogsStream,
    ClientContractsStream,
    ClientFormulaNotesStream,
    ClientIndexesStream,
    ClientReferralTypesStream,
    CustomClientFieldsStream,
    RequiredClientFieldsStream,
    EnrollmentsStream,
    SitesStream,
    ProgramsStream,
    ResourcesStream,
    StaffStream,
    StaffPermissionsStream,
    CrossReigonalClientAssociationsStream,
]

__all__ = [s.__name__ for s in AVAILABLE_STREAMS]