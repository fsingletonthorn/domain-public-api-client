from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sales_results_v1_geo_location import SalesResultsV1GeoLocation


T = TypeVar("T", bound="SalesResultsV1SaleListing")


@_attrs_define
class SalesResultsV1SaleListing:
    """
    Attributes:
        unit_number (Union[None, Unset, str]): Gets or Sets UnitNumber
        street_number (Union[None, Unset, str]): Gets or Sets StreetNumber
        street_name (Union[None, Unset, str]): Gets or Sets StreetName
        street_type (Union[None, Unset, str]): Gets or Sets StreetType
        suburb (Union[None, Unset, str]): Gets or Sets Suburb
        postcode (Union[None, Unset, str]): Gets or Sets Postcode
        state (Union[None, Unset, str]): Gets or Sets State
        geo_location (Union[Unset, SalesResultsV1GeoLocation]): Encapsulates the details of a geo location, long/lat
        property_type (Union[None, Unset, str]): Gets or Sets PropertyType
        bedrooms (Union[None, Unset, int]): Gets or Sets Bedrooms
        bathrooms (Union[None, Unset, int]): Gets or Sets Bathrooms
        carspaces (Union[None, Unset, float]): Gets or Sets Carspaces
        price (Union[None, Unset, int]): Gets or Sets Price
        result (Union[None, Unset, str]): Gets or Sets Result
        agent (Union[None, Unset, str]): Gets or Sets Agent
        agency_name (Union[None, Unset, str]): Gets or Sets AgencyName
        agency_profile_page_url (Union[None, Unset, str]): Gets or Sets AgencyProfilePageUrl
        id (Union[None, Unset, int]): Listing id on Domain
        agency_id (Union[None, Unset, int]):
        property_details_url (Union[None, Unset, str]):
    """

    unit_number: Union[None, Unset, str] = UNSET
    street_number: Union[None, Unset, str] = UNSET
    street_name: Union[None, Unset, str] = UNSET
    street_type: Union[None, Unset, str] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    postcode: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    geo_location: Union[Unset, "SalesResultsV1GeoLocation"] = UNSET
    property_type: Union[None, Unset, str] = UNSET
    bedrooms: Union[None, Unset, int] = UNSET
    bathrooms: Union[None, Unset, int] = UNSET
    carspaces: Union[None, Unset, float] = UNSET
    price: Union[None, Unset, int] = UNSET
    result: Union[None, Unset, str] = UNSET
    agent: Union[None, Unset, str] = UNSET
    agency_name: Union[None, Unset, str] = UNSET
    agency_profile_page_url: Union[None, Unset, str] = UNSET
    id: Union[None, Unset, int] = UNSET
    agency_id: Union[None, Unset, int] = UNSET
    property_details_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unit_number: Union[None, Unset, str]
        if isinstance(self.unit_number, Unset):
            unit_number = UNSET
        else:
            unit_number = self.unit_number

        street_number: Union[None, Unset, str]
        if isinstance(self.street_number, Unset):
            street_number = UNSET
        else:
            street_number = self.street_number

        street_name: Union[None, Unset, str]
        if isinstance(self.street_name, Unset):
            street_name = UNSET
        else:
            street_name = self.street_name

        street_type: Union[None, Unset, str]
        if isinstance(self.street_type, Unset):
            street_type = UNSET
        else:
            street_type = self.street_type

        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        postcode: Union[None, Unset, str]
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        geo_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geo_location, Unset):
            geo_location = self.geo_location.to_dict()

        property_type: Union[None, Unset, str]
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        bedrooms: Union[None, Unset, int]
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        bathrooms: Union[None, Unset, int]
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        carspaces: Union[None, Unset, float]
        if isinstance(self.carspaces, Unset):
            carspaces = UNSET
        else:
            carspaces = self.carspaces

        price: Union[None, Unset, int]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        result: Union[None, Unset, str]
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        agent: Union[None, Unset, str]
        if isinstance(self.agent, Unset):
            agent = UNSET
        else:
            agent = self.agent

        agency_name: Union[None, Unset, str]
        if isinstance(self.agency_name, Unset):
            agency_name = UNSET
        else:
            agency_name = self.agency_name

        agency_profile_page_url: Union[None, Unset, str]
        if isinstance(self.agency_profile_page_url, Unset):
            agency_profile_page_url = UNSET
        else:
            agency_profile_page_url = self.agency_profile_page_url

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        agency_id: Union[None, Unset, int]
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        else:
            agency_id = self.agency_id

        property_details_url: Union[None, Unset, str]
        if isinstance(self.property_details_url, Unset):
            property_details_url = UNSET
        else:
            property_details_url = self.property_details_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if street_type is not UNSET:
            field_dict["streetType"] = street_type
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if state is not UNSET:
            field_dict["state"] = state
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if carspaces is not UNSET:
            field_dict["carspaces"] = carspaces
        if price is not UNSET:
            field_dict["price"] = price
        if result is not UNSET:
            field_dict["result"] = result
        if agent is not UNSET:
            field_dict["agent"] = agent
        if agency_name is not UNSET:
            field_dict["agencyName"] = agency_name
        if agency_profile_page_url is not UNSET:
            field_dict["agencyProfilePageUrl"] = agency_profile_page_url
        if id is not UNSET:
            field_dict["id"] = id
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if property_details_url is not UNSET:
            field_dict["propertyDetailsUrl"] = property_details_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sales_results_v1_geo_location import SalesResultsV1GeoLocation

        d = src_dict.copy()

        def _parse_unit_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit_number = _parse_unit_number(d.pop("unitNumber", UNSET))

        def _parse_street_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_number = _parse_street_number(d.pop("streetNumber", UNSET))

        def _parse_street_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_name = _parse_street_name(d.pop("streetName", UNSET))

        def _parse_street_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_type = _parse_street_type(d.pop("streetType", UNSET))

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_postcode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        _geo_location = d.pop("geoLocation", UNSET)
        geo_location: Union[Unset, SalesResultsV1GeoLocation]
        if isinstance(_geo_location, Unset):
            geo_location = UNSET
        else:
            geo_location = SalesResultsV1GeoLocation.from_dict(_geo_location)

        def _parse_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))

        def _parse_bedrooms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))

        def _parse_bathrooms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))

        def _parse_carspaces(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        carspaces = _parse_carspaces(d.pop("carspaces", UNSET))

        def _parse_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_result(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_agent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agent = _parse_agent(d.pop("agent", UNSET))

        def _parse_agency_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_name = _parse_agency_name(d.pop("agencyName", UNSET))

        def _parse_agency_profile_page_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_profile_page_url = _parse_agency_profile_page_url(d.pop("agencyProfilePageUrl", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_agency_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        agency_id = _parse_agency_id(d.pop("agencyId", UNSET))

        def _parse_property_details_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_details_url = _parse_property_details_url(d.pop("propertyDetailsUrl", UNSET))

        sales_results_v1_sale_listing = cls(
            unit_number=unit_number,
            street_number=street_number,
            street_name=street_name,
            street_type=street_type,
            suburb=suburb,
            postcode=postcode,
            state=state,
            geo_location=geo_location,
            property_type=property_type,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            carspaces=carspaces,
            price=price,
            result=result,
            agent=agent,
            agency_name=agency_name,
            agency_profile_page_url=agency_profile_page_url,
            id=id,
            agency_id=agency_id,
            property_details_url=property_details_url,
        )

        return sales_results_v1_sale_listing
