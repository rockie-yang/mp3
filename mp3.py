
__author__ = 'rockie yang'

import os
from os import path, listdir
from hanzi2pinyin import hanzi2pinyin

def name_converter(old):
    pinyin = hanzi2pinyin(old)
    remove_unconverted_chars = pinyin.encode('ascii', 'ignore').decode('ascii')

    return remove_unconverted_chars


def tranform(root_path, the_path):
    m3u_file = os.path.join(root_path, the_path + ".m3u")

    with open(m3u_file, "w") as m3u:

        for sub_path in listdir(the_path):
            old_full_path = os.path.join(the_path, sub_path)

            if os.path.isdir(old_full_path):
                new_path = name_converter(sub_path)

                new_full_path = os.path.join(the_path, new_path)

                print(sub_path, new_path)
                if old_full_path != new_full_path:
                    os.rename(old_full_path,
                              new_full_path)

                tranform(root_path, os.path.join(the_path, new_path))

            elif sub_path.lower().endswith(".mp3"):
                new_path = name_converter(sub_path)
                old_full_path = os.path.join(the_path, sub_path)
                new_full_path = os.path.join(the_path, new_path)

                print(root_path, new_full_path)
                if old_full_path != new_full_path:
                    os.rename(old_full_path,
                              new_full_path)

                try:
                    m3u.write(new_full_path[(len(root_path) + 1):])
                    m3u.write('\n')
                except Exception as ex:
                    print('could not write', new_full_path, ex)

#
# def tranform(sourcePath):
#     for sub_path in listdir(sourcePath):
#         print(sub_path)
#
#     for dirname, dirnames, filenames in os.walk(sourcePath):
#         # print(dirname)
#         for subdirname in dirnames:
#             # pass
#             print (subdirname) #os.path.join(dirname, subdirname)
#
#         # print path to all filenames.
#         # for filename in filenames:
#         #     if filename.lower().endswith(".mp3"):
#         #         print (filename) #os.path.join(dirname, filename)


tranform(u"/Users/yangyoujiang/Music/music",
         u"/Users/yangyoujiang/Music/music")


#
# #!/usr/bin/env python
#
# import os
# import sys
# import glob
# from mutagen.mp3 import MP3
# from mutagen.easyid3 import EasyID3
#
# #
# # MP3 playlist generator
# #
# # Generate an mp3 playlist file (.m3u), sorted by album track number.
# #
# # DEPENDENCIES
# #
# #   - Mutagen (http://code.google.com/p/mutagen/)
# #
# # NOTE: To install `mutagen`, run:
# #
# #   $ cd /path/to/mutagen/download/dir && python setup.py install
# #
# # USAGE
# #
# # You can pass directories two ways this script - as arguments or
# # via standard input.
# #
# #   $ m3u.py /AphexTwin/Drukqs
# #
# # or multiple directories:
# #
# #   $ find /dir/Music -type d -links 2 | m3u.py -
# #
# # Author: Jon LaBelle <jon@tech0.com>
# # Date: Sun Jul 28 2013 06:27:42 GMT-0500 (CDT)
# #
#
# def create_m3u(dir="."):
#
#     try:
#         print "Processing directory '%s'..." % dir
#
#         playlist = ''
#         mp3s = []
#         glob_pattern = "*.[mM][pP]3"
#
#         os.chdir(dir)
#
#         for file in glob.glob(glob_pattern):
#             if playlist == '':
#                 playlist = EasyID3(file)['album'][0] + '.m3u'
#
#             meta_info = {
#                 'filename': file,
#                 'length': int(MP3(file).info.length),
#                 'tracknumber': EasyID3(file)['tracknumber'][0].split('/')[0],
#                 }
#
#             mp3s.append(meta_info)
#
#         if len(mp3s) > 0:
#             print "Writing playlist '%s'..." % playlist
#
#             # write the playlist
#             of = open(playlist, 'w')
#             of.write("#EXTM3Un")
#
#             # sorted by track number
#             for mp3 in sorted(mp3s, key=lambda mp3: int(mp3['tracknumber'])):
#                 of.write("#EXTINF:%s,%sn" % (mp3['length'], mp3['filename']))
#                 of.write(mp3['filename'] + "n")
#
#             of.close()
#         else:
#             print "No mp3 files found in '%s'." % dir
#
#     except:
#         print "ERROR occured when processing directory '%s'. Ignoring." % dir
#         print "Text: ", sys.exc_info()[0]