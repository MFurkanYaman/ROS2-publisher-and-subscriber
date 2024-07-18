from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mfy',
    maintainer_email='metinfurkanyaman@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_py_node=my_py_pkg.my_first_node:main", #ros2 run dediğimde çalıştırmamı sağlıyor.
            "state_publisher=my_py_pkg.robot_state_publisher:main",
            "satellite=my_py_pkg.satellite:main"
        ],
    },
)
