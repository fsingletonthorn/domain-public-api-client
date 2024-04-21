from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_domain_search_contracts_v2_project_promo_level import (
    DomainSearchServiceV2ModelDomainSearchContractsV2ProjectPromoLevel,
)
from ..models.domain_search_service_v2_model_domain_search_contracts_v2_project_state import (
    DomainSearchServiceV2ModelDomainSearchContractsV2ProjectState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_media import (
        DomainSearchServiceV2ModelDomainSearchContractsV2Media,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2Project")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2Project:
    """
    Attributes:
        promo_level (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2ProjectPromoLevel]):
        state (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2ProjectState]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        banner_url (Union[Unset, str]):
        preferred_color_hex (Union[Unset, str]):
        logo_url (Union[Unset, str]):
        labels (Union[Unset, List[str]]):
        displayable_address (Union[Unset, str]):
        suburb (Union[Unset, str]):
        suburb_id (Union[Unset, int]):
        features (Union[Unset, List[str]]):
        media (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchContractsV2Media']]):
        project_slug (Union[Unset, str]):
    """

    promo_level: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2ProjectPromoLevel] = UNSET
    state: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2ProjectState] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    banner_url: Union[Unset, str] = UNSET
    preferred_color_hex: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    labels: Union[Unset, List[str]] = UNSET
    displayable_address: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    suburb_id: Union[Unset, int] = UNSET
    features: Union[Unset, List[str]] = UNSET
    media: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchContractsV2Media"]] = UNSET
    project_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promo_level: Union[Unset, str] = UNSET
        if not isinstance(self.promo_level, Unset):
            promo_level = self.promo_level.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        id = self.id

        name = self.name

        banner_url = self.banner_url

        preferred_color_hex = self.preferred_color_hex

        logo_url = self.logo_url

        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        displayable_address = self.displayable_address

        suburb = self.suburb

        suburb_id = self.suburb_id

        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        media: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        project_slug = self.project_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promo_level is not UNSET:
            field_dict["promoLevel"] = promo_level
        if state is not UNSET:
            field_dict["state"] = state
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if banner_url is not UNSET:
            field_dict["bannerUrl"] = banner_url
        if preferred_color_hex is not UNSET:
            field_dict["preferredColorHex"] = preferred_color_hex
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if labels is not UNSET:
            field_dict["labels"] = labels
        if displayable_address is not UNSET:
            field_dict["displayableAddress"] = displayable_address
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if suburb_id is not UNSET:
            field_dict["suburbId"] = suburb_id
        if features is not UNSET:
            field_dict["features"] = features
        if media is not UNSET:
            field_dict["media"] = media
        if project_slug is not UNSET:
            field_dict["projectSlug"] = project_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_media import (
            DomainSearchServiceV2ModelDomainSearchContractsV2Media,
        )

        d = src_dict.copy()
        _promo_level = d.pop("promoLevel", UNSET)
        promo_level: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2ProjectPromoLevel]
        if isinstance(_promo_level, Unset):
            promo_level = UNSET
        else:
            promo_level = DomainSearchServiceV2ModelDomainSearchContractsV2ProjectPromoLevel(_promo_level)

        _state = d.pop("state", UNSET)
        state: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2ProjectState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DomainSearchServiceV2ModelDomainSearchContractsV2ProjectState(_state)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        banner_url = d.pop("bannerUrl", UNSET)

        preferred_color_hex = d.pop("preferredColorHex", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        labels = cast(List[str], d.pop("labels", UNSET))

        displayable_address = d.pop("displayableAddress", UNSET)

        suburb = d.pop("suburb", UNSET)

        suburb_id = d.pop("suburbId", UNSET)

        features = cast(List[str], d.pop("features", UNSET))

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = DomainSearchServiceV2ModelDomainSearchContractsV2Media.from_dict(media_item_data)

            media.append(media_item)

        project_slug = d.pop("projectSlug", UNSET)

        domain_search_service_v2_model_domain_search_contracts_v2_project = cls(
            promo_level=promo_level,
            state=state,
            id=id,
            name=name,
            banner_url=banner_url,
            preferred_color_hex=preferred_color_hex,
            logo_url=logo_url,
            labels=labels,
            displayable_address=displayable_address,
            suburb=suburb,
            suburb_id=suburb_id,
            features=features,
            media=media,
            project_slug=project_slug,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_project.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_project

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
