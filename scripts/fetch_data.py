import subprocess
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_RAW.mkdir(parents=True, exist_ok=True)

def msg(s):
    print(textwrap.dedent(s).strip())

def clone_or_update(repo_url: str, dest_dir: Path):
    if dest_dir.exists() and (dest_dir / ".git").exists():
        msg(f"\n[KeystrokeMouse-TZ] Updating existing repo at: {dest_dir}")
        subprocess.run(["git", "-C", str(dest_dir), "pull", "--ff-only"], check=False)
    elif dest_dir.exists() and not any(dest_dir.iterdir()):
        msg(f"\n[KeystrokeMouse-TZ] Empty dir found, cloning into: {dest_dir}")
        subprocess.run(["git", "clone", repo_url, str(dest_dir)], check=True)
    elif not dest_dir.exists():
        msg(f"\n[KeystrokeMouse-TZ] Cloning into: {dest_dir}")
        subprocess.run(["git", "clone", repo_url, str(dest_dir)], check=True)
    else:
        msg(f"\n[KeystrokeMouse-TZ] Destination exists but is not a git repo.\n"
            f"Move it aside and re-run if you want a clean clone:\n  {dest_dir}")

def ensure_dirs():
    for p in [
        DATA_RAW / "keystrokemouse_tz",
        DATA_RAW / "cmu_keystroke",
        DATA_RAW / "dfl_mouse",
    ]:
        p.mkdir(parents=True, exist_ok=True)

def fetch_keystrokemouse_tz():
    repo = "https://github.com/ztn-iplab/banking_CA.git"
    dest = DATA_RAW / "keystrokemouse_tz"
    clone_or_update(repo, dest)

def instructions_manual_datasets():
    msg("""
    [Manual Action Required]

    1) CMU Keystroke Dynamics – Benchmark Data Set
       URL: https://www.cs.cmu.edu/~keystroke/
       Place files under: data/raw/cmu_keystroke/

    2) DFL Mouse Dynamics Data Set
       URL: https://www.ms.sapientia.ro/~manyi/DFL.html
       Place files under: data/raw/dfl_mouse/

    This repo does not redistribute third-party data.
    """)

def main():
    ensure_dirs()
    try:
        fetch_keystrokemouse_tz()
    except FileNotFoundError:
        msg("[WARN] 'git' not found in PATH. Install Git or download the repo manually.")
    except subprocess.CalledProcessError as e:
        msg(f"[WARN] Could not clone/update KeystrokeMouse-TZ automatically: {e}")
    instructions_manual_datasets()
    msg("\nDone. Check data/raw/")

if __name__ == "__main__":
    main()
