---
id: social
type: knowledge
owner: OA_Triage
---
# social
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "social-downloader",
  "displayName": "Social Downloader",
  "version": "0.0.1",
  "description": "Download Social Media with one click.",
  "author": "minhchi1509",
  "scripts": {
    "dev": "plasmo dev",
    "build": "plasmo build --zip && mv build/chrome-mv3-prod.zip social_downloader_extension.zip",
    "package": "plasmo package",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {
    "@ant-design/cssinjs": "^1.23.0",
    "@fast-csv/format": "^5.0.2",
    "antd": "^5.24.4",
    "axios": "^1.8.3",
    "clsx": "^2.1.1",
    "dayjs": "^1.11.13",
    "fast-csv": "^5.0.2",
    "plasmo": "0.90.3",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "react-router-dom": "^7.4.0",
    "sonner": "^2.0.1",
    "tailwind-merge": "^3.0.2",
    "tailwindcss": "3.4.1",
    "uuid": "^11.1.0",
    "zustand": "^5.0.3"
  },
  "devDependencies": {
    "@ianvs/prettier-plugin-sort-imports": "4.1.1",
    "@types/chrome": "0.0.258",
    "@types/node": "20.11.5",
    "@types/react": "18.2.48",
    "@types/react-dom": "18.2.18",
    "postcss": "8.4.33",
    "prettier": "3.2.4",
    "sass": "^1.86.0",
    "typescript": "5.3.3"
  },
  "manifest": {
    "permissions": [
      "cookies",
      "downloads",
      "webRequest",
      "webRequestBlocking",
      "declarativeNetRequest",
      "<all_urls>",
      "activeTab",
      "scripting",
      "tabs",
      "storage"
    ],
    "host_permissions": [
      "<all_urls>"
    ]
  }
}

```

### File: README.md
```md
# Extension tải xuống hàng loạt cho các mạng xã hội

## Giới thiệu

- Đây là một extension cho phép người dùng tải xuống hàng loạt ảnh, video trên các nền tảng mạng xã hội: **Facebook**, **Instagram**, **Threads** và **X**

## Tính năng

- Đối với **Facebook**: Tải xuống tất cả ảnh, video, reel, highlight, story của một trang cá nhân, hoặc Fanpage
- Đối với **Instagram**: Tải xuống ảnh, video từ tất cả các bài viết, reel, highlight, story của profile công khai hoặc riêng tư (nếu bạn đã theo dõi họ)
- Đối với **Threads**: Tải xuống ảnh, video, audio từ tất cả các bài viết của profile công khai, riêng tư (nếu bạn đã theo dõi họ)
- Đối với **X**: Tải xuống tất cả ảnh, video trên trang cá nhân
- Ngoài ra bạn có thể tải riêng lẻ ảnh, video, theo URL.
- Có thể hủy bỏ tiến trình tải nếu cần

## Cài đặt

- Click vào đây để tải xuống extension: [Social Downloader Extension](https://github.com/minhchi1509/social_downloader_extension/raw/main/social_downloader_extension.zip)
- Giải nén, vào **Chrome Extension**, chọn **Load unpacked** ➡️ Upload folder vừa giải nén lên, sau đó click vào icon của extension.
- Ở phía Sidebar bên trái, chọn **Tài khoản**, sau đó thực hiện xác thực các tài khoản để sử dụng các tính năng tải.

> [!TIP]
> Nếu mọi người thấy extension hữu ích, hãy ủng hộ em/mình bằng 1 sao trên repo này hoặc nếu mọi người có nhu cầu donate thì thông qua STK: 1500206139515 (Agribank) - NGUYEN MINH CHI. Em xin cảm ơn

```

### File: postcss.config.js
```js
/**
 * @type {import('postcss').ProcessOptions}
 */
module.exports = {
  plugins: {
    tailwindcss: {}
  }
}

```

### File: tailwind.config.js
```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{tsx,html}"],
  darkMode: "media",
  important: true
}

```

### File: tsconfig.json
```json
{
  "extends": "plasmo/templates/tsconfig.base",
  "exclude": ["node_modules"],
  "include": [".plasmo/index.d.ts", "./**/*.ts", "./**/*.tsx"],
  "compilerOptions": {
    "strict": true,
    "verbatimModuleSyntax": false,
    "paths": {
      "src/*": ["./src/*"]
    },
    "baseUrl": "."
  }
}

```

### File: src\background.ts
```ts
import { ERemoteMessageType } from "src/constants/enum"

chrome.action.onClicked.addListener(() => {
  chrome.runtime.openOptionsPage()
})

let xHeadersData: any = null

chrome.runtime.onInstalled.addListener(async () => {
  const rules = [
    {
      id: 1,
      priority: 1,
      action: {
        type: "modifyHeaders",
        requestHeaders: [
          {
            header: "Origin",
            operation: "remove"
          }
        ]
      },
      condition: {
        urlFilter: "https://www.facebook.com/api/graphql/*",
        resourceTypes: ["xmlhttprequest"]
      }
    }
  ]

  await chrome.declarativeNetRequest.updateDynamicRules({
    removeRuleIds: [1],
    addRules: rules as any
  })

  console.log(
    "Rule to remove Origin header for Facebook GraphQL API has been applied."
  )
})

chrome.webRequest.onBeforeSendHeaders.addListener(
  (details) => {
    const headers = details.requestHeaders || []
    const authorization =
      headers.find((h) => h.name.toLowerCase() === "authorization")?.value || ""
    const xCsrfToken =
      headers.find((h) => h.name.toLowerCase() === "x-csrf-token")?.value || ""

    // Lưu header mới nhất
    if (authorization && xCsrfToken) {
      xHeadersData = {
        authorization,
        xCsrfToken
      }
    }
  },
  { urls: ["*://x.com/i/api/graphql/*"] },
  ["requestHeaders", "extraHeaders"]
)

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === ERemoteMessageType.RETRIEVE_X_ACCOUNT_CREDENTIALS) {
    sendResponse(xHeadersData)
  }
})

```

### File: src\style.css
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

#plasmo-shadow-container {
  all: initial;
  box-sizing: border-box;
}

```

### File: src\configs\axios.config.ts
```ts
import axios from "axios"

import { ESocialProvider } from "src/constants/enum"
import { REQUEST_ACCEPT_HEADER } from "src/constants/variables"
import useAuth from "src/store/auth"

const igAxiosInstance = axios.create({
  baseURL: "https://www.instagram.com/graphql/query"
})

const threadsAxiosInstance = axios.create({
  baseURL: "https://www.threads.net/graphql/query"
})

const fbAxiosInstance = axios.create({
  baseURL: "https://www.facebook.com/api/graphql"
})

const xAxiosInstance = axios.create({
  baseURL: "https://x.com/i/api/graphql"
})

threadsAxiosInstance.interceptors.request.use((config) => {
  const { accounts } = useAuth.getState()
  const igAppId = accounts[ESocialProvider.THREADS]?.igAppId

  if (igAppId) {
    config.headers["x-ig-app-id"] = igAppId
  }
  config.headers["Accept"] = REQUEST_ACCEPT_HEADER
  return config
})

fbAxiosInstance.interceptors.request.use((config) => {
  config.headers["Accept"] = REQUEST_ACCEPT_HEADER

  return config
})

igAxiosInstance.interceptors.request.use((config) => {
  config.headers["Accept"] = REQUEST_ACCEPT_HEADER

  return config
})

xAxiosInstance.interceptors.request.use((config) => {
  const { accounts } = useAuth.getState()
  const xAccount = accounts[ESocialProvider.X]
  if (xAccount) {
    config.headers["authorization"] = xAccount.accessToken
    config.headers["x-csrf-token"] = xAccount.csrfToken
  }
  return config
})

export {
  threadsAxiosInstance,
  igAxiosInstance,
  fbAxiosInstance,
  xAxiosInstance
}

```

### File: src\constants\enum.ts
```ts
export enum EStorageKey {
  ACCOUNTS = "ACCOUNTS",
  THREADS_PROFILE = "THREADS_PROFILE",
  INSTAGRAM_PROFILE = "INSTAGRAM_PROFILE",
  FACEBOOK_PROFILE = "FACEBOOK_PROFILE"
}

export enum ESocialProvider {
  FACEBOOK = "FACEBOOK",
  INSTAGRAM = "INSTAGRAM",
  THREADS = "THREADS",
  X = "X"
}

export enum EDownloadSeperateType {
  FACEBOOK_POST = "FACEBOOK_POST",
  FACEBOOK_STORY = "FACEBOOK_STORY",
  FACEBOOK_VIDEO = "FACEBOOK_VIDEO",
  FACEBOOK_REEL = "FACEBOOK_REEL",
  FACEBOOK_COMMENT_VIDEO = "FACEBOOK_COMMENT_VIDEO",

  INSTAGRAM_POST = "INSTAGRAM_POST",
  INSTAGRAM_REEL = "INSTAGRAM_REEL",
  INSTAGRAM_HIGHLIGHT = "INSTAGRAM_HIGHLIGHT",

  THREADS_POST = "THREADS_POST"
}

export enum ERemoteMessageType {
  RETRIEVE_X_ACCOUNT_CREDENTIALS = "RETRIEVE_X_ACCOUNT_CREDENTIALS"
}

```

### File: src\constants\regex.ts
```ts
import { EDownloadSeperateType } from "src/constants/enum"

const FACEBOOK_POST_URL_PATTERN =
  /https:\/\/www\.facebook\.com\/[^\/]+\/posts\/([\w-]+)/

const FACEBOOK_STORY_URL_PATTERN =
  /https:\/\/www\.facebook\.com\/stories\/([\w-]+)/

const FACEBOOK_VIDEO_URL_PATTERN =
  /https:\/\/www\.facebook\.com\/[^\/]+\/videos\/([\w-]+)/

const FACEBOOK_REEL_URL_PATTERN =
  /https:\/\/www\.facebook\.com\/(?:reel\/|watch\/\?v=)([\w-]+)/

const INSTAGRAM_POST_URL_PATTERN = /https:\/\/www\.instagram\.com\/p\/([\w-]+)/

const INSTAGRAM_REEL_URL_PATTERN =
  /https:\/\/www\.instagram\.com\/reel\/([\w-]+)/

const INSTAGRAM_HIGHLIGHT_URL_PATTERN =
  /https:\/\/www\.instagram\.com\/stories\/highlights\/([\w-]+)/

const THREADS_POST_URL_PATTERN =
  /https:\/\/www\.threads\.net\/@[^\/]+\/post\/([\w-]+)/

export const URL_PATTERN = {
  [EDownloadSeperateType.FACEBOOK_POST]: FACEBOOK_POST_URL_PATTERN,
  [EDownloadSeperateType.FACEBOOK_STORY]: FACEBOOK_STORY_URL_PATTERN,
  [EDownloadSeperateType.FACEBOOK_VIDEO]: FACEBOOK_VIDEO_URL_PATTERN,
  [EDownloadSeperateType.FACEBOOK_REEL]: FACEBOOK_REEL_URL_PATTERN,

  [EDownloadSeperateType.INSTAGRAM_POST]: INSTAGRAM_POST_URL_PATTERN,
  [EDownloadSeperateType.INSTAGRAM_REEL]: INSTAGRAM_REEL_URL_PATTERN,
  [EDownloadSeperateType.INSTAGRAM_HIGHLIGHT]: INSTAGRAM_HIGHLIGHT_URL_PATTERN,

  [EDownloadSeperateType.THREADS_POST]: THREADS_POST_URL_PATTERN
}

```

### File: src\constants\route.ts
```ts
export const APP_ROUTES = {
  ACCOUNTS: "/accounts",
  DOWNLOAD_ALL: {
    FACEBOOK: "/download-all/facebook",
    INSTAGRAM: "/download-all/instagram",
    THREADS: "/download-all/threads",
    X: "/download-all/x"
  },
  DOWNLOAD_SEPERATE: "/download-seperate"
}

```

### File: src\constants\variables.ts
```ts
import { EDownloadSeperateType } from "src/constants/enum"

export const IG_DOWNLOAD_ALL_TYPE = [
  { label: "Ảnh/video trên bài viết", value: "POST" },
  { label: "Reels", value: "REEL" },
  { label: "Story nổi bật", value: "HIGHLIGHT" },
  { label: "Story", value: "STORY" }
]

export const THREADS_DOWNLOAD_ALL_TYPE = [
  { label: "Ảnh/video trên bài viết", value: "POST" }
]

export const X_DOWNLOAD_ALL_TYPE = [
  { label: "Ảnh/video trên trang cá nhân", value: "MEDIA" }
]

export const FB_DOWNLOAD_ALL_TYPE = [
  { label: "Ảnh", value: "PHOTO" },
  { label: "Video", value: "VIDEO" },
  { label: "Reels", value: "REEL" },
  { label: "Story nổi bật", value: "HIGHLIGHT" }
]

export const DOWNLOAD_SEPARATELY_TYPE = [
  { label: "Ảnh/video trên bài viết", value: "POST" },
  { label: "Reels", value: "REEL" },
  { label: "Story nổi bật", value: "HIGHLIGHT" },
  { label: "Story", value: "STORY" },
  { label: "Ảnh đại diện (HD)", value: "AVATAR" }
]

export const DOWNLOAD_SEPERATE_TYPE_OPTIONS = [
  {
    group: "Facebook",
    options: [
      {
        label: "Ảnh/video trên bài viết (Facebook)",
        value: EDownloadSeperateType.FACEBOOK_POST
      },
      {
        label: "Reels/Watch (Facebook)",
        value: EDownloadSeperateType.FACEBOOK_REEL
      },
      {
        label: "Video (Facebook)",
        value: EDownloadSeperateType.FACEBOOK_VIDEO
      },
      {
        label: "Story/Highlight (Facebook)",
        value: EDownloadSeperateType.FACEBOOK_STORY
      },
      {
        label: "Video ở bình luận (Facebook)",
        value: EDownloadSeperateType.FACEBOOK_COMMENT_VIDEO
      }
    ]
  },
  {
    group: "Instagram",
    options: [
      {
        label: "Ảnh/video trên bài viết (Instagram)",
        value: EDownloadSeperateType.INSTAGRAM_POST
      },
      {
        label: "Reels (Instagram)",
        value: EDownloadSeperateType.INSTAGRAM_REEL
      },
      {
        label: "Story nổi bật (Instagram)",
        value: EDownloadSeperateType.INSTAGRAM_HIGHLIGHT
      }
    ]
  },
  {
    group: "Threads",
    options: [
      {
        label: "Ảnh/video trên bài viết (Threads)",
        value: EDownloadSeperateType.THREADS_POST
      }
    ]
  }
]

export const DOWNLOAD_TYPE_TAG_COLOR = {
  POST: "blue",
  REEL: "green",
  HIGHLIGHT: "gold",
  STORY: "purple",
  VIDEO: "red",
  PHOTO: "cyan",
  MEDIA: "magenta"
}

export const PROCESS_STATUS_TAG_COLOR = {
  RUNNING: "blue",
  COMPLETED: "green",
  FAILED: "red"
}

export const PROCESS_TEXT = {
  RUNNING: "Đang tải",
  COMPLETED: "Hoàn thành",
  FAILED: "Thất bại"
}

export const DOWNLOAD_STORIES_IN_HIGHLIGHT_BATCH_SIZE = 15
export const REQUEST_ACCEPT_HEADER =
  "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
export const MAX_RETRY_REQUEST = 15

```

### File: src\interfaces\account.interface.ts
```ts
import { ESocialProvider } from "src/constants/enum"

export interface IAccountData {
  id: string
  username: string
  avatar: string
  cookies: string
}

export interface IInstagramAccount extends IAccountData {
  csrfToken: string
}

export interface IThreadsAccount extends IAccountData {
  igAppId: string
}
export interface IFacebookAccount extends IAccountData {
  fbDtsg: string
}

export interface IXAccount extends IAccountData {
  csrfToken: string
  accessToken: string
}

export interface IAccounts {
  [ESocialProvider.FACEBOOK]: IFacebookAccount | null
  [ESocialProvider.INSTAGRAM]: IInstagramAccount | null
  [ESocialProvider.THREADS]: IThreadsAccount | null
  [ESocialProvider.X]: IXAccount | null
}

```

### File: src\interfaces\common.interface.ts
```ts
export interface IDownloadAllOptions {
  waitUntilCompleted: boolean
  delayTimeInSecond?: number
}

export interface IMedia {
  id: string
  downloadUrl: string
}

```

### File: src\interfaces\download-process.interface.ts
```ts
import { ESocialProvider } from "src/constants/enum"

export type TProcessStatus = "RUNNING" | "COMPLETED" | "FAILED"

export type TIgDownloadAllType = "POST" | "REEL" | "HIGHLIGHT" | "STORY"
export type TThreadsDownloadAllType = "POST"
export type TFacebookDownloadAllType = "PHOTO" | "VIDEO" | "REEL" | "HIGHLIGHT"
export type TXDownloadAllType = "MEDIA"

export interface IDownloadProcessDetail<T> {
  id: string
  username: string
  downloadType: T
  totalDownloadedItems: number
  status: TProcessStatus
}

export interface IDownloadProcess {
  [ESocialProvider.FACEBOOK]: IDownloadProcessDetail<TFacebookDownloadAllType>
  [ESocialProvider.INSTAGRAM]: IDownloadProcessDetail<TIgDownloadAllType>
  [ESocialProvider.THREADS]: IDownloadProcessDetail<TThreadsDownloadAllType>
  [ESocialProvider.X]: IDownloadProcessDetail<TXDownloadAllType>
}

```

### File: src\interfaces\facebook.interface.ts
```ts
import { IMedia } from "src/interfaces/common.interface"

export interface IFacebookStory extends IMedia {
  isVideo: boolean
  thumbnailUrl?: string
}

export interface IFacebookPost extends IMedia {
  isVideo: boolean
}

```

### File: src\interfaces\form.interface.ts
```ts
import { EDownloadSeperateType } from "src/constants/enum"
import { IDownloadAllOptions } from "src/interfaces/common.interface"
import {
  TFacebookDownloadAllType,
  TIgDownloadAllType,
  TThreadsDownloadAllType,
  TXDownloadAllType
} from "src/interfaces/download-process.interface"

export interface IDownloadAllForm<T> extends IDownloadAllOptions {
  username: string
  type: T
}

export interface IIgDownloadAllForm
  extends IDownloadAllForm<TIgDownloadAllType> {}

export interface IThreadsDownloadAllForm
  extends IDownloadAllForm<TThreadsDownloadAllType> {}

export interface IFacebookDownloadAllForm
  extends IDownloadAllForm<TFacebookDownloadAllType> {}

export interface IXDownloadAllForm
  extends IDownloadAllForm<TXDownloadAllType> {}

export interface IDownloadSeperateForm {
  url: string
  type: EDownloadSeperateType
}

```

### File: src\interfaces\instagram.interface.ts
```ts
import { IMedia } from "src/interfaces/common.interface"

export interface IIGProfile {
  id: string
  username: string
  full_name: string
  avatar_url: string
  follower: number
  following: number
  is_private_account: boolean
  total_posts: number
}

export interface IIGPost {
  id: string
  code: string
  title?: string
  takenAt: string
  totalMedia: number
  videoCount: number
  imageCount: number
  likeCount: number | null
  commentCount: number
  videos: IMedia[]
  images: IMedia[]
}

export interface IIGReel {
  id: number
  code: string
  title?: string
  takenAt: string
  likeCount: number | null
  commentCount: number
  downloadUrl: string
}

export interface IIGStory {
  id: string
  downloadUrl: string
  isVideo: boolean
  takenAt: number
}

export interface IIGHighlightStory {
  id: string
  title: string
  totalStories: number
  imageStoryCount: number
  videoStoryCount: number
  stories: IIGStory[]
}

```

### File: src\interfaces\threads.interface.ts
```ts
import { IMedia } from "src/interfaces/common.interface"
import { IIGPost } from "src/interfaces/instagram.interface"

export interface IThreadsPost extends IIGPost {
  audioCount: number
  audios: IMedia[]
}

```

### File: src\interfaces\x.interface.ts
```ts
import { IMedia } from "src/interfaces/common.interface"

export interface IXMedia extends IMedia {
  isVideo: boolean
}

```

### File: src\services\facebook.service.ts
```ts
import axios from "axios"

import { fbAxiosInstance } from "src/configs/axios.config"
import { ESocialProvider } from "src/constants/enum"
import { IFacebookAccount } from "src/interfaces/account.interface"
import {
  IFacebookPost,
  IFacebookStory
} from "src/interfaces/facebook.interface"
import useAuth from "src/store/auth"
import { chromeUtils } from "src/utils/chrome.util"

const makeRequestToFb = async (docID: string, query: any) => {
  try {
    const fbAccountData = useAuth.getState().accounts[ESocialProvider.FACEBOOK]
    if (!fbAccountData) {
      throw new Error("Vui lòng xác thực tài khoản Facebook trước")
    }
    const formData = new FormData()
    formData.set("__a", "1")
    formData.set("__comet_req", "15")
    formData.set("fb_dtsg", fbAccountData.fbDtsg)
    formData.set("av", fbAccountData.id)
    formData.set("doc_id", docID)
    formData.set("variables", JSON.stringify(query))
    const { data } = await fbAxiosInstance.post("/", formData)
    return data
  } catch (error) {
    throw new Error("Đã xảy ra lỗi khi gửi yêu cầu đến Facebook")
  }
}

const getFacebookAccountData = async () => {
  try {
    const cookies = await chromeUtils.getChromeCookies("facebook.com")
    const axiosInstance = axios.create({
      baseURL: "https://www.facebook.com",
      headers: {
        cookie: cookies,
        Accept:
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
      }
    })
    const { data: rawData } = await axiosInstance.get("/")

    const profileRegex = /"story_bucket_owner":(.*?),"story_bucket_type":/
    const fbDtsgRegex = /"DTSGInitialData".*?"token":"(.*?)"/
    const originalProfileInfor = rawData.match(profileRegex)
    const fbDtsg = rawData.match(fbDtsgRegex)?.[1]
    if (!originalProfileInfor || !fbDtsg) {
      throw new Error()
    }
    const profileInfor = JSON.parse(originalProfileInfor[1])

    const id = profileInfor.id
    const fullName = profileInfor.name
    const avatar = profileInfor.profile_picture.uri
    const fbAccountData: IFacebookAccount = {
      id,
      username: fullName,
      avatar,
      cookies,
      fbDtsg
    }
    return fbAccountData
  } catch (error) {
    throw new Error(
      "Không thể lấy dữ liệu tài khoản Facebook. Đảm bảo rằng bạn đã đăng nhập vào Facebook trên trình duyệt"
    )
  }
}

const getFbIdFromUsername = async (username: string) => {
  try {
    const { data } = await fbAxiosInstance.get(
      `https://www.facebook.com/${username}`
    )
    const userId = data.match(/"userID":"(\d+)"/)[1]
    return userId as string
  } catch (error) {
    throw new Error(`Không thể lấy Facebook ID của người dùng ${username}`)
  }
}

const getStoryMedia = async (storyId: string) => {
  const data = await makeRequestToFb("8367440913325249", {
    bucketID: storyId,
    focusCommentID: null,
    scale: 1
  })

  const storiesDataString = data.match(
    /"unified_stories":\{"edges":(.*?)\},"owner":\{/
  )
  const storyOwnerIdString = data.match(
    /"__isNode":"User","id":"(.*?)","name":/
  )

  if (
    storiesDataString &&
    storiesDataString[1] &&
    storyOwnerIdString &&
    storyOwnerIdString[1]
  ) {
    const storyOwnerId = storyOwnerIdString[1]
    const storiesData: any[] = JSON.parse(storiesDataString[1])

    const stories: IFacebookStory[] = storiesData
      .map((story) => {
        const storyData = story?.node?.attachments?.[0]?.media
        if (!storyData) {
          return undefined
        }
        const id = storyData.id
        const isVideo = storyData.__isMedia === "Video"
        if (isVideo) {
          const videoDataList =
            storyData.videoDeliveryResponseFragment.videoDeliveryResponseResult
              .progressive_urls
          const hdVideoUrl = videoDataList.find(
            (videoData: any) => videoData.metadata.quality === "HD"
          )?.progressive_url
          const sdVideoUrl = videoDataList.find(
            (videoData: any) => videoData.metadata.quality === "SD"
          )?.progressive_url
          const videoThumbnailUrl =
            storyData.previewImage.uri ||
            storyData.preferred_thumbnail.image.uri
          return {
            id,
            downloadUrl: hdVideoUrl || sdVideoUrl,
            isVideo,
            thumbnailUrl: videoThumbnailUrl
          }
        }

        return {
          id,
          downloadUrl: storyData.image.uri,
          isVideo,
          thumbnailUrl: undefined
        }
      })
      .filter((story) => !!story)
    return { ownerId: storyOwnerId, stories }
  }
  throw new Error(`Không thể lấy dữ liệu story ${storyId}`)
}

const getVideoDownloadUrl = async (videoUrl: string) => {
  try {
    const { data: responseData } = await fbAxiosInstance.get(videoUrl, {
      headers: {
        Accept:
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
      }
    })
    const regex = /"progressive_urls":(.*?),"hls_playlist_urls":/
    const match = responseData.match(regex)
    if (!match) {
      throw new Error()
    }
    const videoDownloadUris = JSON.parse(match[1])
    const hdUri = videoDownloadUris.find(
      (v: any) => v.metadata.quality === "HD"
    )
    const sdUri = videoDownloadUris.find(
      (v: any) => v.metadata.quality === "SD"
    )
    return (hdUri.progressive_url || sdUri.progressive_url) as string
  } catch (error) {
    throw new Error("Đã xảy ra lỗi khi lấy link tải video")
  }
}

const getPostMedia = async (postUrl: string) => {
  try {
    const { data: rawData } = await fbAxiosInstance.get(postUrl)
    const postMediaRegex =
      /"all_subattachments":(.*?),"comet_product_tag_feed_overlay_renderer"/
    const postMediaMatch = rawData.match(postMediaRegex)
    if (!postMediaMatch) {
      throw new Error("Không thể lấy dữ liệu media của bài viết")
    }
    const postMediaData = JSON.parse(postMediaMatch[1])
    const postMedia: IFacebookPost[] = postMediaData.nodes.map(
      ({ media }: any) => {
        const isVideo = media.__isMedia === "Video"
        const id = media.id
        let downloadUrl = media.viewer_image.uri
        if (isVideo) {
          const videoDataList =
            media.video_grid_renderer.video.videoDeliveryResponseFragment
              .videoDeliveryResponseResult.progressive_urls
          const hdVideoUrl = videoDataList.find(
            (videoData: any) => videoData.metadata.quality === "HD"
          )?.progressive_url
          const sdVideoUrl = videoDataList.find(
            (videoData: any) => videoData.metadata.quality === "SD"
          )?.progressive_url
          downloadUrl = hdVideoUrl || sdVideoUrl
        }
        return {
          id,
          downloadUrl,
          isVideo
        }
      }
    )
    return postMedia
  } catch (error) {
    throw error || new Error("Đã xảy ra lỗi khi lấy dữ liệu của bài viết")
  }
}

const getFbDownloadReelUrl = async (reelUrl: string) => {
  try {
    const { data: rawData } = await fbAxiosInstance.get(reelUrl)
    const reelDataRegex = /"progressive_urls":(.*?),"hls_playlist_urls":/
    const reelDataMatch = rawData.match(reelDataRegex)
    if (!reelDataMatch) {
      throw new Error()
    }
    const reelData = JSON.parse(reelDataMatch[1])
    const hdUri = reelData.find((v: any) => v.metadata.quality === "HD")
    const sdUri = reelData.find((v: any) => v.metadata.quality === "SD")
    return (hdUri.progressive_url || sdUri.progressive_url) as string
  } catch (error) {
    throw new Error("Đã xảy ra lỗi khi lấy link tải reel")
  }
}

const facebookService = {
  makeRequestToFb,
  getFacebookAccountData,
  getFbIdFromUsername,
  getStoryMedia,
  getVideoDownloadUrl,
  getPostMedia,
  getFbDownloadReelUrl
}

export default facebookService

```

### File: src\services\instagram.service.ts
```ts
import axios from "axios"
import dayjs from "dayjs"

import { igAxiosInstance } from "src/configs/axios.config"
import { IInstagramAccount } from "src/interfaces/account.interface"
import { IMedia } from "src/interfaces/common.interface"
import {
  IIGPost,
  IIGProfile,
  IIGReel,
  IIGStory
} from "src/interfaces/instagram.interface"
import { chromeUtils } from "src/utils/chrome.util"

const getInstagramAccountData = async () => {
  try {
    const cookies = await chromeUtils.getChromeCookies("instagram.com")
    const axiosInstance = axios.create({
      baseURL: "https://www.instagram.com/",
      headers: {
        cookie: cookies,
        Accept:
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
      }
    })
    const { data: rawData } = await axiosInstance.get("/")
    const profileRegex = /\{[^{}]*"username":"[^"]*"[^{}]*\}/
    const csrfTokenRegex = /"csrf_token":"(.*?)"/
    const originalProfileInfor = rawData.match(profileRegex)
    const csrfToken = rawData.match(csrfTokenRegex)?.[1]
    if (!originalProfileInfor || !csrfToken) {
      throw new Error()
    }
    const profileInfor = JSON.parse(originalProfileInfor[0])
    const id = profileInfor.id
    const username = profileInfor.username
    const avatar = profileInfor.profile_pic_url_hd
    const instagramProfile: IInstagramAccount = {
      id,
      username,
      avatar,
      cookies,
      csrfToken
    }
    return instagramProfile
  } catch (error) {
    throw new Error(
      "Không thể lấy dữ liệu tài khoản Instagram. Đảm bảo rằng bạn đã đăng nhập vào Instagram trên trình duyệt"
    )
  }
}

const getInstagramIdAndAvatarByUsername = async (username: string) => {
  const { data } = await igAxiosInstance.get(
    `https://www.instagram.com/web/search/topsearch/?query=${username}`
  )

  const user = data?.users?.find(
    (user: any) => user?.user?.username === username
  )

  if (!user) {
    throw new Error(`Tên người dùng ${username} không tồn tại`)
  }
  return {
    id: user.user.pk as string,
    avatarUrl: user.user.profile_pic_url as string
  }
}

const getProfileStatistics = async (username: string) => {
  const { id } = await getInstagramIdAndAvatarByUsername(username)
  const { data } = await igAxiosInstance.get("/", {
    params: {
      doc_id: "8508998995859778",
      variables: JSON.stringify({
        id,
        render_surface: "PROFILE"
      })
    }
  })

  const user = data.data.user
  const profileData: IIGProfile = {
    id: user.pk || user.pk,
    username: user.username,
    full_name: user.full_name,
    avatar_url: user.hd_profile_pic_url_info.url,
    follower: user.follower_count,
    following: user.following_count,
    is_private_account: user.is_private,
    total_posts: user.media_count
  }
  return profileData
}

const getAllStoriesByHighlightId = async (highlightId: string) => {
  const { data } = await igAxiosInstance.get(
    `https://www.instagram.com/graphql/query/?query_hash=45246d3fe16ccc6577e0bd297a5db1ab&variables={"highlight_reel_ids":[${highlightId}],"reel_ids":[],"location_ids":[],"precomposed_overlay":false}`
  )
  const storiesMedia: any[] = data.data?.reels_media?.[0]?.items
  if (!storiesMedia) {
    throw new Error("Không thể lấy story từ highlight")
  }

  const result: IIGStory[] = storiesMedia.map((story) => ({
    id: story.id,
    isVideo: story.is_video,
    takenAt: story.taken_at_timestamp,
    downloadUrl: story.is_video
      ? story.video_resources[0].src
      : story.display_url
  }))

  return result
}

const getAllHighlightsIdOfUser = async (username: string) => {
  const { id: userId } = await getInstagramIdAndAvatarByUsername(username)
  const { data } = await igAxiosInstance.get("/", {
    params: {
      doc_id: "8198469583554901",
      variables: JSON.stringify({
        user_id: userId
      })
    }
  })
  const highlightsData: any[] = data.data.highlights.edges
  const allHighlightsId: string[] = highlightsData.map(
    (highlight) => highlight.node.id.split(":")[1]
  )

  return allHighlightsId
}

const getActiveStoriesByUsername = async (
  username: string
): Promise<IIGStory[]> => {
  try {
    const { id: userId } = await getInstagramIdAndAvatarByUsername(username)
    const { data: responseData } = await igAxiosInstance.get("/", {
      params: {
        query_hash: "45246d3fe16ccc6577e0bd297a5db1ab",
        variables: JSON.stringify({
          highlight_reel_ids: [],
          reel_ids: [userId],
          location_ids: [],
          precomposed_overlay: false
        })
      }
    })
    if (!responseData.data?.reels_media?.length) {
      throw new Error()
    }
    const originalStoriesData = responseData.data.reels_media[0].items
    const result: IIGStory[] = originalStoriesData.map((story: any) => ({
      id: story.id,
      takenAt: story.taken_at_timestamp,
      isVideo: story.is_video,
      downloadUrl: story.is_video
        ? story.video_resources[0].src
        : story.display_url
    }))
    return result
  } catch (error) {
    throw new Error(`Đã xảy ra lỗi khi lấy dữ liệu story của ${username}`)
  }
}

const getIgPostDataByUrl = async (postUrl: string): Promise<IIGPost> => {
  try {
    const regex =
      /"xdt_api__v1__media__shortcode__web_info":\{"items":\[(.*?)\]\}\},"extensions":/
    const { data: responseData } = await igAxiosInstance.get(postUrl)

    const match = responseData.match(regex)
    if (!match) {
      throw new Error()
    }

    const originalPostData = JSON.parse(match[1])

    const originalMediaList: any[] = Array.from(
      originalPostData.carousel_media || [originalPostData]
    )
    const videos: IMedia[] = originalMediaList
      .filter((media) => media.media_type === 2)
      .map((media) => ({
        downloadUrl: media.video_versions[0].url,
        id: media.id
      }))

    const images: IMedia[] = originalMediaList
      .filter((media) => media.media_type === 1)
      .map((media) => ({
        downloadUrl: media.image_versions2.candidates[0].url,
        id: media.id
      }))

    return {
      id: originalPostData.id,
      code: originalPostData.code,
      title: originalPostData.caption?.text,
      takenAt: dayjs
        .unix(originalPostData.taken_at)
        .format("DD/MM/YYYY HH:mm:ss"),
      totalMedia: originalMediaList.length,
      videoCount: videos.length,
      imageCount: images.length,
      likeCount: originalPostData.like_and_view_counts_disabled
        ? null
        : originalPostData.like_count,
      commentCount: originalPostData.comment_count,
      videos,
      images
    }
  } catch (error) {
    throw new Error("Đã xảy ra lỗi khi lấy dữ liệu bài viết")
  }
}

const getIgReelDataByUrl = async (reelUrl: string): Promise<IIGReel> => {
  try {
    const regex =
      /"xdt_api__v1__media__shortcode__web_info":\{"items":\[(.*?)\]\}\},"extensions":/
    const { data: responseData } = await igAxiosInstance.get(reelUrl)

    const match = responseData.match(regex)
    if (!match) {
      throw new Error()
    }

    const originalReelData = JSON.parse(match[1])

    return {
      id: originalReelData.id,
      code: originalReelData.code,
      commentCount: originalReelData.comment_count,
      takenAt: dayjs
        .unix(originalReelData.taken_at)
        .format("DD/MM/YYYY HH:mm:ss"),
      title: originalReelData.caption?.text,
      likeCount: originalReelData.like_and_view_counts_disabled
        ? null
        : originalReelData.like_count,
      downloadUrl: originalReelData.video_versions[0].url
    }
  } catch (error) {
    throw new Error("Đã xảy ra lỗi khi lấy dữ liệu reel")
  }
}

const instagramService = {
  getInstagramAccountData,
  getInstagramIdAndAvatarByUsername,
  getProfileStatistics,
  getAllStoriesByHighlightId,
  getAllHighlightsIdOfUser,
  getActiveStoriesByUsername,
  getIgPostDataByUrl,
  getIgReelDataByUrl
}

export default instagramService

```

### File: src\services\threads.service.ts
```ts
import axios from "axios"
import dayjs from "dayjs"

import { threadsAxiosInstance } from "src/configs/axios.config"
import { IThreadsAccount } from "src/interfaces/account.interface"
import { IMedia } from "src/interfaces/common.interface"
import { IThreadsPost } from "src/interfaces/threads.interface"
import { chromeUtils } from "src/utils/chrome.util"

const getThreadsAccountData = async () => {
  try {
    const cookies = await chromeUtils.getChromeCookies("threads.net")
    const axiosInstance = axios.create({
      baseURL: "https://www.threads.net/",
      headers: {
        cookie: cookies,
        Accept:
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
      }
    })
    const { data: rawData } = await axiosInstance.get("/")
    const profileRegex = /"viewer":(.*?)},/
    const igAppIdRegex = /"APP_ID":"(\d+)"/
    const originalProfileInfor = rawData.match(profileRegex)?.[1]
    const igAppId = rawData.match(igAppIdRegex)?.[1]
    if (!originalProfileInfor || !igAppId) {
      throw new Error()
    }
    const profileInfor = JSON.parse(originalProfileInfor)
    const threadsProfile: IThreadsAccount = {
      id: profileInfor.id,
      username: profileInfor.username,
      avatar: profileInfor.profile_picture_url,
      cookies,
      igAppId
    }
    return threadsProfile
  } catch (error) {
    throw new Error(
      "Không thể lấy dữ liệu tài khoản Threads. Đảm bảo rằng bạn đã đăng nhập vào Threads trên trình duyệt"
    )
  }
}

const getUserIdByUsername = async (username: string) => {
  const { data } = await threadsAxiosInstance.get(
    `https://www.threads.net/@${username}`
  )
  const userId = data.match(/"user_id":"(\d+)"/)?.[1]
  if (!userId) {
    throw new Error("Không thể lấy thông tin người dùng")
  }
  return userId as string
}

const geThreadstPostDataByUrl = async (
  postUrl: string
): Promise<IThreadsPost> => {
  try {
    const regex = /"thread_items":\[(.*?)\],"thread_type":/
    const { data: responseData } = await threadsAxiosInstance.get(postUrl)

    const match = responseData.match(regex)
    if (!match) {
      throw new Error()
    }

    const postData = JSON.parse(match[1]).post
    const haveMedia =
      postData?.carousel_media ||
      postData?.image_versions2?.candidates?.length > 0 ||
      postData?.video_versions ||
      postData?.audio
    if (!haveMedia) {
      return {
        id: postData.pk,
        code: postData.code,
        title: postData.caption?.text,
        takenAt: dayjs.unix(postData.taken_at).format("DD/MM/YYYY HH:mm:ss"),
        totalMedia: 0,
        videoCount: 0,
        imageCount: 0,
        audioCount: 0,
        likeCount: postData.like_and_view_counts_disabled
          ? null
          : postData.like_count,
        commentCount: postData.text_post_app_info.direct_reply_count,
        images: [],
        videos: [],
        audios: []
      }
    }

    const originalMediaList: any[] = Array.from(
      postData.carousel_media || [postData]
    )
    const videos: IMedia[] = originalMediaList
      .filter((media) => !!media.video_versions)
      .map((media) => ({
        id: media.id,
        downloadUrl: media.video_versions[0].url
      }))

    const images: IMedia[] = originalMediaList
      .filter((media) => !!!media.video_versions && !!media.image_versions2)
      .map((media) => ({
        id: media.id,
        downloadUrl: media.image_versions2.candidates[0].url
      }))

    const audios: IMedia[] = originalMediaList
      .filter((media) => !!media.audio)
      .map((media, index) => ({
        id: `audio_${index}`,
        downloadUrl: media.audio.audio_src
      }))

    return {
      id: postData.pk,
      code: postData.code,
      title: postData.caption?.text,
      takenAt: dayjs.unix(postData.taken_at).format("DD/MM/YYYY HH:mm:ss"),
      totalMedia: originalMediaList.length,
      videoCount: videos.length,
      imageCount: images.length,
      audioCount: audios.length,
      likeCount: postData.like_and_view_counts_disabled
        ? null
        : postData.like_count,
      commentCount: postData.text_post_app_info.direct_reply_count,
      videos,
      images,
      audios
    }
  } catch (error) {
    throw new Error(`Đã xảy ra lỗi khi lấy dữ liệu bài viết`)
  }
}

const threadsService = {
  getThreadsAccountData,
  getUserIdByUsername,
  geThreadstPostDataByUrl
}

export default threadsService

```

### File: src\services\x.service.ts
```ts
import axios from "axios"

import { xAxiosInstance } from "src/configs/axios.config"
import { ERemoteMessageType } from "src/constants/enum"
import { IXAccount } from "src/interfaces/account.interface"
import { chromeUtils } from "src/utils/chrome.util"
import { delay } from "src/utils/common.util"

const getXAccountData = async (): Promise<IXAccount> => {
  try {
    const cookies = await chromeUtils.getChromeCookies("x.com")
    const axiosInstance = axios.create({
      baseURL: "https://x.com"
    })
    const { data: rawData } = await axiosInstance.get("/")
    const idRegex = /"users":{"entities":{"(.*?)"/
    const usernameRegex = /"screen_name":"(.*?)"/
    const fullNameRegex = /"name":"(.*?)"/
    const avatarRegex = /"profile_image_url_https":"(.*?)"/
    const id = rawData.match(idRegex)?.[1]
    const fullName = rawData.match(fullNameRegex)?.[1]
    const avatar = rawData.match(avatarRegex)?.[1]
    const username = rawData.match(usernameRegex)?.[1]
    if (!fullName || !avatar || !id || !username) {
      throw new Error()
    }

    const xTab = await chromeUtils.openNewTab({ url: "https://x.com/home" })
    await delay(1000)
    if (xTab.id) {
      await chromeUtils.closeTab(xTab.id)
    }

    const xAccountData: IXAccount = {
      id,
      username,
      avatar,
      cookies,
      accessToken: "",
      csrfToken: ""
    }

    await new Promise((resolve, reject) => {
      chrome.runtime.sendMessage(
        { type: ERemoteMessageType.RETRIEVE_X_ACCOUNT_CREDENTIALS },
        (response) => {
          if (response) {
            xAccountData.accessToken = response.authorization
            xAccountData.csrfToken = response.xCsrfToken
            resolve("")
          }
          reject("")
        }
      )
    })

    return xAccountData
  } catch (error) {
    throw new Error(
      "Không thể lấy dữ liệu tài khoản X. Đảm bảo rằng bạn đã đăng nhập vào X trên trình duyệt"
    )
  }
}

const getXUserIdFromUsername = async (username: string): Promise<string> => {
  try {
    const { data: responseData } = await xAxiosInstance.get(
      "/vqu78dKcEkW-UAYLw5rriA/useFetchProfileSections_canViewExpandedProfileQuery",
      {
        params: {
          variables: JSON.stringify({ screenName: username })
        }
      }
    )
    const base64UserId = responseData.data.user_result_by_screen_name.result.id
    const userId = atob(base64UserId).split(":")[1]
    return userId
  } catch (error) {
    throw new Error(`Không thể lấy ID từ user ${username}`)
  }
}

const xService = {
  getXAccountData,
  getXUserIdFromUsername
}

export default xService

```

### File: src\store\auth.ts
```ts
import axios from "axios"
import { create } from "zustand"

import { ESocialProvider, EStorageKey } from "src/constants/enum"
import { IAccounts } from "src/interfaces/account.interface"
import facebookService from "src/services/facebook.service"
import instagramService from "src/services/instagram.service"
import threadsService from "src/services/threads.service"
import xService from "src/services/x.service"
import { chromeUtils } from "src/utils/chrome.util"

interface IAuthStore {
  accounts: IAccounts
  authenticate: (socialProvider: ESocialProvider) => Promise<void>
  logout: (socialProvider: ESocialProvider) => Promise<void>
  updateAccountData: (accountData: any) => void
}

const useAuth = create<IAuthStore>((setState, getState) => ({
  accounts: {
    [ESocialProvider.FACEBOOK]: null,
    [ESocialProvider.INSTAGRAM]: null,
    [ESocialProvider.THREADS]: null,
    [ESocialProvider.X]: null
  },

  authenticate: async <T extends ESocialProvider>(socialProvider: T) => {
    const authenticateFunction = {
      [ESocialProvider.INSTAGRAM]: instagramService.getInstagramAccountData,
      [ESocialProvider.THREADS]: threadsService.getThreadsAccountData,
      [ESocialProvider.FACEBOOK]: facebookService.getFacebookAccountData,
      [ESocialProvider.X]: xService.getXAccountData
    }
    const accountData = await authenticateFunction[socialProvider]()
    const accountsInStorage = await chromeUtils.getStorage<IAccounts>(
      EStorageKey.ACCOUNTS
    )
    await chromeUtils.setStorage(EStorageKey.ACCOUNTS, {
      ...accountsInStorage,
      [socialProvider]: accountData
    })

    const { data } = await axios.get(accountData?.avatar || "", {
      responseType: "blob"
    })
    URL.revokeObjectURL(getState().accounts[socialProvider]?.avatar || "")
    const avatarUrl = URL.createObjectURL(data)
    setState((state) => ({
      accounts: {
        ...state.accounts,
        [socialProvider]: { ...accountData, avatar: avatarUrl }
      }
    }))
  },

  updateAccountData: (newAccounts: IAccounts) => {
    setState((state) => ({
      accounts: { ...state.accounts, ...newAccounts }
    }))
  },

  logout: async <T extends ESocialProvider>(socialProvider: T) => {
    const accountsInStorage = await chromeUtils.getStorage<IAccounts>(
      EStorageKey.ACCOUNTS
    )
    delete accountsInStorage?.[socialProvider]
    await chromeUtils.setStorage(EStorageKey.ACCOUNTS, accountsInStorage)
    URL.revokeObjectURL(getState().accounts[socialProvider]?.avatar || "")
    setState((state) => ({
      accounts: {
        ...state.accounts,
        [socialProvider]: null
      }
    }))
  }
}))

export default useAuth

```

### File: src\store\download-process.ts
```ts
import { create } from "zustand"

import { ESocialProvider } from "src/constants/enum"
import { IDownloadProcess } from "src/interfaces/download-process.interface"

interface IDownloadProcessState {
  [ESocialProvider.FACEBOOK]: IDownloadProcess[ESocialProvider.FACEBOOK][]
  [ESocialProvider.INSTAGRAM]: IDownloadProcess[ESocialProvider.INSTAGRAM][]
  [ESocialProvider.THREADS]: IDownloadProcess[ESocialProvider.THREADS][]
  [ESocialProvider.X]: IDownloadProcess[ESocialProvider.X][]
}

interface IDownloadProcessStore {
  downloadProcesses: IDownloadProcessState
  addProcess: <T extends ESocialProvider>(
    socialName: T,
    newProcess: IDownloadProcess[T]
  ) => void
  removeProcess: (socialName: ESocialProvider, processId: string) => void
  updateProcess: <T extends ESocialProvider>(
    socialName: T,
    processId: string,
    payload: Partial<IDownloadProcess[T]>
  ) => void
  getDownloadProcessBySocial: <T extends ESocialProvider>(
    socialName: T
  ) => IDownloadProcess[T][]
}

const useDownloadProcesses = create<IDownloadProcessStore>((set, getState) => ({
  downloadProcesses: {
    [ESocialProvider.FACEBOOK]: [],
    [ESocialProvider.INSTAGRAM]: [],
    [ESocialProvider.THREADS]: [],
    [ESocialProvider.X]: []
  },
  addProcess: (socialName, newProcess) => {
    set((state) => ({
      downloadProcesses: {
        ...state.downloadProcesses,
        [socialName]: [...state.downloadProcesses[socialName], newProcess]
      }
    }))
  },
  removeProcess: (socialName, processId) => {
    set((state) => ({
      downloadProcesses: {
        ...state.downloadProcesses,
        [socialName]: state.downloadProcesses[socialName].filter(
          (process) => process.id !== processId
        )
      }
    }))
  },
  updateProcess: (socialName, processId, payload) => {
    set((state) => ({
      downloadProcesses: {
        ...state.downloadProcesses,
        [socialName]: state.downloadProcesses[socialName].map((process) =>
          process.id === processId ? { ...process, ...payload } : process
        )
      }
    }))
  },
  getDownloadProcessBySocial: (socialName) => {
    return getState().downloadProcesses[
      socialName
    ] as IDownloadProcess[typeof socialName][]
  }
}))

export default useDownloadProcesses

```

### File: src\utils\chrome.util.ts
```ts
const getChromeCookies = async (domain: string): Promise<string> => {
  return new Promise((resolve, reject) => {
    chrome.cookies.getAll({ domain }, function (cookies) {
      if (cookies.length > 0) {
        let cookieList = cookies
          .map((cookie) => `${cookie.name}=${cookie.value}`)
          .join(";")
        resolve(cookieList)
      } else {
        reject("Không tìm thấy cookie")
      }
    })
  })
}

const openNewTab = async (options: chrome.tabs.CreateProperties) => {
  const tab = await chrome.tabs.create(options)
  return tab
}

const closeTab = async (tabId: number): Promise<void> => {
  await chrome.tabs.remove(tabId)
}

const getStorage = async <T>(key: string): Promise<T | null> => {
  return new Promise((resolve) => {
    chrome.storage.local.get(key, function (result) {
      resolve(result[key])
    })
  })
}

const setStorage = async <T>(key: string, value: T): Promise<void> => {
  return new Promise((resolve) => {
    chrome.storage.local.set({ [key]: value }, function () {
      resolve()
    })
  })
}

const removeStorage = async (key: string): Promise<void> => {
  return new Promise((resolve) => {
    chrome.storage.local.remove(key, function () {
      resolve()
    })
  })
}

const downloadFile = async (
  options: chrome.downloads.DownloadOptions,
  waitUntilCompleted: boolean = true
) => {
  return new Promise(async (resolve, reject) => {
    chrome.downloads.download(options, (downloadId) => {
      if (chrome.runtime.lastError) {
        return reject(chrome.runtime.lastError)
      }
      if (!waitUntilCompleted) {
        return resolve("Tải xuống bắt đầu")
      } else {
        chrome.downloads.onChanged.addListener(
          function onDownloadChanged(downloadDelta) {
            if (downloadDelta.id === downloadId && downloadDelta.state) {
              if (downloadDelta.state.current === "complete") {
                resolve("Tải xuống hoàn tất")
                chrome.downloads.onChanged.removeListener(onDownloadChanged)
              } else if (downloadDelta.state.current === "interrupted") {
                reject("Tải xuống bị gián đoạn")
                chrome.downloads.onChanged.removeListener(onDownloadChanged)
              }
            }
          }
        )
      }
    })
  })
}

export const chromeUtils = {
  getChromeCookies,
  getStorage,
  setStorage,
  removeStorage,
  downloadFile,
  openNewTab,
  closeTab
}

```

### File: src\utils\common.util.ts
```ts
import { format } from "@fast-csv/format"
import clsx, { ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

import { ESocialProvider } from "src/constants/enum"
import useDownloadProcesses from "src/store/download-process"
import { chromeUtils } from "src/utils/chrome.util"

export const delay = (ms: number) =>
  new Promise((resolve) => setTimeout(resolve, ms))

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export const downloadByBatch = async (
  data: any[],
  downloadFunction: any,
  batchSize: number = 1,
  onDownloadBatchCompleted?: (batchIndex: number) => void | Promise<void>
) => {
  for (let i = 0; i < data.length; i += batchSize) {
    const from = i
    const to = Math.min(i + batchSize, data.length)
    const sliceData = data.slice(from, to)
    await Promise.all(
      sliceData.map((item: any, index: number) =>
        downloadFunction(item, from + index + 1)
      )
    )
    if (onDownloadBatchCompleted) {
      await onDownloadBatchCompleted(to)
    }
  }
}

export const createCsvContentFromData = async <T extends object>(data: T[]) => {
  if (data.length === 0) return ""

  return new Promise<string>((resolve) => {
    const csvStream = format({ headers: true })
    let csvContent = ""

    csvStream
      .on("data", (chunk) => {
        csvContent += chunk.toString()
      })
      .on("end", () => {
        resolve(csvContent)
      })

    data.forEach((row) => csvStream.write(row))
    csvStream.end()
  })
}

export const downloadStatisticCsvFile = async <T extends object>(
  data: T[],
  filename: string
) => {
  const csvContent = await createCsvContentFromData(data)
  const blob = new Blob([csvContent], { type: "text/csv" })
  const url = URL.createObjectURL(blob)
  await chromeUtils.downloadFile({ url, filename })
  URL.revokeObjectURL(url)
}

export const extractIdFromUrl = (url: string, regexPattern: RegExp) => {
  const match = url.match(regexPattern)
  if (!match) {
    throw new Error("URL không hợp lệ")
  }
  return match[1]
}

export const isDownloadProcessExist = (
  socialName: ESocialProvider,
  processId: string
) => {
  const { getDownloadProcessBySocial } = useDownloadProcesses.getState()
  const downloadProcess = getDownloadProcessBySocial(socialName)
  const isProcessExist = downloadProcess.some(
    (process) => process.id === processId
  )
  return isProcessExist
}

```

### File: src\utils\facebook.util.ts
```ts
import { fbAxiosInstance } from "src/configs/axios.config"
import { EDownloadSeperateType } from "src/constants/enum"
import { URL_PATTERN } from "src/constants/regex"
import { DOWNLOAD_STORIES_IN_HIGHLIGHT_BATCH_SIZE } from "src/constants/variables"
import { IFacebookStory } from "src/interfaces/facebook.interface"
import facebookService from "src/services/facebook.service"
import { chromeUtils } from "src/utils/chrome.util"
import { downloadByBatch, extractIdFromUrl } from "src/utils/common.util"

export const downloadFbPostMedia = async (postUrl: string) => {
  try {
    const { data: rawData } = await fbAxiosInstance.get(postUrl)
    const temp = JSON.parse(
      rawData.match(
        /"all_subattachments":(.*?),"comet_product_tag_feed_overlay_renderer"/
      )?.[1]
    )
    const mediaSetToken = rawData.match(/"mediaset_token":"(.*?)"/)?.[1]
    if (!temp || !mediaSetToken) {
      throw new Error()
    }
    const totalPostMedia = temp.count
    const firstMediaId = temp.nodes[0].media.id
    let totalDownloadedItems = 0
    let cursor = firstMediaId
    const baseQuery = {
      isMediaset: true,
      renderLocation: "comet_media_viewer",
      mediasetToken: mediaSetToken,
      scale: 1,
      feedLocation: "COMET_MEDIA_VIEWER"
    }
    const docID = "9478994358856279"

    while (totalDownloadedItems < totalPostMedia) {
      const query = { ...baseQuery, nodeID: cursor }
      const responseData = await facebookService.makeRequestToFb(docID, query)
      const mediaData = JSON.parse(responseData?.split("\n")?.[0])?.data
        ?.mediaset?.currMedia?.edges?.[0]?.node
      if (!mediaData) {
        continue
      }
      const isVideo = mediaData.__isMedia === "Video"
      let downloadUrl = ""
      if (isVideo) {
        const videoData =
          mediaData.videoDeliveryResponseFragment.videoDeliveryResponseResult
            .progressive_urls
        const hdUrl = videoData.find(
          (item: any) => item.metadata.quality === "HD"
        )
        const sdUrl = videoData.find(
          (item: any) => item.metadata.quality === "SD"
        )
        downloadUrl = hdUrl.progressive_url || sdUrl.progressive_url
      } else {
        downloadUrl = mediaData.image.uri
      }

      await chromeUtils.downloadFile({
        url: downloadUrl,
        filename: `fb_post/${totalDownloadedItems + 1}.${
          isVideo ? "mp4" : "jpg"
        }`
      })

      const nextMediaData = JSON.parse(
        responseData.match(/"nextMediaAfterNodeId":(.*?)\},"extensions":/)?.[1]
      )
      cursor = nextMediaData?.id
      totalDownloadedItems += 1
    }
  } catch (error) {
    console.log("Đã xảy ra lỗi khi lấy dữ liệu của bài viết:", error)
    throw new Error("Đã xảy ra lỗi khi lấy dữ liệu của bài viết")
  }
}

export const downloadFbStoryMedia = async (storyUrl: string) => {
  const storyId = extractIdFromUrl(
    storyUrl,
    URL_PATTERN[EDownloadSeperateType.FACEBOOK_STORY]
  )

  const { stories } = await facebookService.getStoryMedia(storyId)
  await downloadByBatch(
    stories,
    async (storyMedia: IFacebookStory, index: number) => {
      await chromeUtils.downloadFile({
        url: storyMedia.downloadUrl,
        filename: `fb_story_${storyId}/${index}.${storyMedia.isVideo ? "mp4" : "jpg"}`
      })
    },
    DOWNLOAD_STORIES_IN_HIGHLIGHT_BATCH_SIZE
  )
}

export const downloadFbVideo = async (videoUrl: string) => {
  const videoId = extractIdFromUrl(
    videoUrl,
    URL_PATTERN[EDownloadSeperateType.FACEBOOK_VIDEO]
  )
  const downloadUrl = await facebookService.getVideoDownloadUrl(videoUrl)
  await chromeUtils.downloadFile({
    url: downloadUrl,
    filename: `fb_video_${videoId}.mp4`
  })
}

export const downloadFbReel = async (reelUrl: string) => {
  const reelId = extractIdFromUrl(
    reelUrl,
    URL_PATTERN[EDownloadSeperateType.FACEBOOK_REEL]
  )
  const reelDownloadUrl = await facebookService.getFbDownloadReelUrl(reelUrl)
  await chromeUtils.downloadFile({
    url: reelDownloadUrl,
    filename: `fb_reel_${reelId}.mp4`
  })
}

export const downloadFbCommentVideo = async (commentUrl: string) => {
  try {
    const commentId = new URL(commentUrl).searchParams.get("comment_id")
    if (!commentId) {
      throw new Error()
    }
    const { data: rawData } = await fbAxiosInstance.get(commentUrl)
    const videoDataRegex = /"progressive_urls":(.*?),"hls_playlist_urls":/
    const videoDataMatch = rawData.match(videoDataRegex)
    if (!videoDataMatch) {
      throw new Error()
    }

    const videoData = JSON.parse(videoDataMatch[1])

    const hdVideo = videoData.find((v: any) => v.metadata.quality === "HD")
    const sdVideo = videoData.find((v: any) => v.metadata.quality === "SD")
    const downloadUrl = hdVideo.progressive_url || sdVideo.progressive_url
    await chromeUtils.downloadFile({
      url: downloadUrl,
      filename: `fb_comment_video_${commentId}.mp4`
    })
  } catch (error) {
    console.log(
      "Đã xảy ra lỗi khi lấy dữ liệu của video trong bình luận:",
      error
    )
    throw new Error("Đã xảy ra lỗi khi lấy dữ liệu của video trong bình luận")
  }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
