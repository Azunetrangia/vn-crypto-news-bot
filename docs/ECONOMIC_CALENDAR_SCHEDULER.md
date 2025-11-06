# Economic Calendar Dynamic Scheduler

## Overview

Hệ thống scheduler mới thay thế polling approach cũ (check mỗi 5 phút) bằng **dynamic scheduled tasks** - schedule chính xác từng event để post vào đúng thời gian.

## Architecture

### 1. Main Scheduler Task (`economic_calendar_scheduler`)

- **Chạy**: Mỗi ngày lúc **00:00 UTC+7** (midnight Vietnam time)
- **Nhiệm vụ**:
  1. Reset tracking và cancel tất cả scheduled tasks cũ
  2. Fetch tất cả economic events trong ngày từ Investing.com
  3. Tạo dynamic tasks cho mỗi event (chỉ Medium/High impact)
  4. Schedule pre-alert và actual value checks

### 2. Pre-Alert System

- **Thời điểm**: Event time - 5 minutes
- **Nội dung**: Post thông báo sắp diễn ra với status ⏰ **Sắp diễn ra**
- **Ví dụ**: Event BoE Interest Rate lúc 19:00 → Pre-alert lúc 18:55

### 3. Actual Value Check System

Mỗi event có **3 lần check** actual value:

1. **T+0** (Đúng giờ event): Check ngay khi event xảy ra
2. **T+5** (5 phút sau): Retry nếu actual value chưa có
3. **T+10** (10 phút sau): Retry lần cuối

**Chỉ post khi actual value tồn tại** (không phải "N/A")

### 4. Status Indicators

- ⏰ **Sắp diễn ra**: Pre-alert (5 minutes trước)
- ✅ **Đã công bố**: Actual value có sẵn
- ⏳ **Pending**: Actual value chưa có (hiển thị trong embeds nhưng không post riêng)

## Data Structures

### `self.scheduled_events`

Dictionary tracking trạng thái của mỗi event:

```python
{
    'event_id_123': {
        'pre_alert_posted': False,  # Đã post pre-alert chưa?
        'actual_posted': False,     # Đã post actual value chưa?
        'event': {...}               # Event data
    }
}
```

### `self.event_tasks`

List các asyncio tasks đang chạy:

```python
[
    <Task _schedule_pre_alert(event1, 18:55)>,
    <Task _schedule_actual_check(event1, 19:00)>,
    <Task _schedule_actual_check(event1, 19:05)>,
    ...
]
```

## Methods

### `economic_calendar_scheduler()`

Main loop chạy mỗi 24 giờ:

1. Cancel tất cả tasks cũ
2. Reset tracking
3. Fetch events
4. Schedule tasks mới

### `_schedule_pre_alert(event, pre_alert_time)`

- Wait đến `pre_alert_time`
- Check xem đã post chưa (tránh duplicate)
- Post pre-alert vào tất cả guilds có config
- Mark `pre_alert_posted = True`

### `_schedule_actual_check(event, check_time, is_first)`

- Wait đến `check_time`
- Check xem đã post actual chưa
- Re-fetch event để lấy actual value mới nhất
- Nếu actual tồn tại → Post và mark `actual_posted = True`
- Nếu không có → Skip (sẽ retry ở lần check tiếp theo)

## Commands

### `!schedulenow`

**Admin only** - Trigger scheduler ngay lập tức (for testing)

```
!schedulenow
```

**Output**:
```
🗓️ Triggering Economic Calendar Scheduler...
📊 Found 60 events, scheduling tasks...
✅ Scheduled 180 tasks for 15 events!
```

### `!testcalendar`

**Admin only** - Show full calendar cho ngày hôm nay (không schedule)

```
!testcalendar
```

## Example Flow

### Event: BoE Interest Rate Decision at 19:00

1. **00:00** - Scheduler fetch event, tạo tasks:
   - Pre-alert task: 18:55
   - Actual check tasks: 19:00, 19:05, 19:10

2. **18:55** - Pre-alert task execute:
   - Post "⏰ Sắp diễn ra - BoE Interest Rate"
   - Mark `pre_alert_posted = True`

3. **19:00** - First actual check:
   - Fetch updated event
   - Actual = "N/A" → Skip
   - Print "⏳ No actual value yet, will retry"

4. **19:05** - Second actual check:
   - Fetch updated event
   - Actual = "5.25%" → Post!
   - Mark `actual_posted = True`
   - Color-code vs previous value

5. **19:10** - Third check:
   - `actual_posted = True` → Skip (đã post rồi)

## Impact Filtering

Chỉ schedule và post **Medium** và **High** impact events.

**Low** impact events bị skip hoàn toàn.

## Timezone

All times sử dụng **UTC+7** (Asia/Ho_Chi_Minh)

Investing.com data ở UTC-5 → convert sang UTC+7 khi parse.

## Tracking & Duplicate Prevention

- `scheduled_events` dictionary ngăn post duplicate
- Reset mỗi ngày lúc 00:00
- Check trước khi post:
  - Pre-alert: Check `pre_alert_posted`
  - Actual: Check `actual_posted`

## Error Handling

- Try/catch trong mỗi scheduled task
- Task cancel an toàn khi scheduler reset
- Print detailed logs cho debugging
- Traceback cho mọi exceptions

## Advantages vs Old Polling System

| Feature | Old (Polling) | New (Scheduled) |
|---------|---------------|-----------------|
| **Timing** | 0-5 min delay | Exact time |
| **CPU Usage** | Constant checking | Only at event time |
| **Accuracy** | ~5 min window | ±1 second |
| **Scalability** | Poor (check all) | Good (per-event) |
| **Complexity** | Simple | Moderate |

## Testing

1. **Start scheduler immediately**:
   ```
   !schedulenow
   ```

2. **Check logs**:
   ```bash
   tail -f bot.log | grep -i "schedule\|alert\|actual"
   ```

3. **Expected output**:
   ```
   🗓️ Economic Calendar Scheduler starting at 2025-01-06 20:43:51
   📊 Fetched 60 events for scheduling
     ⏰ Scheduled pre-alert for S&P Global US Services PMI at 16:35
     📊 Scheduled actual check for S&P Global US Services PMI at 16:40
     ...
   ✅ Scheduled 180 tasks for today's events
   ```

## Future Improvements

- [ ] Add retry với exponential backoff
- [ ] Webhook notifications cho admins khi event post
- [ ] Dashboard tracking event post success rate
- [ ] Custom impact filters per guild
- [ ] Event reminder system (15/30 min trước)

## Code References

- **Scheduler Task**: `cogs/news_cog.py` lines 2130-2224
- **Pre-Alert**: `cogs/news_cog.py` lines 2238-2272
- **Actual Check**: `cogs/news_cog.py` lines 2274-2333
- **Command**: `cogs/news_cog.py` lines 2460-2544
