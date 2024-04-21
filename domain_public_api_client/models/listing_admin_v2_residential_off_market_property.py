from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_residential_off_market_property_property_type_item import (
    ListingAdminV2ResidentialOffMarketPropertyPropertyTypeItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_admin_v2_address import ListingAdminV2Address
    from ..models.listing_admin_v2_area import ListingAdminV2Area
    from ..models.listing_admin_v2_land_area import ListingAdminV2LandArea
    from ..models.listing_admin_v2_parking_info import ListingAdminV2ParkingInfo
    from ..models.listing_admin_v2_property_media import ListingAdminV2PropertyMedia


T = TypeVar("T", bound="ListingAdminV2ResidentialOffMarketProperty")


@_attrs_define
class ListingAdminV2ResidentialOffMarketProperty:
    """Residential off market property

    Attributes:
        property_type (List[ListingAdminV2ResidentialOffMarketPropertyPropertyTypeItem]): Residential property types<br
            />
            'Retirement' requires at least one more property type to be specified with it (for example: "Retirement",
            "ApartmentUnitFlat") ['acreageSemiRural', 'apartmentUnitFlat', 'aquaculture', 'blockOfUnits', 'carSpace',
            'dairyFarming', 'developmentSite', 'duplex', 'farm', 'fishingForestry', 'newHomeDesigns', 'house',
            'newHouseLand', 'irrigationServices', 'newLand', 'livestock', 'newApartments', 'penthouse', 'retirement',
            'rural', 'semiDetached', 'specialistFarm', 'studio', 'terrace', 'townhouse', 'vacantLand', 'villa', 'cropping',
            'viticulture', 'mixedFarming', 'grazing', 'horticulture', 'equine', 'farmlet', 'orchard', 'ruralLifestyle'].
        address (ListingAdminV2Address): Address structure for property
        bed_rooms (Union[Unset, int]): Number of bedrooms
        bath_rooms (Union[Unset, int]): Number of bathrooms
        parking_info (Union[Unset, ListingAdminV2ParkingInfo]): Parking Details
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

    property_type: List[ListingAdminV2ResidentialOffMarketPropertyPropertyTypeItem]
    address: "ListingAdminV2Address"
    bed_rooms: Union[Unset, int] = UNSET
    bath_rooms: Union[Unset, int] = UNSET
    parking_info: Union[Unset, "ListingAdminV2ParkingInfo"] = UNSET
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

        bed_rooms = self.bed_rooms

        bath_rooms = self.bath_rooms

        parking_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parking_info, Unset):
            parking_info = self.parking_info.to_dict()

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
        if bed_rooms is not UNSET:
            field_dict["bedRooms"] = bed_rooms
        if bath_rooms is not UNSET:
            field_dict["bathRooms"] = bath_rooms
        if parking_info is not UNSET:
            field_dict["parkingInfo"] = parking_info
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
        from ..models.listing_admin_v2_parking_info import ListingAdminV2ParkingInfo
        from ..models.listing_admin_v2_property_media import ListingAdminV2PropertyMedia

        d = src_dict.copy()
        property_type = []
        _property_type = d.pop("propertyType")
        for property_type_item_data in _property_type:
            property_type_item = ListingAdminV2ResidentialOffMarketPropertyPropertyTypeItem(property_type_item_data)

            property_type.append(property_type_item)

        address = ListingAdminV2Address.from_dict(d.pop("address"))

        bed_rooms = d.pop("bedRooms", UNSET)

        bath_rooms = d.pop("bathRooms", UNSET)

        _parking_info = d.pop("parkingInfo", UNSET)
        parking_info: Union[Unset, ListingAdminV2ParkingInfo]
        if isinstance(_parking_info, Unset):
            parking_info = UNSET
        else:
            parking_info = ListingAdminV2ParkingInfo.from_dict(_parking_info)

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

        listing_admin_v2_residential_off_market_property = cls(
            property_type=property_type,
            address=address,
            bed_rooms=bed_rooms,
            bath_rooms=bath_rooms,
            parking_info=parking_info,
            images=images,
            area=area,
            land_area=land_area,
        )

        listing_admin_v2_residential_off_market_property.additional_properties = d
        return listing_admin_v2_residential_off_market_property

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
