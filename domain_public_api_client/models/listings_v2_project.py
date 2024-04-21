import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.listings_v2_project_category import ListingsV2ProjectCategory
from ..models.listings_v2_project_estimated_completion_tertile import ListingsV2ProjectEstimatedCompletionTertile
from ..models.listings_v2_project_project_profile_type import ListingsV2ProjectProjectProfileType
from ..models.listings_v2_project_property_types_type_0_item import ListingsV2ProjectPropertyTypesType0Item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_v2_advertiser_identifiers import ListingsV2AdvertiserIdentifiers
    from ..models.listings_v2_pdf_upload import ListingsV2PdfUpload
    from ..models.listings_v2_project_address_parts import ListingsV2ProjectAddressParts
    from ..models.listings_v2_project_media import ListingsV2ProjectMedia
    from ..models.listings_v2_property_inspections import ListingsV2PropertyInspections
    from ..models.listings_v2_provider_details import ListingsV2ProviderDetails


T = TypeVar("T", bound="ListingsV2Project")


@_attrs_define
class ListingsV2Project:
    """A structured representation of a Project

    Attributes:
        project_profile_type (Union[Unset, ListingsV2ProjectProjectProfileType]): Gets or Sets ProjectProfileType
        estimated_completion_tertile (Union[Unset, ListingsV2ProjectEstimatedCompletionTertile]): Gets or Sets
            EstimatedCompletionTertile
        category (Union[Unset, ListingsV2ProjectCategory]): Gets or Sets Category
        id (Union[None, Unset, int]): Project ID
        name (Union[None, Unset, str]): Project Name
        start_date (Union[None, Unset, datetime.datetime]): Start date. DateTime is in a local timezone.
        end_date (Union[None, Unset, datetime.datetime]): End date.DateTime is in a local timezone.
        address (Union[Unset, ListingsV2ProjectAddressParts]): Project address parts
        viewing_address (Union[Unset, ListingsV2ProjectAddressParts]): Project address parts
        property_types (Union[List[ListingsV2ProjectPropertyTypesType0Item], None, Unset]): Property types available at
            the project.
        displayable_address (Union[Unset, ListingsV2ProjectAddressParts]): Project address parts
        enquiry_email_address (Union[None, Unset, str]): Enquiry email address
        advertiser_identifiers (Union[Unset, ListingsV2AdvertiserIdentifiers]): Encapsulates the listing's advertiser
            identifiers
        provider_details (Union[Unset, ListingsV2ProviderDetails]): Information for the listing provider. e.g.
            bulkuploader information
        media (Union[List['ListingsV2ProjectMedia'], None, Unset]): Images and videos
        project_url (Union[None, Unset, str]): Project URL
        headline (Union[None, Unset, str]): Headline
        tagline (Union[None, Unset, str]): Tag line
        display_as_last_updated (Union[None, Unset, datetime.datetime]): The 'last updated' date to show to customers.
            DateTime is in AEST (Australian Eastern Standard Time) or AEDT (Australian Eastern Daylight Time) timezone.
        modified_by (Union[None, Unset, str]): Last updated by
        modified_date (Union[None, Unset, datetime.datetime]): Last updated, used for auditing. DateTime is in AEST
            (Australian Eastern Standard Time) or AEDT (Australian Eastern Daylight Time) timezone.
        created_by (Union[None, Unset, str]): Created by
        created_date (Union[None, Unset, datetime.datetime]): Created date. DateTime is in AEST (Australian Eastern
            Standard Time) or AEDT (Australian Eastern Daylight Time) timezone.
        background_colour (Union[None, Unset, str]): Background colour
        description (Union[None, Unset, str]): Description
        appointment_required (Union[None, Unset, bool]): If inspections require an appointment.
        features (Union[List[str], None, Unset]): Features
        price_from (Union[None, Unset, float]): Price from
        price_to (Union[None, Unset, float]): Price to
        banner_url (Union[None, Unset, str]): Banner URL
        big_banner_url (Union[None, Unset, str]): Big banner URL
        small_banner_url (Union[None, Unset, str]): Small banner URL
        logo_url (Union[None, Unset, str]): Logo URL
        pdfs (Union[List['ListingsV2PdfUpload'], None, Unset]): PDF files, such as brochures etc.
        inspection_details (Union[Unset, ListingsV2PropertyInspections]): Property Inspection(s) details
        number_of_floors (Union[None, Unset, int]): Maximum number of floors
        min_number_of_floors (Union[None, Unset, int]): Minimum number of floors
        min_building_height (Union[None, Unset, int]): Minimum building height
        max_building_height (Union[None, Unset, int]): Maximum building height
        number_of_buildings (Union[None, Unset, int]): Number of buildings
        number_of_apartments (Union[None, Unset, int]): Number of apartments
        estimated_completion_date (Union[None, Unset, datetime.datetime]): Estimated completion date. DateTime in a
            local timezone.
        starting_price (Union[None, Unset, float]): Lowest child listing price
        child_listing_ids (Union[List[int], None, Unset]): Child listing identifiers.
        linked_project_ids (Union[List[int], None, Unset]): Linked project identifiers.
    """

    project_profile_type: Union[Unset, ListingsV2ProjectProjectProfileType] = UNSET
    estimated_completion_tertile: Union[Unset, ListingsV2ProjectEstimatedCompletionTertile] = UNSET
    category: Union[Unset, ListingsV2ProjectCategory] = UNSET
    id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    start_date: Union[None, Unset, datetime.datetime] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    address: Union[Unset, "ListingsV2ProjectAddressParts"] = UNSET
    viewing_address: Union[Unset, "ListingsV2ProjectAddressParts"] = UNSET
    property_types: Union[List[ListingsV2ProjectPropertyTypesType0Item], None, Unset] = UNSET
    displayable_address: Union[Unset, "ListingsV2ProjectAddressParts"] = UNSET
    enquiry_email_address: Union[None, Unset, str] = UNSET
    advertiser_identifiers: Union[Unset, "ListingsV2AdvertiserIdentifiers"] = UNSET
    provider_details: Union[Unset, "ListingsV2ProviderDetails"] = UNSET
    media: Union[List["ListingsV2ProjectMedia"], None, Unset] = UNSET
    project_url: Union[None, Unset, str] = UNSET
    headline: Union[None, Unset, str] = UNSET
    tagline: Union[None, Unset, str] = UNSET
    display_as_last_updated: Union[None, Unset, datetime.datetime] = UNSET
    modified_by: Union[None, Unset, str] = UNSET
    modified_date: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    created_date: Union[None, Unset, datetime.datetime] = UNSET
    background_colour: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    appointment_required: Union[None, Unset, bool] = UNSET
    features: Union[List[str], None, Unset] = UNSET
    price_from: Union[None, Unset, float] = UNSET
    price_to: Union[None, Unset, float] = UNSET
    banner_url: Union[None, Unset, str] = UNSET
    big_banner_url: Union[None, Unset, str] = UNSET
    small_banner_url: Union[None, Unset, str] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    pdfs: Union[List["ListingsV2PdfUpload"], None, Unset] = UNSET
    inspection_details: Union[Unset, "ListingsV2PropertyInspections"] = UNSET
    number_of_floors: Union[None, Unset, int] = UNSET
    min_number_of_floors: Union[None, Unset, int] = UNSET
    min_building_height: Union[None, Unset, int] = UNSET
    max_building_height: Union[None, Unset, int] = UNSET
    number_of_buildings: Union[None, Unset, int] = UNSET
    number_of_apartments: Union[None, Unset, int] = UNSET
    estimated_completion_date: Union[None, Unset, datetime.datetime] = UNSET
    starting_price: Union[None, Unset, float] = UNSET
    child_listing_ids: Union[List[int], None, Unset] = UNSET
    linked_project_ids: Union[List[int], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_profile_type: Union[Unset, str] = UNSET
        if not isinstance(self.project_profile_type, Unset):
            project_profile_type = self.project_profile_type.value

        estimated_completion_tertile: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_completion_tertile, Unset):
            estimated_completion_tertile = self.estimated_completion_tertile.value

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        viewing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.viewing_address, Unset):
            viewing_address = self.viewing_address.to_dict()

        property_types: Union[List[str], None, Unset]
        if isinstance(self.property_types, Unset):
            property_types = UNSET
        elif isinstance(self.property_types, list):
            property_types = []
            for property_types_type_0_item_data in self.property_types:
                property_types_type_0_item = property_types_type_0_item_data.value
                property_types.append(property_types_type_0_item)

        else:
            property_types = self.property_types

        displayable_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.displayable_address, Unset):
            displayable_address = self.displayable_address.to_dict()

        enquiry_email_address: Union[None, Unset, str]
        if isinstance(self.enquiry_email_address, Unset):
            enquiry_email_address = UNSET
        else:
            enquiry_email_address = self.enquiry_email_address

        advertiser_identifiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advertiser_identifiers, Unset):
            advertiser_identifiers = self.advertiser_identifiers.to_dict()

        provider_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_details, Unset):
            provider_details = self.provider_details.to_dict()

        media: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.media, Unset):
            media = UNSET
        elif isinstance(self.media, list):
            media = []
            for media_type_0_item_data in self.media:
                media_type_0_item = media_type_0_item_data.to_dict()
                media.append(media_type_0_item)

        else:
            media = self.media

        project_url: Union[None, Unset, str]
        if isinstance(self.project_url, Unset):
            project_url = UNSET
        else:
            project_url = self.project_url

        headline: Union[None, Unset, str]
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        tagline: Union[None, Unset, str]
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        display_as_last_updated: Union[None, Unset, str]
        if isinstance(self.display_as_last_updated, Unset):
            display_as_last_updated = UNSET
        elif isinstance(self.display_as_last_updated, datetime.datetime):
            display_as_last_updated = self.display_as_last_updated.isoformat()
        else:
            display_as_last_updated = self.display_as_last_updated

        modified_by: Union[None, Unset, str]
        if isinstance(self.modified_by, Unset):
            modified_by = UNSET
        else:
            modified_by = self.modified_by

        modified_date: Union[None, Unset, str]
        if isinstance(self.modified_date, Unset):
            modified_date = UNSET
        elif isinstance(self.modified_date, datetime.datetime):
            modified_date = self.modified_date.isoformat()
        else:
            modified_date = self.modified_date

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        created_date: Union[None, Unset, str]
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        background_colour: Union[None, Unset, str]
        if isinstance(self.background_colour, Unset):
            background_colour = UNSET
        else:
            background_colour = self.background_colour

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        appointment_required: Union[None, Unset, bool]
        if isinstance(self.appointment_required, Unset):
            appointment_required = UNSET
        else:
            appointment_required = self.appointment_required

        features: Union[List[str], None, Unset]
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, list):
            features = self.features

        else:
            features = self.features

        price_from: Union[None, Unset, float]
        if isinstance(self.price_from, Unset):
            price_from = UNSET
        else:
            price_from = self.price_from

        price_to: Union[None, Unset, float]
        if isinstance(self.price_to, Unset):
            price_to = UNSET
        else:
            price_to = self.price_to

        banner_url: Union[None, Unset, str]
        if isinstance(self.banner_url, Unset):
            banner_url = UNSET
        else:
            banner_url = self.banner_url

        big_banner_url: Union[None, Unset, str]
        if isinstance(self.big_banner_url, Unset):
            big_banner_url = UNSET
        else:
            big_banner_url = self.big_banner_url

        small_banner_url: Union[None, Unset, str]
        if isinstance(self.small_banner_url, Unset):
            small_banner_url = UNSET
        else:
            small_banner_url = self.small_banner_url

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        pdfs: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.pdfs, Unset):
            pdfs = UNSET
        elif isinstance(self.pdfs, list):
            pdfs = []
            for pdfs_type_0_item_data in self.pdfs:
                pdfs_type_0_item = pdfs_type_0_item_data.to_dict()
                pdfs.append(pdfs_type_0_item)

        else:
            pdfs = self.pdfs

        inspection_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inspection_details, Unset):
            inspection_details = self.inspection_details.to_dict()

        number_of_floors: Union[None, Unset, int]
        if isinstance(self.number_of_floors, Unset):
            number_of_floors = UNSET
        else:
            number_of_floors = self.number_of_floors

        min_number_of_floors: Union[None, Unset, int]
        if isinstance(self.min_number_of_floors, Unset):
            min_number_of_floors = UNSET
        else:
            min_number_of_floors = self.min_number_of_floors

        min_building_height: Union[None, Unset, int]
        if isinstance(self.min_building_height, Unset):
            min_building_height = UNSET
        else:
            min_building_height = self.min_building_height

        max_building_height: Union[None, Unset, int]
        if isinstance(self.max_building_height, Unset):
            max_building_height = UNSET
        else:
            max_building_height = self.max_building_height

        number_of_buildings: Union[None, Unset, int]
        if isinstance(self.number_of_buildings, Unset):
            number_of_buildings = UNSET
        else:
            number_of_buildings = self.number_of_buildings

        number_of_apartments: Union[None, Unset, int]
        if isinstance(self.number_of_apartments, Unset):
            number_of_apartments = UNSET
        else:
            number_of_apartments = self.number_of_apartments

        estimated_completion_date: Union[None, Unset, str]
        if isinstance(self.estimated_completion_date, Unset):
            estimated_completion_date = UNSET
        elif isinstance(self.estimated_completion_date, datetime.datetime):
            estimated_completion_date = self.estimated_completion_date.isoformat()
        else:
            estimated_completion_date = self.estimated_completion_date

        starting_price: Union[None, Unset, float]
        if isinstance(self.starting_price, Unset):
            starting_price = UNSET
        else:
            starting_price = self.starting_price

        child_listing_ids: Union[List[int], None, Unset]
        if isinstance(self.child_listing_ids, Unset):
            child_listing_ids = UNSET
        elif isinstance(self.child_listing_ids, list):
            child_listing_ids = self.child_listing_ids

        else:
            child_listing_ids = self.child_listing_ids

        linked_project_ids: Union[List[int], None, Unset]
        if isinstance(self.linked_project_ids, Unset):
            linked_project_ids = UNSET
        elif isinstance(self.linked_project_ids, list):
            linked_project_ids = self.linked_project_ids

        else:
            linked_project_ids = self.linked_project_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_profile_type is not UNSET:
            field_dict["projectProfileType"] = project_profile_type
        if estimated_completion_tertile is not UNSET:
            field_dict["estimatedCompletionTertile"] = estimated_completion_tertile
        if category is not UNSET:
            field_dict["category"] = category
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if address is not UNSET:
            field_dict["address"] = address
        if viewing_address is not UNSET:
            field_dict["viewingAddress"] = viewing_address
        if property_types is not UNSET:
            field_dict["propertyTypes"] = property_types
        if displayable_address is not UNSET:
            field_dict["displayableAddress"] = displayable_address
        if enquiry_email_address is not UNSET:
            field_dict["enquiryEmailAddress"] = enquiry_email_address
        if advertiser_identifiers is not UNSET:
            field_dict["advertiserIdentifiers"] = advertiser_identifiers
        if provider_details is not UNSET:
            field_dict["providerDetails"] = provider_details
        if media is not UNSET:
            field_dict["media"] = media
        if project_url is not UNSET:
            field_dict["projectUrl"] = project_url
        if headline is not UNSET:
            field_dict["headline"] = headline
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if display_as_last_updated is not UNSET:
            field_dict["displayAsLastUpdated"] = display_as_last_updated
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if background_colour is not UNSET:
            field_dict["backgroundColour"] = background_colour
        if description is not UNSET:
            field_dict["description"] = description
        if appointment_required is not UNSET:
            field_dict["appointmentRequired"] = appointment_required
        if features is not UNSET:
            field_dict["features"] = features
        if price_from is not UNSET:
            field_dict["priceFrom"] = price_from
        if price_to is not UNSET:
            field_dict["priceTo"] = price_to
        if banner_url is not UNSET:
            field_dict["bannerUrl"] = banner_url
        if big_banner_url is not UNSET:
            field_dict["bigBannerUrl"] = big_banner_url
        if small_banner_url is not UNSET:
            field_dict["smallBannerUrl"] = small_banner_url
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if pdfs is not UNSET:
            field_dict["pdfs"] = pdfs
        if inspection_details is not UNSET:
            field_dict["inspectionDetails"] = inspection_details
        if number_of_floors is not UNSET:
            field_dict["numberOfFloors"] = number_of_floors
        if min_number_of_floors is not UNSET:
            field_dict["minNumberOfFloors"] = min_number_of_floors
        if min_building_height is not UNSET:
            field_dict["minBuildingHeight"] = min_building_height
        if max_building_height is not UNSET:
            field_dict["maxBuildingHeight"] = max_building_height
        if number_of_buildings is not UNSET:
            field_dict["numberOfBuildings"] = number_of_buildings
        if number_of_apartments is not UNSET:
            field_dict["numberOfApartments"] = number_of_apartments
        if estimated_completion_date is not UNSET:
            field_dict["estimatedCompletionDate"] = estimated_completion_date
        if starting_price is not UNSET:
            field_dict["startingPrice"] = starting_price
        if child_listing_ids is not UNSET:
            field_dict["childListingIds"] = child_listing_ids
        if linked_project_ids is not UNSET:
            field_dict["linkedProjectIds"] = linked_project_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listings_v2_advertiser_identifiers import ListingsV2AdvertiserIdentifiers
        from ..models.listings_v2_pdf_upload import ListingsV2PdfUpload
        from ..models.listings_v2_project_address_parts import ListingsV2ProjectAddressParts
        from ..models.listings_v2_project_media import ListingsV2ProjectMedia
        from ..models.listings_v2_property_inspections import ListingsV2PropertyInspections
        from ..models.listings_v2_provider_details import ListingsV2ProviderDetails

        d = src_dict.copy()
        _project_profile_type = d.pop("projectProfileType", UNSET)
        project_profile_type: Union[Unset, ListingsV2ProjectProjectProfileType]
        if isinstance(_project_profile_type, Unset):
            project_profile_type = UNSET
        else:
            project_profile_type = ListingsV2ProjectProjectProfileType(_project_profile_type)

        _estimated_completion_tertile = d.pop("estimatedCompletionTertile", UNSET)
        estimated_completion_tertile: Union[Unset, ListingsV2ProjectEstimatedCompletionTertile]
        if isinstance(_estimated_completion_tertile, Unset):
            estimated_completion_tertile = UNSET
        else:
            estimated_completion_tertile = ListingsV2ProjectEstimatedCompletionTertile(_estimated_completion_tertile)

        _category = d.pop("category", UNSET)
        category: Union[Unset, ListingsV2ProjectCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ListingsV2ProjectCategory(_category)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        _address = d.pop("address", UNSET)
        address: Union[Unset, ListingsV2ProjectAddressParts]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = ListingsV2ProjectAddressParts.from_dict(_address)

        _viewing_address = d.pop("viewingAddress", UNSET)
        viewing_address: Union[Unset, ListingsV2ProjectAddressParts]
        if isinstance(_viewing_address, Unset):
            viewing_address = UNSET
        else:
            viewing_address = ListingsV2ProjectAddressParts.from_dict(_viewing_address)

        def _parse_property_types(data: object) -> Union[List[ListingsV2ProjectPropertyTypesType0Item], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                property_types_type_0 = []
                _property_types_type_0 = data
                for property_types_type_0_item_data in _property_types_type_0:
                    property_types_type_0_item = ListingsV2ProjectPropertyTypesType0Item(
                        property_types_type_0_item_data
                    )

                    property_types_type_0.append(property_types_type_0_item)

                return property_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[ListingsV2ProjectPropertyTypesType0Item], None, Unset], data)

        property_types = _parse_property_types(d.pop("propertyTypes", UNSET))

        _displayable_address = d.pop("displayableAddress", UNSET)
        displayable_address: Union[Unset, ListingsV2ProjectAddressParts]
        if isinstance(_displayable_address, Unset):
            displayable_address = UNSET
        else:
            displayable_address = ListingsV2ProjectAddressParts.from_dict(_displayable_address)

        def _parse_enquiry_email_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        enquiry_email_address = _parse_enquiry_email_address(d.pop("enquiryEmailAddress", UNSET))

        _advertiser_identifiers = d.pop("advertiserIdentifiers", UNSET)
        advertiser_identifiers: Union[Unset, ListingsV2AdvertiserIdentifiers]
        if isinstance(_advertiser_identifiers, Unset):
            advertiser_identifiers = UNSET
        else:
            advertiser_identifiers = ListingsV2AdvertiserIdentifiers.from_dict(_advertiser_identifiers)

        _provider_details = d.pop("providerDetails", UNSET)
        provider_details: Union[Unset, ListingsV2ProviderDetails]
        if isinstance(_provider_details, Unset):
            provider_details = UNSET
        else:
            provider_details = ListingsV2ProviderDetails.from_dict(_provider_details)

        def _parse_media(data: object) -> Union[List["ListingsV2ProjectMedia"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_type_0 = []
                _media_type_0 = data
                for media_type_0_item_data in _media_type_0:
                    media_type_0_item = ListingsV2ProjectMedia.from_dict(media_type_0_item_data)

                    media_type_0.append(media_type_0_item)

                return media_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingsV2ProjectMedia"], None, Unset], data)

        media = _parse_media(d.pop("media", UNSET))

        def _parse_project_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project_url = _parse_project_url(d.pop("projectUrl", UNSET))

        def _parse_headline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_tagline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))

        def _parse_display_as_last_updated(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                display_as_last_updated_type_0 = isoparse(data)

                return display_as_last_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        display_as_last_updated = _parse_display_as_last_updated(d.pop("displayAsLastUpdated", UNSET))

        def _parse_modified_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        modified_by = _parse_modified_by(d.pop("modifiedBy", UNSET))

        def _parse_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_date_type_0 = isoparse(data)

                return modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        modified_date = _parse_modified_date(d.pop("modifiedDate", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        def _parse_created_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_date = _parse_created_date(d.pop("createdDate", UNSET))

        def _parse_background_colour(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        background_colour = _parse_background_colour(d.pop("backgroundColour", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_appointment_required(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        appointment_required = _parse_appointment_required(d.pop("appointmentRequired", UNSET))

        def _parse_features(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                features_type_0 = cast(List[str], data)

                return features_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        features = _parse_features(d.pop("features", UNSET))

        def _parse_price_from(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price_from = _parse_price_from(d.pop("priceFrom", UNSET))

        def _parse_price_to(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price_to = _parse_price_to(d.pop("priceTo", UNSET))

        def _parse_banner_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        banner_url = _parse_banner_url(d.pop("bannerUrl", UNSET))

        def _parse_big_banner_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        big_banner_url = _parse_big_banner_url(d.pop("bigBannerUrl", UNSET))

        def _parse_small_banner_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_banner_url = _parse_small_banner_url(d.pop("smallBannerUrl", UNSET))

        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_pdfs(data: object) -> Union[List["ListingsV2PdfUpload"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pdfs_type_0 = []
                _pdfs_type_0 = data
                for pdfs_type_0_item_data in _pdfs_type_0:
                    pdfs_type_0_item = ListingsV2PdfUpload.from_dict(pdfs_type_0_item_data)

                    pdfs_type_0.append(pdfs_type_0_item)

                return pdfs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingsV2PdfUpload"], None, Unset], data)

        pdfs = _parse_pdfs(d.pop("pdfs", UNSET))

        _inspection_details = d.pop("inspectionDetails", UNSET)
        inspection_details: Union[Unset, ListingsV2PropertyInspections]
        if isinstance(_inspection_details, Unset):
            inspection_details = UNSET
        else:
            inspection_details = ListingsV2PropertyInspections.from_dict(_inspection_details)

        def _parse_number_of_floors(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_floors = _parse_number_of_floors(d.pop("numberOfFloors", UNSET))

        def _parse_min_number_of_floors(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_number_of_floors = _parse_min_number_of_floors(d.pop("minNumberOfFloors", UNSET))

        def _parse_min_building_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_building_height = _parse_min_building_height(d.pop("minBuildingHeight", UNSET))

        def _parse_max_building_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_building_height = _parse_max_building_height(d.pop("maxBuildingHeight", UNSET))

        def _parse_number_of_buildings(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_buildings = _parse_number_of_buildings(d.pop("numberOfBuildings", UNSET))

        def _parse_number_of_apartments(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_apartments = _parse_number_of_apartments(d.pop("numberOfApartments", UNSET))

        def _parse_estimated_completion_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                estimated_completion_date_type_0 = isoparse(data)

                return estimated_completion_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        estimated_completion_date = _parse_estimated_completion_date(d.pop("estimatedCompletionDate", UNSET))

        def _parse_starting_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        starting_price = _parse_starting_price(d.pop("startingPrice", UNSET))

        def _parse_child_listing_ids(data: object) -> Union[List[int], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                child_listing_ids_type_0 = cast(List[int], data)

                return child_listing_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None, Unset], data)

        child_listing_ids = _parse_child_listing_ids(d.pop("childListingIds", UNSET))

        def _parse_linked_project_ids(data: object) -> Union[List[int], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linked_project_ids_type_0 = cast(List[int], data)

                return linked_project_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None, Unset], data)

        linked_project_ids = _parse_linked_project_ids(d.pop("linkedProjectIds", UNSET))

        listings_v2_project = cls(
            project_profile_type=project_profile_type,
            estimated_completion_tertile=estimated_completion_tertile,
            category=category,
            id=id,
            name=name,
            start_date=start_date,
            end_date=end_date,
            address=address,
            viewing_address=viewing_address,
            property_types=property_types,
            displayable_address=displayable_address,
            enquiry_email_address=enquiry_email_address,
            advertiser_identifiers=advertiser_identifiers,
            provider_details=provider_details,
            media=media,
            project_url=project_url,
            headline=headline,
            tagline=tagline,
            display_as_last_updated=display_as_last_updated,
            modified_by=modified_by,
            modified_date=modified_date,
            created_by=created_by,
            created_date=created_date,
            background_colour=background_colour,
            description=description,
            appointment_required=appointment_required,
            features=features,
            price_from=price_from,
            price_to=price_to,
            banner_url=banner_url,
            big_banner_url=big_banner_url,
            small_banner_url=small_banner_url,
            logo_url=logo_url,
            pdfs=pdfs,
            inspection_details=inspection_details,
            number_of_floors=number_of_floors,
            min_number_of_floors=min_number_of_floors,
            min_building_height=min_building_height,
            max_building_height=max_building_height,
            number_of_buildings=number_of_buildings,
            number_of_apartments=number_of_apartments,
            estimated_completion_date=estimated_completion_date,
            starting_price=starting_price,
            child_listing_ids=child_listing_ids,
            linked_project_ids=linked_project_ids,
        )

        return listings_v2_project
