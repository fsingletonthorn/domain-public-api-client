from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisclaimersV1DisclaimerModel")


@_attrs_define
class DisclaimersV1DisclaimerModel:
    """APMAPIModelsDisclaimerV2DisclaimerModel

    Attributes:
        id (Union[None, Unset, str]): Gets or Sets Id
        version (Union[None, Unset, str]): Gets or Sets Version
        text (Union[None, Unset, str]): Gets or Sets Text
        imageurl (Union[None, Unset, str]): Gets or Sets Imageurl
        authorityname (Union[None, Unset, str]): Gets or Sets Authorityname
    """

    id: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    text: Union[None, Unset, str] = UNSET
    imageurl: Union[None, Unset, str] = UNSET
    authorityname: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        imageurl: Union[None, Unset, str]
        if isinstance(self.imageurl, Unset):
            imageurl = UNSET
        else:
            imageurl = self.imageurl

        authorityname: Union[None, Unset, str]
        if isinstance(self.authorityname, Unset):
            authorityname = UNSET
        else:
            authorityname = self.authorityname

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if text is not UNSET:
            field_dict["text"] = text
        if imageurl is not UNSET:
            field_dict["imageurl"] = imageurl
        if authorityname is not UNSET:
            field_dict["authorityname"] = authorityname

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

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_imageurl(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        imageurl = _parse_imageurl(d.pop("imageurl", UNSET))

        def _parse_authorityname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        authorityname = _parse_authorityname(d.pop("authorityname", UNSET))

        disclaimers_v1_disclaimer_model = cls(
            id=id,
            version=version,
            text=text,
            imageurl=imageurl,
            authorityname=authorityname,
        )

        return disclaimers_v1_disclaimer_model
