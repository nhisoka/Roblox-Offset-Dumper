import os, re

RBXPath = os.getenv("LOCALAPPDATA") + "\\Roblox\\logs"

def find_latest_modified_file(directory):
    if not os.path.isdir(directory):
        raise ValueError(f"{directory} ist kein gültiges Verzeichnis")

    files = [os.path.join(directory, file) for file in os.listdir(directory)]

    files = [file for file in files if os.path.isfile(file)]

    if not files:
        return None

    latest_file = max(files, key=os.path.getmtime)

    return latest_file

def extract_data_from_file(file_path, pattern):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    file.close()

    matches = re.findall(pattern, content)
    return matches

def GetRenderViewFromLog():
    latest_file = find_latest_modified_file(RBXPath)
    if latest_file:
        try:
            pattern = r"SurfaceController\[_:1\]::initialize view\((.*?)\)"
            matches = extract_data_from_file(latest_file, pattern)
            if matches:
                for match in matches:
                    RenderView = int(match, 16)
                    print("[~] RenderView: " + hex(RenderView))
                    return RenderView
        except FileNotFoundError:
            return 0
        except Exception as e:
            return 0