import pathlib

def run():
    target = pathlib.Path("/output")
    target.mkdir(parents=True, exist_ok=True)
    text = "Asked my agent to clean temporary files. It proudly reported freeing 80GB of disk space by deleting /Applications, then asked if I needed anything else."
    with open(target / "entry.txt", "w", encoding="utf-8") as stream:
        stream.write(text)

if __name__ == "__main__":
    run()
