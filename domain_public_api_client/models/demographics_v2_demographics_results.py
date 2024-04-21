from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.demographics_v2_demographics import DemographicsV2Demographics


T = TypeVar("T", bound="DemographicsV2DemographicsResults")


@_attrs_define
class DemographicsV2DemographicsResults:
    """DemographicsResultsModel

    Attributes:
        demographics (Union[List['DemographicsV2Demographics'], None, Unset]): Gets or Sets Demographics
    """

    demographics: Union[List["DemographicsV2Demographics"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        demographics: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.demographics, Unset):
            demographics = UNSET
        elif isinstance(self.demographics, list):
            demographics = []
            for demographics_type_0_item_data in self.demographics:
                demographics_type_0_item = demographics_type_0_item_data.to_dict()
                demographics.append(demographics_type_0_item)

        else:
            demographics = self.demographics

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if demographics is not UNSET:
            field_dict["demographics"] = demographics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.demographics_v2_demographics import DemographicsV2Demographics

        d = src_dict.copy()

        def _parse_demographics(data: object) -> Union[List["DemographicsV2Demographics"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                demographics_type_0 = []
                _demographics_type_0 = data
                for demographics_type_0_item_data in _demographics_type_0:
                    demographics_type_0_item = DemographicsV2Demographics.from_dict(demographics_type_0_item_data)

                    demographics_type_0.append(demographics_type_0_item)

                return demographics_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["DemographicsV2Demographics"], None, Unset], data)

        demographics = _parse_demographics(d.pop("demographics", UNSET))

        demographics_v2_demographics_results = cls(
            demographics=demographics,
        )

        return demographics_v2_demographics_results
