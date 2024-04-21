from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_business_property_property_type_item import (
    DomainListingAdminServiceV1ModelBusinessPropertyPropertyTypeItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_address import DomainListingAdminServiceV1ModelAddress
    from ..models.domain_listing_admin_service_v1_model_area import DomainListingAdminServiceV1ModelArea
    from ..models.domain_listing_admin_service_v1_model_land_area import DomainListingAdminServiceV1ModelLandArea
    from ..models.domain_listing_admin_service_v1_model_parking import DomainListingAdminServiceV1ModelParking
    from ..models.domain_listing_admin_service_v1_model_property_media import (
        DomainListingAdminServiceV1ModelPropertyMedia,
    )
    from ..models.domain_listing_admin_service_v1_model_property_pdf import DomainListingAdminServiceV1ModelPropertyPdf


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelBusinessProperty")


@_attrs_define
class DomainListingAdminServiceV1ModelBusinessProperty:
    """Business Property

    Attributes:
        property_type (Union[Unset, List[DomainListingAdminServiceV1ModelBusinessPropertyPropertyTypeItem]]): Business
            property types ['accessoriesParts', 'accommodationTourism', 'accounting', 'adult', 'advertisingMarketing',
            'aerial', 'aeronautical', 'agedCare', 'agricultural', 'air', 'aircraft', 'alarms', 'alcoholLiquor',
            'amusements', 'animalRelated', 'aquaculture', 'aquaticMarineMarinaBerth', 'artsCrafts', 'autoElectrical',
            'automotive', 'backpackerHostel', 'bakery', 'barsNightclubs', 'beautyHealth', 'beautyProducts', 'beautySalon',
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
        land_area (Union[Unset, DomainListingAdminServiceV1ModelLandArea]): Area information, Either single value or
            from and To must be provided
        parking (Union[Unset, DomainListingAdminServiceV1ModelParking]): Parking Details
        pdfs (Union[Unset, List['DomainListingAdminServiceV1ModelPropertyPdf']]): List of PDF files related to the
            listing
        is_marked_for_liveability (Union[Unset, bool]): Is the property liveability compliant
        property_name (Union[Unset, str]): Name of the property up to 70 characters
        location (Union[Unset, str]): Short location information up to 30 character, e.g.: Greenhills Beach
        images (Union[Unset, List['DomainListingAdminServiceV1ModelPropertyMedia']]): List of image files, photos or
            floor plans related to the listing.
        address (Union[Unset, DomainListingAdminServiceV1ModelAddress]): Address structure for property
        area (Union[Unset, DomainListingAdminServiceV1ModelArea]): Area information, Either single value or from and To
            must be provided
    """

    property_type: Union[Unset, List[DomainListingAdminServiceV1ModelBusinessPropertyPropertyTypeItem]] = UNSET
    land_area: Union[Unset, "DomainListingAdminServiceV1ModelLandArea"] = UNSET
    parking: Union[Unset, "DomainListingAdminServiceV1ModelParking"] = UNSET
    pdfs: Union[Unset, List["DomainListingAdminServiceV1ModelPropertyPdf"]] = UNSET
    is_marked_for_liveability: Union[Unset, bool] = UNSET
    property_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    images: Union[Unset, List["DomainListingAdminServiceV1ModelPropertyMedia"]] = UNSET
    address: Union[Unset, "DomainListingAdminServiceV1ModelAddress"] = UNSET
    area: Union[Unset, "DomainListingAdminServiceV1ModelArea"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_type, Unset):
            property_type = []
            for property_type_item_data in self.property_type:
                property_type_item = property_type_item_data.value
                property_type.append(property_type_item)

        land_area: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.land_area, Unset):
            land_area = self.land_area.to_dict()

        parking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parking, Unset):
            parking = self.parking.to_dict()

        pdfs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pdfs, Unset):
            pdfs = []
            for pdfs_item_data in self.pdfs:
                pdfs_item = pdfs_item_data.to_dict()
                pdfs.append(pdfs_item)

        is_marked_for_liveability = self.is_marked_for_liveability

        property_name = self.property_name

        location = self.location

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        area: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if land_area is not UNSET:
            field_dict["landArea"] = land_area
        if parking is not UNSET:
            field_dict["parking"] = parking
        if pdfs is not UNSET:
            field_dict["pdfs"] = pdfs
        if is_marked_for_liveability is not UNSET:
            field_dict["isMarkedForLiveability"] = is_marked_for_liveability
        if property_name is not UNSET:
            field_dict["propertyName"] = property_name
        if location is not UNSET:
            field_dict["location"] = location
        if images is not UNSET:
            field_dict["images"] = images
        if address is not UNSET:
            field_dict["address"] = address
        if area is not UNSET:
            field_dict["area"] = area

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listing_admin_service_v1_model_address import DomainListingAdminServiceV1ModelAddress
        from ..models.domain_listing_admin_service_v1_model_area import DomainListingAdminServiceV1ModelArea
        from ..models.domain_listing_admin_service_v1_model_land_area import DomainListingAdminServiceV1ModelLandArea
        from ..models.domain_listing_admin_service_v1_model_parking import DomainListingAdminServiceV1ModelParking
        from ..models.domain_listing_admin_service_v1_model_property_media import (
            DomainListingAdminServiceV1ModelPropertyMedia,
        )
        from ..models.domain_listing_admin_service_v1_model_property_pdf import (
            DomainListingAdminServiceV1ModelPropertyPdf,
        )

        d = src_dict.copy()
        property_type = []
        _property_type = d.pop("propertyType", UNSET)
        for property_type_item_data in _property_type or []:
            property_type_item = DomainListingAdminServiceV1ModelBusinessPropertyPropertyTypeItem(
                property_type_item_data
            )

            property_type.append(property_type_item)

        _land_area = d.pop("landArea", UNSET)
        land_area: Union[Unset, DomainListingAdminServiceV1ModelLandArea]
        if isinstance(_land_area, Unset):
            land_area = UNSET
        else:
            land_area = DomainListingAdminServiceV1ModelLandArea.from_dict(_land_area)

        _parking = d.pop("parking", UNSET)
        parking: Union[Unset, DomainListingAdminServiceV1ModelParking]
        if isinstance(_parking, Unset):
            parking = UNSET
        else:
            parking = DomainListingAdminServiceV1ModelParking.from_dict(_parking)

        pdfs = []
        _pdfs = d.pop("pdfs", UNSET)
        for pdfs_item_data in _pdfs or []:
            pdfs_item = DomainListingAdminServiceV1ModelPropertyPdf.from_dict(pdfs_item_data)

            pdfs.append(pdfs_item)

        is_marked_for_liveability = d.pop("isMarkedForLiveability", UNSET)

        property_name = d.pop("propertyName", UNSET)

        location = d.pop("location", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = DomainListingAdminServiceV1ModelPropertyMedia.from_dict(images_item_data)

            images.append(images_item)

        _address = d.pop("address", UNSET)
        address: Union[Unset, DomainListingAdminServiceV1ModelAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = DomainListingAdminServiceV1ModelAddress.from_dict(_address)

        _area = d.pop("area", UNSET)
        area: Union[Unset, DomainListingAdminServiceV1ModelArea]
        if isinstance(_area, Unset):
            area = UNSET
        else:
            area = DomainListingAdminServiceV1ModelArea.from_dict(_area)

        domain_listing_admin_service_v1_model_business_property = cls(
            property_type=property_type,
            land_area=land_area,
            parking=parking,
            pdfs=pdfs,
            is_marked_for_liveability=is_marked_for_liveability,
            property_name=property_name,
            location=location,
            images=images,
            address=address,
            area=area,
        )

        domain_listing_admin_service_v1_model_business_property.additional_properties = d
        return domain_listing_admin_service_v1_model_business_property

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
