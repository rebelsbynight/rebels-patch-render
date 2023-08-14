import json
import bpy
import random
import sys
import csv
from os import path

class Patch:
    def __init__(self, patch_name, patch_value):
        self.name = patch_name
        self.value = patch_value

class AssetPatchInfo:
    def __init__(self, value, max_count):
        self.max_count = max_count
        self.value = value

def get_patch_mapping(patch_mapping_filepath):
    res = {}
    with open(patch_mapping_filepath, newline='') as csvfile:
        r = csv.reader(csvfile, dialect='excel')
        header = next(r)
        for row in r:
            faction_name = row[0].strip()
            faction_patch_id = row[1].strip()
            patch_name = row[2].strip()
            value = row[3].strip()
            tmp = {}

            if faction_name not in res:
                res[faction_name] = {}

            res[faction_name][faction_patch_id] = Patch(patch_name, value)

    return res


def get_asset_mapping(hats_mapping_filepath):
    res = {}
    with open(hats_mapping_filepath, newline='') as csvfile:
        r = csv.reader(csvfile, dialect='excel')
        header = next(r)
        header = next(r)
        for row in r:
            asset_name = row[0].strip()
            value = row[1].strip()
            max_count = row[2].strip()
            tmp = {}

            if asset_name not in res:
                res[asset_name] = {}
            res[asset_name] = AssetPatchInfo(value, max_count)

    return res


def main():
    hats_mapping = {}
    clothes_mapping = {}
    patch_mapping = {}

    script_args = sys.argv[sys.argv.index("--") + 1:]
    hats_mapping_path = script_args[0]
    clothes_mapping_path = script_args[1]
    patch_mapping_path = script_args[2]

    with open(patch_mapping_path) as f:
        patch_mapping = get_patch_mapping(patch_mapping_path)
    with open(hats_mapping_path) as f:
        hats_mapping = get_asset_mapping(hats_mapping_path)
    with open(clothes_mapping_path) as f:
        clothes_mapping = get_asset_mapping(clothes_mapping_path)

    # Number of patches per asset (1 to 3) - for now always set to 1
    patch_numb = bpy.data.node_groups["Number of Patches"].nodes["patch_numb"]
    patch_numb.integer = 1

    patch_pos = bpy.data.node_groups["Number of Patches"].nodes["patch_pos"]
    patch_1 = bpy.data.node_groups["Number of Patches"].nodes["patch_1"]
    patch_2 = bpy.data.node_groups["Number of Patches"].nodes["patch_2"]
    patch_3 = bpy.data.node_groups["Number of Patches"].nodes["patch_3"]
    asset = bpy.data.node_groups["Selector"].nodes["Integer"]

    # Render the hats patches
    for hats_asset, hats_asset_data in hats_mapping.items():
        print(f"")
        print(f"**** Rendering Patches for Hat: {hats_asset}")
        print(f"")

        if hats_asset_data.value == "Empty":
            continue

        # Set hat asset value
        asset.integer = int(hats_asset_data.value)

        for i in range(int(hats_asset_data.max_count)):
            # Set the patch position
            patch_pos.integer = i + 1

            # Generate patches for each faction
            for faction in ["watchers", "lightseers", "shadow-clan", "shrouded-devils", "community"]:
                for faction_patch_id in range(1, 11):
                    # Fetch patch ID
                    faction_patch_data = patch_mapping[faction][str(faction_patch_id)]
                    patch_id = int(faction_patch_data.value)

                    # Set the patches Tex(0 to 49)
                    patch_1.integer = patch_id
                    patch_2.integer = patch_id
                    patch_3.integer = patch_id

                    # Set resolution
                    bpy.data.scenes["Scene"].eevee.taa_render_samples = 60
                    bpy.data.scenes["Scene"].render.resolution_x = 3000
                    bpy.data.scenes["Scene"].render.resolution_y = 3000

                    # Set the output file
                    output_file_name = f"patch-hats-{hats_asset_data.value}-pos-{patch_pos.integer}-{faction}-{faction_patch_id}.png"
                    bpy.data.scenes["Scene"].render.filepath = f"./rendered-patches/{output_file_name}"

                    if path.exists(f"./rendered-patches/{output_file_name}") and path.getsize(f"./rendered-patches/{output_file_name}") > 3000000:
                        continue
                    print(f"")
                    print(f"**** Rendering patch: {output_file_name}")
                    print(f"")

                    bpy.ops.render.render(write_still=True)

                    print(f"")
                    print(f"**** ----> Rendered patch: {output_file_name}")
                    print(f"")

    # Render the clothes patches
    for clothes_asset, clothes_asset_data in clothes_mapping.items():
        print(f"")
        print(f"**** Rendering Patches for clothes: {clothes_asset}")
        print(f"")

        if hats_asset_data.value == "Empty":
            continue

        # Set clothes asset value
        asset.integer = int(clothes_asset_data.value)

        for i in range(int(clothes_asset_data.max_count)):
            # Set the patch position
            patch_pos.integer = i + 1

            # Generate patches for each faction
            for faction in ["watchers", "lightseers", "shadow-clan", "shrouded-devils", "community"]:
                for faction_patch_id in range(1, 11):
                    # Fetch patch ID
                    faction_patch_data = patch_mapping[faction][str(faction_patch_id)]
                    patch_id = int(faction_patch_data.value)

                    # Set the patches Tex(0 to 49)
                    patch_1.integer = patch_id
                    patch_2.integer = patch_id
                    patch_3.integer = patch_id

                    # Set resolution
                    bpy.data.scenes["Scene"].eevee.taa_render_samples = 100
                    bpy.data.scenes["Scene"].render.resolution_x = 3000
                    bpy.data.scenes["Scene"].render.resolution_y = 3000

                    # Set the output file
                    output_file_name = f"patch-clothes-{clothes_asset_data.value}-pos-{patch_pos.integer}-{faction}-{faction_patch_id}.png"
                    bpy.data.scenes["Scene"].render.filepath = f"./rendered-patches/{output_file_name}"

                    if path.exists(f"./rendered-patches/{output_file_name}") and path.getsize(f"./rendered-patches/{output_file_name}") > 3000000:
                        continue
                    print(f"")
                    print(f"**** Rendering patch: {output_file_name}")
                    print(f"")

                    bpy.ops.render.render(write_still=True)

                    print(f"")
                    print(f"**** ----> Rendered patch: {output_file_name}")
                    print(f"")


if __name__ == "__main__":
    sys.exit(main())
