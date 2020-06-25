import os
def clear_dist():
    filelist = [f for f in os.listdir("dist")]
    for f in filelist:
        os.remove(os.path.join("dist", f))
def publish_test():
    file = open('hspy_ext/version.txt', 'r+')
    version = file.read()
    version = str(version.split('.')[0])+'.'+version.split('.')[1]+'.'+str(int(version.split('.')[2])+1)
    file.seek(0,0)
    file.write(version)
    file.close()
    clear_dist()
    os.system('python3 setup.py sdist bdist_wheel')
    os.system('python3 -m twine upload --repository testpypi dist/*')
publish_test()
