# KECCEL MESSAGING
Keccel Service Manager is a very simple but powerful SMS Gateway built for developers who just want to send SMS in the
DR Congo at a very affordable cost. Both requests and responses are transmitted in JSON format.

## SENDING AN SMS
Method: POST
URL: https://api.keccel.com/sms/v2/message.asp

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

Example Request

```json
{
 "token":"84hbYi6TU8Zu",
 "to":"243851234567",
 "from":"GUEST",
 "message":"Hello World"
}
```

Response Delivery Report

```json
{
 "status": "SENT",
 "messageID": "123456",
 "description": "Message submitted to the network"
}
```

## DELIVERY REPORTS
This service allows you to receive the delivery status of a previous sent message. There is NO delivery report for rejected
messages. The delivery can be automatically sent to your callback (PUSH) or you can retrieve it (PULL) from our server.

### PUSH: Automatic Delivery
If the Delivery Reports (DLR) are required, you need to provide a callback URL where an automatic HTTP request will be
sent with the previous messageID and the delivery status of the message (DELIVERED or FAILED).
The DLR receipt will be sent to your URL as below:
http(s)://yourcallbackurl?messageID=123456&status=DELIVERED

### PULL: Delivery Check
You can also send a request to our delivery endpoint to check on the delivery status of a previous sent message:
Method: GET
URL: https://api.keccel.com/sms/v2/delivery.asp

| Request Parameter | Description                                                 | Example       |
| -----------       | ---------                                                   | ----------    |
| from              | Name that will appear on the phone as the sender of the SMS | KECCEL, GUEST |
| token             | Your API key that will be provided by Keccel                | 84hbYi6TU8Zu  |
| messageid         | The ID of the message which status is requested             | 123456        |

| Response Parameter | Description                      | Example                     |
| -----------        | ---------                        | ----------                  |
| messageid          | The messageID value as requested | 123456                      |
| status             | Status of the message            | DELIVERED, FAILED (or Error |

## BALANCE CHECK
This request is used to get the amount of the remaining SMS credits and the expiration date of a designated account.
Method: GET
URL: https://api.keccel.com/sms/v2/balance.asp

| Request Parameter | Description                                                 | Example       |
| -----------       | ---------                                                   | ----------    |
| from              | Name that will appear on the phone as the sender of the SMS | KECCEL, GUEST |
| token             | Your API key that will be provided by Keccel                | 84hbYi6TU8Zu  |


| Response Parameter | Description                                              | Example              |
| -----------        | ---------                                                | ----------           |
| balance            | Number of remaining credits                              | 645                  |
| expiration         | Expiration. No SMS will be sent after this date and time | 31-Dec-2021 06:46:17 |
| status             | Status of the account                                    | Active, inactive     |
