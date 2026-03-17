#!/usr/bin/env python3
"""
EPT Week 1 – Scripting (HW1)
Creates a pentesting engagement folder structure in the current working directory.

AndrewID: afrocha
Student: Ariana Rocha
Due Date: 18MAR2026
Github Repo: https://github.com/afro-chai/EPT_HW1_Scripting.git
"""

from pathlib import Path
import sys


# Required folder structure (relative paths from CWD)
FOLDER_STRUCTURE = [
    "Documentation/Customer Info",
    "Documentation/Reports",
    "Findings/External",
    "Findings/Internal",
    "Findings/Phishing",
    "Data/Database",
    "Data/Phishing/Templates",
    "Data/Phishing/Payloads",
    "Data/Network Mapping/External/Nmap",
    "Data/Network Mapping/External/Eyewitness",
    "Data/Network Mapping/Internal/Nmap",
    "Data/Network Mapping/Internal/Eyewitness",
    "Data/Penetration Test",
    "Data/Vulnerability Scanning/External/Nessus",
    "Data/Vulnerability Scanning/Internal/Nessus",
    "Data/Web App/Burp",
    "Data/Web App/Nikto",
]


def create_directories(base_path: Path, relative_paths: list[str], dry_run: bool = False) -> list[Path]:
    """Create directories under base_path. Returns list of created paths."""
    created = []
    for rel in relative_paths:
        full = base_path / rel
        if dry_run:
            print(f"  [dry-run] would create: {full}")
            created.append(full)
            continue
        try:
            full.mkdir(parents=True, exist_ok=True)
            created.append(full)
            print(f"  created: {rel}")
        except OSError as e:
            print(f"  error creating {rel}: {e}", file=sys.stderr)
    return created


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Create pentest engagement folder structure.")
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=None,
        help="Base directory (default: current working directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print folders that would be created without creating them",
    )
    args = parser.parse_args()

    base = args.base_dir if args.base_dir is not None else Path.cwd()
    if not base.is_dir() and not args.dry_run:
        base.mkdir(parents=True, exist_ok=True)

    print(f"Base directory: {base.resolve()}")
    if args.dry_run:
        print("Dry run – no directories will be created.")
    create_directories(base, FOLDER_STRUCTURE, dry_run=args.dry_run)
    print("Done.")


if __name__ == "__main__":
    main()
