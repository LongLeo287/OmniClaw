/**
 * Ollama Client - Thin wrapper around the Ollama REST API
 * 
 * Uses Node 18+ built-in fetch, no npm dependencies required.
 * Default endpoint: http://localhost:11434
 */

let endpoint = 'http://localhost:11434';

/**
 * Set the Ollama API endpoint URL
 */
export function setEndpoint(url) {
    endpoint = url.replace(/\/+$/, '');
}

/**
 * Get the current endpoint URL
 */
export function getEndpoint() {
    return endpoint;
}

/**
 * Check if Ollama is available
 * @returns {{ available: boolean, error?: string, models?: string[] }}
 */
export async function isAvailable() {
    try {
        const res = await fetch(`${endpoint}/api/tags`, {
            signal: AbortSignal.timeout(5000)
        });
        if (!res.ok) return { available: false, error: `HTTP ${res.status}` };
        const data = await res.json();
        const models = (data.models || []).map(m => m.name);
        return { available: true, models };
    } catch (e) {
        return { available: false, error: e.message };
    }
}

/**
 * List available models
 * @returns {string[]}
 */
export async function listModels() {
    try {
        const res = await fetch(`${endpoint}/api/tags`, {
            signal: AbortSignal.timeout(5000)
        });
        if (!res.ok) return [];
        const data = await res.json();
        return (data.models || []).map(m => m.name);
    } catch (e) {
        return [];
    }
}

/**
 * Send a chat conversation to Ollama
 * @param {Array<{role: string, content: string}>} messages - Conversation messages
 * @param {string} model - Model name (e.g. 'llama3', 'mistral')
 * @param {object} [options] - Additional options
 * @returns {{ success: boolean, response?: string, error?: string }}
 */
export async function chat(messages, model, options = {}) {
    try {
        const body = {
            model,
            messages,
            stream: false,
            ...options
        };

        const res = await fetch(`${endpoint}/api/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body),
            signal: AbortSignal.timeout(120000) // 2 min timeout for LLM responses
        });

        if (!res.ok) {
            const text = await res.text().catch(() => '');
            return { success: false, error: `HTTP ${res.status}: ${text}` };
        }

        const data = await res.json();
        return {
            success: true,
            response: data.message?.content || '',
            model: data.model,
            totalDuration: data.total_duration,
            evalCount: data.eval_count
        };
    } catch (e) {
        return { success: false, error: e.message };
    }
}

/**
 * Streaming chat — calls onToken(text) for each token as it arrives
 * @param {Array<{role: string, content: string}>} messages
 * @param {string} model
 * @param {function(string): void} onToken - Called with each text chunk
 * @returns {{ success: boolean, response?: string, error?: string }}
 */
export async function chatStream(messages, model, onToken, options = {}) {
    try {
        const body = { model, messages, stream: true };
        if (options.num_ctx) body.options = { num_ctx: options.num_ctx };
        const res = await fetch(`${endpoint}/api/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body),
            signal: AbortSignal.timeout(300000) // 5 min for streaming
        });

        if (!res.ok) {
            const text = await res.text().catch(() => '');
            return { success: false, error: `HTTP ${res.status}: ${text}` };
        }

        let fullResponse = '';
        const reader = res.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop(); // keep incomplete line in buffer

            for (const line of lines) {
                if (!line.trim()) continue;
                try {
                    const chunk = JSON.parse(line);
                    const token = chunk.message?.content || '';
                    if (token) {
                        fullResponse += token;
                        onToken(token);
                    }
                } catch (parseErr) {
                    // skip malformed lines
                }
            }
        }

        // Process any remaining buffer
        if (buffer.trim()) {
            try {
                const chunk = JSON.parse(buffer);
                const token = chunk.message?.content || '';
                if (token) {
                    fullResponse += token;
                    onToken(token);
                }
            } catch (e) { }
        }

        return { success: true, response: fullResponse };
    } catch (e) {
        return { success: false, error: e.message };
    }
}

/**
 * Simple generate (non-chat) API call
 * @param {string} prompt - The prompt text
 * @param {string} model - Model name
 * @returns {{ success: boolean, response?: string, error?: string }}
 */
export async function generate(prompt, model) {
    try {
        const res = await fetch(`${endpoint}/api/generate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ model, prompt, stream: false }),
            signal: AbortSignal.timeout(120000)
        });

        if (!res.ok) {
            const text = await res.text().catch(() => '');
            return { success: false, error: `HTTP ${res.status}: ${text}` };
        }

        const data = await res.json();
        return { success: true, response: data.response || '' };
    } catch (e) {
        return { success: false, error: e.message };
    }
}
