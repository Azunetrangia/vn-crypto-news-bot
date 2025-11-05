# 💾 Data Directory

Thư mục này chứa các file JSON để lưu trữ dữ liệu của bot.

**Lưu ý:** Thư mục này sẽ được tạo tự động khi bot chạy lần đầu.

---

## 📁 Files

### 📋 news_config.json
**Mục đích:** Lưu cấu hình nguồn tin tức

**Structure:**
```json
{
  "messari_channel": 1234567890,
  "santiment_channel": 1234567891,
  "rss_feeds": [
    {
      "name": "Tin Vĩ Mô ABC",
      "url": "https://example.com/rss.xml",
      "channel_id": 1234567892
    }
  ]
}
```

**Fields:**
- `messari_channel`: ID kênh cho tin Messari (null nếu chưa cài)
- `santiment_channel`: ID kênh cho tin Santiment (null nếu chưa cài)
- `rss_feeds`: Array các RSS feed đã thêm
  - `name`: Tên hiển thị
  - `url`: URL của RSS feed
  - `channel_id`: ID kênh đăng tin

---

### 🔖 last_post_ids.json
**Mục đích:** Tracking các bài viết đã đăng (chống trùng lặp)

**Structure:**
```json
{
  "messari": ["id1", "id2", "id3"],
  "santiment": ["id1", "id2"],
  "rss": {
    "https://example.com/rss.xml": ["id1", "id2"]
  }
}
```

**Fields:**
- `messari`: Array chứa IDs của tin Messari đã đăng
- `santiment`: Array chứa IDs của tin Santiment đã đăng
- `rss`: Object với keys = RSS URLs, values = arrays IDs

**Limit:** Mỗi array giữ tối đa 100 IDs để tránh file quá lớn.

---

### 🔔 alerts.json
**Mục đích:** Lưu các cảnh báo giá đang hoạt động

**Structure:**
```json
[
  {
    "user_id": 123456789,
    "ticker": "bitcoin",
    "ticker_display": "BTC",
    "target_price": 69000.0,
    "channel_id": 987654321,
    "created_at": "2025-01-01T12:00:00"
  }
]
```

**Fields:**
- `user_id`: Discord user ID (người đặt alert)
- `ticker`: CoinGecko coin ID (ví dụ: "bitcoin")
- `ticker_display`: Ticker hiển thị (ví dụ: "BTC")
- `target_price`: Giá mục tiêu (USD)
- `channel_id`: ID kênh nhận thông báo
- `created_at`: Thời gian tạo (ISO format)

---

### 📊 chart_*.png (Temporary)
**Mục đích:** Các biểu đồ giá được tạo tự động

**Format:** `chart_{coin_id}.png`

**Lifecycle:**
1. Tạo khi alert trigger
2. Gửi vào Discord
3. Tự động xóa sau khi gửi

**Size:** ~100-200 KB mỗi chart

---

## 🔄 Data Flow

### News Flow:
```
Bot Start
    ↓
Load news_config.json
    ↓
Load last_post_ids.json
    ↓
Every 10 minutes:
    Fetch new articles
    Check against last_post_ids
    Post new ones
    Update last_post_ids
    Save to disk
```

### Alerts Flow:
```
Bot Start
    ↓
Load alerts.json
    ↓
Every 60 seconds:
    Fetch prices for all tickers
    Check against target prices
    If triggered:
        Generate chart
        Send notification
        Remove from alerts
        Save alerts.json
```

---

## 🔒 File Permissions

**Recommended permissions (Linux/Mac):**
```bash
chmod 600 *.json  # Read/write for owner only
```

**Windows:** No special action needed

---

## 💾 Backup Strategy

**Recommended:**
```bash
# Daily backup
cp data/*.json backups/$(date +%Y%m%d)/

# Keep 7 days of backups
find backups/ -mtime +7 -delete
```

**What to backup:**
- ✅ news_config.json (cấu hình quan trọng)
- ✅ alerts.json (cảnh báo đang hoạt động)
- ⚠️ last_post_ids.json (có thể tái tạo, nhưng nên backup)
- ❌ chart_*.png (tạm thời, không cần backup)

---

## 🛠️ Maintenance

### Clean up old data:
```bash
# Reset last post IDs (sẽ có thể post lại tin cũ)
echo '{"messari": [], "santiment": [], "rss": {}}' > data/last_post_ids.json

# Clear all alerts
echo '[]' > data/alerts.json

# Delete old charts
rm data/chart_*.png
```

### Check file sizes:
```bash
ls -lh data/
```

### Validate JSON:
```bash
# Using jq
jq . data/news_config.json
jq . data/last_post_ids.json
jq . data/alerts.json
```

---

## 🐛 Troubleshooting

### File không tồn tại
```bash
# Tạo thủ công
mkdir -p data
echo '{"messari_channel": null, "santiment_channel": null, "rss_feeds": []}' > data/news_config.json
echo '{"messari": [], "santiment": [], "rss": {}}' > data/last_post_ids.json
echo '[]' > data/alerts.json
```

### File bị corrupt
```bash
# Kiểm tra với jq
jq . data/alerts.json

# Nếu lỗi, backup và reset
cp data/alerts.json data/alerts.json.corrupt
echo '[]' > data/alerts.json
```

### File quá lớn
```bash
# Kiểm tra size
du -h data/*.json

# Nếu last_post_ids.json > 1MB
# Code đã tự động giới hạn 100 IDs
# Nhưng có thể reset thủ công nếu cần
```

---

## 📊 Statistics

**Expected sizes:**
- news_config.json: ~500 bytes - 5 KB
- last_post_ids.json: ~1-10 KB
- alerts.json: ~100 bytes per alert
- chart_*.png: ~100-200 KB (temporary)

**Growth rate:**
- news_config.json: Slow (chỉ khi thêm RSS)
- last_post_ids.json: Stable (limited to 100 IDs)
- alerts.json: Linear (depends on users)

---

## 🔐 Security

**Important:**
- ❌ Không commit folder `data/` vào Git
- ✅ File `.gitignore` đã exclude `data/*.png`
- ✅ JSON files chỉ chứa IDs, không có secrets
- ✅ User IDs là public info trên Discord

**File permissions:**
- Owner: read + write
- Group: none
- Others: none

---

## 📚 Learn More

- JSON Format: https://www.json.org/
- Data persistence: https://realpython.com/python-json/
- File I/O: https://docs.python.org/3/tutorial/inputoutput.html
