import options
from process_cloud import process_cloud
from split_cloud import split_cloud
from utils import find_files

if __name__ == "__main__":
    if options.SPLIT:
        # Split the original cloud
        print('Splitting cloud')
        split_cloud(options.FILENAME, options.GRID_SIZE)

    if options.PROCESS:
        # Process the obtained files
        if options.SINGLE_FILENAME is None:
            clouds = find_files('clouds')
            for cloud_name in clouds:
                print('Processing cloud ' + cloud_name)
                process_cloud(cloud_name)
        else:
            print('Processing cloud ' + options.SINGLE_FILENAME)
            process_cloud(options.SINGLE_FILENAME)

    print('Done')
