import numpy as np 
import matplotlib.pyplot as plt
import time

plt.style.use('seaborn-v0_8-darkgrid')

np.random.seed(42)

print("Lab Environment Ready!")
print(f"NumPy version: {np.__version__}")


def exercise_1_1():
    """
    Create arrays using different methods and visualize them.
    """
    print("="*50)
    print("Exercise 1.1: Array Creation Methods")
    print("="*50)

    
    array_range = np.arange(0, 20, 1)             
    array_linear = np.linspace(0, 2*np.pi, 100)   
    identity_matrix = np.eye(5)                   
    random_matrix = np.random.rand(3, 3)          

    
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    
    axes[0, 0].bar(range(len(array_range)), array_range, color='skyblue')
    axes[0, 0].set_title('Array Range (0 to 19)')
    axes[0, 0].set_xlabel('Index')
    axes[0, 0].set_ylabel('Value')

    # 2. Sine Wave plot
    sine_wave = np.sin(array_linear)
    axes[0, 1].plot(array_linear, sine_wave, 'b-', linewidth=2)
    axes[0, 1].set_title('Sine Wave')
    axes[0, 1].set_xlabel('Radians')
    axes[0, 1].set_ylabel('sin(x)')
    axes[0, 1].grid(True)

    
    im1 = axes[1, 0].imshow(identity_matrix, cmap='RdBu', vmin=0, vmax=1)
    axes[1, 0].set_title('5x5 Identity Matrix')
    plt.colorbar(im1, ax=axes[1, 0])

   
    im2 = axes[1, 1].imshow(random_matrix, cmap='viridis')
    axes[1, 1].set_title('3x3 Random Matrix')
    for i in range(3):
        for j in range(3):
            axes[1, 1].text(j, i, f'{random_matrix[i, j]:.2f}',
                            ha='center', va='center', color='white')
    plt.colorbar(im2, ax=axes[1, 1])

    plt.tight_layout()
    plt.show()

    return array_range, array_linear, identity_matrix, random_matrix


arrays = exercise_1_1()


def exercise_1_2():
    """
    Explore array attributes with different dimensional arrays.
    """
    print("\n" + "="*50)
    print("Exercise 1.2: Array Attributes")
    print("="*50)

    arr_1d = np.array([1, 2, 3, 4, 5])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    arrays = [
        ("1D Array", arr_1d),
        ("2D Array", arr_2d),
        ("3D Array", arr_3d)
    ]

    for name, arr in arrays:
        print(f"\n{name}:")
        print(f" Array:\n{arr}")
        print(f" Shape: {arr.shape}")
        print(f" Dimensions: {arr.ndim}")
        print(f" Data type: {arr.dtype}")

    return arr_1d, arr_2d, arr_3d


exercise_1_2()


def exercise_2_1():
    """
    Compare performance between Numpy arrays and Python Lists.
    Create visualizations showing the speed differences.
    """
    print("\n" + "="*50)
    print("Exercise 2.1: The Great Performance Race!")
    print("="*50)
    
    sizes = [100, 1000, 10000, 100000]
    python_times = []
    numpy_times = []
    
    for size in sizes:
        py_list = list(range(size))
        np_array = np.arange(size)
        
        start_time = time.time()
        py_list_squared = [x**2 for x in py_list]
        py_time = time.time() - start_time
        python_times.append(py_time)
        
        start_time = time.time()
        np_array_squared = np_array ** 2
        np_time = time.time() - start_time
        numpy_times.append(np_time)
        
        speedup = py_time / np_time if np_time > 0 else float('inf')
        print(f"Size: {size:6}, Python Time: {py_time:.6f}s, NumPy Time: {np_time:.6f}s, Speedup: {speedup:.1f}x")
        
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    x = np.arange(len(sizes))
    width = 0.35
    
    ax1.bar(x - width/2, python_times, width, label='Python List', color='coral')
    ax1.bar(x + width/2, numpy_times, width, label='NumPy Array', color='skyblue')
    ax1.set_xlabel('Array Size')
    ax1.set_ylabel('Time (seconds)')
    ax1.set_title('Performance Comparison: Python vs NumPy')
    ax1.set_xticks(x)
    ax1.set_xticklabels(sizes)
    ax1.legend()
    ax1.set_yscale('log')
    
    speedups = [p/n if n > 0 else 0 for p, n in zip(python_times, numpy_times)]
    ax2.plot(sizes, speedups, 'go-', linewidth=2, markersize=10)
    ax2.set_xlabel('Array Size')
    ax2.set_ylabel('Speedup Factor')
    ax2.set_title('NumPy Speedup Over Python Lists')
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    
    plt.tight_layout()
    plt.show()
    
    return python_times, numpy_times


exercise_2_1()

import numpy as np
import matplotlib.pyplot as plt

def exercise_3_1():
    '''
    Create Pixel Art using NumPy arrays and matplotlib!
    '''
    print("\n" + "="*50)
    print("Exercise 3.1: NumPy Pixel Art")
    print("="*50)
    
    smiley = np.zeros((10, 10, 3), dtype=np.uint8)

    smiley[:] = [255, 255, 0]
    smiley[2:3, 3:4] = [0, 0, 0]
    smiley[2:3, 6:7] = [0, 0, 0]
    smiley[4:5, 4:6] = [255, 0, 0]
    smiley[7, 3:7] = [0, 0, 0]      
    smiley[6, 2] = [0, 0, 0]          
    smiley[6, 7] = [0, 0, 0]          
    smiley[5, 3] = [255, 255, 0]          
    smiley[5, 6] = [255, 255, 0]         
    plt.figure(figsize=(5, 5))
    plt.imshow(smiley, interpolation='nearest')
    plt.title('NumPy Pixel Art: Smiley Face')
    plt.axis('off')
    plt.show()
    
    return smiley

exercise_3_1()


def exercise_3_2():
    """
    Use broadcasting to create beautiful color gradients.
    """
    print("\n" + "="*50)
    print("Exercise 3.2: Color Gradients with Broadcasting")
    print("="*50)

    height, width = 256, 256

    x, y = np.meshgrid(np.arange(width), np.arange(height))

    gradient1 = x.astype(float)
    gradient2 = y.astype(float)
    gradient3 = x + y

    center_x, center_y = width // 2, height // 2
    gradient4 = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

    gradient5 = np.sin(x * 0.10) * np.cos(y * 0.10)

    block = 16
    checkerboard = ((x // block) + (y // block)) % 2         
    sine_component = np.sin((x + y) * 0.12)
    gradient6 = sine_component + 0.8 * checkerboard           

    
    gradients = [gradient1, gradient2, gradient3, gradient4, gradient5, gradient6]
    gradients_norm = []
    for g in gradients:
        g = g.astype(float)
        gmin, gmax = g.min(), g.max()
        if gmax > gmin:
            g = (g - gmin) / (gmax - gmin)
        else:
            g = np.zeros_like(g)
        gradients_norm.append(g)

    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    titles = ['Horizontal', 'Vertical', 'Diagonal', 'Circular', 'Sine Wave', 'Checkerboard + Sine']
    for ax, grad, title in zip(axes.flat, gradients_norm, titles):
        ax.imshow(grad, cmap='viridis', origin='lower', interpolation='nearest')
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

    return gradients_norm

exercise_3_2()

def exercise_4_1():
    """
    Analyze temperature data from multiple weather stations.
    """
    print("\n" + "="*50)
    print("Exercise 4.1: Weather Station Analysis")
    print("="*50)

    np.random.seed(42)
    base_temps = np.array([20, 22, 18, 25, 15])
    daily_variations = np.random.uniform(-5, 5, (5, 30))
    temperatures = base_temps.reshape(-1, 1) + daily_variations  
    mean_temps = np.mean(temperatures, axis=1)
    max_temps = np.max(temperatures, axis=1)
    min_temps = np.min(temperatures, axis=1)
    temp_ranges = max_temps - min_temps
    hottest_temp = np.max(temperatures)
    hottest_day_index = np.unravel_index(np.argmax(temperatures), temperatures.shape)[1]
    coldest_temp = np.min(temperatures)
    coldest_day_index = np.unravel_index(np.argmin(temperatures), temperatures.shape)[1]
    station_names = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']
    print("\nWeather Station Statistics:")
    for i, name in enumerate(station_names):
        if mean_temps is not None:
            print(f"{name}: Mean={mean_temps[i]:.1f}°C, "
                  f"Max={max_temps[i]:.1f}°C, "
                  f"Min={min_temps[i]:.1f}°C, "
                  f"Range={temp_ranges[i]:.1f}°C")
    
    if hottest_day_index is not None:
        print(f"\nHottest day: Day {hottest_day_index + 1} with {hottest_temp:.1f}°C")
    if coldest_day_index is not None:
        print(f"Coldest day: Day {coldest_day_index + 1} with {coldest_temp:.1f}°C")

    if temperatures is not None:
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        im = axes[0, 0].imshow(temperatures, cmap='coolwarm', aspect='auto')
        axes[0, 0].set_title('Temperature Heatmap (°C)')
        axes[0, 0].set_xlabel('Day')
        axes[0, 0].set_ylabel('Station')
        axes[0, 0].set_yticks(range(5))
        axes[0, 0].set_yticklabels(station_names)
        plt.colorbar(im, ax=axes[0, 0])

        days = np.arange(1, 31)
        for i, name in enumerate(station_names):
            axes[0, 1].plot(days, temperatures[i], label=name, linewidth=2)
        axes[0, 1].set_title('Daily Temperature Trends')
        axes[0, 1].set_xlabel('Day')
        axes[0, 1].set_ylabel('Temperature (°C)')
        axes[0, 1].legend(loc='best')
        axes[0, 1].grid(True, alpha=0.3)

        if mean_temps is not None:
            x_pos = np.arange(len(station_names))
            axes[1, 0].bar(x_pos, mean_temps, color='skyblue', label='Mean')
            axes[1, 0].errorbar(x_pos, mean_temps,
                              yerr=[(mean_temps - min_temps), (max_temps - mean_temps)],
                              fmt='none', color='black', capsize=5, label='Range')
            axes[1, 0].set_title('Station Temperature Comparison')
            axes[1, 0].set_xlabel('Station')
            axes[1, 0].set_ylabel('Temperature (°C)')
            axes[1, 0].set_xticks(x_pos)
            axes[1, 0].set_xticklabels(station_names)
            axes[1, 0].legend()

        daily_avg = temperatures.mean(axis=0)
        axes[1, 1].fill_between(days, daily_avg, alpha=0.3, color='green')
        axes[1, 1].plot(days, daily_avg, 'g-', linewidth=2)
        axes[1, 1].set_title('Daily Average Temperature (All Stations)')
        axes[1, 1].set_xlabel('Day')
        axes[1, 1].set_ylabel('Temperature (°C)')
        axes[1, 1].grid(True, alpha=0.3)
        if hottest_day_index is not None:
            axes[1, 1].plot(hottest_day_index + 1, daily_avg[hottest_day_index],
                           'ro', markersize=10, label=f'Hottest: Day {hottest_day_index + 1}')
        if coldest_day_index is not None:
            axes[1, 1].plot(coldest_day_index + 1, daily_avg[coldest_day_index],
                           'bo', markersize=10, label=f'Coldest: Day {coldest_day_index + 1}')
        axes[1, 1].legend()
        
        plt.tight_layout()
        plt.show()
    
    return temperatures, mean_temps, max_temps, min_temps
exercise_4_1()

def challenge_1():
    """
    Create a magic square where all rows, columns, and diagonals sum to the same value.
    """
    print("\n" + "="*50)
    print("Challenge 1: Magic Square")
    print("="*50)

    magic = np.array([[2, 7, 6],
                      [9, 5, 1],
                      [4, 3, 8]])
    row_sums = np.sum(magic, axis=1)
    col_sums = np.sum(magic, axis=0)
    diag1_sum = np.sum(np.diag(magic))
    diag2_sum = np.sum(np.diag(np.fliplr(magic)))  
    

    print(f"Row sums: {row_sums}")
    print(f"Column sums: {col_sums}")
    print(f"Main diagonal sum: {diag1_sum}")
    print(f"Anti-diagonal sum: {diag2_sum}")

    magic_constant = 15 
    is_magic = (np.all(row_sums == magic_constant) and 
                np.all(col_sums == magic_constant) and 
                diag1_sum == magic_constant and 
                diag2_sum == magic_constant)
    print(f"Is this a magic square? {is_magic}")
    magic_4x4 = np.array([[16,  3,  2, 13],
                          [ 5, 10, 11,  8],
                          [ 9,  6,  7, 12],
                          [ 4, 15, 14,  1]])
    
    print(f"\n4x4 Magic Square:")
    print(magic_4x4)
    print(f"4x4 Row sums: {np.sum(magic_4x4, axis=1)}")
    print(f"4x4 Column sums: {np.sum(magic_4x4, axis=0)}")
    print(f"4x4 Main diagonal sum: {np.sum(np.diag(magic_4x4))}")
    print(f"4x4 Anti-diagonal sum: {np.sum(np.diag(np.fliplr(magic_4x4)))}")
    
    return magic, magic_4x4
challenge_1()

def challenge_2():
    """
    Create and transform a simple image using NumPy operations.
    """
    print("\n" + "="*50)
    print("Challenge 2: Image Transformations")
    print("="*50)
    
    size = 20
    checkerboard = np.zeros((size, size))
    for i in range(0, size, 4):
        for j in range(0, size, 4):
            checkerboard[i:i+2, j:j+2] = 1
            checkerboard[i+2:i+4, j+2:j+4] = 1
    
    rotated = np.rot90(checkerboard)
    flipped_h = np.fliplr(checkerboard)
    flipped_v = np.flipud(checkerboard)
    inverted = 1 - checkerboard
    center = size // 2
    y, x = np.ogrid[:size, :size]
    mask = (x - center)**2 + (y - center)**2 <= (size//3)**2
    your_transform = checkerboard * mask  
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    images = [checkerboard, rotated, flipped_h, flipped_v, inverted, your_transform]
    titles = ['Original', 'Rotated 90°', 'Flipped H', 'Flipped V', 'Inverted', 'Circular Mask']
    
    for ax, img, title in zip(axes.flat, images, titles):
        if img is not None:
            ax.imshow(img, cmap='gray', interpolation='nearest')
            ax.set_title(title)
            ax.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return checkerboard, rotated, flipped_h, flipped_v, inverted
challenge_2()

def test_submission():
    """
    Test that all exercises run without errors.
    """
    print("Testing your submission...")
try:
        print("Testing Exercise 1.1...")
        exercise_1_1()
        
        print("Testing Exercise 1.2...")
        exercise_1_2()
        
        print("Testing Exercise 2.1...")
        exercise_2_1()
        
        print("Testing Exercise 3.1...")
        exercise_3_1()
        
        print("Testing Exercise 3.2...")
        exercise_3_2()
        
        print("Testing Exercise 4.1...")
        exercise_4_1()
        
        print("Testing Challenge 1...")
        challenge_1()
        
        print("Testing Challenge 2...")
        challenge_2()
        
        print("\n All tests passed! Ready to submit.")
        
except Exception as e:
        print(f"\n Error found: {e}")
        print("Please fix the error before submitting.")
        
test_submission()
