import os, re

RBXPath = os.getenv("LOCALAPPDATA") + "\\Roblox\\logs"

def find_rizz(directory):
    if not os.path.isdir(directory):
        raise ValueError(f"{directory} is not valid directory")

    files = [os.path.join(directory, file) for file in os.listdir(directory)]

    files = [file for file in files if os.path.isfile(file)]

    if not files:
        return None

    gyat = max(files, key=os.path.getmtime)

    return gyat

def get_rizz_level(file_path, pattern):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    file.close()

    matches = re.findall(pattern, content)
    return matches

def GetRenderViewFromLog():
    latest_sigma_i_found = find_rizz(RBXPath)
    if latest_sigma_i_found:
        try:
            skibidi = r"SurfaceController\[_:1\]::initialize view\((.*?)\)"
            sigmas_remaining = get_rizz_level(latest_sigma_i_found, skibidi)
            if sigmas_remaining:
                for sigma_remained in sigmas_remaining:
                    RenderView = int(sigma_remained, 16)
                    print("[~] RenderView: " + hex(RenderView))
                    return RenderView
        except FileNotFoundError:
            return 0
        except Exception as e:
            return 0
