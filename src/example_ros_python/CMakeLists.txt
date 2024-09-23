cmake_minimum_required(VERSION 3.10)
project(example_ros_python)

## Use C++14
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

## By adding -Wall and -Werror, the compiler does not ignore warnings anymore,
## enforcing cleaner code.
add_definitions(-Wall -Wpedantic)

## Find catkin macros and libraries
find_package(catkin REQUIRED
  COMPONENTS
)



catkin_package(
  INCLUDE_DIRS
  CATKIN_DEPENDS rospy  
)

# Mark launch for instalation
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
# Mark launch for confirguration file
install(DIRECTORY config
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Install the ros node(s)
catkin_install_python(PROGRAMS 
  src/node.py 
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
