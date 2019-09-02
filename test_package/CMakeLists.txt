project(AVTPTest)
cmake_minimum_required(VERSION 3.0.0)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(AVTPTest main.c)
target_compile_definitions(AVTPTest PUBLIC "${CONAN_DEFINES}")
target_link_libraries(AVTPTest PUBLIC "${CONAN_LIBS}")
set_target_properties(AVTPTest PROPERTIES LINK_FLAGS "${CONAN_EXE_LINKER_FLAGS}")