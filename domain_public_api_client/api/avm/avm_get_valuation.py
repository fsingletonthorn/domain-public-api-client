from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_avm_v1_problem_details import DomainAvmV1ProblemDetails
from ...models.domain_avm_v1_request import DomainAvmV1Request
from ...models.domain_avm_v1_response import DomainAvmV1Response
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        DomainAvmV1Request,
        DomainAvmV1Request,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/avm/getvaluation",
    }

    if isinstance(body, DomainAvmV1Request):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DomainAvmV1Request):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainAvmV1Response.from_dict(response.text)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = DomainAvmV1ProblemDetails.from_dict(response.text)

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = DomainAvmV1ProblemDetails.from_dict(response.text)

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = DomainAvmV1ProblemDetails.from_dict(response.text)

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]]:
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
        DomainAvmV1Request,
        DomainAvmV1Request,
    ],
) -> Response[Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]]:
    """Creates a bank grade valuation and PDF report for a given property address or GnafPId.

    Args:
        body (DomainAvmV1Request): The model used to request a bank grade valuation.
        body (DomainAvmV1Request): The model used to request a bank grade valuation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]]
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
        DomainAvmV1Request,
        DomainAvmV1Request,
    ],
) -> Optional[Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]]:
    """Creates a bank grade valuation and PDF report for a given property address or GnafPId.

    Args:
        body (DomainAvmV1Request): The model used to request a bank grade valuation.
        body (DomainAvmV1Request): The model used to request a bank grade valuation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainAvmV1Request,
        DomainAvmV1Request,
    ],
) -> Response[Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]]:
    """Creates a bank grade valuation and PDF report for a given property address or GnafPId.

    Args:
        body (DomainAvmV1Request): The model used to request a bank grade valuation.
        body (DomainAvmV1Request): The model used to request a bank grade valuation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]]
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
        DomainAvmV1Request,
        DomainAvmV1Request,
    ],
) -> Optional[Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]]:
    """Creates a bank grade valuation and PDF report for a given property address or GnafPId.

    Args:
        body (DomainAvmV1Request): The model used to request a bank grade valuation.
        body (DomainAvmV1Request): The model used to request a bank grade valuation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DomainAvmV1ProblemDetails, DomainAvmV1Response]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
