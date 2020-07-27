import obj_detect as od

def callback(message):
    print(message)


def main():
    od.__init__("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")


if __name__ == "__main__":
    main()
