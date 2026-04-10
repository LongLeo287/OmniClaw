# Azure Identity SDK Acceptance Criteria

**SDK**: `azure-identity`
**Repository**: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity
**Commit**: `main`
**Purpose**: Skill testing acceptance criteria for validating generated code correctness

---

## 1. Correct Import Patterns

### 1.1 ✅ CORRECT: Sync Credential Imports

```python
from azure.identity import (
    DefaultAzureCredential,
    ManagedIdentityCredential,
    ClientSecretCredential,
    ClientCertificateCredential,
    InteractiveBrowserCredential,
    ChainedTokenCredential,
    TokenCachePersistenceOptions,
    AzureCliCredential,
    WorkloadIdentityCredential,
    DeviceCodeCredential,
)
```

### 1.2 ✅ CORRECT: Async Credential Imports

```python
from azure.identity.aio import (
    DefaultAzureCredential,
    ManagedIdentityCredential,
    ClientSecretCredential,
    ClientCertificateCredential,
    InteractiveBrowserCredential,
    ChainedTokenCredential,
    AzureCliCredential,
    WorkloadIdentityCredential,
)
```

### 1.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Using sync credential in async code

```python
# WRONG - async code must use azure.identity.aio credentials
from azure.identity import DefaultAzureCredential
from azure.storage.blob.aio import BlobServiceClient

credential = DefaultAzureCredential()  # sync credential with async client
async with BlobServiceClient(account_url, credential=credential) as client:
    pass
```

#### ❌ INCORRECT: TokenCachePersistenceOptions is not in azure.identity.aio

```python
# WRONG - token cache options are only in azure.identity (not .aio)
from azure.identity.aio import TokenCachePersistenceOptions
```

---

## 2. DefaultAzureCredential

### 2.1 ✅ CORRECT: Basic DefaultAzureCredential

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
token = credential.get_token("https://management.azure.com/.default")
print(token.expires_on)
```

### 2.2 ✅ CORRECT: Customize DefaultAzureCredential

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential(
    exclude_environment_credential=True,
    exclude_shared_token_cache_credential=True,
    exclude_interactive_browser_credential=False,
    managed_identity_client_id="<user-assigned-mi-client-id>",
)
```

### 2.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Hardcoded access token usage

```python
# WRONG - never hardcode access tokens
token = "eyJ0eXAiOiJKV1QiLCJhbGci..."
```

---

## 3. ManagedIdentityCredential

### 3.1 ✅ CORRECT: System-assigned Managed Identity

```python
from azure.identity import ManagedIdentityCredential

credential = ManagedIdentityCredential()
```

### 3.2 ✅ CORRECT: User-assigned Managed Identity

```python
from azure.identity import ManagedIdentityCredential

credential = ManagedIdentityCredential(client_id="<user-assigned-mi-client-id>")
```

### 3.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Passing tenant_id to ManagedIdentityCredential

```python
# WRONG - ManagedIdentityCredential doesn't accept tenant_id
credential = ManagedIdentityCredential(tenant_id="<tenant-id>")
```

---

## 4. ClientSecretCredential

### 4.1 ✅ CORRECT: Client Secret Auth

```python
import os
from azure.identity import ClientSecretCredential

credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"],
)
```

### 4.2 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Hardcoded secrets

```python
# WRONG - never hardcode secrets
credential = ClientSecretCredential(
    tenant_id="tenant-id",
    client_id="client-id",
    client_secret="super-secret",
)
```

---

## 5. CertificateCredential

### 5.1 ✅ CORRECT: Certificate from file path

```python
import os
from azure.identity import CertificateCredential

credential = CertificateCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    certificate_path=os.environ["AZURE_CLIENT_CERTIFICATE_PATH"],
)
```

### 5.2 ✅ CORRECT: Certificate from in-memory PEM data

```python
import os
from azure.identity import CertificateCredential

credential = CertificateCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    certificate_data=cert_pem_bytes,
)
```

### 5.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Using wrong parameter name for certificate

```python
# WRONG - parameter is certificate_path, not cert_path
credential = CertificateCredential(
    tenant_id="<tenant-id>",
    client_id="<client-id>",
    cert_path="/path/to/cert.pem",
)
```

#### ❌ INCORRECT: Passing both certificate_path and certificate_data

```python
# WRONG - use one or the other, not both
credential = CertificateCredential(
    tenant_id="<tenant-id>",
    client_id="<client-id>",
    certificate_path="/path/to/cert.pem",
    certificate_data=cert_pem_bytes,
)
```

---

## 6. WorkloadIdentityCredential

### 6.1 ✅ CORRECT: Default (env vars set by AKS webhook)

```python
from azure.identity import WorkloadIdentityCredential

credential = WorkloadIdentityCredential()
```

### 6.2 ✅ CORRECT: Explicit configuration

```python
from azure.identity import WorkloadIdentityCredential

credential = WorkloadIdentityCredential(
    tenant_id="<tenant-id>",
    client_id="<client-id>",
    token_file_path="/var/run/secrets/azure/tokens/azure-identity-token",
)
```

### 6.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Using client_secret with WorkloadIdentityCredential

```python
# WRONG - WorkloadIdentityCredential uses federated tokens, not secrets
credential = WorkloadIdentityCredential(
    tenant_id="<tenant-id>",
    client_id="<client-id>",
    client_secret="<secret>",
)
```

---

## 7. InteractiveBrowserCredential

### 7.1 ✅ CORRECT: Interactive Browser Auth

```python
from azure.identity import InteractiveBrowserCredential

credential = InteractiveBrowserCredential()
token = credential.get_token("https://management.azure.com/.default")
print(token.token)
```

### 7.2 ✅ CORRECT: Custom tenant and client ID

```python
from azure.identity import InteractiveBrowserCredential

credential = InteractiveBrowserCredential(
    tenant_id="<tenant-id>",
    client_id="<client-id>",
)
```

### 7.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Using sync InteractiveBrowserCredential in async code

```python
# WRONG - async code must use azure.identity.aio
from azure.identity import InteractiveBrowserCredential

credential = InteractiveBrowserCredential()
# This credential cannot be used with async clients
```

---

## 8. DeviceCodeCredential

### 8.1 ✅ CORRECT: Basic Device Code Auth

```python
from azure.identity import DeviceCodeCredential

credential = DeviceCodeCredential()
token = credential.get_token("https://management.azure.com/.default")
```

### 8.2 ✅ CORRECT: Custom prompt callback

```python
from azure.identity import DeviceCodeCredential

def prompt_callback(verification_uri, user_code, expires_on):
    print(f"Go to {verification_uri} and enter code: {user_code}")

credential = DeviceCodeCredential(prompt_callback=prompt_callback)
```

### 8.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Using DeviceCodeCredential in production services

```python
# WRONG - DeviceCodeCredential requires human interaction
# Use ManagedIdentityCredential or ClientSecretCredential for services
credential = DeviceCodeCredential()  # Do not use for automated/production workloads
```

---

## 9. ChainedTokenCredential

### 9.1 ✅ CORRECT: Custom Credential Chain

```python
from azure.identity import ChainedTokenCredential, ManagedIdentityCredential, AzureCliCredential

credential = ChainedTokenCredential(
    ManagedIdentityCredential(client_id="<user-assigned-mi-client-id>"),
    AzureCliCredential(),
)
```

### 9.2 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Passing strings instead of credential instances

```python
# WRONG - ChainedTokenCredential expects credential instances
credential = ChainedTokenCredential(
    "ManagedIdentityCredential",
    "AzureCliCredential",
)
```

#### ❌ INCORRECT: Passing a list instead of positional args

```python
# WRONG - credentials are positional arguments, not a list
credential = ChainedTokenCredential(
    [ManagedIdentityCredential(), AzureCliCredential()]
)
```

---

## 10. Token Caching

### 10.1 ✅ CORRECT: Enable persistent token cache

```python
from azure.identity import DefaultAzureCredential, TokenCachePersistenceOptions

cache_options = TokenCachePersistenceOptions(
    name="azure_identity_cache",
    allow_unencrypted_storage=True,
)

credential = DefaultAzureCredential(cache_persistence_options=cache_options)
```

### 10.2 ✅ CORRECT: In-memory token caching (default)

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
```

### 10.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Rolling your own disk cache for access tokens

```python
# WRONG - don't persist raw tokens yourself
with open("token.txt", "w") as handle:
    handle.write("<raw-token>")
```

---

## 11. Async Credential Lifecycle

### 11.1 ✅ CORRECT: Async credential with explicit close

```python
import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.storage.blob.aio import BlobServiceClient

async def main():
    credential = DefaultAzureCredential()

    async with BlobServiceClient(
        account_url="https://<account>.blob.core.windows.net",
        credential=credential
    ) as client:
        pass

    await credential.close()

asyncio.run(main())
```

### 11.2 ✅ CORRECT: Async credential as context manager

```python
import asyncio
from azure.identity.aio import ClientSecretCredential

async def main():
    async with ClientSecretCredential(
        tenant_id=os.environ["AZURE_TENANT_ID"],
        client_id=os.environ["AZURE_CLIENT_ID"],
        client_secret=os.environ["AZURE_CLIENT_SECRET"],
    ) as credential:
        token = await credential.get_token("https://management.azure.com/.default")
        print(token.token)

asyncio.run(main())
```

### 11.3 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Sync credential with async client

```python
# WRONG - must use azure.identity.aio for async clients
from azure.identity import DefaultAzureCredential
from azure.storage.blob.aio import BlobServiceClient

credential = DefaultAzureCredential()
async with BlobServiceClient(account_url, credential=credential) as client:
    pass  # Will fail or behave unexpectedly
```

#### ❌ INCORRECT: Not closing async credential

```python
# WRONG - async credential must be closed to release resources
from azure.identity.aio import DefaultAzureCredential

credential = DefaultAzureCredential()
token = await credential.get_token("https://management.azure.com/.default")
# Missing: await credential.close()
```

---

## 12. Error Handling

### 12.1 ✅ CORRECT: Catching authentication errors

```python
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ClientAuthenticationError

try:
    credential = DefaultAzureCredential()
    token = credential.get_token("https://management.azure.com/.default")
except ClientAuthenticationError as e:
    print(f"Authentication failed: {e.message}")
```

### 12.2 Anti-Patterns (ERRORS)

#### ❌ INCORRECT: Bare except or swallowing authentication errors

```python
# WRONG - don't silently swallow authentication errors
try:
    credential = DefaultAzureCredential()
    token = credential.get_token("https://management.azure.com/.default")
except Exception:
    pass  # Silent failure hides misconfiguration
```
