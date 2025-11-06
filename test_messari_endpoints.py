#!/usr/bin/env python3
"""Test các Messari endpoints khác nhau"""

import os
import asyncio
import aiohttp
from dotenv import load_dotenv

load_dotenv()

async def test_endpoint(endpoint_name, url, api_key):
    """Test một endpoint của Messari"""
    try:
        async with aiohttp.ClientSession() as session:
            headers = {'x-messari-api-key': api_key}
            
            print(f"\n📡 Testing: {endpoint_name}")
            print(f"   URL: {url}")
            
            async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
                print(f"   Status: {response.status}")
                
                if response.status == 200:
                    data = await response.json()
                    print(f"   ✅ Success!")
                    
                    # Hiển thị structure
                    if isinstance(data, dict):
                        print(f"   Keys: {list(data.keys())}")
                        
                        if 'data' in data:
                            data_content = data['data']
                            if isinstance(data_content, list) and len(data_content) > 0:
                                print(f"   Found {len(data_content)} items")
                                print(f"   First item keys: {list(data_content[0].keys())}")
                                
                                # Hiển thị item đầu tiên
                                item = data_content[0]
                                print(f"\n   📰 First item:")
                                for key in ['title', 'name', 'slug', 'id', 'url', 'published_at', 'content']:
                                    if key in item:
                                        value = str(item[key])[:100]
                                        print(f"      - {key}: {value}")
                            elif isinstance(data_content, dict):
                                print(f"   Data keys: {list(data_content.keys())}")
                    
                    return True
                elif response.status == 401:
                    text = await response.text()
                    if "Enterprise" in text or "gated" in text:
                        print(f"   ❌ Requires Enterprise plan")
                    else:
                        print(f"   ❌ Auth error: {text[:150]}")
                    return False
                else:
                    text = await response.text()
                    print(f"   ❌ Error {response.status}: {text[:150]}")
                    return False
                    
    except asyncio.TimeoutError:
        print(f"   ⏱️ Timeout")
        return False
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False

async def main():
    api_key = os.getenv('MESSARI_API_KEY')
    
    if not api_key:
        print("❌ MESSARI_API_KEY not found in .env")
        return
    
    print("=" * 70)
    print("🔍 TESTING MESSARI API ENDPOINTS")
    print("=" * 70)
    print(f"API Key: {api_key[:10]}...")
    
    # Danh sách endpoints để test
    endpoints = [
        ("News (trả phí)", "https://data.messari.io/api/v1/news"),
        ("Assets", "https://data.messari.io/api/v2/assets"),
        ("Assets with metrics", "https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd"),
        ("Markets", "https://data.messari.io/api/v1/markets"),
        ("All Assets", "https://data.messari.io/api/v2/assets?fields=id,slug,symbol,name"),
    ]
    
    results = {}
    for name, url in endpoints:
        results[name] = await test_endpoint(name, url, api_key)
        await asyncio.sleep(0.5)  # Rate limiting
    
    # Summary
    print("\n" + "=" * 70)
    print("📋 SUMMARY:")
    for name, success in results.items():
        status = "✅ OK" if success else "❌ FAILED"
        print(f"   {status:12} {name}")
    print("=" * 70)

if __name__ == '__main__':
    asyncio.run(main())
