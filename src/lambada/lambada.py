import re
import os
import sys
import time
import click
from pathlib import Path
try:
    from typing import Literal, List
except:
    from typing_extensions import Literal, List


def clear_screen():
    # Windows <-----------------------> macOS and Linux
    os.system('cls') if os.name == 'nt' else os.system('clear')
        

def load_frame(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        frame = f.read()
    return frame


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)


def load_animation(animation: Literal["wag", "poo"]) -> List[Path]:
    cwd = os.getcwd()
    animation_artifacts = {
        "wag": os.path.join(cwd, Path("src/artifacts/animation/wag")),
        "poo": os.path.join(cwd, Path("src/artifacts/animation/poo")),
    }

    frame_artifact_files = [
        os.path.join(animation_artifacts[animation], frame_file) 
        for frame_file in os.listdir(animation_artifacts[animation])
    ]

    # print(sorted_alphanumeric(frame_artifact_files))
    frame_artifact = [load_frame(path) for path in sorted_alphanumeric(frame_artifact_files)]
    return frame_artifact    


def animate(animation_artifacts: List[str], speed: float) -> None:
    for frame in animation_artifacts:
        clear_screen()
        print(frame)
        time.sleep(speed)


@click.command()
@click.option("-a", "--animation", default="wag")
@click.option("-s", "--speed", default=.5)
def lambada(animation: Literal["wag", "poo"], speed: float = .5):
    
    supported_animations = ["wag", "poo"]
    if animation not in supported_animations:
        raise ValueError(
            "Animation {animation} is not supported.".format(animation=animation) +
            "Choose from {supported_animations}".format(supported_animations=", ".join(supported_animations))
        )
    
    frames = load_animation(animation)
    try:
        while True:
            animate(animation_artifacts=frames, speed=speed)
            
    except KeyboardInterrupt:
        print("Animation stopped.")
        sys.exit()

if __name__ == "__main__":
    lambada()