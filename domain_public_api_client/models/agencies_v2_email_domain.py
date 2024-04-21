from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgenciesV2EmailDomain")


@_attrs_define
class AgenciesV2EmailDomain:
    """EmailDomain

    Attributes:
        domain (Union[None, Unset, str]): Gets or Sets Domain
    """

    domain: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        domain: Union[None, Unset, str]
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_domain(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        domain = _parse_domain(d.pop("domain", UNSET))

        agencies_v2_email_domain = cls(
            domain=domain,
        )

        return agencies_v2_email_domain
