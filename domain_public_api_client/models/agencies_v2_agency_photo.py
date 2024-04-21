from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgenciesV2AgencyPhoto")


@_attrs_define
class AgenciesV2AgencyPhoto:
    """AgencyPhoto

    Attributes:
        url (Union[None, Unset, str]): Gets or Sets Url
    """

    url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        agencies_v2_agency_photo = cls(
            url=url,
        )

        return agencies_v2_agency_photo
