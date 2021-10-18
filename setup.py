from distutils.core import setup, Extension
import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
def main():
    setup(name="transfer.py",
          version="beta",
          description="transfers a PyObject",
          author="<Jordan Alexander Sweetman>",
          author_email="jordan.a.sweetman@icloud.com",
          ext_modules=[Extension("read_obj", ["read.c"]), Extension("write_obj", ["write.c"])])

if __name__ == "__main__":
    main()
