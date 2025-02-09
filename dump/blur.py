from PIL import Image

def convolve(image, kernel):
    """Applies a convolution operation on an image with the given kernel."""
    image_array = [[pixel for pixel in row] for row in image.getdata()]  # Convert image to a 2D list
    width, height = image.size
    image_array = [image_array[i * width:(i + 1) * width] for i in range(height)]

    kernel_height = len(kernel)
    kernel_width = len(kernel[0])
    pad_h = kernel_height // 2
    pad_w = kernel_width // 2

    # Pad the image to handle edges
    padded_image = [[0] * (width + 2 * pad_w) for _ in range(height + 2 * pad_h)]
    for i in range(height):
        for j in range(width):
            padded_image[i + pad_h][j + pad_w] = image_array[i][j]

    # Initialize output array
    output = [[0] * width for _ in range(height)]

    # Perform convolution
    for i in range(height):
        for j in range(width):
            sum_value = 0
            for ki in range(kernel_height):
                for kj in range(kernel_width):
                    sum_value += padded_image[i + ki][j + kj] * kernel[ki][kj]
            output[i][j] = min(max(int(sum_value), 0), 255)  # Clip values to 0-255 range

    # Convert output to image
    output_image = Image.new("L", (width, height))
    output_image.putdata([pixel for row in output for pixel in row])
    return output_image

# Define Gaussian Blur kernel
def gaussian_blur_kernel(size=3, sigma=1.0):
    """Generates a Gaussian blur kernel."""
    ax = [(x - size // 2) for x in range(size)]
    kernel = [[0] * size for _ in range(size)]
    sum_value = 0
    for i in range(size):
        for j in range(size):
            value = (1 / (2.0 * 3.141592653589793 * sigma**2)) * (2.718281828459045 ** (-(ax[i]**2 + ax[j]**2) / (2.0 * sigma**2)))
            kernel[i][j] = value
            sum_value += value
    kernel = [[value / sum_value for value in row] for row in kernel]
    return kernel

# Define Edge Detection kernel (Sobel example)
def sobel_edge_detection_kernel():
    """Returns Sobel kernels for edge detection in x and y directions."""
    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    return sobel_x, sobel_y

# Example usage
if __name__ == "__main__":
    image = Image.open("lena.png").convert("L")  # Open image and convert to grayscale

    # Gaussian Blur
    gaussian_kernel = gaussian_blur_kernel(size=5, sigma=1.5)
    blurred_image = convolve(image, gaussian_kernel)
    blurred_image.show()  # Display blurred image

    # Edge Detection
    sobel_x, sobel_y = sobel_edge_detection_kernel()
    edges_x = convolve(image, sobel_x)
    edges_y = convolve(image, sobel_y)

    edges_x.show()  # Display horizontal edges
    edges_y.show()  # Display vertical edges
