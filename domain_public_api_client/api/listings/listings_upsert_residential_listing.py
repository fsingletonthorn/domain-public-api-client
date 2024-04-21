from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_listing_admin_service_v1_model_listing_response import (
    DomainListingAdminServiceV1ModelListingResponse,
)
from ...models.domain_listing_admin_service_v1_model_residential_listing import (
    DomainListingAdminServiceV1ModelResidentialListing,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        DomainListingAdminServiceV1ModelResidentialListing,
        DomainListingAdminServiceV1ModelResidentialListing,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v1/listings/residential",
    }

    if isinstance(body, DomainListingAdminServiceV1ModelResidentialListing):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DomainListingAdminServiceV1ModelResidentialListing):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DomainListingAdminServiceV1ModelListingResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainListingAdminServiceV1ModelListingResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = DomainListingAdminServiceV1ModelListingResponse.from_dict(response.json())

        return response_202
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DomainListingAdminServiceV1ModelListingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainListingAdminServiceV1ModelResidentialListing,
        DomainListingAdminServiceV1ModelResidentialListing,
    ],
) -> Response[DomainListingAdminServiceV1ModelListingResponse]:
    """Creates or updates a residential listing

    Args:
        body (DomainListingAdminServiceV1ModelResidentialListing): Residential Listing
        body (DomainListingAdminServiceV1ModelResidentialListing): Residential Listing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainListingAdminServiceV1ModelListingResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainListingAdminServiceV1ModelResidentialListing,
        DomainListingAdminServiceV1ModelResidentialListing,
    ],
) -> Optional[DomainListingAdminServiceV1ModelListingResponse]:
    """Creates or updates a residential listing

    Args:
        body (DomainListingAdminServiceV1ModelResidentialListing): Residential Listing
        body (DomainListingAdminServiceV1ModelResidentialListing): Residential Listing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainListingAdminServiceV1ModelListingResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainListingAdminServiceV1ModelResidentialListing,
        DomainListingAdminServiceV1ModelResidentialListing,
    ],
) -> Response[DomainListingAdminServiceV1ModelListingResponse]:
    """Creates or updates a residential listing

    Args:
        body (DomainListingAdminServiceV1ModelResidentialListing): Residential Listing
        body (DomainListingAdminServiceV1ModelResidentialListing): Residential Listing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainListingAdminServiceV1ModelListingResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainListingAdminServiceV1ModelResidentialListing,
        DomainListingAdminServiceV1ModelResidentialListing,
    ],
) -> Optional[DomainListingAdminServiceV1ModelListingResponse]:
    """Creates or updates a residential listing

    Args:
        body (DomainListingAdminServiceV1ModelResidentialListing): Residential Listing
        body (DomainListingAdminServiceV1ModelResidentialListing): Residential Listing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainListingAdminServiceV1ModelListingResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
