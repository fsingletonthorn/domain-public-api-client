import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_public_adapter_web_api_models_v1_listings_listing_channel import (
    DomainPublicAdapterWebApiModelsV1ListingsListingChannel,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_listing_objective import (
    DomainPublicAdapterWebApiModelsV1ListingsListingObjective,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_listing_property_types_item import (
    DomainPublicAdapterWebApiModelsV1ListingsListingPropertyTypesItem,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_listing_sale_mode import (
    DomainPublicAdapterWebApiModelsV1ListingsListingSaleMode,
)
from ..models.domain_public_adapter_web_api_models_v1_listings_listing_status import (
    DomainPublicAdapterWebApiModelsV1ListingsListingStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_address_parts import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressParts,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_advertiser_identifiers import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_australian_property_monitors_identifiers import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAustralianPropertyMonitorsIdentifiers,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_geo_location import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingGeoLocation,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_listing_media import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMedia,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_property_inspections import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_provider_details import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingProviderDetails,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_rental_details import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetails,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sale_details import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetails,
    )
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_statement_of_information import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingStatementOfInformation,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsListing")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsListing:
    r"""Represents a Property Listing

    Attributes:
        objective (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingObjective]): The type of Advertisement
        property_types (Union[Unset, List[DomainPublicAdapterWebApiModelsV1ListingsListingPropertyTypesItem]]): Types of
            the property e.g. House, Duplex, Apartment/Unit/Flat
        status (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingStatus]): The current status of the
            property
        sale_mode (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingSaleMode]): Sale method of the property
        channel (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingChannel]): Listing channel
        address_parts (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressParts]):
        advertiser_identifiers (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers]):
        apm_identifiers (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAustralianPropertyMonitorsIdentifiers]):
        bathrooms (Union[Unset, float]): Total number of bathrooms in the property
        bedrooms (Union[Unset, float]): Total number of bedrooms in the property; Studio apartments have a value of
            \"0\"
        building_area (Union[Unset, str]): The building area display value of the property e.g. 160 ha
        building_area_sqm (Union[Unset, float]): The properties building area in square meters
        carspaces (Union[Unset, float]): Total number of car spaces in the property.
        date_available (Union[Unset, datetime.datetime]): The date the property is available
        date_created (Union[Unset, datetime.datetime]): The date/time the listing was created
        date_updated (Union[Unset, datetime.datetime]): The date/time the listing had major update
        date_minor_updated (Union[Unset, datetime.datetime]): When minor update applied to listing
        date_listed (Union[Unset, datetime.datetime]): The date/time the listing was first listed
        date_purged (Union[Unset, datetime.datetime]): The date/time the listing was purged.
        description (Union[Unset, str]): The long description of the property provided by the advertiser
        dev_project_id (Union[Unset, int]): The ID of the development project - null if no associated project
        energy_efficiency_rating (Union[Unset, int]): Energy Efficiency Rating value for ACT properties
        features (Union[Unset, List[str]]): The property features specified by the advertiser
        geo_location (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingGeoLocation]):
        headline (Union[Unset, str]): The short description of the property provided by the advertiser
        id (Union[Unset, int]): The identifier which uniquely identifies the listing
        inspection_details (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections]):
        is_new_development (Union[Unset, bool]): Indicates whether the property is a new development
        land_area (Union[Unset, str]): The land area display string for the property e.g. 160 sqm
        land_area_sqm (Union[Unset, float]): The properties land area in square meters
        media (Union[Unset, List['DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMedia']]):
            The media associated with the property provided by the advertiser
        price_details (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails]):
        property_id (Union[Unset, str]): The identifier which uniquely identifies the property being advertised.
            This may be empty if the Address of property is poorly described
        provider_details (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingProviderDetails]):
        rental_details (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetails]):
        sale_details (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetails]):
        is_withdrawn (Union[Unset, bool]): Indicates if the property has been withdrawn               from the market
        seo_url (Union[Unset, str]): listing SEO Url
        error_message (Union[Unset, str]): In case of a mapping error is used to display error details
        virtual_tour_url (Union[Unset, str]): The Listing's Surroundpix Url.
        homepass_enabled (Union[Unset, bool]): If homepass is enabled for the listing (agency)
        statement_of_information (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingStatementOfInformation]):
        number_of_dwellings (Union[Unset, int]): Number of dwellings for current listing
        highlights (Union[Unset, List[str]]): Highlight items for the listing
    """

    objective: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingObjective] = UNSET
    property_types: Union[Unset, List[DomainPublicAdapterWebApiModelsV1ListingsListingPropertyTypesItem]] = UNSET
    status: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingStatus] = UNSET
    sale_mode: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingSaleMode] = UNSET
    channel: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingChannel] = UNSET
    address_parts: Union[Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressParts"] = (
        UNSET
    )
    advertiser_identifiers: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers"
    ] = UNSET
    apm_identifiers: Union[
        Unset,
        "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAustralianPropertyMonitorsIdentifiers",
    ] = UNSET
    bathrooms: Union[Unset, float] = UNSET
    bedrooms: Union[Unset, float] = UNSET
    building_area: Union[Unset, str] = UNSET
    building_area_sqm: Union[Unset, float] = UNSET
    carspaces: Union[Unset, float] = UNSET
    date_available: Union[Unset, datetime.datetime] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_updated: Union[Unset, datetime.datetime] = UNSET
    date_minor_updated: Union[Unset, datetime.datetime] = UNSET
    date_listed: Union[Unset, datetime.datetime] = UNSET
    date_purged: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    dev_project_id: Union[Unset, int] = UNSET
    energy_efficiency_rating: Union[Unset, int] = UNSET
    features: Union[Unset, List[str]] = UNSET
    geo_location: Union[Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingGeoLocation"] = (
        UNSET
    )
    headline: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    inspection_details: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections"
    ] = UNSET
    is_new_development: Union[Unset, bool] = UNSET
    land_area: Union[Unset, str] = UNSET
    land_area_sqm: Union[Unset, float] = UNSET
    media: Union[Unset, List["DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMedia"]] = (
        UNSET
    )
    price_details: Union[Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails"] = (
        UNSET
    )
    property_id: Union[Unset, str] = UNSET
    provider_details: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingProviderDetails"
    ] = UNSET
    rental_details: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetails"
    ] = UNSET
    sale_details: Union[Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetails"] = (
        UNSET
    )
    is_withdrawn: Union[Unset, bool] = UNSET
    seo_url: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    virtual_tour_url: Union[Unset, str] = UNSET
    homepass_enabled: Union[Unset, bool] = UNSET
    statement_of_information: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingStatementOfInformation"
    ] = UNSET
    number_of_dwellings: Union[Unset, int] = UNSET
    highlights: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objective: Union[Unset, str] = UNSET
        if not isinstance(self.objective, Unset):
            objective = self.objective.value

        property_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_types, Unset):
            property_types = []
            for property_types_item_data in self.property_types:
                property_types_item = property_types_item_data.value
                property_types.append(property_types_item)

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

        advertiser_identifiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advertiser_identifiers, Unset):
            advertiser_identifiers = self.advertiser_identifiers.to_dict()

        apm_identifiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.apm_identifiers, Unset):
            apm_identifiers = self.apm_identifiers.to_dict()

        bathrooms = self.bathrooms

        bedrooms = self.bedrooms

        building_area = self.building_area

        building_area_sqm = self.building_area_sqm

        carspaces = self.carspaces

        date_available: Union[Unset, str] = UNSET
        if not isinstance(self.date_available, Unset):
            date_available = self.date_available.isoformat()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_updated: Union[Unset, str] = UNSET
        if not isinstance(self.date_updated, Unset):
            date_updated = self.date_updated.isoformat()

        date_minor_updated: Union[Unset, str] = UNSET
        if not isinstance(self.date_minor_updated, Unset):
            date_minor_updated = self.date_minor_updated.isoformat()

        date_listed: Union[Unset, str] = UNSET
        if not isinstance(self.date_listed, Unset):
            date_listed = self.date_listed.isoformat()

        date_purged: Union[Unset, str] = UNSET
        if not isinstance(self.date_purged, Unset):
            date_purged = self.date_purged.isoformat()

        description = self.description

        dev_project_id = self.dev_project_id

        energy_efficiency_rating = self.energy_efficiency_rating

        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        geo_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geo_location, Unset):
            geo_location = self.geo_location.to_dict()

        headline = self.headline

        id = self.id

        inspection_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inspection_details, Unset):
            inspection_details = self.inspection_details.to_dict()

        is_new_development = self.is_new_development

        land_area = self.land_area

        land_area_sqm = self.land_area_sqm

        media: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        price_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_details, Unset):
            price_details = self.price_details.to_dict()

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

        is_withdrawn = self.is_withdrawn

        seo_url = self.seo_url

        error_message = self.error_message

        virtual_tour_url = self.virtual_tour_url

        homepass_enabled = self.homepass_enabled

        statement_of_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statement_of_information, Unset):
            statement_of_information = self.statement_of_information.to_dict()

        number_of_dwellings = self.number_of_dwellings

        highlights: Union[Unset, List[str]] = UNSET
        if not isinstance(self.highlights, Unset):
            highlights = self.highlights

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objective is not UNSET:
            field_dict["objective"] = objective
        if property_types is not UNSET:
            field_dict["propertyTypes"] = property_types
        if status is not UNSET:
            field_dict["status"] = status
        if sale_mode is not UNSET:
            field_dict["saleMode"] = sale_mode
        if channel is not UNSET:
            field_dict["channel"] = channel
        if address_parts is not UNSET:
            field_dict["addressParts"] = address_parts
        if advertiser_identifiers is not UNSET:
            field_dict["advertiserIdentifiers"] = advertiser_identifiers
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
        if date_listed is not UNSET:
            field_dict["dateListed"] = date_listed
        if date_purged is not UNSET:
            field_dict["datePurged"] = date_purged
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
        if id is not UNSET:
            field_dict["id"] = id
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
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
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
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_address_parts import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressParts,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_advertiser_identifiers import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_australian_property_monitors_identifiers import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAustralianPropertyMonitorsIdentifiers,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_geo_location import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingGeoLocation,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_listing_media import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMedia,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_property_inspections import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_provider_details import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingProviderDetails,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_rental_details import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetails,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sale_details import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetails,
        )
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_statement_of_information import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingStatementOfInformation,
        )

        d = src_dict.copy()
        _objective = d.pop("objective", UNSET)
        objective: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingObjective]
        if isinstance(_objective, Unset):
            objective = UNSET
        else:
            objective = DomainPublicAdapterWebApiModelsV1ListingsListingObjective(_objective)

        property_types = []
        _property_types = d.pop("propertyTypes", UNSET)
        for property_types_item_data in _property_types or []:
            property_types_item = DomainPublicAdapterWebApiModelsV1ListingsListingPropertyTypesItem(
                property_types_item_data
            )

            property_types.append(property_types_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DomainPublicAdapterWebApiModelsV1ListingsListingStatus(_status)

        _sale_mode = d.pop("saleMode", UNSET)
        sale_mode: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingSaleMode]
        if isinstance(_sale_mode, Unset):
            sale_mode = UNSET
        else:
            sale_mode = DomainPublicAdapterWebApiModelsV1ListingsListingSaleMode(_sale_mode)

        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsListingChannel]
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = DomainPublicAdapterWebApiModelsV1ListingsListingChannel(_channel)

        _address_parts = d.pop("addressParts", UNSET)
        address_parts: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressParts]
        if isinstance(_address_parts, Unset):
            address_parts = UNSET
        else:
            address_parts = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressParts.from_dict(
                _address_parts
            )

        _advertiser_identifiers = d.pop("advertiserIdentifiers", UNSET)
        advertiser_identifiers: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers
        ]
        if isinstance(_advertiser_identifiers, Unset):
            advertiser_identifiers = UNSET
        else:
            advertiser_identifiers = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers.from_dict(
                    _advertiser_identifiers
                )
            )

        _apm_identifiers = d.pop("apmIdentifiers", UNSET)
        apm_identifiers: Union[
            Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAustralianPropertyMonitorsIdentifiers,
        ]
        if isinstance(_apm_identifiers, Unset):
            apm_identifiers = UNSET
        else:
            apm_identifiers = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAustralianPropertyMonitorsIdentifiers.from_dict(
                _apm_identifiers
            )

        bathrooms = d.pop("bathrooms", UNSET)

        bedrooms = d.pop("bedrooms", UNSET)

        building_area = d.pop("buildingArea", UNSET)

        building_area_sqm = d.pop("buildingAreaSqm", UNSET)

        carspaces = d.pop("carspaces", UNSET)

        _date_available = d.pop("dateAvailable", UNSET)
        date_available: Union[Unset, datetime.datetime]
        if isinstance(_date_available, Unset):
            date_available = UNSET
        else:
            date_available = isoparse(_date_available)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_updated = d.pop("dateUpdated", UNSET)
        date_updated: Union[Unset, datetime.datetime]
        if isinstance(_date_updated, Unset):
            date_updated = UNSET
        else:
            date_updated = isoparse(_date_updated)

        _date_minor_updated = d.pop("dateMinorUpdated", UNSET)
        date_minor_updated: Union[Unset, datetime.datetime]
        if isinstance(_date_minor_updated, Unset):
            date_minor_updated = UNSET
        else:
            date_minor_updated = isoparse(_date_minor_updated)

        _date_listed = d.pop("dateListed", UNSET)
        date_listed: Union[Unset, datetime.datetime]
        if isinstance(_date_listed, Unset):
            date_listed = UNSET
        else:
            date_listed = isoparse(_date_listed)

        _date_purged = d.pop("datePurged", UNSET)
        date_purged: Union[Unset, datetime.datetime]
        if isinstance(_date_purged, Unset):
            date_purged = UNSET
        else:
            date_purged = isoparse(_date_purged)

        description = d.pop("description", UNSET)

        dev_project_id = d.pop("devProjectId", UNSET)

        energy_efficiency_rating = d.pop("energyEfficiencyRating", UNSET)

        features = cast(List[str], d.pop("features", UNSET))

        _geo_location = d.pop("geoLocation", UNSET)
        geo_location: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingGeoLocation]
        if isinstance(_geo_location, Unset):
            geo_location = UNSET
        else:
            geo_location = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingGeoLocation.from_dict(
                _geo_location
            )

        headline = d.pop("headline", UNSET)

        id = d.pop("id", UNSET)

        _inspection_details = d.pop("inspectionDetails", UNSET)
        inspection_details: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections
        ]
        if isinstance(_inspection_details, Unset):
            inspection_details = UNSET
        else:
            inspection_details = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.from_dict(
                    _inspection_details
                )
            )

        is_new_development = d.pop("isNewDevelopment", UNSET)

        land_area = d.pop("landArea", UNSET)

        land_area_sqm = d.pop("landAreaSqm", UNSET)

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMedia.from_dict(
                media_item_data
            )

            media.append(media_item)

        _price_details = d.pop("priceDetails", UNSET)
        price_details: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails]
        if isinstance(_price_details, Unset):
            price_details = UNSET
        else:
            price_details = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.from_dict(
                _price_details
            )

        property_id = d.pop("propertyId", UNSET)

        _provider_details = d.pop("providerDetails", UNSET)
        provider_details: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingProviderDetails
        ]
        if isinstance(_provider_details, Unset):
            provider_details = UNSET
        else:
            provider_details = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingProviderDetails.from_dict(
                    _provider_details
                )
            )

        _rental_details = d.pop("rentalDetails", UNSET)
        rental_details: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetails]
        if isinstance(_rental_details, Unset):
            rental_details = UNSET
        else:
            rental_details = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetails.from_dict(
                    _rental_details
                )
            )

        _sale_details = d.pop("saleDetails", UNSET)
        sale_details: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetails]
        if isinstance(_sale_details, Unset):
            sale_details = UNSET
        else:
            sale_details = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSaleDetails.from_dict(
                _sale_details
            )

        is_withdrawn = d.pop("isWithdrawn", UNSET)

        seo_url = d.pop("seoUrl", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        virtual_tour_url = d.pop("virtualTourUrl", UNSET)

        homepass_enabled = d.pop("homepassEnabled", UNSET)

        _statement_of_information = d.pop("statementOfInformation", UNSET)
        statement_of_information: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingStatementOfInformation
        ]
        if isinstance(_statement_of_information, Unset):
            statement_of_information = UNSET
        else:
            statement_of_information = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingStatementOfInformation.from_dict(
                    _statement_of_information
                )
            )

        number_of_dwellings = d.pop("numberOfDwellings", UNSET)

        highlights = cast(List[str], d.pop("highlights", UNSET))

        domain_public_adapter_web_api_models_v1_listings_listing = cls(
            objective=objective,
            property_types=property_types,
            status=status,
            sale_mode=sale_mode,
            channel=channel,
            address_parts=address_parts,
            advertiser_identifiers=advertiser_identifiers,
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
            date_listed=date_listed,
            date_purged=date_purged,
            description=description,
            dev_project_id=dev_project_id,
            energy_efficiency_rating=energy_efficiency_rating,
            features=features,
            geo_location=geo_location,
            headline=headline,
            id=id,
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
            error_message=error_message,
            virtual_tour_url=virtual_tour_url,
            homepass_enabled=homepass_enabled,
            statement_of_information=statement_of_information,
            number_of_dwellings=number_of_dwellings,
            highlights=highlights,
        )

        domain_public_adapter_web_api_models_v1_listings_listing.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_listing

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
