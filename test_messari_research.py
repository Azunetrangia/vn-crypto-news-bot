#!/usr/bin/env python3
"""Test Messari research endpoints"""

import os
import asyncio
import aiohttp
from dotenv import load_dotenv

load_dotenv()

async def test_messari_research():
    api_key = os.getenv('MESSARI_API_KEY')
    
    print("=" * 70)
    print("🔍 TESTING MESSARI RESEARCH/REPORTS")
    print("=" * 70)
    
    # Thử các endpoint research khác nhau
    endpoints = [
        "https://data.messari.io/api/v1/news",
        "https://data.messari.io/api/v2/news", 
        "https://data.messari.io/api/v1/reports",
        "https://data.messari.io/api/v2/reports",
        "https://messari.io/api/news",
        "https://messari.io/api/v1/news",
    ]
    
    async with aiohttp.ClientSession() as session:
        for url in endpoints:
            try:
                headers = {'x-messari-api-key': api_key}
                print(f"\n📡 Testing: {url}")
                
                async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=5)) as response:
                    print(f"   Status: {response.status}")
                    
                    if response.status == 200:
                        data = await response.json()
                        print(f"   ✅ Success! Keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}")
                    elif response.status == 401:
                        text = await response.text()
                        if "Enterprise" in text:
                            print(f"   ❌ Enterprise only")
                        else:
                            print(f"   ❌ Auth failed")
                    elif response.status == 404:
                        print(f"   ❌ Not found")
                    else:
                        print(f"   ❌ Error: {response.status}")
                        
            except asyncio.TimeoutError:
                print(f"   ⏱️ Timeout")
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            await asyncio.sleep(0.3)

asyncio.run(test_messari_research())
