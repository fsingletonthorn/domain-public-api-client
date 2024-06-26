from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_location_profiles_service_v1_model_location import DomainLocationProfilesServiceV1ModelLocation
from ...types import Response


def _get_kwargs(
    domain_location_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/locations/profiles/{domain_location_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DomainLocationProfilesServiceV1ModelLocation]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainLocationProfilesServiceV1ModelLocation.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DomainLocationProfilesServiceV1ModelLocation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    domain_location_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, DomainLocationProfilesServiceV1ModelLocation]]:
    """Get location data based on the given domainLocationId

    Args:
        domain_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainLocationProfilesServiceV1ModelLocation]]
    """

    kwargs = _get_kwargs(
        domain_location_id=domain_location_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    domain_location_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, DomainLocationProfilesServiceV1ModelLocation]]:
    """Get location data based on the given domainLocationId

    Args:
        domain_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DomainLocationProfilesServiceV1ModelLocation]
    """

    return sync_detailed(
        domain_location_id=domain_location_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain_location_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, DomainLocationProfilesServiceV1ModelLocation]]:
    """Get location data based on the given domainLocationId

    Args:
        domain_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainLocationProfilesServiceV1ModelLocation]]
    """

    kwargs = _get_kwargs(
        domain_location_id=domain_location_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    domain_location_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, DomainLocationProfilesServiceV1ModelLocation]]:
    """Get location data based on the given domainLocationId

    Args:
        domain_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DomainLocationProfilesServiceV1ModelLocation]
    """

    return (
        await asyncio_detailed(
            domain_location_id=domain_location_id,
            client=client,
        )
    ).parsed
