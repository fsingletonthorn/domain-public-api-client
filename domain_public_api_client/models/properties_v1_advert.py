from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.properties_v1_advert_on_market_types_type_0_item import PropertiesV1AdvertOnMarketTypesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertiesV1Advert")


@_attrs_define
class PropertiesV1Advert:
    """DomainPropertyIdModelModelsAdvert

    Attributes:
        on_market_types (Union[List[PropertiesV1AdvertOnMarketTypesType0Item], None, Unset]): Gets or Sets OnMarketTypes
        advert_id (Union[None, Unset, int]): Gets or Sets AdvertId
        agency (Union[None, Unset, str]): Gets or Sets Agency
        agency_colour (Union[None, Unset, str]): Gets or Sets AgencyColour
        agency_id (Union[None, Unset, int]): Gets or Sets AgencyId
        agency_logo (Union[None, Unset, str]): Gets or Sets AgencyLogo
        url (Union[None, Unset, str]): Gets or Sets Url
    """

    on_market_types: Union[List[PropertiesV1AdvertOnMarketTypesType0Item], None, Unset] = UNSET
    advert_id: Union[None, Unset, int] = UNSET
    agency: Union[None, Unset, str] = UNSET
    agency_colour: Union[None, Unset, str] = UNSET
    agency_id: Union[None, Unset, int] = UNSET
    agency_logo: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        advert_id: Union[None, Unset, int]
        if isinstance(self.advert_id, Unset):
            advert_id = UNSET
        else:
            advert_id = self.advert_id

        agency: Union[None, Unset, str]
        if isinstance(self.agency, Unset):
            agency = UNSET
        else:
            agency = self.agency

        agency_colour: Union[None, Unset, str]
        if isinstance(self.agency_colour, Unset):
            agency_colour = UNSET
        else:
            agency_colour = self.agency_colour

        agency_id: Union[None, Unset, int]
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        else:
            agency_id = self.agency_id

        agency_logo: Union[None, Unset, str]
        if isinstance(self.agency_logo, Unset):
            agency_logo = UNSET
        else:
            agency_logo = self.agency_logo

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if on_market_types is not UNSET:
            field_dict["onMarketTypes"] = on_market_types
        if advert_id is not UNSET:
            field_dict["advertId"] = advert_id
        if agency is not UNSET:
            field_dict["agency"] = agency
        if agency_colour is not UNSET:
            field_dict["agencyColour"] = agency_colour
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if agency_logo is not UNSET:
            field_dict["agencyLogo"] = agency_logo
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_on_market_types(data: object) -> Union[List[PropertiesV1AdvertOnMarketTypesType0Item], None, Unset]:
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
                    on_market_types_type_0_item = PropertiesV1AdvertOnMarketTypesType0Item(
                        on_market_types_type_0_item_data
                    )

                    on_market_types_type_0.append(on_market_types_type_0_item)

                return on_market_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[PropertiesV1AdvertOnMarketTypesType0Item], None, Unset], data)

        on_market_types = _parse_on_market_types(d.pop("onMarketTypes", UNSET))

        def _parse_advert_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        advert_id = _parse_advert_id(d.pop("advertId", UNSET))

        def _parse_agency(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency = _parse_agency(d.pop("agency", UNSET))

        def _parse_agency_colour(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_colour = _parse_agency_colour(d.pop("agencyColour", UNSET))

        def _parse_agency_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        agency_id = _parse_agency_id(d.pop("agencyId", UNSET))

        def _parse_agency_logo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_logo = _parse_agency_logo(d.pop("agencyLogo", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        properties_v1_advert = cls(
            on_market_types=on_market_types,
            advert_id=advert_id,
            agency=agency,
            agency_colour=agency_colour,
            agency_id=agency_id,
            agency_logo=agency_logo,
            url=url,
        )

        return properties_v1_advert
