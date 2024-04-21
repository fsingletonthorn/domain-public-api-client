from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.social_boost_v1_rate_for_new_social_boost import SocialBoostV1RateForNewSocialBoost
from ...models.social_boost_v1_rate_for_new_social_boost_request_model import (
    SocialBoostV1RateForNewSocialBoostRequestModel,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        SocialBoostV1RateForNewSocialBoostRequestModel,
        SocialBoostV1RateForNewSocialBoostRequestModel,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/products/ratefornewsocialboost",
    }

    if isinstance(body, SocialBoostV1RateForNewSocialBoostRequestModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, SocialBoostV1RateForNewSocialBoostRequestModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SocialBoostV1RateForNewSocialBoost]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SocialBoostV1RateForNewSocialBoost.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SocialBoostV1RateForNewSocialBoost]:
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
        SocialBoostV1RateForNewSocialBoostRequestModel,
        SocialBoostV1RateForNewSocialBoostRequestModel,
    ],
) -> Response[SocialBoostV1RateForNewSocialBoost]:
    """Get updated pricing information for a hypothetical listing

    Args:
        body (SocialBoostV1RateForNewSocialBoostRequestModel):
        body (SocialBoostV1RateForNewSocialBoostRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialBoostV1RateForNewSocialBoost]
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
        SocialBoostV1RateForNewSocialBoostRequestModel,
        SocialBoostV1RateForNewSocialBoostRequestModel,
    ],
) -> Optional[SocialBoostV1RateForNewSocialBoost]:
    """Get updated pricing information for a hypothetical listing

    Args:
        body (SocialBoostV1RateForNewSocialBoostRequestModel):
        body (SocialBoostV1RateForNewSocialBoostRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialBoostV1RateForNewSocialBoost
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        SocialBoostV1RateForNewSocialBoostRequestModel,
        SocialBoostV1RateForNewSocialBoostRequestModel,
    ],
) -> Response[SocialBoostV1RateForNewSocialBoost]:
    """Get updated pricing information for a hypothetical listing

    Args:
        body (SocialBoostV1RateForNewSocialBoostRequestModel):
        body (SocialBoostV1RateForNewSocialBoostRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialBoostV1RateForNewSocialBoost]
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
        SocialBoostV1RateForNewSocialBoostRequestModel,
        SocialBoostV1RateForNewSocialBoostRequestModel,
    ],
) -> Optional[SocialBoostV1RateForNewSocialBoost]:
    """Get updated pricing information for a hypothetical listing

    Args:
        body (SocialBoostV1RateForNewSocialBoostRequestModel):
        body (SocialBoostV1RateForNewSocialBoostRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialBoostV1RateForNewSocialBoost
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
