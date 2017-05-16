import os, tarfile
import datetime

root_path = os.path.dirname(__file__)
tar_path = os.path.join(root_path, datetime.datetime.today().strftime('%Y-%m-%d'))
# 一次性打包整个根目录。空子目录会被打包。
# 如果只打包不压缩，将"w:gz"参数改为"w:"或"w"即可。
def make_targz(source_dir, output_filename):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

if __name__ == '__main__':
    bf_list = ['/home/liuchang/764191074/']
    for k, d in enumerate(bf_list):
        make_targz(d, tar_path + '-{}.tar'.format(k))