import numpy as np
import math
import cc3d

# For a given vertex, calculates area(A) & perimeter(P) values according to marching squares,
# and divides those values among each of the cells neighboring that vertex
def contourer(threshold, v0, v1, v2, v3, cell_id):
    area = np.zeros(4)
    perimeter = np.zeros(4)
    c0 = int(v0 > threshold)
    c1 = int(v1 > threshold)
    c2 = int(v2 > threshold)
    c3 = int(v3 > threshold)
    D = c0 + 2*c1 + 4*c2 + 8*c3
    if (D == 0):
        area[0], area[1], area[2], area[3] = 0, 0, 0, 0
        perimeter[0], perimeter[1], perimeter[2], perimeter[3] = 0, 0, 0, 0
    if (D == 1):
        p1 = (v0 - threshold) / (v0 - v1)
        p3 = (v0 - threshold) / (v0 - v3)
        area[0] = 0.5*p1*p3
        perimeter[0] = math.sqrt(p1*p1 + p3*p3)
    if (D == 2):
        p0 = (v1 - threshold) / (v1 - v0)
        p2 = (v1 - threshold) / (v1 - v2)
        area[1] = 0.5*p0*p2
        perimeter[1] = math.sqrt(p0*p0 + p2*p2)
    if (D == 4):
        p1 = (v2 - threshold) / (v2 - v1)
        p3 = (v2 - threshold) / (v2 - v3)
        area[2] = 0.5*p1*p3
        perimeter[2] = math.sqrt(p1*p1 + p3*p3)
    if (D == 8):
        p0 = (v3 - threshold) / (v3 - v0)
        p2 = (v3 - threshold) / (v3 - v2)
        area[3] = 0.5*p0*p2
        perimeter[3] = math.sqrt(p0*p0 + p2*p2)
    if (D == 14):
        p1 = (v0 - threshold) / (v0 - v1)
        p3 = (v0 - threshold) / (v0 - v3)
        area[1], area[3], area[2] = (0.75 - 0.5*p1*p3)/2, (0.75 - 0.5*p1*p3)/2, 0.25
        perimeter[1], perimeter[3] = (math.sqrt(p1*p1 + p3*p3))/2, (math.sqrt(p1*p1 + p3*p3))/2 
    if (D == 13):
        p0 = (v1 - threshold) / (v1 - v0)
        p2 = (v1 - threshold) / (v1 - v2)
        area[0], area[2], area[3] = (0.75 - 0.5*p0*p2)/2, (0.75 - 0.5*p0*p2)/2, 0.25
        perimeter[0], perimeter[2] = (math.sqrt(p0*p0 + p2*p2))/2, (math.sqrt(p0*p0 + p2*p2))/2
    if (D == 11):
        p1 = (v2 - threshold) / (v2 - v1)
        p3 = (v2 - threshold) / (v2 - v3)
        area[1], area[3], area[0] = (0.75 - 0.5*p1*p3)/2, (0.75 - 0.5*p1*p3)/2, 0.25
        perimeter[1], perimeter[3] = (math.sqrt(p1*p1 + p3*p3))/2, (math.sqrt(p1*p1 + p3*p3))/2
    if (D == 7):
        p0 = (v3 - threshold) / (v3 - v0)
        p2 = (v3 - threshold) / (v3 - v2)
        area[0], area[2], area[1] = (0.75 - 0.5*p0*p2)/2, (0.75 - 0.5*p0*p2)/2, 0.25
        perimeter[0], perimeter[2] = (math.sqrt(p0*p0 + p2*p2))/2, (math.sqrt(p0*p0 + p2*p2))/2
    if (D == 3):
        p_a = (v1 - threshold) / (v1 - v2)
        p_b = (v0 - threshold) / (v0 - v3)
        p_l, p_s = max(p_a, p_b), min(p_a, p_b)
        area[0], area[1] = (p_s + 0.5*(p_l - p_s))/2, (p_s + 0.5*(p_l - p_s))/2
        perimeter[0], perimeter[1] = (math.sqrt(1 + (p_l - p_s)*(p_l - p_s)))/2, (math.sqrt(1 + (p_l - p_s)*(p_l - p_s)))/2
    if (D == 6):
        p_a = (v1 - threshold) / (v1 - v0)
        p_b = (v2 - threshold) / (v2 - v3)
        p_l, p_s = max(p_a, p_b), min(p_a, p_b)
        area[1], area[2] = (p_s + 0.5*(p_l - p_s))/2, (p_s + 0.5*(p_l - p_s))/2
        perimeter[1], perimeter[2] = (math.sqrt(1 + (p_l - p_s)*(p_l - p_s)))/2, (math.sqrt(1 + (p_l - p_s)*(p_l - p_s)))/2
    if (D == 12):
        p_a = (v2 - threshold) / (v2 - v1)
        p_b = (v3 - threshold) / (v3 - v0)
        p_l, p_s = max(p_a, p_b), min(p_a, p_b)
        area[2], area[3] = (p_s + 0.5*(p_l - p_s))/2, (p_s + 0.5*(p_l - p_s))/2
        perimeter[2], perimeter[3] = (math.sqrt(1 + (p_l - p_s)*(p_l - p_s)))/2, (math.sqrt(1 + (p_l - p_s)*(p_l - p_s)))/2
    if (D == 9):
        p_a = (v0 - threshold) / (v0 - v1)
        p_b = (v3 - threshold) / (v3 - v2)
        p_l, p_s = max(p_a, p_b), min(p_a, p_b)
        area[3], area[0] = (p_s + 0.5*(p_l - p_s))/2, (p_s + 0.5*(p_l - p_s))/2
        perimeter[3], perimeter[0] = (math.sqrt(1 + (p_l - p_s)*(p_l - p_s)))/2, (math.sqrt(1 + (p_l - p_s)*(p_l - p_s)))/2
    if (D == 5):
        p1 = (v0 - threshold) / (v0 - v1)
        p2 = (v2 - threshold) / (v2 - v1)
        p3 = (v0 - threshold) / (v0 - v3)
        p4 = (v2 - threshold) / (v2 - v3)
        area[0], area[2] = (1 - ( 0.5*(1 - p1)*(1 - p2) + 0.5*(1 - p3)*(1 - p4) ))/2, (1 - ( 0.5*(1 - p1)*(1 - p2) + 0.5*(1 - p3)*(1 - p4) ))/2
        perimeter[0], perimeter[2] = (math.sqrt((1 - p1)*(1 - p1) + (1 - p2)*(1 - p2)) + math.sqrt((1 - p3)*(1 - p3) + (1 - p4)*(1 - p4)))/2, (math.sqrt((1 - p1)*(1 - p1) + (1 - p2)*(1 - p2)) + math.sqrt((1 - p3)*(1 - p3) + (1 - p4)*(1 - p4)))/2
    if (D == 10):
        p1 = (v1 - threshold) / (v1 - v0)
        p2 = (v3 - threshold) / (v3 - v0)
        p3 = (v1 - threshold) / (v1 - v2)
        p4 = (v3 - threshold) / (v3 - v2)
        area[1], area[3] = (1 - ( 0.5*(1 - p1)*(1 - p2) + 0.5*(1 - p3)*(1 - p4) ))/2, (1 - ( 0.5*(1 - p1)*(1 - p2) + 0.5*(1 - p3)*(1 - p4) ))/2
        perimeter[1], perimeter[3] = (math.sqrt((1 - p1)*(1 - p1) + (1 - p2)*(1 - p2)) + math.sqrt((1 - p3)*(1 - p3) + (1 - p4)*(1 - p4)))/2, (math.sqrt((1 - p1)*(1 - p1) + (1 - p2)*(1 - p2)) + math.sqrt((1 - p3)*(1 - p3) + (1 - p4)*(1 - p4)))/2
    if (D == 15):
        area[0], area[1], area[2], area[3] = 0.25, 0.25, 0.25, 0.25
        perimeter[0], perimeter[1], perimeter[2], perimeter[3] = 0, 0, 0, 0
    result_0, result_1 = 0, 0
    if cell_id == 0:
        result_0, result_1 = area[0], perimeter[0]
    if cell_id == 1:
        result_0, result_1 = area[1], perimeter[1]
    if cell_id == 2:
        result_0, result_1 = area[2], perimeter[2]
    if cell_id == 3:
        result_0, result_1 = area[3], perimeter[3]
    return [result_0, result_1]

# Applies the contourer() function to every vertex in the image, and
# stores the A values in data[0] and P values in data[1], 
# both of which have the same dimensions as the image 
def contour_all(image, threshold):
    sizelist = image.shape
    data = np.zeros((sizelist[0], sizelist[1], 2))
    for i in range(sizelist[0]+1):
        for j in range(sizelist[1]+1):
            if (i == 0 or j == 0 or i == sizelist[0] or j == sizelist[1]):
                if (i == 0 and j == 0):
                    v0, v1, v3 = (threshold - abs(image[i, j] - threshold)), (threshold - abs(image[i, j] - threshold)), (threshold - abs(image[i, j] - threshold))
                    v2 = image[i, j]
                    data[i, j, 0], data[i, j, 1] = data[i, j, 0] + contourer(threshold, v0, v1, v2, v3, 2)[0], data[i, j, 1] + contourer(threshold, v0, v1, v2, v3, 2)[1]
                elif (i == sizelist[0] and j == 0):
                    v0, v2, v3 = (threshold - abs(image[i-1, j] - threshold)), (threshold - abs(image[i-1, j] - threshold)), (threshold - abs(image[i-1, j] - threshold))
                    v1 = image[i-1, j]
                    data[i-1, j, 0], data[i-1, j, 1] = data[i-1, j, 0] + contourer(threshold, v0, v1, v2, v3, 1)[0], data[i-1, j, 1] + contourer(threshold, v0, v1, v2, v3, 1)[1]
                elif (i == 0 and j == sizelist[1]):
                    v0, v1, v2 = (threshold - abs(image[i, j-1] - threshold)), (threshold - abs(image[i, j-1] - threshold)), (threshold - abs(image[i, j-1] - threshold))
                    v3 = image[i, j-1]
                    data[i, j-1, 0], data[i, j-1, 1] = data[i, j-1, 0] + contourer(threshold, v0, v1, v2, v3, 3)[0], data[i, j-1, 1] + contourer(threshold, v0, v1, v2, v3, 3)[1]
                elif (i == sizelist[0] and j == sizelist[1]):
                    v1, v2, v3 = (threshold - abs(image[i-1, j-1] - threshold)), (threshold - abs(image[i-1, j-1] - threshold)), (threshold - abs(image[i-1, j-1] - threshold))
                    v0 = image[i-1, j-1]
                    data[i-1, j-1, 0], data[i-1, j-1, 1] = data[i-1, j-1, 0] + contourer(threshold, v0, v1, v2, v3, 0)[0], data[i-1, j-1, 1] + contourer(threshold, v0, v1, v2, v3, 0)[1]
                elif (i == 0):
                    v0, v1 = (threshold - abs(image[i, j-1] - threshold)), (threshold - abs(image[i, j] - threshold))
                    v2 = image[i, j]
                    v3 = image[i, j-1]
                    data[i, j-1, :] = data[i, j-1, :] + contourer(threshold, v0, v1, v2, v3, 3)
                    data[i, j, :] = data[i, j, :] + contourer(threshold, v0, v1, v2, v3, 2)
                elif (i == sizelist[0]):
                    v3, v2 = (threshold - abs(image[i-1, j-1] - threshold)), (threshold - abs(image[i-1, j] - threshold))
                    v1 = image[i-1, j]
                    v0 = image[i-1, j-1]
                    data[i-1, j-1, :] = data[i-1, j-1, :] + contourer(threshold, v0, v1, v2, v3, 0)
                    data[i-1, j, :] = data[i-1, j, :] + contourer(threshold, v0, v1, v2, v3, 1)
                elif (j == 0):
                    v0, v3 = (threshold - abs(image[i-1, j] - threshold)), (threshold - abs(image[i, j] - threshold))
                    v1 = image[i-1, j]
                    v2 = image[i, j]
                    data[i-1, j, :] = data[i-1, j, :] + contourer(threshold, v0, v1, v2, v3, 1)
                    data[i, j, :] = data[i, j, :] + contourer(threshold, v0, v1, v2, v3, 2)
                elif (j == sizelist[1]):
                    v1, v2 = (threshold - abs(image[i-1, j-1] - threshold)), (threshold - abs(image[i, j-1] - threshold))
                    v0 = image[i-1, j-1]
                    v3 = image[i, j-1]
                    data[i-1, j-1, :] = data[i-1, j-1, :] + contourer(threshold, v0, v1, v2, v3, 0)
                    data[i, j-1, :] = data[i, j-1, :] + contourer(threshold, v0, v1, v2, v3, 3)
            else:
                v0 = image[i-1, j-1]
                v1 = image[i-1, j]
                v2 = image[i, j]
                v3 = image[i, j-1]
                data[i-1, j-1, :] = data[i-1, j-1, :] + contourer(threshold, v0, v1, v2, v3, 0)
                data[i-1, j, :] = data[i-1, j, :] + contourer(threshold, v0, v1, v2, v3, 1)
                data[i, j, :] = data[i, j, :] + contourer(threshold, v0, v1, v2, v3, 2)
                data[i, j-1, :] = data[i, j-1, :] + contourer(threshold, v0, v1, v2, v3, 3)
    
    return data

# Takes a threshold value as input, and
# converts the image into a binary image with
# 1 above the threshold and 0 below the threshold.
# Returns this binary image (to be used for connected-component analysis)
def thresholder(image, threshold):
    sizelist = image.shape
    thresh = np.zeros((sizelist[0], sizelist[1]))
    for i in range(sizelist[0]):
        for j in range(sizelist[1]):
            if image[i, j] > threshold:
                thresh[i, j] = 1
    return thresh

# First performs connected-component analysis on the binary image.
# Then, for each such connected component, adds up the A & P values in each cell belonging to that component,
# in a single pass through the data[0] and data[1] arrays respectively.
# Returns a list of shape (N+1,2), where N is the number of distinct connected components.
# in the second index, 0 refers to area and 1 refers to perimeter, so e.g.
# value_list(img, t)[m, 1] equals the perimeter of the m-th connected component when the threshold value t is applied to the image img.
#
# **************   This completes the task of finding A & P of each component from an image at a given threshold.    ******************
def value_list(image, threshold):
    conn, N = cc3d.connected_components(np.array(thresholder(image, threshold), dtype = bool), connectivity=8, return_N=True)
    values = np.zeros((N+1, 2))
    data = contour_all(image, threshold)
    sizelist = image.shape
    for i in range(sizelist[0]):
        for j in range(sizelist[1]):
            if conn[i, j] > 0:
                ID = conn[i, j]
                values[ID, :] = values[ID, :] + data[i, j, :]
    return values
# *************************************************************************************************************************************


# Following are some functions for studying the filamentarity of the connected components:


# Reads greyscale input image and threshold, and returns the full list of filamentarities of the connected components found
# at that threshold 
def filamentarity(img, threshold):
    V_arr = value_list(img, threshold)
    A = V_arr[1:,0]
    P = V_arr[1:,1]
    F = ( (P**2 / (4*math.pi*A)) - 1 ) / ( (P**2 / (4*math.pi*A)) + 1 )
    return F

# Reads greyscale input image and threshold, and returns mean filamentarity of the connected components found
# at that threshold (having area greater than A_min)
def mean_filamentarity(img, threshold, A_min):
    V_arr = value_list(img, threshold)
    A = V_arr[1:,0]
    P = V_arr[1:,1]
    F = ( (P**2 / (4*math.pi*A)) - 1 ) / ( (P**2 / (4*math.pi*A)) + 1 )
    if np.sum(A) == 0 or A[(A>A_min)].size == 0:
        return 0
    F_mean = np.mean(F[(A>A_min)])
    return F_mean

# Creates a list of mean filamentarity values corresponding to a range of threshold values
# specified in threshold_list argument
def mean_fil_list(img, threshold_list, A_min):
    fil_list = np.zeros(threshold_list.size)
    for i in range(threshold_list.size):
        fil_list[i] = filamentarity(img, threshold_list[i], A_min)
    return fil_list


