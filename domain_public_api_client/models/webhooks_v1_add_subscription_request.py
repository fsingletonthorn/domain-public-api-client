from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhooksV1AddSubscriptionRequest")


@_attrs_define
class WebhooksV1AddSubscriptionRequest:
    """AddSubscriptionRequest

    Attributes:
        resource_type (str): Gets or Sets ResourceType
        owner_type (str): Gets or Sets OwnerType
        owner_id (str): Gets or Sets OwnerId
    """

    resource_type: str
    owner_type: str
    owner_id: str

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type

        owner_type = self.owner_type

        owner_id = self.owner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "resourceType": resource_type,
                "ownerType": owner_type,
                "ownerId": owner_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource_type = d.pop("resourceType")

        owner_type = d.pop("ownerType")

        owner_id = d.pop("ownerId")

        webhooks_v1_add_subscription_request = cls(
            resource_type=resource_type,
            owner_type=owner_type,
            owner_id=owner_id,
        )

        return webhooks_v1_add_subscription_request
