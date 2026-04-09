# Acceptance Criteria

## Authentication and Setup
- [ ] MUST use `AzureKeyCredential` from `azure.core.credentials` for authentication.
- [ ] MUST initialize `ConversationAnalysisClient` correctly with an endpoint and credential.
- [ ] MUST NOT hardcode API keys or endpoints in the code examples.

## Payload Construction
- [ ] MUST properly define the `task` dictionary with `"kind": "Conversation"`.
- [ ] MUST include a correctly structured `analysisInput` with `conversationItem` details (id, participantId, modality, text).
- [ ] MUST include required `parameters` (`projectName` and `deploymentName`).

## API Usage and Extraction
- [ ] MUST demonstrate calling `analyze_conversation`.
- [ ] MUST show how to correctly parse the response dictionary to extract the `topIntent` or entities.
- [ ] MUST use a context manager (`with client:`) for the client instance.