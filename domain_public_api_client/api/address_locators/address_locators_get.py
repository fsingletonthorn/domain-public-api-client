from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_locators_v1_address_data_model import AddressLocatorsV1AddressDataModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search_level: Union[Unset, str] = UNSET,
    unit_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    suburb: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["searchLevel"] = search_level

    params["unitNumber"] = unit_number

    params["streetNumber"] = street_number

    params["streetName"] = street_name

    params["streetType"] = street_type

    params["suburb"] = suburb

    params["state"] = state

    params["postcode"] = postcode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/addressLocators",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AddressLocatorsV1AddressDataModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AddressLocatorsV1AddressDataModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AddressLocatorsV1AddressDataModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    search_level: Union[Unset, str] = UNSET,
    unit_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    suburb: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
) -> Response[List["AddressLocatorsV1AddressDataModel"]]:
    """Retrieves matching ids for use in other services.

     Use this endpoint to retrieve IDs that may be used to query information from other endpoints.

    For example use `id` of the `Suburb` level to query
    [`demographics`](/docs/v1/apis/pkg_properties_locations/references/demographics_get)

    Args:
        search_level (Union[Unset, str]):
        unit_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        suburb (Union[Unset, str]):
        state (Union[Unset, str]):
        postcode (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AddressLocatorsV1AddressDataModel']]
    """

    kwargs = _get_kwargs(
        search_level=search_level,
        unit_number=unit_number,
        street_number=street_number,
        street_name=street_name,
        street_type=street_type,
        suburb=suburb,
        state=state,
        postcode=postcode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    search_level: Union[Unset, str] = UNSET,
    unit_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    suburb: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
) -> Optional[List["AddressLocatorsV1AddressDataModel"]]:
    """Retrieves matching ids for use in other services.

     Use this endpoint to retrieve IDs that may be used to query information from other endpoints.

    For example use `id` of the `Suburb` level to query
    [`demographics`](/docs/v1/apis/pkg_properties_locations/references/demographics_get)

    Args:
        search_level (Union[Unset, str]):
        unit_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        suburb (Union[Unset, str]):
        state (Union[Unset, str]):
        postcode (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AddressLocatorsV1AddressDataModel']
    """

    return sync_detailed(
        client=client,
        search_level=search_level,
        unit_number=unit_number,
        street_number=street_number,
        street_name=street_name,
        street_type=street_type,
        suburb=suburb,
        state=state,
        postcode=postcode,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search_level: Union[Unset, str] = UNSET,
    unit_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    suburb: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
) -> Response[List["AddressLocatorsV1AddressDataModel"]]:
    """Retrieves matching ids for use in other services.

     Use this endpoint to retrieve IDs that may be used to query information from other endpoints.

    For example use `id` of the `Suburb` level to query
    [`demographics`](/docs/v1/apis/pkg_properties_locations/references/demographics_get)

    Args:
        search_level (Union[Unset, str]):
        unit_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        suburb (Union[Unset, str]):
        state (Union[Unset, str]):
        postcode (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AddressLocatorsV1AddressDataModel']]
    """

    kwargs = _get_kwargs(
        search_level=search_level,
        unit_number=unit_number,
        street_number=street_number,
        street_name=street_name,
        street_type=street_type,
        suburb=suburb,
        state=state,
        postcode=postcode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    search_level: Union[Unset, str] = UNSET,
    unit_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    suburb: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
) -> Optional[List["AddressLocatorsV1AddressDataModel"]]:
    """Retrieves matching ids for use in other services.

     Use this endpoint to retrieve IDs that may be used to query information from other endpoints.

    For example use `id` of the `Suburb` level to query
    [`demographics`](/docs/v1/apis/pkg_properties_locations/references/demographics_get)

    Args:
        search_level (Union[Unset, str]):
        unit_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        suburb (Union[Unset, str]):
        state (Union[Unset, str]):
        postcode (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AddressLocatorsV1AddressDataModel']
    """

    return (
        await asyncio_detailed(
            client=client,
            search_level=search_level,
            unit_number=unit_number,
            street_number=street_number,
            street_name=street_name,
            street_type=street_type,
            suburb=suburb,
            state=state,
            postcode=postcode,
        )
    ).parsed
