from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_avm_piv1_problem_details import DomainAvmPIV1ProblemDetails
from ...models.domain_avm_piv1_property_price_estimate import DomainAvmPIV1PropertyPriceEstimate
from ...types import Response


def _get_kwargs(
    property_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/properties/{property_id}/priceEstimate",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainAvmPIV1PropertyPriceEstimate.from_dict(response.text)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = DomainAvmPIV1ProblemDetails.from_dict(response.text)

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = DomainAvmPIV1ProblemDetails.from_dict(response.text)

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = DomainAvmPIV1ProblemDetails.from_dict(response.text)

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    property_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]]:
    """Price estimates based on propertyId

    Args:
        property_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]]
    """

    kwargs = _get_kwargs(
        property_id=property_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    property_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]]:
    """Price estimates based on propertyId

    Args:
        property_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]
    """

    return sync_detailed(
        property_id=property_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    property_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]]:
    """Price estimates based on propertyId

    Args:
        property_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]]
    """

    kwargs = _get_kwargs(
        property_id=property_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    property_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]]:
    """Price estimates based on propertyId

    Args:
        property_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DomainAvmPIV1ProblemDetails, DomainAvmPIV1PropertyPriceEstimate]
    """

    return (
        await asyncio_detailed(
            property_id=property_id,
            client=client,
        )
    ).parsed
