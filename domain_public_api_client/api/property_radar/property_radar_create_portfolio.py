from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.property_activity_apiv1_portfolio_created import PropertyActivityAPIV1PortfolioCreated
from ...models.property_radar_create_portfolio_body_type_1 import PropertyRadarCreatePortfolioBodyType1
from ...types import Response


def _get_kwargs(
    *,
    body: Union["PropertyRadarCreatePortfolioBodyType1", Any],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/propertyradar/portfolio",
    }

    _body: Union[Any, Dict[str, Any]]
    if isinstance(body, PropertyRadarCreatePortfolioBodyType1):
        _body = body.to_dict()
    else:
        _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PropertyActivityAPIV1PortfolioCreated]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PropertyActivityAPIV1PortfolioCreated.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PropertyActivityAPIV1PortfolioCreated]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["PropertyRadarCreatePortfolioBodyType1", Any],
) -> Response[Union[Any, PropertyActivityAPIV1PortfolioCreated]]:
    """Create Portfolio

     Creates a portfolio and returns portfolio id

    Args:
        body (Union['PropertyRadarCreatePortfolioBodyType1', Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PropertyActivityAPIV1PortfolioCreated]]
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
    body: Union["PropertyRadarCreatePortfolioBodyType1", Any],
) -> Optional[Union[Any, PropertyActivityAPIV1PortfolioCreated]]:
    """Create Portfolio

     Creates a portfolio and returns portfolio id

    Args:
        body (Union['PropertyRadarCreatePortfolioBodyType1', Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PropertyActivityAPIV1PortfolioCreated]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["PropertyRadarCreatePortfolioBodyType1", Any],
) -> Response[Union[Any, PropertyActivityAPIV1PortfolioCreated]]:
    """Create Portfolio

     Creates a portfolio and returns portfolio id

    Args:
        body (Union['PropertyRadarCreatePortfolioBodyType1', Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PropertyActivityAPIV1PortfolioCreated]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union["PropertyRadarCreatePortfolioBodyType1", Any],
) -> Optional[Union[Any, PropertyActivityAPIV1PortfolioCreated]]:
    """Create Portfolio

     Creates a portfolio and returns portfolio id

    Args:
        body (Union['PropertyRadarCreatePortfolioBodyType1', Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PropertyActivityAPIV1PortfolioCreated]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
