#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:18:21 2020

@author: jack
"""


import asyncio 
if asyncio.get_event_loop().is_running (): # Only patch if needed (i.e. running in Notebook, Spyder, etc) 
    import nest_asyncio
    nest_asyncio.apply()
import time

async def Func1():
    current_time = time.time
    print(f"Current time is {current_time}")

async def Func2():
    print("Two")
    
async def Func3():
    print("Three")

async def main():
    REALOP_queue = asyncio.Queue()
    
    work = [await Func1(), await Func2(), await Func3()]
    
    for work in work:
        await REALOP_queue.put(work)
    
    while True:
        if REALOP_queue.empty():
            await REALOP_queue.put(await Func1())
        
        await REALOP_queue.get()
            

if __name__ == "__main__":
    asyncio.run(main())