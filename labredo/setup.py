from setuptools import setup
from glob import glob
import os 

package_name = 'labredo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name), glob('*launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ankit',
    maintainer_email='ankit@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'newpublisher = labredo.newpublisher:main',
            'newsubscriber = labredo.newsubscriber:main',
            'add_two_ints_newserver = labredo.add_two_ints_newserver:main',
            'add_two_ints_newclient = labredo.add_two_ints_newclient:main',
            'newturtle_controller = labredo.newturtle_controller:main'
        ],
    },
)
