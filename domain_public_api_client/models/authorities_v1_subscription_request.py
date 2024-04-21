from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthoritiesV1SubscriptionRequest")


@_attrs_define
class AuthoritiesV1SubscriptionRequest:
    """
    Attributes:
        webhook_id (Union[Unset, str]):  Example: whk_7d9c8f4a0cb54b948a010bb56ea98fe0.
    """

    webhook_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        webhook_id = self.webhook_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        webhook_id = d.pop("webhookId", UNSET)

        authorities_v1_subscription_request = cls(
            webhook_id=webhook_id,
        )

        authorities_v1_subscription_request.additional_properties = d
        return authorities_v1_subscription_request

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
