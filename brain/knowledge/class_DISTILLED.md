---
id: Class
type: knowledge
owner: OA_Triage
---
# Class
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# 🚀 Dự án Hệ thống Docker

## 📌 Giới thiệu

**Dự án Hệ thống Docker** là một dự án thực tiễn được thiết kế để minh họa

cách xây dựng, quản lý và triển khai ứng dụng bằng **Docker** và

kiến trúc hệ thống container.

Dự án này giúp AE hiểu: - Các nguyên tắc cơ bản của Docker -

Vòng đời của container - Cấu hình Dockerfile - Điều phối Docker Compose
- Mạng dịch vụ - Cấu hình môi trường - Quy trình triển khai cơ bản

------------------------------------------------------------------------

## ⚙️ Các công nghệ được sử dụng

- 🐳 Docker
- 🐳 Docker Compose
- Các công nghệ đang ứng dụng trong các hệ thống

------------------------------------------------------------------------

## 🔧 Cài đặt & Thiết lập

### 1️⃣ Sao chép kho lưu trữ

``` bash
git clone https://github.com/fdhhhdjd/Class_Docker_Systems.git
cd Class_Docker_Systems
```

### 2️⃣ Xây dựng container Docker

``` bash
docker-compose build
```

### 3️⃣ Chạy hệ thống

``` bash
docker-compose up -d
```

### 4️⃣ Dừng hệ thống

``` bash
docker-compose down
```

------------------------------------------------------------------------

## 🌐 Truy cập ứng dụng

Sau khi chạy thành công:

- Ứng dụng: http://localhost:PORT

- Cơ sở dữ liệu: Được cấu hình trong docker-compose.yml

(Thay đổi PORT theo cấu hình của bạn)

------------------------------------------------------------------------

## 📚 Mục tiêu học tập

Thông qua dự án này, AE sẽ học được:

- Cách xây dựng ảnh Docker
- Cách các container giao tiếp
- Cách hoạt động của volume
- Cách quản lý biến môi trường
- Cách triển khai ứng dụng đa dịch vụ

------------------------------------------------------------------------

## 🧪 Các lệnh Docker thông dụng

``` bash
docker ps
docker images
docker logs <container_name>
docker exec -it <container_name> sh
docker-compose down -v

```

------------------------------------------------------------------------

## 🛠️ Khắc phục sự cố

Nếu bạn gặp sự cố:

- Đảm bảo Docker đã được cài đặt: `docker --version`
- Kiểm tra các container đang chạy: `docker ps`
- Kiểm tra nhật ký: `docker logs <container_name>`
- Xây dựng lại container: `docker-compose up --build`

------------------------------------------------------------------------

## 📈 Cải tiến trong tương lai

- Tích hợp CI/CD
- Cấu hình triển khai sản xuất
- Thiết lập proxy ngược
- Cấu hình SSL
- Giám sát (Prometheus, Grafana)


⭐ Nếu dự án này hữu ích với bạn, hãy tặng sao nhé!

------------------------------------------------------------------------
## 📚 Dạy Học Online

Bên cạnh tài liệu miễn phí, mình còn mở các khóa học online:

- **Lập trình web cơ bản → nâng cao**
- **Ứng dụng về AI và Automation**
- **Kỹ năng phỏng vấn & xây CV IT**

### Thông Tin Đăng Ký

- 🌐 Website: [https://codewebkhongkho.com](https://codewebkhongkho.com/portfolios)
- 📧 Email: nguyentientai10@gmail.com
- 📞 Zalo/Hotline: 0798805741

---

## 💖 Donate Ủng Hộ

Nếu bạn thấy các source hữu ích và muốn mình tiếp tục phát triển nội dung miễn phí, hãy ủng hộ mình bằng cách donate.  
Mình sẽ sử dụng kinh phí cho:

- 🌐 Server, domain, hosting
- 🛠️ Công cụ bản quyền (IDE, plugin…)
- 🎓 Học bổng, quà tặng cho cộng đồng

### QR Code Ngân Hàng

Quét QR để ủng hộ nhanh:

<img src="https://res.cloudinary.com/ecommerce2021/image/upload/v1760680573/abbank_yjbpat.jpg" alt="QR Code ABBank" width="300">


**QR Code ABBank**  
- Chủ tài khoản: Nguyễn Tiến Tài  
- Ngân hàng: NGAN HANG TMCP AN BINH  
- Số tài khoản: 1651002972052

---

## 📞 Liên Hệ

- 📚 Facebook Dạy Học: [Code Web Không Khó](https://www.facebook.com/codewebkhongkho)
- 📚 Tiktok Dạy Học: [@code.web.khng.kh](https://www.tiktok.com/@code.web.khng.kh)
- 💻 GitHub: [fdhhhdjd](https://github.com/fdhhhdjd)
- 📧 Email: [nguyentientai10@gmail.com](mailto:nguyentientai10@gmail.com)

Cảm ơn bạn đã quan tâm & chúc bạn học tập hiệu quả! Have a nice day <3!!

```

### File: DOCKER.md
```md
# Learn Docker

## 1. DOWNLOAD docker ubuntu
```bash
    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    apt-cache policy docker-ce
    sudo systemctl status docker
    sudo usermod -aG docker ${USER}
    su - ${USER}
    sudo snap install docker
    sudo apt install docker-compose
    # restart computer is yet 

    # Download Makefile
    sudo apt install make 
```

## 2. Hello Docker
```bash
    docker build -t hello-docker .
    docker run hello-docker
```

## 3. React Docker
```bash
    docker image build -t react-docker . && docker run react-docker
    docker run -p 5173:5173 react-docker
    docker container prune
    docker compose up -d --build
```

## 4. Restarted Docker

```bash 
    sudo systemctl restart docker.socket docker.service
    # Move image
    sudo docker image rm -f $(sudo docker image ls -q)
```

## 5. Used image
```
    docker pull nguyentientai/class_fullstack:node-docker-taidev
    docker run -d -p 5000:5004 --name my_container nguyentientai/class_fullstack:node-docker-taidev
```

## 6. Check port and kill 
```
    sudo apt update
    sudo apt install net-tools
    sudo ss -tuln | grep :<port>
    sudo netstat -tuln | grep :<port>
    sudo kill <ID>
    sudo fuser -k 81/tcp
```


```

