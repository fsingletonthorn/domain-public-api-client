from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PreMarketV1StatementOfInformation")


@_attrs_define
class PreMarketV1StatementOfInformation:
    """
    Attributes:
        documentation_url (str): Link to the statement of information documentation file.
            Must be a PDF file.
            File should be less than 10 MB in size
            The Statement of Information must be updated if there is a change in the indicative selling price.
    """

    documentation_url: str

    def to_dict(self) -> Dict[str, Any]:
        documentation_url = self.documentation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "documentationUrl": documentation_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        documentation_url = d.pop("documentationUrl")

        pre_market_v1_statement_of_information = cls(
            documentation_url=documentation_url,
        )

        return pre_market_v1_statement_of_information
