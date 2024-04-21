from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pre_market_v1_listing_request_operation import PreMarketV1ListingRequestOperation
    from ..models.pre_market_v1i_contract_resolver import PreMarketV1IContractResolver


T = TypeVar("T", bound="PreMarketV1ListingRequestJsonPatchDocument")


@_attrs_define
class PreMarketV1ListingRequestJsonPatchDocument:
    """
    Attributes:
        operations (Union[List['PreMarketV1ListingRequestOperation'], None, Unset]):
        contract_resolver (Union[Unset, PreMarketV1IContractResolver]):
    """

    operations: Union[List["PreMarketV1ListingRequestOperation"], None, Unset] = UNSET
    contract_resolver: Union[Unset, "PreMarketV1IContractResolver"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        operations: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.operations, Unset):
            operations = UNSET
        elif isinstance(self.operations, list):
            operations = []
            for operations_type_0_item_data in self.operations:
                operations_type_0_item = operations_type_0_item_data.to_dict()
                operations.append(operations_type_0_item)

        else:
            operations = self.operations

        contract_resolver: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contract_resolver, Unset):
            contract_resolver = self.contract_resolver.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if operations is not UNSET:
            field_dict["operations"] = operations
        if contract_resolver is not UNSET:
            field_dict["contractResolver"] = contract_resolver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pre_market_v1_listing_request_operation import PreMarketV1ListingRequestOperation
        from ..models.pre_market_v1i_contract_resolver import PreMarketV1IContractResolver

        d = src_dict.copy()

        def _parse_operations(data: object) -> Union[List["PreMarketV1ListingRequestOperation"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                operations_type_0 = []
                _operations_type_0 = data
                for operations_type_0_item_data in _operations_type_0:
                    operations_type_0_item = PreMarketV1ListingRequestOperation.from_dict(operations_type_0_item_data)

                    operations_type_0.append(operations_type_0_item)

                return operations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PreMarketV1ListingRequestOperation"], None, Unset], data)

        operations = _parse_operations(d.pop("operations", UNSET))

        _contract_resolver = d.pop("contractResolver", UNSET)
        contract_resolver: Union[Unset, PreMarketV1IContractResolver]
        if isinstance(_contract_resolver, Unset):
            contract_resolver = UNSET
        else:
            contract_resolver = PreMarketV1IContractResolver.from_dict(_contract_resolver)

        pre_market_v1_listing_request_json_patch_document = cls(
            operations=operations,
            contract_resolver=contract_resolver,
        )

        return pre_market_v1_listing_request_json_patch_document
