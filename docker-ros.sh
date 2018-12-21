xhost +local:root

XAUTH=/tmp/.docker.xauth
if [ ! -f $XAUTH ]
then
    xauth_list=$(xauth nlist :0 | sed -e 's/^..../ffff/')
    if [ ! -z "$xauth_list" ]
    then
        echo $xauth_list | xauth -f $XAUTH nmerge -
    else
        touch $XAUTH
    fi
    chmod a+r $XAUTH
fi

docker run -it \
	-v /home/rafal/RosProjects/catkin_ws/:/catkin_ws/ \
	-v /home/rafal/RosProjects/turtlebot_ws/:/turtlebot_ws/ \
	--name=ros-kinetic \
	--shm-size=1g \
	--ulimit memlock=-1 \
	--env="DISPLAY" \
	--env="QT_X11_NO_MITSHM=1" \
	--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	--env="XAUTHORITY=$XAUTH" \
	--env="NVIDIA_VISIBLE_DEVICES=all" \
	--env="NVIDIA_DRIVER_CAPABILITIES=all" \
        --network=host \
	-p 8008:22 \
	-p 6006:6006 \
	-p 11311:11311 \
	ros:kinetic-robot \
	bash

