"""
Launcher for the Teaching Internship Portfolio Django site.

Runs Django in-process (no external Python/pipenv required) and opens the
site in the default web browser. This is the entry point PyInstaller freezes
into portfolio.exe -- Django itself is bundled inside the .exe, so the
target machine needs nothing installed.
"""
import os
import sys
import threading
import time
import urllib.request
import webbrowser

HOST = "127.0.0.1"
PORT = "8000"
URL = f"http://{HOST}:{PORT}/"


def server_already_running():
    try:
        urllib.request.urlopen(URL, timeout=1)
        return True
    except Exception:
        return False


def open_browser_when_ready(timeout=25):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if server_already_running():
            webbrowser.open(URL)
            return
        time.sleep(0.5)
    print(f"Server did not respond after startup; opening {URL} anyway.")
    webbrowser.open(URL)


def main():
    if getattr(sys, "frozen", False):
        # Running as portfolio.exe -- data (db.sqlite3) lives beside it.
        os.chdir(os.path.dirname(os.path.abspath(sys.executable)))

    print("Teaching Internship Portfolio")

    if server_already_running():
        print(f"Already running at {URL} -- opening browser.")
        webbrowser.open(URL)
        return

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internship_portfolio.settings")

    import django
    django.setup()
    from django.core.management import call_command, execute_from_command_line

    try:
        call_command("migrate", verbosity=0, interactive=False)
    except Exception as exc:
        print(f"Warning: could not run migrations ({exc}); continuing with existing database.")

    print(f"Starting server at {URL}")
    print("Close this window (or press Ctrl+C) to stop it.")
    print()

    threading.Thread(target=open_browser_when_ready, daemon=True).start()

    try:
        execute_from_command_line(
            [sys.argv[0], "runserver", f"{HOST}:{PORT}", "--noreload", "--skip-checks"]
        )
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
