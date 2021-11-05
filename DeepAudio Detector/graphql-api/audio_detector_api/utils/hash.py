"""Utils methods to calculate hashs"""
import hashlib

def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


def upload_to(instance, filename):
    """
    :type instance: dolphin.models.File
    """
    print("Llego acá")
    instance.my_file.open() # make sure we're at the beginning of the file
    contents = instance.my_file.read() # get the contents
    fname, ext = os.path.splitext(filename)
    return "{0}_{1}{2}".format(fname, hash_function(contents), ext) # assemble the filename