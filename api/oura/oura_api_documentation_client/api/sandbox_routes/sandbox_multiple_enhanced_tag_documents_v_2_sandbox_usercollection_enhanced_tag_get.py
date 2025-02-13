import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.multi_document_response_enhanced_tag_model import MultiDocumentResponseEnhancedTagModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    end_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    next_token: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date: Union[None, Unset, str]
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    elif isinstance(start_date, datetime.datetime):
        json_start_date = start_date.isoformat()
    elif isinstance(start_date, datetime.date):
        json_start_date = start_date.isoformat()
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: Union[None, Unset, str]
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    elif isinstance(end_date, datetime.datetime):
        json_end_date = end_date.isoformat()
    elif isinstance(end_date, datetime.date):
        json_end_date = end_date.isoformat()
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    json_next_token: Union[None, Unset, str]
    if isinstance(next_token, Unset):
        json_next_token = UNSET
    else:
        json_next_token = next_token
    params["next_token"] = json_next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/sandbox/usercollection/enhanced_tag",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]]:
    if response.status_code == 200:
        response_200 = MultiDocumentResponseEnhancedTagModel.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    end_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    next_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]]:
    """Sandbox - Multiple Enhanced Tag Documents

    Args:
        start_date (Union[None, Unset, datetime.date, datetime.datetime]):
        end_date (Union[None, Unset, datetime.date, datetime.datetime]):
        next_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        next_token=next_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    end_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    next_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]]:
    """Sandbox - Multiple Enhanced Tag Documents

    Args:
        start_date (Union[None, Unset, datetime.date, datetime.datetime]):
        end_date (Union[None, Unset, datetime.date, datetime.datetime]):
        next_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    end_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    next_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]]:
    """Sandbox - Multiple Enhanced Tag Documents

    Args:
        start_date (Union[None, Unset, datetime.date, datetime.datetime]):
        end_date (Union[None, Unset, datetime.date, datetime.datetime]):
        next_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        next_token=next_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    end_date: Union[None, Unset, datetime.date, datetime.datetime] = UNSET,
    next_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]]:
    """Sandbox - Multiple Enhanced Tag Documents

    Args:
        start_date (Union[None, Unset, datetime.date, datetime.datetime]):
        end_date (Union[None, Unset, datetime.date, datetime.datetime]):
        next_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, MultiDocumentResponseEnhancedTagModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            next_token=next_token,
        )
    ).parsed
