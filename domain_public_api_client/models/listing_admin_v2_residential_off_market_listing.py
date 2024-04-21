from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_residential_off_market_listing_listing_action import (
    ListingAdminV2ResidentialOffMarketListingListingAction,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_admin_v2_contact import ListingAdminV2Contact
    from ..models.listing_admin_v2_off_market_details_base import ListingAdminV2OffMarketDetailsBase
    from ..models.listing_admin_v2_residential_off_market_property import ListingAdminV2ResidentialOffMarketProperty


T = TypeVar("T", bound="ListingAdminV2ResidentialOffMarketListing")


@_attrs_define
class ListingAdminV2ResidentialOffMarketListing:
    """Residential off market listing

    Attributes:
        domain_agency_id (int): The Domain Agency ID
        provider_ad_id (str): External Advertisement Id of up to 50 characters will be stored.<br />
            This value is used to identify an Advertisement for updates and should be unique for listing provider.<br />
            This value is case-insensitive (meaning AAAA will update aaaa).
        listing_action (ListingAdminV2ResidentialOffMarketListingListingAction): Sale or Rent
        off_market_details (ListingAdminV2OffMarketDetailsBase): Off market details base
        property_details (ListingAdminV2ResidentialOffMarketProperty): Residential off market property
        listing_provider (Union[Unset, str]): A string identifying the data provider
        description (Union[Unset, str]): Description of the property.
            6000 characters in length. The following HTML elements are permitted: &lt;br /&gt;, &lt;p&gt;&lt;/p&gt;,
            &amp;nbsp;. HTML must be well-formed.
            Carriage Returns are interpreted as line breaks. Foreign characters must be HTML encoded, e.g., façade for
            façade.
            Unicode characters which are unsupported by Latin-1 (ISO-8859-1 range from U+0080 to U+00FF), will be removed
            https://en.wikipedia.org/wiki/ISO/IEC_8859-1
        summary (Union[Unset, str]): 'Headline' Any HTML stripped out.  If the Summary is less than 80 characters long
            then the description is concatenated to it and the total trimmed to 250 characters.
        contacts (Union[Unset, List['ListingAdminV2Contact']]): Minimum required attributes: First name, last name and
            E-mail.
            If the DomainAgentId is provided, contact information will be based on the existing agent found for that id.
            Otherwise first name, last name and email will be used to find the matching contact. A new contact will be
            created if no contact can be found.
    """

    domain_agency_id: int
    provider_ad_id: str
    listing_action: ListingAdminV2ResidentialOffMarketListingListingAction
    off_market_details: "ListingAdminV2OffMarketDetailsBase"
    property_details: "ListingAdminV2ResidentialOffMarketProperty"
    listing_provider: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    contacts: Union[Unset, List["ListingAdminV2Contact"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain_agency_id = self.domain_agency_id

        provider_ad_id = self.provider_ad_id

        listing_action = self.listing_action.value

        off_market_details = self.off_market_details.to_dict()

        property_details = self.property_details.to_dict()

        listing_provider = self.listing_provider

        description = self.description

        summary = self.summary

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainAgencyID": domain_agency_id,
                "providerAdId": provider_ad_id,
                "listingAction": listing_action,
                "offMarketDetails": off_market_details,
                "propertyDetails": property_details,
            }
        )
        if listing_provider is not UNSET:
            field_dict["listingProvider"] = listing_provider
        if description is not UNSET:
            field_dict["description"] = description
        if summary is not UNSET:
            field_dict["summary"] = summary
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_admin_v2_contact import ListingAdminV2Contact
        from ..models.listing_admin_v2_off_market_details_base import ListingAdminV2OffMarketDetailsBase
        from ..models.listing_admin_v2_residential_off_market_property import ListingAdminV2ResidentialOffMarketProperty

        d = src_dict.copy()
        domain_agency_id = d.pop("domainAgencyID")

        provider_ad_id = d.pop("providerAdId")

        listing_action = ListingAdminV2ResidentialOffMarketListingListingAction(d.pop("listingAction"))

        off_market_details = ListingAdminV2OffMarketDetailsBase.from_dict(d.pop("offMarketDetails"))

        property_details = ListingAdminV2ResidentialOffMarketProperty.from_dict(d.pop("propertyDetails"))

        listing_provider = d.pop("listingProvider", UNSET)

        description = d.pop("description", UNSET)

        summary = d.pop("summary", UNSET)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = ListingAdminV2Contact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        listing_admin_v2_residential_off_market_listing = cls(
            domain_agency_id=domain_agency_id,
            provider_ad_id=provider_ad_id,
            listing_action=listing_action,
            off_market_details=off_market_details,
            property_details=property_details,
            listing_provider=listing_provider,
            description=description,
            summary=summary,
            contacts=contacts,
        )

        listing_admin_v2_residential_off_market_listing.additional_properties = d
        return listing_admin_v2_residential_off_market_listing

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
