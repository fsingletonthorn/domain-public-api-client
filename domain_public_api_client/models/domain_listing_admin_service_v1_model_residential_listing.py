import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_listing_admin_service_v1_model_residential_listing_contact_preference import (
    DomainListingAdminServiceV1ModelResidentialListingContactPreference,
)
from ..models.domain_listing_admin_service_v1_model_residential_listing_life_style_type import (
    DomainListingAdminServiceV1ModelResidentialListingLifeStyleType,
)
from ..models.domain_listing_admin_service_v1_model_residential_listing_listing_action import (
    DomainListingAdminServiceV1ModelResidentialListingListingAction,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_auction import DomainListingAdminServiceV1ModelAuction
    from ..models.domain_listing_admin_service_v1_model_contact import DomainListingAdminServiceV1ModelContact
    from ..models.domain_listing_admin_service_v1_model_inspection_details import (
        DomainListingAdminServiceV1ModelInspectionDetails,
    )
    from ..models.domain_listing_admin_service_v1_model_listing_project import (
        DomainListingAdminServiceV1ModelListingProject,
    )
    from ..models.domain_listing_admin_service_v1_model_listing_supplementary import (
        DomainListingAdminServiceV1ModelListingSupplementary,
    )
    from ..models.domain_listing_admin_service_v1_model_price import DomainListingAdminServiceV1ModelPrice
    from ..models.domain_listing_admin_service_v1_model_property_media import (
        DomainListingAdminServiceV1ModelPropertyMedia,
    )
    from ..models.domain_listing_admin_service_v1_model_residential_property import (
        DomainListingAdminServiceV1ModelResidentialProperty,
    )
    from ..models.domain_listing_admin_service_v1_model_statement_of_information import (
        DomainListingAdminServiceV1ModelStatementOfInformation,
    )


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelResidentialListing")


@_attrs_define
class DomainListingAdminServiceV1ModelResidentialListing:
    """Residential Listing

    Attributes:
        life_style_type (Union[Unset, DomainListingAdminServiceV1ModelResidentialListingLifeStyleType]): Lifestyle type
        listing_action (Union[Unset, DomainListingAdminServiceV1ModelResidentialListingListingAction]): Sale or Rent
        contact_preference (Union[Unset, DomainListingAdminServiceV1ModelResidentialListingContactPreference]):
            Indicates the listing preferred contact method. Default by both phone and email if not provided.
        under_offer_or_contract (Union[Unset, bool]): Set for Sale listings only
        auction (Union[Unset, DomainListingAdminServiceV1ModelAuction]): Auction Details
        bond (Union[Unset, int]): Optional.  Ignored for sale listings
        available_from (Union[Unset, datetime.datetime]): Optional. Sets the Date from which a Rental or Share property
            is available. Date format: yyyy-mm-dd
        property_details (Union[Unset, DomainListingAdminServiceV1ModelResidentialProperty]): Residential Property
        is_new_development (Union[Unset, bool]): True if the property is a new development
        statement_of_information (Union[Unset, DomainListingAdminServiceV1ModelStatementOfInformation]): Statement of
            Information  Regarding sale listing
        price (Union[Unset, DomainListingAdminServiceV1ModelPrice]): Pricing Information
        project (Union[Unset, DomainListingAdminServiceV1ModelListingProject]): Listing development project details.
        domain_ad_id (Union[Unset, int]): Domain Advertisement Id, not applicable for creating new ads.  Mandatory when
            updating a listing that belongs to an agency that  is in the process of being migrated between listing
            providers.
        domain_agency_id (Union[Unset, int]): The Domain Agency Id number
        provider_ad_id (Union[Unset, str]): External Advertisement Id of up to 50 characters will be stored.&lt;br /&gt;
            This value is used to identify an Advertisement for updates and should be unique for listing provider.&lt;br
            /&gt;  This value is case-insensitive (meaning AAAA will update aaaa).
        features (Union[Unset, str]): Comma-separated list of features. 1000 characters in length. Select as appropriate
            or write your own.  INSIDE: Air conditioning, Ensuite, Floorboards, Indoor Spa, Gym, Alarm System, Intercom,
            Built in wardrobes, Furnished, Internal Laundry, Pets allowed, Cable or Satellite, Gas, Broadband internet
            access, Bath, Fireplace(s), Separate Dining Room, Heating, Dishwasher, Study.  OUTSIDE: Tennis Court, Secure
            Parking, Shed, Fully fenced, Balcony / Deck, Garden / Courtyard, Swimming Pool, Outdoor Spa.  LOCATION: Ground
            floor, Water Views, North Facing, City Views.  ECO FRIENDLY: Double glazed windows, Energy efficient appliances,
            Water efficient appliances, Wall / ceiling insulation, Rainwater storage tank, Greywater system, Water efficient
            fixtures, Solar hot water, Solar panels
        description (Union[Unset, str]): Description of the property.  6000 characters in length. The following HTML
            elements are permitted: &amp;lt;br /&amp;gt;, &amp;lt;p&amp;gt;&amp;lt;/p&amp;gt;, &amp;amp;nbsp;. HTML must be
            well-formed.  Carriage Returns are interpreted as line breaks. Foreign characters must be HTML encoded, e.g.,
            façade for façade.  Unicode characters which are unsupported by Latin-1 (ISO-8859-1 range from U+0080 to
            U+00FF), will be removed https://en.wikipedia.org/wiki/ISO/IEC_8859-1
        summary (Union[Unset, str]): 'Headline' Any HTML stripped out.  If the Summary is less than 80 characters long
            then the description is concatenated to it and the total trimmed to 250 characters.
        inspection_details (Union[Unset, DomainListingAdminServiceV1ModelInspectionDetails]): Inspection details
        media (Union[Unset, List['DomainListingAdminServiceV1ModelPropertyMedia']]): Links to VideoURL, virtual tour or
            weblink. Maximum length of media URLs is 255 characters.
        contacts (Union[Unset, List['DomainListingAdminServiceV1ModelContact']]): Minimum required attributes: First
            name, last name and E-mail.  If the DomainAgentId is provided, contact information will be based on the existing
            agent found for that id.  Otherwise first name, last name and email will be used to find the matching contact. A
            new contact will be created if no contact can be found.
        other_enquiry_email (Union[Unset, str]): Sets an additional Email Address to which enquiries on the Listing will
            be sent
        receive_emails_to_default_address (Union[Unset, bool]): Send email enquiries to the default address for this
            listing type
        is_rural (Union[Unset, bool]): True if the property is rural
        supplementary (Union[Unset, List['DomainListingAdminServiceV1ModelListingSupplementary']]): Rural attributes
            *Improvements* (optional)    Available `types` (fixed list, optional):  * Machinery Shed  * Shearing Shed  *
            Workshop  * Shearers Quarters  * Silos  * Other Housing  * Managers Accommodation    *Fencing* (optional)
            `description` (string, optional): free text fencing description, maximum 250 characters.    *Yards* (optional)
            Available `types` (fixed list, optional):  * Sheep  * Cattle    *Homestead* (optional)    `description` (string,
            optional): description of the homestead and construction, maximum 250 characters.    `metadata` (optional)  *
            `area` (decimal, optional): homestead area in square metres.    Available `types` (fixed list, optional):  *
            Office  * Ensuite  * Tennis Court  * Mains Gas  * Floorboards  * Internal Laundry    *Water* (optional)
            `description` (string, optional): water comments, maximum 250 characters.    Available `types` (fixed list,
            optional):  * Tank  * Well  * Reticulated  * Bores  * Springs  * Creeks  * Dams  * River    *Crops* (optional)
            `description` (string, optional): description of the crops, maximum 250 characters.    `metadata` (optional)  *
            `croppedAnnually` (decimal, optional): average annual area cropped in hectares.  * `fallowAnnually` (decimal,
            optional): average annual fallow area in hectares.  * `pastures` (string, optional): description of pastures
            available, maximum 250 characters.    *Livestock* (optional)    `description` (string, optional): additional
            comments, maximum 250 characters.    `metadata` (optional)  * `capacity` (decimal, optional): property carrying
            capacity in DSE (unit of carry capacity).    Available `types` (fixed list, optional):  * Sheep  * Pigs  *
            Cattle  * Poultry  * Horses  * Exotic  * Goats  * Stud    *Inclusions* (optional)    `description` (string,
            optional): description of plant and machinery included in sale, maximum 250 characters.    `metadata` (optional)
            * `livestock` (string, optional): description of livestock included in sale, maximum 250 characters.  * `crop`
            (string, optional): description of crops included in sale, maximum 250 characters.    *Irrigation* (optional)
            `description` (string, optional): irrigation comments, maximum 250 characters    `metadata` (optional)  *
            `rainfall` (decimal, optional): annual rainfall in millimetres.
    """

    life_style_type: Union[Unset, DomainListingAdminServiceV1ModelResidentialListingLifeStyleType] = UNSET
    listing_action: Union[Unset, DomainListingAdminServiceV1ModelResidentialListingListingAction] = UNSET
    contact_preference: Union[Unset, DomainListingAdminServiceV1ModelResidentialListingContactPreference] = UNSET
    under_offer_or_contract: Union[Unset, bool] = UNSET
    auction: Union[Unset, "DomainListingAdminServiceV1ModelAuction"] = UNSET
    bond: Union[Unset, int] = UNSET
    available_from: Union[Unset, datetime.datetime] = UNSET
    property_details: Union[Unset, "DomainListingAdminServiceV1ModelResidentialProperty"] = UNSET
    is_new_development: Union[Unset, bool] = UNSET
    statement_of_information: Union[Unset, "DomainListingAdminServiceV1ModelStatementOfInformation"] = UNSET
    price: Union[Unset, "DomainListingAdminServiceV1ModelPrice"] = UNSET
    project: Union[Unset, "DomainListingAdminServiceV1ModelListingProject"] = UNSET
    domain_ad_id: Union[Unset, int] = UNSET
    domain_agency_id: Union[Unset, int] = UNSET
    provider_ad_id: Union[Unset, str] = UNSET
    features: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    inspection_details: Union[Unset, "DomainListingAdminServiceV1ModelInspectionDetails"] = UNSET
    media: Union[Unset, List["DomainListingAdminServiceV1ModelPropertyMedia"]] = UNSET
    contacts: Union[Unset, List["DomainListingAdminServiceV1ModelContact"]] = UNSET
    other_enquiry_email: Union[Unset, str] = UNSET
    receive_emails_to_default_address: Union[Unset, bool] = UNSET
    is_rural: Union[Unset, bool] = UNSET
    supplementary: Union[Unset, List["DomainListingAdminServiceV1ModelListingSupplementary"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        life_style_type: Union[Unset, str] = UNSET
        if not isinstance(self.life_style_type, Unset):
            life_style_type = self.life_style_type.value

        listing_action: Union[Unset, str] = UNSET
        if not isinstance(self.listing_action, Unset):
            listing_action = self.listing_action.value

        contact_preference: Union[Unset, str] = UNSET
        if not isinstance(self.contact_preference, Unset):
            contact_preference = self.contact_preference.value

        under_offer_or_contract = self.under_offer_or_contract

        auction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auction, Unset):
            auction = self.auction.to_dict()

        bond = self.bond

        available_from: Union[Unset, str] = UNSET
        if not isinstance(self.available_from, Unset):
            available_from = self.available_from.isoformat()

        property_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_details, Unset):
            property_details = self.property_details.to_dict()

        is_new_development = self.is_new_development

        statement_of_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statement_of_information, Unset):
            statement_of_information = self.statement_of_information.to_dict()

        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        domain_ad_id = self.domain_ad_id

        domain_agency_id = self.domain_agency_id

        provider_ad_id = self.provider_ad_id

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
        field_dict.update({})
        if life_style_type is not UNSET:
            field_dict["lifeStyleType"] = life_style_type
        if listing_action is not UNSET:
            field_dict["listingAction"] = listing_action
        if contact_preference is not UNSET:
            field_dict["contactPreference"] = contact_preference
        if under_offer_or_contract is not UNSET:
            field_dict["underOfferOrContract"] = under_offer_or_contract
        if auction is not UNSET:
            field_dict["auction"] = auction
        if bond is not UNSET:
            field_dict["bond"] = bond
        if available_from is not UNSET:
            field_dict["availableFrom"] = available_from
        if property_details is not UNSET:
            field_dict["propertyDetails"] = property_details
        if is_new_development is not UNSET:
            field_dict["isNewDevelopment"] = is_new_development
        if statement_of_information is not UNSET:
            field_dict["statementOfInformation"] = statement_of_information
        if price is not UNSET:
            field_dict["price"] = price
        if project is not UNSET:
            field_dict["project"] = project
        if domain_ad_id is not UNSET:
            field_dict["domainAdId"] = domain_ad_id
        if domain_agency_id is not UNSET:
            field_dict["domainAgencyID"] = domain_agency_id
        if provider_ad_id is not UNSET:
            field_dict["providerAdId"] = provider_ad_id
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
        from ..models.domain_listing_admin_service_v1_model_auction import DomainListingAdminServiceV1ModelAuction
        from ..models.domain_listing_admin_service_v1_model_contact import DomainListingAdminServiceV1ModelContact
        from ..models.domain_listing_admin_service_v1_model_inspection_details import (
            DomainListingAdminServiceV1ModelInspectionDetails,
        )
        from ..models.domain_listing_admin_service_v1_model_listing_project import (
            DomainListingAdminServiceV1ModelListingProject,
        )
        from ..models.domain_listing_admin_service_v1_model_listing_supplementary import (
            DomainListingAdminServiceV1ModelListingSupplementary,
        )
        from ..models.domain_listing_admin_service_v1_model_price import DomainListingAdminServiceV1ModelPrice
        from ..models.domain_listing_admin_service_v1_model_property_media import (
            DomainListingAdminServiceV1ModelPropertyMedia,
        )
        from ..models.domain_listing_admin_service_v1_model_residential_property import (
            DomainListingAdminServiceV1ModelResidentialProperty,
        )
        from ..models.domain_listing_admin_service_v1_model_statement_of_information import (
            DomainListingAdminServiceV1ModelStatementOfInformation,
        )

        d = src_dict.copy()
        _life_style_type = d.pop("lifeStyleType", UNSET)
        life_style_type: Union[Unset, DomainListingAdminServiceV1ModelResidentialListingLifeStyleType]
        if isinstance(_life_style_type, Unset):
            life_style_type = UNSET
        else:
            life_style_type = DomainListingAdminServiceV1ModelResidentialListingLifeStyleType(_life_style_type)

        _listing_action = d.pop("listingAction", UNSET)
        listing_action: Union[Unset, DomainListingAdminServiceV1ModelResidentialListingListingAction]
        if isinstance(_listing_action, Unset):
            listing_action = UNSET
        else:
            listing_action = DomainListingAdminServiceV1ModelResidentialListingListingAction(_listing_action)

        _contact_preference = d.pop("contactPreference", UNSET)
        contact_preference: Union[Unset, DomainListingAdminServiceV1ModelResidentialListingContactPreference]
        if isinstance(_contact_preference, Unset):
            contact_preference = UNSET
        else:
            contact_preference = DomainListingAdminServiceV1ModelResidentialListingContactPreference(
                _contact_preference
            )

        under_offer_or_contract = d.pop("underOfferOrContract", UNSET)

        _auction = d.pop("auction", UNSET)
        auction: Union[Unset, DomainListingAdminServiceV1ModelAuction]
        if isinstance(_auction, Unset):
            auction = UNSET
        else:
            auction = DomainListingAdminServiceV1ModelAuction.from_dict(_auction)

        bond = d.pop("bond", UNSET)

        _available_from = d.pop("availableFrom", UNSET)
        available_from: Union[Unset, datetime.datetime]
        if isinstance(_available_from, Unset):
            available_from = UNSET
        else:
            available_from = isoparse(_available_from)

        _property_details = d.pop("propertyDetails", UNSET)
        property_details: Union[Unset, DomainListingAdminServiceV1ModelResidentialProperty]
        if isinstance(_property_details, Unset):
            property_details = UNSET
        else:
            property_details = DomainListingAdminServiceV1ModelResidentialProperty.from_dict(_property_details)

        is_new_development = d.pop("isNewDevelopment", UNSET)

        _statement_of_information = d.pop("statementOfInformation", UNSET)
        statement_of_information: Union[Unset, DomainListingAdminServiceV1ModelStatementOfInformation]
        if isinstance(_statement_of_information, Unset):
            statement_of_information = UNSET
        else:
            statement_of_information = DomainListingAdminServiceV1ModelStatementOfInformation.from_dict(
                _statement_of_information
            )

        _price = d.pop("price", UNSET)
        price: Union[Unset, DomainListingAdminServiceV1ModelPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = DomainListingAdminServiceV1ModelPrice.from_dict(_price)

        _project = d.pop("project", UNSET)
        project: Union[Unset, DomainListingAdminServiceV1ModelListingProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = DomainListingAdminServiceV1ModelListingProject.from_dict(_project)

        domain_ad_id = d.pop("domainAdId", UNSET)

        domain_agency_id = d.pop("domainAgencyID", UNSET)

        provider_ad_id = d.pop("providerAdId", UNSET)

        features = d.pop("features", UNSET)

        description = d.pop("description", UNSET)

        summary = d.pop("summary", UNSET)

        _inspection_details = d.pop("inspectionDetails", UNSET)
        inspection_details: Union[Unset, DomainListingAdminServiceV1ModelInspectionDetails]
        if isinstance(_inspection_details, Unset):
            inspection_details = UNSET
        else:
            inspection_details = DomainListingAdminServiceV1ModelInspectionDetails.from_dict(_inspection_details)

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = DomainListingAdminServiceV1ModelPropertyMedia.from_dict(media_item_data)

            media.append(media_item)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = DomainListingAdminServiceV1ModelContact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        other_enquiry_email = d.pop("otherEnquiryEmail", UNSET)

        receive_emails_to_default_address = d.pop("receiveEmailsToDefaultAddress", UNSET)

        is_rural = d.pop("isRural", UNSET)

        supplementary = []
        _supplementary = d.pop("supplementary", UNSET)
        for supplementary_item_data in _supplementary or []:
            supplementary_item = DomainListingAdminServiceV1ModelListingSupplementary.from_dict(supplementary_item_data)

            supplementary.append(supplementary_item)

        domain_listing_admin_service_v1_model_residential_listing = cls(
            life_style_type=life_style_type,
            listing_action=listing_action,
            contact_preference=contact_preference,
            under_offer_or_contract=under_offer_or_contract,
            auction=auction,
            bond=bond,
            available_from=available_from,
            property_details=property_details,
            is_new_development=is_new_development,
            statement_of_information=statement_of_information,
            price=price,
            project=project,
            domain_ad_id=domain_ad_id,
            domain_agency_id=domain_agency_id,
            provider_ad_id=provider_ad_id,
            features=features,
            description=description,
            summary=summary,
            inspection_details=inspection_details,
            media=media,
            contacts=contacts,
            other_enquiry_email=other_enquiry_email,
            receive_emails_to_default_address=receive_emails_to_default_address,
            is_rural=is_rural,
            supplementary=supplementary,
        )

        domain_listing_admin_service_v1_model_residential_listing.additional_properties = d
        return domain_listing_admin_service_v1_model_residential_listing

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
