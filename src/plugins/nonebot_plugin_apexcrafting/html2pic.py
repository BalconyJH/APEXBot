import os.path
import jinja2
from pathlib import Path
from playwright.async_api import Page, Browser, async_playwright, Error
import time
from .get_info import *


async def render(data):
    data = data
    timeRemain1 = await time_Remain1(data)
    dailycrafting1img = await dailycrafting1_img(data)
    dailycrafting2img = await dailycrafting2_img(data)
    dailycrafting1name = await dailycrafting1_name(data)
    dailycrafting2name = await dailycrafting2_name(data)
    dailycrafting1cost = await dailycrafting1_cost(data)
    dailycrafting2cost = await dailycrafting2_cost(data)
    timeRemain2 = await time_Remain2(data)
    weeklycrafting1img = await weeklycrafting1_img(data)
    weeklycrafting2img = await weeklycrafting2_img(data)
    weeklycrafting1name = await weeklycrafting1_name(data)
    weeklycrafting2name = await weeklycrafting2_name(data)
    weeklycrafting1cost = await weeklycrafting1_cost(data)
    weeklycrafting2cost = await weeklycrafting2_cost(data)

    localtime = int(time.time())
    n1 = timeRemain1 - localtime - 3600
    timeRemain1 = time.strftime("%H:%M:%S", time.gmtime(n1))

    n2 = timeRemain2 - localtime - 3600
    timeRemain2 = time.strftime("%d天%H:%M:%S", time.gmtime(n2))

    TEMPLATES_PATH = str(Path(__file__).parent / "templates")
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
        enable_async=True,
    )
    template = env.get_template('crafting.html')  # 获取一个模板文件
    element = {
        'timeRemain1':timeRemain1,
        'daily_crafting_img1':dailycrafting1img,
        'daily_crafting_img2':dailycrafting2img,
        'daily_crafting_text1': dailycrafting1name,
        'daily_crafting_text2': dailycrafting2name,
        'daily_crafting_cost1': dailycrafting1cost,
        'daily_crafting_cost2': dailycrafting2cost,
        'timeRemain2':timeRemain2,
        'weekly_crafting_img1': weeklycrafting1img,
        'weekly_crafting_img2': weeklycrafting2img,
        'weekly_crafting_text1': weeklycrafting1name,
        'weekly_crafting_text2': weeklycrafting2name,
        'weekly_crafting_cost1': weeklycrafting1cost,
        'weekly_crafting_cost2': weeklycrafting2cost,
    }

    test = await template.render_async(element)
    return test

async def htmltopic(path):
    fullpath = path
    async with async_playwright() as p:
        browser_type = p.chromium
        browser = await browser_type.launch()
        page = await browser.new_page(viewport={"width": 450, "height": 550})
        await page.goto('file:///' + os.path.abspath(fullpath))
        img = await page.screenshot(full_page=True)
        await page.close()

    return img
