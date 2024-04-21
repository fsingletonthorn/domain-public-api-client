"""Contains all the data models used in inputs/outputs"""

from .demographics_v2_demographics import DemographicsV2Demographics
from .demographics_v2_demographics_item import DemographicsV2DemographicsItem
from .demographics_v2_demographics_results import DemographicsV2DemographicsResults
from .listing_admin_v2_address import ListingAdminV2Address
from .listing_admin_v2_address_display_option import ListingAdminV2AddressDisplayOption
from .listing_admin_v2_address_state import ListingAdminV2AddressState
from .listing_admin_v2_agent_contact import ListingAdminV2AgentContact
from .listing_admin_v2_area import ListingAdminV2Area
from .listing_admin_v2_area_unit import ListingAdminV2AreaUnit
from .listing_admin_v2_business_off_market_listing import ListingAdminV2BusinessOffMarketListing
from .listing_admin_v2_business_off_market_listing_listing_action import (
    ListingAdminV2BusinessOffMarketListingListingAction,
)
from .listing_admin_v2_business_off_market_property import ListingAdminV2BusinessOffMarketProperty
from .listing_admin_v2_business_off_market_property_property_type_item import (
    ListingAdminV2BusinessOffMarketPropertyPropertyTypeItem,
)
from .listing_admin_v2_commercial_auction import ListingAdminV2CommercialAuction
from .listing_admin_v2_commercial_listing_v2 import ListingAdminV2CommercialListingV2
from .listing_admin_v2_commercial_listing_v2_contact_preference import (
    ListingAdminV2CommercialListingV2ContactPreference,
)
from .listing_admin_v2_commercial_listing_v2_listing_action import ListingAdminV2CommercialListingV2ListingAction
from .listing_admin_v2_commercial_listing_v2_occupancy_type import ListingAdminV2CommercialListingV2OccupancyType
from .listing_admin_v2_commercial_off_market_listing import ListingAdminV2CommercialOffMarketListing
from .listing_admin_v2_commercial_off_market_listing_listing_action import (
    ListingAdminV2CommercialOffMarketListingListingAction,
)
from .listing_admin_v2_commercial_off_market_property import ListingAdminV2CommercialOffMarketProperty
from .listing_admin_v2_commercial_off_market_property_building_type import (
    ListingAdminV2CommercialOffMarketPropertyBuildingType,
)
from .listing_admin_v2_commercial_off_market_property_property_type_item import (
    ListingAdminV2CommercialOffMarketPropertyPropertyTypeItem,
)
from .listing_admin_v2_commercial_price import ListingAdminV2CommercialPrice
from .listing_admin_v2_commercial_price_gst_option_type import ListingAdminV2CommercialPriceGstOptionType
from .listing_admin_v2_commercial_price_price_type import ListingAdminV2CommercialPricePriceType
from .listing_admin_v2_commercial_price_price_unit_type import ListingAdminV2CommercialPricePriceUnitType
from .listing_admin_v2_commercial_property import ListingAdminV2CommercialProperty
from .listing_admin_v2_commercial_property_building_type import ListingAdminV2CommercialPropertyBuildingType
from .listing_admin_v2_commercial_property_property_type_item import ListingAdminV2CommercialPropertyPropertyTypeItem
from .listing_admin_v2_contact import ListingAdminV2Contact
from .listing_admin_v2_geo_location import ListingAdminV2GeoLocation
from .listing_admin_v2_inspection import ListingAdminV2Inspection
from .listing_admin_v2_inspection_details import ListingAdminV2InspectionDetails
from .listing_admin_v2_land_area import ListingAdminV2LandArea
from .listing_admin_v2_land_area_unit import ListingAdminV2LandAreaUnit
from .listing_admin_v2_lease import ListingAdminV2Lease
from .listing_admin_v2_leased_details import ListingAdminV2LeasedDetails
from .listing_admin_v2_listing_response import ListingAdminV2ListingResponse
from .listing_admin_v2_listing_response_process_status import ListingAdminV2ListingResponseProcessStatus
from .listing_admin_v2_listing_supplementary import ListingAdminV2ListingSupplementary
from .listing_admin_v2_off_market_details_base import ListingAdminV2OffMarketDetailsBase
from .listing_admin_v2_off_market_details_base_off_market_action import (
    ListingAdminV2OffMarketDetailsBaseOffMarketAction,
)
from .listing_admin_v2_parking import ListingAdminV2Parking
from .listing_admin_v2_parking_details import ListingAdminV2ParkingDetails
from .listing_admin_v2_parking_details_parking_type import ListingAdminV2ParkingDetailsParkingType
from .listing_admin_v2_parking_info import ListingAdminV2ParkingInfo
from .listing_admin_v2_parking_parking_type import ListingAdminV2ParkingParkingType
from .listing_admin_v2_property_media import ListingAdminV2PropertyMedia
from .listing_admin_v2_property_media_resource_type import ListingAdminV2PropertyMediaResourceType
from .listing_admin_v2_property_pdf import ListingAdminV2PropertyPdf
from .listing_admin_v2_property_pdf_type import ListingAdminV2PropertyPdfType
from .listing_admin_v2_residential_off_market_listing import ListingAdminV2ResidentialOffMarketListing
from .listing_admin_v2_residential_off_market_listing_listing_action import (
    ListingAdminV2ResidentialOffMarketListingListingAction,
)
from .listing_admin_v2_residential_off_market_property import ListingAdminV2ResidentialOffMarketProperty
from .listing_admin_v2_residential_off_market_property_property_type_item import (
    ListingAdminV2ResidentialOffMarketPropertyPropertyTypeItem,
)
from .listing_admin_v2_sale_info import ListingAdminV2SaleInfo
from .listing_admin_v2_sold_details import ListingAdminV2SoldDetails
from .listing_admin_v2_sold_details_sold_type import ListingAdminV2SoldDetailsSoldType
from .listing_admin_v2_specific_unit_detail import ListingAdminV2SpecificUnitDetail
from .listing_admin_v2_specific_unit_detail_occupancy import ListingAdminV2SpecificUnitDetailOccupancy
from .listing_admin_v2_specific_unit_detail_price_unit import ListingAdminV2SpecificUnitDetailPriceUnit
from .listing_admin_v2_supplementary_metadata import ListingAdminV2SupplementaryMetadata
from .listing_admin_v2_supplementary_metadata_measurement_unit import ListingAdminV2SupplementaryMetadataMeasurementUnit
from .listing_admin_v2_tenant import ListingAdminV2Tenant
from .listing_admin_v2_tender import ListingAdminV2Tender
from .listing_admin_v2eoi import ListingAdminV2EOI
from .listings_bypropertyid_sale_mode import ListingsBypropertyidSaleMode
from .listings_v2_address_parts import ListingsV2AddressParts
from .listings_v2_address_parts_display_type import ListingsV2AddressPartsDisplayType
from .listings_v2_address_parts_state_abbreviation import ListingsV2AddressPartsStateAbbreviation
from .listings_v2_advertiser_identifiers import ListingsV2AdvertiserIdentifiers
from .listings_v2_advertiser_identifiers_advertiser_type import ListingsV2AdvertiserIdentifiersAdvertiserType
from .listings_v2_auction_details import ListingsV2AuctionDetails
from .listings_v2_auction_schedule import ListingsV2AuctionSchedule
from .listings_v2_australian_property_monitors_identifiers import ListingsV2AustralianPropertyMonitorsIdentifiers
from .listings_v2_basic_price import ListingsV2BasicPrice
from .listings_v2_comparable_data import ListingsV2ComparableData
from .listings_v2_geo_location import ListingsV2GeoLocation
from .listings_v2_inspection import ListingsV2Inspection
from .listings_v2_inspection_recurrence import ListingsV2InspectionRecurrence
from .listings_v2_listing import ListingsV2Listing
from .listings_v2_listing_channel import ListingsV2ListingChannel
from .listings_v2_listing_media import ListingsV2ListingMedia
from .listings_v2_listing_media_category import ListingsV2ListingMediaCategory
from .listings_v2_listing_media_type import ListingsV2ListingMediaType
from .listings_v2_listing_objective import ListingsV2ListingObjective
from .listings_v2_listing_property_types_item import ListingsV2ListingPropertyTypesItem
from .listings_v2_listing_sale_mode import ListingsV2ListingSaleMode
from .listings_v2_listing_status import ListingsV2ListingStatus
from .listings_v2_median_price_data import ListingsV2MedianPriceData
from .listings_v2_median_price_data_price_type import ListingsV2MedianPriceDataPriceType
from .listings_v2_past_sale_data import ListingsV2PastSaleData
from .listings_v2_price_details import ListingsV2PriceDetails
from .listings_v2_price_details_gst_option import ListingsV2PriceDetailsGstOption
from .listings_v2_price_details_hidden_reasons_type_0_item import ListingsV2PriceDetailsHiddenReasonsType0Item
from .listings_v2_price_details_price_type import ListingsV2PriceDetailsPriceType
from .listings_v2_price_details_price_unit import ListingsV2PriceDetailsPriceUnit
from .listings_v2_property_inspections import ListingsV2PropertyInspections
from .listings_v2_provider_details import ListingsV2ProviderDetails
from .listings_v2_rental_details import ListingsV2RentalDetails
from .listings_v2_rental_details_rental_method import ListingsV2RentalDetailsRentalMethod
from .listings_v2_rental_details_source import ListingsV2RentalDetailsSource
from .listings_v2_sale_details import ListingsV2SaleDetails
from .listings_v2_sale_details_sale_method import ListingsV2SaleDetailsSaleMethod
from .listings_v2_sold_details import ListingsV2SoldDetails
from .listings_v2_sold_details_sold_action import ListingsV2SoldDetailsSoldAction
from .listings_v2_sold_details_source import ListingsV2SoldDetailsSource
from .listings_v2_statement_of_information import ListingsV2StatementOfInformation
from .listings_v2_tenant_details import ListingsV2TenantDetails
from .listings_v2_tender_details import ListingsV2TenderDetails
from .pre_market_v1_address import PreMarketV1Address
from .pre_market_v1_address_response import PreMarketV1AddressResponse
from .pre_market_v1_advertiser_identifiers import PreMarketV1AdvertiserIdentifiers
from .pre_market_v1_authority_type import PreMarketV1AuthorityType
from .pre_market_v1_contact import PreMarketV1Contact
from .pre_market_v1_create_or_update_listing_response import PreMarketV1CreateOrUpdateListingResponse
from .pre_market_v1_geo_location import PreMarketV1GeoLocation
from .pre_market_v1_listing_request import PreMarketV1ListingRequest
from .pre_market_v1_listing_request_json_patch_document import PreMarketV1ListingRequestJsonPatchDocument
from .pre_market_v1_listing_request_metadata_type_0 import PreMarketV1ListingRequestMetadataType0
from .pre_market_v1_listing_request_operation import PreMarketV1ListingRequestOperation
from .pre_market_v1_listing_response import PreMarketV1ListingResponse
from .pre_market_v1_listing_response_metadata_type_0 import PreMarketV1ListingResponseMetadataType0
from .pre_market_v1_operation_type import PreMarketV1OperationType
from .pre_market_v1_pre_portal_listing_status import PreMarketV1PrePortalListingStatus
from .pre_market_v1_price import PreMarketV1Price
from .pre_market_v1_problem_details import PreMarketV1ProblemDetails
from .pre_market_v1_property_media import PreMarketV1PropertyMedia
from .pre_market_v1_property_type import PreMarketV1PropertyType
from .pre_market_v1_provider_details import PreMarketV1ProviderDetails
from .pre_market_v1_resource_type import PreMarketV1ResourceType
from .pre_market_v1_sold_details import PreMarketV1SoldDetails
from .pre_market_v1_state import PreMarketV1State
from .pre_market_v1_statement_of_information import PreMarketV1StatementOfInformation
from .pre_market_v1i_contract_resolver import PreMarketV1IContractResolver
from .problem_details import ProblemDetails
from .schools_v2_school import SchoolsV2School
from .schools_v2_school_catchment import SchoolsV2SchoolCatchment
from .schools_v2_school_catchment_type import SchoolsV2SchoolCatchmentType
from .schools_v2_school_gender import SchoolsV2SchoolGender
from .schools_v2_school_profile import SchoolsV2SchoolProfile
from .schools_v2_school_school_sector import SchoolsV2SchoolSchoolSector
from .schools_v2_school_school_type import SchoolsV2SchoolSchoolType
from .schools_v2_school_with_distance import SchoolsV2SchoolWithDistance
from .suburb_performance_get_by_named_suburb_period_size import SuburbPerformanceGetByNamedSuburbPeriodSize
from .suburb_performance_get_by_named_suburb_property_category import SuburbPerformanceGetByNamedSuburbPropertyCategory
from .suburb_performance_get_by_named_suburb_without_postcode_period_size import (
    SuburbPerformanceGetByNamedSuburbWithoutPostcodePeriodSize,
)
from .suburb_performance_get_by_named_suburb_without_postcode_property_category import (
    SuburbPerformanceGetByNamedSuburbWithoutPostcodePropertyCategory,
)
from .suburb_performance_statistics_v3_suburb_performance import SuburbPerformanceStatisticsV3SuburbPerformance
from .suburb_performance_statistics_v3_suburb_series import SuburbPerformanceStatisticsV3SuburbSeries
from .suburb_performance_statistics_v3_suburb_series_header import SuburbPerformanceStatisticsV3SuburbSeriesHeader
from .suburb_performance_statistics_v3_suburb_series_info import SuburbPerformanceStatisticsV3SuburbSeriesInfo
from .suburb_performance_statistics_v3_suburb_series_info_values_type_0 import (
    SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0,
)

__all__ = (
    "DemographicsV2Demographics",
    "DemographicsV2DemographicsItem",
    "DemographicsV2DemographicsResults",
    "ListingAdminV2Address",
    "ListingAdminV2AddressDisplayOption",
    "ListingAdminV2AddressState",
    "ListingAdminV2AgentContact",
    "ListingAdminV2Area",
    "ListingAdminV2AreaUnit",
    "ListingAdminV2BusinessOffMarketListing",
    "ListingAdminV2BusinessOffMarketListingListingAction",
    "ListingAdminV2BusinessOffMarketProperty",
    "ListingAdminV2BusinessOffMarketPropertyPropertyTypeItem",
    "ListingAdminV2CommercialAuction",
    "ListingAdminV2CommercialListingV2",
    "ListingAdminV2CommercialListingV2ContactPreference",
    "ListingAdminV2CommercialListingV2ListingAction",
    "ListingAdminV2CommercialListingV2OccupancyType",
    "ListingAdminV2CommercialOffMarketListing",
    "ListingAdminV2CommercialOffMarketListingListingAction",
    "ListingAdminV2CommercialOffMarketProperty",
    "ListingAdminV2CommercialOffMarketPropertyBuildingType",
    "ListingAdminV2CommercialOffMarketPropertyPropertyTypeItem",
    "ListingAdminV2CommercialPrice",
    "ListingAdminV2CommercialPriceGstOptionType",
    "ListingAdminV2CommercialPricePriceType",
    "ListingAdminV2CommercialPricePriceUnitType",
    "ListingAdminV2CommercialProperty",
    "ListingAdminV2CommercialPropertyBuildingType",
    "ListingAdminV2CommercialPropertyPropertyTypeItem",
    "ListingAdminV2Contact",
    "ListingAdminV2EOI",
    "ListingAdminV2GeoLocation",
    "ListingAdminV2Inspection",
    "ListingAdminV2InspectionDetails",
    "ListingAdminV2LandArea",
    "ListingAdminV2LandAreaUnit",
    "ListingAdminV2Lease",
    "ListingAdminV2LeasedDetails",
    "ListingAdminV2ListingResponse",
    "ListingAdminV2ListingResponseProcessStatus",
    "ListingAdminV2ListingSupplementary",
    "ListingAdminV2OffMarketDetailsBase",
    "ListingAdminV2OffMarketDetailsBaseOffMarketAction",
    "ListingAdminV2Parking",
    "ListingAdminV2ParkingDetails",
    "ListingAdminV2ParkingDetailsParkingType",
    "ListingAdminV2ParkingInfo",
    "ListingAdminV2ParkingParkingType",
    "ListingAdminV2PropertyMedia",
    "ListingAdminV2PropertyMediaResourceType",
    "ListingAdminV2PropertyPdf",
    "ListingAdminV2PropertyPdfType",
    "ListingAdminV2ResidentialOffMarketListing",
    "ListingAdminV2ResidentialOffMarketListingListingAction",
    "ListingAdminV2ResidentialOffMarketProperty",
    "ListingAdminV2ResidentialOffMarketPropertyPropertyTypeItem",
    "ListingAdminV2SaleInfo",
    "ListingAdminV2SoldDetails",
    "ListingAdminV2SoldDetailsSoldType",
    "ListingAdminV2SpecificUnitDetail",
    "ListingAdminV2SpecificUnitDetailOccupancy",
    "ListingAdminV2SpecificUnitDetailPriceUnit",
    "ListingAdminV2SupplementaryMetadata",
    "ListingAdminV2SupplementaryMetadataMeasurementUnit",
    "ListingAdminV2Tenant",
    "ListingAdminV2Tender",
    "ListingsBypropertyidSaleMode",
    "ListingsV2AddressParts",
    "ListingsV2AddressPartsDisplayType",
    "ListingsV2AddressPartsStateAbbreviation",
    "ListingsV2AdvertiserIdentifiers",
    "ListingsV2AdvertiserIdentifiersAdvertiserType",
    "ListingsV2AuctionDetails",
    "ListingsV2AuctionSchedule",
    "ListingsV2AustralianPropertyMonitorsIdentifiers",
    "ListingsV2BasicPrice",
    "ListingsV2ComparableData",
    "ListingsV2GeoLocation",
    "ListingsV2Inspection",
    "ListingsV2InspectionRecurrence",
    "ListingsV2Listing",
    "ListingsV2ListingChannel",
    "ListingsV2ListingMedia",
    "ListingsV2ListingMediaCategory",
    "ListingsV2ListingMediaType",
    "ListingsV2ListingObjective",
    "ListingsV2ListingPropertyTypesItem",
    "ListingsV2ListingSaleMode",
    "ListingsV2ListingStatus",
    "ListingsV2MedianPriceData",
    "ListingsV2MedianPriceDataPriceType",
    "ListingsV2PastSaleData",
    "ListingsV2PriceDetails",
    "ListingsV2PriceDetailsGstOption",
    "ListingsV2PriceDetailsHiddenReasonsType0Item",
    "ListingsV2PriceDetailsPriceType",
    "ListingsV2PriceDetailsPriceUnit",
    "ListingsV2PropertyInspections",
    "ListingsV2ProviderDetails",
    "ListingsV2RentalDetails",
    "ListingsV2RentalDetailsRentalMethod",
    "ListingsV2RentalDetailsSource",
    "ListingsV2SaleDetails",
    "ListingsV2SaleDetailsSaleMethod",
    "ListingsV2SoldDetails",
    "ListingsV2SoldDetailsSoldAction",
    "ListingsV2SoldDetailsSource",
    "ListingsV2StatementOfInformation",
    "ListingsV2TenantDetails",
    "ListingsV2TenderDetails",
    "PreMarketV1Address",
    "PreMarketV1AddressResponse",
    "PreMarketV1AdvertiserIdentifiers",
    "PreMarketV1AuthorityType",
    "PreMarketV1Contact",
    "PreMarketV1CreateOrUpdateListingResponse",
    "PreMarketV1GeoLocation",
    "PreMarketV1IContractResolver",
    "PreMarketV1ListingRequest",
    "PreMarketV1ListingRequestJsonPatchDocument",
    "PreMarketV1ListingRequestMetadataType0",
    "PreMarketV1ListingRequestOperation",
    "PreMarketV1ListingResponse",
    "PreMarketV1ListingResponseMetadataType0",
    "PreMarketV1OperationType",
    "PreMarketV1PrePortalListingStatus",
    "PreMarketV1Price",
    "PreMarketV1ProblemDetails",
    "PreMarketV1PropertyMedia",
    "PreMarketV1PropertyType",
    "PreMarketV1ProviderDetails",
    "PreMarketV1ResourceType",
    "PreMarketV1SoldDetails",
    "PreMarketV1State",
    "PreMarketV1StatementOfInformation",
    "ProblemDetails",
    "SchoolsV2School",
    "SchoolsV2SchoolCatchment",
    "SchoolsV2SchoolCatchmentType",
    "SchoolsV2SchoolGender",
    "SchoolsV2SchoolProfile",
    "SchoolsV2SchoolSchoolSector",
    "SchoolsV2SchoolSchoolType",
    "SchoolsV2SchoolWithDistance",
    "SuburbPerformanceGetByNamedSuburbPeriodSize",
    "SuburbPerformanceGetByNamedSuburbPropertyCategory",
    "SuburbPerformanceGetByNamedSuburbWithoutPostcodePeriodSize",
    "SuburbPerformanceGetByNamedSuburbWithoutPostcodePropertyCategory",
    "SuburbPerformanceStatisticsV3SuburbPerformance",
    "SuburbPerformanceStatisticsV3SuburbSeries",
    "SuburbPerformanceStatisticsV3SuburbSeriesHeader",
    "SuburbPerformanceStatisticsV3SuburbSeriesInfo",
    "SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0",
)
