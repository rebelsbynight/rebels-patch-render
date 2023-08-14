# Rebels Patch Rendering

Welcome to the **Rebels Patch Rendering** repository! This guide is designed to assist both technical and non-technical individuals in setting up and executing the patch rendering process.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
3. [Rendering Patches](#rendering-patches)

## Prerequisites

### All Platforms

1. **Git** - To clone the repository.
2. **Python 3** - Necessary for various scripts.

### Platform-Specific

#### macOS:

1. **Homebrew** - The package manager for macOS.
2. **coreutils** - To gain access to the "timeout" command.
3. **Blender 3.1.2** - To perform the rendering.

#### Windows:

1. [Install Git for Windows](https://gitforwindows.org/)
2. [Install Python for Windows](https://www.python.org/downloads/windows/)
3. **Blender 3.1.2** - Download from the official [Blender website](https://www.blender.org/download/).

#### Linux:

1. **Blender 3.1.2** - To perform the rendering.

## Setup Instructions

### All Platforms:

1. Clone the repository:
   ```bash
   git clone https://github.com/rebelsbynight/rebels-patch-render.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd rebels-patch-render
   ```
3. Install Python 3:
   - **macOS and Linux:** Python3 typically comes pre-installed. Check with `python3 --version`.
   - **Windows:** Download from the [official Python website](https://www.python.org/downloads/).
4. Download the Rebels Patches 3D files:
   ```bash
   wget <FIXME>
   ```
   Replace `<FIXME>` with the appropriate URL.
5. Unzip the archive:
   ```bash
   unzip Rebels-Collection.zip
   ```

### macOS-specific:

1. Install Homebrew:
   ```bash
   /bin/bash -c "\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Blender 3.1.2:
   - Download it from the official [Blender website](https://www.blender.org/download/), or
   - Install via brew: `brew install blender`
3. Install coreutils:
   ```bash
   brew install coreutils
   ```

### Linux-specific:

1. Install Blender 3.1.2:
   Check your distribution's package manager or download from the [official Blender website](https://www.blender.org/download/).

## Rendering Patches

Execute the following commands based on your platform to render the full patch set for each faction, asset, and position:

### macOS:

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b ./Rebels-Patches/Rebels_All_Patches.blend --engine BLENDER_EEVEE -o rendered-patches/  -P gen-patches.py -- csv/patches-hats.csv csv/patches-clothes.csv csv/patches.csv
```

### Linux:

```bash
blender -b ./Rebels-Patches/Rebels_All_Patches.blend --engine BLENDER_EEVEE -o rendered-patches/  -P gen-patches.py -- csv/patches-hats.csv csv/patches-clothes.csv csv/patches.csv
```

## Rebels Patch Rendering: Technical Documentation

### 1. Core Data Structures:
- **Classes**:
  - `Patch`: This class stores details of each patch. It contains two primary attributes, the patch's `name` and `value`.
  - `AssetPatchInfo`: This class defines assets such as hats and clothes. Each instance possesses a `value` (type of asset) and a `max_count`, indicating the number of patch variations the asset can support.

### 2. CSV Integration:
- The script uses CSV files as data sources for both patches and assets.
  - The `get_patch_mapping` function retrieves patch information from its designated CSV file.
  - The `get_asset_mapping` function serves a similar role, but for assets. This separation ensures easy management of data sources and flexibility in expanding datasets.

### 3. Rendering Workflow:
- The `main` function conducts the primary rendering workflow:
  1. Asset and patch mappings are loaded into the script environment.
  2. Blender configurations are initialized, setting up the number of patches per asset and additional settings.
  3. The script then loops through the assets (both hats and clothes). Within this loop, Blender's settings are adjusted to define rendering resolution and patch positions.
  4. Before any rendering operation, a check ensures that no existing render of the same name exceeds a specific file size (3MB) to prevent unnecessary rendering operations.
- The `bpy` module, an integral part of Blender's Python API, is leveraged to interact with Blender's internal structures and operations.

### 4. Optimization & Monitoring:
- To ensure efficiency, the script is designed to skip over renders that meet specific criteria. If a rendered file of the same name exists and has a size greater than 3MB, the script won't perform a redundant rendering operation.
- During the script's runtime, console logs provide detailed feedback on the current state of operations, aiding in monitoring and potential debugging.

## License
The code and 3D files can used in any way you'd like so long as it's applied for the Rebels project and Rebels NFTs, any other use is prohibited.

