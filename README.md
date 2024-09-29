# saleae-rename-channels
Python script to rename channels in a Saleae Logic2 capture file (*.sal)

For Saleae Logic2, see: https://www.saleae.com/

Original Saleae discussion response that inspire this script:
* https://discuss.saleae.com/t/applying-a-preset-to-logic2-automation-api-capture/3022/3

**References:**
* Python `zipfile` library: https://docs.python.org/3/library/zipfile.html
* StackOverflow: https://stackoverflow.com/questions/65090421/python-replace-string-on-files-inside-zipfile
* Saleae SAL file format:
  * Support: https://support.saleae.com/faq/technical-faq/sal-file-format
  * Discuss: https://discuss.saleae.com/t/logic-2-capture-format-sal/1858
* Other pages related to Logic2 channel rename feature:
  * https://discuss.saleae.com/t/applying-a-preset-to-logic2-automation-api-capture/3022
  * https://discuss.saleae.com/t/python-api-channel-naming/1926
  * https://ideas.saleae.com/b/feature-requests/automation-api-edit-channel-names-labels/
  * https://discuss.saleae.com/t/automatization-changing-label/1955


**sal-rename-channels.py script:** 

>     usage: sal-rename-channels.py [-h] [-o OUTFILE] [-f] [-d] [--new_ch0 NEW_CH0]
>                                   [--new_ch1 NEW_CH1] [--new_ch2 NEW_CH2]
>                                   [--new_ch3 NEW_CH3] [--new_ch4 NEW_CH4]
>                                   [--new_ch5 NEW_CH5] [--new_ch6 NEW_CH6]
>                                   [--new_ch7 NEW_CH7] [--new_ch8 NEW_CH8]
>                                   [--new_ch9 NEW_CH9] [--new_ch10 NEW_CH10]
>                                   [--new_ch11 NEW_CH11] [--new_ch12 NEW_CH12]
>                                   [--new_ch13 NEW_CH13] [--new_ch14 NEW_CH14]
>                                   [--new_ch15 NEW_CH15] [--old_ch0 OLD_CH0]
>                                   [--old_ch1 OLD_CH1] [--old_ch2 OLD_CH2]
>                                   [--old_ch3 OLD_CH3] [--old_ch4 OLD_CH4]
>                                   [--old_ch5 OLD_CH5] [--old_ch6 OLD_CH6]
>                                   [--old_ch7 OLD_CH7] [--old_ch8 OLD_CH8]
>                                   [--old_ch9 OLD_CH9] [--old_ch10 OLD_CH10]
>                                   [--old_ch11 OLD_CH11] [--old_ch12 OLD_CH12]
>                                   [--old_ch13 OLD_CH13] [--old_ch14 OLD_CH14]
>                                   [--old_ch15 OLD_CH15]
>                                   infile
>     
>     Rename channel labels in Saleae Logic 2 capture file (*.sal)
>     
>     positional arguments:
>       infile                Input (*.sal) filename
>     
>     options:
>       -h, --help            show this help message and exit
>       -o OUTFILE, --outfile OUTFILE
>                             Output (*.sal) filename; default "<infile>-out.sal"
>       -f, --force           Force overwriting existing output file
>       -d, --debug           Enable debug of channel renaming
>       --new_ch0 NEW_CH0     New label for channel 0
>       --new_ch1 NEW_CH1     New label for channel 1
>       --new_ch2 NEW_CH2     New label for channel 2
>       --new_ch3 NEW_CH3     New label for channel 3
>       --new_ch4 NEW_CH4     New label for channel 4
>       --new_ch5 NEW_CH5     New label for channel 5
>       --new_ch6 NEW_CH6     New label for channel 6
>       --new_ch7 NEW_CH7     New label for channel 7
>       --new_ch8 NEW_CH8     New label for channel 8
>       --new_ch9 NEW_CH9     New label for channel 9
>       --new_ch10 NEW_CH10   New label for channel 10
>       --new_ch11 NEW_CH11   New label for channel 11
>       --new_ch12 NEW_CH12   New label for channel 12
>       --new_ch13 NEW_CH13   New label for channel 13
>       --new_ch14 NEW_CH14   New label for channel 14
>       --new_ch15 NEW_CH15   New label for channel 15
>       --old_ch0 OLD_CH0     Old label for channel 0; default: "Channel 0"
>       --old_ch1 OLD_CH1     Old label for channel 1; default: "Channel 1"
>       --old_ch2 OLD_CH2     Old label for channel 2; default: "Channel 2"
>       --old_ch3 OLD_CH3     Old label for channel 3; default: "Channel 3"
>       --old_ch4 OLD_CH4     Old label for channel 4; default: "Channel 4"
>       --old_ch5 OLD_CH5     Old label for channel 5; default: "Channel 5"
>       --old_ch6 OLD_CH6     Old label for channel 6; default: "Channel 6"
>       --old_ch7 OLD_CH7     Old label for channel 7; default: "Channel 7"
>       --old_ch8 OLD_CH8     Old label for channel 8; default: "Channel 8"
>       --old_ch9 OLD_CH9     Old label for channel 9; default: "Channel 9"
>       --old_ch10 OLD_CH10   Old label for channel 10; default: "Channel 10"
>       --old_ch11 OLD_CH11   Old label for channel 11; default: "Channel 11"
>       --old_ch12 OLD_CH12   Old label for channel 12; default: "Channel 12"
>       --old_ch13 OLD_CH13   Old label for channel 13; default: "Channel 13"
>       --old_ch14 OLD_CH14   Old label for channel 14; default: "Channel 14"
>       --old_ch15 OLD_CH15   Old label for channel 15; default: "Channel 15" 
    
