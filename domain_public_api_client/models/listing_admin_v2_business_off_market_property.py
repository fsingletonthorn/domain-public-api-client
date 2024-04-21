from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_business_off_market_property_property_type_item import (
    ListingAdminV2BusinessOffMarketPropertyPropertyTypeItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_admin_v2_address import ListingAdminV2Address
    from ..models.listing_admin_v2_area import ListingAdminV2Area
    from ..models.listing_admin_v2_land_area import ListingAdminV2LandArea
    from ..models.listing_admin_v2_parking import ListingAdminV2Parking
    from ..models.listing_admin_v2_property_media import ListingAdminV2PropertyMedia


T = TypeVar("T", bound="ListingAdminV2BusinessOffMarketProperty")


@_attrs_define
class ListingAdminV2BusinessOffMarketProperty:
    """Business off market property

    Attributes:
        property_type (List[ListingAdminV2BusinessOffMarketPropertyPropertyTypeItem]): Business property types
            ['accessoriesParts', 'accommodationTourism', 'accounting', 'adult', 'advertisingMarketing', 'aerial',
            'aeronautical', 'agedCare', 'agricultural', 'air', 'aircraft', 'alarms', 'alcoholLiquor', 'amusements',
            'animalRelated', 'aquaculture', 'aquaticMarineMarinaBerth', 'artsCrafts', 'autoElectrical', 'automotive',
            'backpackerHostel', 'bakery', 'barsNightclubs', 'beautyHealth', 'beautyProducts', 'beautySalon',
            'bikeAndMotorcycle', 'boardingKennels', 'boatsMarineMarinaBerth', 'bookkeeping', 'brokerage', 'builder',
            'buildingAndConstruction', 'bus', 'butcher', 'cafeCoffeeShop', 'car', 'carBusTruck', 'carDealership',
            'carRental', 'carWash', 'caravanPark', 'carpenter', 'catering', 'childCare', 'civil', 'cleaning',
            'cleaningAndMaintenance', 'clinicalPractice', 'clothingAccessories', 'clothingFootwear', 'communication',
            'communications', 'computerIT', 'computerAndInternet', 'construction', 'convenienceStore', 'copyLaminate',
            'courier', 'cropHarvesting', 'customs', 'dairyFarming', 'deli', 'dental', 'detailing', 'distributors',
            'drivingSchools', 'educationTraining', 'educational', 'electrical', 'employmentRecruitment', 'entertainment',
            'entertainmentTechnology', 'export', 'farming', 'fertiliser', 'finance', 'financialServices', 'fishingForestry',
            'floristNursery', 'foodBeverage', 'foodBeverageHospitality', 'franchiseBusinessOpportunities', 'freight',
            'fruitVegFreshProduce', 'fruitPicking', 'functionCentre', 'furnitureTimber', 'gambling', 'gardenHousehold',
            'gardenNurseries', 'gardening', 'glassCeramic', 'guestHouseBB', 'hairdresser', 'healthBeauty', 'healthSpa',
            'hire', 'homeGarden', 'homeBased', 'homewareHardware', 'hospital', 'hotel', 'huntingTrap', 'import',
            'importExportWholesale', 'industrialManufacturing', 'insemination', 'insurance', 'internet',
            'irrigationServices', 'juiceBar', 'landClearing', 'landscaping', 'laundryDryCleaning', 'legal',
            'leisureEntertainment', 'limousineTaxi', 'livestock', 'machinery', 'machineryMetal', 'managementRights',
            'manufacturers', 'manufacturingEngineering', 'marine', 'massage', 'mechanicalRepair', 'media', 'medical',
            'medicalPractice', 'miningEarthMoving', 'mobileServices', 'motel', 'motorcycle', 'musicRelated', 'mustering',
            'nails', 'naturalTherapies', 'newsagency', 'nursery', 'nursingHome', 'officeSupplies', 'oilGas', 'panelBeating',
            'paperPrinting', 'parkingCarSpace', 'pestRelated', 'pharmacies', 'plastic', 'plumbing', 'poolWater',
            'postOffices', 'printPhoto', 'professional', 'propertyRealEstate', 'rail', 'recreationSport', 'recruitment',
            'repair', 'resort', 'restaurant', 'retail', 'retailer', 'retirement', 'retirementVillage', 'road', 'rural',
            'scientific', 'sea', 'security', 'serviceStation', 'services', 'shearing', 'sportsComplexGym', 'supermarket',
            'takeawayFood', 'taxi', 'themePark', 'tours', 'training', 'transportDistribution', 'travel', 'truck', 'vending',
            'water', 'welding', 'wholesale', 'wholesalers', 'woolClassing', 'wreckers', 'alcoholGrocery', 'cafeRestaurants',
            'discountStore', 'ecoFriendly', 'green', 'grocery', 'specialityRetail', 'storage', 'travelAgency',
            'varietyStore', 'chickenShop', 'seafoodShop', 'deliCafe', 'cropping', 'viticulture', 'grazing', 'horticulture',
            'equine', 'farmlet', 'orchard', 'ruralLifestyle', 'onlineBusiness'].
        address (ListingAdminV2Address): Address structure for property
        parking (Union[Unset, ListingAdminV2Parking]): Parking Details
        images (Union[Unset, List['ListingAdminV2PropertyMedia']]): List of image files, photos or floor plans related
            to the listing.
            Supported image file formats: AVIF, BMP, GIF, HEIF/HEIC, JPEG, JPEG 2000, PNG, TIFF, WebP.
            The file size is restricted to maximum 100MB.
            We recommend against using transparent backgrounds.
            Some image formats, such as PNG, support transparency, but when images with transparent areas are resized, they
            may be converted to a format that doesn’t support transparency, such as JPEG.
            By default, transparent areas are converted to black, but the application displaying the image may convert the
            transparent area to the most appropriate colour for the area where the image is being placed.
        area (Union[Unset, ListingAdminV2Area]): Area information, Either single value or from and To must be provided
        land_area (Union[Unset, ListingAdminV2LandArea]): Area information, Either single value or from and To must be
            provided
    """

    property_type: List[ListingAdminV2BusinessOffMarketPropertyPropertyTypeItem]
    address: "ListingAdminV2Address"
    parking: Union[Unset, "ListingAdminV2Parking"] = UNSET
    images: Union[Unset, List["ListingAdminV2PropertyMedia"]] = UNSET
    area: Union[Unset, "ListingAdminV2Area"] = UNSET
    land_area: Union[Unset, "ListingAdminV2LandArea"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_type = []
        for property_type_item_data in self.property_type:
            property_type_item = property_type_item_data.value
            property_type.append(property_type_item)

        address = self.address.to_dict()

        parking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parking, Unset):
            parking = self.parking.to_dict()

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        area: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.to_dict()

        land_area: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.land_area, Unset):
            land_area = self.land_area.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyType": property_type,
                "address": address,
            }
        )
        if parking is not UNSET:
            field_dict["parking"] = parking
        if images is not UNSET:
            field_dict["images"] = images
        if area is not UNSET:
            field_dict["area"] = area
        if land_area is not UNSET:
            field_dict["landArea"] = land_area

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_admin_v2_address import ListingAdminV2Address
        from ..models.listing_admin_v2_area import ListingAdminV2Area
        from ..models.listing_admin_v2_land_area import ListingAdminV2LandArea
        from ..models.listing_admin_v2_parking import ListingAdminV2Parking
        from ..models.listing_admin_v2_property_media import ListingAdminV2PropertyMedia

        d = src_dict.copy()
        property_type = []
        _property_type = d.pop("propertyType")
        for property_type_item_data in _property_type:
            property_type_item = ListingAdminV2BusinessOffMarketPropertyPropertyTypeItem(property_type_item_data)

            property_type.append(property_type_item)

        address = ListingAdminV2Address.from_dict(d.pop("address"))

        _parking = d.pop("parking", UNSET)
        parking: Union[Unset, ListingAdminV2Parking]
        if isinstance(_parking, Unset):
            parking = UNSET
        else:
            parking = ListingAdminV2Parking.from_dict(_parking)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ListingAdminV2PropertyMedia.from_dict(images_item_data)

            images.append(images_item)

        _area = d.pop("area", UNSET)
        area: Union[Unset, ListingAdminV2Area]
        if isinstance(_area, Unset):
            area = UNSET
        else:
            area = ListingAdminV2Area.from_dict(_area)

        _land_area = d.pop("landArea", UNSET)
        land_area: Union[Unset, ListingAdminV2LandArea]
        if isinstance(_land_area, Unset):
            land_area = UNSET
        else:
            land_area = ListingAdminV2LandArea.from_dict(_land_area)

        listing_admin_v2_business_off_market_property = cls(
            property_type=property_type,
            address=address,
            parking=parking,
            images=images,
            area=area,
            land_area=land_area,
        )

        listing_admin_v2_business_off_market_property.additional_properties = d
        return listing_admin_v2_business_off_market_property

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
