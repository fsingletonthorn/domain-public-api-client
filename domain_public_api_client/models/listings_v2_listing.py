import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.listings_v2_listing_channel import ListingsV2ListingChannel
from ..models.listings_v2_listing_objective import ListingsV2ListingObjective
from ..models.listings_v2_listing_property_types_item import ListingsV2ListingPropertyTypesItem
from ..models.listings_v2_listing_sale_mode import ListingsV2ListingSaleMode
from ..models.listings_v2_listing_status import ListingsV2ListingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_v2_address_parts import ListingsV2AddressParts
    from ..models.listings_v2_advertiser_identifiers import ListingsV2AdvertiserIdentifiers
    from ..models.listings_v2_australian_property_monitors_identifiers import (
        ListingsV2AustralianPropertyMonitorsIdentifiers,
    )
    from ..models.listings_v2_geo_location import ListingsV2GeoLocation
    from ..models.listings_v2_listing_media import ListingsV2ListingMedia
    from ..models.listings_v2_price_details import ListingsV2PriceDetails
    from ..models.listings_v2_property_inspections import ListingsV2PropertyInspections
    from ..models.listings_v2_provider_details import ListingsV2ProviderDetails
    from ..models.listings_v2_rental_details import ListingsV2RentalDetails
    from ..models.listings_v2_sale_details import ListingsV2SaleDetails
    from ..models.listings_v2_statement_of_information import ListingsV2StatementOfInformation


T = TypeVar("T", bound="ListingsV2Listing")


@_attrs_define
class ListingsV2Listing:
    r"""Represents a Property Listing

    Attributes:
        id (int): The identifier which uniquely identifies the listing.
        advertiser_identifiers (ListingsV2AdvertiserIdentifiers): Encapsulates the listing's advertiser identifiers
        property_types (List[ListingsV2ListingPropertyTypesItem]): Types of the property
        objective (Union[Unset, ListingsV2ListingObjective]): Gets or Sets Objective
        status (Union[Unset, ListingsV2ListingStatus]): Gets or Sets Status
        sale_mode (Union[Unset, ListingsV2ListingSaleMode]): Gets or Sets SaleMode
        channel (Union[Unset, ListingsV2ListingChannel]): Gets or Sets Channel
        address_parts (Union[Unset, ListingsV2AddressParts]): Encapsulates the parts that make up an Address
        apm_identifiers (Union[Unset, ListingsV2AustralianPropertyMonitorsIdentifiers]): APM Identifiers
        bathrooms (Union[None, Unset, float]): Total number of bathrooms in the property
        bedrooms (Union[None, Unset, float]): Total number of bedrooms in the property; Studio apartments have a value
            of \"0\"
        building_area (Union[None, Unset, str]): The building area display value of the property e.g. 160 ha
        building_area_sqm (Union[None, Unset, float]): The properties building area in square meters
        carspaces (Union[None, Unset, float]): Total number of car spaces in the property.
        date_available (Union[None, Unset, datetime.datetime]): The date the property is available. DateTime is in a
            local timezone.
        date_created (Union[None, Unset, datetime.datetime]): The date/time the listing was created. DateTime is in AEST
            (Australian Eastern Standard Time) or AEDT (Australian Eastern Daylight Time) timezone.
        date_updated (Union[None, Unset, datetime.datetime]): The date/time the listing had major update. DateTime is in
            AEST (Australian Eastern Standard Time) or AEDT (Australian Eastern Daylight Time) timezone.
        date_minor_updated (Union[None, Unset, datetime.datetime]): When minor update applied to the listing. DateTime
            is in AEST (Australian Eastern Standard Time) or AEDT (Australian Eastern Daylight Time) timezone.
        date_purged (Union[None, Unset, datetime.datetime]): The date/time the listing was purged. It's only returned
            for archived listings. DateTime is in AEST (Australian Eastern Standard Time) or AEDT (Australian Eastern
            Daylight Time) timezone.
        date_listed (Union[None, Unset, datetime.datetime]): The date/time last listed. DateTime is in AEST (Australian
            Eastern Standard Time) or AEDT (Australian Eastern Daylight Time) timezone.
        description (Union[None, Unset, str]): The long description of the property provided by the advertiser.
        dev_project_id (Union[None, Unset, int]): The ID of the development project - null if no associated project
        energy_efficiency_rating (Union[None, Unset, int]): Energy Efficiency Rating value for ACT properties
        features (Union[List[str], None, Unset]): The property features specified by the advertiser
        geo_location (Union[Unset, ListingsV2GeoLocation]): Encapsulates the details of a geo location, long/lat
        headline (Union[None, Unset, str]): The short description of the property provided by the advertiser.
        inspection_details (Union[Unset, ListingsV2PropertyInspections]): Property Inspection(s) details
        is_new_development (Union[None, Unset, bool]): Indicates whether the property is a new development
        land_area (Union[None, Unset, str]): The land area display string for the property e.g. 160 sqm
        land_area_sqm (Union[None, Unset, float]): The properties land area in square meters
        media (Union[List['ListingsV2ListingMedia'], None, Unset]): The media associated with the property provided by
            the advertiser
        price_details (Union[Unset, ListingsV2PriceDetails]): Encapsulates a listing's price information
        property_id (Union[None, Unset, str]): The identifier which uniquely identifies the property being advertised.
            This may be empty if the Address of property is poorly described
        provider_details (Union[Unset, ListingsV2ProviderDetails]): Information for the listing provider. e.g.
            bulkuploader information
        rental_details (Union[Unset, ListingsV2RentalDetails]): The rental detail's of the listing in case of it being
            for rent or leased
        sale_details (Union[Unset, ListingsV2SaleDetails]): The sale detail's of the listing in case of it being for
            sale or sold
        is_withdrawn (Union[None, Unset, bool]): Indicates if the property has been withdrawn from the market  The value
            will be 'true' When a listing is taken off market without being sold or leased.
        seo_url (Union[None, Unset, str]): Listing SEO URL
        virtual_tour_url (Union[None, Unset, str]): The Listing's Virtual Tour URL.
        homepass_enabled (Union[None, Unset, bool]): If Homepass is enabled for the listing (agency)
        statement_of_information (Union[Unset, ListingsV2StatementOfInformation]): Statement of Information  Regarding
            sale listing
        number_of_dwellings (Union[None, Unset, int]): Number of dwellings for current listing
        highlights (Union[List[str], None, Unset]): Highlight items for the listing
    """

    id: int
    advertiser_identifiers: "ListingsV2AdvertiserIdentifiers"
    property_types: List[ListingsV2ListingPropertyTypesItem]
    objective: Union[Unset, ListingsV2ListingObjective] = UNSET
    status: Union[Unset, ListingsV2ListingStatus] = UNSET
    sale_mode: Union[Unset, ListingsV2ListingSaleMode] = UNSET
    channel: Union[Unset, ListingsV2ListingChannel] = UNSET
    address_parts: Union[Unset, "ListingsV2AddressParts"] = UNSET
    apm_identifiers: Union[Unset, "ListingsV2AustralianPropertyMonitorsIdentifiers"] = UNSET
    bathrooms: Union[None, Unset, float] = UNSET
    bedrooms: Union[None, Unset, float] = UNSET
    building_area: Union[None, Unset, str] = UNSET
    building_area_sqm: Union[None, Unset, float] = UNSET
    carspaces: Union[None, Unset, float] = UNSET
    date_available: Union[None, Unset, datetime.datetime] = UNSET
    date_created: Union[None, Unset, datetime.datetime] = UNSET
    date_updated: Union[None, Unset, datetime.datetime] = UNSET
    date_minor_updated: Union[None, Unset, datetime.datetime] = UNSET
    date_purged: Union[None, Unset, datetime.datetime] = UNSET
    date_listed: Union[None, Unset, datetime.datetime] = UNSET
    description: Union[None, Unset, str] = UNSET
    dev_project_id: Union[None, Unset, int] = UNSET
    energy_efficiency_rating: Union[None, Unset, int] = UNSET
    features: Union[List[str], None, Unset] = UNSET
    geo_location: Union[Unset, "ListingsV2GeoLocation"] = UNSET
    headline: Union[None, Unset, str] = UNSET
    inspection_details: Union[Unset, "ListingsV2PropertyInspections"] = UNSET
    is_new_development: Union[None, Unset, bool] = UNSET
    land_area: Union[None, Unset, str] = UNSET
    land_area_sqm: Union[None, Unset, float] = UNSET
    media: Union[List["ListingsV2ListingMedia"], None, Unset] = UNSET
    price_details: Union[Unset, "ListingsV2PriceDetails"] = UNSET
    property_id: Union[None, Unset, str] = UNSET
    provider_details: Union[Unset, "ListingsV2ProviderDetails"] = UNSET
    rental_details: Union[Unset, "ListingsV2RentalDetails"] = UNSET
    sale_details: Union[Unset, "ListingsV2SaleDetails"] = UNSET
    is_withdrawn: Union[None, Unset, bool] = UNSET
    seo_url: Union[None, Unset, str] = UNSET
    virtual_tour_url: Union[None, Unset, str] = UNSET
    homepass_enabled: Union[None, Unset, bool] = UNSET
    statement_of_information: Union[Unset, "ListingsV2StatementOfInformation"] = UNSET
    number_of_dwellings: Union[None, Unset, int] = UNSET
    highlights: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        advertiser_identifiers = self.advertiser_identifiers.to_dict()

        property_types = []
        for property_types_item_data in self.property_types:
            property_types_item = property_types_item_data.value
            property_types.append(property_types_item)

        objective: Union[Unset, str] = UNSET
        if not isinstance(self.objective, Unset):
            objective = self.objective.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        sale_mode: Union[Unset, str] = UNSET
        if not isinstance(self.sale_mode, Unset):
            sale_mode = self.sale_mode.value

        channel: Union[Unset, str] = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        address_parts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_parts, Unset):
            address_parts = self.address_parts.to_dict()

        apm_identifiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.apm_identifiers, Unset):
            apm_identifiers = self.apm_identifiers.to_dict()

        bathrooms: Union[None, Unset, float]
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        bedrooms: Union[None, Unset, float]
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        building_area: Union[None, Unset, str]
        if isinstance(self.building_area, Unset):
            building_area = UNSET
        else:
            building_area = self.building_area

        building_area_sqm: Union[None, Unset, float]
        if isinstance(self.building_area_sqm, Unset):
            building_area_sqm = UNSET
        else:
            building_area_sqm = self.building_area_sqm

        carspaces: Union[None, Unset, float]
        if isinstance(self.carspaces, Unset):
            carspaces = UNSET
        else:
            carspaces = self.carspaces

        date_available: Union[None, Unset, str]
        if isinstance(self.date_available, Unset):
            date_available = UNSET
        elif isinstance(self.date_available, datetime.datetime):
            date_available = self.date_available.isoformat()
        else:
            date_available = self.date_available

        date_created: Union[None, Unset, str]
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_updated: Union[None, Unset, str]
        if isinstance(self.date_updated, Unset):
            date_updated = UNSET
        elif isinstance(self.date_updated, datetime.datetime):
            date_updated = self.date_updated.isoformat()
        else:
            date_updated = self.date_updated

        date_minor_updated: Union[None, Unset, str]
        if isinstance(self.date_minor_updated, Unset):
            date_minor_updated = UNSET
        elif isinstance(self.date_minor_updated, datetime.datetime):
            date_minor_updated = self.date_minor_updated.isoformat()
        else:
            date_minor_updated = self.date_minor_updated

        date_purged: Union[None, Unset, str]
        if isinstance(self.date_purged, Unset):
            date_purged = UNSET
        elif isinstance(self.date_purged, datetime.datetime):
            date_purged = self.date_purged.isoformat()
        else:
            date_purged = self.date_purged

        date_listed: Union[None, Unset, str]
        if isinstance(self.date_listed, Unset):
            date_listed = UNSET
        elif isinstance(self.date_listed, datetime.datetime):
            date_listed = self.date_listed.isoformat()
        else:
            date_listed = self.date_listed

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        dev_project_id: Union[None, Unset, int]
        if isinstance(self.dev_project_id, Unset):
            dev_project_id = UNSET
        else:
            dev_project_id = self.dev_project_id

        energy_efficiency_rating: Union[None, Unset, int]
        if isinstance(self.energy_efficiency_rating, Unset):
            energy_efficiency_rating = UNSET
        else:
            energy_efficiency_rating = self.energy_efficiency_rating

        features: Union[List[str], None, Unset]
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, list):
            features = self.features

        else:
            features = self.features

        geo_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geo_location, Unset):
            geo_location = self.geo_location.to_dict()

        headline: Union[None, Unset, str]
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        inspection_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inspection_details, Unset):
            inspection_details = self.inspection_details.to_dict()

        is_new_development: Union[None, Unset, bool]
        if isinstance(self.is_new_development, Unset):
            is_new_development = UNSET
        else:
            is_new_development = self.is_new_development

        land_area: Union[None, Unset, str]
        if isinstance(self.land_area, Unset):
            land_area = UNSET
        else:
            land_area = self.land_area

        land_area_sqm: Union[None, Unset, float]
        if isinstance(self.land_area_sqm, Unset):
            land_area_sqm = UNSET
        else:
            land_area_sqm = self.land_area_sqm

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

        price_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_details, Unset):
            price_details = self.price_details.to_dict()

        property_id: Union[None, Unset, str]
        if isinstance(self.property_id, Unset):
            property_id = UNSET
        else:
            property_id = self.property_id

        provider_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_details, Unset):
            provider_details = self.provider_details.to_dict()

        rental_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rental_details, Unset):
            rental_details = self.rental_details.to_dict()

        sale_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sale_details, Unset):
            sale_details = self.sale_details.to_dict()

        is_withdrawn: Union[None, Unset, bool]
        if isinstance(self.is_withdrawn, Unset):
            is_withdrawn = UNSET
        else:
            is_withdrawn = self.is_withdrawn

        seo_url: Union[None, Unset, str]
        if isinstance(self.seo_url, Unset):
            seo_url = UNSET
        else:
            seo_url = self.seo_url

        virtual_tour_url: Union[None, Unset, str]
        if isinstance(self.virtual_tour_url, Unset):
            virtual_tour_url = UNSET
        else:
            virtual_tour_url = self.virtual_tour_url

        homepass_enabled: Union[None, Unset, bool]
        if isinstance(self.homepass_enabled, Unset):
            homepass_enabled = UNSET
        else:
            homepass_enabled = self.homepass_enabled

        statement_of_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statement_of_information, Unset):
            statement_of_information = self.statement_of_information.to_dict()

        number_of_dwellings: Union[None, Unset, int]
        if isinstance(self.number_of_dwellings, Unset):
            number_of_dwellings = UNSET
        else:
            number_of_dwellings = self.number_of_dwellings

        highlights: Union[List[str], None, Unset]
        if isinstance(self.highlights, Unset):
            highlights = UNSET
        elif isinstance(self.highlights, list):
            highlights = self.highlights

        else:
            highlights = self.highlights

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "advertiserIdentifiers": advertiser_identifiers,
                "propertyTypes": property_types,
            }
        )
        if objective is not UNSET:
            field_dict["objective"] = objective
        if status is not UNSET:
            field_dict["status"] = status
        if sale_mode is not UNSET:
            field_dict["saleMode"] = sale_mode
        if channel is not UNSET:
            field_dict["channel"] = channel
        if address_parts is not UNSET:
            field_dict["addressParts"] = address_parts
        if apm_identifiers is not UNSET:
            field_dict["apmIdentifiers"] = apm_identifiers
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if building_area is not UNSET:
            field_dict["buildingArea"] = building_area
        if building_area_sqm is not UNSET:
            field_dict["buildingAreaSqm"] = building_area_sqm
        if carspaces is not UNSET:
            field_dict["carspaces"] = carspaces
        if date_available is not UNSET:
            field_dict["dateAvailable"] = date_available
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if date_minor_updated is not UNSET:
            field_dict["dateMinorUpdated"] = date_minor_updated
        if date_purged is not UNSET:
            field_dict["datePurged"] = date_purged
        if date_listed is not UNSET:
            field_dict["dateListed"] = date_listed
        if description is not UNSET:
            field_dict["description"] = description
        if dev_project_id is not UNSET:
            field_dict["devProjectId"] = dev_project_id
        if energy_efficiency_rating is not UNSET:
            field_dict["energyEfficiencyRating"] = energy_efficiency_rating
        if features is not UNSET:
            field_dict["features"] = features
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if headline is not UNSET:
            field_dict["headline"] = headline
        if inspection_details is not UNSET:
            field_dict["inspectionDetails"] = inspection_details
        if is_new_development is not UNSET:
            field_dict["isNewDevelopment"] = is_new_development
        if land_area is not UNSET:
            field_dict["landArea"] = land_area
        if land_area_sqm is not UNSET:
            field_dict["landAreaSqm"] = land_area_sqm
        if media is not UNSET:
            field_dict["media"] = media
        if price_details is not UNSET:
            field_dict["priceDetails"] = price_details
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if provider_details is not UNSET:
            field_dict["providerDetails"] = provider_details
        if rental_details is not UNSET:
            field_dict["rentalDetails"] = rental_details
        if sale_details is not UNSET:
            field_dict["saleDetails"] = sale_details
        if is_withdrawn is not UNSET:
            field_dict["isWithdrawn"] = is_withdrawn
        if seo_url is not UNSET:
            field_dict["seoUrl"] = seo_url
        if virtual_tour_url is not UNSET:
            field_dict["virtualTourUrl"] = virtual_tour_url
        if homepass_enabled is not UNSET:
            field_dict["homepassEnabled"] = homepass_enabled
        if statement_of_information is not UNSET:
            field_dict["statementOfInformation"] = statement_of_information
        if number_of_dwellings is not UNSET:
            field_dict["numberOfDwellings"] = number_of_dwellings
        if highlights is not UNSET:
            field_dict["highlights"] = highlights

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listings_v2_address_parts import ListingsV2AddressParts
        from ..models.listings_v2_advertiser_identifiers import ListingsV2AdvertiserIdentifiers
        from ..models.listings_v2_australian_property_monitors_identifiers import (
            ListingsV2AustralianPropertyMonitorsIdentifiers,
        )
        from ..models.listings_v2_geo_location import ListingsV2GeoLocation
        from ..models.listings_v2_listing_media import ListingsV2ListingMedia
        from ..models.listings_v2_price_details import ListingsV2PriceDetails
        from ..models.listings_v2_property_inspections import ListingsV2PropertyInspections
        from ..models.listings_v2_provider_details import ListingsV2ProviderDetails
        from ..models.listings_v2_rental_details import ListingsV2RentalDetails
        from ..models.listings_v2_sale_details import ListingsV2SaleDetails
        from ..models.listings_v2_statement_of_information import ListingsV2StatementOfInformation

        d = src_dict.copy()
        id = d.pop("id")

        advertiser_identifiers = ListingsV2AdvertiserIdentifiers.from_dict(d.pop("advertiserIdentifiers"))

        property_types = []
        _property_types = d.pop("propertyTypes")
        for property_types_item_data in _property_types:
            property_types_item = ListingsV2ListingPropertyTypesItem(property_types_item_data)

            property_types.append(property_types_item)

        _objective = d.pop("objective", UNSET)
        objective: Union[Unset, ListingsV2ListingObjective]
        if isinstance(_objective, Unset):
            objective = UNSET
        else:
            objective = ListingsV2ListingObjective(_objective)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ListingsV2ListingStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ListingsV2ListingStatus(_status)

        _sale_mode = d.pop("saleMode", UNSET)
        sale_mode: Union[Unset, ListingsV2ListingSaleMode]
        if isinstance(_sale_mode, Unset):
            sale_mode = UNSET
        else:
            sale_mode = ListingsV2ListingSaleMode(_sale_mode)

        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, ListingsV2ListingChannel]
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = ListingsV2ListingChannel(_channel)

        _address_parts = d.pop("addressParts", UNSET)
        address_parts: Union[Unset, ListingsV2AddressParts]
        if isinstance(_address_parts, Unset):
            address_parts = UNSET
        else:
            address_parts = ListingsV2AddressParts.from_dict(_address_parts)

        _apm_identifiers = d.pop("apmIdentifiers", UNSET)
        apm_identifiers: Union[Unset, ListingsV2AustralianPropertyMonitorsIdentifiers]
        if isinstance(_apm_identifiers, Unset):
            apm_identifiers = UNSET
        else:
            apm_identifiers = ListingsV2AustralianPropertyMonitorsIdentifiers.from_dict(_apm_identifiers)

        def _parse_bathrooms(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))

        def _parse_bedrooms(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))

        def _parse_building_area(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        building_area = _parse_building_area(d.pop("buildingArea", UNSET))

        def _parse_building_area_sqm(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        building_area_sqm = _parse_building_area_sqm(d.pop("buildingAreaSqm", UNSET))

        def _parse_carspaces(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        carspaces = _parse_carspaces(d.pop("carspaces", UNSET))

        def _parse_date_available(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_available_type_0 = isoparse(data)

                return date_available_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_available = _parse_date_available(d.pop("dateAvailable", UNSET))

        def _parse_date_created(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = isoparse(data)

                return date_created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_created = _parse_date_created(d.pop("dateCreated", UNSET))

        def _parse_date_updated(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_updated_type_0 = isoparse(data)

                return date_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_updated = _parse_date_updated(d.pop("dateUpdated", UNSET))

        def _parse_date_minor_updated(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_minor_updated_type_0 = isoparse(data)

                return date_minor_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_minor_updated = _parse_date_minor_updated(d.pop("dateMinorUpdated", UNSET))

        def _parse_date_purged(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_purged_type_0 = isoparse(data)

                return date_purged_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_purged = _parse_date_purged(d.pop("datePurged", UNSET))

        def _parse_date_listed(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_listed_type_0 = isoparse(data)

                return date_listed_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_listed = _parse_date_listed(d.pop("dateListed", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_dev_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dev_project_id = _parse_dev_project_id(d.pop("devProjectId", UNSET))

        def _parse_energy_efficiency_rating(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        energy_efficiency_rating = _parse_energy_efficiency_rating(d.pop("energyEfficiencyRating", UNSET))

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

        _geo_location = d.pop("geoLocation", UNSET)
        geo_location: Union[Unset, ListingsV2GeoLocation]
        if isinstance(_geo_location, Unset):
            geo_location = UNSET
        else:
            geo_location = ListingsV2GeoLocation.from_dict(_geo_location)

        def _parse_headline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        headline = _parse_headline(d.pop("headline", UNSET))

        _inspection_details = d.pop("inspectionDetails", UNSET)
        inspection_details: Union[Unset, ListingsV2PropertyInspections]
        if isinstance(_inspection_details, Unset):
            inspection_details = UNSET
        else:
            inspection_details = ListingsV2PropertyInspections.from_dict(_inspection_details)

        def _parse_is_new_development(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_new_development = _parse_is_new_development(d.pop("isNewDevelopment", UNSET))

        def _parse_land_area(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        land_area = _parse_land_area(d.pop("landArea", UNSET))

        def _parse_land_area_sqm(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        land_area_sqm = _parse_land_area_sqm(d.pop("landAreaSqm", UNSET))

        def _parse_media(data: object) -> Union[List["ListingsV2ListingMedia"], None, Unset]:
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
                    media_type_0_item = ListingsV2ListingMedia.from_dict(media_type_0_item_data)

                    media_type_0.append(media_type_0_item)

                return media_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingsV2ListingMedia"], None, Unset], data)

        media = _parse_media(d.pop("media", UNSET))

        _price_details = d.pop("priceDetails", UNSET)
        price_details: Union[Unset, ListingsV2PriceDetails]
        if isinstance(_price_details, Unset):
            price_details = UNSET
        else:
            price_details = ListingsV2PriceDetails.from_dict(_price_details)

        def _parse_property_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_id = _parse_property_id(d.pop("propertyId", UNSET))

        _provider_details = d.pop("providerDetails", UNSET)
        provider_details: Union[Unset, ListingsV2ProviderDetails]
        if isinstance(_provider_details, Unset):
            provider_details = UNSET
        else:
            provider_details = ListingsV2ProviderDetails.from_dict(_provider_details)

        _rental_details = d.pop("rentalDetails", UNSET)
        rental_details: Union[Unset, ListingsV2RentalDetails]
        if isinstance(_rental_details, Unset):
            rental_details = UNSET
        else:
            rental_details = ListingsV2RentalDetails.from_dict(_rental_details)

        _sale_details = d.pop("saleDetails", UNSET)
        sale_details: Union[Unset, ListingsV2SaleDetails]
        if isinstance(_sale_details, Unset):
            sale_details = UNSET
        else:
            sale_details = ListingsV2SaleDetails.from_dict(_sale_details)

        def _parse_is_withdrawn(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_withdrawn = _parse_is_withdrawn(d.pop("isWithdrawn", UNSET))

        def _parse_seo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        seo_url = _parse_seo_url(d.pop("seoUrl", UNSET))

        def _parse_virtual_tour_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        virtual_tour_url = _parse_virtual_tour_url(d.pop("virtualTourUrl", UNSET))

        def _parse_homepass_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        homepass_enabled = _parse_homepass_enabled(d.pop("homepassEnabled", UNSET))

        _statement_of_information = d.pop("statementOfInformation", UNSET)
        statement_of_information: Union[Unset, ListingsV2StatementOfInformation]
        if isinstance(_statement_of_information, Unset):
            statement_of_information = UNSET
        else:
            statement_of_information = ListingsV2StatementOfInformation.from_dict(_statement_of_information)

        def _parse_number_of_dwellings(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_dwellings = _parse_number_of_dwellings(d.pop("numberOfDwellings", UNSET))

        def _parse_highlights(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                highlights_type_0 = cast(List[str], data)

                return highlights_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        highlights = _parse_highlights(d.pop("highlights", UNSET))

        listings_v2_listing = cls(
            id=id,
            advertiser_identifiers=advertiser_identifiers,
            property_types=property_types,
            objective=objective,
            status=status,
            sale_mode=sale_mode,
            channel=channel,
            address_parts=address_parts,
            apm_identifiers=apm_identifiers,
            bathrooms=bathrooms,
            bedrooms=bedrooms,
            building_area=building_area,
            building_area_sqm=building_area_sqm,
            carspaces=carspaces,
            date_available=date_available,
            date_created=date_created,
            date_updated=date_updated,
            date_minor_updated=date_minor_updated,
            date_purged=date_purged,
            date_listed=date_listed,
            description=description,
            dev_project_id=dev_project_id,
            energy_efficiency_rating=energy_efficiency_rating,
            features=features,
            geo_location=geo_location,
            headline=headline,
            inspection_details=inspection_details,
            is_new_development=is_new_development,
            land_area=land_area,
            land_area_sqm=land_area_sqm,
            media=media,
            price_details=price_details,
            property_id=property_id,
            provider_details=provider_details,
            rental_details=rental_details,
            sale_details=sale_details,
            is_withdrawn=is_withdrawn,
            seo_url=seo_url,
            virtual_tour_url=virtual_tour_url,
            homepass_enabled=homepass_enabled,
            statement_of_information=statement_of_information,
            number_of_dwellings=number_of_dwellings,
            highlights=highlights,
        )

        return listings_v2_listing
