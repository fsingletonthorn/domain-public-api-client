from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeV1MyDetails")


@_attrs_define
class MeV1MyDetails:
    """
    Attributes:
        authenticated (Union[Unset, bool]): True if the current request was successfully authenticated
        client_id (Union[None, Unset, str]): The Client ID or API Key used to authenticated this request
        subject_id (Union[None, Unset, str]): A unique user id, only if this request is authenticated as a user context.
        subject_email (Union[None, Unset, str]): The users email address if available
    """

    authenticated: Union[Unset, bool] = UNSET
    client_id: Union[None, Unset, str] = UNSET
    subject_id: Union[None, Unset, str] = UNSET
    subject_email: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        authenticated = self.authenticated

        client_id: Union[None, Unset, str]
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        subject_id: Union[None, Unset, str]
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        else:
            subject_id = self.subject_id

        subject_email: Union[None, Unset, str]
        if isinstance(self.subject_email, Unset):
            subject_email = UNSET
        else:
            subject_email = self.subject_email

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id
        if subject_email is not UNSET:
            field_dict["subjectEmail"] = subject_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authenticated = d.pop("authenticated", UNSET)

        def _parse_client_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_id = _parse_client_id(d.pop("clientId", UNSET))

        def _parse_subject_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject_id = _parse_subject_id(d.pop("subjectId", UNSET))

        def _parse_subject_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject_email = _parse_subject_email(d.pop("subjectEmail", UNSET))

        me_v1_my_details = cls(
            authenticated=authenticated,
            client_id=client_id,
            subject_id=subject_id,
            subject_email=subject_email,
        )

        return me_v1_my_details
