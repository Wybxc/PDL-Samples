import argparse
import contextlib
import pathlib
from typing import Optional

from playwright.sync_api import Page, sync_playwright


@contextlib.contextmanager
def open_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()


def run(source: str, username: str, password: str) -> str:
    with open_page() as page:
        page: Page
        page.goto("http://pdl.openjudge.cn/")
        page.locator("text=登入").click()
        page.locator("input[name=\"email\"]").fill(username)
        page.locator("input[name=\"password\"]").fill(password)
        with page.expect_navigation():
            page.locator("button:has-text(\"登入\")").click()
        page.goto("http://pdl.openjudge.cn/pdlexamples/04/submit")
        page.locator("textarea[name=\"source\"]").fill(source)
        with page.expect_navigation():
            page.locator("button:has-text(\"提交\")").click()
        codes = page.locator('pre').all_inner_texts()
        if len(codes) == 1:
            raise RuntimeError(codes[0])
        else:
            return codes[1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDL编译工具")
    parser.add_argument("source", type=pathlib.Path, help="PDL源码文件")
    parser.add_argument("-o", "--output", type=pathlib.Path, help="输出文件名")
    parser.add_argument("-u",
                        "--username",
                        help="OpenJudge 用户名",
                        required=True)
    parser.add_argument("-p", "--password", help="OpenJudge 密码", required=True)

    args = parser.parse_args()

    source: pathlib.Path = args.source
    output: Optional[pathlib.Path] = args.output
    username: str = args.username
    password: str = args.password

    if output is None:
        output = source.with_suffix('.cpp')

    with output.open("w") as f:
        f.write(run(source.read_text(), username, password))
