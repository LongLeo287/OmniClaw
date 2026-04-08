# CrotMail API Documentation

API documentation for the CrotMail temporary email service.

## Basic Information

- **Base URL**: `https://your-domain.workers.dev`
- **Content-Type**: `application/json`
- **Authentication**:
  - `X-Access-Key` header: used for sensitive operations such as mailbox creation
  - `Bearer Token`: used for mailbox actions via the `Authorization` header

---

## Domain Management

### GET /api/domains

Get the list of available domains.

**Request Headers**:
```
X-Access-Key: your-access-key
```

**Response**:
```json
{
  "hydra:member": [
    {
      "id": "uuid",
      "domain": "example.com",
      "isVerified": true,
      "createdAt": "2024-01-01T00:00:00Z"
    }
  ],
  "hydra:totalItems": 1
}
```

---

## Mailbox Accounts

### POST /api/accounts

Create a new mailbox account with a password.

**Request Headers**:
```
X-Access-Key: your-access-key
```

**Request Body**:
```json
{
  "address": "user@example.com",
  "password": "yourpassword"
}
```

**Parameters**:
| Field | Type | Required | Description |
|------|------|------|------|
| address | string | Yes | Full mailbox address |
| password | string | Yes | Password, minimum 6 characters |

**Response**: `201 Created`
```json
{
  "id": "uuid",
  "address": "user@example.com",
  "authType": "email",
  "expiresAt": "2024-01-01T01:00:00Z",
  "createdAt": "2024-01-01T00:00:00Z"
}
```

**Error Responses**:
- `400` - Invalid email format or password too short
- `409` - Mailbox address already exists
- `422` - Domain is unavailable

---

### POST /api/generate

Generate a random temporary mailbox.

**Request Headers**:
```
X-Access-Key: your-access-key
```

**Request Body** (optional):
```json
{
  "domain": "example.com"
}
```

**Parameters**:
| Field | Type | Required | Description |
|------|------|------|------|
| domain | string | No | Specific domain to use; if omitted, a random domain is selected |

**Response**: `201 Created`
```json
{
  "id": "uuid",
  "address": "randomuser@example.com",
  "password": "randompassword",
  "token": "jwt-token",
  "expiresAt": "2024-01-01T01:00:00Z"
}
```

---

### POST /api/custom

Create a mailbox with a custom username.

**Request Headers**:
```
X-Access-Key: your-access-key
```

**Request Body**:
```json
{
  "address": "myname@example.com"
}
```

**Parameters**:
| Field | Type | Required | Description |
|------|------|------|------|
| address | string | Yes | Full mailbox address (username must be 3-30 characters) |

**Response**: `201 Created`
```json
{
  "id": "uuid",
  "address": "myname@example.com",
  "password": "randompassword",
  "token": "jwt-token",
  "expiresAt": "2024-01-01T01:00:00Z"
}
```

**Error Responses**:
- `400` - Invalid email format or username length
- `409` - Mailbox address already exists
- `422` - Domain is unavailable

---

### POST /api/token

Get an authentication token (login).

**Request Body**:
```json
{
  "address": "user@example.com",
  "password": "yourpassword"
}
```

**Response**:
```json
{
  "id": "uuid",
  "token": "jwt-token",
  "mode": "full",
  "expiresAt": "2024-01-01T01:00:00Z"
}
```

**Error Responses**:
- `401` - Invalid credentials

---

### POST /api/resume

Resume mailbox access using an 8-character unique code.

**Request Body**:
```json
{
  "code": "Ab12Cd34"
}
```

**Response**:
```json
{
  "id": "uuid",
  "address": "user@example.com",
  "token": "jwt-token",
  "mode": "limited",
  "expiresAt": "2024-01-01T01:00:00Z"
}
```

**Notes**:
- `mode = limited` can read messages and delete messages only.

**Error Responses**:
- `400` - Invalid resume code format
- `401` - Invalid or expired code

---

### GET /api/me

Get current account information.

**Request Headers**:
```
Authorization: Bearer <token>
```

**Response**:
```json
{
  "id": "uuid",
  "address": "user@example.com",
  "authType": "email",
  "mode": "full",
  "expiresAt": "2024-01-01T01:00:00Z",
  "createdAt": "2024-01-01T00:00:00Z"
}
```

**Error Responses**:
- `401` - Unauthorized

---

### PATCH /api/me/extend

Extend mailbox expiration time.

**Request Headers**:
```
Authorization: Bearer <token>
```

**Request Body**:
```json
{
  "minutes": 30
}
```

**Parameters**:
| Field | Type | Required | Description |
|------|------|------|------|
| minutes | number | No | Extension time in minutes (default: 30) |

**Response**:
```json
{
  "success": true,
  "expiresAt": "2024-01-01T01:30:00Z"
}
```

---

### DELETE /api/accounts/{id}

Delete a mailbox account (and all associated emails).

**Request Headers**:
```
Authorization: Bearer <token>
```

**Response**: `204 No Content`

**Error Responses**:
- `401` - Unauthorized
- `403` - Not allowed to delete another user's account

---

### POST /api/admin/delete-account

Admin endpoint to delete mailbox by full email address.

**Request Headers**:
```
X-Access-Key: your-access-key
```

**Request Body**:
```json
{
  "address": "username@example.com"
}
```

**Response**:
```json
{
  "success": true,
  "deleted": true,
  "id": "uuid",
  "address": "username@example.com"
}
```

**Error Responses**:
- `401` - Unauthorized (invalid access key)
- `404` - Account not found

---

## Message Management

### GET /api/messages

Get the message list.

**Request Headers**:
```
Authorization: Bearer <token>
```

**Query Parameters**:
| Parameter | Type | Default | Description |
|------|------|--------|------|
| page | number | 1 | Page number |

**Response**:
```json
{
  "hydra:member": [
    {
      "id": "uuid",
      "msgid": "message-id",
      "from": {
        "name": "Sender Name",
        "address": "sender@example.com"
      },
      "to": [
        {
          "name": "",
          "address": "user@example.com"
        "mode": "full",
        "resumeCode": "Ab12Cd34",
        "resumeUrl": "https://your-domain.workers.dev/r/Ab12Cd34",
        }
      ],
      "subject": "Message Subject",
      "seen": false,
      "hasAttachments": true,
      "size": 1234,
      "createdAt": "2024-01-01T00:00:00Z"
    }
  ],
  "hydra:totalItems": 10
}
```

    "mode": "full",
    "resumeCode": "Ab12Cd34",
    "resumeUrl": "https://your-domain.workers.dev/r/Ab12Cd34",
---

### GET /api/messages/{id}

Get message details.

**Request Headers**:
```
Authorization: Bearer <token>
```

**Response**:
```json
{
  "id": "uuid",
  "msgid": "message-id",
  "from": {
    "name": "Sender Name",
    "address": "sender@example.com"
  },
  "to": [
    {
      "name": "",
      "address": "user@example.com"
    }
  ],
  "subject": "Message Subject",
  "text": "Plain text content",
  "html": ["<html>...</html>"],
  "seen": false,
  "hasAttachments": true,
  "size": 1234,
  "attachments": [
    {
      "id": "uuid",
      "filename": "document.pdf",
      "contentType": "application/pdf",
      "size": 5678
    }
  ],
  "createdAt": "2024-01-01T00:00:00Z"
}
```

**Error Responses**:
- `404` - Message not found

---

### PATCH /api/messages/{id}

Mark a message as read.

**Request Headers**:
```
Authorization: Bearer <token>
```

**Response**:
```json
{
  "seen": true
}
```

---

### DELETE /api/messages/{id}

Delete a message.

**Request Headers**:
```
Authorization: Bearer <token>
```

**Response**: `204 No Content`

---

### GET /api/sources/{id}

Get raw email source.

**Request Headers**:
```
Authorization: Bearer <token>
```

**Response**:
```json
{
  "id": "uuid",
  "data": "Full raw email content..."
}
```

---

## Attachments

### GET /api/attachments/{id}

Download an attachment.

**Request Headers**:
```
Authorization: Bearer <token>
```

**Response**: Binary file stream

**Response Headers**:
```
Content-Type: <attachment content type>
Content-Disposition: attachment; filename="<filename>"
```

---

## Error Response Format

All error responses follow this format:

```json
{
  "error": "Error",
  "message": "Error description"
}
```

**Common Status Codes**:
| Status Code | Description |
|--------|------|
| 400 | Invalid request parameters |
| 401 | Unauthorized (missing or invalid credentials) |
| 403 | Forbidden (no permission) |
| 404 | Resource not found |
| 409 | Resource conflict (for example, mailbox already exists) |
| 422 | Unprocessable entity (for example, invalid domain) |
| 500 | Internal server error |

---

## Environment Variables

| Variable | Required | Default | Description |
|--------|------|--------|------|
| JWT_SECRET | Yes | - | JWT signing secret |
| ACCESS_KEY | Yes | - | API access key |
| MAIL_DOMAINS | Yes | - | Available domains, comma-separated |
| EXPIRE_MINUTES | No | 43200 | Mailbox expiration time (minutes), default 30 days |
| MESSAGE_RETENTION_DAYS | No | 1 | Message retention period before scheduled cleanup |

---

## Usage Examples

### Create a Random Mailbox

```bash
curl -X POST https://your-domain.workers.dev/api/generate \
  -H "Content-Type: application/json" \
  -H "X-Access-Key: your-access-key"
```

### Create a Custom Mailbox

```bash
curl -X POST https://your-domain.workers.dev/api/custom \
  -H "Content-Type: application/json" \
  -H "X-Access-Key: your-access-key" \
  -d '{"address": "myname@example.com"}'
```

### Get Message List

```bash
curl https://your-domain.workers.dev/api/messages \
  -H "Authorization: Bearer <token>"
```

### Download an Attachment

```bash
curl https://your-domain.workers.dev/api/attachments/<id> \
  -H "Authorization: Bearer <token>" \
  -o filename.pdf
```
