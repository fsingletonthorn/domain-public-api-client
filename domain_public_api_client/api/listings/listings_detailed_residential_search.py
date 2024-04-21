from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_search_service_v2_model_domain_search_contracts_v2_search_result import (
    DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult,
)
from ...models.domain_search_service_v2_model_domain_search_web_api_v2_models_search_parameters import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/residential/_search",
    }

    if isinstance(body, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult"]]:
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
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
    ],
) -> Response[List["DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult"]]:
    """Retrieves residential listings matching the specified criteria.

     Search results are limited to the first 1000 results.

    If the number of results is greater, the intention is to refine the search by adding more
    restrictive parameters, to find a relevant set of results.

    Args:
        body (DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):
        body (DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult']]
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
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
    ],
) -> Optional[List["DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult"]]:
    """Retrieves residential listings matching the specified criteria.

     Search results are limited to the first 1000 results.

    If the number of results is greater, the intention is to refine the search by adding more
    restrictive parameters, to find a relevant set of results.

    Args:
        body (DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):
        body (DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
    ],
) -> Response[List["DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult"]]:
    """Retrieves residential listings matching the specified criteria.

     Search results are limited to the first 1000 results.

    If the number of results is greater, the intention is to refine the search by adding more
    restrictive parameters, to find a relevant set of results.

    Args:
        body (DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):
        body (DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult']]
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
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters,
    ],
) -> Optional[List["DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult"]]:
    """Retrieves residential listings matching the specified criteria.

     Search results are limited to the first 1000 results.

    If the number of results is greater, the intention is to refine the search by adding more
    restrictive parameters, to find a relevant set of results.

    Args:
        body (DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):
        body (DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
