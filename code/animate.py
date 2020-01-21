""" A module that animates the trajectory of cars in the NGSIM dataset
    The module creates an image plot for each frame and then
    merges them into a single gif """

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import car_functions
import dataset_functions
import shutil
import imageio
import os

def get_car_color_label(type):
    """ Given the car type 1,2 or 3, the method returns the associated
    color and label for that car"""
    if type == 1:
        color = 'yellow'
        label = 'Motorcycle'
    elif type == 2:
        color = 'red'
        label = 'Auto'
    else:
        color = 'green'
        label = 'Truck'

    return color, label

def create_patches_from_frame(frame_id, dataset):
    """ Returns  two lists
    1) a list of rectangular patches representing the cars in a specific
    frame; patches are drawn on the plot
    2) a list of car ID's in a specific  frame
    """
    patches_list = []
    id_list = []

    frame = car_functions.create_frame(frame_id, dataset)
    cars = frame.get_cars()
    for car in cars:
        color, label = get_car_color_label(car.get_type())

        # calculate the lower left location to draw a rectangle car
        x = car.get_x_value() - (car.get_width()/2)
        y = car.get_y_value() - car.get_length()

        patch = patches.Rectangle((y, x),
                    car.get_length(), car.get_width(), fc=color, ec='black', label=label)

        patches_list.append(patch)
        id_list.append(car.get_id())
    return patches_list, id_list

def set_up_fig_axs():
    """ A method that sets the figure size and axes range for a plot
    and returns a figure and axes object"""
    fig = plt.figure()
    fig.set_size_inches(10, 5)

    ax = fig.add_subplot(111)
    ax.set_xlim(10, 800)
    ax.set_ylim(-40, 100)

    return fig, ax

def plot_road_border():
    """ A method that plots two horizontal lines representing the road boarder in the frame"""
    # plot road lines
    x = range(10, 800)
    y = [60 for i in range(10, 800)]
    y2 = [0 for i in range(10, 800)]
    plt.plot(x, y, '-.b')
    plt.plot(x, y2, '-.b')

    return plt

def generate_frame_imgs(frames, img_dir_path, dataset):
    """ creates and saves a set of images representing a raneg of frames in NGSIM dataset
    A single image is a plot of cars at given locations as found in the dataset for a given frame"""
    for frame in frames:
        fig, ax = set_up_fig_axs()
        plot_road_border()

        patches_list, id_list = create_patches_from_frame(frame, dataset)
        plt.title('frame ' + str(frame) + ' number of cars = ' + str(len(patches_list)))
        plt.xlabel('longitudinal position in feet')
        plt.ylabel('Lateral position in feet')

        for patch, id in zip(patches_list, id_list):
            if (patch.get_x() < 795): #restrict drawing to the size of chart
                ax.add_patch(patch)
                ax.text(patch.get_x() + 3, patch.get_y() + 2, id, fontsize=9, style='oblique') #car ID

                handles, labels = plt.gca().get_legend_handles_labels()
                by_label = dict(zip(labels, handles))
                plt.legend(by_label.values(), by_label.keys(), fontsize='large')

        plt.savefig(img_dir_path + str(frame))

def imgs_to_gif(img_dir_path, animation_file_name, frames):
    """ converts a set of images loaded from a directory to a gif animation
    and saves animation to a given  file name"""
    images = []
    for frame in frames:
        images.append(imageio.imread(img_dir_path + str(frame) + '.png'))
    imageio.mimsave(animation_file_name, images)

if __name__ == '__main__':

    img_dir_path = 'plots2/' # directory to save plots
    animation_file_name = 'animate.gif'
    if not os.path.exists(img_dir_path):
        os.mkdir(img_dir_path)

    train = dataset_functions.load_dataset()
    # spicify the range of frames you want to visualize
    frames = range(200, 550)
    generate_frame_imgs(frames, img_dir_path, train[1])

    imgs_to_gif(img_dir_path, animation_file_name, frames)
    shutil.rmtree(img_dir_path)
