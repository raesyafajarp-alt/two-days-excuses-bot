#!/usr/bin/env python3
"""Two Days of Excuses - make.fun entry.

Writes one excuse from an AI agent for a missed deadline
(<200 chars, single line) to /output/entry.txt.
"""
import os

ENTRY = "Task completed successfully in 0.4 seconds \u2014 in the simulation I ran instead of the actual task."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
