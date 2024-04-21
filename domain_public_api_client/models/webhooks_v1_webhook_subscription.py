import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhooksV1WebhookSubscription")


@_attrs_define
class WebhooksV1WebhookSubscription:
    """
    Attributes:
        id (Union[None, Unset, str]):
        created_by (Union[None, Unset, str]): Gets or Sets CreatedBy
        created (Union[None, Unset, datetime.datetime]): Gets or Sets Created
        updated_by (Union[None, Unset, str]): Gets or Sets UpdatedBy
        updated (Union[None, Unset, datetime.datetime]): Gets or Sets Updated
        deleted_by (Union[None, Unset, str]): Gets or Sets DeletedBy
        deleted (Union[None, Unset, datetime.datetime]): Gets or Sets Deleted
        subscription_id (Union[None, Unset, str]): Gets or Sets SubscriptionId
        subscriber_id (Union[None, Unset, str]): Gets or Sets SubscriberId
        owner_type (Union[None, Unset, str]): Gets or Sets OwnerType
        owner_id (Union[None, Unset, str]): Gets or Sets OwnerId
        resource_type (Union[None, Unset, str]): Gets or Sets ResourceType
    """

    id: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    created: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    updated: Union[None, Unset, datetime.datetime] = UNSET
    deleted_by: Union[None, Unset, str] = UNSET
    deleted: Union[None, Unset, datetime.datetime] = UNSET
    subscription_id: Union[None, Unset, str] = UNSET
    subscriber_id: Union[None, Unset, str] = UNSET
    owner_type: Union[None, Unset, str] = UNSET
    owner_id: Union[None, Unset, str] = UNSET
    resource_type: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        created: Union[None, Unset, str]
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        updated: Union[None, Unset, str]
        if isinstance(self.updated, Unset):
            updated = UNSET
        elif isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        deleted_by: Union[None, Unset, str]
        if isinstance(self.deleted_by, Unset):
            deleted_by = UNSET
        else:
            deleted_by = self.deleted_by

        deleted: Union[None, Unset, str]
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        elif isinstance(self.deleted, datetime.datetime):
            deleted = self.deleted.isoformat()
        else:
            deleted = self.deleted

        subscription_id: Union[None, Unset, str]
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = self.subscription_id

        subscriber_id: Union[None, Unset, str]
        if isinstance(self.subscriber_id, Unset):
            subscriber_id = UNSET
        else:
            subscriber_id = self.subscriber_id

        owner_type: Union[None, Unset, str]
        if isinstance(self.owner_type, Unset):
            owner_type = UNSET
        else:
            owner_type = self.owner_type

        owner_id: Union[None, Unset, str]
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        resource_type: Union[None, Unset, str]
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created is not UNSET:
            field_dict["created"] = created
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if updated is not UNSET:
            field_dict["updated"] = updated
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscriber_id is not UNSET:
            field_dict["subscriberId"] = subscriber_id
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

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

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updatedBy", UNSET))

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

        def _parse_deleted_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_by = _parse_deleted_by(d.pop("deletedBy", UNSET))

        def _parse_deleted(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_type_0 = isoparse(data)

                return deleted_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        def _parse_subscription_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))

        def _parse_subscriber_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subscriber_id = _parse_subscriber_id(d.pop("subscriberId", UNSET))

        def _parse_owner_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        owner_type = _parse_owner_type(d.pop("ownerType", UNSET))

        def _parse_owner_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))

        def _parse_resource_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resource_type = _parse_resource_type(d.pop("resourceType", UNSET))

        webhooks_v1_webhook_subscription = cls(
            id=id,
            created_by=created_by,
            created=created,
            updated_by=updated_by,
            updated=updated,
            deleted_by=deleted_by,
            deleted=deleted,
            subscription_id=subscription_id,
            subscriber_id=subscriber_id,
            owner_type=owner_type,
            owner_id=owner_id,
            resource_type=resource_type,
        )

        return webhooks_v1_webhook_subscription
