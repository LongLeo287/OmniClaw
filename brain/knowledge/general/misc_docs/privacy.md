---
id: privacy
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:01.910700
---

# Privacy Policy for Assistant Context

**Last updated:** December 2024

## Introduction

Assistant Context ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how our Chrome extension handles your data.

## Our Commitment to Privacy

**We do NOT collect, store, or transmit any of your personal data to our servers.** This extension operates entirely locally on your device and only communicates directly with third-party AI service providers (OpenAI and Google Gemini) when you explicitly use the chat feature.

## Data Collection and Storage

### What We Do NOT Do

- ❌ We do **NOT** collect any personal information
- ❌ We do **NOT** store your data on our servers
- ❌ We do **NOT** track your browsing activity
- ❌ We do **NOT** collect analytics or usage statistics
- ❌ We do **NOT** sell or share your data with third parties
- ❌ We do **NOT** have access to your stored data

### Local Storage Only

All data is stored **locally** on your device using Chrome's built-in `chrome.storage.sync` API:

- **API Keys**: Your OpenAI and Gemini API keys are stored locally in your browser. They are never transmitted to us or any third party except when you use the chat feature, at which point they are sent directly to the respective API provider (OpenAI or Google).
- **Settings**: Your preferences (model selection, transparency settings, etc.) are stored locally.
- **Custom Prompts**: Your custom prompts are stored locally.

**Important**: We have no access to any of this locally stored data. It remains on your device and is synced across your Chrome browsers only if you have Chrome sync enabled.

## Third-Party Services

This extension communicates directly with third-party AI service providers:

### OpenAI API
- When you use OpenAI models, your messages and API key are sent **directly** to OpenAI (`https://api.openai.com`)
- We do not intercept, store, or have access to these communications
- Please review [OpenAI's Privacy Policy](https://openai.com/policies/privacy-policy) for information on how they handle your data

### Google Gemini API
- When you use Gemini models, your messages and API key are sent **directly** to Google (`https://generativelanguage.googleapis.com`)
- We do not intercept, store, or have access to these communications
- Please review [Google's Privacy Policy](https://policies.google.com/privacy) for information on how they handle your data

## Data Security

- All data is stored locally in your browser using Chrome's secure storage API
- API keys are encrypted by Chrome's storage system
- We do not have servers that could be compromised
- We do not have access to your stored data

## Permissions Explained

This extension requires the following permissions:

- **`contextMenus`**: To add right-click menu options for quick access
- **`storage`**: To save your API keys and preferences locally on your device (not on our servers)
- **`activeTab`**: To inject the chat interface on web pages you visit
- **`scripting`**: To inject content scripts that enable the chat popup
- **`host_permissions`** (`https://api.openai.com/*` and `https://generativelanguage.googleapis.com/*`): To communicate directly with OpenAI and Google Gemini APIs when you use the chat feature

**None of these permissions are used to collect or transmit your data to us.**

## Open Source

This extension is open source. You can review the source code at: https://github.com/huynamboz/assistant-context

## Changes to This Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by updating the "Last updated" date at the top of this document.

## Contact

If you have questions about this Privacy Policy, please contact us via:
- GitHub: https://github.com/huynamboz/assistant-context
- GitHub Issues: https://github.com/huynamboz/assistant-context/issues

---

**Summary**: This extension does not collect, store, or transmit any of your data to our servers. All data remains on your device, and API communications go directly to OpenAI or Google Gemini when you use the chat feature.