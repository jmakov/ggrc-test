from os.path import abspath, dirname, join

THIS_ABS_PATH = abspath(dirname(__file__))
test_dir_name = THIS_ABS_PATH.split('/')[-1]
base_metrics_dir = join(THIS_ABS_PATH, '../../metrics/{}'.format(test_dir_name))
outfile = join(base_metrics_dir, "output1.csv")
with open(outfile, "w") as f:
	f.write("donkey")
