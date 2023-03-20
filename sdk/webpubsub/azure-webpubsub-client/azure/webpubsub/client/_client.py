# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, overload, Callable, Union, Optional, Dict, List
import time
import sys
import logging
import threading
import urllib.parse
import websocket  # type: ignore
from azure.core.tracing.decorator import distributed_trace

from .models._models import (
    OnConnectedArgs,
    OnDisconnectedArgs,
    OnServerDataMessageArgs,
    OnGroupDataMessageArgs,
    WebPubSubJsonProtocol,
    WebPubSubJsonReliableProtocol,
    SequenceId,
    RetryPolicy,
    WebPubSubGroup,
    SendMessageErrorOptions,
    WebPubSubMessage,
    SendMessageError,
    SendEventMessage,
    SendToGroupMessage,
    AckMessage,
    ConnectedMessage,
    SequenceAckMessage,
    CloseEvent,
    OnRejoinGroupFailedArgs,
    DisconnectedMessage,
    GroupDataMessage,
    ServerDataMessage,
    JoinGroupMessage,
    LeaveGroupMessage,
    AckMessageError,
)
from .models._enums import WebPubSubDataType, WebPubSubClientState, CallBackType, WebPubSubProtocolType
from ._util import delay, format_user_agent

_LOGGER = logging.getLogger(__name__)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports


class WebPubSubClientCredential:
    @overload
    def __init__(self, client_access_url_provider: str) -> None:
        ...

    @overload
    def __init__(self, client_access_url_provider: Callable[[Any], str]) -> None:
        ...

    def __init__(self, client_access_url_provider: Union[str, Callable]) -> None:
        if isinstance(client_access_url_provider, str):
            self._client_access_url_provider = lambda: client_access_url_provider
        else:
            self._client_access_url_provider = client_access_url_provider

    def get_client_access_url(self) -> str:
        return self._client_access_url_provider()


_RETRY_TOTAL = 30
_RETRY_BACKOFF_FACTOR = 1.0
_RETRY_BACKOFF_MAX = 120.0
_RECOVERY_TIMEOUT = 30.0
_RECOVERY_RETRY_INTERVAL = 1.0
_USER_AGENT = "User-Agent"


class WebPubSubClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """WebPubSubClient

    :param credential: The url to connect or credential to use when connecting. Required.
    :type credential: str or WebPubSubClientCredential
    :keyword bool auto_rejoin_groups: Whether to enable restoring group after reconnecting
    :keyword azure.webpubsub.client.WebPubSubProtocolType protocol_type: Subprotocol type
    :keyword int reconnect_retry_total: total number of retries to allow for reconnect. If 0, it means disable
     reconnect. Default is 3.
    :keyword float reconnect_retry_backoff_factor: A backoff factor to apply between attempts after the second try
     (most errors are resolved immediately by a second try without a delay). In fixed mode, retry policy will always
     sleep for {backoff factor}. In 'exponential' mode, retry policy will sleep for:
     "{backoff factor} * (2 ** ({number of retries} - 1))" seconds. If the backoff_factor is 0.1, then the
     retry will sleep for [0.0s, 0.2s, 0.4s, ...] between retries. The default value is 1.0.
    :keyword float reconnect_retry_backoff_max: The maximum back off time. Default value is 120.0 seconds
    :keyword RetryMode reconnect_retry_mode: Fixed or exponential delay between attemps, default is exponential.
    :keyword int message_retry_total: total number of retries to allow for sending message. Default is 3.
    :keyword float message_retry_backoff_factor: A backoff factor to apply between attempts after the second try
     (most errors are resolved immediately by a second try without a delay). In fixed mode, retry policy will always
     sleep for {backoff factor}. In 'exponential' mode, retry policy will sleep for:
     "{backoff factor} * (2 ** ({number of retries} - 1))" seconds. If the backoff_factor is 0.1, then the
     retry will sleep for [0.0s, 0.2s, 0.4s, ...] between retries. The default value is 1.0.
    :keyword float message_retry_backoff_max: The maximum back off time. Default value is 120.0 seconds
    :keyword RetryMode message_retry_mode: Fixed or exponential delay between attemps, default is exponential.
    :keyword bool auto_rejoin_groups: auto_rejoin_groups, default is True
    :keyword str user_agent: The user agent to be used for the request. If specified, this will be added in front of
     the defualt user agent string.
    """

    def __init__(
        self,
        credential: Union[WebPubSubClientCredential, str],
        **kwargs: Any,
    ) -> None:
        if isinstance(credential, WebPubSubClientCredential):
            self._credential = credential
        elif isinstance(credential, str):
            self._credential = WebPubSubClientCredential(credential)
        else:
            raise TypeError("type of credential must be str or WebPubSubClientCredential")
        reconnect_retry_total = kwargs.pop("reconnect_retry_total", _RETRY_TOTAL)
        self._auto_reconnect = reconnect_retry_total > 0
        self._auto_rejoin_groups = kwargs.pop("auto_rejoin_groups", True)
        protocol_type = kwargs.pop("protocol_type", WebPubSubProtocolType.JSON_RELIABLE)
        protocol_map = {
            WebPubSubProtocolType.JSON: WebPubSubJsonProtocol,
            WebPubSubProtocolType.JSON_RELIABLE: WebPubSubJsonReliableProtocol,
        }
        if protocol_type in protocol_map:
            self._protocol = protocol_map[protocol_type]()
        else:
            self._protocol = WebPubSubJsonReliableProtocol()

        self._reconnect_retry_policy = RetryPolicy(
            retry_total=reconnect_retry_total,
            retry_backoff_factor=kwargs.pop("reconnect_retry_backoff_factor", _RETRY_BACKOFF_FACTOR),
            retry_backoff_max=kwargs.pop("reconnect_retry_backoff_max", _RETRY_BACKOFF_MAX),
            mode=kwargs.pop("reconnect_retry_mode", RetryMode.Fixed),
        )
        self._message_retry_policy = RetryPolicy(
            retry_total=kwargs.pop("message_retry_total", _RETRY_TOTAL),
            retry_backoff_factor=kwargs.pop("message_retry_backoff_factor", _RETRY_BACKOFF_FACTOR),
            retry_backoff_max=kwargs.pop("message_retry_backoff_max", _RETRY_BACKOFF_MAX),
            mode=kwargs.pop("message_retry_mode", RetryMode.Fixed),
        )
        self._group_map: Dict[str, WebPubSubGroup] = {}
        self._ack_map: Dict[int, SendMessageErrorOptions] = {}
        self._sequence_id = SequenceId()
        self._state = WebPubSubClientState.STOPPED
        self._ack_id = 0
        self._url = None
        self._ws: Optional[websocket.WebSocketApp] = None
        self._handler: Dict[str, List[Callable]] = {
            CallBackType.CONNECTED: [],
            CallBackType.DISCONNECTED: [],
            CallBackType.REJOIN_GROUP_FAILED: [],
            CallBackType.GROUP_MESSAGE: [],
            CallBackType.SERVER_MESSAGE: [],
            CallBackType.STOPPED: [],
        }
        self._last_disconnected_message: Optional[DisconnectedMessage] = None
        self._connection_id: Optional[str] = None
        self._is_initial_connected = False
        self._is_stopping = False
        self._last_close_event: Optional[CloseEvent] = None
        self._reconnection_token: Optional[str] = None
        self._cv: threading.Condition = threading.Condition()
        self._thread_seq_ack: Optional[threading.Thread] = None
        self._thread: Optional[threading.Thread] = None
        self._ack_timeout: float = kwargs.pop("ack_timeout", 1.0)
        self._start_timeout: float = kwargs.pop("start_timeout", 60.0)
        self._user_agent: Optional[str] = kwargs.pop("user_agent", None)

    def _next_ack_id(self) -> int:
        self._ack_id = self._ack_id + 1
        return self._ack_id

    def _send_message(self, message: WebPubSubMessage) -> None:
        pay_load = self._protocol.write_message(message)
        if not self._ws or not self._ws.sock:
            raise Exception("The connection is not connected.")

        self._ws.send(pay_load)

    def _send_message_with_ack_id(
        self,
        message_provider: Callable[[int], WebPubSubMessage],
        ack_id: Optional[int] = None,
    ) -> None:
        if ack_id is None:
            ack_id = self._next_ack_id()

        message = message_provider(ack_id)
        if ack_id not in self._ack_map:
            self._ack_map[ack_id] = SendMessageErrorOptions(
                error_detail=AckMessageError(name="", message="timeout to receive ack message")
            )
        try:
            self._send_message(message)
        except Exception as e:
            self._ack_map.pop(ack_id)
            raise e

        with self._ack_map[ack_id].cv:
            self._ack_map[ack_id].cv.wait(self._ack_timeout)
            options = self._ack_map.pop(ack_id)
            if options.error_detail is not None:
                raise SendMessageError(
                    message="Failed to send message.", ack_id=options.ack_id, error_detail=options.error_detail
                )

    def _get_or_add_group(self, name: str) -> WebPubSubGroup:
        if name not in self._group_map:
            self._group_map[name] = WebPubSubGroup(name=name)
        return self._group_map[name]

    @distributed_trace
    def join_group(self, group_name: str, **kwargs: Any) -> None:
        """Join the client to group.

        :param group_name: The group name. Required.
        :type group_name: str.
        :keyword int ack_id: The optional ackId. If not specified, client will generate one.
        """

        def join_group_attempt():
            group = self._get_or_add_group(group_name)
            self._join_group_core(group_name, **kwargs)
            group.is_joined = True

        self._retry(join_group_attempt)

    def _join_group_core(self, group_name: str, **kwargs: Any) -> None:
        ack_id = kwargs.pop("ack_id", None)
        self._send_message_with_ack_id(
            message_provider=lambda id: JoinGroupMessage(group=group_name, ack_id=id),
            ack_id=ack_id,
        )

    @distributed_trace
    def leave_group(self, group_name: str, **kwargs: Any) -> None:
        """Leave the client from group
        :param group_name: The group name. Required.
        :type group_name: str.
        :keyword int ack_id: The optional ackId. If not specified, client will generate one.
        """

        def leave_group_attempt():
            group = self._get_or_add_group(group_name)
            ack_id = kwargs.pop("ack_id", None)
            self._send_message_with_ack_id(
                message_provider=lambda id: LeaveGroupMessage(group=group_name, ack_id=id),
                ack_id=ack_id,
            )
            group.is_joined = False

        self._retry(leave_group_attempt)

    @distributed_trace
    def send_event(
        self,
        event_name: str,
        content: Any,
        data_type: WebPubSubDataType,
        **kwargs: Any,
    ) -> None:
        """Send custom event to server
        :param event_name: The event name. Required.
        :type event_name: str.
        :param content: The data content. Required.
        :type content: Any.
        :param data_type: The data type. Required.
        :type data_type: Any.
        :keyword int ack_id: The optional ackId. If not specified, client will generate one.
        :keyword bool fire_and_forget: If true, the message won't contains ackId and no AckMessage
         will be returned from the service.
        """

        def send_event_attempt():
            fire_and_forget = kwargs.pop("fire_and_forget", False)
            ack_id = kwargs.pop("ack_id", None)
            if not fire_and_forget:
                self._send_message_with_ack_id(
                    message_provider=lambda id: SendEventMessage(
                        data_type=data_type, data=content, ack_id=id, event=event_name
                    ),
                    ack_id=ack_id,
                )
            else:
                self._send_message(message=SendEventMessage(data_type=data_type, data=content, event=event_name))

        self._retry(send_event_attempt)

    @distributed_trace
    def send_to_group(
        self,
        group_name: str,
        content: Any,
        data_type: WebPubSubDataType,
        **kwargs: Any,
    ) -> None:
        """Send message to group.
        :param group_name: The group name. Required.
        :type group_name: str.
        :param content: The data content. Required.
        :type content: Any.
        :param data_type: The data type. Required.
        :type data_type: Any.
        :keyword bool fire_and_forget: If true, the message won't contains ackId and no AckMessage
         will be returned from the service.
        :keyword int no_echo: Whether the message needs to echo to sender
        """

        def send_to_group_attempt():
            fire_and_forget = kwargs.pop("fire_and_forget", False)
            no_echo = kwargs.pop("no_echo", False)
            if not fire_and_forget:
                self._send_message_with_ack_id(
                    message_provider=lambda id: SendToGroupMessage(
                        group=group_name, data_type=data_type, data=content, ack_id=id, no_echo=no_echo
                    )
                )
            else:
                self._send_message(
                    message=SendToGroupMessage(group=group_name, data_type=data_type, data=content, no_echo=no_echo)
                )

        self._retry(send_to_group_attempt)

    def _retry(self, func: Callable[[], None]):
        retry_attempt = 0
        while self._ws and self._ws.sock:
            try:
                func()
                return
            except Exception as e:  # pylint: disable=broad-except
                retry_attempt = retry_attempt + 1
                delay_seconds = self._message_retry_policy.next_retry_delay(retry_attempt)
                if delay_seconds is None:
                    raise e
                _LOGGER.debug("will retry %sth times after %s seconds", retry_attempt, delay_seconds)
                delay(delay_seconds)

    def _call_back(self, callback_type: CallBackType, *args):
        for func in self._handler[callback_type]:
            # _call_back works in listener thread which must not be blocked so we have to execute the func
            # in new thread to avoid dead lock
            threading.Thread(target=func, args=args, daemon=True).start()

    def _start_from_restarting(self):
        if self._state != WebPubSubClientState.DISCONNECTED:
            _LOGGER.warning("Client can be only restarted when it's Disconnected")
            return

        try:
            self._start_core()
        except Exception as e:
            self._state = WebPubSubClientState.DISCONNECTED
            raise e

    def _handle_auto_reconnect(self):
        success = False
        attempt = 0
        while not self._is_stopping:
            try:
                self._start_from_restarting()
                success = True
                break
            except Exception as e:  # pylint: disable=broad-except
                _LOGGER.warning("An attempt to reconnect connection failed %s", e)
                attempt = attempt + 1
                delay_seconds = self._reconnect_retry_policy.next_retry_delay(attempt)
                if not delay_seconds:
                    break
                _LOGGER.debug("Delay time for reconnect attempt %d: %ds", attempt, delay_seconds)
                delay(delay_seconds)
        if not success:
            self._handle_connection_stopped()

    def _handle_connection_stopped(self):
        self._is_stopping = False
        self._state = WebPubSubClientState.STOPPED
        self._call_back(CallBackType.STOPPED)

    def _handle_connection_close_and_no_recovery(self):
        self._state = WebPubSubClientState.DISCONNECTED
        self._call_back(
            CallBackType.DISCONNECTED,
            OnDisconnectedArgs(connection_id=self._connection_id, message=self._last_disconnected_message),
        )
        if self._auto_reconnect:
            self._handle_auto_reconnect()
        else:
            self._handle_connection_stopped()

    def _build_recovery_url(self):
        if self._connection_id and self._reconnection_token and self._url:
            params = {"awps_connection_id": self._connection_id, "awps_reconnection_token": self._reconnection_token}
            url_parse = urllib.parse.urlparse(self._url)
            url_dict = dict(urllib.parse.parse_qsl(url_parse.query))
            url_dict.update(params)
            new_query = urllib.parse.urlencode(url_dict)
            url_parse = url_parse._replace(query=new_query)
            new_url = urllib.parse.urlunparse(url_parse)
            return new_url
        return None

    def _is_connected(self) -> bool:
        """check whether the client is still coneected to server after start"""
        return bool(
            self._state == WebPubSubClientState.CONNECTED
            and self._thread
            and self._thread.is_alive()
            and self._ws
            and self._ws.sock
        )

    def _connect(self, url: str):  # pylint: disable=too-many-statements
        def on_open(_: Any):
            if self._is_stopping:
                try:
                    if self._ws:
                        self._ws.close()
                finally:
                    raise Exception("The client is stopped")

            _LOGGER.debug("WebSocket connection has opened")
            self._state = WebPubSubClientState.CONNECTED
            with self._cv:
                self._cv.notify()

        def on_message(_: Any, data: str):
            def handle_ack_message(message: AckMessage):
                if message.ack_id in self._ack_map:
                    if not (message.success or (message.error and message.error.name == "Duplicate")):
                        self._ack_map[message.ack_id].error_detail = message.error
                    else:
                        self._ack_map[message.ack_id].error_detail = None
                    self._ack_map[message.ack_id].ack_id = message.ack_id
                    with self._ack_map[message.ack_id].cv:
                        self._ack_map[message.ack_id].cv.notify()

            def handle_connected_message(message: ConnectedMessage):
                self._connection_id = message.connection_id
                self._reconnection_token = message.reconnection_token

                if not self._is_initial_connected:
                    self._is_initial_connected = True
                    if self._auto_rejoin_groups:
                        for group_name, group in self._group_map.items():
                            if group.is_joined:
                                try:
                                    self._join_group_core(group_name)
                                except Exception as e:  # pylint: disable=broad-except
                                    self._call_back(
                                        CallBackType.REJOIN_GROUP_FAILED,
                                        OnRejoinGroupFailedArgs(group=group_name, error=e),
                                    )

                    self._call_back(
                        CallBackType.CONNECTED,
                        OnConnectedArgs(connection_id=message.connection_id, user_id=message.user_id),
                    )

            def handle_disconnected_message(message: DisconnectedMessage):
                self._last_disconnected_message = message

            def handle_group_data_message(message: GroupDataMessage):
                if message.sequence_id:
                    if not self._sequence_id.try_update(message.sequence_id):
                        # // drop duplicated message
                        return

                self._call_back(
                    CallBackType.GROUP_MESSAGE,
                    OnGroupDataMessageArgs(
                        data_type=message.data_type,
                        data=message.data,
                        group=message.group,
                        from_user_id=message.from_user_id,
                        sequence_id=message.sequence_id,
                    ),
                )

            def handle_server_data_message(message: ServerDataMessage):
                if message.sequence_id:
                    if not self._sequence_id.try_update(message.sequence_id):
                        # // drop duplicated message
                        return

                self._call_back(
                    CallBackType.SERVER_MESSAGE,
                    OnServerDataMessageArgs(
                        data_type=message.data_type, data=message.data, sequence_id=message.sequence_id
                    ),
                )

            parsed_message = self._protocol.parse_messages(data)
            if parsed_message is None:
                #  None means the message is not recognized.
                return
            if parsed_message.kind == "connected":
                handle_connected_message(parsed_message)
            elif parsed_message.kind == "disconnected":
                handle_disconnected_message(parsed_message)
            elif parsed_message.kind == "ack":
                handle_ack_message(parsed_message)
            elif parsed_message.kind == "groupData":
                handle_group_data_message(parsed_message)
            elif parsed_message.kind == "serverData":
                handle_server_data_message(parsed_message)
            else:
                _LOGGER.warning("unknown message type: %s", parsed_message.kind)

        def on_close(_: Any, close_status_code: int, close_msg: str):
            if self._state == WebPubSubClientState.CONNECTED:
                _LOGGER.info("WebSocket connection closed. Code: %s, Reason: %s", close_status_code, close_msg)

                self._last_close_event = CloseEvent(close_status_code=close_status_code, close_reason=close_msg)
                # clean ack cache
                self._ack_map.clear()

                if self._is_stopping:
                    _LOGGER.warning("The client is stopping state. Stop recovery.")
                    self._handle_connection_close_and_no_recovery()
                    return

                if self._last_close_event and self._last_close_event.close_status_code == 1008:
                    _LOGGER.warning("The websocket close with status code 1008. Stop recovery.")
                    self._handle_connection_close_and_no_recovery()
                    return

                if not self._protocol.is_reliable_sub_protocol:
                    _LOGGER.warning("The protocol is not reliable, recovery is not applicable")
                    self._handle_connection_close_and_no_recovery()
                    return

                recovery_url = self._build_recovery_url()
                if not recovery_url:
                    _LOGGER.warning("Connection id or reconnection token is not available")
                    self._handle_connection_close_and_no_recovery()
                    return

                self._state = WebPubSubClientState.RECOVERING
                recovery_start = time.time()
                while (time.time() - recovery_start < _RECOVERY_TIMEOUT) and not self._is_stopping:
                    try:
                        self._connect(recovery_url)
                        return
                    except:  # pylint: disable=bare-except
                        _LOGGER.debug("Try to recover after %d seconds", _RECOVERY_RETRY_INTERVAL)
                        delay(_RECOVERY_RETRY_INTERVAL)

                _LOGGER.warning("Recovery attempts failed after 30 seconds or the client is stopping")
                self._handle_connection_close_and_no_recovery()
            else:
                _LOGGER.debug("WebSocket closed before open")
                raise Exception(f"Fail to start Websocket: {close_status_code}")

        if self._is_stopping:
            raise Exception("Can't start a client during stopping")

        self._ws = websocket.WebSocketApp(
            url=url,
            on_open=on_open,
            on_message=on_message,
            on_close=on_close,
            subprotocols=[self._protocol.name] if self._protocol else [],
            header=[f"{_USER_AGENT}: {format_user_agent(self._user_agent)}"],
        )

        # set thread to start listen to server
        self._thread = threading.Thread(target=self._ws.run_forever)
        self._thread.start()
        with self._cv:
            self._cv.wait(timeout=self._start_timeout)
        if not self._is_connected():
            raise Exception("Fail to start client")

        # set thread to check sequence id if needed
        if self._protocol.is_reliable_sub_protocol and (
            (self._thread_seq_ack and not self._thread_seq_ack.is_alive()) or (self._thread_seq_ack is None)
        ):

            def sequence_id_ack_periodically():
                while self._is_connected():
                    try:
                        is_updated, seq_id = self._sequence_id.try_get_sequence_id()
                        if is_updated:
                            self._send_message(SequenceAckMessage(sequence_id=seq_id))
                    finally:
                        delay(1.0)

            self._thread_seq_ack = threading.Thread(target=sequence_id_ack_periodically)
            self._thread_seq_ack.start()

    def _start_core(self):
        self._state = WebPubSubClientState.CONNECTING
        _LOGGER.info("Staring a new connection")

        # Reset before a pure new connection
        self._sequence_id.reset()
        self._is_initial_connected = False
        self._last_close_event = None
        self._last_disconnected_message = None
        self._connection_id = None
        self._reconnection_token = None
        self._url = None

        self._url = self._credential.get_client_access_url()
        self._connect(self._url)

    @distributed_trace
    def start(self) -> None:
        """start the client and connect to service"""

        if self._is_stopping:
            raise Exception("Can't start a client during stopping")
        if self._state != WebPubSubClientState.STOPPED:
            raise Exception("Client can be only started when it's Stopped")

        try:
            self._start_core()
        except Exception as e:
            self._state = WebPubSubClientState.STOPPED
            self._is_stopping = False
            raise e

    @distributed_trace
    def stop(self) -> None:
        """stop the client"""

        if self._state == WebPubSubClientState.STOPPED or self._is_stopping:
            return
        self._is_stopping = True

        # we can't use self._ws.close otherwise on_close may not be triggered
        # (realted issue: https://github.com/websocket-client/websocket-client/issues/899)
        if self._ws and self._ws.sock:
            self._ws.sock.close()

        if self._thread_seq_ack and self._thread_seq_ack.is_alive():
            _LOGGER.debug("wait for seq thread stop")
            self._thread_seq_ack.join()
        if self._thread and self._thread.is_alive():
            _LOGGER.debug("wait for listener thread stop")
            self._thread.join()
        self._thread_seq_ack = None
        self._thread = None

        _LOGGER.info("stop client successfully")

    @overload
    def on(self, event: Literal[CallBackType.CONNECTED], listener: Callable[[OnConnectedArgs], None]) -> None:
        """Add handler for connected event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(self, event: Literal[CallBackType.DISCONNECTED], listener: Callable[[OnDisconnectedArgs], None]) -> None:
        """Add handler for disconnected event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(self, event: Literal[CallBackType.STOPPED], listener: Callable[[], None]) -> None:
        """Add handler for stopped event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(
        self, event: Literal[CallBackType.SERVER_MESSAGE], listener: Callable[[OnServerDataMessageArgs], None]
    ) -> None:
        """Add handler for server messages.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(
        self, event: Literal[CallBackType.GROUP_MESSAGE], listener: Callable[[OnGroupDataMessageArgs], None]
    ) -> None:
        """Add handler for group messages.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(
        self, event: Literal[CallBackType.REJOIN_GROUP_FAILED], listener: Callable[[OnRejoinGroupFailedArgs], None]
    ) -> None:
        """Add handler for rejoining group failed.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @distributed_trace
    def on(self, event: CallBackType, listener: Callable) -> None:
        if event in self._handler:
            self._handler[event].append(listener)
        else:
            _LOGGER.error("wrong event type: %s", event)

    @overload
    def off(self, event: Literal[CallBackType.CONNECTED], listener: Callable[[OnConnectedArgs], None]) -> None:
        """Remove handler for connected event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(self, event: Literal[CallBackType.DISCONNECTED], listener: Callable[[OnDisconnectedArgs], None]) -> None:
        """Remove handler for connected event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(self, event: Literal[CallBackType.STOPPED], listener: Callable[[], None]) -> None:
        """Remove handler for stopped event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(
        self, event: Literal[CallBackType.SERVER_MESSAGE], listener: Callable[[OnServerDataMessageArgs], None]
    ) -> None:
        """Remove handler for server message.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(
        self, event: Literal[CallBackType.GROUP_MESSAGE], listener: Callable[[OnGroupDataMessageArgs], None]
    ) -> None:
        """Remove handler for group message.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(
        self, event: Literal[CallBackType.REJOIN_GROUP_FAILED], listener: Callable[[OnRejoinGroupFailedArgs], None]
    ) -> None:
        """Remove handler for rejoining group failed.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @distributed_trace
    def off(self, event: CallBackType, listener: Callable) -> None:
        if event in self._handler:
            if listener in self._handler[event]:
                self._handler[event].remove(listener)
            else:
                _LOGGER.info("target listener does not exist")
        else:
            _LOGGER.error("wrong event type: %s", event)

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
