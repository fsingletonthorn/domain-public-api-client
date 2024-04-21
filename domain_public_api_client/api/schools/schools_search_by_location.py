from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schools_v2_school_with_distance import SchoolsV2SchoolWithDistance
from ...types import Response


def _get_kwargs(
    latitude: float,
    longitude: float,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/schools/{latitude}/{longitude}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["SchoolsV2SchoolWithDistance"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SchoolsV2SchoolWithDistance.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["SchoolsV2SchoolWithDistance"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    latitude: float,
    longitude: float,
    *,
    client: AuthenticatedClient,
) -> Response[List["SchoolsV2SchoolWithDistance"]]:
    """Search for a school in a location

    Args:
        latitude (float):
        longitude (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['SchoolsV2SchoolWithDistance']]
    """

    kwargs = _get_kwargs(
        latitude=latitude,
        longitude=longitude,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    latitude: float,
    longitude: float,
    *,
    client: AuthenticatedClient,
) -> Optional[List["SchoolsV2SchoolWithDistance"]]:
    """Search for a school in a location

    Args:
        latitude (float):
        longitude (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['SchoolsV2SchoolWithDistance']
    """

    return sync_detailed(
        latitude=latitude,
        longitude=longitude,
        client=client,
    ).parsed


async def asyncio_detailed(
    latitude: float,
    longitude: float,
    *,
    client: AuthenticatedClient,
) -> Response[List["SchoolsV2SchoolWithDistance"]]:
    """Search for a school in a location

    Args:
        latitude (float):
        longitude (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['SchoolsV2SchoolWithDistance']]
    """

    kwargs = _get_kwargs(
        latitude=latitude,
        longitude=longitude,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    latitude: float,
    longitude: float,
    *,
    client: AuthenticatedClient,
) -> Optional[List["SchoolsV2SchoolWithDistance"]]:
    """Search for a school in a location

    Args:
        latitude (float):
        longitude (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['SchoolsV2SchoolWithDistance']
    """

    return (
        await asyncio_detailed(
            latitude=latitude,
            longitude=longitude,
            client=client,
        )
    ).parsed
