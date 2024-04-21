from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_listing_admin_service_v1_model_listing_report import DomainListingAdminServiceV1ModelListingReport
from ...types import UNSET, Response


def _get_kwargs(
    *,
    agency_id: int,
    provider_ad_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["agencyId"] = agency_id

    params["providerAdId"] = provider_ad_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/processingReports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DomainListingAdminServiceV1ModelListingReport"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DomainListingAdminServiceV1ModelListingReport.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["DomainListingAdminServiceV1ModelListingReport"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    agency_id: int,
    provider_ad_id: str,
) -> Response[List["DomainListingAdminServiceV1ModelListingReport"]]:
    """Searches processing reports

    Args:
        agency_id (int):
        provider_ad_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainListingAdminServiceV1ModelListingReport']]
    """

    kwargs = _get_kwargs(
        agency_id=agency_id,
        provider_ad_id=provider_ad_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    agency_id: int,
    provider_ad_id: str,
) -> Optional[List["DomainListingAdminServiceV1ModelListingReport"]]:
    """Searches processing reports

    Args:
        agency_id (int):
        provider_ad_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainListingAdminServiceV1ModelListingReport']
    """

    return sync_detailed(
        client=client,
        agency_id=agency_id,
        provider_ad_id=provider_ad_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    agency_id: int,
    provider_ad_id: str,
) -> Response[List["DomainListingAdminServiceV1ModelListingReport"]]:
    """Searches processing reports

    Args:
        agency_id (int):
        provider_ad_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainListingAdminServiceV1ModelListingReport']]
    """

    kwargs = _get_kwargs(
        agency_id=agency_id,
        provider_ad_id=provider_ad_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    agency_id: int,
    provider_ad_id: str,
) -> Optional[List["DomainListingAdminServiceV1ModelListingReport"]]:
    """Searches processing reports

    Args:
        agency_id (int):
        provider_ad_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainListingAdminServiceV1ModelListingReport']
    """

    return (
        await asyncio_detailed(
            client=client,
            agency_id=agency_id,
            provider_ad_id=provider_ad_id,
        )
    ).parsed
