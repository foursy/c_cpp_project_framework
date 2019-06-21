#
# @file from https://github.com/Neutree/c_cpp_project_framework
# @author neucrack
#

import argparse
import os, sys, time, re


parser = argparse.ArgumentParser(description='generate time info for', prog=os.path.basename(sys.argv[0]))

parser.add_argument('--toolchain',
                        help='toolchain path ( absolute path )',
                        default="")

parser.add_argument('--toolchain-prefix',
                        help='toolchain prefix(e.g. mips-elf-',
                        default="")

args = parser.parse_args()

config_filename = ".config.mk"

if not os.path.exists("CMakeLists.txt") or
    not os.path.exists("main"):
    print("please run me at project folder!")
    exit(1)

if args.toolchain == "" or not os.path.exists(args.toolchain):
    print("config toolchain path error:", args.toolchain)
    exit(1)
header = "# Generated by config.py, DO NOT edit!\n\n"
config_content = header
config_content += 'CONFIG_TOOLCHAIN_PATH="'+args.toolchain.strip()+'"\n'
config_content += 'CONFIG_TOOLCHAIN_PREFIX="'+args.toolchain_prefix+'"\n'
config_content += '\n'
with open(config_filename, "w") as f:
    f.write(config_content)
if os.path.exists("build/config/global_config.mk"):
    os.remove("build/config/global_config.mk")

print("generate config file at: {}".format(config_filename))

