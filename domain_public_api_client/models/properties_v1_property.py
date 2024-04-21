import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.properties_v1_property_cadastre_type import PropertiesV1PropertyCadastreType
from ..models.properties_v1_property_on_market_types_type_0_item import PropertiesV1PropertyOnMarketTypesType0Item
from ..models.properties_v1_property_status import PropertiesV1PropertyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.properties_v1_advert import PropertiesV1Advert
    from ..models.properties_v1_claim_data import PropertiesV1ClaimData
    from ..models.properties_v1_geo_coordinate import PropertiesV1GeoCoordinate
    from ..models.properties_v1_gnaf_id import PropertiesV1GnafId
    from ..models.properties_v1_photo import PropertiesV1Photo
    from ..models.properties_v1_property_history import PropertiesV1PropertyHistory


T = TypeVar("T", bound="PropertiesV1Property")


@_attrs_define
class PropertiesV1Property:
    """
    Attributes:
        cadastre_type (Union[Unset, PropertiesV1PropertyCadastreType]): Gets or Sets CadastreType
        on_market_types (Union[List[PropertiesV1PropertyOnMarketTypesType0Item], None, Unset]): Gets or Sets
            OnMarketTypes
        status (Union[Unset, PropertiesV1PropertyStatus]): Gets or Sets Status
        address (Union[None, Unset, str]): Gets or Sets Address
        address_coordinate (Union[Unset, PropertiesV1GeoCoordinate]): DomainPropertyIdModelModelsGeoCoordinate
        address_id (Union[None, Unset, int]): Gets or Sets AddressId
        adverts (Union[List['PropertiesV1Advert'], None, Unset]): Gets or Sets Adverts
        bathrooms (Union[None, Unset, int]): Gets or Sets Bathrooms
        bedrooms (Union[None, Unset, int]): Gets or Sets Bedrooms
        car_spaces (Union[None, Unset, int]): Gets or Sets CarSpaces
        claim (Union[Unset, PropertiesV1ClaimData]): DomainPropertyIdModelClaimsClaimData
        condition (Union[None, Unset, str]): Gets or Sets Condition
        created (Union[None, Unset, datetime.datetime]): Gets or Sets Created
        ensuites (Union[None, Unset, int]): Gets or Sets Ensuites
        features (Union[List[str], None, Unset]): Gets or Sets Features
        flat_number (Union[None, Unset, str]): Gets or Sets FlatNumber
        history (Union[Unset, PropertiesV1PropertyHistory]):
        id (Union[None, Unset, str]): Gets or Sets Id
        improvements (Union[None, Unset, str]): Gets or Sets Improvements
        internal_area (Union[None, Unset, int]): Gets or Sets InternalArea
        is_residential (Union[None, Unset, bool]): Gets or Sets IsResidential
        land_use (Union[None, Unset, str]): Gets or Sets LandUse
        lot_number (Union[None, Unset, str]): Gets or Sets LotNumber
        photos (Union[List['PropertiesV1Photo'], None, Unset]): Gets or Sets Photos
        plan_number (Union[None, Unset, str]): Gets or Sets PlanNumber
        postcode (Union[None, Unset, str]): Gets or Sets Postcode
        property_category (Union[None, Unset, str]): Gets or Sets PropertyCategory
        property_category_id (Union[None, Unset, int]): Gets or Sets PropertyCategoryId
        property_type (Union[None, Unset, str]): Gets or Sets PropertyType
        property_type_id (Union[None, Unset, int]): Gets or Sets PropertyTypeId
        rooms (Union[None, Unset, int]): Gets or Sets Rooms
        section_number (Union[None, Unset, str]): Gets or Sets SectionNumber
        state (Union[None, Unset, str]): Gets or Sets State
        storeys (Union[None, Unset, int]): Gets or Sets Storeys
        street_address (Union[None, Unset, str]): Gets or Sets StreetAddress
        street_name (Union[None, Unset, str]): Gets or Sets StreetName
        street_number (Union[None, Unset, str]): Gets or Sets StreetNumber
        street_type (Union[None, Unset, str]): Gets or Sets StreetType
        street_type_long (Union[None, Unset, str]): Gets or Sets StreetTypeLong
        suburb (Union[None, Unset, str]): Gets or Sets Suburb
        suburb_id (Union[None, Unset, int]): Gets or Sets SuburbId
        title (Union[None, Unset, str]): Gets or Sets Title
        updated (Union[None, Unset, datetime.datetime]): Gets or Sets Updated
        url_slug (Union[None, Unset, str]): Gets or Sets UrlSlug
        url_slug_short (Union[None, Unset, str]): Gets or Sets UrlSlugShort
        zone (Union[None, Unset, str]): Gets or Sets Zone
        gnaf_ids (Union[List['PropertiesV1GnafId'], None, Unset]): Gets or Sets GnafIds
        area_size (Union[None, Unset, int]): Gets or Sets AreaSize
        canonical_url (Union[None, Unset, str]):
    """

    cadastre_type: Union[Unset, PropertiesV1PropertyCadastreType] = UNSET
    on_market_types: Union[List[PropertiesV1PropertyOnMarketTypesType0Item], None, Unset] = UNSET
    status: Union[Unset, PropertiesV1PropertyStatus] = UNSET
    address: Union[None, Unset, str] = UNSET
    address_coordinate: Union[Unset, "PropertiesV1GeoCoordinate"] = UNSET
    address_id: Union[None, Unset, int] = UNSET
    adverts: Union[List["PropertiesV1Advert"], None, Unset] = UNSET
    bathrooms: Union[None, Unset, int] = UNSET
    bedrooms: Union[None, Unset, int] = UNSET
    car_spaces: Union[None, Unset, int] = UNSET
    claim: Union[Unset, "PropertiesV1ClaimData"] = UNSET
    condition: Union[None, Unset, str] = UNSET
    created: Union[None, Unset, datetime.datetime] = UNSET
    ensuites: Union[None, Unset, int] = UNSET
    features: Union[List[str], None, Unset] = UNSET
    flat_number: Union[None, Unset, str] = UNSET
    history: Union[Unset, "PropertiesV1PropertyHistory"] = UNSET
    id: Union[None, Unset, str] = UNSET
    improvements: Union[None, Unset, str] = UNSET
    internal_area: Union[None, Unset, int] = UNSET
    is_residential: Union[None, Unset, bool] = UNSET
    land_use: Union[None, Unset, str] = UNSET
    lot_number: Union[None, Unset, str] = UNSET
    photos: Union[List["PropertiesV1Photo"], None, Unset] = UNSET
    plan_number: Union[None, Unset, str] = UNSET
    postcode: Union[None, Unset, str] = UNSET
    property_category: Union[None, Unset, str] = UNSET
    property_category_id: Union[None, Unset, int] = UNSET
    property_type: Union[None, Unset, str] = UNSET
    property_type_id: Union[None, Unset, int] = UNSET
    rooms: Union[None, Unset, int] = UNSET
    section_number: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    storeys: Union[None, Unset, int] = UNSET
    street_address: Union[None, Unset, str] = UNSET
    street_name: Union[None, Unset, str] = UNSET
    street_number: Union[None, Unset, str] = UNSET
    street_type: Union[None, Unset, str] = UNSET
    street_type_long: Union[None, Unset, str] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    suburb_id: Union[None, Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET
    updated: Union[None, Unset, datetime.datetime] = UNSET
    url_slug: Union[None, Unset, str] = UNSET
    url_slug_short: Union[None, Unset, str] = UNSET
    zone: Union[None, Unset, str] = UNSET
    gnaf_ids: Union[List["PropertiesV1GnafId"], None, Unset] = UNSET
    area_size: Union[None, Unset, int] = UNSET
    canonical_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        cadastre_type: Union[Unset, str] = UNSET
        if not isinstance(self.cadastre_type, Unset):
            cadastre_type = self.cadastre_type.value

        on_market_types: Union[List[str], None, Unset]
        if isinstance(self.on_market_types, Unset):
            on_market_types = UNSET
        elif isinstance(self.on_market_types, list):
            on_market_types = []
            for on_market_types_type_0_item_data in self.on_market_types:
                on_market_types_type_0_item = on_market_types_type_0_item_data.value
                on_market_types.append(on_market_types_type_0_item)

        else:
            on_market_types = self.on_market_types

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        address_coordinate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_coordinate, Unset):
            address_coordinate = self.address_coordinate.to_dict()

        address_id: Union[None, Unset, int]
        if isinstance(self.address_id, Unset):
            address_id = UNSET
        else:
            address_id = self.address_id

        adverts: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.adverts, Unset):
            adverts = UNSET
        elif isinstance(self.adverts, list):
            adverts = []
            for adverts_type_0_item_data in self.adverts:
                adverts_type_0_item = adverts_type_0_item_data.to_dict()
                adverts.append(adverts_type_0_item)

        else:
            adverts = self.adverts

        bathrooms: Union[None, Unset, int]
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        bedrooms: Union[None, Unset, int]
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        car_spaces: Union[None, Unset, int]
        if isinstance(self.car_spaces, Unset):
            car_spaces = UNSET
        else:
            car_spaces = self.car_spaces

        claim: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.claim, Unset):
            claim = self.claim.to_dict()

        condition: Union[None, Unset, str]
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        created: Union[None, Unset, str]
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        ensuites: Union[None, Unset, int]
        if isinstance(self.ensuites, Unset):
            ensuites = UNSET
        else:
            ensuites = self.ensuites

        features: Union[List[str], None, Unset]
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, list):
            features = self.features

        else:
            features = self.features

        flat_number: Union[None, Unset, str]
        if isinstance(self.flat_number, Unset):
            flat_number = UNSET
        else:
            flat_number = self.flat_number

        history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.history, Unset):
            history = self.history.to_dict()

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        improvements: Union[None, Unset, str]
        if isinstance(self.improvements, Unset):
            improvements = UNSET
        else:
            improvements = self.improvements

        internal_area: Union[None, Unset, int]
        if isinstance(self.internal_area, Unset):
            internal_area = UNSET
        else:
            internal_area = self.internal_area

        is_residential: Union[None, Unset, bool]
        if isinstance(self.is_residential, Unset):
            is_residential = UNSET
        else:
            is_residential = self.is_residential

        land_use: Union[None, Unset, str]
        if isinstance(self.land_use, Unset):
            land_use = UNSET
        else:
            land_use = self.land_use

        lot_number: Union[None, Unset, str]
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        photos: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.photos, Unset):
            photos = UNSET
        elif isinstance(self.photos, list):
            photos = []
            for photos_type_0_item_data in self.photos:
                photos_type_0_item = photos_type_0_item_data.to_dict()
                photos.append(photos_type_0_item)

        else:
            photos = self.photos

        plan_number: Union[None, Unset, str]
        if isinstance(self.plan_number, Unset):
            plan_number = UNSET
        else:
            plan_number = self.plan_number

        postcode: Union[None, Unset, str]
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        property_category: Union[None, Unset, str]
        if isinstance(self.property_category, Unset):
            property_category = UNSET
        else:
            property_category = self.property_category

        property_category_id: Union[None, Unset, int]
        if isinstance(self.property_category_id, Unset):
            property_category_id = UNSET
        else:
            property_category_id = self.property_category_id

        property_type: Union[None, Unset, str]
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        property_type_id: Union[None, Unset, int]
        if isinstance(self.property_type_id, Unset):
            property_type_id = UNSET
        else:
            property_type_id = self.property_type_id

        rooms: Union[None, Unset, int]
        if isinstance(self.rooms, Unset):
            rooms = UNSET
        else:
            rooms = self.rooms

        section_number: Union[None, Unset, str]
        if isinstance(self.section_number, Unset):
            section_number = UNSET
        else:
            section_number = self.section_number

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        storeys: Union[None, Unset, int]
        if isinstance(self.storeys, Unset):
            storeys = UNSET
        else:
            storeys = self.storeys

        street_address: Union[None, Unset, str]
        if isinstance(self.street_address, Unset):
            street_address = UNSET
        else:
            street_address = self.street_address

        street_name: Union[None, Unset, str]
        if isinstance(self.street_name, Unset):
            street_name = UNSET
        else:
            street_name = self.street_name

        street_number: Union[None, Unset, str]
        if isinstance(self.street_number, Unset):
            street_number = UNSET
        else:
            street_number = self.street_number

        street_type: Union[None, Unset, str]
        if isinstance(self.street_type, Unset):
            street_type = UNSET
        else:
            street_type = self.street_type

        street_type_long: Union[None, Unset, str]
        if isinstance(self.street_type_long, Unset):
            street_type_long = UNSET
        else:
            street_type_long = self.street_type_long

        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        suburb_id: Union[None, Unset, int]
        if isinstance(self.suburb_id, Unset):
            suburb_id = UNSET
        else:
            suburb_id = self.suburb_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        updated: Union[None, Unset, str]
        if isinstance(self.updated, Unset):
            updated = UNSET
        elif isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        url_slug: Union[None, Unset, str]
        if isinstance(self.url_slug, Unset):
            url_slug = UNSET
        else:
            url_slug = self.url_slug

        url_slug_short: Union[None, Unset, str]
        if isinstance(self.url_slug_short, Unset):
            url_slug_short = UNSET
        else:
            url_slug_short = self.url_slug_short

        zone: Union[None, Unset, str]
        if isinstance(self.zone, Unset):
            zone = UNSET
        else:
            zone = self.zone

        gnaf_ids: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.gnaf_ids, Unset):
            gnaf_ids = UNSET
        elif isinstance(self.gnaf_ids, list):
            gnaf_ids = []
            for gnaf_ids_type_0_item_data in self.gnaf_ids:
                gnaf_ids_type_0_item = gnaf_ids_type_0_item_data.to_dict()
                gnaf_ids.append(gnaf_ids_type_0_item)

        else:
            gnaf_ids = self.gnaf_ids

        area_size: Union[None, Unset, int]
        if isinstance(self.area_size, Unset):
            area_size = UNSET
        else:
            area_size = self.area_size

        canonical_url: Union[None, Unset, str]
        if isinstance(self.canonical_url, Unset):
            canonical_url = UNSET
        else:
            canonical_url = self.canonical_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if cadastre_type is not UNSET:
            field_dict["cadastreType"] = cadastre_type
        if on_market_types is not UNSET:
            field_dict["onMarketTypes"] = on_market_types
        if status is not UNSET:
            field_dict["status"] = status
        if address is not UNSET:
            field_dict["address"] = address
        if address_coordinate is not UNSET:
            field_dict["addressCoordinate"] = address_coordinate
        if address_id is not UNSET:
            field_dict["addressId"] = address_id
        if adverts is not UNSET:
            field_dict["adverts"] = adverts
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if car_spaces is not UNSET:
            field_dict["carSpaces"] = car_spaces
        if claim is not UNSET:
            field_dict["claim"] = claim
        if condition is not UNSET:
            field_dict["condition"] = condition
        if created is not UNSET:
            field_dict["created"] = created
        if ensuites is not UNSET:
            field_dict["ensuites"] = ensuites
        if features is not UNSET:
            field_dict["features"] = features
        if flat_number is not UNSET:
            field_dict["flatNumber"] = flat_number
        if history is not UNSET:
            field_dict["history"] = history
        if id is not UNSET:
            field_dict["id"] = id
        if improvements is not UNSET:
            field_dict["improvements"] = improvements
        if internal_area is not UNSET:
            field_dict["internalArea"] = internal_area
        if is_residential is not UNSET:
            field_dict["isResidential"] = is_residential
        if land_use is not UNSET:
            field_dict["landUse"] = land_use
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if photos is not UNSET:
            field_dict["photos"] = photos
        if plan_number is not UNSET:
            field_dict["planNumber"] = plan_number
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if property_category is not UNSET:
            field_dict["propertyCategory"] = property_category
        if property_category_id is not UNSET:
            field_dict["propertyCategoryId"] = property_category_id
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if property_type_id is not UNSET:
            field_dict["propertyTypeId"] = property_type_id
        if rooms is not UNSET:
            field_dict["rooms"] = rooms
        if section_number is not UNSET:
            field_dict["sectionNumber"] = section_number
        if state is not UNSET:
            field_dict["state"] = state
        if storeys is not UNSET:
            field_dict["storeys"] = storeys
        if street_address is not UNSET:
            field_dict["streetAddress"] = street_address
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street_type is not UNSET:
            field_dict["streetType"] = street_type
        if street_type_long is not UNSET:
            field_dict["streetTypeLong"] = street_type_long
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if suburb_id is not UNSET:
            field_dict["suburbId"] = suburb_id
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated
        if url_slug is not UNSET:
            field_dict["urlSlug"] = url_slug
        if url_slug_short is not UNSET:
            field_dict["urlSlugShort"] = url_slug_short
        if zone is not UNSET:
            field_dict["zone"] = zone
        if gnaf_ids is not UNSET:
            field_dict["gnafIds"] = gnaf_ids
        if area_size is not UNSET:
            field_dict["areaSize"] = area_size
        if canonical_url is not UNSET:
            field_dict["canonicalUrl"] = canonical_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.properties_v1_advert import PropertiesV1Advert
        from ..models.properties_v1_claim_data import PropertiesV1ClaimData
        from ..models.properties_v1_geo_coordinate import PropertiesV1GeoCoordinate
        from ..models.properties_v1_gnaf_id import PropertiesV1GnafId
        from ..models.properties_v1_photo import PropertiesV1Photo
        from ..models.properties_v1_property_history import PropertiesV1PropertyHistory

        d = src_dict.copy()
        _cadastre_type = d.pop("cadastreType", UNSET)
        cadastre_type: Union[Unset, PropertiesV1PropertyCadastreType]
        if isinstance(_cadastre_type, Unset):
            cadastre_type = UNSET
        else:
            cadastre_type = PropertiesV1PropertyCadastreType(_cadastre_type)

        def _parse_on_market_types(
            data: object,
        ) -> Union[List[PropertiesV1PropertyOnMarketTypesType0Item], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                on_market_types_type_0 = []
                _on_market_types_type_0 = data
                for on_market_types_type_0_item_data in _on_market_types_type_0:
                    on_market_types_type_0_item = PropertiesV1PropertyOnMarketTypesType0Item(
                        on_market_types_type_0_item_data
                    )

                    on_market_types_type_0.append(on_market_types_type_0_item)

                return on_market_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[PropertiesV1PropertyOnMarketTypesType0Item], None, Unset], data)

        on_market_types = _parse_on_market_types(d.pop("onMarketTypes", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PropertiesV1PropertyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PropertiesV1PropertyStatus(_status)

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        _address_coordinate = d.pop("addressCoordinate", UNSET)
        address_coordinate: Union[Unset, PropertiesV1GeoCoordinate]
        if isinstance(_address_coordinate, Unset):
            address_coordinate = UNSET
        else:
            address_coordinate = PropertiesV1GeoCoordinate.from_dict(_address_coordinate)

        def _parse_address_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        address_id = _parse_address_id(d.pop("addressId", UNSET))

        def _parse_adverts(data: object) -> Union[List["PropertiesV1Advert"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                adverts_type_0 = []
                _adverts_type_0 = data
                for adverts_type_0_item_data in _adverts_type_0:
                    adverts_type_0_item = PropertiesV1Advert.from_dict(adverts_type_0_item_data)

                    adverts_type_0.append(adverts_type_0_item)

                return adverts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PropertiesV1Advert"], None, Unset], data)

        adverts = _parse_adverts(d.pop("adverts", UNSET))

        def _parse_bathrooms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))

        def _parse_bedrooms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))

        def _parse_car_spaces(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        car_spaces = _parse_car_spaces(d.pop("carSpaces", UNSET))

        _claim = d.pop("claim", UNSET)
        claim: Union[Unset, PropertiesV1ClaimData]
        if isinstance(_claim, Unset):
            claim = UNSET
        else:
            claim = PropertiesV1ClaimData.from_dict(_claim)

        def _parse_condition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        condition = _parse_condition(d.pop("condition", UNSET))

        def _parse_created(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created = _parse_created(d.pop("created", UNSET))

        def _parse_ensuites(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ensuites = _parse_ensuites(d.pop("ensuites", UNSET))

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

        def _parse_flat_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        flat_number = _parse_flat_number(d.pop("flatNumber", UNSET))

        _history = d.pop("history", UNSET)
        history: Union[Unset, PropertiesV1PropertyHistory]
        if isinstance(_history, Unset):
            history = UNSET
        else:
            history = PropertiesV1PropertyHistory.from_dict(_history)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_improvements(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        improvements = _parse_improvements(d.pop("improvements", UNSET))

        def _parse_internal_area(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        internal_area = _parse_internal_area(d.pop("internalArea", UNSET))

        def _parse_is_residential(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_residential = _parse_is_residential(d.pop("isResidential", UNSET))

        def _parse_land_use(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        land_use = _parse_land_use(d.pop("landUse", UNSET))

        def _parse_lot_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))

        def _parse_photos(data: object) -> Union[List["PropertiesV1Photo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                photos_type_0 = []
                _photos_type_0 = data
                for photos_type_0_item_data in _photos_type_0:
                    photos_type_0_item = PropertiesV1Photo.from_dict(photos_type_0_item_data)

                    photos_type_0.append(photos_type_0_item)

                return photos_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PropertiesV1Photo"], None, Unset], data)

        photos = _parse_photos(d.pop("photos", UNSET))

        def _parse_plan_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        plan_number = _parse_plan_number(d.pop("planNumber", UNSET))

        def _parse_postcode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        def _parse_property_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_category = _parse_property_category(d.pop("propertyCategory", UNSET))

        def _parse_property_category_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        property_category_id = _parse_property_category_id(d.pop("propertyCategoryId", UNSET))

        def _parse_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))

        def _parse_property_type_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        property_type_id = _parse_property_type_id(d.pop("propertyTypeId", UNSET))

        def _parse_rooms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rooms = _parse_rooms(d.pop("rooms", UNSET))

        def _parse_section_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        section_number = _parse_section_number(d.pop("sectionNumber", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_storeys(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        storeys = _parse_storeys(d.pop("storeys", UNSET))

        def _parse_street_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_address = _parse_street_address(d.pop("streetAddress", UNSET))

        def _parse_street_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_name = _parse_street_name(d.pop("streetName", UNSET))

        def _parse_street_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_number = _parse_street_number(d.pop("streetNumber", UNSET))

        def _parse_street_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_type = _parse_street_type(d.pop("streetType", UNSET))

        def _parse_street_type_long(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_type_long = _parse_street_type_long(d.pop("streetTypeLong", UNSET))

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_suburb_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        suburb_id = _parse_suburb_id(d.pop("suburbId", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_updated(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_type_0 = isoparse(data)

                return updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated = _parse_updated(d.pop("updated", UNSET))

        def _parse_url_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url_slug = _parse_url_slug(d.pop("urlSlug", UNSET))

        def _parse_url_slug_short(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url_slug_short = _parse_url_slug_short(d.pop("urlSlugShort", UNSET))

        def _parse_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zone = _parse_zone(d.pop("zone", UNSET))

        def _parse_gnaf_ids(data: object) -> Union[List["PropertiesV1GnafId"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gnaf_ids_type_0 = []
                _gnaf_ids_type_0 = data
                for gnaf_ids_type_0_item_data in _gnaf_ids_type_0:
                    gnaf_ids_type_0_item = PropertiesV1GnafId.from_dict(gnaf_ids_type_0_item_data)

                    gnaf_ids_type_0.append(gnaf_ids_type_0_item)

                return gnaf_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PropertiesV1GnafId"], None, Unset], data)

        gnaf_ids = _parse_gnaf_ids(d.pop("gnafIds", UNSET))

        def _parse_area_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        area_size = _parse_area_size(d.pop("areaSize", UNSET))

        def _parse_canonical_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canonical_url = _parse_canonical_url(d.pop("canonicalUrl", UNSET))

        properties_v1_property = cls(
            cadastre_type=cadastre_type,
            on_market_types=on_market_types,
            status=status,
            address=address,
            address_coordinate=address_coordinate,
            address_id=address_id,
            adverts=adverts,
            bathrooms=bathrooms,
            bedrooms=bedrooms,
            car_spaces=car_spaces,
            claim=claim,
            condition=condition,
            created=created,
            ensuites=ensuites,
            features=features,
            flat_number=flat_number,
            history=history,
            id=id,
            improvements=improvements,
            internal_area=internal_area,
            is_residential=is_residential,
            land_use=land_use,
            lot_number=lot_number,
            photos=photos,
            plan_number=plan_number,
            postcode=postcode,
            property_category=property_category,
            property_category_id=property_category_id,
            property_type=property_type,
            property_type_id=property_type_id,
            rooms=rooms,
            section_number=section_number,
            state=state,
            storeys=storeys,
            street_address=street_address,
            street_name=street_name,
            street_number=street_number,
            street_type=street_type,
            street_type_long=street_type_long,
            suburb=suburb,
            suburb_id=suburb_id,
            title=title,
            updated=updated,
            url_slug=url_slug,
            url_slug_short=url_slug_short,
            zone=zone,
            gnaf_ids=gnaf_ids,
            area_size=area_size,
            canonical_url=canonical_url,
        )

        return properties_v1_property
