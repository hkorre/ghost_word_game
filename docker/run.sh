docker run --rm \
       -p 8888:8888 \
       -w /home \
       --name hk_ghost \
       -h hk-ghost \
       -it hkorre:ghost \
       /bin/bash
