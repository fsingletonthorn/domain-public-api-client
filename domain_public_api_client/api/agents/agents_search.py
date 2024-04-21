from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_agent_search_v1_model_auto_suggest_agent_result_dto import (
    DomainAgentSearchV1ModelAutoSuggestAgentResultDto,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query"] = query

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DomainAgentSearchV1ModelAutoSuggestAgentResultDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DomainAgentSearchV1ModelAutoSuggestAgentResultDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["DomainAgentSearchV1ModelAutoSuggestAgentResultDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[List["DomainAgentSearchV1ModelAutoSuggestAgentResultDto"]]:
    """Search for agents by name.

     The returned Agent ID can be used to get an agent details by ID. See `GET /agents/{id}/`

    Args:
        query (str):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainAgentSearchV1ModelAutoSuggestAgentResultDto']]
    """

    kwargs = _get_kwargs(
        query=query,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[List["DomainAgentSearchV1ModelAutoSuggestAgentResultDto"]]:
    """Search for agents by name.

     The returned Agent ID can be used to get an agent details by ID. See `GET /agents/{id}/`

    Args:
        query (str):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainAgentSearchV1ModelAutoSuggestAgentResultDto']
    """

    return sync_detailed(
        client=client,
        query=query,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[List["DomainAgentSearchV1ModelAutoSuggestAgentResultDto"]]:
    """Search for agents by name.

     The returned Agent ID can be used to get an agent details by ID. See `GET /agents/{id}/`

    Args:
        query (str):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainAgentSearchV1ModelAutoSuggestAgentResultDto']]
    """

    kwargs = _get_kwargs(
        query=query,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[List["DomainAgentSearchV1ModelAutoSuggestAgentResultDto"]]:
    """Search for agents by name.

     The returned Agent ID can be used to get an agent details by ID. See `GET /agents/{id}/`

    Args:
        query (str):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainAgentSearchV1ModelAutoSuggestAgentResultDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed
