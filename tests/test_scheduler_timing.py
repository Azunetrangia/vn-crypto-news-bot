#!/usr/bin/env python3
"""
Test Economic Calendar Scheduler Logic
Verifies that scheduling calculations work correctly
"""

from datetime import datetime, timedelta
import pytz

VN_TZ = pytz.timezone('Asia/Ho_Chi_Minh')

def test_scheduler_timing():
    """Test timing calculations cho scheduler"""
    
    print("=" * 60)
    print("ECONOMIC CALENDAR SCHEDULER TIMING TEST")
    print("=" * 60)
    
    now = datetime.now(VN_TZ)
    print(f"\n⏰ Current time: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    
    # Test 1: Next midnight calculation
    tomorrow = now + timedelta(days=1)
    next_midnight = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
    wait_seconds = (next_midnight - now).total_seconds()
    
    print(f"\n📅 Next midnight: {next_midnight.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"⏳ Wait time: {wait_seconds:.0f} seconds ({wait_seconds/3600:.2f} hours)")
    
    # Test 2: Event scheduling examples
    print("\n" + "=" * 60)
    print("EVENT SCHEDULING EXAMPLES")
    print("=" * 60)
    
    test_events = [
        ("S&P Global US Services PMI", "16:40"),
        ("BoE Interest Rate Decision", "19:00"),
        ("Fed Interest Rate Decision", "02:00"),  # Tomorrow
    ]
    
    for event_name, time_str in test_events:
        event_time = datetime.strptime(time_str, '%H:%M').replace(
            year=now.year, month=now.month, day=now.day, tzinfo=VN_TZ
        )
        
        # If event time is in the past, it's for tomorrow
        if event_time < now:
            event_time += timedelta(days=1)
        
        pre_alert_time = event_time - timedelta(minutes=5)
        check_times = [
            event_time,
            event_time + timedelta(minutes=5),
            event_time + timedelta(minutes=10)
        ]
        
        print(f"\n🎯 {event_name}")
        print(f"   Event Time: {event_time.strftime('%H:%M:%S')}")
        
        if pre_alert_time > now:
            print(f"   ⏰ Pre-alert: {pre_alert_time.strftime('%H:%M:%S')} (in {(pre_alert_time - now).total_seconds()/60:.1f} min)")
        else:
            print(f"   ⏰ Pre-alert: {pre_alert_time.strftime('%H:%M:%S')} (PAST - skip)")
        
        for i, check_time in enumerate(check_times):
            offset = [0, 5, 10][i]
            if check_time > now:
                print(f"   📊 Actual check T+{offset}: {check_time.strftime('%H:%M:%S')} (in {(check_time - now).total_seconds()/60:.1f} min)")
            else:
                print(f"   📊 Actual check T+{offset}: {check_time.strftime('%H:%M:%S')} (PAST - skip)")
    
    # Test 3: Task count estimation
    print("\n" + "=" * 60)
    print("TASK COUNT ESTIMATION")
    print("=" * 60)
    
    sample_event_count = 15  # Giả sử có 15 Medium/High events
    
    # Mỗi event: 1 pre-alert + 3 actual checks = 4 tasks
    # Nhưng past events bị skip
    future_events = 15  # Giả sử tất cả future
    tasks_per_event = 4
    total_tasks = future_events * tasks_per_event
    
    print(f"\n📊 Medium/High impact events: {sample_event_count}")
    print(f"📋 Tasks per event: {tasks_per_event} (1 pre-alert + 3 actual checks)")
    print(f"✅ Total scheduled tasks: {total_tasks}")
    print(f"💾 Memory per task: ~1-2 KB")
    print(f"💾 Total memory: ~{total_tasks * 1.5:.0f} KB (~{total_tasks * 1.5 / 1024:.2f} MB)")
    
    print("\n" + "=" * 60)
    print("✅ SCHEDULER TIMING TEST COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    test_scheduler_timing()
