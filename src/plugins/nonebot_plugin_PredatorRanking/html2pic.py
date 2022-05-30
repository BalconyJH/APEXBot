import os.path
import webbrowser

import jinja2
from pathlib import Path
import random
from playwright.async_api import Page, Browser, async_playwright, Error
import asyncio

from .get_info import *


async def render(data):
    data = data

    pc_foundrank_rp, pc_val_rp, ps4_foundrank_rp, ps4_val_rp, x1_foundrank_rp, x1_val_rp, switch_foundrank_rp, switch_val_rp, pc_totalMastersAndPreds_rp, ps4_totalMastersAndPreds_rp, x1_totalMastersAndPreds_rp, switch_totalMastersAndPreds_rp = await rp_data(data)
    pc_foundrank_ap, pc_val_ap, ps4_foundrank_ap, ps4_val_ap, x1_foundrank_ap, x1_val_ap, switch_foundrank_ap, switch_val_ap, pc_totalMastersAndPreds_ap, ps4_totalMastersAndPreds_ap, x1_totalMastersAndPreds_ap, switch_totalMastersAndPreds_ap = await ap_data(data)

    # 格式化输出
    if pc_foundrank_rp == -1:
        pc_foundrank_rp = "未排名"

    if ps4_foundrank_rp == -1:
        ps4_foundrank_rp = "未排名"
    
    if x1_foundrank_rp == -1:
        x1_foundrank_rp = "未排名"

    if switch_foundrank_rp == -1:
        switch_foundrank_rp = "未排名"

    if pc_foundrank_ap == -1:
        pc_foundrank_ap = "未排名"

    if ps4_foundrank_ap == -1:
        ps4_foundrank_ap = "未排名"
    
    if x1_foundrank_ap == -1:
        x1_foundrank_ap = "未排名"

    if switch_foundrank_ap == -1:
        switch_foundrank_ap = "未排名"

    TEMPLATES_PATH = str(Path(__file__).parent / "templates")
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
        enable_async=True,
    )

    template = env.get_template('rank.html')
    element = {
        'pc_foundrank_rp': pc_foundrank_rp,
        'pc_val_rp': pc_val_rp,
        'ps4_foundrank_rp': ps4_foundrank_rp,
        'ps4_val_rp': ps4_val_rp,
        'x1_foundrank_rp': x1_foundrank_rp,
        'x1_val_rp': x1_val_rp,
        'switch_foundrank_rp': switch_foundrank_rp,
        'switch_val_rp': switch_val_rp,
        'pc_foundrank_ap': pc_foundrank_ap,
        'pc_val_ap': pc_val_ap,
        'ps4_foundrank_ap': ps4_foundrank_ap,
        'ps4_val_ap': ps4_val_ap,
        'x1_foundrank_ap': x1_foundrank_ap,
        'x1_val_ap': x1_val_ap,
        'switch_foundrank_ap': switch_foundrank_ap,
        'switch_val_ap': switch_val_ap,
        'pc_totalMastersAndPreds_rp': pc_totalMastersAndPreds_rp,
        'ps4_totalMastersAndPreds_rp': ps4_totalMastersAndPreds_rp,
        'x1_totalMastersAndPreds_rp': x1_totalMastersAndPreds_rp,
        'switch_totalMastersAndPreds_rp': switch_totalMastersAndPreds_rp,
        'pc_totalMastersAndPreds_ap': pc_totalMastersAndPreds_ap,
        'ps4_totalMastersAndPreds_ap': ps4_totalMastersAndPreds_ap,
        'x1_totalMastersAndPreds_ap': x1_totalMastersAndPreds_ap,
        'switch_totalMastersAndPreds_ap': switch_totalMastersAndPreds_ap,
    }
    html = await template.render_async(element)
    return html

async def htmltopic(path):
    fullpath = path
    async with async_playwright() as p:
        browser_type = p.chromium
        browser = await browser_type.launch()
        page = await browser.new_page(viewport={"width": 1000, "height": 700})
        await page.goto('file:///' + os.path.abspath(fullpath))
        img = await page.screenshot(full_page=True)
        await page.close()
    return img