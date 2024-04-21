from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disclaimers_v1_disclaimer_model import DisclaimersV1DisclaimerModel
from ...types import Response


def _get_kwargs(
    product: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/disclaimers/product/{product}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DisclaimersV1DisclaimerModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DisclaimersV1DisclaimerModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["DisclaimersV1DisclaimerModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["DisclaimersV1DisclaimerModel"]]:
    """Retrieves disclaimers for given product

    Args:
        product (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DisclaimersV1DisclaimerModel']]
    """

    kwargs = _get_kwargs(
        product=product,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["DisclaimersV1DisclaimerModel"]]:
    """Retrieves disclaimers for given product

    Args:
        product (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DisclaimersV1DisclaimerModel']
    """

    return sync_detailed(
        product=product,
        client=client,
    ).parsed


async def asyncio_detailed(
    product: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["DisclaimersV1DisclaimerModel"]]:
    """Retrieves disclaimers for given product

    Args:
        product (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DisclaimersV1DisclaimerModel']]
    """

    kwargs = _get_kwargs(
        product=product,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["DisclaimersV1DisclaimerModel"]]:
    """Retrieves disclaimers for given product

    Args:
        product (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DisclaimersV1DisclaimerModel']
    """

    return (
        await asyncio_detailed(
            product=product,
            client=client,
        )
    ).parsed
