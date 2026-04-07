---
title: "Offline-First & High-Performance POS (React & Virtuoso)"
description: "Kiến trúc cho ứng dụng Điểm Bán Hàng (Point of Sale) chạy trên Web Cloud ưu tiên Offline-First, kết hợp List Virtualization để đảm bảo thao tác mượt mà dưới môi trường thiết bị thu ngân yếu tải."
tags: ["react", "pos", "offline-first", "virtuoso", "localstorage", "ui-optimization"]
related_projects: ["Tiem_Nuoc_Nho_v5"]
---

# Web POS Kiến trúc Offline-First & High Performance UI

Khác với các Single Page Applications (SPA) truyền thống, phần mềm POS phải đối mặt với đặc thù cực đoan:
- Truyền tải danh sách hàng trăm (thậm chí hàng ngàn) danh mục món ăn và đơn hàng.
- Web trên máy tính quán cà phê thường yếu, môi trường Internet trồi sụt.
- Khách hàng không thể đứng chờ Loading API để thanh toán.

Để đáp ứng được điều này, hệ thống áp dụng chiến lược thiết kế "Offline-First" và "DOM Virtualization".

## 1. Local Caching & Sync Queue (Offline-First)

Thay vì trực tiếp chờ phản hồi từ REST API (Data Source of Truth), ứng dụng thực hiện Optimistic UI cập nhật (cập nhật giao diện trước, background-sync sau) và lấy LocalStorage/IDB làm Database tức thời.

### Cơ chế hoạt động trong Provider (`DataContext.tsx`):
- **Store Local:** Ngay khi mở App, hệ thống sẽ chắp ghép State từ dữ liệu cũ lưu trong `localStorage`: `rawMenuItems`, `orders_data`. Góp phần giảm TTFP (Time to First Paint) xuống dưới 1s bằng Cache.
- **Fetch Ngầm (Stale-While-Revalidate):** Một Hook `fetchAllData` âm thầm chọc lên Google Apps Script, đem dữ liệu chuẩn trên Cloud đè lại State nếu có sự khác biệt (so sánh Hash JSON).
- **Cart Context lưu trữ:** 
  Dữ liệu giỏ hàng (Cart) trong phiên phục vụ chưa thanh toán cũng được serialize vào RAM và LocalStorage để nếu nhân viên tải lại trang/cúp điện đột ngột hoặc rớt mạng không bị mất bill khách đang chờ.

## 2. List Virtualization (Giữ DOM luôn nhẹ)

Khi cửa hàng có menu lên tới 300 thức uống + Topping, một vòng lặp `Array.map` sẽ sinh ra hàng nghìn DOM Node chồng chéo đẩy CPU trình duyệt chạy 100%.

**Sử dụng Thư Viện: `react-virtuoso`**
- App thay thế hoàn toàn lưới CSS Grid/Flexbox thông thường bằng Virtual Grid.
- Hệ thống chỉ "Vẽ" (Render vào DOM) 12 - 20 Item đang lọt vào khung hình Camera của cửa sổ cuộn trình duyệt.
- Những Item trôi lên trên/xuống dưới khu vực nhìn thấy sẽ bị Unmount hoàn toàn và tái chế thẻ `<div>` tái sử dụng, giúp máy pos Celeron yếu đuối cũng có thể lướt danh sách siêu cường.

```typescript
// Mẫu sử dụng VirtuosoGrid cho Menu
import { VirtuosoGrid } from 'react-virtuoso';

<VirtuosoGrid
  style={{ height: '100%', width: '100%' }}
  data={filteredMenuItems}
  components={{
    List: React.forwardRef((props, ref) => (
      <div {...props} ref={ref} className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-3" />
    )),
    Item: ({ children, ...props }) => (
      <div {...props} className="w-full h-full flex flex-col">{children}</div>
    )
  }}
  itemContent={(index, item) => (
    <MenuItemCard key={item.id} item={item} onSelect={...} />
  )}
/>
```

## 3. Tích hợp thanh toán linh hoạt bằng VietQR
Tích hợp thẳng thư viện sinh QR Code động từ SDK (`vietnam-qr-pay`). 
QR chỉ là kết quả của việc ghép Text format (Số tài khoản + Ngân Hàng + Số Tiền + Nội dung hóa đơn) rồi vẽ thành SVG/Canvas, không nhất thiết phụ thuộc internet external API như Napas API nếu đã nắm thuật toán quy chuẩn tạo chuỗi VietQR tĩnh. Cực kỳ tối ưu không cần backend server đứng giữa generate QR.
