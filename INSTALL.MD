sudo apt-get install libzmq3-dev python-zmq flite1-dev

Clone protobuf and pyflite from github

cd protobuf && ./autogen.sh && ./configure && make -j<num_cpu> && sudo make install && python python/setup.py build && sudo python python/setup.py install
cd ../pyflite && sudo python setup.py install
