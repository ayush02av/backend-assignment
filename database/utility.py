def get_file_upload_path(path_url, path_vars_array):
	return path_url.format(path_vars_array)

def record_image_path(instance, filename):
    url = "records/{0[0]}_{0[1]}_{0[2]}"
    vars_array = [
        instance.record_name,
        {instance._id},
        filename
    ]
    return get_file_upload_path(url, vars_array)

def resize_image(image_path):
    import cv2

    original_image = cv2.imread(image_path, 1)

    resize_scale = 0.5

    resize_dimension = ( int(original_image.shape[1] * resize_scale), int(original_image.shape[0] * resize_scale) )

    resized_image = cv2.resize(original_image, (144, 144))

    cv2.imwrite(image_path, resized_image)