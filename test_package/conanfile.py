from conans import ConanFile, CMake, tools, RunEnvironment
import os

class TestGlew(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            bin_path = os.path.join("bin", "AVTPTest")
            if self.settings.os == "Linux":
                self.run("LD_LIBRARY_PATH=%s:bin %s" % (os.environ.get('LD_LIBRARY_PATH', ''), bin_path))        

    def imports(self):
        if self.settings.os == "Linux":
            self.copy(pattern="*.so", dst="bin", src="lib")
