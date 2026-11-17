import shutil
import subprocess
import sys


def check_tool(name: str, args: list[str]) -> tuple[bool, str]:
    exe = shutil.which(name)
    if not exe:
        return False, "Chưa cài đặt hoặc chưa thêm vào PATH"
    try:
        result = subprocess.run(
            [exe, *args],
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        output = (result.stdout or result.stderr).strip().splitlines()[0]
        return True, output
    except Exception as exc:
        return False, f"Lỗi khi kiểm tra: {exc}"


def main() -> None:
    # Đảm bảo hiển thị tiếng Việt có dấu trên Windows Terminal
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 55)
    print("  KIỂM TRA MÔI TRƯỜNG LẬP TRÌNH AI (WINDOWS)")
    print("=" * 55)

    checks = [
        ("Python", "python", ["--version"]),
        ("pip", "pip", ["--version"]),
        ("Node.js", "node", ["-v"]),
        ("npm", "npm", ["-v"]),
        ("Git", "git", ["--version"]),
    ]

    all_ok = True
    for label, cmd, args in checks:
        ok, info = check_tool(cmd, args)
        status = "[OK]  " if ok else "[THIẾU]"
        if not ok:
            all_ok = False
        print(f"{status} {label:<10}: {info}")

    print("=" * 55)
    if all_ok:
        print("Tất cả công cụ đã sẵn sàng để lập trình AI và đẩy code lên GitHub!")
    else:
        print("Một số công cụ chưa sẵn sàng. Hãy hoàn tất cài đặt các mục [THIẾU].")


if __name__ == "__main__":
    main()
