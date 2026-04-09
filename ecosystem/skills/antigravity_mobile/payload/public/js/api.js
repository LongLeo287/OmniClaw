/* ============================================
 * API — Server URL, auth, fetch helpers
 * ============================================ */

        // ====================================================================
        // State
        // ====================================================================
        let ws = null;
        let autoRefresh = false;
        let refreshTimer = null;
        let chatMessages = [];
        const serverUrl = window.location.origin;

        // Auth state
        let authToken = localStorage.getItem('authToken');

        // Helper for authenticated fetch
        async function authFetch(url, options = {}) {
            const headers = { ...(options.headers || {}) };
            if (authToken) {
                headers['Authorization'] = `Bearer ${authToken}`;
            }

            const res = await fetch(url, { ...options, headers });

            // If unauthorized, show login screen but don't throw for polling calls
            if (res.status === 401) {
                try {
                    const clonedRes = res.clone();
                    const data = await clonedRes.json();
                    if (data.needsAuth) {
                        authToken = null;
                        localStorage.removeItem('authToken');
                        showLoginScreen();
                    }
                } catch (e) {
                    // Ignore JSON parse errors
                }
            }

            return res;
        }

        // ====================================================================
        // Authentication
        // ====================================================================
        async function checkAuth() {
            try {
                const res = await fetch(`${serverUrl}/api/auth/status`);
                const data = await res.json();

                if (!data.authEnabled) {
                    // No auth required, hide login screen
                    hideLoginScreen();
                    return true;
                }

                // Auth is enabled, check if we have a valid token
                if (authToken) {
                    const testRes = await authFetch(`${serverUrl}/api/status`);
                    if (testRes.ok) {
                        hideLoginScreen();
                        return true;
                    }
                }

                // Need to login
                showLoginScreen();
                return false;
            } catch (e) {
                console.error('Auth check failed:', e);
                return false;
            }
        }

        function showLoginScreen() {
            document.getElementById('loginScreen').classList.remove('hidden');
        }

        function hideLoginScreen() {
            document.getElementById('loginScreen').classList.add('hidden');
        }

        async function submitPin() {
            const pin = document.getElementById('pinInput').value;
            const errorEl = document.getElementById('loginError');

            if (!pin || pin.length < 4) {
                errorEl.textContent = 'Please enter your PIN';
                errorEl.style.display = 'block';
                return;
            }

            try {
                const res = await fetch(`${serverUrl}/api/auth/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ pin })
                });

                const data = await res.json();

                if (data.success) {
                    authToken = data.token;
                    localStorage.setItem('authToken', authToken);
                    hideLoginScreen();
                    errorEl.style.display = 'none';
                    document.getElementById('pinInput').value = '';
                } else {
                    errorEl.textContent = data.error || 'Invalid PIN';
                    errorEl.style.display = 'block';
                }
            } catch (e) {
                errorEl.textContent = 'Connection error';
                errorEl.style.display = 'block';
            }
        }

        // Submit PIN on Enter key
        document.addEventListener('DOMContentLoaded', () => {
            document.getElementById('pinInput').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') submitPin();
            });
        });

        // ====================================================================
        // WebSocket
        // ====================================================================
