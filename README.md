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
