from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_commercial_listing_v2_contact_preference import (
    ListingAdminV2CommercialListingV2ContactPreference,
)
from ..models.listing_admin_v2_commercial_listing_v2_listing_action import (
    ListingAdminV2CommercialListingV2ListingAction,
)
from ..models.listing_admin_v2_commercial_listing_v2_occupancy_type import (
    ListingAdminV2CommercialListingV2OccupancyType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_admin_v2_agent_contact import ListingAdminV2AgentContact
    from ..models.listing_admin_v2_commercial_auction import ListingAdminV2CommercialAuction
    from ..models.listing_admin_v2_commercial_price import ListingAdminV2CommercialPrice
    from ..models.listing_admin_v2_commercial_property import ListingAdminV2CommercialProperty
    from ..models.listing_admin_v2_contact import ListingAdminV2Contact
    from ..models.listing_admin_v2_inspection_details import ListingAdminV2InspectionDetails
    from ..models.listing_admin_v2_lease import ListingAdminV2Lease
    from ..models.listing_admin_v2_listing_supplementary import ListingAdminV2ListingSupplementary
    from ..models.listing_admin_v2_property_media import ListingAdminV2PropertyMedia
    from ..models.listing_admin_v2_specific_unit_detail import ListingAdminV2SpecificUnitDetail
    from ..models.listing_admin_v2_tenant import ListingAdminV2Tenant
    from ..models.listing_admin_v2_tender import ListingAdminV2Tender
    from ..models.listing_admin_v2eoi import ListingAdminV2EOI


T = TypeVar("T", bound="ListingAdminV2CommercialListingV2")


@_attrs_define
class ListingAdminV2CommercialListingV2:
    """Commercial Listing V2

    Example:
        {'salePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex', 'priceReduction':
            True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to': 2200000}, 'leasePrice': {'priceUnitType':
            'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide
            $2,200', 'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3, 'leaseOutgoings': 3200},
            'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00', 'leaseEnd': '2022-11-11T16:31:07.5504369+11:00',
            'name': 'John Smith', 'rentalDetails': 'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May
            2013', 'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False}, 'tender':
            {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011', 'endDate':
            '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted', 'annualReturn': 10, 'unitsOffered': 1,
            'nabers': 4.5, 'saleTerms': 'will be started after 3 days', 'auction': {'auctionTerms': '10% deposit, balance 60
            days.', 'dateTime': '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'}, 'propertyDetails':
            {'propertyType': ['retail'], 'buildingType': 'whole', 'parking': {'parkingType': 'noParking', 'numberOnSite':
            0}, 'pdfs': [], 'images': [{'resourceType': 'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'}, {'resourceType': 'photograph',
            'url': 'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'}, {'resourceType':
            'photograph', 'url': 'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress', 'streetNumber': '287',
            'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area': {'value': 174, 'unit': 'squareMetres'},
            'landArea': {'unit': 'squareMetres', 'value': 194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId':
            484442, 'firstName': 'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile': '0411
            345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight 1', 'Hightlight 2',
            'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider': 'YOUR_LISTING_PROVIDER', 'domainAgencyID':
            13, 'providerAdId': 'YOUR_PROVIDER_AD_ID', 'features': ' Air conditioning, Alarm System, Intercom',
            'description': 'Situated within Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property
            represents a fantastic opportunity to own a tenanted strata retail shop in a successful shopping centre.',
            'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails': {'inspections': [{'from':
            '2022-10-11T17:00:00.0000000+11:00', 'to': '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-15T17:00:00.0000000+11:00', 'to': '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-19T17:00:00.0000000+11:00', 'to': '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media':
            [{'resourceType': 'video', 'url': 'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}, {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}], 'listingAction': 'saleAndLease',
            'contacts': [{'domainAgentId': 881492, 'firstName': 'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax':
            '23444 444 44', 'mobile': '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}

    Attributes:
        property_details (ListingAdminV2CommercialProperty): Commercial Property
        domain_agency_id (int): The Domain Agency Id number
        provider_ad_id (str): External Advertisement Id of up to 50 characters will be stored.<br />
            This value is used to identify an Advertisement for updates and should be unique for listing provider.<br />
            This value is case-insensitive (meaning AAAA will update aaaa).
        listing_action (ListingAdminV2CommercialListingV2ListingAction): Sale or Rent
        sale_price (Union[Unset, ListingAdminV2CommercialPrice]): Commercial component for price
        lease_price (Union[Unset, ListingAdminV2CommercialPrice]): Commercial component for price
        lease (Union[Unset, ListingAdminV2Lease]): Properties for lease listings
        eoi (Union[Unset, ListingAdminV2EOI]): Express of Interest
        tenant (Union[Unset, ListingAdminV2Tenant]): Tenant Information
        tender (Union[Unset, ListingAdminV2Tender]): Tender Information
        occupancy_type (Union[Unset, ListingAdminV2CommercialListingV2OccupancyType]): Occupancy. Can be 'Tenanted',
            'Vacant'
        annual_return (Union[Unset, int]): Integer value of percentage return on this property or business.
        units_offered (Union[Unset, int]): Integer value of units offered for sale or lease
        unit_details (Union[Unset, List['ListingAdminV2SpecificUnitDetail']]): Units details
        nabers (Union[Unset, float]): The NABERS Rating is the energy efficiency rating that the property has been
            measured to have.
            This rating is measured in increments of .5 and can range from 0 to 6.
            The NABERS rating is required for spaces within office buildings of 1000 square metres or more.
            For more information on the NABERS rating system please visit http://www.nabers.gov.au
        sale_terms (Union[Unset, str]): Information relating to aspects of the sale, such as required deposit,
            settlement time. Up to 50 characters, optional. Ignored for lease listings
        auction (Union[Unset, ListingAdminV2CommercialAuction]): Commercial Auction Details
        conjunction_agents (Union[Unset, List['ListingAdminV2AgentContact']]): List of conjunction agents
        highlights (Union[Unset, List[str]]): Highlight Items
        under_offer_or_contract (Union[Unset, bool]): Set for Sale listings only
        domain_ad_id (Union[Unset, int]): Domain Advertisement Id, not applicable for creating new ads.
            Mandatory when updating a listing that belongs to an agency that
            is in the process of being migrated between listing providers.
        listing_provider (Union[Unset, str]): A string identifying the data provider
        features (Union[Unset, str]):  Comma-separated list of features. 1000 characters in length. Select as
            appropriate or write your own.
            INSIDE: Air conditioning, Ensuite, Floorboards, Indoor Spa, Gym, Alarm System, Intercom, Built in wardrobes,
            Furnished, Internal Laundry, Pets allowed, Cable or Satellite, Gas, Broadband internet access, Bath,
            Fireplace(s), Separate Dining Room, Heating, Dishwasher, Study.
            OUTSIDE: Tennis Court, Secure Parking, Shed, Fully fenced, Balcony / Deck, Garden / Courtyard, Swimming Pool,
            Outdoor Spa.
            LOCATION: Ground floor, Water Views, North Facing, City Views.
            ECO FRIENDLY: Double glazed windows, Energy efficient appliances, Water efficient appliances, Wall / ceiling
            insulation, Rainwater storage tank, Greywater system, Water efficient fixtures, Solar hot water, Solar panels
        description (Union[Unset, str]): Description of the property.
            6000 characters in length. The following HTML elements are permitted: &lt;br /&gt;, &lt;p&gt;&lt;/p&gt;,
            &amp;nbsp;. HTML must be well-formed.
            Carriage Returns are interpreted as line breaks. Foreign characters must be HTML encoded, e.g., façade for
            façade.
            Unicode characters which are unsupported by Latin-1 (ISO-8859-1 range from U+0080 to U+00FF), will be removed
            https://en.wikipedia.org/wiki/ISO/IEC_8859-1
        summary (Union[Unset, str]): 'Headline' Any HTML stripped out.  If the Summary is less than 80 characters long
            then the description is concatenated to it and the total trimmed to 250 characters.
        inspection_details (Union[Unset, ListingAdminV2InspectionDetails]): Inspection details
        media (Union[Unset, List['ListingAdminV2PropertyMedia']]): Links to VideoURL, virtual tour or weblink. Maximum
            length of media URLs is 255 characters.
        contact_preference (Union[Unset, ListingAdminV2CommercialListingV2ContactPreference]): Indicates the listing
            preferred contact method. Default by both phone and email if not provided.
        contacts (Union[Unset, List['ListingAdminV2Contact']]): Minimum required attributes: First name, last name and
            E-mail.
            If the DomainAgentId is provided, contact information will be based on the existing agent found for that id.
            Otherwise first name, last name and email will be used to find the matching contact. A new contact will be
            created if no contact can be found.
        other_enquiry_email (Union[Unset, str]): Sets an additional Email Address to which enquiries on the Listing will
            be sent
        receive_emails_to_default_address (Union[Unset, bool]): Send email enquiries to the default address for this
            listing type
        is_rural (Union[Unset, bool]): True if the property is rural
        supplementary (Union[Unset, List['ListingAdminV2ListingSupplementary']]): Rural attributes

            *Improvements* (optional)

            Available `types` (fixed list, optional):
            * Machinery Shed
            * Shearing Shed
            * Workshop
            * Shearers Quarters
            * Silos
            * Other Housing
            * Managers Accommodation

            *Fencing* (optional)

            `description` (string, optional): free text fencing description, maximum 250 characters.

            *Yards* (optional)

            Available `types` (fixed list, optional):
            * Sheep
            * Cattle

            *Homestead* (optional)

            `description` (string, optional): description of the homestead and construction, maximum 250 characters.

            `metadata` (optional)
            * `area` (decimal, optional): homestead area in square metres.

            Available `types` (fixed list, optional):
            * Office
            * Ensuite
            * Tennis Court
            * Mains Gas
            * Floorboards
            * Internal Laundry

            *Water* (optional)

            `description` (string, optional): water comments, maximum 250 characters.

            Available `types` (fixed list, optional):
            * Tank
            * Well
            * Reticulated
            * Bores
            * Springs
            * Creeks
            * Dams
            * River

            *Crops* (optional)

            `description` (string, optional): description of the crops, maximum 250 characters.

            `metadata` (optional)
            * `croppedAnnually` (decimal, optional): average annual area cropped in hectares.
            * `fallowAnnually` (decimal, optional): average annual fallow area in hectares.
            * `pastures` (string, optional): description of pastures available, maximum 250 characters.

            *Livestock* (optional)

            `description` (string, optional): additional comments, maximum 250 characters.

            `metadata` (optional)
            * `capacity` (decimal, optional): property carrying capacity in DSE (unit of carry capacity).

            Available `types` (fixed list, optional):
            * Sheep
            * Pigs
            * Cattle
            * Poultry
            * Horses
            * Exotic
            * Goats
            * Stud

            *Inclusions* (optional)

            `description` (string, optional): description of plant and machinery included in sale, maximum 250 characters.

            `metadata` (optional)
            * `livestock` (string, optional): description of livestock included in sale, maximum 250 characters.
            * `crop` (string, optional): description of crops included in sale, maximum 250 characters.

            *Irrigation* (optional)

            `description` (string, optional): irrigation comments, maximum 250 characters

            `metadata` (optional)
            * `rainfall` (decimal, optional): annual rainfall in millimetres.
    """

    property_details: "ListingAdminV2CommercialProperty"
    domain_agency_id: int
    provider_ad_id: str
    listing_action: ListingAdminV2CommercialListingV2ListingAction
    sale_price: Union[Unset, "ListingAdminV2CommercialPrice"] = UNSET
    lease_price: Union[Unset, "ListingAdminV2CommercialPrice"] = UNSET
    lease: Union[Unset, "ListingAdminV2Lease"] = UNSET
    eoi: Union[Unset, "ListingAdminV2EOI"] = UNSET
    tenant: Union[Unset, "ListingAdminV2Tenant"] = UNSET
    tender: Union[Unset, "ListingAdminV2Tender"] = UNSET
    occupancy_type: Union[Unset, ListingAdminV2CommercialListingV2OccupancyType] = UNSET
    annual_return: Union[Unset, int] = UNSET
    units_offered: Union[Unset, int] = UNSET
    unit_details: Union[Unset, List["ListingAdminV2SpecificUnitDetail"]] = UNSET
    nabers: Union[Unset, float] = UNSET
    sale_terms: Union[Unset, str] = UNSET
    auction: Union[Unset, "ListingAdminV2CommercialAuction"] = UNSET
    conjunction_agents: Union[Unset, List["ListingAdminV2AgentContact"]] = UNSET
    highlights: Union[Unset, List[str]] = UNSET
    under_offer_or_contract: Union[Unset, bool] = UNSET
    domain_ad_id: Union[Unset, int] = UNSET
    listing_provider: Union[Unset, str] = UNSET
    features: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    inspection_details: Union[Unset, "ListingAdminV2InspectionDetails"] = UNSET
    media: Union[Unset, List["ListingAdminV2PropertyMedia"]] = UNSET
    contact_preference: Union[Unset, ListingAdminV2CommercialListingV2ContactPreference] = UNSET
    contacts: Union[Unset, List["ListingAdminV2Contact"]] = UNSET
    other_enquiry_email: Union[Unset, str] = UNSET
    receive_emails_to_default_address: Union[Unset, bool] = UNSET
    is_rural: Union[Unset, bool] = UNSET
    supplementary: Union[Unset, List["ListingAdminV2ListingSupplementary"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_details = self.property_details.to_dict()

        domain_agency_id = self.domain_agency_id

        provider_ad_id = self.provider_ad_id

        listing_action = self.listing_action.value

        sale_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sale_price, Unset):
            sale_price = self.sale_price.to_dict()

        lease_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lease_price, Unset):
            lease_price = self.lease_price.to_dict()

        lease: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lease, Unset):
            lease = self.lease.to_dict()

        eoi: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.eoi, Unset):
            eoi = self.eoi.to_dict()

        tenant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tenant, Unset):
            tenant = self.tenant.to_dict()

        tender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tender, Unset):
            tender = self.tender.to_dict()

        occupancy_type: Union[Unset, str] = UNSET
        if not isinstance(self.occupancy_type, Unset):
            occupancy_type = self.occupancy_type.value

        annual_return = self.annual_return

        units_offered = self.units_offered

        unit_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unit_details, Unset):
            unit_details = []
            for unit_details_item_data in self.unit_details:
                unit_details_item = unit_details_item_data.to_dict()
                unit_details.append(unit_details_item)

        nabers = self.nabers

        sale_terms = self.sale_terms

        auction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auction, Unset):
            auction = self.auction.to_dict()

        conjunction_agents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conjunction_agents, Unset):
            conjunction_agents = []
            for conjunction_agents_item_data in self.conjunction_agents:
                conjunction_agents_item = conjunction_agents_item_data.to_dict()
                conjunction_agents.append(conjunction_agents_item)

        highlights: Union[Unset, List[str]] = UNSET
        if not isinstance(self.highlights, Unset):
            highlights = self.highlights

        under_offer_or_contract = self.under_offer_or_contract

        domain_ad_id = self.domain_ad_id

        listing_provider = self.listing_provider

        features = self.features

        description = self.description

        summary = self.summary

        inspection_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inspection_details, Unset):
            inspection_details = self.inspection_details.to_dict()

        media: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        contact_preference: Union[Unset, str] = UNSET
        if not isinstance(self.contact_preference, Unset):
            contact_preference = self.contact_preference.value

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        other_enquiry_email = self.other_enquiry_email

        receive_emails_to_default_address = self.receive_emails_to_default_address

        is_rural = self.is_rural

        supplementary: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supplementary, Unset):
            supplementary = []
            for supplementary_item_data in self.supplementary:
                supplementary_item = supplementary_item_data.to_dict()
                supplementary.append(supplementary_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyDetails": property_details,
                "domainAgencyID": domain_agency_id,
                "providerAdId": provider_ad_id,
                "listingAction": listing_action,
            }
        )
        if sale_price is not UNSET:
            field_dict["salePrice"] = sale_price
        if lease_price is not UNSET:
            field_dict["leasePrice"] = lease_price
        if lease is not UNSET:
            field_dict["lease"] = lease
        if eoi is not UNSET:
            field_dict["eoi"] = eoi
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if tender is not UNSET:
            field_dict["tender"] = tender
        if occupancy_type is not UNSET:
            field_dict["occupancyType"] = occupancy_type
        if annual_return is not UNSET:
            field_dict["annualReturn"] = annual_return
        if units_offered is not UNSET:
            field_dict["unitsOffered"] = units_offered
        if unit_details is not UNSET:
            field_dict["unitDetails"] = unit_details
        if nabers is not UNSET:
            field_dict["nabers"] = nabers
        if sale_terms is not UNSET:
            field_dict["saleTerms"] = sale_terms
        if auction is not UNSET:
            field_dict["auction"] = auction
        if conjunction_agents is not UNSET:
            field_dict["conjunctionAgents"] = conjunction_agents
        if highlights is not UNSET:
            field_dict["highlights"] = highlights
        if under_offer_or_contract is not UNSET:
            field_dict["underOfferOrContract"] = under_offer_or_contract
        if domain_ad_id is not UNSET:
            field_dict["domainAdId"] = domain_ad_id
        if listing_provider is not UNSET:
            field_dict["listingProvider"] = listing_provider
        if features is not UNSET:
            field_dict["features"] = features
        if description is not UNSET:
            field_dict["description"] = description
        if summary is not UNSET:
            field_dict["summary"] = summary
        if inspection_details is not UNSET:
            field_dict["inspectionDetails"] = inspection_details
        if media is not UNSET:
            field_dict["media"] = media
        if contact_preference is not UNSET:
            field_dict["contactPreference"] = contact_preference
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if other_enquiry_email is not UNSET:
            field_dict["otherEnquiryEmail"] = other_enquiry_email
        if receive_emails_to_default_address is not UNSET:
            field_dict["receiveEmailsToDefaultAddress"] = receive_emails_to_default_address
        if is_rural is not UNSET:
            field_dict["isRural"] = is_rural
        if supplementary is not UNSET:
            field_dict["supplementary"] = supplementary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_admin_v2_agent_contact import ListingAdminV2AgentContact
        from ..models.listing_admin_v2_commercial_auction import ListingAdminV2CommercialAuction
        from ..models.listing_admin_v2_commercial_price import ListingAdminV2CommercialPrice
        from ..models.listing_admin_v2_commercial_property import ListingAdminV2CommercialProperty
        from ..models.listing_admin_v2_contact import ListingAdminV2Contact
        from ..models.listing_admin_v2_inspection_details import ListingAdminV2InspectionDetails
        from ..models.listing_admin_v2_lease import ListingAdminV2Lease
        from ..models.listing_admin_v2_listing_supplementary import ListingAdminV2ListingSupplementary
        from ..models.listing_admin_v2_property_media import ListingAdminV2PropertyMedia
        from ..models.listing_admin_v2_specific_unit_detail import ListingAdminV2SpecificUnitDetail
        from ..models.listing_admin_v2_tenant import ListingAdminV2Tenant
        from ..models.listing_admin_v2_tender import ListingAdminV2Tender
        from ..models.listing_admin_v2eoi import ListingAdminV2EOI

        d = src_dict.copy()
        property_details = ListingAdminV2CommercialProperty.from_dict(d.pop("propertyDetails"))

        domain_agency_id = d.pop("domainAgencyID")

        provider_ad_id = d.pop("providerAdId")

        listing_action = ListingAdminV2CommercialListingV2ListingAction(d.pop("listingAction"))

        _sale_price = d.pop("salePrice", UNSET)
        sale_price: Union[Unset, ListingAdminV2CommercialPrice]
        if isinstance(_sale_price, Unset):
            sale_price = UNSET
        else:
            sale_price = ListingAdminV2CommercialPrice.from_dict(_sale_price)

        _lease_price = d.pop("leasePrice", UNSET)
        lease_price: Union[Unset, ListingAdminV2CommercialPrice]
        if isinstance(_lease_price, Unset):
            lease_price = UNSET
        else:
            lease_price = ListingAdminV2CommercialPrice.from_dict(_lease_price)

        _lease = d.pop("lease", UNSET)
        lease: Union[Unset, ListingAdminV2Lease]
        if isinstance(_lease, Unset):
            lease = UNSET
        else:
            lease = ListingAdminV2Lease.from_dict(_lease)

        _eoi = d.pop("eoi", UNSET)
        eoi: Union[Unset, ListingAdminV2EOI]
        if isinstance(_eoi, Unset):
            eoi = UNSET
        else:
            eoi = ListingAdminV2EOI.from_dict(_eoi)

        _tenant = d.pop("tenant", UNSET)
        tenant: Union[Unset, ListingAdminV2Tenant]
        if isinstance(_tenant, Unset):
            tenant = UNSET
        else:
            tenant = ListingAdminV2Tenant.from_dict(_tenant)

        _tender = d.pop("tender", UNSET)
        tender: Union[Unset, ListingAdminV2Tender]
        if isinstance(_tender, Unset):
            tender = UNSET
        else:
            tender = ListingAdminV2Tender.from_dict(_tender)

        _occupancy_type = d.pop("occupancyType", UNSET)
        occupancy_type: Union[Unset, ListingAdminV2CommercialListingV2OccupancyType]
        if isinstance(_occupancy_type, Unset):
            occupancy_type = UNSET
        else:
            occupancy_type = ListingAdminV2CommercialListingV2OccupancyType(_occupancy_type)

        annual_return = d.pop("annualReturn", UNSET)

        units_offered = d.pop("unitsOffered", UNSET)

        unit_details = []
        _unit_details = d.pop("unitDetails", UNSET)
        for unit_details_item_data in _unit_details or []:
            unit_details_item = ListingAdminV2SpecificUnitDetail.from_dict(unit_details_item_data)

            unit_details.append(unit_details_item)

        nabers = d.pop("nabers", UNSET)

        sale_terms = d.pop("saleTerms", UNSET)

        _auction = d.pop("auction", UNSET)
        auction: Union[Unset, ListingAdminV2CommercialAuction]
        if isinstance(_auction, Unset):
            auction = UNSET
        else:
            auction = ListingAdminV2CommercialAuction.from_dict(_auction)

        conjunction_agents = []
        _conjunction_agents = d.pop("conjunctionAgents", UNSET)
        for conjunction_agents_item_data in _conjunction_agents or []:
            conjunction_agents_item = ListingAdminV2AgentContact.from_dict(conjunction_agents_item_data)

            conjunction_agents.append(conjunction_agents_item)

        highlights = cast(List[str], d.pop("highlights", UNSET))

        under_offer_or_contract = d.pop("underOfferOrContract", UNSET)

        domain_ad_id = d.pop("domainAdId", UNSET)

        listing_provider = d.pop("listingProvider", UNSET)

        features = d.pop("features", UNSET)

        description = d.pop("description", UNSET)

        summary = d.pop("summary", UNSET)

        _inspection_details = d.pop("inspectionDetails", UNSET)
        inspection_details: Union[Unset, ListingAdminV2InspectionDetails]
        if isinstance(_inspection_details, Unset):
            inspection_details = UNSET
        else:
            inspection_details = ListingAdminV2InspectionDetails.from_dict(_inspection_details)

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = ListingAdminV2PropertyMedia.from_dict(media_item_data)

            media.append(media_item)

        _contact_preference = d.pop("contactPreference", UNSET)
        contact_preference: Union[Unset, ListingAdminV2CommercialListingV2ContactPreference]
        if isinstance(_contact_preference, Unset):
            contact_preference = UNSET
        else:
            contact_preference = ListingAdminV2CommercialListingV2ContactPreference(_contact_preference)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = ListingAdminV2Contact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        other_enquiry_email = d.pop("otherEnquiryEmail", UNSET)

        receive_emails_to_default_address = d.pop("receiveEmailsToDefaultAddress", UNSET)

        is_rural = d.pop("isRural", UNSET)

        supplementary = []
        _supplementary = d.pop("supplementary", UNSET)
        for supplementary_item_data in _supplementary or []:
            supplementary_item = ListingAdminV2ListingSupplementary.from_dict(supplementary_item_data)

            supplementary.append(supplementary_item)

        listing_admin_v2_commercial_listing_v2 = cls(
            property_details=property_details,
            domain_agency_id=domain_agency_id,
            provider_ad_id=provider_ad_id,
            listing_action=listing_action,
            sale_price=sale_price,
            lease_price=lease_price,
            lease=lease,
            eoi=eoi,
            tenant=tenant,
            tender=tender,
            occupancy_type=occupancy_type,
            annual_return=annual_return,
            units_offered=units_offered,
            unit_details=unit_details,
            nabers=nabers,
            sale_terms=sale_terms,
            auction=auction,
            conjunction_agents=conjunction_agents,
            highlights=highlights,
            under_offer_or_contract=under_offer_or_contract,
            domain_ad_id=domain_ad_id,
            listing_provider=listing_provider,
            features=features,
            description=description,
            summary=summary,
            inspection_details=inspection_details,
            media=media,
            contact_preference=contact_preference,
            contacts=contacts,
            other_enquiry_email=other_enquiry_email,
            receive_emails_to_default_address=receive_emails_to_default_address,
            is_rural=is_rural,
            supplementary=supplementary,
        )

        listing_admin_v2_commercial_listing_v2.additional_properties = d
        return listing_admin_v2_commercial_listing_v2

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
