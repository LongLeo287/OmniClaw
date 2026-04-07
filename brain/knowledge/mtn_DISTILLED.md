---
id: mtn
type: knowledge
owner: OA_Triage
---
# mtn
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "mtn-momo-sdk",
  "version": "1.3.0",
  "description": "A Node.js SDK to integrate with MTN MoMo API",
  "main": "lib/index.js",
  "directories": {
    "lib": "lib"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "MTN",
    "MoMo",
    "API",
    "SDK",
    "Payments",
    "Node.js",
    "Payment Gateway",
    "Mobile Money Payments",
    "Financial Integration",
    "Sandbox",
    "Production",
    "Callback",
    "Bearer Token",
    "REST API",
    "HTTP Client",
    "Node.js",
    "MTN Node SDK",
    "MTN MoMo Node SDK"
  ],
  "author": "Damiano Chintala",
  "homepage": "https://github.com/DamianoSilverhand/mtn-momo-node#readme",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/DamianoSilverhand/mtn-momo-node.git"
  },
  "license": "MIT",
  "dependencies": {
    "axios": "^1.7.5",
    "dotenv": "^16.4.5",
    "uuid": "^10.0.0"
  }
}

```

### File: README.md
```md
# MTN MoMo Node SDK

A comprehensive Node.js SDK for integrating with the MTN MoMo API, supporting both sandbox and production environments with automatic API user/key management, real-time callbacks, and intelligent polling mechanisms.

## Features

- **Dual Environment Support**: Seamless switching between sandbox and production environments
- **Automatic API Management**: Creates API users and keys automatically in sandbox mode
- **Real-Time Callbacks**: Supports callback URLs for instant payment status updates
- **Intelligent Polling**: Fallback polling mechanism with configurable retries and delays
- **Bearer Token Management**: Automatic token generation and management
- **Comprehensive Error Handling**: Detailed error logging with full response data
- **Unique Payment References**: Generates unique external IDs using UUID v4

## Prerequisites

- Node.js (>= 14.x)
- NPM or Yarn
- MTN MoMo API access (sandbox and/or production)

## Installation

Install the package in your Node.js project:

```bash
npm install mtn-momo-sdk
```

## Configuration

1. Copy the `env.example` file to `.env`:
```bash
cp env.example .env
```

2. Update the `.env` file with your actual values:

```bash
# Environment Configuration
MTN_MOMO_ENV=sandbox  # Set to 'sandbox' or 'production'
LOCAL_CURRENCY=ZMW    # Local currency for transactions

# Sandbox Configuration
MOMO_API_BASE_URL_SANDBOX=https://sandbox.momodeveloper.mtn.com
X_TARGET_ENVIRONMENT_SANDBOX=sandbox
SUBSCRIPTION_KEY_SANDBOX=your_sandbox_subscription_key_here
PROVIDER_CALLBACK_HOST_SANDBOX=https://your-sandbox-callback-url.com

# Production Configuration
MOMO_API_BASE_URL_PRODUCTION=https://your-production-api-url.com
X_TARGET_ENVIRONMENT_PRODUCTION=production
SUBSCRIPTION_KEY_PRODUCTION=your_production_subscription_key_here
API_USER_PRODUCTION=your_production_api_user_here
API_KEY_PRODUCTION=your_production_api_key_here
PROVIDER_CALLBACK_HOST_PRODUCTION=https://your-production-callback-url.com

# Polling Configuration
DEFAULT_POLL_RETRIES=3
DEFAULT_POLL_DELAY_MS=5000
```

## Usage

### Basic Payment Processing

To initiate a payment, call the `processPayment` function with the payment amount, recipient's phone number, and a business reference.

```javascript
const { processPayment } = require('mtn-momo-sdk');

async function makePayment() {
    try {
        const amount = '100.00';
        const phone = '260XXXXXXXXX';  // Recipient's phone number with country code
        const businessRef = 'Invoice #12345';  // Business reference for the payment

        const paymentResult = await processPayment(amount, phone, businessRef);
        console.log('Final Payment Status:', paymentResult);
        
        // paymentResult will contain:
        // { status: 'SUCCESSFUL' | 'FAILED', data: responseData }
        
    } catch (error) {
        console.error('Payment processing failed:', error.message);
    }
}

makePayment();

### 2. Poll Payment Status

To check the status of an existing payment without creating a new one, use the `pollPaymentStatus` function:

```javascript
const { pollPaymentStatus } = require('mtn-momo-sdk');

async function checkPaymentStatus() {
    try {
        const transactionId = 'your_transaction_id_here';
        const status = await pollPaymentStatus(transactionId);
        console.log('Payment Status:', status);
        
        // status will contain:
        // { status: 'SUCCESSFUL' | 'FAILED' | 'PENDING' | 'UNKNOWN', data: responseData, message: string }
        
    } catch (error) {
        console.error('Status check failed:', error.message);
    }
}

checkPaymentStatus();
```
```

### Environment-Specific Behavior

The SDK automatically handles different behaviors based on the environment:

#### Sandbox Mode (`MTN_MOMO_ENV=sandbox`)
- Automatically creates API users and keys for each transaction
- Uses the business reference as the API user ID
- Generates new API keys dynamically
- Perfect for testing and development

#### Production Mode (`MTN_MOMO_ENV=production`)
- Uses pre-configured API user and key from environment variables
- Requires `API_USER_PRODUCTION` and `API_KEY_PRODUCTION` to be set
- Optimized for production workloads

### Payment Flow

1. **Environment Detection**: SDK determines sandbox vs production mode
2. **API User/Key Setup**: Creates or uses existing API credentials
3. **Bearer Token Generation**: Authenticates with MTN MoMo API
4. **Payment Request**: Initiates the payment with callback URL
5. **Status Polling**: Polls for payment status if callback fails
6. **Result Return**: Returns final payment status and data

## Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `MTN_MOMO_ENV` | Environment mode (sandbox/production) | - | Yes |
| `LOCAL_CURRENCY` | Currency code for transactions | `ZMW` | No |
| `MOMO_API_BASE_URL_SANDBOX` | Sandbox API base URL | - | Yes (sandbox) |
| `X_TARGET_ENVIRONMENT_SANDBOX` | Sandbox target environment | - | Yes (sandbox) |
| `SUBSCRIPTION_KEY_SANDBOX` | Sandbox subscription key | - | Yes (sandbox) |
| `PROVIDER_CALLBACK_HOST_SANDBOX` | Sandbox callback URL | - | Yes (sandbox) |
| `MOMO_API_BASE_URL_PRODUCTION` | Production API base URL | - | Yes (production) |
| `X_TARGET_ENVIRONMENT_PRODUCTION` | Production target environment | - | Yes (production) |
| `SUBSCRIPTION_KEY_PRODUCTION` | Production subscription key | - | Yes (production) |
| `API_USER_PRODUCTION` | Production API user | - | Yes (production) |
| `API_KEY_PRODUCTION` | Production API key | - | Yes (production) |
| `PROVIDER_CALLBACK_HOST_PRODUCTION` | Production callback URL | - | Yes (production) |
| `DEFAULT_POLL_RETRIES` | Maximum polling retries | `3` | No |
| `DEFAULT_POLL_DELAY_MS` | Polling interval (ms) | `5000` | No |

## API Endpoints

The SDK interacts with the following MTN MoMo API endpoints:

- **API User Creation**: `POST /v1_0/apiuser` (sandbox only)
- **API Key Generation**: `POST /v1_0/apiuser/{referenceId}/apikey` (sandbox only)
- **Bearer Token**: `POST /collection/token/`
- **Payment Request**: `POST /collection/v1_0/requesttopay`
- **Payment Status**: `GET /collection/v1_0/requesttopay/{referenceId}`

## Error Handling

The SDK provides comprehensive error handling:
- All API errors are logged with full response details
- Automatic retry mechanism for failed requests
- Detailed error messages for debugging
- Graceful handling of network timeouts
- Environment validation with clear error messages

## Payment Status Values

The SDK returns the following payment statuses:
- `SUCCESSFUL`: Payment completed successfully
- `FAILED`: Payment failed
- `PENDING`: Payment is being processed
- `TIMEOUT`: Payment status polling timed out

## Callback Integration

The SDK supports callback URLs for real-time payment status updates:
- Set `PROVIDER_CALLBACK_HOST_SANDBOX` or `PROVIDER_CALLBACK_HOST_PRODUCTION`
- Callbacks are sent to your specified URL with payment status updates
- If callbacks fail, the SDK automatically falls back to polling

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Official Documentation

For more information on the MTN MoMo API, please refer to the [official MTN MoMo developer documentation](https://momodeveloper.mtn.com).
```

### File: lib\index.js
```js
//lib/index.js

require('dotenv').config();
const axios = require('axios');
const { v4: uuidv4 } = require('uuid');

// ───────────────────────────────────────────────────────────────────────────────
// 1) Configuration & Environment
// ───────────────────────────────────────────────────────────────────────────────
// Read MTN_MOMO_ENV directly—no fallback here
const MTN_MOMO_ENV = process.env.MTN_MOMO_ENV;
if (!MTN_MOMO_ENV) {
  throw new Error('MTN_MOMO_ENV is not set. Must be "sandbox" or "production".');
}
if (!['sandbox', 'production'].includes(MTN_MOMO_ENV)) {
  throw new Error(`Invalid MTN_MOMO_ENV "${MTN_MOMO_ENV}". Must be "sandbox" or "production".`);
}

const LOCAL_CURRENCY = process.env.LOCAL_CURRENCY || 'ZMW';

// Sandbox vars
const {
  MOMO_API_BASE_URL_SANDBOX,
  X_TARGET_ENVIRONMENT_SANDBOX,
  SUBSCRIPTION_KEY_SANDBOX,
  PROVIDER_CALLBACK_HOST_SANDBOX
} = process.env;

// Production vars
const {
  MOMO_API_BASE_URL_PRODUCTION,
  X_TARGET_ENVIRONMENT_PRODUCTION,
  SUBSCRIPTION_KEY_PRODUCTION,
  API_USER_PRODUCTION,
  API_KEY_PRODUCTION,
  PROVIDER_CALLBACK_HOST_PRODUCTION
} = process.env;

// Polling defaults
const DEFAULT_POLL_RETRIES   = Number(process.env.DEFAULT_POLL_RETRIES  || 3);
const DEFAULT_POLL_DELAY_MS  = Number(process.env.DEFAULT_POLL_DELAY_MS || 5000);

const isProduction = MTN_MOMO_ENV === 'production';

const CONFIG = {
  baseUrl:             isProduction ? MOMO_API_BASE_URL_PRODUCTION   : MOMO_API_BASE_URL_SANDBOX,
  targetEnv:           isProduction ? X_TARGET_ENVIRONMENT_PRODUCTION : X_TARGET_ENVIRONMENT_SANDBOX,
  subscriptionKey:     isProduction ? SUBSCRIPTION_KEY_PRODUCTION     : SUBSCRIPTION_KEY_SANDBOX,
  providerCallbackHost: isProduction ? PROVIDER_CALLBACK_HOST_PRODUCTION : PROVIDER_CALLBACK_HOST_SANDBOX,
  apiUser:             API_USER_PRODUCTION,
  apiKey:              API_KEY_PRODUCTION
};

// ───────────────────────────────────────────────────────────────────────────────
// 2) Utility: Centralized Error Logging
// ───────────────────────────────────────────────────────────────────────────────
function logAxiosError(fnName, error) {
  console.error(`Error in ${fnName}:`, error.message);
  if (error.response) {
    console.error('  Response Status:', error.response.status);
    console.error('  Response Headers:', error.response.headers);
    console.error('  Response Data:', error.response.data);
    console.error('  Response URL:', error.response.config?.url);
    console.error('  Request Method:', error.response.config?.method);
    console.error('  Request Headers:', error.response.config?.headers);
    console.error('  Request Data:', error.response.config?.data);
  } else if (error.request) {
    console.error('  Request was made but no response received');
    console.error('  Request:', error.request);
  } else {
    console.error('  Error setting up request:', error.message);
  }
}

// ───────────────────────────────────────────────────────────────────────────────
// 3) Sandbox‐only setup: create API user & key
// ───────────────────────────────────────────────────────────────────────────────
async function createApiUser(referenceId) {
  console.log('[Sandbox] Creating API user, X-Reference-Id:', referenceId);
  const url = `${CONFIG.baseUrl}/v1_0/apiuser`;
  try {
    const { data } = await axios.post(
      url,
      { providerCallbackHost: CONFIG.providerCallbackHost },
      {
        headers: {
          'Ocp-Apim-Subscription-Key': CONFIG.subscriptionKey,
          'Content-Type': 'application/json',
          'X-Reference-Id': referenceId
        }
      }
    );
    console.log('[Sandbox] API user created:', data);
    return data;
  } catch (err) {
    logAxiosError('createApiUser', err);
    throw err;
  }
}

async function createApiKey(referenceId) {
  console.log('[Sandbox] Creating API key, for user:', referenceId);
  const url = `${CONFIG.baseUrl}/v1_0/apiuser/${referenceId}/apikey`;
  try {
    const { data } = await axios.post(
      url,
      null,
      {
        headers: {
          'Ocp-Apim-Subscription-Key': CONFIG.subscriptionKey
        }
      }
    );
    console.log('[Sandbox] API key created.');
    return data.apiKey;
  } catch (err) {
    logAxiosError('createApiKey', err);
    throw err;
  }
}

// ───────────────────────────────────────────────────────────────────────────────
// 4) Create Bearer Token
// ───────────────────────────────────────────────────────────────────────────────
async function createBearerToken(apiUserId, apiKey) {
  console.log('Requesting Bearer token for user:', apiUserId);
  const url = `${CONFIG.baseUrl}/collection/token/`;
  const auth = Buffer.from(`${apiUserId}:${apiKey}`).toString('base64');
  try {
    const { data } = await axios.post(
      url,
      null,
      {
        headers: {
          'Ocp-Apim-Subscription-Key': CONFIG.subscriptionKey,
          Authorization: `Basic ${auth}`,
          'Content-Length': 0
        }
      }
    );
    console.log('Bearer token acquired.');
    return data.access_token;
  } catch (err) {
    logAxiosError('createBearerToken', err);
    throw err;
  }
}

// ───────────────────────────────────────────────────────────────────────────────
// 5) Request Payment
// ───────────────────────────────────────────────────────────────────────────────
async function requestPayment({ referenceId, bearerToken, amount, phone, businessRef, xReferenceId }) {
  console.log('Requesting payment, X-Reference-Id:', xReferenceId);
  const url = `${CONFIG.baseUrl}/collection/v1_0/requesttopay`;
  
  const body = {
    amount,
    currency: LOCAL_CURRENCY,
    externalId: uuidv4(),
    payer: { partyIdType: 'MSISDN', partyId: phone },
    payerMessage: `Payment for ${businessRef}`,
    payeeNote: 'Payment Initiated'
  };

  // Debug logging - show exactly what we're sending
  console.log('=== DEBUG: Request Details ===');
  console.log('URL:', url);
  console.log('Body:', JSON.stringify(body, null, 2));
  console.log('Config:', {
    baseUrl: CONFIG.baseUrl,
    targetEnv: CONFIG.targetEnv,
    subscriptionKey: CONFIG.subscriptionKey ? '***SET***' : '***MISSING***',
    providerCallbackHost: CONFIG.providerCallbackHost ? '***SET***' : '***MISSING***',
    apiUser: CONFIG.apiUser ? '***SET***' : '***MISSING***',
    apiKey: CONFIG.apiKey ? '***SET***' : '***MISSING***'
  });
  console.log('Bearer Token:', bearerToken ? '***SET***' : '***MISSING***');
  console.log('Phone:', phone);
  console.log('Amount:', amount, 'Type:', typeof amount);
  console.log('X-Reference-Id (UUID):', xReferenceId);
  console.log('Business Ref:', businessRef);
  console.log('==============================');

  try {
    const { data } = await axios.post(
      url,
      body,
      {
        headers: {
          'X-Target-Environment': CONFIG.targetEnv,
          'X-Reference-Id': xReferenceId, // Use the generated UUID
          'Ocp-Apim-Subscription-Key': CONFIG.subscriptionKey,
          'Content-Type': 'application/json',
          'X-Callback-Url': CONFIG.providerCallbackHost,
          Authorization: `Bearer ${bearerToken}`
        }
      }
    );
    console.log('Payment request accepted:', data);
    return data;
  } catch (err) {
    logAxiosError('requestPayment', err);
    throw err;
  }
}

// ───────────────────────────────────────────────────────────────────────────────
// 6) Get Payment Status
// ───────────────────────────────────────────────────────────────────────────────
async function getPaymentStatus({ referenceId, bearerToken, xReferenceId }) {
  console.log('Fetching payment status, X-Reference-Id:', xReferenceId);
  const url = `${CONFIG.baseUrl}/collection/v1_0/requesttopay/${xReferenceId}`;
  try {
    const { data } = await axios.get(
      url,
      {
        headers: {
          'X-Target-Environment': CONFIG.targetEnv,
          'Ocp-Apim-Subscription-Key': CONFIG.subscriptionKey,
          Authorization: `Bearer ${bearerToken}`
        }
      }
    );
    console.log('Payment status:', data);
    return data;
  } catch (err) {
    logAxiosError('getPaymentStatus', err);
    throw err;
  }
}

// ───────────────────────────────────────────────────────────────────────────────
// 7) Polling Loop
// ───────────────────────────────────────────────────────────────────────────────
async function pollPaymentStatus({ referenceId, bearerToken, xReferenceId, retries = DEFAULT_POLL_RETRIES, delay = DEFAULT_POLL_DELAY_MS }) {
  console.log('Starting polling for', xReferenceId);
  for (let i = 1; i <= retries; i++) {
    try {
      const status = await getPaymentStatus({ referenceId, bearerToken, xReferenceId });
      if (['SUCCESSFUL', 'FAILED'].includes(status.status)) {
        console.log('Final status:', status.status);
        return status;
      }
      console.log(`Status = ${status.status}, retrying in ${delay}ms (${i}/${retries})`);
    } catch (err) {
      console.error(`Polling error (attempt ${i}):`, err.message);
    }
    await new Promise(res => setTimeout(res, delay));
  }
  console.error('Polling timed out after', retries, 'attempts');
  throw new Error('Payment status polling timed out');
}

// ───────────────────────────────────────────────────────────────────────────────
// 8) Public API: processPayment()
// ───────────────────────────────────────────────────────────────────────────────
async function processPayment(amount, phone, businessRef) {
  console.log(`\n=== Processing Payment (${MTN_MOMO_ENV}) ===`);
  console.log(`Amount: ${amount}, Phone: ${phone}, Ref: ${businessRef}`);
  
  // Debug: Show input types and values
  console.log('=== INPUT DEBUG ===');
  console.log('Amount type:', typeof amount, 'Value:', amount);
  console.log('Phone type:', typeof phone, 'Value:', phone);
  console.log('BusinessRef type:', typeof businessRef, 'Value:', businessRef);
  console.log('Environment:', MTN_MOMO_ENV);
  console.log('Is Production:', isProduction);
  console.log('==================');

  // Generate a proper UUID for X-Reference-Id as required by MTN MoMo API
  const xReferenceId = uuidv4();
  console.log('Generated X-Reference-Id (UUID):', xReferenceId);

  try {
    let apiUserId, apiKey;

    if (isProduction) {
      console.log('Production mode: using env API_USER & API_KEY');
      apiUserId = CONFIG.apiUser;
      apiKey     = CONFIG.apiKey;
    } else {
      console.log('Sandbox mode: creating API user & key');
      await createApiUser(xReferenceId);
      apiUserId = xReferenceId;
      apiKey    = await createApiKey(xReferenceId);
    }

    const bearerToken = await createBearerToken(apiUserId, apiKey);

    await requestPayment({ referenceId: businessRef, bearerToken, amount, phone, businessRef, xReferenceId });

    // If callback fails, fallback to polling:
    const finalStatus = await pollPaymentStatus({ referenceId: businessRef, bearerToken, xReferenceId });

    return { status: finalStatus.status, data: finalStatus };
  } catch (err) {
    console.error('processPayment failed:', err.message);
    throw err;
  }
}

// ───────────────────────────────────────────────────────────────────────────────
// 9) Public API: Poll Payment Status (NEW - for checking existing payments)
// ───────────────────────────────────────────────────────────────────────────────
async function pollPaymentStatus(transactionIdOrRef) {
  console.log(`\n=== Polling MTN payment status ===`);
  console.log(`Transaction ID/Reference: ${transactionIdOrRef}`);
  
  try {
    let apiUserId, apiKey;

    if (isProduction) {
      console.log('Production mode: using env API_USER & API_KEY');
      apiUserId = CONFIG.apiUser;
      apiKey     = CONFIG.apiKey;
    } else {
      console.log('Sandbox mode: creating API user & key for status check');
      await createApiUser(transactionIdOrRef);
      apiUserId = transactionIdOrRef;
      apiKey    = await createApiKey(transactionIdOrRef);
    }

    const bearerToken = await createBearerToken(apiUserId, apiKey);
    console.log('Bearer token acquired for status check.');

    // Check the payment status
    const status = await getPaymentStatus({ 
      referenceId: transactionIdOrRef, 
      bearerToken, 
      xReferenceId: transactionIdOrRef 
    });
    
    console.log('Status check result:', JSON.stringify(status, null, 2));
    
    // Parse the response to determine final status
    if (status?.status) {
      if (status.status === 'SUCCESSFUL') {
        console.log('Final status: Payment successful');
        return { status: 'SUCCESSFUL', data: status, message: 'Payment successful' };
      } else if (status.status === 'FAILED') {
        console.log('Final status: Payment failed');
        return { status: 'FAILED', data: status, message: status.message || 'Payment failed' };
      } else if (status.status === 'PENDING') {
        console.log('Status: Payment pending');
        return { status: 'PENDING', data: status, message: 'Payment pending' };
      } else {
        console.log('Status: Unknown status');
        return { status: 'UNKNOWN', data: status, message: `Status: ${status.status}` };
      }
    } else {
      console.log('No status data in response');
      return { status: 'UNKNOWN', data: status, message: 'No status data' };
    }
  } catch (err) {
    console.error('pollPaymentStatus failed:', err.message);
    throw err;
  }
}

// ───────────────────────────────────────────────────────────────────────────────
// 10) Export
// ───────────────────────────────────────────────────────────────────────────────
module.exports = { 
  processPayment,
  pollPaymentStatus
};

```

### File: package-lock.json
```json
{
  "name": "mtn-momo-sdk",
  "version": "1.2.2",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "mtn-momo-sdk",
      "version": "1.2.2",
      "license": "MIT",
      "dependencies": {
        "axios": "^1.7.5",
        "dotenv": "^16.4.5",
        "uuid": "^10.0.0"
      }
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q=="
    },
    "node_modules/axios": {
      "version": "1.7.5",
      "resolved": "https://registry.npmjs.org/axios/-/axios-1.7.5.tgz",
      "integrity": "sha512-fZu86yCo+svH3uqJ/yTdQ0QHpQu5oL+/QE+QPSv6BZSkDAoky9vytxp7u5qk83OJFS3kEBcesWni9WTZAv3tSw==",
      "dependencies": {
        "follow-redirects": "^1.15.6",
        "form-data": "^4.0.0",
        "proxy-from-env": "^1.1.0"
      }
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/dotenv": {
      "version": "16.4.5",
      "resolved": "https://registry.npmjs.org/dotenv/-/dotenv-16.4.5.tgz",
      "integrity": "sha512-ZmdL2rui+eB2YwhsWzjInR8LldtZHGDoQ1ugH85ppHKwpUHL7j7rN0Ti9NCnGiQbhaZ11FpR+7ao1dNsmduNUg==",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://dotenvx.com"
      }
    },
    "node_modules/follow-redirects": {
      "version": "1.15.6",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.15.6.tgz",
      "integrity": "sha512-wWN62YITEaOpSK584EZXJafH1AGpO8RVgElfkuXbTOrPX4fIfOyEpW/CsiNd8JdYrAoOvafRTOEnvsO++qCqFA==",
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/RubenVerborgh"
        }
      ],
      "engines": {
        "node": ">=4.0"
      },
      "peerDependenciesMeta": {
        "debug": {
          "optional": true
        }
      }
    },
    "node_modules/form-data": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-4.0.0.tgz",
      "integrity": "sha512-ETEklSGi5t0QMZuiXoA/Q6vcnxcLQP5vdugSpuAyi6SVGi2clPPp+xgEhuMaHC+zGgn31Kd235W35f7Hykkaww==",
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.8",
        "mime-types": "^2.1.12"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/mime-db": {
      "version": "1.52.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
      "integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime-types": {
      "version": "2.1.35",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
      "integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
      "dependencies": {
        "mime-db": "1.52.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/proxy-from-env": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-1.1.0.tgz",
      "integrity": "sha512-D+zkORCbA9f1tdWRK0RaCR3GPv50cMxcrz4X8k5LTSUD1Dkw47mKJEZQNunItRTkWwgtaUSo1RVFRIG9ZXiFYg=="
    },
    "node_modules/uuid": {
      "version": "10.0.0",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-10.0.0.tgz",
      "integrity": "sha512-8XkAphELsDnEGrDxUOHB3RGvXz6TeuYSGEZBOjtTtPm2lwhGBjLgOzLHB63IUWfBpNucQjND6d3AOudO+H3RWQ==",
      "funding": [
        "https://github.com/sponsors/broofa",
        "https://github.com/sponsors/ctavan"
      ],
      "bin": {
        "uuid": "dist/bin/uuid"
      }
    }
  }
}

```

