import datetime
import platform
import sys


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Xin chào từ Google Antigravity IDE!")
    print(f"- Thời gian chạy : {now}")
    print(f"- Hệ điều hành   : {platform.system()} {platform.release()}")
    print(f"- Phiên bản Python: {platform.python_version()}")


if __name__ == "__main__":
    main()
