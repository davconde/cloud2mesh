import options
from process_cloud import process_cloud
from split_cloud import split_cloud
from utils import find_files

if __name__ == "__main__":
    if options.split:
        # Split the original cloud
        print('Splitting cloud')
        split_cloud(options.filename, options.grid_size)

    if options.process:
        # Process the obtained files
        if options.single_filename is None:
            clouds = find_files('clouds')
            for cloud_name in clouds:
                print('Processing cloud ' + cloud_name)
                process_cloud(cloud_name)
        else:
            print('Processing cloud ' + options.single_filename)
            process_cloud(options.single_filename)

    print('Done')
