"""Keccel Messaging API Client Implementation.

"""
import requests


class APIClient:
    """The API Client."""

    def __init__(self, token: str, sender_id: str):
        """Create a client with `token` and `sender_id` as from."""
        self.sender_id = sender_id
        self.token = token
        self.base_url = "https://api.keccel.com/sms/v2"

    @property
    def _shared_params(self) -> dict:
        """Return shared request params."""
        params = {
            "token": self.token,
            "from": self.sender_id,
        }
        return params

    def _get(self, endpoint: str, payload: dict) -> dict:
        """Post the payload to the keccel api endpoint."""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, json=payload)
        print(f"URL: {url} Response status: {response.status_code}")
        return response.json()

    def _post(self, endpoint: str, payload: dict) -> dict:
        """Post the payload to the keccel api endpoint."""
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=payload)
        print(f"URL: {url} Response status: {response.status_code}")
        return response.json()

    def send_messsage(self, to: str, message: str) -> dict:
        """Send SMS message to this phonenumber.

        | Request Parameter | Description                                                 | Example       |
        | -----------       | ---------                                                   | ----------    |
        | to                | Receiver phone number                                       | 243851234567  |
        | message           | Message body                                                | Hello world   |
        | from              | Name that will appear on the phone as the sender of the SMS | KECCEL, GUEST |
        | token             | Your API key that will be provided by Keccel                | 84hbYi6TU8Zu  |

        All parameters are mandatory.

        Note: In GUEST or trial modes, the SMS will be displayed as coming from KECCEL. In production, you need to provide an
        appropriate name to use as the sender of the SMS, such as the name of your application or your company.

        | Response Parameter | Description                             | Example                                         |
        | -----------        | ---------                               | ----------                                      |
        | status             | Status of the message                   | Rejected, Sent                                  |
        | messageID          | The ID of the sent message              | 123456 (used for Delivery Receipt)              |
        | description        | A string describing the status or error | Invalid token, Message submitted to the network |
        """
        endpoint = "/message.asp"
        payload = self._shared_params
        payload["to"] = to
        payload["message"] = message
        return self._post(endpoint, payload)
        ...

    def get_balance(self) -> dict:
        """Return the remaining SMS Credits for this client.

        | Request Parameter | Description                                                 | Example       |
        | -----------       | ---------                                                   | ----------    |
        | from              | Name that will appear on the phone as the sender of the SMS | KECCEL, GUEST |
        | token             | Your API key that will be provided by Keccel                | 84hbYi6TU8Zu  |


        | Response Parameter | Description                                              | Example              |
        | -----------        | ---------                                                | ----------           |
        | balance            | Number of remaining credits                              | 645                  |
        | expiration         | Expiration. No SMS will be sent after this date and time | 31-Dec-2021 06:46:17 |
        | status             | Status of the account                                    | Active, inactive     |
        """
        endpoint = "/balance.asp"
        payload = self._shared_params
        return self._get(endpoint, payload)
        ...

    def get_delivery_report(self, message_id: str) -> dict:
        """Check the delivery report for this message_id.

        | Request Parameter | Description                                                 | Example       |
        | -----------       | ---------                                                   | ----------    |
        | from              | Name that will appear on the phone as the sender of the SMS | KECCEL, GUEST |
        | token             | Your API key that will be provided by Keccel                | 84hbYi6TU8Zu  |
        | messageid         | The ID of the message which status is requested             | 123456        |

        | Response Parameter | Description                      | Example                     |
        | -----------        | ---------                        | ----------                  |
        | messageid          | The messageID value as requested | 123456                      |
        | status             | Status of the message            | DELIVERED, FAILED (or Error |
        """
        endpoint = "/delivery.asp"
        payload = self._shared_params
        payload["messageid"] = message_id
        return self._get(endpoint, payload)
        ...
