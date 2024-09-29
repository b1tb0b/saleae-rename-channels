import argparse
import zipfile
import os.path
import sys

def sal_rename_channels(src_file, new_file, *,
    new_ch0 = 'Channel 0',
    new_ch1 = 'Channel 1',
    new_ch2 = 'Channel 2',
    new_ch3 = 'Channel 3',
    new_ch4 = 'Channel 4',
    new_ch5 = 'Channel 5',
    new_ch6 = 'Channel 6',
    new_ch7 = 'Channel 7',
    new_ch8 = 'Channel 8',
    new_ch9 = 'Channel 9',
    new_ch10 = 'Channel 10',
    new_ch11 = 'Channel 11',
    new_ch12 = 'Channel 12',
    new_ch13 = 'Channel 13',
    new_ch14 = 'Channel 14',
    new_ch15 = 'Channel 15',
    new_channel_names = None,
    old_ch0 = 'Channel 0',
    old_ch1 = 'Channel 1',
    old_ch2 = 'Channel 2',
    old_ch3 = 'Channel 3',
    old_ch4 = 'Channel 4',
    old_ch5 = 'Channel 5',
    old_ch6 = 'Channel 6',
    old_ch7 = 'Channel 7',
    old_ch8 = 'Channel 8',
    old_ch9 = 'Channel 9',
    old_ch10 = 'Channel 10',
    old_ch11 = 'Channel 11',
    old_ch12 = 'Channel 12',
    old_ch13 = 'Channel 13',
    old_ch14 = 'Channel 14',
    old_ch15 = 'Channel 15',
    old_channel_names = None,
    debug=False):

    if debug: print(f"{src_file=}")
    if debug: print(f"{new_file=}")

    # Build array of default channel names: ['Channel 0', .., 'Channel 15'] 
    def_channel_names = ['Channel {}'.format(i) for i in range(0,16)]

    # Aggregate individual channel strings to array
    all_old_channels = [old_ch0,  old_ch1,  old_ch2,  old_ch3,
                        old_ch4,  old_ch5,  old_ch6,  old_ch7,
                        old_ch8,  old_ch9,  old_ch10, old_ch11,
                        old_ch12, old_ch13, old_ch14, old_ch15]

    all_new_channels = [new_ch0,  new_ch1,  new_ch2,  new_ch3,
                        new_ch4,  new_ch5,  new_ch6,  new_ch7,
                        new_ch8,  new_ch9,  new_ch10, new_ch11,
                        new_ch12, new_ch13, new_ch14, new_ch15]

    # Debug output
    if debug: print(f"{new_channel_names=}")
    if debug: print(f"{old_channel_names=}")
    if debug: print(f"{all_old_channels=}")
    if debug: print(f"{all_new_channels=}")

    # Set new channel names array, if not provided
    # Then check if both array and individual name(s) both provided
    if new_channel_names is None:
        new_channel_names = all_new_channels
    elif all_new_channels != def_channel_names:
        sys.stderr.write("ERROR: specify individual new channel(s) or all, not both")
        return 1

    # Set old channel names array, if not provided
    # Then check if both array and individual name(s) both provided
    if old_channel_names is None:
        old_channel_names = all_old_channels
    elif all_old_channels != def_channel_names:
        sys.stderr.write("ERROR: specify individual old channel(s) or all, not both")
        return 2

    # Enclose channel name strings with quotes ("")
    # Note: this avoids 'Channel 1' matching substring of 'Channel 10', etc.
    #   -> Must match '"Channel 1"', doesn't match '"Channel 10"', etc.
    new_channel_names = ['"{}"'.format(n) for n in new_channel_names]
    old_channel_names = ['"{}"'.format(n) for n in old_channel_names]
    if debug: print(f"{new_channel_names=}")
    if debug: print(f"{old_channel_names=}")

    # Setup channel rename dict
    channel_rename = dict(zip(old_channel_names, new_channel_names))
    if debug: print(f"{channel_rename=}")

    # Open source and destination (*.sal) zipfiles
    srczip = zipfile.ZipFile(src_file, 'r')
    newzip = zipfile.ZipFile(new_file, "w", compression=zipfile.ZIP_DEFLATED)

    # Iterate on all files within source zipfile
    for srczipinfo in srczip.infolist():

        # Read a file within source zipfile
        tmpfile = srczip.open(srczipinfo)

        # Check if filename matches for renaming
        if srczipinfo.filename == "meta.json":

            # Copy content 'bytes' and convert to 'str' (utf-8)
            content = str(tmpfile.read(), 'utf-8')

            # Rename all channels in dict (old -> new)
	    # Note: this is a 'dumb' string replace vs. 'smart' JSON parser
	    # (relies on Saleae using '"Channel {}"' as label strings only)
            for old, new in channel_rename.items():
                if debug: print(f'Rename: {old} -> {new}')
                content = content.replace(old, new)

        else:
            # Copy content (not the right filename)
            content = tmpfile.read()

        # Write content
        newzip.writestr(srczipinfo.filename, content)

    srczip.close()
    newzip.close()
    return 0


# Create an argparse argument parser
parser = argparse.ArgumentParser(description='Rename channel labels in Saleae Logic 2 capture file (*.sal)')
parser.add_argument("infile", help="Input (*.sal) filename")
parser.add_argument("-o", "--outfile", help="Output (*.sal) filename; default \"<infile>-out.sal\"")
parser.add_argument("-f", "--force", help="Force overwriting existing output file", action="store_true")
parser.add_argument("-d", "--debug", help="Enable debug of channel renaming", action="store_true")

for i in range(0,16):
    parser.add_argument("--new_ch{}".format(i),
                        help="New label for channel {}".format(i),
                        default="Channel {}".format(i))

for i in range(0,16):
    parser.add_argument("--old_ch{}".format(i),
                        help="Old label for channel {}; default: \"Channel {}\"".format(i,i),
                        default="Channel {}".format(i))
args = parser.parse_args()


# Set 'srcfile' based on argparse INFILE argument
srcfile=args.infile

# Check if 'srcfile' exists
if not os.path.isfile(srcfile):
    sys.stderr.write(f"ERROR: file \"{srcfile}\" not found!")
    exit(1)

# Check if OUTFILE specified as an argument
if args.outfile is None:
    # Extract path/base/extension from 'srcfile'
    (src_path,src_name) = os.path.split(srcfile)
    (src_base,src_extn) = os.path.splitext(src_name)
    if args.debug: print(f'{src_path=}')
    if args.debug: print(f'{src_name=}')
    if args.debug: print(f'{src_base=}')
    if args.debug: print(f'{src_extn=}')

    # Confirm *.sal file extension was passed as first argument
    if (src_extn.lower() != ".sal"):
        sys.stderr.write(f"WARNING: expected file extension \".sal\", not \"{src_extn}\"")

    # Create defile output filename: {src_base}-out.sal
    outfile=os.path.join(src_path, f'{src_base}-out.sal')

else:
    outfile=args.outfile

if os.path.isfile(outfile) and not args.force:
    sys.stderr.write(f"ERROR: file \"{outfile}\" already exists (use '--force' to overwrite)!")
    exit(1)

if args.debug:
    print(f"{args.new_ch0=}")
    print(f"{args.new_ch1=}")
    print(f"{args.new_ch2=}")
    print(f"{args.new_ch3=}")
    print(f"{args.new_ch4=}")
    print(f"{args.new_ch5=}")
    print(f"{args.new_ch6=}")
    print(f"{args.new_ch7=}")
    print(f"{args.new_ch8=}")
    print(f"{args.new_ch9=}")
    print(f"{args.new_ch10=}")
    print(f"{args.new_ch11=}")
    print(f"{args.new_ch12=}")
    print(f"{args.new_ch13=}")
    print(f"{args.new_ch14=}")
    print(f"{args.new_ch15=}")

    print(f"{args.old_ch0=}")
    print(f"{args.old_ch1=}")
    print(f"{args.old_ch2=}")
    print(f"{args.old_ch3=}")
    print(f"{args.old_ch4=}")
    print(f"{args.old_ch5=}")
    print(f"{args.old_ch6=}")
    print(f"{args.old_ch7=}")
    print(f"{args.old_ch8=}")
    print(f"{args.old_ch9=}")
    print(f"{args.old_ch10=}")
    print(f"{args.old_ch11=}")
    print(f"{args.old_ch12=}")
    print(f"{args.old_ch13=}")
    print(f"{args.old_ch14=}")
    print(f"{args.old_ch15=}")

sal_rename_channels(srcfile, outfile,
                    new_ch0=args.new_ch0,
                    new_ch1=args.new_ch1,
                    new_ch2=args.new_ch2,
                    new_ch3=args.new_ch3,
                    new_ch4=args.new_ch4,
                    new_ch5=args.new_ch5,
                    new_ch6=args.new_ch6,
                    new_ch7=args.new_ch7,
                    new_ch8=args.new_ch8,
                    new_ch9=args.new_ch9,
                    new_ch10=args.new_ch10,
                    new_ch11=args.new_ch11,
                    new_ch12=args.new_ch12,
                    new_ch13=args.new_ch13,
                    new_ch14=args.new_ch14,
                    new_ch15=args.new_ch15,
                    old_ch0=args.old_ch0,
                    old_ch1=args.old_ch1,
                    old_ch2=args.old_ch2,
                    old_ch3=args.old_ch3,
                    old_ch4=args.old_ch4,
                    old_ch5=args.old_ch5,
                    old_ch6=args.old_ch6,
                    old_ch7=args.old_ch7,
                    old_ch8=args.old_ch8,
                    old_ch9=args.old_ch9,
                    old_ch10=args.old_ch10,
                    old_ch11=args.old_ch11,
                    old_ch12=args.old_ch12,
                    old_ch13=args.old_ch13,
                    old_ch14=args.old_ch14,
                    old_ch15=args.old_ch15,
                    debug=args.debug)
