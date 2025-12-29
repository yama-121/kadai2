from setuptools import find_packages, setup

package_name = 'ros2_kadai2'

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
    maintainer='ikki',
    maintainer_email='ikki.yama@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'translator_node = ros2_kadai2.translator_node:main',
            'display = ros2_morse_converter.display:main',
        ],
    },
)
