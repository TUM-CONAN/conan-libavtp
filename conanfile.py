import os
from conans import ConanFile, Meson
from conans import tools

class libavtpConan(ConanFile):
    name = "libavtp"
    version = "0.2.0"
    source_directory = "%s-%s" % (name, version)
    description = "The libavtp library"
    generators = "cmake", "txt"
    settings = "os", "arch", "build_type", "compiler"
    url="http://github.com/ulricheck/conan-libavtp"
    license="https://github.com/AVnu/libavtp/blob/master/LICENSE"
    
    scm = {
        "type": "git",
        "subfolder": "sources",
        "url": "https://github.com/AVnu/libavtp.git",
        "revision": "v{0}".format(version),
    }

    def build_requirements(self):
        self.build_requires("meson/0.54.2")
        self.build_requires("cmocka/1.1.5")

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
         meson = Meson(self)
         meson.configure(source_folder="sources", build_folder="build")
         meson.build()


    def package(self):
        self.copy("*.h", dst="include", src=os.path.join("sources", "include"))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
