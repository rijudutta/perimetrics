# perimetrics: accurate measurement of each connected-component contour
The function of this code is to:
- Read a grayscale image (as a 2D array) and the threshold at which the image is to be contoured
- Contour the image vertex-by-vertex and distribute the area, perimeter values found at that vertex to the above-threshold cells surrounding that vertex, in a single pass through the image
- Perform connected-component labeling to assign a unique integer (1 to N) to the cells of each connected component
- In another single pass through the image, store the total area, perimeter values of the cells of the m-th connected component into the (m+1)-th element of a list, for 1 <= m <= N
- Return the list containing area and perimeter values for each connected component

For connected-component labeling, the package <tt>connected-components-3d</tt> is used.
For contouring, the algorithm used is marching squares with linear interpolation of values between cell centers, based on:
*Utilizing Minkowski functionals for image analysis: a marching square algorithm*, Hubert Mantz *et al J. Stat. Mech.* (2008) P12015, DOI: 10.1088/1742-5468/2008/12/P12015
