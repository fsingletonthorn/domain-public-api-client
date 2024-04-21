import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.pre_market_v1_authority_type import PreMarketV1AuthorityType
from ..models.pre_market_v1_pre_portal_listing_status import PreMarketV1PrePortalListingStatus
from ..models.pre_market_v1_property_type import PreMarketV1PropertyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pre_market_v1_address import PreMarketV1Address
    from ..models.pre_market_v1_contact import PreMarketV1Contact
    from ..models.pre_market_v1_listing_request_metadata_type_0 import PreMarketV1ListingRequestMetadataType0
    from ..models.pre_market_v1_price import PreMarketV1Price
    from ..models.pre_market_v1_property_media import PreMarketV1PropertyMedia
    from ..models.pre_market_v1_sold_details import PreMarketV1SoldDetails
    from ..models.pre_market_v1_statement_of_information import PreMarketV1StatementOfInformation


T = TypeVar("T", bound="PreMarketV1ListingRequest")


@_attrs_define
class PreMarketV1ListingRequest:
    """Pre-portal listing request.

    Attributes:
        listing_status (PreMarketV1PrePortalListingStatus):
        address (PreMarketV1Address):
        domain_agency_id (int): The Domain agency ID. Must match an existing Domain agency ID.
        listing_provider (str): A string identifying the source of the listing.
        provider_ad_id (str): External Advertisement Id of up to 50 characters will be stored.
            This value is correlated with actual Domain listing when it is created, and it should be unique for the listing
            provider.
            This value is case-insensitive (meaning AAAA will update aaaa).
        bedrooms (float): Number of bedrooms divisible by 0.5.
        bathrooms (float): Number of bathrooms divisible by 0.5.
        carspaces (float): Number of car spaces divisible by 0.5.
        estimated_sale_price (PreMarketV1Price):
        property_types (List[PreMarketV1PropertyType]): The property types (e.g. house, apartment/unit/flat, etc.).
        contacts (Union[List['PreMarketV1Contact'], None, Unset]):
        summary (Union[None, Unset, str]): Headline of the advertisement. Any HTML will be stripped out.
        description (Union[None, Unset, str]): Description of the property.
            Allow up to 6000 characters in length. The following HTML elements are permitted: ```<br />, <p></p>, &nbsp;```
            . HTML must be well-formed.
            Carriage Returns are interpreted as line breaks. Foreign characters must be HTML encoded, e.g., façade for
            façade
        authority_executed_date (Union[None, Unset, datetime.datetime]): The date on which the authority contract was
            executed.
            The date must comply with the ISO 8601 and be in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        reserve_price (Union[None, Unset, float]): Vendor reserve price.
        authority_type (Union[Unset, PreMarketV1AuthorityType]):
        exclusive_period_days (Union[None, Unset, int]): The time (in days) that the agent has exclusive authority to
            sell the property.
        exclusive_continuing_period_days (Union[None, Unset, int]): The time (in days) that exclusive authority has been
            extended.
        exclusive_period_start_date (Union[None, Unset, datetime.datetime]): Start date of the exclusivity period.
            The date must comply with the ISO 8601 and be in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        statement_of_information (Union[Unset, PreMarketV1StatementOfInformation]):
        images (Union[List['PreMarketV1PropertyMedia'], None, Unset]):
        metadata (Union['PreMarketV1ListingRequestMetadataType0', None, Unset]): Optional listing metadata.
        comment (Union[None, Unset, str]): Optional listing comment.
        sold_details (Union[Unset, PreMarketV1SoldDetails]):
    """

    listing_status: PreMarketV1PrePortalListingStatus
    address: "PreMarketV1Address"
    domain_agency_id: int
    listing_provider: str
    provider_ad_id: str
    bedrooms: float
    bathrooms: float
    carspaces: float
    estimated_sale_price: "PreMarketV1Price"
    property_types: List[PreMarketV1PropertyType]
    contacts: Union[List["PreMarketV1Contact"], None, Unset] = UNSET
    summary: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    authority_executed_date: Union[None, Unset, datetime.datetime] = UNSET
    reserve_price: Union[None, Unset, float] = UNSET
    authority_type: Union[Unset, PreMarketV1AuthorityType] = UNSET
    exclusive_period_days: Union[None, Unset, int] = UNSET
    exclusive_continuing_period_days: Union[None, Unset, int] = UNSET
    exclusive_period_start_date: Union[None, Unset, datetime.datetime] = UNSET
    statement_of_information: Union[Unset, "PreMarketV1StatementOfInformation"] = UNSET
    images: Union[List["PreMarketV1PropertyMedia"], None, Unset] = UNSET
    metadata: Union["PreMarketV1ListingRequestMetadataType0", None, Unset] = UNSET
    comment: Union[None, Unset, str] = UNSET
    sold_details: Union[Unset, "PreMarketV1SoldDetails"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pre_market_v1_listing_request_metadata_type_0 import PreMarketV1ListingRequestMetadataType0

        listing_status = self.listing_status.value

        address = self.address.to_dict()

        domain_agency_id = self.domain_agency_id

        listing_provider = self.listing_provider

        provider_ad_id = self.provider_ad_id

        bedrooms = self.bedrooms

        bathrooms = self.bathrooms

        carspaces = self.carspaces

        estimated_sale_price = self.estimated_sale_price.to_dict()

        property_types = []
        for property_types_item_data in self.property_types:
            property_types_item = property_types_item_data.value
            property_types.append(property_types_item)

        contacts: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.contacts, Unset):
            contacts = UNSET
        elif isinstance(self.contacts, list):
            contacts = []
            for contacts_type_0_item_data in self.contacts:
                contacts_type_0_item = contacts_type_0_item_data.to_dict()
                contacts.append(contacts_type_0_item)

        else:
            contacts = self.contacts

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        authority_executed_date: Union[None, Unset, str]
        if isinstance(self.authority_executed_date, Unset):
            authority_executed_date = UNSET
        elif isinstance(self.authority_executed_date, datetime.datetime):
            authority_executed_date = self.authority_executed_date.isoformat()
        else:
            authority_executed_date = self.authority_executed_date

        reserve_price: Union[None, Unset, float]
        if isinstance(self.reserve_price, Unset):
            reserve_price = UNSET
        else:
            reserve_price = self.reserve_price

        authority_type: Union[Unset, str] = UNSET
        if not isinstance(self.authority_type, Unset):
            authority_type = self.authority_type.value

        exclusive_period_days: Union[None, Unset, int]
        if isinstance(self.exclusive_period_days, Unset):
            exclusive_period_days = UNSET
        else:
            exclusive_period_days = self.exclusive_period_days

        exclusive_continuing_period_days: Union[None, Unset, int]
        if isinstance(self.exclusive_continuing_period_days, Unset):
            exclusive_continuing_period_days = UNSET
        else:
            exclusive_continuing_period_days = self.exclusive_continuing_period_days

        exclusive_period_start_date: Union[None, Unset, str]
        if isinstance(self.exclusive_period_start_date, Unset):
            exclusive_period_start_date = UNSET
        elif isinstance(self.exclusive_period_start_date, datetime.datetime):
            exclusive_period_start_date = self.exclusive_period_start_date.isoformat()
        else:
            exclusive_period_start_date = self.exclusive_period_start_date

        statement_of_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statement_of_information, Unset):
            statement_of_information = self.statement_of_information.to_dict()

        images: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        metadata: Union[Dict[str, Any], None, Unset]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PreMarketV1ListingRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        sold_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sold_details, Unset):
            sold_details = self.sold_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "listingStatus": listing_status,
                "address": address,
                "domainAgencyId": domain_agency_id,
                "listingProvider": listing_provider,
                "providerAdId": provider_ad_id,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "carspaces": carspaces,
                "estimatedSalePrice": estimated_sale_price,
                "propertyTypes": property_types,
            }
        )
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if authority_executed_date is not UNSET:
            field_dict["authorityExecutedDate"] = authority_executed_date
        if reserve_price is not UNSET:
            field_dict["reservePrice"] = reserve_price
        if authority_type is not UNSET:
            field_dict["authorityType"] = authority_type
        if exclusive_period_days is not UNSET:
            field_dict["exclusivePeriodDays"] = exclusive_period_days
        if exclusive_continuing_period_days is not UNSET:
            field_dict["exclusiveContinuingPeriodDays"] = exclusive_continuing_period_days
        if exclusive_period_start_date is not UNSET:
            field_dict["exclusivePeriodStartDate"] = exclusive_period_start_date
        if statement_of_information is not UNSET:
            field_dict["statementOfInformation"] = statement_of_information
        if images is not UNSET:
            field_dict["images"] = images
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if comment is not UNSET:
            field_dict["comment"] = comment
        if sold_details is not UNSET:
            field_dict["soldDetails"] = sold_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pre_market_v1_address import PreMarketV1Address
        from ..models.pre_market_v1_contact import PreMarketV1Contact
        from ..models.pre_market_v1_listing_request_metadata_type_0 import PreMarketV1ListingRequestMetadataType0
        from ..models.pre_market_v1_price import PreMarketV1Price
        from ..models.pre_market_v1_property_media import PreMarketV1PropertyMedia
        from ..models.pre_market_v1_sold_details import PreMarketV1SoldDetails
        from ..models.pre_market_v1_statement_of_information import PreMarketV1StatementOfInformation

        d = src_dict.copy()
        listing_status = PreMarketV1PrePortalListingStatus(d.pop("listingStatus"))

        address = PreMarketV1Address.from_dict(d.pop("address"))

        domain_agency_id = d.pop("domainAgencyId")

        listing_provider = d.pop("listingProvider")

        provider_ad_id = d.pop("providerAdId")

        bedrooms = d.pop("bedrooms")

        bathrooms = d.pop("bathrooms")

        carspaces = d.pop("carspaces")

        estimated_sale_price = PreMarketV1Price.from_dict(d.pop("estimatedSalePrice"))

        property_types = []
        _property_types = d.pop("propertyTypes")
        for property_types_item_data in _property_types:
            property_types_item = PreMarketV1PropertyType(property_types_item_data)

            property_types.append(property_types_item)

        def _parse_contacts(data: object) -> Union[List["PreMarketV1Contact"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contacts_type_0 = []
                _contacts_type_0 = data
                for contacts_type_0_item_data in _contacts_type_0:
                    contacts_type_0_item = PreMarketV1Contact.from_dict(contacts_type_0_item_data)

                    contacts_type_0.append(contacts_type_0_item)

                return contacts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PreMarketV1Contact"], None, Unset], data)

        contacts = _parse_contacts(d.pop("contacts", UNSET))

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_authority_executed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authority_executed_date_type_0 = isoparse(data)

                return authority_executed_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        authority_executed_date = _parse_authority_executed_date(d.pop("authorityExecutedDate", UNSET))

        def _parse_reserve_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        reserve_price = _parse_reserve_price(d.pop("reservePrice", UNSET))

        _authority_type = d.pop("authorityType", UNSET)
        authority_type: Union[Unset, PreMarketV1AuthorityType]
        if isinstance(_authority_type, Unset):
            authority_type = UNSET
        else:
            authority_type = PreMarketV1AuthorityType(_authority_type)

        def _parse_exclusive_period_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        exclusive_period_days = _parse_exclusive_period_days(d.pop("exclusivePeriodDays", UNSET))

        def _parse_exclusive_continuing_period_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        exclusive_continuing_period_days = _parse_exclusive_continuing_period_days(
            d.pop("exclusiveContinuingPeriodDays", UNSET)
        )

        def _parse_exclusive_period_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exclusive_period_start_date_type_0 = isoparse(data)

                return exclusive_period_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        exclusive_period_start_date = _parse_exclusive_period_start_date(d.pop("exclusivePeriodStartDate", UNSET))

        _statement_of_information = d.pop("statementOfInformation", UNSET)
        statement_of_information: Union[Unset, PreMarketV1StatementOfInformation]
        if isinstance(_statement_of_information, Unset):
            statement_of_information = UNSET
        else:
            statement_of_information = PreMarketV1StatementOfInformation.from_dict(_statement_of_information)

        def _parse_images(data: object) -> Union[List["PreMarketV1PropertyMedia"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = PreMarketV1PropertyMedia.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PreMarketV1PropertyMedia"], None, Unset], data)

        images = _parse_images(d.pop("images", UNSET))

        def _parse_metadata(data: object) -> Union["PreMarketV1ListingRequestMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PreMarketV1ListingRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PreMarketV1ListingRequestMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        _sold_details = d.pop("soldDetails", UNSET)
        sold_details: Union[Unset, PreMarketV1SoldDetails]
        if isinstance(_sold_details, Unset):
            sold_details = UNSET
        else:
            sold_details = PreMarketV1SoldDetails.from_dict(_sold_details)

        pre_market_v1_listing_request = cls(
            listing_status=listing_status,
            address=address,
            domain_agency_id=domain_agency_id,
            listing_provider=listing_provider,
            provider_ad_id=provider_ad_id,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            carspaces=carspaces,
            estimated_sale_price=estimated_sale_price,
            property_types=property_types,
            contacts=contacts,
            summary=summary,
            description=description,
            authority_executed_date=authority_executed_date,
            reserve_price=reserve_price,
            authority_type=authority_type,
            exclusive_period_days=exclusive_period_days,
            exclusive_continuing_period_days=exclusive_continuing_period_days,
            exclusive_period_start_date=exclusive_period_start_date,
            statement_of_information=statement_of_information,
            images=images,
            metadata=metadata,
            comment=comment,
            sold_details=sold_details,
        )

        return pre_market_v1_listing_request
