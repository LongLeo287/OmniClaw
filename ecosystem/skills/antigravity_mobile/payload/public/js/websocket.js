/* ============================================
 * WebSocket — Connection, message handling
 * ============================================ */

        function connectWebSocket() {
            const wsUrl = serverUrl.replace('http', 'ws');
            ws = new WebSocket(wsUrl);

            ws.onopen = () => {
                updateStatus(true);
                const wsEl = document.getElementById('wsStatus');
                wsEl.innerHTML = '<svg class="status-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Connected';
                wsEl.style.color = 'var(--success)';
            };

            ws.onclose = () => {
                updateStatus(false);
                const wsEl = document.getElementById('wsStatus');
                wsEl.innerHTML = '<svg class="status-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg> Disconnected';
                wsEl.style.color = 'var(--error)';
                setTimeout(connectWebSocket, 3000);
            };

            ws.onerror = () => updateStatus(false);

            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                handleMessage(data);
            };
        }

        function handleMessage(data) {
            if (data.event === 'history') {
                data.data.messages.forEach(msg => addChatMessage(msg, false));
            } else if (data.event === 'message' || data.event === 'mobile_command') {
                addChatMessage(data.data, true);
            } else if (data.event === 'file_changed') {
                // Auto-refresh file list when files change
                handleFileChanged(data.data);
            } else if (data.event === 'workspace_changed') {
                // IDE workspace changed - update file browser
                handleWorkspaceChanged(data.data);
            }
        }

        function handleWorkspaceChanged(data) {
            console.log('📂 Workspace changed:', data.path);

            // Update the workspace path display if we have one
            const workspaceLabel = document.getElementById('workspaceLabel');
            if (workspaceLabel) {
                workspaceLabel.textContent = data.projectName || 'Files';
            }

            // If files panel is open, reload from new workspace root
            const filesPanel = document.getElementById('filesPanel');
            if (filesPanel.classList.contains('open')) {
                // Reset to workspace root
                currentFilePath = '';
                loadFiles('');
                showToast(`📂 Switched to: ${data.projectName}`, 'status');
            }
        }

        function handleFileChanged(data) {
            // Only refresh if files panel is open
            const filesPanel = document.getElementById('filesPanel');
            if (!filesPanel.classList.contains('open')) return;

            console.log('📁 File changed:', data.filename);

            // Reload current folder
            if (currentFilePath) {
                loadFiles(currentFilePath);
            }

            // If viewing a file that changed, show a notification
            if (currentViewingFile && data.filename) {
                const viewingFilename = currentViewingFile.split(/[/\\]/).pop();
                if (viewingFilename === data.filename) {
                    showToast('File changed - tap to reload', 'status');
                }
            }
        }
