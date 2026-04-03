<template>
  <div>
    <div class="d-flex align-center mb-6">
      <h1 class="text-h5 font-weight-bold">{{ $t('nav_users') }}</h1>
      <v-spacer />
      <v-btn color="primary" prepend-icon="mdi-account-plus" @click="inviteDialog = true">
        {{ $t('create_user') }}
      </v-btn>
    </div>

    <v-card>
      <v-table density="compact">
        <thead>
          <tr>
            <th>{{ $t('display_name') }}</th>
            <th>{{ $t('email') }}</th>
            <th>{{ $t('role') }}</th>
            <th>{{ $t('actions') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="u in userStore.users" :key="u.user_id">
            <td>{{ u.name }}</td>
            <td>{{ u.email }}</td>
            <td>
              <v-select
                :model-value="u.role"
                :items="roleOptions"
                density="compact"
                variant="plain"
                hide-details
                style="max-width: 140px"
                :disabled="u.user_id === authStore.user?.id"
                @update:model-value="changeRole(u.user_id, $event)"
              />
            </td>
            <td>
              <v-btn
                v-if="u.role === 'member' && u.user_id !== authStore.user?.id"
                icon="mdi-shield-edit"
                size="small"
                variant="text"
                @click="openPermissions(u)"
                title="Phân quyền"
              />
              <v-btn
                v-if="u.user_id !== authStore.user?.id"
                icon="mdi-lock-reset"
                size="small"
                variant="text"
                @click="openResetPassword(u)"
                title="Đặt lại mật khẩu"
              />
              <v-btn
                v-if="u.user_id !== authStore.user?.id"
                icon="mdi-delete"
                size="small"
                color="error"
                variant="text"
                @click="confirmRemove(u)"
              />
            </td>
          </tr>
        </tbody>
      </v-table>
    </v-card>

    <!-- Create user dialog -->
    <v-dialog v-model="inviteDialog" max-width="450">
      <v-card>
        <v-card-title>{{ $t('create_user') }}</v-card-title>
        <v-card-text>
          <v-form ref="createFormRef">
            <v-text-field v-model="inviteForm.name" :label="$t('display_name')" class="mb-2" :rules="[v => !!v || $t('validation_required')]" />
            <v-text-field v-model="inviteForm.email" label="Email" type="email" class="mb-2" :rules="[v => !!v || $t('validation_required'), v => /.+@.+\..+/.test(v) || 'Email invalid']" />
            <v-text-field v-model="inviteForm.password" :label="$t('password')" type="password" class="mb-2" :rules="[v => !!v || $t('validation_required'), v => v.length >= 6 || $t('password_too_short')]" />
            <v-select v-model="inviteForm.role" :items="roleOptions" :label="$t('role')" class="mb-2" />

            <!-- Member permissions -->
            <div v-if="inviteForm.role === 'member'" class="mt-2">
              <div class="text-subtitle-2 mb-2">{{ $t('permissions') }}</div>
              <v-table density="compact">
                <thead><tr><th>{{ $t('feature') }}</th><th>{{ $t('view') }}</th><th>{{ $t('edit') }}</th></tr></thead>
                <tbody>
                  <tr v-for="feat in permissionFeatures" :key="feat.key">
                    <td class="text-body-2">{{ feat.label }}</td>
                    <td><v-checkbox-btn v-model="inviteForm.permissions[feat.key]" true-value="r" false-value="" density="compact" /></td>
                    <td><v-checkbox-btn v-model="inviteForm.permissions[feat.key]" true-value="rw" :false-value="inviteForm.permissions[feat.key] === 'rw' ? 'r' : ''" density="compact" /></td>
                  </tr>
                </tbody>
              </v-table>
            </div>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn @click="inviteDialog = false">{{ $t('cancel') }}</v-btn>
          <v-btn color="primary" :loading="inviting" @click="doInvite">{{ $t('create_user') }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Remove confirm -->
    <v-dialog v-model="removeDialog" max-width="400">
      <v-card>
        <v-card-title>{{ $t('confirm') }}</v-card-title>
        <v-card-text>{{ $t('confirm_remove_user') }} <strong>{{ removeTarget?.email }}</strong>?</v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn @click="removeDialog = false">{{ $t('cancel') }}</v-btn>
          <v-btn color="error" @click="doRemove">{{ $t('delete') }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Permissions edit dialog -->
    <v-dialog v-model="permDialog" max-width="450">
      <v-card>
        <v-card-title>{{ $t('permissions') }} — {{ permTarget?.name }}</v-card-title>
        <v-card-text>
          <v-table density="compact">
            <thead><tr><th>{{ $t('feature') }}</th><th>{{ $t('view') }}</th><th>{{ $t('edit') }}</th></tr></thead>
            <tbody>
              <tr v-for="feat in permissionFeatures" :key="feat.key">
                <td class="text-body-2">{{ feat.label }}</td>
                <td><v-checkbox-btn v-model="editPerms[feat.key]" true-value="r" false-value="" density="compact" /></td>
                <td><v-checkbox-btn v-model="editPerms[feat.key]" true-value="rw" :false-value="editPerms[feat.key] === 'rw' ? 'r' : ''" density="compact" /></td>
              </tr>
            </tbody>
          </v-table>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn @click="permDialog = false">{{ $t('cancel') }}</v-btn>
          <v-btn color="primary" :loading="savingPerms" @click="savePermissions">{{ $t('save_settings') }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Reset password dialog -->
    <v-dialog v-model="resetDialog" max-width="400">
      <v-card>
        <v-card-title>Đặt lại mật khẩu — {{ resetTarget?.name }}</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="resetPassword"
            label="Mật khẩu mới"
            type="password"
            :rules="[v => !!v || 'Bắt buộc', v => v.length >= 8 || 'Tối thiểu 8 ký tự']"
          />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn @click="resetDialog = false">Hủy</v-btn>
          <v-btn color="primary" :loading="resettingPassword" @click="doResetPassword">Đặt lại</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-snackbar v-model="snack" :color="snackColor" timeout="3000">{{ snackText }}</v-snackbar>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore, type TenantUser } from '../stores/users'
import api from '../api'
import { useAuthStore } from '../stores/auth'

const route = useRoute()
const userStore = useUserStore()
const authStore = useAuthStore()
const tenantId = computed(() => route.params.tenantId as string)

const roleOptions = [
  { title: 'Owner', value: 'owner' },
  { title: 'Admin', value: 'admin' },
  { title: 'Member', value: 'member' },
]

const inviteDialog = ref(false)
const inviting = ref(false)
const inviteForm = ref({ name: '', email: '', password: '', role: 'member', permissions: { channels: 'r', messages: 'r', jobs: 'r', settings: '' } as Record<string, string> })
const createFormRef = ref<any>(null)
const permissionFeatures = [
  { key: 'channels', label: 'Kênh chat' },
  { key: 'messages', label: 'Tin nhắn' },
  { key: 'jobs', label: 'Công việc' },
  { key: 'settings', label: 'Cài đặt' },
]

const removeDialog = ref(false)
const removeTarget = ref<TenantUser | null>(null)

const permDialog = ref(false)
const permTarget = ref<TenantUser | null>(null)
const editPerms = ref<Record<string, string>>({})
const savingPerms = ref(false)

const resetDialog = ref(false)
const resetTarget = ref<TenantUser | null>(null)
const resetPassword = ref('')
const resettingPassword = ref(false)

const snack = ref(false)
const snackText = ref('')
const snackColor = ref('success')

onMounted(() => userStore.fetchUsers(tenantId.value))

async function doInvite() {
  const { valid } = await createFormRef.value?.validate() || {}
  if (!valid) return

  inviting.value = true
  try {
    const payload = {
      ...inviteForm.value,
      permissions: inviteForm.value.role === 'member' ? JSON.stringify(inviteForm.value.permissions) : '',
    }
    await userStore.inviteUser(tenantId.value, payload)
    inviteDialog.value = false
    inviteForm.value = { name: '', email: '', password: '', role: 'member', permissions: { channels: 'r', messages: 'r', jobs: 'r', settings: '' } }
    showSnack('User created', 'success')
  } catch (err: any) {
    showSnack(friendlyError(err), 'error')
  } finally {
    inviting.value = false
  }
}

async function changeRole(userId: string, role: string) {
  try {
    await userStore.updateRole(tenantId.value, userId, role)
    showSnack('Role updated', 'success')
  } catch (err: any) {
    showSnack(err.response?.data?.error || 'Error', 'error')
    userStore.fetchUsers(tenantId.value) // reload to revert
  }
}

function confirmRemove(u: TenantUser) {
  removeTarget.value = u
  removeDialog.value = true
}

async function doRemove() {
  if (!removeTarget.value) return
  try {
    await userStore.removeUser(tenantId.value, removeTarget.value.user_id)
    removeDialog.value = false
    showSnack('User removed', 'success')
  } catch (err: any) {
    showSnack(err.response?.data?.error || 'Error', 'error')
  }
}

function openPermissions(u: TenantUser) {
  permTarget.value = u
  try {
    editPerms.value = u.permissions ? JSON.parse(u.permissions) : { channels: 'r', messages: 'r', jobs: 'r', settings: '' }
  } catch {
    editPerms.value = { channels: 'r', messages: 'r', jobs: 'r', settings: '' }
  }
  permDialog.value = true
}

async function savePermissions() {
  if (!permTarget.value) return
  savingPerms.value = true
  try {
    await api.put(`/tenants/${tenantId.value}/users/${permTarget.value.user_id}/role`, {
      role: 'member',
      permissions: JSON.stringify(editPerms.value),
    })
    // Update local
    permTarget.value.permissions = JSON.stringify(editPerms.value)
    permDialog.value = false
    showSnack('Permissions updated', 'success')
  } catch (err: any) {
    showSnack(err.response?.data?.error || 'Error', 'error')
  } finally {
    savingPerms.value = false
  }
}

function openResetPassword(u: TenantUser) {
  resetTarget.value = u
  resetPassword.value = ''
  resetDialog.value = true
}

async function doResetPassword() {
  if (!resetTarget.value || resetPassword.value.length < 8) return
  resettingPassword.value = true
  try {
    await api.put(`/tenants/${tenantId.value}/users/${resetTarget.value.user_id}/reset-password`, {
      password: resetPassword.value,
    })
    resetDialog.value = false
    showSnack('Đã đặt lại mật khẩu', 'success')
  } catch (err: any) {
    showSnack(friendlyError(err), 'error')
  } finally {
    resettingPassword.value = false
  }
}

function friendlyError(err: any): string {
  const key = err?.response?.data?.error
  const msg = err?.response?.data?.message
  if (msg) return msg
  const map: Record<string, string> = {
    weak_password: 'Mật khẩu phải có ít nhất 8 ký tự, 1 chữ hoa và 1 chữ số',
    email_already_exists: 'Email đã tồn tại',
    invalid_request: 'Vui lòng kiểm tra lại thông tin',
    password_reset_failed: 'Không thể đặt lại mật khẩu',
  }
  return map[key] || key || 'Có lỗi xảy ra'
}

function showSnack(text: string, color: string) {
  snackText.value = text
  snackColor.value = color
  snack.value = true
}
</script>
