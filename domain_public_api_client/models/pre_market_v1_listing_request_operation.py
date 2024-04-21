from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.pre_market_v1_operation_type import PreMarketV1OperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PreMarketV1ListingRequestOperation")


@_attrs_define
class PreMarketV1ListingRequestOperation:
    """
    Attributes:
        operation_type (Union[Unset, PreMarketV1OperationType]):
        path (Union[None, Unset, str]):
        op (Union[None, Unset, str]):
        from_ (Union[None, Unset, str]):
        value (Union[Unset, Any]):
    """

    operation_type: Union[Unset, PreMarketV1OperationType] = UNSET
    path: Union[None, Unset, str] = UNSET
    op: Union[None, Unset, str] = UNSET
    from_: Union[None, Unset, str] = UNSET
    value: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        operation_type: Union[Unset, str] = UNSET
        if not isinstance(self.operation_type, Unset):
            operation_type = self.operation_type.value

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        op: Union[None, Unset, str]
        if isinstance(self.op, Unset):
            op = UNSET
        else:
            op = self.op

        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if operation_type is not UNSET:
            field_dict["operationType"] = operation_type
        if path is not UNSET:
            field_dict["path"] = path
        if op is not UNSET:
            field_dict["op"] = op
        if from_ is not UNSET:
            field_dict["from"] = from_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _operation_type = d.pop("operationType", UNSET)
        operation_type: Union[Unset, PreMarketV1OperationType]
        if isinstance(_operation_type, Unset):
            operation_type = UNSET
        else:
            operation_type = PreMarketV1OperationType(_operation_type)

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_op(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        op = _parse_op(d.pop("op", UNSET))

        def _parse_from_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        value = d.pop("value", UNSET)

        pre_market_v1_listing_request_operation = cls(
            operation_type=operation_type,
            path=path,
            op=op,
            from_=from_,
            value=value,
        )

        return pre_market_v1_listing_request_operation
