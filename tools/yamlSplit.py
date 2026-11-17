import yaml
import os
import hashlib
import shutil
from glob import glob
import tools.twobppextract

def doSplit(dir):
    if os.path.exists("extract/"):
        shutil.rmtree("extract/")
    os.mkdir("extract/")

    yamlname = dir+".yaml"
    if not os.path.exists(yamlname):
        print("yaml does not exist! skipping...")
        return False
    data_loaded = yaml.safe_load(open(yamlname, 'r'))

    rom = ""
    for mrom in glob("*.vb"):
        hash = hashlib.md5(open(mrom,'rb').read()).hexdigest()
        for expect_hash in data_loaded["md5"]:
            if hash == expect_hash:
                rom = mrom
                break
    if rom == "":
        return False

    rom_bytes = open(rom, "rb").read()
    rom_name = data_loaded["name"]
    print(f"splitting {rom} for {rom_name} assets")

    output = f"{dir}/"

    if os.path.exists(output):
        shutil.rmtree(output)
    os.makedirs(output)

    x = 0
    if "header" in list(data_loaded.keys()):
        open(output+'header.bin', "wb").write(rom_bytes[0:0x10])
        x += 0x10

    i = 0
    for real_entry in data_loaded["splits"]:
        start = real_entry[0]
        end = 0
        if i < len(data_loaded["splits"])-1:
            end = data_loaded["splits"][i+1][0]
        else:
            end = data_loaded["end"]
        do_extract = None
        usename = ""
        if len(real_entry) > 1:
            usename = real_entry[1]
            if len(real_entry) > 2:
                do_extract = real_entry[2]
        else:
            fake_addr = hex(start).replace("0x","")
            usename = f"unk{fake_addr}"
        end_result = f'{output}{usename}.bin'
        pathOnly = end_result.split("/")
        pathOnly.pop(-1)
        pathOnly = "/".join(pathOnly)
        if not os.path.exists(pathOnly):
            os.makedirs(pathOnly)
        bytes = rom_bytes[start:end]
        open(end_result, "ab").write(bytes)

        if do_extract != None:
            if do_extract == "png":
                tools.twobppextract.extract(usename, bytes, real_entry[3])

        i += 1
    return True
